from django.shortcuts import render
from .forms import UploadImageForm
# Create your views here.

from utils.file_handler import handle_uploaded_file

# def home_view(request):
#     return render(request, 'home_page.html', {})



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
        return render(request, 'result_page.html', {'message':message, 'valid':valid})
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})
