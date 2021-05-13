import cv2
import matplotlib.pyplot as plt
import numpy as np

def handle_uploaded_file(f):
    with open('static_my_project/input.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def image_processor(selected_option):
    img1 = cv2.imread('static_my_project/input.jpg')
    if selected_option == "1":
        img2 = binarize(img1)
    elif selected_option == "2":
        img2 = invert(img1)
    elif selected_option == "3":
        img2 = hist_eq(img1)
    else:
        return False
    cv2.imwrite('static_my_project/output.jpg', img2)
    return True


def binarize(img):
    print("hi2", type(img))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bin_img = np.where(img>130, 1, 0)
    return bin_img

def invert(img):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	inv_img = (255-img)
	return inv_img

def hist_eq(img):
    data = img.copy().flatten()
    hist, bins = np.histogram(data, 256, density=True)
    cdf = hist.cumsum()
    cdf = 255*cdf/cdf[-1]
    img_eq = np.interp(data, bins[:-1], cdf)
    return img_eq.reshape(img.shape)

