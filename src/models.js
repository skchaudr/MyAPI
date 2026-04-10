class CanonicalDoc {
    constructor({
        id,
        title,
        content,
        provenance,
        timestamps,
        status,
        tags,
        projects,
        doc_type,
        quality_warnings
    }) {
        this.id = id;
        this.title = title;
        this.content = content;
        this.provenance = provenance || {};
        this.timestamps = timestamps || {};
        this.status = status || 'draft';
        this.tags = tags || [];
        this.projects = projects || [];
        this.doc_type = doc_type || 'document';
        this.quality_warnings = quality_warnings || [];
    }
}

module.exports = { CanonicalDoc };
