# -*- coding: utf-8 -*-
"""
@author: Mariana Busarello, 2024
"""

import warnings
import os
import rasterio as rio
import numpy as np
import argparse
warnings.filterwarnings('ignore', category=rio.errors.NotGeoreferencedWarning)

def separating(input_path,output_path):
    for filename in os.listdir(input_path):
        if filename.endswith('.tif'):
            print('separating ' + filename + ' into ditches and streams')
            file = os.path.join(input_path,filename)
            
            raster = rio.open(file)
                
            rasterD = raster.read(1) #rasterD is now an array
            rasterD = rasterD.astype(np.uint8) #rasterD is now uint8
                
            sep = {0:[rasterD < 2, 'streams_'],1:[rasterD > 1, 'ditches_']}
                
            for n in sep:
                selection = np.where(sep[n][0], rasterD, 0)
                output_file = os.path.join(output_path,sep[n][1] + filename)
                
                file_dd = rio.open(
                                        output_file,
                                       'w',
                                       driver='GTiff',
                                       height=rasterD.shape[0],
                                       width=rasterD.shape[1],
                                       count=1,
                                       dtype=rasterD.dtype,
                                       crs=raster.crs,
                                       transform = rio.Affine(
                                           raster.profile['transform'][0],raster.profile['transform'][1],
                                           raster.profile['transform'][2],raster.profile['transform'][3],
                                           raster.profile['transform'][4],raster.profile['transform'][5])
                                       )
                    
                file_dd.write(selection,1)
                file_dd.close()
        
        
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='Separates streams and ditches from the channels raster',
                                     add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('input_path',help='path to the raster classified between 0, 1 and/or 2')
    parser.add_argument('output_path', help='destination path for the one raster containing the ditches and one with streams')
    args = vars(parser.parse_args())
    separating(**args)