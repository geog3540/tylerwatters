from PIL import Image

# Open the PNG image
image = Image.open("FinalWIP.png")

# Resize the image to new dimensions
new_size = (799, 572)  # Replace width and height with your desired dimensions
resized_image = image.resize(new_size)

# Save the modified image
resized_image.save("finalWIPresized.png")
