# Joshua H. Santiago
# ASCII Art Maker
# An open source statement generator
import os

# Take in the text file name
file_path = input("Please enter the path to the file: ")

# Have user enter an output file name
output_file_Path = input("Please enter the path of the output file along with a file name and extension: ")

# look for the output file. If it exists, delete
try:
    if os.path.exists(output_file_Path):
        os.remove(output_file_Path)
        print('File Cleanup Complete')
except Exception as e:
    print(e)

# Try opening the file. If successful, read each line and place into a print statement. Append the line to the output document
try:
    with open(file_path) as reader_file:
        for line in reader_file.readlines():
            with open(output_file_Path, 'a') as writer_file:
                writer_file.write('print(\"{}\")\n'.format(line.rstrip().replace('\"', '\\"').replace("\'", "\\'")))
except Exception as e:
    print(e)
    
