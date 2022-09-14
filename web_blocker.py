import PySimpleGUI as sg
import requests

hosts_file = "C:\Windows\System32\drivers\etc\hosts"
ip_add = "127.0.0.1"

def check(window,site):
    global hosts
    site=ip_add+"\t"+site
    with open(hosts_file, 'r') as file:
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

def block(site):
    global hosts
    f = open(hosts_file, 'a')
    f.write("\n"+ip_add+"\t"+site+"\t#Blocked website (Delete this if you want to unblock)\n")
    f.close()


def unblock(site):
    global hosts
    link=ip_add+"\t"+site+"\t#Blocked website (Delete this if you want to unblock)"
    print(link)
    with open(hosts_file, "r") as fp:
        lines = fp.readlines()

    with open(hosts_file, "w") as fp:
        for line in lines:
            if line.strip("\n") != link:
                fp.write(line)


def display_hosts():
    try:
        global hosts
        hosts = open(hosts_file,'r') #should be a path to hosts file
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
            if values['-INPUT-'] == "":
                pass
            else:
                try:
                    response = requests.get('http://'+values['-INPUT-'])
                    if response.status_code == 200:
                        check(window,site=values['-INPUT-'])
                except:
                    sg.popup_error("Website doesn't exist!")
        if event=="-BLOCK-":
            block(site=values['-INPUT-'])
            sg.popup_ok("Website sucessfully blocked!")
        if event=="-UNBLOCK-":
            unblock(site=values['-INPUT-'])
            sg.popup_ok("Website sucessfully unblocked!")
        if event == "Display file":
            display_hosts()
    window.close()

if __name__ == "__main__":
    sg.theme('DarkBlack')
    main_window()