#!/bin/bash
DEM_path=$1
ti_path=$2
ditches_folder=$3

python calculating_hillshade.py "$1" "$2" 90
python semantic_segmentation/inference_unet.py best_models/Ditches_Hillshade90.h5 "$3" UNet -I "$2" --classes 0,1