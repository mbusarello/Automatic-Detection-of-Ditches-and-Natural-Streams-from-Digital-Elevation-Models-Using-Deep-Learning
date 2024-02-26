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

Reclassifies the HPMF values based on the threshold of -0.075, with 0 for values above it, and 1 for those below it.

7. multiplying_rasters.py

Multiplies the reclassified rasters and the buffered ones, and outputs the pixels that are within the buffer zone.

8. majority_filtering.py

Smooths the multiplied output.

9. combining_rasters_finaloutput.py

Combines the rasters with the ditch and stream pixels into a single one.

10. dataset_channels_labels.py

Creates the dataset Channels.

11. dataset_ditches_labels.py

Creates the dataset Ditches.

12. dataset_streams_labels.py

Creates the dataset Streams.


## Topographic indices
- calculating_hillshade.py
  Calculates the hillshade from the digital elevation model.
  
- calculating_slope.py
  Calculates the slope from the digital elevation model.
  
- calculating_svf.py
  Calculates the Sky-view Factor
  

## Creating the input chips
1. splitting_rasters.py
  Splits the tiles into chips to be used as training data.

2. selecting_labeled_chips_by_threshold.py
  Selects the dataset chips that are over the established threshold.

3. selecting_ti_chips.py
  Selects the chips of topographic indices based on the previously selected dataset chips.

4. splitting_training_data.py
  Splits the dataset and topographic indices chips between training (80%) and testing (20%).


## Semantic segmentation
- train.py
- evaluate.py
- inference_unet.py
