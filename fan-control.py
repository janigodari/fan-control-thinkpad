#!/usr/bin/python3
import PySimpleGUI as sg
import os
import subprocess

def fanControl(level):
    if level != "refresh":
        os.system("sudo echo level " + level + " | sudo tee /proc/acpi/ibm/fan")
        print("Fan level: " + level)

def fanSpeed():
    sensorInfo = subprocess.check_output("sensors").decode("utf-8").split("\n")
    fanSpeed = []
    
    for i in sensorInfo:
        if "fan" in i:
            fanSpeed.append(i.split(":")[-1].strip())
    window['fanSpeed'].update('Fan Speed: ' + fanSpeed[0])

layout = [ [sg.Text('', key='fanSpeed')],
           [sg.Text('Refresh Stats'), sg.Button('↺', key='refresh')],
           [sg.Button('auto', button_color=('white', 'grey'), key='auto'),
           sg.Button('0', button_color=('white', 'blue'), key='0'), 
           sg.Button('1', button_color=('white', 'grey'), key='1'),
           sg.Button('2', button_color=('white', 'grey'), key='2'),
           sg.Button('3', button_color=('white', 'green'), key='3'),
           sg.Button('4', button_color=('white', 'green'), key='4'),
           sg.Button('5', button_color=('white', 'green'), key='5'),
           sg.Button('6', button_color=('white', 'red'), key='6'),
           sg.Button('7', button_color=('white', 'red'), key='7'),
           sg.Button('Exit', button_color=('white', 'red'), key='exit')]]

window = sg.Window('Control Fan Lenovo Thinkpad Laptops', layout)

while True:          
        event, values = window.Read()
        if event == sg.WIN_CLOSED or event == 'exit':
            break
        elif event == 'refresh':
           fanSpeed()
        else:
            fanControl(event)
            fanSpeed()
        
window.close()