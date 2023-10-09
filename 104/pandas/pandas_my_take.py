#!/usr/bin/python3
"""This is a script to convert json,csv and xlsx"""

import pandas as pd

def read_file() -> pd.DataFrame: # type: ignore
    """This function reads the file"""
    filename = input("Enter the file name: ")
    if filename.endswith(".json"):
        return pd.read_json(filename),filename # type: ignore
    elif filename.endswith(".csv"):
        return pd.read_csv(filename),filename # type: ignore
    elif filename.endswith(".xlsx"):
        return pd.read_excel(filename),filename # type: ignore
    else:
        print("File format not supported")

def write_file(filename,df) -> None:
    """This function writes the file"""
    extension = input("Enter the file type that you would like to convert to: ").lower()
    fileout =filename.split(".")[0] + "." + extension
    if extension=="json":
        df.to_json(fileout)
    elif extension=="csv":
        df.to_csv(fileout)
    elif extension=="xlsx":
        df.to_excel(fileout)
    else:
        print("File format not supported")

def main():
    """Main Function"""
    df,filename=read_file()
    write_file(filename,df)


if __name__ == "__main__":
    main()

