import sys
import os

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import pandas as pd


# Functions

# Browse file
def browse_file1(master, case):

    filename = filedialog.askopenfilename(title="Please Select a File")
    try:
        if case ==1:
            # filtering(master,1,filename) #Apply a filtering to show a plot
            # master.commission_frame.filelocation1.delete(0, END) #Insert the file location of the audio in the label
            # master.commission_frame.filelocation1.insert(0, filename)
            df = pd.read_excel (filename) #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
            print (df)

            clear_data(master)
                    #entering the data into treeview from dataframe
            master.frame_tv.tv["columns"] = list(df.columns)
            master.frame_tv.tv["show"] = "headings"

            #getting column headings
            for _ in  master.frame_tv.tv["columns"]:
                master.frame_tv.tv.heading(_,text = _)
            df_rows = df.to_numpy().tolist()
            #getting rows
            for _ in df_rows:
                master.frame_tv.tv.insert("","end" , values = _)


        

    except Exception as e:
        messagebox.showerror(message="File not supported", title="Something went wrong")
        print(e) #For developers

    return filename


def clear_data(master):
    master.frame_tv.tv.delete(*master.frame_tv.tv.get_children())
    return None

# bank selection change
def change_bank_selected(master,data):
    print(data)
    
   
def combobox_callback(master,choice):
    print(choice)
    master.current_bank_title.configure(text=choice + " Commission")
    master.settings_title.configure(text=choice + " Settings")
    master.view_data_title.configure(text=choice + " Data")
    
# Functions to change between frames
# Commission
def change_to_frame1(master):
    try:
        master.commission_frame.tkraise()
        

    except Exception:
        # Error
        messagebox.showerror(message="Something went wrong", title="You can not get there!")

# Settings Frame
def change_to_frame2(master):
    try:
        master.settings_frame.tkraise()

    except Exception:
        # Error
        messagebox.showerror(message="Something went wrong", title="You can not get there!")

# Data Frame
def change_to_frame3(master):
    try:
        master.view_data_frame.tkraise()

    except Exception:
        # Error
        messagebox.showerror(message="Something went wrong", title="You can not get there!")


def change_to_frame4(master):
    try:
        master.log_frame.tkraise()

    except Exception:
        # Error
        messagebox.showerror(message="Something went wrong", title="You can not get there!")


def login(master,user,password):
    print(user)
    print(password)
    if user == "user":
        master.log_frame.grid_forget()
        master.menu_frame_left.grid(row=0, column=0, sticky="nswe")
    else:
        messagebox.showerror(message="Wrong Username Or Password", title="Login Error")

def logout(master):
    master.menu_frame_left.grid_forget()
    master.log_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
    master.log_frame.tkraise()