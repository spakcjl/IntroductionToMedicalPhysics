import fitz  # pymupdf
import pathlib
import traceback

def pdf_to_clean_text(pdf_path):
    try:
        doc = fitz.open(pdf_path)
    except Exception:
        print(f"Could not open {pdf_path}. Make sure the file exists in this folder.")
        return None

    text_content = []
    
    print(f"Processing {len(doc)} pages...")
    
    for i, page in enumerate(doc):
        # "text" extracts plain text.
        # sort=True forces reading order (top-left to bottom-right), fixing the column issue.
        text = page.get_text("text", sort=True)
        
        # Add a page marker so the AI knows where page breaks are
        text_content.append(f"--- PAGE {i+1} ---")
        text_content.append(text)
        
    return "\n\n".join(text_content)

if __name__ == "__main__":
    pdf_file = "chapter1SandS.pdf"
    output_file = "chapter1.md"
    
    try:
        clean_text = pdf_to_clean_text(pdf_file)
        if clean_text:
            pathlib.Path(output_file).write_text(clean_text, encoding="utf-8")
            print(f"Success! Saved clean text to: {output_file}")
            print("You can now run 'jules @prompt_slides.txt'")
    except Exception:
        traceback.print_exc()