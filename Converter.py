# We need to grab two arguments - one for current folder of images, and one for new folder for converted images
# We also need to grab the image files

import sys
import os
import os.path
from PIL import Image

# grab first and second argument

image_folder = sys.argv[1] + "/"
output_folder = sys.argv[2]
# check if new/ exists, and if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through the current file and convert jpg files into png files. Save these files in new folder
for filename in os.listdir(image_folder):
    clean_name = os.path.splitext(filename)[0]
    image = Image.open(f'{image_folder}{filename}')
    image.save(f"{output_folder}/{clean_name}.png", 'png')

print("Finished Conversion")

# Expand on this idea to create an image conversion app with conversion type choices