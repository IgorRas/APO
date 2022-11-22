import ctypes
from io import BytesIO
from pathlib import Path
from PIL import Image
import numpy as np
import PySimpleGUI as sg

class GUI():

    def __init__(self):
        ctypes.windll.user32.SetProcessDPIAware()   # Set unit of GUI to pixels
        self.column_width  = 960
        self.column_height = 720
        self.width  = 0
        self.height = 0
        self.diff = 10
        self.white = (255, 255, 255, 0)
        self.font   = ('Courier New', 16, 'bold')
        col         = [[self.graph()]]
        layout      = [[self.column(col, key='Column')],
                       [self.button('Open'), self.button('Save'),
                        self.button('Exit'),
                        self.button('Zoom In'), self.button('Zoom Out')]]
        self.window = sg.Window('Outline', layout, finalize=True,
            use_default_focus=False)
        self.draw   = self.window['Graph']
        self.im     = None
        self.key    = None
        self.scale  = 1

    """
    PySimpleGUI Elements
    """
    def button(self, text):
        return sg.Button(button_text=text, enable_events=True, font=self.font,
            key=text)

    def column(self, layout, key='Column'):
        return sg.Column(layout, background_color='grey', scrollable=True,
            size=(self.column_width, self.column_height), key='Column')

    def file(self, save=False):
        return sg.popup_get_file('message', save_as=save, no_window=True,
            font=self.font, file_types=(
            ("ALL Files", "*.*"), ("PNG Files", "*.jpg")),
            default_extension='png')

    def graph(self):
        return sg.Graph(
            (self.column_width, self.column_height), (0, self.column_height),
            (self.column_width, 0), pad=(0, 0), background_color='grey',
            enable_events=True, key='Graph')

    def image(self):
        return sg.Image(key='Image', enable_events=True)

    def draw_image(self):
        if self.key:
            self.draw.delete_figure(self.key)
        self.key = self.draw.draw_image(data=self.data, location=(0, 0))
        self.draw.Widget.configure(width=self.width*self.scale, height=self.height*self.scale)
        max_width = max(self.width*self.scale, self.column_width)
        max_height = max(self.height*self.scale, self.column_height)
        canvas = g.window['Column'].Widget.canvas
        canvas.configure(scrollregion=(0, 0, max_width, max_height))

    """
    Image Function
    """

    @property
    def data(self):
        if self.scale == 1:
            im = self.im
        else:
            im = self.im.resize(
                (int(self.width*self.scale), int(self.height*self.scale)),
                resample=Image.NEAREST)
        with BytesIO() as output:
            im.save(output, format="PNG")
            data = output.getvalue()
        return data

    def grey(self):
        im_grey = np.array(self.im.convert(mode="L"), dtype=np.uint8)
        im      = np.array(self.im, dtype=np.uint8)
        return im, im_grey

    def open_file(self):
        filename = self.file(save=False)
        if filename and Path(filename).is_file():
            self.im = Image.open(filename).convert(mode='RGBA')
            self.width, self.height = self.im.size
            self.scale = 1
            self.draw_image()

    def remove(self):
        x, y = values['Graph']
        x, y = x//self.scale, y//self.scale
        image, image_grey = self.grey()
        pixel = image_grey[y, x]
        lst = [(x, y)]
        checked = set()
        while lst:
            tmp = set()
            for point in lst:
                x1, y1 = point
                if point not in checked:
                    checked.add((x1, y1))
                    if pixel-self.diff <= image_grey[y1, x1] <= pixel+self.diff:
                        image[y1, x1] = self.white
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if 0<=x1+dx<self.width and 0<=y1+dy<self.height:
                                tmp.add((x1+dx, y1+dy))
            lst = tmp
        self.im = Image.fromarray(image)
        self.draw_image()

    def save_file(self):
        if self.key:
            filename = self.file(save=True)
            if filename:
                g.im.save(filename)

    def zoom_in(self):
        self.scale = min(self.scale+1, 10)
        self.draw_image()

    def zoom_out(self):
        self.scale = max(self.scale-1, 1)
        self.draw_image()

g = GUI()
function = {'Open':g.open_file,  'Save':g.save_file, 'Graph':g.remove,
            'Zoom In':g.zoom_in, 'Zoom Out':g.zoom_out}
while True:

    event, values = g.window.read()

    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event in function:
        function[event]()

g.window.close()