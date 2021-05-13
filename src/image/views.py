from os import name
from django.shortcuts import render
from .forms import UploadImageForm
# Create your views here.

from .utils import *

# def home_view(request):
#     return render(request, 'home_page.html', {})

class Option:
    def __init__(self, name, id):
        self.name = name
        self.id = id

def upload_image_view(request):
    message = ''
    valid = False
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        print("hello")
        if form.is_valid():
            print("hi")
            print(type(request.FILES['file']))
            handle_uploaded_file(request.FILES['file'])
            message = "Successfully Uploaded!!"
            valid = True
        else:
            message = 'Invalid File Upload!!'
        options = []
        options.append(Option('Convert to Binary(binarize)', 1))
        options.append(Option('Invert', 2))
        context = {
            "options": options,
            "message": message,
            "valid": valid
        }                                                                     
        return render(request, 'process_select_page.html', context)
        # return render(request, 'result_page.html', {'message':message, 'valid':valid})
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})


def process_select_view(request):
    if request.method == "POST":
        selected_option = request.POST['selected_option']
        print(selected_option, type(selected_option))
    else:
        print("loda")
