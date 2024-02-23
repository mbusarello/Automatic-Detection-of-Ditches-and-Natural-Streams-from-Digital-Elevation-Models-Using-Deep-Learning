# -*- coding: utf-8 -*-
"""
@author: Mariana Busarello, 2024
"""

import os
import argparse

def selecting_chips(label_path,ti_path): 
    
    unique = sorted([chip for chip in os.listdir(label_path) if chip.endswith('.tif')])
    
    for chip in sorted(os.listdir(ti_path)):       
        if chip in unique:
            pass
        else:
            os.remove(os.path.join(ti_path,chip))
                    
            
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='matches the topographic index chips to the selected labeled chips',
                                         add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('label_path', help='path to the folder containing the selected label chips')
    parser.add_argument('ti_path', help='path to the folder containing the split topographic index')
    args = vars(parser.parse_args())
    selecting_chips(**args)
