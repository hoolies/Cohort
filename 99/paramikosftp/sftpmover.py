#!/usr/bin/python3 
"""Alta3 Research | rzfeeser@alta3.com
   Use Paramiko to create an SFTP session and transport files into a directory determined by the user"""

# python3 -m pip install paramiko
import paramiko # allows Python to ssh


# standard library
import os # low level operating system commands
import getpass # we need this to accept passwords


def transfer_to_this_remote_dir():
    """ask user for full path of directory to be created"""
    while True:
        what_dir = input("What directory on the remote host would you like to transfer files to (default: /tmp/)? ")
        if what_dir == "":   # if they just hit "enter" we can assume they want the default
            what_dir = "/tmp/"
            break  # escape the infinite loop
        elif what_dir[0] == "/" and what_dir[-1] == "/":
            break  # escape the infinite loop
        print("You must enter a full path for the remote host. Full paths must begin and end with '/'.")
    return what_dir  # this should be a full path


def movethemfiles(sftp):
    """a simple function that moves files across an SFTP paramiko channel"""
    what_dir = transfer_to_this_remote_dir()  # nested function call to determine the full path to transfer to

    # iterate across the files within directory
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
      if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
        sftp.put("/home/student/filestocopy/"+x, what_dir+x) # sftp.put("from_path_local", "to_path_remote") - move file to target location
    return

def main():
    """runtime"""
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender

    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass

    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    # call function that moves files
    movethemfiles(sftp)  # we must pass the sftp connection channel to the function

    ## close the connection
    sftp.close() # close the sftp connection
    t.close()    # close the transport channel

if __name__ == "__main__":
    main()

