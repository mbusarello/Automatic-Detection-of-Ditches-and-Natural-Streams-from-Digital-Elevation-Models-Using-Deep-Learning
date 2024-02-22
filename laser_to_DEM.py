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

def lasering(input_path,output_path):  
    
    for laz in os.listdir(input_path):
        if laz.endswith('laz'):
            wbt.lidar_tin_gridding(
                i=os.path.join(input_path,laz),
                output=output_path+laz.replace('laz','tif'), 
                parameter="elevation", 
                returns="all", 
                resolution=1.0, 
                exclude_cls="0,1,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18", 
                minz=None, 
                maxz=None
                                    )
            
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='buffers the streams and ditches rasters',
                                     add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('input_path',help='path to the laser data')
    parser.add_argument('output_path', help='destination path for the generated DEMs')
    args = vars(parser.parse_args())
    lasering(**args)