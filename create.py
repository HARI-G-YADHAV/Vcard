
# Define the input text files and the output CSV file
import csv

file1 = 'file1.txt'
file2 = 'file2.txt'
output_csv = 'input.csv'

# Read data from the two text files
with open(file1, 'r') as f1, open(file2, 'r') as f2:
    data1 = [line.strip() for line in f1.readlines()]
    data2 = [line.strip() for line in f2.readlines()]

# Ensure both lists have the same length
if len(data1) != len(data2) or len(data2) != len(data1):
    print("Error: Input files have different numbers of lines.")
else:
    # Combine the two lists into a list of pairs
    combined_data = list(zip(data1, data2))

    # Write the combined data to a CSV file
    with open(output_csv, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        
        # Write the data to the CSV file
        csv_writer.writerows(combined_data)
