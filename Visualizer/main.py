from utils import *
import cv2 as cv
import numpy as np
from PIL import Image


def show_pic(p):
        img = cv.resize(p, (600,600))
        cv.imshow('Color image', img)
        while True:
            k = cv.waitKey(0) & 0xFF
            if k == 27: break 
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
    return output_return
            


def main():
    img = np.array(Image.open("3.png"))
    
    # Convolve using the specified kernel, then normalize the output to a range between 0-255
    conv = convolve(img, LEFT_VERTICAL_LINE_KERNEL)
    conv = conv + abs(np.min(conv))
    conv = conv / np.max(conv) * 255
    
    # Create colored picture (bgr values) from convolution -> small numbers red, large numbers green
    bgr_array = [ [ None for y in range( np.shape(conv)[0] ) ] for x in range( np.shape(conv)[1] ) ]
    for ir, row in enumerate(conv):
        for ic, col in enumerate(row):
            if conv[ir][ic] < 100:
                bgr_array[ir][ic] = [0,0,255]
            elif conv[ir][ic] > 200:
                bgr_array[ir][ic] = [0,255,0]
            else:
                bgr_array[ir][ic] = [0,0,0]
    show_pic(np.array(bgr_array).astype(np.uint8)) # Convert to uint8 to avoid errors


if __name__ == "__main__":
    main()