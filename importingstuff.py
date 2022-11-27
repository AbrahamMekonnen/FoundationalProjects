import pandas as pd
import PySimpleGUI as sg

sg.theme("Hotdogstand")
#sg.popup("hello")
val = 0
slider = sg.Slider(range=(0, 1000), default_value=val, size=(50, 10), orientation="h",
                enable_events=True, key="slider")
layout = [
    [sg.Text("your stuff")],
    [sg.Text('Name', size =(15,1)), sg.InputText(key ="hi")],
    [sg.Text("your gorcoery list", size = (30,1)),
     sg.Combo(['EMU',"Home","academic"], key = "Location")],
    
    [sg.Slider(range=(0, 1000), default_value=val, size=(50, 10), orientation="h",
                enable_events=True, key="slider")],
    [sg.Button('Read')],
    [sg.Text('Plans for Break', size  = (15,1))],
    [sg.Checkbox("Checkthis", key = "Checkthis")],
    [sg.Text('Current excitment for Break', size=(15,1)),
         sg.Spin([i for i in range(0,10)], initial_value=0, key ="Excitment")],
    
    
    
        
    [sg.Submit(), sg.Exit()]
    ]
print(slider)
window = sg.Window("Simple data form",layout)
#window.read()

writer = pd.ExcelWriter("classForm.xlsx", engine = "xlsxwriter")
writer.close()
df = pd.read_excel("classForm.xlsx")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event =="Exit":
        break
    if event =="Read":
        window.Element('Checkthis').update([sg.Checkbox("Checkthis", key = "Checkthis") for i in range(5)])
    
    if event == "Submit":
        new_record = pd.DataFrame(values, index = [0])
        df = pd.concat([df, new_record], ignore_index = True)
        df.to_excel("classForm.xlsx", index = False)
        sg.popup("Data Saved")
print(df)
