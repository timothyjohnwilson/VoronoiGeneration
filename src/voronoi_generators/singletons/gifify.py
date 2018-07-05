import os
import random
import string
from os import listdir
import sys

sys.path.append("../../../")

import imageio
import base


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


base_path = base.get_path()
images_to_gif_path = base_path + '/sample_images/turn_into_gif/'
gif_path = base_path + '/sample_images/gif/'
gif_name = id_generator() + '.gif'

only_files_length = len(listdir(images_to_gif_path))
images = []

print("Compressing Images")
os.system("optipng " + images_to_gif_path + "*")

print("Adding files to data structure")
for i in range(0, only_files_length):
    images.append(imageio.imread(images_to_gif_path + str(i) + '.png'))
print("Added files to data structure\nConverting images to GIF")
imageio.mimsave(gif_path + gif_name, images)
print("Speeding up GIF")
os.system("convert -delay 1x60 " + gif_path + gif_name + " " + gif_path + gif_name)
print("GIF " + gif_path + gif_name + " complete")