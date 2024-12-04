import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
data = pd.read_csv("SLAmerged_data_Fort_Pulaski.csv")

# Ensure SLA column is numeric
data['sla'] = pd.to_numeric(data['sla'], errors='coerce')

# Drop rows with missing values for simplicity
data = data.dropna()

# Calculate global mean and standard deviation of SLA for anomaly detection
mean_sla = data['sla'].mean()
std_sla = data['sla'].std()

# Define thresholds for anomalies (e.g., 2 standard deviations from mean)
upper_threshold = mean_sla + 2 * std_sla
lower_threshold = mean_sla - 2 * std_sla

# Flag anomalies based on thresholds
data['new_anomaly'] = ((data['sla'] > upper_threshold) | (data['sla'] < lower_threshold)).astype(int)
# Initialize a new column for extended anomalies
data['extended_anomaly'] = 0

# Define stabilization range (e.g., within 1 standard deviation of mean)
stabilization_threshold = std_sla

# Propagate anomalies until stabilization
anomalous_state = False
for i in range(len(data)):
    if data.loc[i, 'new_anomaly'] == 1:  # Start of an anomaly
        anomalous_state = True
    elif anomalous_state:  # Continue marking as anomaly until stabilized
        if abs(data.loc[i, 'sla'] - mean_sla) <= stabilization_threshold:
            anomalous_state = False  # Exit anomalous state
    data.loc[i, 'extended_anomaly'] = int(anomalous_state)
  # Add rolling mean and rolling standard deviation as features
window_size = 7  # Adjust based on your needs
data['rolling_mean'] = data['sla'].rolling(window=window_size, center=True).mean()
data['rolling_std'] = data['sla'].rolling(window=window_size, center=True).std()

# Fill NaN values resulting from rolling calculations with global stats
data['rolling_mean'].fillna(mean_sla, inplace=True)
data['rolling_std'].fillna(std_sla, inplace=True)

# Define features (X) and target (y)
X = data[['sla', 'rolling_mean', 'rolling_std']]  # Features include SLA and rolling stats
y = data['extended_anomaly']  # Target is the recalculated anomaly label

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Random Forest model
rf_model = RandomForestClassifier(random_state=42)

# Train the model on training data
rf_model.fit(X_train, y_train)

# Make predictions on test set
y_pred = rf_model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

