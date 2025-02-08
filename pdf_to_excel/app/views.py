from django.shortcuts import render
from .forms import UploadForm
from .utils import process_pdf_to_excel
import pandas as pd
import os

def home(request):
    return render(request, 'base.html')

def upload_doc(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_instance = form.save()  # Save the uploaded file

            # Convert PDF to Excel
            excel_path = process_pdf_to_excel(pdf_instance.doc.path)

            # Save the generated Excel file path in the model
            pdf_instance.excel_file.name = f"excels/{os.path.basename(excel_path)}"
            pdf_instance.save()

            # Read the Excel file content and convert it into an HTML table
            df = pd.read_excel(excel_path)
            excel_data = df.to_html(index=False)

            return render(request, 'success.html', {
                'doc': pdf_instance, 
                'excel_data': excel_data
            })

    else:
        form = UploadForm()
    
    return render(request, "upload.html", {'form': form})
