import PySimpleGUI as sg

font=('Arial', 18)
sg.theme('Topanga')

layout = [
    [sg.Text('Result')],
    [sg.Input('', key='-output-')],
    [
        sg.Button('7', key='7'), sg.Button('8', key='8'), sg.Button('9', key='9'), sg.Button('+', key='+')
    ],
    [
        sg.Button('4', key='4'), sg.Button('5', key='5'), sg.Button('6', key='6'), sg.Button('-', key='-')
    ],
    [
        sg.Button('1', key='1'), sg.Button('2', key='2'), sg.Button('3', key='3'), sg.Button('*', key='*')
    ],
    [
        sg.Button('0', key='0'), sg.Button('.', key='.'), sg.Button('Calc', key='Calc'), sg.Button('/', key='/')
    ]
]

window = sg.Window('Calculator', layout, font=font)
str = ''
values = []
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    # Calculator keys
    elif event == '9':
        str = str+'9'
        window['-output-'].update(f'{str}')
    elif event == '8':
        str = str+'8'
        window['-output-'].update(f'{str}')
    elif event == '7':
        str = str+'7'
        window['-output-'].update(f'{str}')
   
    elif event == '6':
        str = str+'6'
        window['-output-'].update(f'{str}')
    elif event == '5':
        str = str+'5'
        window['-output-'].update(f'{str}')
    elif event == '4':
        str = str+'4'
        window['-output-'].update(f'{str}')

    elif event == '3':
        str = str+'3'
        window['-output-'].update(f'{str}')
    elif event == '2':
        str = str+'2'
        window['-output-'].update(f'{str}')
    elif event == '1':
        str = str+'1'
        window['-output-'].update(f'{str}')

    elif event == '0':
        str = str+'0'
        window['-output-'].update(f'{str}')
    elif event == 'Calc':
        window['-output-'].update('')
    
    elif event == '+':
        values.append(str)
        operand = '+'
        window['-output-'].update('')
    elif event == '-':
        values.append(str)
        operand = '-'
        window['-output-'].update('')
    elif event == '/':
        values.append(str)
        operand = '/'
        window['-output-'].update('')
    elif event == '*':
        values.append(str)
        operand = '*'
        window['-output-'].update('')
print(str)
print(values)
window.close()