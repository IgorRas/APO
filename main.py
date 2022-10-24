from lab1 import basichistogram
import PySimpleGUI as sg
from PIL import Image
import shutil
import os
import cv2
import matplotlib.pyplot as plt
from lab2 import hisogramop
number = 0


def copy_image(filename):
    global number
    name = os.path.basename(filename)[:-4]
    new_filename = f'copied/{name + str(number)}.png'
    shutil.copy(filename, new_filename)
    make_win1(new_filename,  1)
    number += 1
    return new_filename


def save_image(filename):
    name = os.path.basename(filename)[:-4]
    img = Image.open(filename)
    path_to = sg.popup_get_folder('file to open', no_window=True)
    img.save(f'{path_to}/{name}.png', format='PNG')
    print('Saved')


def make_win1(filename, scale):
    im = Image.open(filename)
    width, height = im.size
    new_im = im.copy()
    new_im_resized = new_im.resize((int(width*scale), int(height*scale)))
    name = os.path.basename(filename)[:-4]
    new_im_resized.save(f'copied/{name}.png', format='PNG')
    column = [[sg.Image(f'copied/{name}.png')]]
    layout = [[sg.Column(column, scrollable=True, size_subsample_width=1, size_subsample_height=1)]]
    return sg.Window(filename, layout,
                     resizable=True, finalize=True)


def test_menus():

    filename = 'images/Mona_Lisa_GS2.jpg'
    sg.theme('LightGreen')
    sg.set_options(element_padding=(0, 0))

    # ------ Menu Definition ------ #
    menu_def = [['&File', ['&Open', 'Save', 'Duplicate']],
                ['&Lab1', ['&Histogram', ['&Monochromatic', '&Color']], ],
                ['&Lab2', ['Stretch histogram', ['Linear', 'Nonlinear']]],
                ['&Lab3', []],
                ['&Lab4', []],
                ['&Lab5', []],
                ['&Lab6', []],
                ['&Lab7', []],
                ['&Lab8', []], ]

    right_click_menu = ['', ['Zoom', ['10%', '20%', '25%', '50%', '100%', '150%', '200%']]]

    # ------ GUI Definition ------ #
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
            shutil.rmtree('copied')
            break
        print(event, values)
        # ------ Process menu choices ------ #
        if event == 'Open':
            filename = sg.popup_get_file('file to open', no_window=True)
            new_window = make_win1(filename, 1)
            print(filename)
        elif event == 'Save':
            save_image(filename)
        elif event == 'Duplicate':
            copy_image(filename)
        elif event == 'Monochromatic':
            basichistogram.hist_mono(filename)
        elif event == 'Color':
            basichistogram.hist_color(filename)
        elif event == '10%':
            new_window = make_win1(filename, 0.10)
        elif event == '20%':
            new_window = make_win1(filename, 0.20)
        elif event == '25%':
            new_window = make_win1(filename, 0.25)
        elif event == '50%':
            new_window = make_win1(filename, 0.50)
        elif event == '150%':
            new_window = make_win1(filename, 1.50)
        elif event == '200%':
            new_window = make_win1(filename, 2.00)
        elif event == 'Linear':
            layout = [
                [sg.Text('Min:'), sg.InputText()],
                [sg.Text('Max:'), sg.InputText()],
                [sg.Submit()]
            ]
            n_window = sg.Window('Podaj dane', layout)
            event, values = n_window.read()
            n_window.close()
            if int(values[0]) == 0 and int(values[1]) == 255:
                hisogramop.roz_hist_max(filename)
            else:
                hisogramop.roz_hist(filename, int(values[0]), int(values[1]))
        elif event == 'Nonlinear':
            new_window = make_win1(filename, 1)

    window.close()


if __name__ == '__main__':
    os.mkdir('copied')
    test_menus()
