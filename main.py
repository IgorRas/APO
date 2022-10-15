from lab1 import basichistogram
import PySimpleGUI as sg
from PIL import Image
import shutil
import os
import cv2
import matplotlib.pyplot as plt

number = 0


def copy_image(filename):
    global number
    name = os.path.basename(filename)[:-4]
    new_filename = f'copied/{name + str(number)}.png'
    shutil.copy(filename, new_filename)
    make_win1(new_filename)
    os.remove(new_filename)
    number += 1
    return new_filename


def save_image(filename):
    name = os.path.basename(filename)[:-4]
    img = Image.open(filename)
    path_to = sg.popup_get_folder('file to open', no_window=True)
    img.save(f'{path_to}/{name}.png', format='PNG')
    print('Saved')


def make_win1(filename):
    im = Image.open(filename)
    im.thumbnail(size=(900, 900))
    im.save(filename, format="PNG")
    column = [[sg.Image(filename, size=(500, 500))]]
    layout = [[sg.Column(column, scrollable=True, size=(500, 500))]]
    right_click_menu = ['Unused', ['Refresh']]
    return sg.Window(filename, layout, location=(800, 600),
                     resizable=True, finalize=True,
                     right_click_menu=right_click_menu)


def make_win2(filename):
    fig = plt.figure(figsize=(8, 8))
    img = cv2.imread(filename)
    fig.add_subplot(1, 1, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()


def test_menus():

    filename = 'images/Mona_Lisa_GS2.jpg'
    sg.theme('LightGreen')
    sg.set_options(element_padding=(0, 0))

    # ------ Menu Definition ------ #
    menu_def = [['&File', ['&Open', 'Save', 'Duplicate']],
                ['&Lab1', ['&Histogram', ['&Monochromatic', '&Color']], ],
                ['&Lab2', []],
                ['&Lab3', []],
                ['&Lab4', []],
                ['&Lab5', []],
                ['&Lab6', []],
                ['&Lab7', []],
                ['&Lab8', []], ]

    right_click_menu = ['Unused', []]

    # ------ GUI Defintion ------ #
    layout = [
        [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
        [sg.Output(expand_x=True, expand_y=True, size=(60, 5))]
    ]

    window = sg.Window("APO",
                       layout,
                       default_element_size=(12, 1),
                       default_button_element_size=(12, 1),
                       right_click_menu=right_click_menu,
                       resizable=True)

    # ------ Loop & Process button menu choices ------ #
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        print(event, values)
        # ------ Process menu choices ------ #
        if event == 'Open':
            filename = sg.popup_get_file('file to open', no_window=True)
            new_window = make_win1(filename)
            # make_win2(filename)
            print(filename)
        elif event == 'Save':
            save_image(filename)
        elif event == 'Duplicate':
            copy_image(filename)
        elif event == 'Monochromatic':
            basichistogram.hist_mono(filename)
        elif event == 'Color':
            basichistogram.hist_color(filename)
        elif event == 'refresh':
            new_window.refresh()
    window.close()


if __name__ == '__main__':
    test_menus()
