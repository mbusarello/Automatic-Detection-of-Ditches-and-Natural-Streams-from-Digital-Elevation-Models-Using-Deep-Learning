# -*- coding: utf-8 -*-
"""
@author: Mariana Busarello, 2024
"""

import os
import numpy as np
import rasterio as rio
import shutil
import argparse

def thresholding_chips(input_path,output_path,size):
    for chip in os.listdir(input_path):
        if chip.endswith('tif'):
            chip_o = rio.open(os.path.join(input_path+chip))
            c_chip = chip_o.read(1)
            count = np.sum(np.isnan(c_chip))
            if count > int(0):
                shutil.copyfile(os.path.join(input_path+chip),os.path.join(output_path+chip))
                print('moving file',chip)
            else:
                count2 = np.count_nonzero(c_chip)
                if count2 >= int(size):
                    print('moving file',chip)
                    shutil.copyfile(os.path.join(input_path+chip),os.path.join(output_path+chip))
            chip_o.close()
    
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='selects the chips that have more pixels than the threshold and copies them to a new folder',
                                     add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('input_path', help='path to the chips to be selected')
    parser.add_argument('output_path', help='destination path to the chips that satisfy the condition')
    parser.add_argument('size', help='the minimum number of labeled pixels that a chip must have')
    args = vars(parser.parse_args())
    thresholding_chips(**args)