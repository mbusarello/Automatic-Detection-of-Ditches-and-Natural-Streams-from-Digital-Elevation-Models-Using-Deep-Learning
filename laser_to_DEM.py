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

def lasering(input_path):  
    
    for laz in os.listdir(input_path):
        wbt.set_working_dir(input_path)
        wbt.lidar_tin_gridding(
            parameter="elevation", 
            returns="last", 
            resolution=0.5, 
            exclude_cls="0,1,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18",
            max_triangle_edge_length = 50,
            minz=None, 
            maxz=None
                                )
            
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='creates the Digital Elevation Models from the LiDAR data',
                                     add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('input_path',help='path to the laser data')
    args = vars(parser.parse_args())
    lasering(**args)