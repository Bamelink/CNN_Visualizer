import cv2 as cv
import numpy as np
from PIL import Image


def show_pic(p):
    img = cv.resize(p, (600,600))
    cv.imshow('image', img)
    while cv.getWindowProperty('image', cv.WND_PROP_VISIBLE) > 0:
        k = cv.waitKey(0) & 0xFF # "ESC" key
        if k == 27: 
            break 
    cv.destroyAllWindows()
        
        

def convolve(img,kernel):
    # Create return array the size of the img-kernel (Output gets smaller after convolution)
    output_return = d = [ [ None for y in range( np.shape(img)[0] - np.shape(kernel)[0] ) ] for x in range( np.shape(img)[1] - np.shape(kernel)[1] ) ]
    # Flip Kernel horizontally and vertically (see definition of convolution, otherwise it would be a correlation)
    kernel_flipped = np.flipud(np.fliplr(kernel))
    
    # Iterate through rows and cols
    for row in range(np.shape(img)[1] - np.shape(kernel)[1]):
        row_array = img[row : row + np.shape(kernel)[0]]
        for col in range(np.shape(img)[0] - np.shape(kernel)[0]):
            # Create a block which matches the size of the kernel
            X = row_array[:, col : col + np.shape(kernel)[1]]
            #Multiply elementwise and sum up the resulting matrix. Then append to the ouput array
            output_return[row][col] = np.sum(np.multiply(X, kernel))
    
    # Normalize array to values between 0-255
    output_return = output_return + abs(np.min(output_return))
    output_return = output_return / np.max(output_return) * 255
    return output_return


# Create colored picture (bgr values) from convolution -> small numbers red, large numbers green
def create_colored_array_from_grayscale(img):
    bgr_array = [ [ None for y in range( np.shape(img)[1] ) ] for x in range( np.shape(img)[0] ) ]
    
    for ir, row in enumerate(img):
        for ic, col in enumerate(row):
            if img[ir][ic] < 100:
                bgr_array[ir][ic] = [0,0,255]
            elif img[ir][ic] > 200:
                bgr_array[ir][ic] = [0,255,0]
            else:
                bgr_array[ir][ic] = [0,0,0]
                
    return np.array(bgr_array).astype(np.uint8)