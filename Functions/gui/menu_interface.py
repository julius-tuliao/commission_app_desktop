import customtkinter
from Functions import utilities as f

import os
import sys
import tkinter as tk


def create_main_interface(master):

   

    
    # Create the pitch frame

    master.view_data_frame = customtkinter.CTkFrame(master=master)
    master.view_data_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    # Create the stretcher frame

    master.settings_frame = customtkinter.CTkFrame(master=master)
    master.settings_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    #Create the equalizer frame

    master.commission_frame = customtkinter.CTkFrame(master=master)
    master.commission_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)


    # Create the Log frame

    master.log_frame = customtkinter.CTkFrame(master=master)
    master.log_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)



     # Create the Menu Selector Frame
    master.menu_frame_left = customtkinter.CTkFrame(master=master, width=180, corner_radius=0)
    master.menu_frame_left.grid(row=0, column=0, sticky="nswe")
    
    # configure grid layout (1x11)
    master.menu_frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
    master.menu_frame_left.grid_rowconfigure(6, weight=1)  # empty row as spacing
    master.menu_frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
    master.menu_frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

    #define a function to load images
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

   
    #Label button for the logo of the app
    master.title_label = customtkinter.CTkButton(master=master.menu_frame_left,
                                             text = 'SPM Commission',
                                             fg_color='#ffffff',
                                             state = "DISABLED",
                                             width = 100, height = 5)

    master.title_label.grid(row=1, column=0, pady=5, padx=0)

    # Add the button to go to the Commission frame
    master.commission_btn = customtkinter.CTkButton(master=master.menu_frame_left,
                                              text="Commission",
                                              fg_color=("gray75", "gray30"),
                                              command=lambda: f.change_to_frame1(master))

    master.commission_btn.grid(row=2, column=0, pady=10, padx=20)

    # Add a button to go to the Settings frame
    master.settings_btn = customtkinter.CTkButton(master=master.menu_frame_left,
                                              text="Settings",
                                              fg_color=("gray75", "gray30"),
                                              command=lambda: f.change_to_frame2(master))

    master.settings_btn.grid(row=3, column=0, pady=10, padx=20)

    # Add a button to go to the View Data frame
    master.view_data_btn = customtkinter.CTkButton(master=master.menu_frame_left,
                                              text="View Data",
                                              fg_color=("gray75", "gray30"),
                                              command=lambda: f.change_to_frame3(master))

    master.view_data_btn.grid(row=4, column=0, pady=10, padx=20)


    
    master.menu_frame_left.bank_option =  customtkinter.CTkOptionMenu(master=master.menu_frame_left,
                                       values=["Select Bank","PIF", "SBC"],
                                       command=lambda selected:f.combobox_callback(master,selected))
    master.menu_frame_left.bank_option.grid(row=5, column=0, pady=10, padx=20, sticky="we")  

    master.logout_btn = customtkinter.CTkButton(master=master.menu_frame_left,
                                              text="LogOut",
                                              fg_color=("gray75", "gray30"),
                                              command=lambda: f.logout(master))

    master.logout_btn.grid(row=10, column=0, pady=10, padx=20)


    master.menu_frame_left.grid_forget()
   