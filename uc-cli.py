import polars                                   # Import Polars to do the conversions
from re import sub                              # Regex
from sys import argv                            # Command Line Arguments
from argparse import ArgumentParser             # Argument Parser


# Initialize the parser
parser = ArgumentParser(
    prog = 'Universall Converter',
    description = 'This programs allow you to convert json to csv,xlsx and vice-versa',
    epilog = 'This is created by hoolies, feel free to reach out if you have questions or concerns.'
)

# Set the optional parameters
parser.add_argument('-c', '--convert',default = False, required = True, help = "Convert file in type.\nExample: \nuc-cli.py -c ./test.csv -t json")
parser.add_argument('-t', '--type',default = False, required = True, help = "Convert file in type.\nExample: \nuc-cli.py -c ./test.csv -t xlsx")

# Parse the arguments
args = parser.parse_args()

# Set variables with the arguments
convert =  args.convert
file_type = args.type

print(f'This is the convert file: {convert} \nThis is the file type: {file_type}\n')

# Select the file
def cherry_pick (convert):
    try:    
        filename = convert
        if filename:
            print(f'\n\nThis is the filename you selected: {filename}')
            return filename
        else:
            print("Error, please select a file")
    except Exception as e:
        print(e)
        return None

# Check format
def check_format(filename):
    try:
        print(filename)
        if filename:
            format = sub(r'^.*\.', '', filename)
            print(f'This is the input of check_format: {filename}\nThis is the format of the file you selected: {format}\n')
            return format
        else:
            print("Error, the filename you selected has no extension")
    except Exception as e:
        print(e)
        return None

# Read the file:
def read_file(filename,format):
    try:
        if format == 'csv':
            df = polars.read_csv(filename)
            return df
        elif format == 'json':
            df = polars.read_json(filename)
            return df
        elif format == 'xlsx':
            df = polars.read_excel(filename) # type: ignore
            return df
    except Exception as e:
        print(e)
        return None
    else:
        print("Error, the file format you selected is not supported")

# Write the file with the other format
def write_file(df,filename,file_type):
    try:
        print(f'Write file inputs:\n\tdf: {df}\n\tfilename: {filename}\n\tfile_type: {file_type}\n')
        if file_type.lower() == 'csv':
            fileout = sub(r'\.\w+', 'csv', filename)
            df.write_csv(fileout)
            print(f'This is the file you converted: {fileout}\n')
        elif file_type.lower() == 'xlsx':
            fileout = sub(r'\.\w+', 'xlsx', filename)
            df.write_excel(fileout)
            print(f'This is the file you converted: {fileout}\n')
        elif file_type.lower() == 'json':
            fileout = sub(r'(?<=\.)\w+', 'json', filename)
            df.write_json(fileout)
            print(f'This is the file you converted: {fileout}\n')
        else:
            print("Error, please enter a valid format: csv,xlsx or json")
    except ValueError as e:
        print(e)
        return None

# Main Function
def main():
    if convert:
        filename = cherry_pick(convert)
        format = check_format(filename) # type: ignore
        df = read_file(filename,format)
        write_file(df,filename,file_type)


if __name__ == "__main__":
    main()
