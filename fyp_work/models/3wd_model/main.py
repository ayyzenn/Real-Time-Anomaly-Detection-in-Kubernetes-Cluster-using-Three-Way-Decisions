import pandas as pd

# Function to open the file
def open_file(filename):
    return pd.read_csv(filename)

# Function to create equivalence classes
def create_equivalence_classes(dataset, columns):
    equivalence_classes = {}
    for idx, row in dataset.iterrows():
        key = tuple(row[columns].values)
        if key not in equivalence_classes:
            equivalence_classes[key] = []
        equivalence_classes[key].append(idx)
    return equivalence_classes

# Function to calculate probabilities and classify them
def calculate_probabilities(equivalence_classes, dataset, condition_column, condition_value):
    positive = []
    negative = []
    uncertain = []
    i=0
    for key, indices in equivalence_classes.items():
        i+=1
        probability = calculate_conditional_probability(dataset.iloc[indices], condition_column, condition_value)
        class_name = f"X{i}"
        if probability > 0.74:
            # class_info = (class_name, probability)

            positive.append((class_name, probability, key))
        elif probability < 0.25:
            negative.append((class_name, probability, key))
        else:
            uncertain.append((class_name, probability, key))
            
    return positive, negative, uncertain

# Function to print equivalence classes
def print_equivalence_classes(equivalence_classes):
    for idx, key in enumerate(equivalence_classes.keys(), start=1):
        print(f"Class X{idx}: {key}")

def print_classification_results(positive, negative, uncertain):
    print("Positive Classes:")
    for item in positive:
        print(f"Class: {item[0]}, Probability: {item[1]}, Key: {item[2]}")

    print("\nNegative Classes:")
    for item in negative:
        print(f"Class: {item[0]}, Probability: {item[1]}, Key: {item[2]}")

    print("\nUncertain Classes:")
    for item in uncertain:
        print(f"Class: {item[0]}, Probability: {item[1]}, Key: {item[2]}")

# Function to calculate conditional probability
def calculate_conditional_probability(class_data, condition_column, condition_value):
    intersection_count = len(class_data[class_data[condition_column] == condition_value])
    total_count = len(class_data)
    probability = intersection_count / total_count
    return probability

# Main function
def main():
    # Read the CSV file
    df = open_file("./dataset/A4Benchmark/A4Benchmark-TS1.csv")

    # Make equivalence classes based on seasonality1, seasonality2, seasonality3
    equivalence_classes = create_equivalence_classes(df, ['seasonality1', 'seasonality2', 'seasonality3'])

    # Calculate conditional probabilities and classify them
    positive, negative, uncertain = calculate_probabilities(equivalence_classes, df, 'changepoint', 1)

    # Print equivalence classes
    # print_equivalence_classes(equivalence_classes)

    # Print classification results
    # print_classification_results(positive, negative, uncertain)

if __name__ == "__main__":
    main()