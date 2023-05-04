from utils import *

def main():
    img = np.array(Image.open("3.png"))
    
    # Convolve using the specified kernel, Output is an array with values between 0-255
    conv = convolve(img, TEST_KERNEL1) # See settings.py for available kernels
    
    # Show grayscaled convolution
    show_pic(np.array(conv).astype(np.uint8)) # Convert to uint8 to avoid errors
    
    # Show colored convolution (Red/Green/Black)
    show_pic(create_colored_array_from_grayscale(conv))


if __name__ == "__main__":
    main()