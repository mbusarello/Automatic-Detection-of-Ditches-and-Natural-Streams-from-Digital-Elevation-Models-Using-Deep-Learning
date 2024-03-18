# -*- coding: utf-8 -*-
"""
@author: Mariana Busarello, 2024
"""

import os
import numpy as np
import rasterio as rio
import argparse

def making_ditches(input_path,output_path):
    for chip in os.listdir(input_path):
        if chip.endswith('.tif'):
            print(chip)
            filepath = input_path+chip
            output_file = output_path+chip

            ff = rio.open(filepath)
            ffD = ff.read(1)
            ffD = ffD.astype(np.uint8)
        
            file_s = np.where(ffD < 2, ffD, 0)
            print('crs: ',ff.crs)
            file_save = rio.open(
                            output_file,
                           'w',
                           driver='GTiff',
                           height=ffD.shape[0],
                           width=ffD.shape[1],
                           count=1,
                           dtype=ffD.dtype,
                           crs=ff.crs,
                           transform = rio.Affine(
                               ff.profile['transform'][0],ff.profile['transform'][1],
                               ff.profile['transform'][2],ff.profile['transform'][3],
                               ff.profile['transform'][4],ff.profile['transform'][5])
                           )
        
            file_save.write(file_s,1)
            file_save.close()
        

if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='turns the dataset Ditches&Streams into dataset Ditches by removing the streams from it',
                                     add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('input_path', help='path to the folder containing the labeled chips from Ditches&Streams')
    parser.add_argument('output_path', help='destination path to dataset Ditches')
    args = vars(parser.parse_args())
    making_ditches(**args)