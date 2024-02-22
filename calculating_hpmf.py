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

def hpmf(input_path,output_path):
    output=os.path.join(output_path,'unnormalized')
    try:
        os.makedirs(output)
    except Exception as e:
        print(e)
        print('error when creating destination directory') 
        
    for dem in sorted(os.listdir(input_path)):
        if dem.endswith('.tif'):     
            print(dem)
            
            wbt.high_pass_median_filter(
                                        os.path.join(input_path,dem),
                                        os.path.join(output,dem),
                                        filterx=11,
                                        filtery=11,
                                        sig_digits=2
                                        )
            
            print('normalizing HPMF....')
            HPMF = rio.open(os.path.join(output,dem))
            HPMF_r = HPMF.read(1)
            hpmf_norm = (HPMF_r--6) / (8--6)
            final_output = output_path
           
            
            output_norm = os.path.join(final_output,dem)
            
            hpmf_s = rio.open(
                                output_norm,
                               'w',
                               driver='GTiff',
                               height=hpmf_norm.shape[0],
                               width=hpmf_norm.shape[1],
                               count=1,
                               dtype=hpmf_norm.dtype,
                               crs=HPMF.crs,
                               transform = rio.Affine(
                                   HPMF.profile['transform'][0],HPMF.profile['transform'][1],
                                   HPMF.profile['transform'][2],HPMF.profile['transform'][3],
                                   HPMF.profile['transform'][4],HPMF.profile['transform'][5])
                               )
            hpmf_s.write(hpmf_norm.astype(np.float32),1)
            hpmf_s.close()
            HPMF.close()

            
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='creates the normalized and unnormalized High-Pass Median Filter rasters',
                                         add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('input_path', help='path to DEMs')
    parser.add_argument('output_path', help='destination path to the High-Pass Median Filter')
    args = vars(parser.parse_args())
    hpmf(**args) 