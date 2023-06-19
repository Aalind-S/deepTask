from django import forms

class UploadForm(forms.Form):
    uploaded_file = forms.FileField(label='Select a PDF file')

"""            pdf_new = UploadPdf.objects.create(pdf_file = uploaded_file)
            pdf_new.save()
            
            pdf_obj = UploadPdf.objects.filter(pdf_file=uploaded_file.name)
            pdf_file = pdf_obj.uploaded_file
            """