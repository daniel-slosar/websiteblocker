import PySimpleGUI as sg
import requests
import os

# hosts_file = "C:\Windows\System32\drivers\etc\hosts"

ip_add = "127.0.0.1"

def display_hosts():
    try:
        hosts = open('hosts.txt','r') #should be a path to hosts file
        txt = hosts.read()
        sg.popup_scrolled(txt)
        
    except Exception as e:
        sg.popup_error(e)   


def main_window():
    layout = [
        [sg.Text("Website Blocker", font="Arial 14 bold",justification='l')],
        [sg.Text("Website: ", font="Arial 12"),sg.Input(font="Arial 12",key="-INPUT-") ,sg.Button("Check website",font="Arial 12")],
        [sg.Button("Block website",key='-BLOCK-',visible=False,font="Arial 12"),sg.Button("Unblock",key='-UNBLOCK-',visible=False,font="Arial 12")],
        [sg.Button("Display file",font='Arial 11 bold'),sg.Button("Next",'center',font='Arial 11 bold')],
        [sg.Exit(button_color=("white","red"),font='Arial 11 bold')]
    ]

    window = sg.Window("Website Blocker", layout, size=(650, 200),grab_anywhere=True)

    while True:
        event, values = window.read()
        print(values)
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
    
    window.close()

if __name__ == "__main__":
    sg.theme('DarkBlack')
    main_window()