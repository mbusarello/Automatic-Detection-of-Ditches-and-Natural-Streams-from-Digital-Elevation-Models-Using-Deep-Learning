# -*- coding: utf-8 -*-
"""
@author: Mariana Busarello, 2024
"""

import os
import rasterio as rio
import numpy as np
import argparse
try:
    import whitebox
    whitebox.download_wbt(linux_musl=True, reset=True)
    wbt = whitebox.WhiteboxTools()
except:
    from WBT.whitebox_tools import WhiteboxTools
    whitebox.download_wbt(linux_musl=True, reset=True)
    wbt = WhiteboxTools()


def buffering(input_path,output_path,size):
    
    input_files = os.listdir(input_path)    
    for file in input_files:
        if file.endswith('.tif'):
            i = os.path.join(input_path,file)
            print(i)
        
            wbt.buffer_raster(
                i,
                output=os.path.join(output_path,file),
                size=size,
                gridcells=False
                )

            
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='Buffers the channels in the raster. The buffer is applied in both sides of the rasterline, so plan the size accordingly',
                                     add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('input_path',help='path to the raster separated between streams and ditches')
    parser.add_argument('output_path', help='destination path for the buffered DEMs separated between streams and ditches')
    parser.add_argument('size', help='size of the buffer (m)')
    args = vars(parser.parse_args())
    buffering(**args)