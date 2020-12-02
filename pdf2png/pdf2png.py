# -*- coding: utf-8 -*-
# Author: Héctor Salas

import os
import glob
import readline
from pdf2image import convert_from_path

readline.parse_and_bind('tab: complete')
readline.set_completer_delims(' \t\n')

help_text = '''Converts .pdf images  to .png
            use -i for specific files, and -d for all files inside a directry'''
sign_off = 'Author: Hector Salas <hector.salas.o@gmail.com>'

parser = argparse.ArgumentParser(description=help_text, epilog=sign_off)

parser.add_argument('-i', '--image', type=str, default=None, dest='images', help='Name(s) of image(s) to be converted. If more than one, names should be separated with " " eg: "filea fileb". For a list of images in a text file (one image per line) add "@" before the filename eg: "@list.txt"', action='store')
parser.add_argument('-d', '--directory', type=str, default=None, dest='folder', help='Name of directory with pdf images. All .pdf images inside the directory are converted to png', action='store')

arguments = parser.parse_args()
images = arguments.images
folder = arguments.folder

def conv(image_list):
    """convert a PDF image to png.
    """
    for image in image_list:
        aux = convert_from_path('image')
        name = image[:-4]+'.png'
        check_file(name)
        aux.save(name, 'PNG')
        print('{} converted to {}'.format(image, name))

def check_parser():
    """Checks that the parser inputs.
    """
    if (images == None) and (folder == None):
        aux = True
    elif (images != None) and (folder == None):
        raise ValueError('''-i and -d annot be use togheter''')
    else:
        aux = False
    return aux

def check_inputs(images):
    """Check the content of the Inputs.

    """
    if images[0] == '@':
        pass
    elif ' ' in  images:
        image_list = images.split(' ')
    else:
        image_list = []
        image_list.append(images)

    if folder is not None:
        image_list = [i for i in os.listdir(folder) if i[-4:]=='.pdf']
        if len(image_list) == 0:
            raise FileNotFoundError("No '.pdf' files in directory')

    return image_list

def check_file(filename):
    """ Checks if filename already exists and wheter or not to overwirte
    """
    aux = glob.os.path.isfile(filename)
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    while aux:
        print(f'File {name} already exists.')
        # loop to force user to enter only yes or no options
        while True:
            ow = input('Overwrite file (yes/no)? ')
            ow.lower()
            try:
                aux = valid[ow]
                break
            except ValueError:
                pass
        if not aux:
            name = input('Enter new name to save the image: ')
            # check if new name chosen already exists
            aux = glob.os.path.isfile(name)
        else:
            aux = False

def main():
    interactive = check_parser()
    if interactive:
        image_name = input('Please enter image name(s): ')
        image_list = check_inputs(image_name)
    conv(image_lidst)


if __name__ == '__main__':
    main()
