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

<img src="https://github.com/arJ-V/NSF-HDR-Flood-Map-Prediction-Challenge/blob/main/Gaugemap.jpg" alt="Alt text" width="300"/>


Map of possible tide gauge stations on US East Coast


## **Data Preprocessing**
Data preprocessing involved several critical steps:
1. **Handling Missing Values:** Replaced filler values with NaN and removed incomplete records.
2. **Scaling:** Applied scaling factors to convert raw measurements into meaningful units.
3. **Time Conversion:** Converted time data into a standard datetime format for analysis.
4. **Feature Engineering:** Extracted relevant features such as geostrophic velocity anomalies and corrected for instrumental drift.

## **Model Development**
The model development phase focused on selecting appropriate machine learning algorithms capable of handling time series data with spatial components. Key steps included:
- **Algorithm Selection:** Evaluated models such as Random Forests, LSTM networks, and hybrid models combining neural networks with fuzzy logic.
- **Training and Validation:** Used cross-validation techniques to ensure model robustness across different stations.

## **Model Creation/Results**
The final model was trained on the preprocessed dataset and evaluated using metrics such as precision, recall, and F1-score. Results indicated:
- High accuracy in detecting anomalies during extreme weather events.
- Improved prediction reliability by incorporating geostrophic velocity data.

### **Visualization**
Graphs and plots were generated to visualize the model's predictions against actual sea-level measurements, highlighting areas of success and potential improvement.

## **Conclusion/Future Work**
This project successfully demonstrated the application of machine learning in predicting sea-level anomalies. Future work will focus on:
- Enhancing model accuracy by integrating additional meteorological data.
- Expanding the temporal scope to include more recent data for better generalization.
- Exploring real-time anomaly detection capabilities for proactive coastal management.

## **Acknowledgments**
We would like to acknowledge the following sources for their invaluable contributions:
- [National Data Buoy Center (NDBC)](https://www.ndbc.noaa.gov/)
- [Copernicus Climate Change Service (C3S)](http://climate.copernicus.eu)
- Relevant academic publications on anomaly detection and machine learning methodologies.
