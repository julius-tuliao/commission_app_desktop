from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter


from Functions import utilities as f


def commission_interface(master):

    ## CONFIGURE THE COMMISSION FRAME


    # configure grid layout (3x7)
    master.commission_frame.rowconfigure((0, 1, 2, 3), weight=1)
    master.commission_frame.rowconfigure(10, weight=10)
    master.commission_frame.columnconfigure((0, 1,2,3), weight=1)
    master.commission_frame.columnconfigure((0, 1,2,3), weight=1)
    master.commission_frame.columnconfigure(4, weight=0)
    master.frame_info_commission = customtkinter.CTkFrame(master=master.commission_frame)
    master.frame_info_commission.grid(row=0, column=0, columnspan=8, rowspan=4, pady=20, padx=10, sticky="nsew")

    # configure grid layout (1x1)
    master.frame_info_commission.rowconfigure(0, weight=1)
    master.frame_info_commission.columnconfigure(0, weight=1)

    master.current_bank_title = customtkinter.CTkLabel(master.frame_info_commission,
                                                text="SPM Commission" ,
                                                height=70,
                                                text_font=("Calibri",20),
                                                corner_radius=6,  # <- custom corner radius
                                                fg_color=("white", "gray38") # <- custom tuple-color
                                               )
    master.current_bank_title.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

    

    # master.bank_option = customtkinter.CTkComboBox(master.commission_frame,
    #                                  values=["option 1", "option 2"],
    #                                  command=f.combobox_callback)
    # master.bank_option.grid(row=4, column=0, columnspan=1, sticky="w", padx=15, pady=5)
    
    master.import_file = customtkinter.CTkButton(master.commission_frame,fg_color='#ffffff',
                                                text="Import",command= lambda: f.browse_file1(master,1))
    master.import_file.grid(row=2, column=0, columnspan=1, sticky="w", padx=45, pady=5)

    master.calculate_commission = customtkinter.CTkButton(master.commission_frame,fg_color='#ffffff',
                                                text="Calculate")
    master.calculate_commission.grid(row=2, column=1, columnspan=1, sticky="w", padx=45, pady=5)

    master.save_to_db = customtkinter.CTkButton(master.commission_frame,fg_color='#ffffff',
                                            text="Save to DB")
    master.save_to_db.grid(row=2, column=2, columnspan=1, sticky="w", padx=45, pady=5)

    master.generate_billing = customtkinter.CTkButton(master.commission_frame,fg_color='#ffffff',
                                            text="Generate Billing")
    master.generate_billing.grid(row=2, column=3, columnspan=1, sticky="w", padx=45, pady=5)

    #frame for the treeview
    master.frame_table_view = customtkinter.CTkFrame(master=master.commission_frame)
    master.frame_table_view.grid(row=6, column=0, columnspan=8, rowspan=4, pady=20, padx=10, sticky="nsew")

    # configure grid layout (1x1)
    master.frame_table_view.rowconfigure(0, weight=1)
    master.frame_table_view.columnconfigure(8, weight=1)

    master.frame_tv = customtkinter.CTkFrame(master.frame_table_view)
    master.frame_tv.pack(fill=BOTH, expand=1,padx=0,pady=(0,0))
    #creating a treeview
    master.frame_tv.tv = ttk.Treeview(master.frame_tv)
    master.frame_tv.tv.pack(fill=BOTH, expand=1,padx=10,pady = (15,0))

    frame_scroll = customtkinter.CTkFrame(master.frame_tv)
    frame_scroll.pack(padx = 10 , pady = (0,15) , fill="x")
    #creating the scroll bars
    treescrollx = tk.Scrollbar(frame_scroll,  
                                orient="horizontal",
                                command = master.frame_tv.tv.xview)
    treescrollx.pack(pady = 0, padx = 0 , fill = "x")

