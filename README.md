# Automatic Detection of Ditches and Natural Streams from Digital Elevation Models Using Deep Learning
Public repository containing the code developed to prepare and analyse the data in the manuscript "Automatic Detection of Ditches and Natural Streams from Digital Elevation Models Using Deep Learning". The highest performing models for each dataset are also included, as well as sample data.

![workflow](https://github.com/mbusarello/Automatic-Detection-of-Ditches-and-Natural-Streams-from-Digital-Elevation-Models-Using-Deep-Learning/assets/72121679/60d71954-85c2-42fb-a39d-c42c253828b8)

Using topographic indices derived from the Swedish Aerial Laser Scanning data, we have trained models to detect ditches and stream channels. The topographic indices were evaluated alone and in combination.
This repository has scripts to create labels, calculate topographic indices, train and evaluate the models, and apply them to detect the location of channels. The best ranking models are available.

This is how the models performed, by Matthew's Correlation Coefficient:

![image](https://github.com/mbusarello/Automatic-Detection-of-Ditches-and-Natural-Streams-from-Digital-Elevation-Models-Using-Deep-Learning/assets/72121679/5129f3b0-a362-47bd-b74b-16201129580f)


These are the predicted locations made by the models with the highest MCC:

![combined_inferences3x2_times_24_v2](https://github.com/mbusarello/Automatic-Detection-of-Ditches-and-Natural-Streams-from-Digital-Elevation-Models-Using-Deep-Learning/assets/72121679/46954d09-e9a5-40e9-84d1-4b402bbf811f)


## Necessary data
- Channel network as a polyline shapefile
- Aerial Laser Scanning data

## Creating the labels
1. create_labels.py
2. laser_to_DEM.py
3. create_rasterlines-py
4. separating_channels.py
5. buffering_raster.py
6. calculating_hpmf.py 
7. lessthan_reclassification.py
8. multiplying_rasters.py
9. majority_filtering.py
10. combining_rasters_finaloutput.py
11. dataset_channels_labels.py
12. dataset_ditches_labels.py
13. dataset_streams_labels.py

## Topographic indices
- calculating_hillshade.py
- calculating_slope.py
- calculating_svf.py

## Creating the input chips
1. splitting_rasters.py
2. selecting_labeled_chips_by_threshold.py
3. selecting_ti_chips.py
4. splitting_training_data.py

## Semantic segmentation
- train.py
- evaluate.py
- inference_unet.py
