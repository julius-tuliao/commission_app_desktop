import os
import sys
import customtkinter
import base64

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Functions/gui'))
from Functions.gui import  commission_interface as ci, log_interface as li, menu_interface as mi, settings_interface as si, view_data_interface as vi


## ============= INITIALIZE MASTER =============

#Configure customtkinter appearance
customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

#Initialize the master root as a Tkinter interface
master = customtkinter.CTk()
master.title("SPM Commission App")


#Set the size of the window
master.geometry("1000x660")   #Minimum window size

## ============= CREATE THE INTERFACES =============

#Configure grid layout (2x1)
master.grid_columnconfigure(1, weight=1)
master.grid_rowconfigure(0, weight=1)







#Create the principal interface
mi.create_main_interface(master)

#Create the Log In interface
li.log_interface(master)

#Create the commission interface
ci.commission_interface(master)

#Create the settings interface
si.settings_interface(master)

#Create the data interface
vi.view_data_interface(master)


##The Base64 icon version as a string
## The temp file is icon.ico
tempFile= "logo.ico"
iconfile= open(tempFile,"wb")
## Extract the icon
iconfile.close()
master.wm_iconbitmap(tempFile)
## Delete the tempfile
os.remove(tempFile)

#main loop of the root tkinter window
master.mainloop()
