import cv2

def handle_uploaded_file(f):
    with open('static_my_project/input.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    image_processor()



def image_processor():
    grayscale_img = cv2.imread('static_my_project/input.jpg', 0)
    cv2.imwrite('static_my_project/output.jpg', grayscale_img)