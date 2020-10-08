'''
guietta
A tool for making simple Python GUIs

https://github.com/alfiopuglisi/guietta

pip install guietta
'''

from guietta import _, Gui, Quit
gui = Gui(
	[ "Enter numbers:",  "__a__", "*", "__b__", ["Calculate"] ],
	[    "Result: -->", "result",   _,       _,             _ ],
	[                _,        _,   _,       _,          Quit ]
)

with gui.Calculate:
	gui.result = int(float(gui.a) * float(gui.b))

gui.run()