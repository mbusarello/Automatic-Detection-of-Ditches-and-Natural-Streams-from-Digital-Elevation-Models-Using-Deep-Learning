# -*- coding: utf-8 -*-
"""
@author: Mariana Busarello, 2024
"""

import os
import rasterio as rio
import numpy as np
import argparse
import time


try:
    import whitebox
    whitebox.download_wbt(linux_musl=True, reset=True)
    wbt = whitebox.WhiteboxTools()
except:
    from WBT.whitebox_tools import WhiteboxTools
    whitebox.download_wbt(linux_musl=True, reset=True)
    wbt = WhiteboxTools()

def hillshading(input_path,output_path,azi):
        try:
            os.makedirs(output_path)
        except Exception as e:
            print(e)
        temp_output=os.path.join(output_path,'temp')
        try:
            os.makedirs(temp_output)
        except Exception as e:
            print(e)
            print('error when creating temporary destination directory')  
        
        for dem in sorted(os.listdir(input_path)):         
            if dem.endswith('.tif'):     
                print(dem)
                wbt.hillshade(
                                    os.path.join(input_path,dem),
                                    os.path.join(temp_output,dem),
                                    azimuth=azi,
                                    altitude=30.0,
                                    zfactor=None
                                  )
                    
                print('normalizing hillshade....',dem)
                    
                hShade = rio.open(os.path.join(temp_output,dem))        
                hillshade_norm = ((hShade.read(1)/32767)).astype(np.float32)
                output_norm = os.path.join(output_path,dem)
                    
                hs = rio.open(
                                        output_norm,
                                       'w',
                                       driver='GTiff',
                                       height=hillshade_norm.shape[0],
                                       width=hillshade_norm.shape[1],
                                       count=1,
                                       dtype=hillshade_norm.dtype,
                                       crs=hShade.crs,
                                       transform = rio.Affine(
                                           hShade.profile['transform'][0],hShade.profile['transform'][1],
                                           hShade.profile['transform'][2],hShade.profile['transform'][3],
                                           hShade.profile['transform'][4],hShade.profile['transform'][5])
                                       )
                hs.write(hillshade_norm,1)
                hs.close()
                hShade.close()
                os.remove(os.path.join(temp_output,dem))
        os.rmdir(temp_output)
                
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='creates the normalized hillshade rasters',
                                     add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('input_path', help='path to DEM tiles')
    parser.add_argument('output_path', help='destination path to the normalized hillshade')
    parser.add_argument('azi', help='azimuth angle')
    args = vars(parser.parse_args())
    hillshading(**args)     