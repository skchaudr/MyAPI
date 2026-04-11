import os
import json
import yaml
import pytest
import shutil
from context_refinery.models import CanonicalDoc
from context_refinery.exporter import KhojExporter

@pytest.fixture
def output_dir(tmpdir):
    out = str(tmpdir.mkdir("test_output"))
    yield out
    if os.path.exists(out):
        shutil.rmtree(out)

def test_get_safe_filename():
    exporter = KhojExporter()
    assert exporter.get_safe_filename('My Document Title!', 'id-1') == 'my-document-title.md'
    assert exporter.get_safe_filename(None, 'id-123') == 'id-123.md'
    assert exporter.get_safe_filename('A/B/C*D?E"F>G', 'id') == 'abcdefg.md'
    assert exporter.get_safe_filename('Title   With   Spaces', 'id') == 'title-with-spaces.md'

def test_export(output_dir):
    exporter = KhojExporter()

    doc1 = CanonicalDoc(
        id='doc-1',
        title='Hello World',
        content='# Heading 1\n\nContent here.',
        tags=['test', 'js'],
        provenance={'source': 'test'}
    )

    doc2 = CanonicalDoc(
        id='doc-2',
        title='Another Doc',
        content='Some more content.',
        status='final'
    )

    manifest = exporter.export([doc1, doc2], output_dir)

    assert os.path.exists(output_dir)

    manifest_path = os.path.join(output_dir, 'output_manifest.json')
    assert os.path.exists(manifest_path)

    with open(manifest_path, 'r', encoding='utf-8') as f:
        loaded_manifest = json.load(f)

    assert len(loaded_manifest['documents']) == 2
    assert 'exported_at' in loaded_manifest

    doc1_path = os.path.join(output_dir, 'hello-world.md')
    assert os.path.exists(doc1_path)

    doc2_path = os.path.join(output_dir, 'another-doc.md')
    assert os.path.exists(doc2_path)

    with open(doc1_path, 'r', encoding='utf-8') as f:
        doc1_content = f.read()

    assert doc1_content.startswith('---\n')

    parts = doc1_content.split('---\n')
    assert len(parts) >= 3

    frontmatter_raw = parts[1]
    markdown_body = '---\n'.join(parts[2:]).strip()

    parsed_frontmatter = yaml.safe_load(frontmatter_raw)
    assert parsed_frontmatter['id'] == 'doc-1'
    assert parsed_frontmatter['title'] == 'Hello World'
    assert parsed_frontmatter['tags'] == ['test', 'js']

    assert markdown_body == '# Heading 1\n\nContent here.'
