# Importing the PySimpleGUI library and giving it the name sg
import PySimpleGUI as sg

# Changing the theme to green
sg.theme("Green")

# Asigning a global variable a float value
cvt_metres_to_feet = 3.28084

# Creating a list
units_list = ["Feet", "Meteres"]

# Designing the layout for the GUI, with an input box, text box, button, and 2 drop down menus.
layout = [[sg.Text("Length To Convert?")],
          [sg.Input(key="-INPUT-")],
          [
            sg.Combo(values=units_list, default_value="Meters", key="-UNITS1-", expand_x=True),
            sg.Combo(values=units_list, default_value="Feet", key="-UNITS2-", expand_x=True)
          ],
          [sg.Text("Converted Value")],
          [sg.Input("", key="-OUTPUT-")],
          [sg.Button("Convert", key="-CONVERT-"), sg.Button("Quit")]]

# Creating the GUI window and inputting the layout.
window = sg.Window("Length Converter GUI", layout)

# Starting the GUI loop

while True:

    # reading in the values for the currency converter
    event, values = window.read()
    
    # If quit button pressed then break loop
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break
    # if convert button pressed then start convert
    elif event == "-CONVERT-":
        from_unit = values["-UNITS1-"]
        to_unit = values["-UNITS2-"]
        # checking for the dropdown values, then creating the conversion factor from there.
        if from_unit == to_unit:
            conversion_factor = 1
        elif from_unit == "Metres":
            conversion_factor = cvt_metres_to_feet
        else:
            conversion_factor = 1 / cvt_metres_to_feet
        
        amount = values["-INPUT-"]

        print(f"TEST amont={amount}, con={conversion_factor}")
        # converts the inputed text into a float then does the caluclation, then updates the output screen
        if amount:
            try:
                amount = float(amount)
                result = round(amount * conversion_factor, 3)
                print(f"T2 result={result}")
                window["-OUTPUT-"].update(f"{result:,}")
            except:
                pass
# once the loop has been broken, the window is forced to close.
window.close()