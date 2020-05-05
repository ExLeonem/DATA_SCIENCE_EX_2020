
import os
from skimage import io


def read_img(name, resize = None, grey = False):
    base_path = os.path.join(os.getcwd(), "..", "datasets", "captures")
    img_path = os.path.join(base_path, name)
    img_data = io.imread(img_path, as_gray=grey)

    return img_data


# Scale image down (pixelwise)
def scale_to(img, down_to):
    y_scaling = int(img.shape[0]/down_to)
    x_scaling = int(img.shape[1]/down_to)

    return img[::y_scaling, ::x_scaling]