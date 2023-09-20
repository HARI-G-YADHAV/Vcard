import csv

def create():
    file1 = 'file1.txt'
    file2 = 'file2.txt'
    output_csv = 'input.csv'

    # Read data from the two text files
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = [line.strip() for line in f1.readlines()]
        data2 = [line.strip() for line in f2.readlines()]

    # Ensure both lists have the same length
    if len(data1) != len(data2):
        return 0
    else:
        # Combine the two lists into a list of pairs
        combined_data = list(zip(data1, data2))

        # Write the combined data to a CSV file
        with open(output_csv, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            
            # Write the data to the CSV file
            csv_writer.writerows(combined_data)
        return 1

def add_dept(content_to_concatenate):
    input_csv = 'input.csv'
    output_csv = 'input.csv'
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

def csv_to_vcard(input_csv_file, output_vcard_file):
    with open(input_csv_file, 'r') as csv_file, open(output_vcard_file, 'w') as vcard_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            first_name = row.get('First Name', '')
            phone = row.get('Phone', '')

            vcard = f'BEGIN:VCARD\nVERSION:3.0\nFN:{first_name}\nTEL:{phone}\nEND:VCARD\n\n'

            vcard_file.write(vcard)

if __name__ == "__main__":
    input_csv_file = "input.csv"  # Replace with your CSV file name
    content_to_concatenate = input("Enter dept name: ")
    output_vcard_file = content_to_concatenate + '.vcf'# Replace with your desired VCF file name
    flag = create()
    if flag == 1:
        add_dept(content_to_concatenate)
        csv_to_vcard(input_csv_file, output_vcard_file,)
    else:
        print("Error: Input files have different numbers of lines.")
