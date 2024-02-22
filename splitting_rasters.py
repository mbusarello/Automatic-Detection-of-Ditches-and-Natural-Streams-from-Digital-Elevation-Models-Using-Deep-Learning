# -*- coding: utf-8 -*-
"""
@author: Mariana Busarello, 2024
"""


import os
from splitraster import geo
import argparse


def splitting_raster(input_path, output_path):
    
    tile_size = 500
    
    for raster in sorted(os.listdir(input_path)):
        if raster.endswith('.tif'):
            chip_label = os.path.join(input_path,raster)
            try:
                geo.split_image(chip_label, os.path.join(output_path,raster.split('.')[0]), int(tile_size), 0, overwrite=False)
            except Exception as e:
                print('error when splitting the image '+ raster)
                print(e)
                
    print('moving chips to main folder...')
    
    for raster in os.listdir(output_path):
        print('moving chips from',raster)
        for chip in sorted(os.listdir(os.path.join(output_path,raster))):
            if chip.endswith('.tif'):
                print(chip)
                os.rename(os.path.join(output_path,raster,chip),os.path.join(output_path,raster,'_',chip))
        os.rmdir(os.path.join(output_path,raster))
    
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='splits the raster tiles into 500 px chips',
                                         add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('input_path', help='folder with the rasters to be splitted')
    parser.add_argument('output_path', help='chips destination folder')
    args = vars(parser.parse_args())
    splitting_raster(**args)