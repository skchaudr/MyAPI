const fs = require('fs');
const path = require('path');
const { CanonicalDoc } = require('../src/models');
const { KhojExporter } = require('../src/exporter');
const yaml = require('yaml');

describe('KhojExporter', () => {
    const outputDir = path.join(__dirname, 'test_output');
    let exporter;

    beforeEach(() => {
        exporter = new KhojExporter();
        if (fs.existsSync(outputDir)) {
            fs.rmSync(outputDir, { recursive: true, force: true });
        }
    });

    afterAll(() => {
        if (fs.existsSync(outputDir)) {
            fs.rmSync(outputDir, { recursive: true, force: true });
        }
    });

    describe('getSafeFilename', () => {
        it('should safely format typical titles', () => {
            expect(KhojExporter.getSafeFilename('My Document Title!', 'id-1')).toBe('my-document-title.md');
        });

        it('should use id if title is empty or null', () => {
            expect(KhojExporter.getSafeFilename(null, 'id-123')).toBe('id-123.md');
        });

        it('should handle weird characters', () => {
            expect(KhojExporter.getSafeFilename('A/B/C*D?E"F>G', 'id')).toBe('abcdefg.md');
        });

        it('should handle spaces and multiple spaces', () => {
            expect(KhojExporter.getSafeFilename('Title   With   Spaces', 'id')).toBe('title-with-spaces.md');
        });
    });

    describe('export', () => {
        it('should export documents correctly and generate manifest', async () => {
            const doc1 = new CanonicalDoc({
                id: 'doc-1',
                title: 'Hello World',
                content: '# Heading 1\n\nContent here.',
                tags: ['test', 'js'],
                provenance: { source: 'test' }
            });

            const doc2 = new CanonicalDoc({
                id: 'doc-2',
                title: 'Another Doc',
                content: 'Some more content.',
                status: 'final'
            });

            await exporter.export([doc1, doc2], outputDir);

            // Check if directory exists
            expect(fs.existsSync(outputDir)).toBe(true);

            // Check manifest
            const manifestPath = path.join(outputDir, 'output_manifest.json');
            expect(fs.existsSync(manifestPath)).toBe(true);
            const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));

            expect(manifest.documents.length).toBe(2);
            expect(manifest.exported_at).toBeDefined();

            // Check generated files
            const doc1Path = path.join(outputDir, 'hello-world.md');
            expect(fs.existsSync(doc1Path)).toBe(true);

            const doc2Path = path.join(outputDir, 'another-doc.md');
            expect(fs.existsSync(doc2Path)).toBe(true);

            // Check file content (YAML frontmatter + markdown)
            const doc1Content = fs.readFileSync(doc1Path, 'utf-8');
            expect(doc1Content.startsWith('---\n')).toBe(true);

            const parts = doc1Content.split('---\n');
            expect(parts.length).toBeGreaterThanOrEqual(3);

            const frontmatterRaw = parts[1];
            const markdownBody = parts.slice(2).join('---\n').trim();

            const parsedFrontmatter = yaml.parse(frontmatterRaw);
            expect(parsedFrontmatter.id).toBe('doc-1');
            expect(parsedFrontmatter.title).toBe('Hello World');
            expect(parsedFrontmatter.tags).toEqual(['test', 'js']);

            expect(markdownBody).toBe('# Heading 1\n\nContent here.');
        });
    });
});
