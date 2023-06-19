from django.shortcuts import render
from toCSV.script import extract_kv_pairs, extract_kv_pairs_pdf, extract_kv_pairs_img
from .forms import UploadForm
from .models import UploadPdf
from converter.settings import BASE_DIR
import os
# Create your views here.

def extract_data_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['uploaded_file']
            pdf_new = UploadPdf.objects.create(pdf_file = uploaded_file)
            pdf_new.save()

            #pdf_obj = UploadPdf.objects.get(pdf_file=uploaded_file.name)
            pdf_file = pdf_new.pdf_file

            if uploaded_file.name.lower().endswith('.pdf'):
                file_path_str = pdf_file.url[1:]
                file_path = os.path.join(BASE_DIR, file_path_str)
                
                extracted_data = extract_kv_pairs_pdf(file_path)
            else:
                extracted_data = extract_kv_pairs_img(pdf_file)

            return render(request, 'result.html', {
                'extracted_data': extracted_data
            })
        else:
            form = UploadForm()
        
        return render(request, 'result.html') 
    
def upload(request):
    return render(request, 'upload.html')