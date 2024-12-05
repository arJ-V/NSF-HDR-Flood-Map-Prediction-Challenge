# **iHARP HDR Anomaly Challenge Submission**
NSF/HDR Flood Prediction Challenge Submission

## **Introduction**
This project is a submission for the iHARP HDR Anomaly Challenge, which aims to predict sea-level anomalies along the US East Coast using machine learning techniques. The challenge focuses on utilizing historical tide gauge data to improve the accuracy of anomaly detection, which is crucial for coastal flood management and maritime safety.

## **Problem Statement**
The challenge involves predicting sea-level anomalies from daily tide gauge data. These anomalies represent deviations from expected sea-level conditions, often caused by events such as storm surges, hurricanes, or long-term climatic changes like the El Niño Southern Oscillation (ENSO). Accurate predictions are essential for mitigating the impacts of these events on coastal communities.

## **Data Investigation**
The dataset includes hourly sea-level measurements from 12 tide gauge stations along the US East Coast, covering the period from 1993 to 2013. Key variables include:
- **Sea Level Anomaly (SLA):** The deviation of sea surface height from the mean.
- **Location Information:** Latitude and longitude of each measurement point.
- **Temporal Coverage:** Daily records over a 20-year span.

### **Data Sources**
- National Data Buoy Center (NDBC)
- Copernicus Climate Change Service (C3S)

<img src="https://github.com/arJ-V/NSF-HDR-Flood-Map-Prediction-Challenge/blob/main/Gaugemap.jpg" alt="Alt text" width="500"/>


Map of possible tide gauge stations on US East Coast


## **Data Preprocessing**
Data preprocessing involved several critical steps:
1. **Handling Missing Values:** Replaced filler values with NaN and removed incomplete records.
    -- A note on this issue is that many missing values were filled with an arbitrary large negative number (~-270000...) such our preprocessing had to account for this also
   
2. **Time Conversion:** Converted time data into a standard datetime format for analysis. Cross referencing recorded anomaly data which included time & coordinates to the record sheet which held location (one of 12 gauges) and the SLA value at a certain time.
   
3. **Feature Engineering:** Extracted relevant features mainly looking at Sea Level Anomaly. Other values recorded on the record sheet were used for research and developing an understanding of the data set but were ultimately not necessary for our model.

### Model Visualization
One important step to help us develop our intuituion and understanding of the data and the ideal outcome was looking at the data in a time series format.

<img src="https://github.com/arJ-V/NSF-HDR-Flood-Map-Prediction-Challenge/blob/main/prophetmapping.png" alt="Alt text" width="700"/>

#### Mapping of Training data set using Meta's Prophet -- a time series forecasting algorithm (https://facebook.github.io/prophet/)

<img src="https://github.com/arJ-V/NSF-HDR-Flood-Map-Prediction-Challenge/blob/main/combineddata.jpeg" alt="Alt text" width="700"/>

#### Data plotted with anomalies marked 

<img src="https://github.com/arJ-V/NSF-HDR-Flood-Map-Prediction-Challenge/blob/main/anomaldatay.jpeg" alt="Alt text" width="700"/>

#### Anomalies isolated and marked in red 

## **Model Development**
The model development phase focused on selecting appropriate machine learning algorithms capable of handling time series data with spatial components. Key steps included:

- **Algorithm Selection:** Evaluated models such as Random Forests, LSTM networks, and hybrid models combining neural networks with fuzzy logic. Our research included a 'sweep' of relevant literature of flood analysis and model development.
  
- **Training and Validation:** Used cross-validation techniques to ensure model robustness across different stations. In addition, our project was offered with a training data set and a testing data set such that the training contained 20 years worth of data previous from 2013 and the testing container 2013-2024. 


## **Model Creation/Results**
The final model was developed with a random forest model and evaluated using metrics such as precision, recall, and F1-score. Results indicated:

<img src="https://github.com/arJ-V/NSF-HDR-Flood-Map-Prediction-Challenge/blob/main/Results.jpg" alt="Alt text" width="500"/>


## **Conclusion/Future Work**
This project successfully demonstrated the application of machine learning in predicting sea-level anomalies. Future work will focus on:
- Enhancing model accuracy by a more indepth analysis of data relationships
- Developing forecasting for 10 years beyond 2013
- Exploring real-time anomaly detection capabilities for proactive coastal management.

## **Acknowledgments**
We would like to acknowledge the following sources for their invaluable contributions:
- [National Data Buoy Center (NDBC)](https://www.ndbc.noaa.gov/)
- [Copernicus Climate Change Service (C3S)](http://climate.copernicus.eu)
- Relevant academic publications on anomaly detection and machine learning methodologies.
