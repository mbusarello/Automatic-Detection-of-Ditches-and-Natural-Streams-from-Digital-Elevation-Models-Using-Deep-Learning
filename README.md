# Automatic Detection of Ditches and Natural Streams from Digital Elevation Models Using Deep Learning

![workflow](https://github.com/mbusarello/Automatic-Detection-of-Ditches-and-Natural-Streams-from-Digital-Elevation-Models-Using-Deep-Learning/assets/72121679/60d71954-85c2-42fb-a39d-c42c253828b8)

Using topographic indices derived from the Swedish Aerial Laser Scanning data, we have trained models to detect ditches and stream channels. The topographic indices were evaluated alone and in combination.
This repository has scripts to create labels, calculate topographic indices, train and evaluate the models, and apply them to detect the location of channels. The best ranking models are available.

This is how the models performed according to their Matthew's Correlation Coefficient (MCC):

![image](https://github.com/mbusarello/Automatic-Detection-of-Ditches-and-Natural-Streams-from-Digital-Elevation-Models-Using-Deep-Learning/assets/72121679/5129f3b0-a362-47bd-b74b-16201129580f)

These are examples of the predictions made by the models with the highest MCC:

![combined_inferences3x2_times_24_v2](https://github.com/mbusarello/Automatic-Detection-of-Ditches-and-Natural-Streams-from-Digital-Elevation-Models-Using-Deep-Learning/assets/72121679/46954d09-e9a5-40e9-84d1-4b402bbf811f)


## Data
- Channel network as a polyline shapefile
- Aerial Laser Scanning data

The data for this study comes from 12 study areas spread across Sweden, with different characteristics regarding land use, forest cover, among others.

![study_sites_mn1_bigger](https://github.com/mbusarello/Automatic-Detection-of-Ditches-and-Natural-Streams-from-Digital-Elevation-Models-Using-Deep-Learning/assets/72121679/5f09ad14-17ca-40bc-8a39-a784dacfef49)

The data is originally organized into tiles of 2500 km x 2500 km, and for this work it is further splited into chips of 250 m x 250 m.

![tiles_chips](https://github.com/mbusarello/Automatic-Detection-of-Ditches-and-Natural-Streams-from-Digital-Elevation-Models-Using-Deep-Learning/assets/72121679/ee10caf4-b2b8-4e70-afda-b69dc3ed1a4e)


## Creating the labels
1. laser_to_DEM.py
  Creates the digital elevation model from the aerial laser data.

2. create_rasterlines-py
  Turns the polyline channels from the shapefiles into lines in raster data. The raster pixels can be 0 (background), 1 (ditches), or 2 (streams).

3. separating_channels.py
  Splits the raster data between channel type, creating a copy with only ditches and another with only streams.
  
4. buffering_raster.py
  Creates a buffer of 1.5 m around each channel in the raster data, to *****simulate the mean channel width of 3 m.

5. calculating_hpmf.py 
  Calculates the High-Pass Median Filter from the digital elevation model.

6. lessthan_reclassification.py
  

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
