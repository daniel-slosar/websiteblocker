import PySimpleGUI as sg
import requests


# hosts_file = "C:\Windows\System32\drivers\etc\hosts"

ip_add = "127.0.0.1"

def check(window,site):
    site=ip_add+"\t"+site
    with open('hosts.txt', 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if site in content:
            print(site)
            window['-UNBLOCK-'].update("Unblock", visible=True)
        elif site not in content:
            print(site)
            window['-BLOCK-'].update("Block", visible=True)
        else:
            sg.popup_error("Error!")

def display_hosts():
    try:
        hosts = open('hosts.txt','r') #should be a path to hosts file
        txt = hosts.read()
        sg.popup_scrolled(txt)
        
    except Exception as e:
        sg.popup_error(e)   


def main_window():
    column_to_be_centered = [
        [sg.Button("Block website",key='-BLOCK-',visible=False,font="Arial 12"),sg.Button("Unblock",key='-UNBLOCK-',visible=False,font="Arial 12")],
        [sg.Button("Display file",font='Arial 11 bold'),sg.Button("Next",'center',font='Arial 11 bold')]]
    layout = [
        [sg.Text("Website Blocker", font="Arial 14 bold",justification='l')],
        [sg.Text("Website: ", font="Arial 12"),sg.Input(font="Arial 12",key="-INPUT-") ,sg.Button("Check website",font="Arial 10")],
        [sg.Push(), sg.Column(column_to_be_centered,element_justification='c'), sg.Push()],
        [sg.Exit(button_color=("white","red"),font='Arial 11 bold')]
    ]

    window = sg.Window("Website Blocker", layout, size=(690, 220),grab_anywhere=True)

    while True:
        event, values = window.read()
        window['-UNBLOCK-'].update("Unblock", visible=False)
        window['-BLOCK-'].update("Block", visible=False)
        print(values)
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        if event=="Check website":
            check(window,site=values['-INPUT-'])
        if event=="-BLOCK-":
            sg.popup_ok("Website sucessfully blocked!")
        if event=="-UNBLOCK-":
            sg.popup_ok("Website sucessfully unblocked!")
        if event == "Display file":
            display_hosts()
    window.close()

if __name__ == "__main__":
    sg.theme('DarkBlack')
    main_window()