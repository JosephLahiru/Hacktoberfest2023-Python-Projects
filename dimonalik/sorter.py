# Small script that sorts files into folders if there are more then 1 file with similar name.
import os
import PySimpleGUI as sg
import shutil
log_entries = ""
window = sg.Window(title="Sorter", layout=[[sg.Text('Choose folder to sort')], [sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse()], [sg.Button('OK')], [sg.Text(log_entries, key='-logtext-')]], margins=(100, 50))
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == 'OK':
        folder = values["-FOLDER-"]
        print(folder)
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        for dirn in file_list:
            if os.path.isdir(folder+"/"+dirn):
                for i in file_list:
                    print
                    if dirn in i and os.path.isfile(folder+"/"+i):
                        if os.path.exists(folder+"/"+dirn+"/"+i):
                            log_entries = log_entries +"\n"+ folder+"/"+dirn+"/"+i+" already exists"
                        else:
                            shutil.move(folder+"/"+i, folder+"/"+dirn+"/")
                            log_entries = log_entries +"\n"+"moved "+i+" to "+ folder+"/"+dirn+"/"
        print(log_entries)
        if log_entries != "":
            with open(folder+"/log_script.txt", 'a') as f:
                f.write(log_entries)
            window.Element('-logtext-').Update("Done. Log written to file "+folder+"/log_script.txt")
        else:
            with open(folder+"/log_script.txt", 'a') as f:
                f.write("\n"+"No similarities found ")
            window.Element('-logtext-').Update("No similar filenames found, folder untouched ")
    log_entries = ""             
