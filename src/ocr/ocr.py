import os
import pytesseract
from pdf2image import convert_from_path
from PIL import Image


def extract_text_from_pdf(pdf_path):
    """Run OCR on a scanned PDF and return combined text."""
    pages = convert_from_path(pdf_path)
    all_text = ""

    for page in pages:
        text = pytesseract.image_to_string(page, lang="eng+hin")
        all_text += text + "\n\n"

    return all_text


def extract_text_from_image(image_path):
    """OCR for a single image file."""
    img = Image.open(image_path)
    return pytesseract.image_to_string(img, lang="eng+hin")


def save_text_as_txt(text, output_path):
    """Save OCR text into a UTF-8 TXT file."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


def ocr_to_txt(input_path, output_folder="data/processed"):
    """Main helper: extract text and save as TXT."""
    os.makedirs(output_folder, exist_ok=True)

    filename = os.path.splitext(os.path.basename(input_path))[0]
    output_txt = os.path.join(output_folder, f"{filename}-ocred.txt")

    ext = input_path.lower().split(".")[-1]

    # PDF case
    if ext == "pdf":
        text = extract_text_from_pdf(input_path)

    # Image case
    elif ext in ["png", "jpg", "jpeg"]:
        text = extract_text_from_image(input_path)

    else:
        raise ValueError("Unsupported file type for OCR → TXT")

    save_text_as_txt(text, output_txt)

    print(f"[SUCCESS] Saved OCR text → {output_txt}")
    return output_txt

