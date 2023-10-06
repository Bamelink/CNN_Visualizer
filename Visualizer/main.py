from utils import *

OPTIONS = {
    "Left verticle line kernel": LEFT_VERTICAL_LINE_KERNEL,
    "Top horizontal line kernel": TOP_HORIZONTAL_LINE_KERNEL,
    "Edge detector kernel": EDGE_KERNEL
}

def main():
    img = np.array(Image.open("20231006-091411.png"))
    
    # Convolve using the specified kernel, Output is an array with values between 0-255
    conv = convolve(img, RIGHT_VERTICAL_LINE_KERNEL) # See settings.py for available kernels
    
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    axs[0, 0].set_title("Original")
    
    for i, option in enumerate(OPTIONS):
        conv = convolve(img, OPTIONS[option])
        #conv = convolve(conv, OPTIONS[option])
        axs[(i**i) % (i+1), (i+1)%2].imshow(cv.cvtColor(create_colored_array_from_grayscale(conv), cv.COLOR_BGR2RGB))
        axs[(i**i) % (i+1), (i+1)%2].set_title(option)
    
    # Show grayscaled convolution
    #show_pic(np.array(conv).astype(np.uint8)) # Convert to uint8 to avoid errors
    
    # Show colored convolution (Red/Green/Black)
    #show_pic(create_colored_array_from_grayscale(conv))


if __name__ == "__main__":
    main()