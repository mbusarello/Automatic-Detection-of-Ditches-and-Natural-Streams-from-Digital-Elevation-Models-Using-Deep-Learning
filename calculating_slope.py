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


def sloping(input_path,output_path):
    temp_output=os.path.join(output_path,'temp')
    try:
        os.makedirs(temp_output)
    except Exception as e:
        print(e)
        print('error when creating destination directory')
        
    for dem in os.listdir(input_path):
        if dem.endswith('.tif'):     
            print(dem)
    
            wbt.slope(
                        os.path.join(input_path,dem),
                        os.path.join(temp_output,dem),
                        zfactor=None,
                        units='degrees'
                      )
            
            print('normalizing slope....')
            
            Slope = rio.open(os.path.join(temp_output,dem))
            slope_norm = ((Slope.read(1)/90)).astype(np.float32)
                   
            output_norm = os.path.join(output_path,dem)
            
            sl = rio.open(
                                output_norm,
                               'w',
                               driver='GTiff',
                               height=slope_norm.shape[0],
                               width=slope_norm.shape[1],
                               count=1,
                               dtype=slope_norm.dtype,
                               crs=Slope.crs,
                               transform = rio.Affine(
                                   Slope.profile['transform'][0],Slope.profile['transform'][1],
                                   Slope.profile['transform'][2],Slope.profile['transform'][3],
                                   Slope.profile['transform'][4],Slope.profile['transform'][5])
                               )
            sl.write(slope_norm,1)
            sl.close()
            Slope.close()
            os.remove(os.path.join(temp_output,dem))
    os.rmdir(temp_output)

if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='creates the normalized slope rasters',
                                     add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('input_path', help='path to DEM tiles')
    parser.add_argument('output_path', help='destination path to the output normalized slope rasters')
    args = vars(parser.parse_args())
    sloping(**args)