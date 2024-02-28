import PySimpleGUI as sg

values = ["Fahrenheit", "Celsius"]
sg.theme("Topanga")
def convert(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        Celsius = (value - 32) * (5/9)
        return Celsius
    else:
        Fahrenheit = (value * 9/5) + 32
        return Fahrenheit
        


layout=[[sg.Text("Convert F to C")],
        [sg.Input(key="-INPUT-")],
        [
          sg.Combo(values=values, default_value="Fahrenheit", key="-UNIT1-", expand_x=True),
          sg.Combo(values=values, default_value="Celsius", key="-UNIT2-", expand_x=True)
        ],
        [sg.Text("Converted Value")],
        [sg.Input("", key="-OUTPUT-")],
        [sg.Button("Convert", key="-CONVERT-"), sg.Button("Quit")]]

window = sg.Window("F to C Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Quit":
        break
    elif event == "-CONVERT-":
        from_unit = values["-UNIT1-"]
        to_unit = values["-UNIT2-"]
        amount = values["-INPUT-"]
        try:
            result = convert(float(amount), from_unit, to_unit)
            window["-OUTPUT-"].update(f"{round(result, 3)}")
        except:
            pass
window.close()
























































