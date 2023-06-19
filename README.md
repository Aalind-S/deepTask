# deepTask
Deeplogic AI Task

This assignment was divided into two parts.
Part 1 being to write a script to perform data extraction from pdf or img files.
Part 2 being to develop a basic web application that utilises this script in order to perform data extraction.

# Approach
My approach to this problem involved researching on how to handle pdfs and images. I searched about various libraries but then ended up deciding on to using Tesseract OCR engine as well pdf2image library along with others.
My solution was to convert any pdf to image by using pdf2image and then scan it using pytesseract libray that would ultimately convert it into string form.
Afterwards I would parse the string and look for Key, Value pairs then add it to a hashmap/dictionary and then return the dictionary of pairs.

# Django Approach
To develop it in Django I made a model and a form to deal with FILES.
Whenever a file is uploaded, it is saved by the Django Backend.
Afterwards if the file is valid then it is processed by script which has been modified a little bit and then the solution is rendered on a new page.

# Set Up and Installation
Clone the repository 
```
git clone https://github.com/Aalind-S/deepTask
```

Tesseract should be installed

Set up and activate python virtual environment

install all the requirements
```
pip install -r requirements.txt
```
Run the following command

```
python manage.py runserver
```
