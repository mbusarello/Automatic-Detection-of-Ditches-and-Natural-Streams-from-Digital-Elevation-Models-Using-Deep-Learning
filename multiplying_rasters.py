# -*- coding: utf-8 -*-
"""
@author: Mariana Busarello, 2024
"""
import os
import argparse
import whitebox
try:
    import whitebox
    whitebox.download_wbt(linux_musl=True, reset=True)
    wbt = whitebox.WhiteboxTools()
except:
    from WBT.whitebox_tools import WhiteboxTools
    whitebox.download_wbt(linux_musl=True, reset=True)
    wbt = WhiteboxTools()


def multiplying(buffered_path,reclass_path,output_path):        
    for reclass_file in os.listdir(reclass_path):
        print(reclass_file)
        reclass_raster = os.path.join(reclass_path,reclass_file)
        for buffer_file in os.listdir(buffered_path):
            print(buffer_file)
            if buffer_file.endswith(reclass_file):
                input2 = os.path.join(buffered_path,buffer_file) 
                wbt.multiply(
                            input2, 
                            reclass_raster, 
                            output=os.path.join(output_path,buffer_file)
                            )
            else:
                print('files do not match, trying the next one')
                
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='multiplies the reclassified raster by the buffered raster separated between ditches and streams',
                                     add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('buffered_path',help='path to the buffered rasters separated between ditches and streams')
    parser.add_argument('reclass_path', help='path to the reclassified rasters')
    parser.add_argument('output_path', help='path to the destination of the multiplied files')
    args = vars(parser.parse_args())
    multiplying(**args)
