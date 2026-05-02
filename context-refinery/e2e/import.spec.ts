import { test, expect } from '@playwright/test';

test.describe('Import View', () => {
  test.beforeEach(async ({ page }) => {
    // Intercept the Obsidian import endpoint
    await page.route('**/import/obsidian', async (route) => {
      const mockDoc = {
        id: 'test-doc-id',
        title: 'Mock Obsidian File',
        source: {
          system: 'obsidian',
          type: 'md',
          original_file_name: 'test.md'
        },
        timestamps: {
          ingested_at: new Date().toISOString()
        },
        author: 'Test User',
        status: 'scratchpad',
        doc_type: 'note',
        tags: [],
        projects: [],
        content: {
          cleaned_markdown: 'This is a test file'
        },
        quality: {
          is_noisy: false,
          warnings: []
        }
      };

      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify(mockDoc)
      });
    });
  });

  test('should upload a markdown file and display it in the table', async ({ page }) => {
    // Navigate to the app (defaults to import view)
    await page.goto('/');

    // Clear local storage to start fresh
    await page.evaluate(() => {
      localStorage.clear();
    });
    await page.reload();

    // Ensure the empty state is visible
    await expect(page.getByText('No sources detected yet')).toBeVisible();
    await expect(page.getByText('No documents imported yet')).toBeVisible();

    // Trigger file upload
    const fileChooserPromise = page.waitForEvent('filechooser');
    await page.getByRole('button', { name: 'Browse Files' }).click();
    const fileChooser = await fileChooserPromise;

    // Create a dummy markdown file in memory and upload it
    await fileChooser.setFiles({
      name: 'test.md',
      mimeType: 'text/markdown',
      buffer: Buffer.from('# This is a test file'),
    });

    // Wait for the table to update
    await expect(page.getByText('No documents imported yet')).not.toBeVisible();

    // Verify the document appears in the table with correct data
    const row = page.locator('table tbody tr').first();
    await expect(row).toBeVisible();

    // Check Title
    await expect(row.getByRole('cell', { name: 'Mock Obsidian File' })).toBeVisible();

    // Check Source
    await expect(row.getByRole('cell', { name: 'obsidian', exact: true })).toBeVisible();

    // Check Status
    await expect(row.getByRole('cell', { name: 'scratchpad' })).toBeVisible();

    // Verify dynamic sources panel updated
    await expect(page.getByText('No sources detected yet')).not.toBeVisible();
    await expect(page.locator('.bg-white.rounded-2xl', { hasText: 'Obsidian Vault' })).toBeVisible();
    await expect(page.locator('.bg-white.rounded-2xl', { hasText: '1 Document' })).toBeVisible();

    // Verify it was persisted to localStorage
    const savedDocsStr = await page.evaluate(() => localStorage.getItem('cr_docs_default'));
    expect(savedDocsStr).toBeTruthy();

    const savedDocs = JSON.parse(savedDocsStr as string);
    expect(savedDocs.length).toBe(1);
    expect(savedDocs[0].title).toBe('Mock Obsidian File');
  });
});
