import os
import json
import re
import pdfplumber
from datetime import datetime

def extract_amount_from_pdf(first_page_text):
    """Finds the total amount owed."""
    keywords = ["Total Amount Due", "Amount Due", "Total New Charges", "Balance Due", "Please Pay", "Total Payable"]
    lines = first_page_text.split('\n')
    for line in lines:
        if any(key.lower() in line.lower() for key in keywords):
            match = re.search(r"(\$?\d{1,4}(?:[.,]\d{3})*[.,]\d{2})", line)
            if match:
                return match.group(1)
    all_amounts = re.findall(r"\$\d+\.\d{2}", first_page_text)
    return all_amounts[0] if all_amounts else "---"

def extract_period_from_pdf(first_page_text, util_type):
    """Extracts billing period based on utility type patterns."""
    if not first_page_text:
        return "---"
    
    if util_type == 'electricity':
        # Pattern for: E-OAK137900 03/04/2024 04/03/2024
        match = re.search(r"\d{2}/\d{2}/\d{4}\s+\d{2}/\d{2}/\d{4}", first_page_text)
        if match:
            return match.group(0).replace(" ", " to ")
            
    elif util_type == 'gas':
        # Pattern for: Billing Period Jan 24, 2024 - Feb 21, 2024
        # Matches Month Date, Year - Month Date, Year
        match = re.search(r"[A-Z][a-z]{2}\s\d{1,2},\s\d{4}\s-\s[A-Z][a-z]{2}\s\d{1,2},\s\d{4}", first_page_text)
        if match:
            return match.group(0)

    return "---"

def generate_miller_data():
    image_folders = {'main': 'main_floor', 'basement': 'basement', 'common': 'common'}
    utility_folders = ['electricity', 'gas']
    data = {}

    # 1. Process Images
    for web_key, folder_name in image_folders.items():
        path = os.path.join("images", folder_name)
        if os.path.exists(path):
            files = sorted([f for f in os.listdir(path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))])
            data[web_key] = {"images": [f"images/{folder_name}/{f}" for f in files]}
        else:
            data[web_key] = {"images": []}

    # 2. Process Utility PDFs
    data['utility_bills'] = {}
    for util in utility_folders:
        path = os.path.join("utilities", util)
        if os.path.exists(path):
            pdfs = sorted([f for f in os.listdir(path) if f.lower().endswith('.pdf')], reverse=True)
            bill_entries = []
            for f in pdfs:
                full_path = os.path.join(path, f)
                try:
                    with pdfplumber.open(full_path) as pdf:
                        page_text = pdf.pages[0].extract_text() or ""
                        amt = extract_amount_from_pdf(page_text)
                        period = extract_period_from_pdf(page_text, util)
                        
                        bill_entries.append({
                            "name": f, 
                            "url": f"utilities/{util}/{f}",
                            "amount": amt,
                            "period": period
                        })
                except Exception as e:
                    print(f"Error reading {f}: {e}")
            
            data['utility_bills'][util] = bill_entries
    
    data['last_updated'] = datetime.now().strftime("%B %d, %Y")
    with open('miller_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("\nSuccess: miller_data.json updated with amounts and periods!")

if __name__ == "__main__":
    generate_miller_data()