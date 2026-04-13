import re

body = "Hello world\n\n## Related\n- [[old_file]]\n\n## Next Section\nMore text."
related_filenames = ["file1", "file2"]
links = "\n".join(f"- [[{fn}]]" for fn in related_filenames)
section = f"\n## Related\n{links}"

pattern = r"\n## Related\b.*?(?=\n## |\Z)"
new_body = re.sub(pattern, section, body, flags=re.DOTALL)
print(repr(new_body))

expected = "Hello world\n\n## Related\n- [[file1]]\n- [[file2]]\n\n## Next Section\nMore text."
print(repr(expected))
