from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter


from Functions import utilities as f


def view_data_interface(master):
    # CONFIGURE THE VIEW DATA FRAME
# configure grid layout (3x7)
    master.view_data_frame.rowconfigure((0, 1, 2, 3), weight=1)
    master.view_data_frame.rowconfigure(10, weight=10)
    master.view_data_frame.columnconfigure((0, 1,2,3), weight=1)
    master.view_data_frame.columnconfigure((0, 1,2,3), weight=1)
    master.view_data_frame.columnconfigure(4, weight=0)
    master.frame_info_view_data = customtkinter.CTkFrame(master=master.view_data_frame)
    master.frame_info_view_data.grid(row=0, column=0, columnspan=8, rowspan=4, pady=20, padx=10, sticky="nsew")

    # configure grid layout (1x1)
    master.frame_info_view_data.rowconfigure(0, weight=1)
    master.frame_info_view_data.columnconfigure(0, weight=1)

    master.view_data_title = customtkinter.CTkLabel(master.frame_info_view_data,
                                                text="View Data" ,
                                                height=70,
                                                text_font=("Calibri",20),
                                                corner_radius=6,  # <- custom corner radius
                                                fg_color=("white", "gray38") # <- custom tuple-color
                                               )
    master.view_data_title.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

    