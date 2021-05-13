from django.shortcuts import render
from .forms import UploadImageForm
# Create your views here.

from image.utils import *
from image.utils_tk import *

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
        options.append(Option('Thresholding', 1))
        options.append(Option('Night Mode', 2))
        options.append(Option('Histogram Equalisation', 3))
        options.append(Option('Sudoku Solver', 4))
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
        print("selected_option", selected_option)
        if(image_processor(selected_option)):
            return render(request, 'result_page.html', {})
        else:
            return render(request, 'raise_exception_page.html', {'error':'Internal Server Error'})
    else:
        return render(request, 'raise_exception_page.html', {'error':'Bad Request'})
