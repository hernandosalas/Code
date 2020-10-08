'''
Create HTML User Interface for Python using Eel Library
https://medium.com/wronmbertech/create-html-user-interface-for-python-using-eel-library-bab101cc0f99

https://github.com/samuelhwilliams/Eel

pip install eel
'''

import eel

# Set web files folder
eel.init('web')

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

eel.start('hello.html', size=(300, 200))  # Start