const fs = require('fs');
const path = require('path');
const yaml = require('yaml');

class KhojExporter {
    constructor() {}

    /**
     * Converts a string to a safe filesystem filename.
     */
    static getSafeFilename(title, id) {
        if (!title && !id) return 'document.md';

        let base = title || id;

        // Lowercase, replace spaces with hyphens, remove non-alphanumeric (except hyphens and underscores)
        base = base.toLowerCase()
            .replace(/\s+/g, '-')
            .replace(/[^a-z0-9-_]/g, '');

        // Default to ID if title becomes empty after sanitization
        if (base.length === 0) {
            base = id;
        }

        return `${base}.md`;
    }

    /**
     * Exports an array of CanonicalDoc objects to the specified output directory.
     * Generates markdown files with YAML frontmatter and an output_manifest.json.
     */
    async export(docs, outputDir) {
        if (!fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        const manifest = {
            exported_at: new Date().toISOString(),
            documents: []
        };

        for (const doc of docs) {
            const filename = KhojExporter.getSafeFilename(doc.title, doc.id);
            const docPath = path.join(outputDir, filename);

            const frontmatter = {
                id: doc.id,
                title: doc.title,
                provenance: doc.provenance,
                timestamps: doc.timestamps,
                status: doc.status,
                tags: doc.tags,
                projects: doc.projects,
                doc_type: doc.doc_type,
                quality_warnings: doc.quality_warnings
            };

            const yamlString = yaml.stringify(frontmatter);
            const markdownContent = `---\n${yamlString}---\n\n${doc.content || ''}`;

            fs.writeFileSync(docPath, markdownContent, 'utf-8');

            manifest.documents.push({
                id: doc.id,
                title: doc.title,
                filename: filename,
                path: docPath
            });
        }

        const manifestPath = path.join(outputDir, 'output_manifest.json');
        fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), 'utf-8');

        return manifest;
    }
}

module.exports = { KhojExporter };
