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

def main(base_file_path, input_observations, output_label_path):
    
    for f in os.listdir(base_file_path):
        base = os.path.join(base_file_path,f)
        label_tiles = os.path.join(output_label_path,f)
        
        wbt.vector_lines_to_raster(        
            i = input_observations,
            output = label_tiles, 
            field="id", 
            nodata=False, 
            cell_size=None, 
            base=base
        )


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
                       description='Convert vector observaions to binary raster labels',
                       formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('base_file_path', help='path to input files to use as basefile')
    parser.add_argument('input_observations', help = 'shapefile with identified channels to convert to labels')
    parser.add_argument('output_label_path', help = 'path to output raster with channels')
    args = vars(parser.parse_args())
    main(**args)