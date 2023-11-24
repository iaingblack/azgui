######################################################################
# Import Required Libraries
######################################################################
import PySimpleGUI as sg
import yaml
import sys
import subprocess
import os
######################################################################
# Global Vars
######################################################################

######################################################################
# Global Functions and Data
######################################################################
# Had to create this to be able to resize the GUI. I'm not sure if this is the best way to do it, but it works.
# https://github.com/PySimpleGUI/PySimpleGUI/issues/4976
def new_window():
    ### Manage Instances ###
    # Instance Name
    txtInstanceName = sg.Text('Instance Name', tooltip='Leave blank for a random name')
    inpInstanceName = sg.Input(key='-INSTANCENAME-')

    # LAYOUT
    layout = [
        [txtInstanceName, inpInstanceName],
    ]

    # window = sg.Window("MultiManage", icon=icon_base64_png)
    window = sg.Window("AZGUI").Layout(layout)
    return window

def IsAzCliInstalled():
    # results = sg.execute_get_results(sg.execute_command_subprocess(r'az --version', pipe_output=True, wait=True, stdin=subprocess.PIPE))
    results ='ddfdf'
    if 'azure-cli' in results[0]:
        print('AZ CLI FOUND')
        return True
    else:
        print('AZ CLI NOT FOUND')
        return False

######################################################################
# Look and Feel
######################################################################
# Setup and Create Window
window = new_window()

######################################################################
# Pre Launch Check and Data Initialization
######################################################################
# if not IsAzCliInstalled():
#     import PySimpleGUI as psgazclinotfound
#     psgazclinotfound.Popup("AZ CLI not found \nPlease ensure the command\n\n  az --version\n\nworks from the command line first.")
#     sys.exit()

######################################################################
# Event Loop
######################################################################
while True:
    event, values = window.Read()
    # print(event, values)  # Useful for debugging
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

######################################################################
# Close
######################################################################
window.close()