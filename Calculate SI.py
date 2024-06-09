import pandas as pd
import os

def calculate_and_append_column(csv_file_path):
    # Load the CSV file
    data = pd.read_csv(csv_file_path)

    # Ensure that the dataframe has at least 8 columns
    if data.shape[1] < 8:
        raise ValueError("The CSV file must have at least 8 columns.")

    # Calculating the new column 'SI' and rounding to two decimal places
    data['SI'] = (((data.iloc[:, 6] / (data.iloc[:, 4] + data.iloc[:, 6])) / 
                  (data.iloc[:, 1] + data.iloc[:, 2] + data.iloc[:, 3] + 2 * data.iloc[:, 5])) + data.iloc[:, 7]).round(2)

    # Save the updated dataframe back to the original CSV file
    data.to_csv(csv_file_path, index=False)

def process_all_csv_files(folder_path):
    # Iterate through all files in the folder
    for file in os.listdir(folder_path):
        # Check if the file is a CSV file
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)
            try:
                calculate_and_append_column(file_path)
                print(f"Processed {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

# Your folder path
folder_path = 'your path'
process_all_csv_files(folder_path)