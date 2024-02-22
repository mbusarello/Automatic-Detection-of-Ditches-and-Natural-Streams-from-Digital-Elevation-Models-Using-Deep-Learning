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

def majority(multiply_path,output_path):
    for multiplied_raster in os.listdir(multiply_path):
        print(multiplied_raster)
        i = os.path.join(multiply_path,multiplied_raster)
        output = os.path.join(output_path,multiplied_raster)
        wbt.majority_filter(
                            i,
                            output,
                            filterx=3,
                            filtery=3
                            )
        
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='applies majority filter',
                                     add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('multiply_path',help='path to the multiplied rasters')
    parser.add_argument('output_path', help='path to the destination folder')
    args = vars(parser.parse_args())
    majority(**args)