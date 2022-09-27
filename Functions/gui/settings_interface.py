from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

from Functions import utilities as f


def settings_interface(master):

    ## CONFIGURE THE FRAME FOR THE STRETCHER

    # configure grid layout (3x7)
    master.settings_frame.rowconfigure((0, 1, 2, 3), weight=1)
    master.settings_frame.rowconfigure(10, weight=10)
    master.settings_frame.columnconfigure((0, 1), weight=1)
    master.settings_frame.columnconfigure((0, 1,2,3), weight=1)
    master.settings_frame.columnconfigure(4, weight=0)
    master.frame_info_settings = customtkinter.CTkFrame(master=master.settings_frame)
    master.frame_info_settings.grid(row=0, column=0, columnspan=8, rowspan=1, pady=20, padx=10, sticky="nsew")

    # configure grid layout (1x1)
    master.frame_info_settings.rowconfigure(0, weight=1)
    master.frame_info_settings.columnconfigure(0, weight=1)

    master.settings_title = customtkinter.CTkLabel(master.frame_info_settings,
                                                text="Settings" ,
                                                height=70,
                                                text_font=("Calibri",20),
                                                corner_radius=6,  # <- custom corner radius
                                                fg_color=("white", "gray38") # <- custom tuple-color
                                               )
    master.settings_title.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

    master.baseline = customtkinter.CTkLabel(master.settings_frame, text="Baseline")
    master.baseline.grid(column=0, row=2, sticky="e", padx=5, pady=0)
    master.baseline_amt = customtkinter.CTkEntry(master.settings_frame, placeholder_text="Baseline Amount")
    master.baseline_amt.grid(column=1, row=2, sticky="w", padx=5, pady=0)

    master.label_2 = customtkinter.CTkLabel(master.settings_frame, text="CTkLabel")
    master.label_2.grid(column=2, row=2, sticky="e", padx=5, pady=0)
    master.entry_2 = customtkinter.CTkEntry(master.settings_frame, placeholder_text="CTkEntry")
    master.entry_2.grid(column=3, row=2, sticky="w", padx=5, pady=0)

    master.label_3 = customtkinter.CTkLabel(master.settings_frame, text="CTkLabel")
    master.label_3.grid(column=0, row=3, sticky="e", padx=5, pady=0)
    master.entry_3 = customtkinter.CTkEntry(master.settings_frame, placeholder_text="CTkEntry")
    master.entry_3.grid(column=1, row=3, sticky="w", padx=5, pady=0)
    master.label_4 = customtkinter.CTkLabel(master.settings_frame, text="CTkLabel")
    master.label_4.grid(column=2, row=3, sticky="e", padx=5, pady=0)
    master.entry_4 = customtkinter.CTkEntry(master.settings_frame, placeholder_text="CTkEntry")
    master.entry_4.grid(column=3, row=3, sticky="w", padx=5, pady=0)