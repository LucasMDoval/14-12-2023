import PySimpleGUI as sg

# Define the layout with default values for input fields
layout = [
    [sg.InputText('', key='expression_input', enable_events=True, justification='right')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/'), sg.Button('C')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*'), sg.Button('(')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-'), sg.Button(')')],
    [sg.Button('0'), sg.Button('.'), sg.Button('+'), sg.Button('='), sg.Button('Exit')],
    [sg.Text('', key='result', size=(20, 1))]
]

# Create the window
window = sg.Window('Expression Calculator', layout)

# Event loop
expression = ''
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == '=':
        try:
            result = eval(expression)
            window['result'].update(result)
        except Exception as e:
            sg.popup_error(f'Error: {e}')

    elif event == 'C':
        expression = ''
        window['expression_input'].update(expression)

    else:
        expression += event
        window['expression_input'].update(expression)

# Close the window
window.close()
