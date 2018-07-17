# GE_OCR
## Installation
- Install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki#tesseract-at-ub-mannheim)
- Configure Tesseract OCR
   - Add Tesseract folder to `PATH`
   - Create system variable `TESSDATA_PREFIX` pointing to `/Tesseract-OCR/tessdata`
   - Copy the **GE** config file to `/Tesseract-OCR/tessdata/configs`
- Install Python (3.6) libraries
   ```
   pip install psd-tools
   pip install Pillow
   pip install pytesseract
   ```
