# -*- coding: utf-8 -*-
"""
@author: Mariana Busarello, 2024
"""


import os
import argparse
try:
    import whitebox
    whitebox.download_wbt(linux_musl=True, reset=True)
    wbt = whitebox.WhiteboxTools()
except:
    from WBT.whitebox_tools import WhiteboxTools
    whitebox.download_wbt(linux_musl=True, reset=True)
    wbt = WhiteboxTools()

def reclassifying(hpmf_path,output_path):

    for file in os.listdir(hpmf_path):
        if file.endswith('.tif'):
            input_dem = os.path.join(hpmf_path,file)
            output_dem = os.path.join(output_path,file)

            print(input_dem,'input2')
                       
            wbt.less_than(input1=input_dem,
                          input2='-0.075',
                          output=output_dem)
            
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='Selects the High-Pass Median Filter values below the threshold',
                                     add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('hpmf_path',help='path to the unnormalized High-Pass Median Filter rasters')
    parser.add_argument('output_path', help='destination path of the raster with the pixels that satisfy the condition')
    args = vars(parser.parse_args())
    reclassifying(**args)