import os
import pandas as pd
from tqdm import tqdm

def process_excel_to_csv(file_path, output_folder, sheet_name='ann'):
    # Load the specified table of an Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

    # Delete the first four lines
    df = df.iloc[4:]

    # Setting a new header (fifth row of data)
    new_header = df.iloc[0] 
    df = df[1:] 
    df.columns = new_header 

    # Select the specified column
    columns_to_keep = [0, 3, 5, 14, 15, 19, 25, 31]
    df = df.iloc[:, columns_to_keep]

    # Build CSV file name
    csv_file_name = os.path.splitext(os.path.basename(file_path))[0] + '.csv'
    csv_file_path = os.path.join(output_folder, csv_file_name)

    # Save as CSV file
    df.to_csv(csv_file_path, index=False)

def process_all_files_in_folder(folder_path, output_folder):
    files = [f for f in os.listdir(folder_path) if f.endswith('.xls') or f.endswith('.xlsx')]
    for file in tqdm(files, desc='Processing files', unit='file'):
        file_path = os.path.join(folder_path, file)
        process_excel_to_csv(file_path, output_folder)

# Your folder path
source_folder = 'your path'  
output_folder = 'your path'  

process_all_files_in_folder(source_folder, output_folder)