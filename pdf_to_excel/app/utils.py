import pdfplumber  # type: ignore
import pandas as pd

def process_pdf_to_excel(file_path):
    extracted_data = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                extracted_data.extend(table)

    df = pd.DataFrame(extracted_data)
    excel_path = file_path.replace('.pdf', '.xlsx')
    df.to_excel(excel_path, index=False, header=False)

    return excel_path
