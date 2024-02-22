# -*- coding: utf-8 -*-
"""
@author: Mariana Busarello, 2024
"""

import os
import rasterio as rio
import numpy as np
import argparse

def combination(separated_path,majority_path,output_path):
    for split_stream in os.listdir(separated_path):
        if split_stream.endswith('.tif'):
            print(split_stream.replace('streams_',''))
            
            if split_stream.split('_')[0] == 'streams':
                split_ditch = split_stream.replace('streams','ditches')
                
                streams = rio.open(os.path.join(separated_path,split_stream))
                ditches = rio.open(os.path.join(separated_path,split_ditch))
       
                majorityS = rio.open(os.path.join(majority_path,split_stream))
                majorityD = rio.open(os.path.join(majority_path,split_ditch))

                    #combine ditches with ditches and remove overlaps
                input_sum1 = ditches.read(1) + majorityD.read(1)
                input_sum1 = input_sum1.astype(np.uint8)
                selecting_sum1 = np.where(input_sum1 < 1, input_sum1,1)
                    
                    #combine streams with streams and remove overlaps
                input_sum2 = streams.read(1) + majorityS.read(1)
                input_sum2 = input_sum2.astype(np.uint8)
                selecting_sum2 = np.where(input_sum2 < 1, input_sum2, 2)
                    
                    #combine streams and ditches in a single raster, changing overlaps to label 2
                final_sum = selecting_sum1 + selecting_sum2
                final_selection = np.where(final_sum < 3, final_sum, 2)
                
                output = os.path.join(output_path,split_stream.replace('streams_',''))
         
                try:
                        
                    output_final = rio.open(
                                            output,
                                           'w',
                                           driver='GTiff',
                                           height=streams.shape[0],
                                           width=streams.shape[1],
                                           count=1,
                                           dtype=input_sum1.dtype,
                                           crs=streams.crs,
                                           transform = rio.Affine(
                                               streams.profile['transform'][0],streams.profile['transform'][1],
                                               streams.profile['transform'][2],streams.profile['transform'][3],
                                               streams.profile['transform'][4],streams.profile['transform'][5])
                                           )
                except Exception as e:
                    print('error while creating the output file: '+split_stream.replace('streams_',''))
                    print(e)
                
                try:
                    output_final.write(final_selection,1)
                    output_final.close()
                
                except Exception as e:
                    print('error saving the output file: '+split_stream.replace('streams_',''))
                    print(e)                        

            
        else:
            print('done')
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='combines streams and ditches based on the latvian data, classifying overlaps as streams',
                                     add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('separated_path',help='path to the data separated between ditches and streams (pre-buffer)')
    parser.add_argument('majority_path', help='path to the separated rasters after the majority filter')
    parser.add_argument('output_path', help='path to the destination of the combined data')
    args = vars(parser.parse_args())
    combination(**args)            
        