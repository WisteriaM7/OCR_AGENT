#!/usr/bin/env python
# src/ocr_ollama/main.py

from ocr_ollama.crew import InvoiceExtractionCrew
from ocr_ollama.tools.custom_tool import extract_text_from_image

def run():
    """
    Run the invoice extraction crew.
    """
    image_path = "bill.jpg"

    # OCR the image
    ocr_text = extract_text_from_image(image_path)

    # Initialize the crew and inject the dynamic input
    crew = InvoiceExtractionCrew()
    crew.ocr_text = ocr_text  # Set OCR text directly

    # Kick off the crew with optional input dict if needed
    inputs = {}  # You can pass named input keys here if any task uses placeholders

    crew.crew().kickoff(inputs=inputs)

