import fitz
import os

pdf_name = "HST.583_2024__MR_Physics_1__Wald__slides.pdf"
img_dir = "extracted_images"

if not os.path.exists(img_dir):
    os.makedirs(img_dir)

if os.path.exists(pdf_name):
    print(f"Processing {pdf_name}...")
    doc = fitz.open(pdf_name)
    for i in range(len(doc)):
        page = doc.load_page(i)
        pix = page.get_pixmap(dpi=150)
        output = os.path.join(img_dir, f"slide_{i+1}.png")
        pix.save(output)
    print("Done.")
else:
    print(f"Error: {pdf_name} not found.")
