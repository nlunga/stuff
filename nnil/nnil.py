import PySimpleGUI as sg
from playsound import playsound
from gtts import gTTS
import os
import wikipedia

# Define the window's contents
def test_main():
    layout = [[sg.Text("What's on your mind?")],
            [sg.Input(key='-INPUT-')],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Ok'), sg.Button('Quit')]]

    # Create the window
    window = sg.Window('Nnil', layout)

    language = 'en'
    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        # Output a message to the window
        #window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")
        wikipedia.set_lang(language)
        try:
            wiki_res = wikipedia.summary(values['-INPUT-'], sentences=2)
        except wikipedia.exceptions.PageError:
            wiki_res = "Something went wrong"
        answer = gTTS(text=wiki_res, lang=language, slow=False)
        answer.save("answer.mp3")
        sg.Popup(wiki_res)
        playsound("answer.mp3")
        os.remove("answer.mp3")

    #	print(values[0])

    # Finish up by removing from the screen
    window.close()

if __name__ == "__main__":
    test_main()
