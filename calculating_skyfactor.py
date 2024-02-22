# -*- coding: utf-8 -*-
"""
@author: Mariana Busarello, 2024
"""
import os
import rasterio as rio
from rvt import vis
import argparse

def skyfactoring(input_path,output_path):
    for dem in os.listdir(input_path):
        print(dem)
        if dem.endswith('.tif'):
            raster = rio.open(os.path.join(input_path,dem))
            DEM = raster.read(1)      
            dict_svf = vis.sky_view_factor(
                                                DEM, 
                                                resolution=1, 
                                                compute_svf=True,
                                                compute_opns=False,
                                                compute_asvf=False,
                                                svf_n_dir=16,
                                                svf_r_max=10,
                                                svf_noise=0
                                                )
            SVF = dict_svf['svf']
            output_file=os.path.join(output_path,dem)
            skyv_s = rio.open(
                                output_file,
                               'w',
                               driver='GTiff',
                               height=raster.shape[0],
                               width=raster.shape[1],
                               count=1,
                               dtype=DEM.dtype,
                               crs=raster.crs,
                               transform = rio.Affine(
                                   raster.profile['transform'][0],raster.profile['transform'][1],
                                   raster.profile['transform'][2],raster.profile['transform'][3],
                                   raster.profile['transform'][4],raster.profile['transform'][5])
                               )
            skyv_s.write(SVF,1)
            skyv_s.close()
            

if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='creates the sky view factor raster',
                                         add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('input_path', help='path to DEM tiles')
    parser.add_argument('output_path', help='destination path to the output')
    args = vars(parser.parse_args())
    skyfactoring(**args)