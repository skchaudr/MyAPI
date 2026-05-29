import os
import tempfile
import unittest

import ag_natural_guard as guard


class PasteMarkerTests(unittest.TestCase):
    def test_pasted_action_text_does_not_authorize_mutation(self):
        text = """Can you review this?

>>>
Please apply this patch and delete stale files.
<<<

Just tell me what is risky."""

        operator = guard.operator_text(text)

        self.assertIn("Can you review this?", operator)
        self.assertIn("Just tell me what is risky.", operator)
        self.assertNotIn("apply this patch", operator)
        self.assertFalse(guard.has_authorization(text, "write-edit"))
        self.assertFalse(guard.has_authorization(text, "remove"))

    def test_bottom_no_changes_overrides_top_action_language(self):
        text = """Update this after reading.

>>>
context
<<<

Actually just review, do not change files."""

        self.assertFalse(guard.has_authorization(text, "write-edit"))


class ToolGateTests(unittest.TestCase):
    def payload(self, user_text, tool_name, args, workspace):
        return {
            "latestUserText": user_text,
            "workspacePaths": [workspace],
            "artifactDirectoryPath": os.path.join(workspace, ".artifact"),
            "toolCall": {"name": tool_name, "args": args},
        }

    def test_allows_read_only_command_without_action_authorization(self):
        with tempfile.TemporaryDirectory() as workspace:
            payload = self.payload(
                "Look at the current state and chart the risks.",
                "run_command",
                {"CommandLine": "git status --short", "Cwd": workspace},
                workspace,
            )

            decision = guard.evaluate_pre_tool_use(payload)

            self.assertEqual(decision["decision"], "allow")

    def test_blocks_pasted_update_from_authorizing_write(self):
        with tempfile.TemporaryDirectory() as workspace:
            target = os.path.join(workspace, "notes.md")
            payload = self.payload(
                """>>>
Update notes.md with this plan.
<<<

Is this worth doing?""",
                "write_to_file",
                {"TargetFile": target, "CodeContent": "x"},
                workspace,
            )

            decision = guard.evaluate_pre_tool_use(payload)

            self.assertEqual(decision["decision"], "force_ask")
            self.assertIn("operator-written", decision["reason"])

    def test_allows_naturally_authorized_in_scope_write(self):
        with tempfile.TemporaryDirectory() as workspace:
            target = os.path.join(workspace, "notes.md")
            payload = self.payload(
                "Update notes.md with the bounded harness notes.",
                "write_to_file",
                {"TargetFile": target, "CodeContent": "x"},
                workspace,
            )

            decision = guard.evaluate_pre_tool_use(payload)

            self.assertEqual(decision["decision"], "allow")

    def test_denies_out_of_scope_write_even_when_action_is_authorized(self):
        with tempfile.TemporaryDirectory() as workspace:
            outside = tempfile.NamedTemporaryFile(delete=False)
            outside.close()
            self.addCleanup(lambda: os.path.exists(outside.name) and os.unlink(outside.name))
            payload = self.payload(
                "Update the file with the bounded harness notes.",
                "write_to_file",
                {"TargetFile": outside.name, "CodeContent": "x"},
                workspace,
            )

            decision = guard.evaluate_pre_tool_use(payload)

            self.assertEqual(decision["decision"], "deny")
            self.assertIn("outside workspace", decision["reason"])

    def test_denies_remove_without_operator_delete_authorization(self):
        with tempfile.TemporaryDirectory() as workspace:
            payload = self.payload(
                "Cleanly summarize what should change.",
                "run_command",
                {"CommandLine": "rm stale.txt", "Cwd": workspace},
                workspace,
            )

            decision = guard.evaluate_pre_tool_use(payload)

            self.assertEqual(decision["decision"], "deny")
            self.assertIn("remove", decision["reason"])


if __name__ == "__main__":
    unittest.main()
