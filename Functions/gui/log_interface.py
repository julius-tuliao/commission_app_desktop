from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter


from Functions import utilities as f


def log_interface(master):

   
    # CONFIGURE THE VIEW DATA FRAME
    # configure grid layout (3x7)
    master.log_frame.rowconfigure((0, 1), weight=1)
    master.log_frame.rowconfigure(10, weight=10)
    master.log_frame.columnconfigure((0, 1,), weight=1)
    master.log_frame.columnconfigure((0, 1,), weight=1)
    master.log_frame.columnconfigure(2, weight=0)
    master.frame_info_log = customtkinter.CTkFrame(master=master.log_frame)
    master.frame_info_log.grid(row=0, column=0, columnspan=8, rowspan=2, pady=20, padx=10, sticky="nsew")

    # configure grid layout (1x1)
    master.frame_info_log.rowconfigure(0, weight=1)
    master.frame_info_log.columnconfigure(0, weight=1)

    master.log_title = customtkinter.CTkLabel(master.frame_info_log,
                                                text="SPM Commission App" ,
                                                height=70,
                                                text_font=("Calibri",20),
                                                corner_radius=6,  # <- custom corner radius
                                                fg_color=("white", "gray38") # <- custom tuple-color
                                               )
    master.log_title.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

    
    master.username = customtkinter.CTkEntry(master=master.log_frame, highlightbackground="lightgray", width=200,justify='center',placeholder_text="Username")
    master.username.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    master.password = customtkinter.CTkEntry(master=master.log_frame, highlightbackground="lightgray", show="*", width=200,justify='center',placeholder_text="Password")
    master.password.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    master.login = customtkinter.CTkButton(master=master.log_frame, text="Login",command= lambda: f.login(master,master.username.get(),master.password.get()))
    master.login.place(relx=0.5, rely=0.6, anchor=tk.CENTER)