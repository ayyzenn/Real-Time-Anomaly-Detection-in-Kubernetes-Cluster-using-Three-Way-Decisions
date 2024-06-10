import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Functions for anomaly detection and evaluation

def sliding_window_std(df, column_name, window_size, threshold):
    results = []
    problem_vals = []  # List to store values that exceed the threshold
    problematic_rows = []  # List to store rows corresponding to problematic values
    j=0
    for i in range(len(df)):
        # Calculate the window boundaries
        start_index = max(0, i - window_size // 2)
        end_index = min(len(df), i + window_size // 2 + 1)
        
        # Get the numbers within the window
        window = df[column_name].iloc[start_index:end_index]
        
        # Calculate the standard deviation of the window
        std_dev = window.std()
        
        # Append the result to the results list
        results.append((i, df.iloc[i][column_name], window.tolist(), std_dev))
        if len(results) >= 3:
            avg_prev_results = (results[-3][3] + results[-2][3]) / 2
            threshold_value = avg_prev_results + threshold

            if std_dev > threshold_value:
                # Append the index and value to problem_vals
                problem_vals.append((i - window_size // 2, window.iloc[-1]))
                # print(problem_vals)
                row = finding_row_number(df[column_name], problem_vals)
                # print(row)
                # print(i) 
                row_num = row[j][0]
                
                # print(row_num)
                problematic_rows.append(df.iloc[row_num])
                j +=1
    print(problematic_rows)
    return results, problem_vals #, problematic_rows

def actual_anomaly(df):
    anomaly_rows = []

    # Iterate over each row in the DataFrame
    for i, row in df.iterrows():
        if row['anomaly'] == 1:
            # Append a tuple containing the row number and the value from the 'anomaly' column to the result list
            anomaly_rows.append((i, row['value']))
    # print(anomaly_rows)
    return anomaly_rows

def find_normal_values(original_lst, anomaly_lst):
    normal_values = []
    for num in original_lst:
        is_anomaly = False
        for win_num, value in anomaly_lst:
            if num == value:
                is_anomaly = True
                break
        if not is_anomaly:
            normal_values.append(num)
    return normal_values

def finding_row_number(original_lst, anomaly_lst):
    rows = []
    i = -1
    for num in original_lst:
        i +=1
        for win_num, value in anomaly_lst:
            if num == value:
                rows.append((i,num))
    return rows

def categorize_points(original_lst, anomaly_lst):
    normal = []
    seasonal = []
    anomalies = []

    for i, num in enumerate(original_lst):
        if num not in (value for _, value in anomaly_lst):
            normal.append((i, num))
        elif i % 12 == 0 or i % 168 ==0:
            seasonal.append((i, num))
        else:
            anomalies.append((i, num))

    return normal, seasonal, anomalies

def evaluate_anomaly_detection(true_labels, predicted_labels):
    # Generate confusion matrix
    cm = confusion_matrix(true_labels, predicted_labels)

    # Extract true positives (TP) and true negatives (TN)
    TP = cm[1, 1]  # Actual positive (1) and predicted positive (1)
    TN = cm[0, 0]  # Actual negative (0) and predicted negative (0)
    FP = cm[0, 1]  # Actual negative (0) but predicted positive (1)
    FN = cm[1, 0]  # Actual positive (1) but predicted negative (0)

    # # Output true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN)
    # print("True Positives (TP):", TP)
    # print("True Negatives (TN):", TN)
    # print("False Positives (FP):", FP)
    # print("False Negatives (FN):", FN)

    # # Generate classification report
    # report = classification_report(true_labels, predicted_labels)
    # print("\nClassification Report:\n", report)

    # Calculate Accuracy
    accuracy = (TP + TN) / (TP + TN + FP + FN)

    # Calculate Precision
    precision = TP / (TP + FP)

    # Calculate Recall
    recall = TP / (TP + FN)

    # Calculate F1-score
    f1_score = 2 * (precision * recall) / (precision + recall)

    # print("Accuracy:", accuracy)
    # print("Precision:", precision)
    # print("Recall:", recall)
    # print("F1-score:", f1_score)

    return accuracy

df = pd.read_csv("./dataset/A4Benchmark/A4Benchmark-TS1.csv")

# Specify the column name containing the data
column_name = 'value'

window_size = 20
threshold = 20  # Adjust threshold as needed
std_devs, anomalies = sliding_window_std(df, column_name, window_size, threshold)
actual = actual_anomaly(df)
normal_values = find_normal_values(df[column_name], anomalies)

anomaly_row_list = finding_row_number(df[column_name], anomalies)
normal_list, seasonal_anomalies, other_anomalies = categorize_points(df['value'], anomaly_row_list)

# Initialize and mark predicted anomalies
df['predicted_anomalies'] = 0
for anomaly_index, _ in other_anomalies:
    df.at[anomaly_index, 'predicted_anomalies'] = 1

# Evaluate anomaly detection and return accuracy
accuracy = evaluate_anomaly_detection(df['anomaly'], df['predicted_anomalies'])
# print(accuracy)