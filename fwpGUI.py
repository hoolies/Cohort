import polars                                   # Import Polars to do the conversions
from tkinter import filedialog, messagebox      # Provide GUI 
from re import sub                              # Regex
 
# Select the file
def cherry_pick ():
    try:    
        while True:    
            filename = filedialog.askopenfilename()
            if filename:
                return filename
            else:
                 messagebox.showerror("Error", "Please select a file")
    except Exception as e:
        print(e)
        return None

# Check format
def check_format(filename):
    try:
        print(filename)
        if filename:
            format = sub(r'^.*\.', '', filename)
            # file = sub(r'^.*(\\|/)', '', filename.split(".")[0])
            return format
        else:
            messagebox.showerror("Error", "The filename you selected has no extension")
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
        messagebox.showerror("Error", "The file format you selected is not supported")

# Write the file with the other format
def write_file(df,filename,format):
    formats = ['csv', 'json', 'xlsx']
    formats.remove(format)
    while True:
        try:
            output_format = int(input(f"Please select the output format:\n Press:\n\t1. for {formats[0]} \n\t2. for {formats[1]}\n"))
            if output_format == 1:
                fileout = sub(r'\.\w+', 'csv', filename)
                df.write_csv(fileout)
                break
            elif output_format == 2:
                fileout = sub(r'(?<=\.)\w+', 'json', filename)
                df.write_json(fileout)
                break
            else:
                print("Please enter a valid number")
                messagebox.showerror("Error", "Please enter a valid number")
                continue
        except ValueError:
            print("Please enter a number")
            messagebox.showerror("Error", "Please enter a number")
            continue

# Main Function
def main():
    filename = cherry_pick()
    format = check_format(filename) # type: ignore
    df = read_file(filename,format)
    write_file(df,filename,format)


if __name__ == "__main__":
    main()
