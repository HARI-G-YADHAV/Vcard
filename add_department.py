import csv

# Define the input CSV file, output CSV file, and the content to concatenate
input_csv = 'input.csv'
output_csv = 'input.csv'
content_to_concatenate = input("Enter dept name: ")
space = " "

# Read data from the input CSV file
with open(input_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)

# Concatenate the content to the existing data in the first column of each row
for row in data:
    row[0] = row[0] + space + content_to_concatenate

# Write the modified data back to the output CSV file
with open(output_csv, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
     # Write the header row
    csv_writer.writerow(['First Name','Phone'])
    csv_writer.writerows(data)

print(f"Content '{content_to_concatenate}' concatenated with the first column of each row in '{output_csv}'")
