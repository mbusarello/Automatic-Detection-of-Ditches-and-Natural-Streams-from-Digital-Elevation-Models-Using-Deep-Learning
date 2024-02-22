#from https://github.com/FlorianWestphal/Dev-Ditch-Detection/tree/DevDitchNet-0.5-m-resolution
import os
import argparse
import whitebox
wbt = whitebox.WhiteboxTools()

def main(base_file_path, input_observations, output_label_path):
    
    for f in os.listdir(base_file_path):
        base = base_file_path + f
        label_tiles = output_label_path + f
        wbt.vector_lines_to_raster(
            i = input_observations, 
            output = label_tiles, 
            field="class", 
            nodata=False, 
            cell_size=None, 
            base=base
        )


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
                       description='Convert vector observaions to binary raster labels',
                       formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('base_file_path', help='Path to input files to use as basefile')
    parser.add_argument('input_observations', help = 'shapefile with observations to convert to labels')
    parser.add_argument('output_label_path', help = 'path to output labels')
    args = vars(parser.parse_args())
    main(**args)