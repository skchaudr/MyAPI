import os
import argparse
from typing import Optional
from google.cloud import documentai
from google.cloud.documentai_toolbox import document

# Hardcoded for the sb-genai-2026 project, but can be parameterized
PROJECT_ID = "240906076368"
LOCATION = "us"
PROCESSOR_ID = "6e8cfb681fa4264f"

def extract_pdf_to_markdown(file_path: str, output_path: str):
    """
    Runs a PDF through Google Cloud Document AI (OCR) and converts the extracted
    document layout and text into Markdown using the Document AI Toolbox.
    """
    print(f"Processing {file_path} with Document AI...")
    
    opts = {"api_endpoint": f"{LOCATION}-documentai.googleapis.com"}
    client = documentai.DocumentProcessorServiceClient(client_options=opts)
    
    name = client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)
    
    with open(file_path, "rb") as image:
        image_content = image.read()
        
    raw_document = documentai.RawDocument(
        content=image_content, 
        mime_type="application/pdf"
    )
    
    request = documentai.ProcessRequest(
        name=name,
        raw_document=raw_document
    )
    
    # Process the document
    result = client.process_document(request=request)
    
    # Wrap in Toolbox Document for easy formatting (like Markdown)
    wrapped_document = document.Document.from_documentai_document(result.document)
    
    # Export to markdown
    # documentai-toolbox's export_to_markdown() returns a string of the document
    markdown_text = wrapped_document.text
    
    # Write to output file
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(markdown_text)
        
    print(f"✅ Successfully extracted markdown to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract PDF to Markdown via Document AI")
    parser.add_argument("input_pdf", help="Path to input PDF file")
    parser.add_argument("output_md", help="Path to output Markdown file")
    args = parser.parse_args()
    
    extract_pdf_to_markdown(args.input_pdf, args.output_md)
