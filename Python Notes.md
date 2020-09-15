# PYTHON 

### PYTHON INTERVIEW

###### TEMPLATE
```python

```

### PYTHON TIPS

- Readability is important
- Avoid unuseful conditions
- Adequate use of Whitespace
- Docstrings and Comments

##### Functional Programming

- Functions should not modify outside variables is better to pass a copy
- Do not modify values multiple times
- Pass functions as arguments

##### Principles

- **Integrity** of the code, in terms of how well it is written, resilient to errors, catching exceptions, tested and being reviewed by others
- **Explainability** of the code, with a proper documentation
- **Velocity** of the code for it to be run in live environments
- **Modularity** of your scripts and objects in order to be reusable, avoiding repetition and gaining efficiency across classes of your code
- **Generosity** with your team, for them to review your code as fast as possible and in the future understand any piece of code written why you

##### Clean code

- Be descriptive with the names within your code. I never forgot a concept I learnt ages ago when I took some Java lectures at Uni: aim for your code to be mnemonic. Mnemonic refers to a system such as a pattern of letters, ideas, or associations which assists in remembering something. I.e. it means writing self-explanatory names
- Whenever possible try to imply the type. For example for a function returning a boolean object, you can prefix it with is_ or has
Avoid abbreviations and especially single letters
- On the other hand, avoid long names and lines. Writing long names doesn’t mean being more descriptive and in terms of the lines’ length, the guideline in the PEP 8 style guide for Python Code recommends lines up to 79 characters approx.
- Don’t sacrifice clarity for consistency. If for example you’ll have objects representing employees and a list containing them all, employee_list and employee_1 is clearer than employees and employee_1
- In regards to blank lines and indentation, make your code easier to read separating sections with bank likes and using consistent indentation

##### Modular Code

- DRY: Don’t Repeat Yourself
- Using functions not only makes it less repetitive but also improves readability with descriptive names to understand what each module does
- Minimize the number of entities (functions, classes, modules, etc.)
- Single Responsibility Principle: The idea that a class should have one-and-only-one responsibility. Harder than one might expect.
- Follow the Open/Closed Principle. I.e. objects should be open for extension but closed for modification. The idea is to write code so that you’ll be able to add new functionality without changing the existing code, preventing situations in which a change to one of your classes also requires you to adapt all depending classes. There are different ways of facing this challenge, though in Python it’s very common to use inheritance.
- Try to use less than three arguments per function. If it has many, maybe split it. A similar criterion applies for the length of the function; ideally, a function should have between 20 and 50 lines. If it has more, then you might want to break it into separate functions
- Mind the length of your classes as well. If a class has more than 300 lines then it should probably be split into smaller classes.

##### Code Review

- Is the code clean and modular? Look for duplication, whitespaces, readability and modularity
- Is the code efficient? Look at loops, objects, functions structure, can it use multiprocessing?
- Is documentation effective? Look for in-line comments, docstrings and readme files
- Has the code been tested? Look for unit tests
- Is the logging good enough? Look for clarity and right frequency of logging message


### PYTHON LIBRARIES

##### **Interesting Python Libraries**
```python

#Bashplotlib
pip install bashplotlib
import numpy as np
from bashplotlib.histogram import plot_hist
arr = np.random.normal(size=1000, loc=0, scale=1)
plot_hist(arr, bincount=50)

#PrettyTable
pip install prettytable
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ['Name', 'Age', 'City']
table.add_row(["Alice", 20, "Adelaide"])
table.add_row(["Bob", 20, "Brisbane"])
table.add_row(["Chris", 20, "Cairns"])
table.add_row(["David", 20, "Sydney"])
table.add_row(["Ella", 20, "Melbourne"])
print(table)

#FyzzyWuzzy
pip install fuzzywuzzy
from fuzzywuzzy import fuzz
fuzz.ratio("Let’s do a simple test", "Let us do a simple test")

#TQDM - Progress bar
pip install tqdm
from tqdm import trange
for i in trange(100):
    sleep(0.01)
from tqdm import tqdm
for e in tqdm([1,2,3,4,5,6,7,8,9]):
    sleep(0.5)  # Suppose we are doing something with the elements
    

#RICH
#(https://github.com/willmcgugan/rich)
pip install rich
from rich import print
print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

#PIPENV
#(https://realpython.com/pipenv-guide/)
pip install pipenv
$ pipenv shell
$ pipenv install flask==0.12.1
$ pipenv install numpy
$ pipenv install pytest --dev
$ pipenv install -e git+https://github.com/requests/requests.git#egg=requests
$ pipenv install --dev
$ pipenv install -r requirements.txt
$ pipenv install -r dev-requirements.txt --dev
$ pipenv lock -r > requirements.txt
$ pipenv lock -r -d > dev-requirements.txt


#Useful libraries
Urllib3,Requests
python-dateutil,Pytz
simplejson
rsa
Setuptools
Dash - data visualization
Pygame - game framework
Pillow - Python Image Library
JmesPath - makes JSON in Python even easier. It allows you to declaratively specify how to extract elements from a JSON document
emoji
ipython
Homeassistant - Smart home automation
flask
beautifulsoup


#Black
pip install black
$black filename.py
$black --check .  #This will check which python file(s) can be formatted in the current folder (but doesn’t actually modify the python file(s)).
$black  --check --diff file_name.py  Tshis shows what needs to be done to the file but doesn’t modify the file.


#OS
import os
### Execute a shell command
os.system("echo 'My name is bob the builder'")
### Return the current working directory
os.getcwd()
### List all of the files and sub-directories in a particular folder
os.listdir("Documents")
### Create a single folder
os.mkdir("Data Science Projects")
### Create folders recursively
### The below line creates a folder "Documents" with a subfolder 
### inside it called "Data Science Projects" with a subfolder inside ### that one called "Project 1"
os.makedirs("Documents/Data Science Projects/Project 1")
### Delete a file 
os.remove("data.txt")  
### Delete a folder
os.rmdir("Data Science Projects")  
### Delete directories recursively.
os.removedirs("Documents/Data Science Projects/Project 1") 
### Rename a file or folder
os.rename("My Documents", "Your Documents")

### Handling slashes / when creating file paths
file = "process.py"
folder = "Documents/project1"
full_path = os.path.join(folder, file)
### Get the directory and file name from a full path
file = os.path.basename(full_path)
folder = os.path.dirname(full_path)
### Check if a file or folder exists
os.path.exists(full_path)
### Get the extension of a file 
name, extension = os.path.splitext(file)

# Time
import time
import datetime
import calendar
### Get the current date and time
datetime.datetime.now()
2018-11-01 20:17:12.964253
### Get just the current time
datetime.datetime.now().time()
2018-11-01 20:19:16.819745
### Freeze the program for a set period of time
time.sleep(secs=5)
### Measure runtime of a python command
start = time.time()
100 / 5
end = time.time()
print(end - start)
0.000005346

```

### PYTHON HANDY SNIPPETS

###### Interactive mode
```python
$python -i
```

###### Black in Jupyter Notebook
```python
pip install jupyter_contrib_nbextensions
jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip — user
jupyter nbextension enable jupyter-black-master/jupyter-black
```

##### **Using the enumerate() Function**
```python
scores = [54,67,48,99,27]
for i, score in enumerate(scores):
   print(i, score)
```
#### **Lambda Functions**
###### Comparing Lambda Functions with Regular Functions
```python
lambda: x: x + 3
#versus
def add3():
    return x + 3
```
###### Lambda with Apply
```python
df=pd.DataFrame({
    'id':[1,2,3,4,5],
    'name':['Jeremy','Frank','Janet','Ryan','Mary'],
    'age':[20,25,15,10,30],
    'income':[4000,7000,200,0,10000]
})
```
```python
df['age']=df.apply(lambda x: x['age']+3,axis=1)
```
###### Lambda with Filter
```python
list(filter(lambda x: x>18,df['age']))
```
###### Lambda with Map
```python
df['income']=list(map(lambda x: int(x+x*0.2),df['income']))
```
###### Lambda with Reduce
```python
import functools
functools.reduce(lambda a,b: a+b,df['income'])
```
###### Conditional Statements using Lambda Functions
```python
df['category']=df['age'].apply(lambda x: 'Adult' if x>=18 else 'Child')
```

###### Sort Sequences of Data
```python
 # Create a sequence of data
 grades = [{'name': 'Jennifer', 'final': 95},
            {'name': 'David', 'final': 92},
            {'name': 'Aaron', 'final': 98}]
 
 # Sort by name
 sorted(grades, key=lambda x: x['name'])
# [{'name': 'Aaron', 'final': 98}, {'name': 'David', 'final': 92}, {'name': 'Jennifer', 'final': 95}]
 
 # Sort by final grades, descending
 sorted(grades, key=lambda x: x['final'], reverse=True)
# [{'name': 'Aaron', 'final': 98}, {'name': 'Jennifer', 'final': 95}, {'name': 'David', 'final': 92}]
```

###### Find the Minimal and Maximal Values
```python
 # Create a sequence of data
 grades = [{'name': 'Jennifer', 'final': 95},
            {'name': 'David', 'final': 92},
            {'name': 'Aaron', 'final': 98}]
 
 # Get the highest final score
 max(grades, key=lambda x: x['final'])
# {'name': 'Aaron', 'final': 98}
 
 # Get the lowest final score
 min(grades, key=lambda x: x['final'])
# {'name': 'David', 'final': 92}
```

###### Serve As a Factory Function
```python
from collections import defaultdict

# Create a defaultdict
known_points = {'first': (2, 3), 'second': (4, 2)}
points = defaultdict(lambda: (0, 0), known_points)

# Retrive some points
points['first']
# (2, 3)
points['second']
# (4, 2)
points['three']
# (0, 0)
```

##### **LRU_cache**

```python
from functools import lru_cache
from datetime import datetime

@lru_cache(maxsize=None)
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n-1) + fib_cache(n-2)

def fib_no_cache(n):
    if n < 2:
        return n
    return fib_no_cache(n-1) + fib_no_cache(n-2)

def timeit(func,samples):
    start = datetime.now()
    func(samples)
    end = datetime.now()
    return end-start
    
UPPER = 40

cached = []
for i in range(0,UPPER):
    cached.append(timeit(fib_cache,i))

not_cached = []
for i in range(0,UPPER):
    not_cached.append(timeit(fib_no_cache,i))
```
##### **partition() Method**
```python
myString.partition("search string")

'''
The method will return a tuple — immutable, ordered data type — with three values. Assuming the substring is found, the three values will be (1) text before, (2) substring, and (3) text after.

What happens if the substring is not found? The method will still return a three-value tuple, but index 2 and 3 will be empty strings.
'''
```

##### **Combine less frequent categories into one**
![](https://miro.medium.com/max/916/1*HWVDCs8sUrjeLN1s-rSWBg.png)
![](https://miro.medium.com/max/868/1*YhWWrSP1WOsliJ6wot0CcA.png)
```python
df.artists.value_counts()
myList = df.artists.value_counts().nlargest(3).index
df_new = df.where(df.artists.isin(myList),other='other artists')
df_new.artists.value_counts()
```

##### **To find new elements of a list**
```python
A = [ 1, 3, 5, 7, 9 ]
B = [ 4, 5, 6, 7, 8 ]
set(A) - set(B) # {1,3,9}
```

##### **Map() function**
```python
#func is a function to which map passes each element of given iterable.
#itr is a iterable which is to be mapped.
map(func,itr)

def product(n1,n2): 
    return n1 *n2 
    
list1 = (1, 2, 3, 4) 
list2 = (10,20,30,40)
result = map(product, list1,list2) 
list(result) # [10,40,90,160]

#Using Map + Lambda combination
list1 = (1, 2, 3, 4) 
list2 = (10,20,30,40)
result = map(lambda x,y: x * y, list1,list2) 
print(list(result))
```

##### **Start, Stop and Set**
```python
slice(start:stop[:step])

x = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
x[ 1: 6: 2] # [2,4,6]
x[::-1] # [8,7,6,5,4,3,2,1]
```

##### **Zip and Enumerate together**
![](https://miro.medium.com/max/1400/1*b2Ah-jCUMiTMDMFSe-dyog.png)
```python
'''
Zip function helps you to bring all the list together as one so that you can iterate through each of them simultaneously whereas Enumerate helps you in getting index as well as an element attached to that index.
'''
NAME = ['Sid','John','David']
BIRD = ['Eagle','Sparrow','Vulture']
CITY =['Mumbai','US','London']

for i,(name,bird,city) in enumerate(zip(NAME,BIRD,CITY)):
    print(i,' represents ',name,' , ',bird,' and ',city)
```

##### **Random Sampling**
```python
df.sample(n=10)

df.sample(frac=0.5).reset_index(drop=True)
```

##### **Get Rid of Warnings**
```python
import warnings 
warnings.filterwarnings(action='ignore')
import keras
```

##### **Generators**
```python
def SampleGenerator(n):
    yield n
    n = n+1
    yield n
    n = n+1
    yield n
    
gen = SampleGenerator(1)

print(next(gen)) #1
print(next(gen)) #2
print(next(gen)) #3

def updatedGenerator(n):
    while(1):
        yield n
        n = n + 1
        
a = updatedGenerator(1)

for i in range(5):
    print(next(a))
```

##### **Skiprows**
```python
df = pd.read_csv('artist.csv')
df_new = pd.read_csv('artist.csv',skiprows=50)
df.shape, df_new.shape
```


##### **Logging**
```python
pip install -U logzero

#import logger from logzero
from logzero import logger

logger.debug("hello")
logger.info("info")
logger.warning("warning")
logger.error("error")


import logger and logfile
from logzero import logger, logfile

#set logfile path
logfile('my_logfile.log')

# Log messages
logger.info("This log message saved in the log file")

# Set a rotating logfile
logzero.logfile("my_logfile.log", maxBytes=1000000, backupCount=3

#import logzero package
from logzero import logger, logfile
import logging

# You can also set a different loglevel for the file handler
logfile("my_logfile.log", loglevel=logging.WARNING)

# Log messages
logger.info("This log message saved in the log file")
logger.warning("This log message saved in the log file")

#import logzero package
import logzero
from logzero import logger, logfile
import logging

#set file path
logfile("my_logfile.log")

# Set a custom formatter
my_formatter = logging.Formatter('%(filename)s - %(asctime)s - %(levelname)s: %(message)s');
logzero.formatter(my_formatter)

# Log messages
logger.info("This log message saved in the log file")
logger.warning("This log message saved in the log file")

import logzero package
from logzero import logger, logfile, setup_logger
import logging

# Set a custom formatter
my_formatter = logging.Formatter('%(filename)s - %(asctime)s - %(levelname)s: %(message)s');


#create custom logger instance
custom_logger = setup_logger(
 name="My Custom Logger",
 logfile="my_logfile.log",
 formatter=my_formatter,
 maxBytes=1000000,
 backupCount=3,level=logging.INFO)

# Log messages
custom_logger.info("This log message saved in the log file")
custom_logger.warning("This log message saved in the log file")
```


##### **Read Common File Formats**
###### Extracting from Zip Files in Python
```python
# import zipfile
from zipfile import ZipFile

# path to the zipfile
file = './Importing files.zip'

# read zipfile and extract contents
with ZipFile (file, 'r') as zip:
    zip.printdir()
    zip.extractall()
```

###### Reading Text Files in Python
```python
# read text file
with open(r'./Importing files/Analytics Vidhya.txt','r') as f:
    print(f.read(10))
    
# read text file
with open(r'./Importing files/Analytics Vidhya.txt','r') as f:
    print(f.readline())
    
# read text file
with open(r'./Importing files/Analytics Vidhya.txt','r') as f:
    print(f.readlines())

```

###### Reading CSV Files in Python
```python
# import pandas
import pandas as pd

# read csv file into a DataFrame
df = pd.read_csv(r'./Importing files/Products.csv')
# display DataFrame
df

import pandas as pd

df = pd.read_csv(r'./Importing files/Employee.txt',delimiter='\t')
df
```

###### Reading Excel Files in Python
```python
# read Excel file into a DataFrame
df = pd.read_excel(r'./Importing files/World_city.xlsx')
# print values
df

# read Europe sheet
df = pd.read_excel(r'./Importing files/World_city.xlsx',sheet_name='Europe')
df
```

###### Importing Data from a Database using Python
```python
import pandas as pd
import sqlite3

# open engine connection
con=sqlite3.connect('./Importing files/sample_test.db')

# create a cursor object
cur = con.cursor()

# Perform query: rs
rs = cur.execute('select * from TEST')

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.commit()

# Print head of DataFrame df
df
```

###### Working with JSON Files in Python
```python
import json

# open json file
with open('./Importing files/sample_json.json','r') as file:
    data = json.load(file)

# json dictionary
print(type(data))

# loading into a DataFrame
df_json = pd.DataFrame(data)
df_json

# reading directly into a DataFrame usind pd.read_json()
path = './Importing files/sample_json.json'
df = pd.read_json(path)
df
```

###### Reading Data from Pickle Files in Python
```python
import pickle

with open('./Importing files/sample_pickle.pkl','rb') as file:
    data = pickle.load(file)

# pickle data
print(type(data))

df_pkl = pd.DataFrame(data)
df_pkl
```

###### Web Scraping using Python
```python
import requests

# url = "https://weather.com/en-IN/weather/tenday/l/aff9460b9160c73ff01769fd83ae82cf37cb27fb7eb73c70b91257d413147b69"
url = "https://en.wikipedia.org/wiki/Delhi"

# response object
resp = requests.get(url)

# using text attribute of the response object, return the HTML of webpage as string
text = resp.text

print(text)

import requests
from bs4 import BeautifulSoup

# url
# url = "https://weather.com/en-IN/weather/tenday/l/aff9460b9160c73ff01769fd83ae82cf37cb27fb7eb73c70b91257d413147b69"
url = "https://en.wikipedia.org/wiki/Delhi"

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Print the response
print(soup.prettify())

title = soup.title
title

import urllib

# function to save image from the passed URL
def download_img(url, i):
    
    # folder = r'C:\Users\Dell\Desktop\Analytics Vidhya\Delhi\\'
    folder = r'./Importing files/Delhi/'
    
    # define the file path to store images
    filepath = folder + str(i) +'.jpg'
    
    # retrieve the image from the URL and save in the folder
    urllib.request.urlretrieve(url,filepath)
    
images = soup.find_all('img')
i = 1
for image in images[2:10]:
    try:
        download_img('https:'+image.get('src'), i)
        i = i+1
    except: 
        continue
        
        
################

headers = {
    "User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

URL = 'https://www.amazon.de/gp/product/B0756CYWWD/ref=as_li_tl?ie=UTF8&tag=idk01e-21&camp=1638&creative=6742&linkCode=as2&creativeASIN=B0756CYWWD&linkId=18730d371b945bad11e9ea58ab9d8b32'
def amazon():

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
sep = ','
con_price = price.split(sep, 1)[0]
converted_price = int(con_price.replace('.', ''))

# price
print(title.strip())
print(converted_price)

        
```

###### Reading Image Files using PIL
```python
from PIL import Image

# filename = r'C:\Users\Dell\Desktop\Analytics Vidhya\Delhi\1.jpg'
filename = r'./Importing files/Delhi/1.jpg'

Image.open(filename)
```

###### Read Multiple Files using Glob
```python
for i in glob.glob('.\Importing files\*.py'):
    print(i)
    
for i in glob.glob('.\Importing files\?????.py'):
    print(i)   

for i in glob.glob('./Importing files/test_image[0-9].png'):
    print(i)
    
import cv2
import matplotlib.pyplot as plt

# import glob

filepath = r'./Importing files/Delhi'

images = glob.glob(filepath+'\*.jpg')

for i in images[:3]:
    im = Image.open(i)
    plt.imshow(im)
    plt.show()
```

###### Exception Handling
```python
try:
    myfunction(100, a)
except (TypeError, NameError) as e:
    print(f"Cannot sum the variables. The exception was {e}")
except Exception as e:
    print(f"Unhandled exception: {e}")
```


###### Function Wrappers
```python
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper
    
@timethis
def predict():
    result = model.predict(X_test)
    return result    
```

###### Download image from url
```python
import requests
import os

def download_image(url, dir):
    if url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        img = requests.get(url).content
        file_name = os.path.basename(url)
        with open(f'{dir}{file_name}', 'wb') as f:
            f.write(img)

download_image('https://impshum.co.uk/red.png', './')
```

###### Download mp4 from url
```python
import requests
import os

def download_mp4(url, dir):
    mp4 = requests.get(url)
    file_name = os.path.basename(url)
    with open(f'{dir}{file_name}', 'wb') as f:
        for chunk in mp4.iter_content(chunk_size=255):
            if chunk:
                f.write(chunk)

download_mp4('https://archive.org/download/user-mp4-test/ac3.mp4', './')
```

###### Get random images from a folder
```python
from random import sample
import os

def get_random_images(dir, count):
    return sample([x for x in os.listdir(dir) if x.endswith(('jpg', 'jpeg', 'png', 'gif'))], count)

get_random_images('images', 3)
```

###### BeautifulSoup starter script
```python
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

ua = UserAgent()

def lovely_soup(url):
    r = requests.get(url, headers={'User-Agent': ua.chrome})
    return BeautifulSoup(r.text, 'lxml')

soup = lovely_soup(url)
```

###### Display notification on mac
```python
import os

def notify(title, text):
    os.system("""
        osascript -e 'display notification "{}" with title "{}"'
        """.format(text, title))

notify('title', 'content')
```

###### Create centered thumbnail from image
```python
from PIL import Image

def create_thumbnail(infile, outfile, width, height):
    thumb = width, height
    img = Image.open(infile)
    width, height = img.size

    if width > height:
        delta = width - height
        left = int(delta / 2)
        upper = 0
        right = height + left
        lower = height
    else:
        delta = height - width
        left = 0
        upper = int(delta / 2)
        right = width
        lower = width + upper

    img = img.crop((left, upper, right, lower))
    img.thumbnail(thumb, Image.ANTIALIAS)
    img.save(outfile)

create_thumbnail('file.jpg', 'file_thumb.jpg', 300, 300)
```

###### Add to pickledb if not exists
```python
db = pickledb.load(db_file, False)

def add_to_db(key, value):
    if not db.exists(key):
        db.set(key, value)
        db.dump()
        return True

add_to_db('key', 'value')
```

###### Get string between characters
```python
def get_between(s, start, end):
    return s[s.find(start) + len(start):s.rfind(end)].strip()

get_between('abc', 'a', 'c')
```

###### Print in colour
```python
class C:
    W, G, R, P, Y, C = '\033[0m', '\033[92m', '\033[91m', '\033[95m', '\033[93m', '\033[36m'

print(f'{C.G}green{C.W}')
```

###### Get JSON from url
```python
import requests

data = requests.get(url).json()
```

###### Print human readable date from epoch time
```python
import time

def get_readable_date(epoch):
    return time.strftime("%a %-d %b %Y %H:%M", time.gmtime(epoch))

get_readable_date(12345)
```

###### The simple run again loop
```python
def run_again():
    if 'y' in input('Run again (y/N): ').lower():
        run_again()

run_again()
```

###### Handle keyboard interrupt (Ctrl + C)
```python
try:
    # DO STUFF HERE
except KeyboardInterrupt:
    print('stopped')
finally:
    # DO STUFF HERE
    print('Exiting')
```

###### Read the news
```python
from GoogleNews import GoogleNews

googlenews = GoogleNews()

def get_news(query):
    googlenews.search(query)
    results = googlenews.result()
    googlenews.clear()
    return results

get_news('doom and gloom')
```

###### Multiple Assignment
```python
a = b = c = 1
```

###### Sequence Unpacking
```python
our_list = [1, 2, 3]
a, b, c = our_list
```

###### Variable swapping
```python
a, b = b, a
```

###### Reversing a list
```python
our_list = [1, 2, 3]
reversed_list = our_list[::-1]
```

###### All and any
```python
all_true = [True, True, 1, 'hello']
any_true = [0, False, True, '', []]
# all(all_true) == True
# any(all_true) == True
# all(any_true) == False
# any(any_true) == True
```

###### 7 Easter Eggs in Python
```python
import __hello__
import this
import antigravity
from __future__ import braces
hash(float('inf'))
hash(float('nan'))
from __future__ import barry_as_FLUFL
#SyntaxError: with Barry as BDFL, use '<>' instead of '!='
```

###### Splat Operator
```python
a = [1,2,3]
b = [*a,4,5,6]
print(b) # [1,2,3,4,5,6]

```

###### How To Use *args and **kwargs
```python
def printScores(student, *scores):
   print(f"Student Name: {student}")
   for score in scores:
      print(score)
printScores("Jonathan",100, 95, 88, 92, 99)
"""
Student Name: Jonathan
100
95
88
92
99
"""

def printPetNames(owner, **pets):
   print(f"Owner Name: {owner}")
   for pet,name in pets.items():
      print(f"{pet}: {name}")
printPetNames("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")
"""
Owner Name: Jonathan
dog: Brock
fish: ['Larry', 'Curly', 'Moe']
turtle: Shelldon
"""

#If we give a parameter a default value in the function definition, then it becomes optional.
def printThese(a,b,c=None):
   print(a, "is stored in a")
   print(b, "is stored in b")
   print(c, "is stored in c")
printThese(1,2)
"""
1 is stored in a
2 is stored in b
None is stored in c
"""
```

###### Enumerate
```python
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))
```

###### Zip
```python
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print("{}% {}".format(ratio * 100, color))

```

###### Print Documentation (doc)
```python
print(str.__doc__)
```

###### Dir - Return a list of attributes
```python
cool_var = str()
dir(cool_var)

```

###### Type - The type function will return the type of a given object.
```python
mystery = str()
type(mystery)
```

###### Builtins - There is a set of classes, objects, and functions, among other things, that will always be there for you in Python
```python
dir(__builtins__)
```

###### Iterate With enumerate() Instead of range()
```python
numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers):
    print(f"i: {i} num: {num}")
# i: 0 num: 45
# i: 1 num: 22
# i: 2 num: 14
# i: 3 num: 65
# i: 4 num: 97
# i: 5 num: 72

```

###### Use List Comprehensions Instead of map() and filter()
```python
numbers = [4, 2, 1, 6, 9, 7]
def square(x):
    return x*x

list(map(square, numbers))
# [16, 4, 1, 36, 81, 49]

[square(x) for x in numbers]
# [16, 4, 1, 36, 81, 49]

def is_odd(x):
    return bool(x % 2)

list(filter(is_odd, numbers))
# [1, 9, 7]

[x for x in numbers if is_odd(x)]
# [1, 9, 7]

```

###### Debug pdb
```python
'''
Here are some of the most useful commands to aid you in your debugging adventure:
n: To continue execution until the next line in the current function is reached or it returns.
l: list code
j <line>: jump to a line
b <line>: set breakpoint()
c: continue until breakpoint
q: quit
'''
import pdb

# In-line breakpoint
pdb.set_trace()

# In Python 3.7 and later
breakpoint()

# pdb.py can also be invoked as a script to debug other scripts
$ python3 -m pdb myscript.py
```

###### Format strings With f-Strings
```python
def get_name_and_decades(name, age):
    return (f"My name is {name} and I'm {age / 10:.5f} decades old.")
```

###### Sort Complex Lists With sorted()
```python
sorted([6,5,3,7,2,4,1])
# [1, 2, 3, 4, 5, 6, 7]

animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},
]
animals = sorted(animals, key=lambda animal: animal['age'])
print(animals)
# 'type': 'elephant', 'name': 'Devon', 'age': 3
# 'type': 'puma', 'name': 'Moe', 'age': 5
# 'type': 'penguin', 'name': 'Stephanie, 'age': 8
```

###### Define Default Values in Dictionaries With .get() and .setdefault()
```python
cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}
name = cowboy.get('name', 'The Man with No Name')
print(name)
#The Man with No Name 

cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}
name = cowboy.setdefault('name', 'The Man with No Name')
#{'age': 32, 'horse': 'mustang', 'hat_size': 'large', 'name': 'The Man with No Name'}
```

###### Count Hashable Objects With collections.Counter
```python
from collections import Counter
words = "if there was there was but if there was not there was not".split()
counts = Counter(words)
print(dict(counts))
# {'if': 2, 'there': 4, 'was': 4, 'but': 1, 'not': 2}
print(dict(counts.most_common(2)))
# {'there': 4, 'was': 4}

```

###### Generate Permutations and Combinations With itertools
```python
import itertools
friends = ['Monique', 'Ashish', 'Devon', 'Bernie']
print(list(itertools.permutations(friends, r=2)))
# [('Monique', 'Ashish'), ('Monique', 'Devon'), ('Monique', 'Bernie'),
# ('Ashish', 'Monique'), ('Ashish', 'Devon'), ('Ashish', 'Bernie'),
# ('Devon', 'Monique'), ('Devon', 'Ashish'), ('Devon', 'Bernie'),
# ('Bernie', 'Monique'), ('Bernie', 'Ashish'), ('Bernie', 'Devon')]

import itertools
friends = ['Monique', 'Ashish', 'Devon', 'Bernie']
print(list(itertools.combinations(friends, r=2)))
# [('Monique', 'Ashish'), ('Monique', 'Devon'), ('Monique', 'Bernie'),
# ('Ashish', 'Devon'), ('Ashish', 'Bernie'), ('Devon', 'Bernie')]

```

###### The n-largest/n-smallest function of the heapq Package.
```python
# Python code to find 3 largest and 4 smallest
# elements of a list.
import heapq

grades = [110, 25, 38, 49, 20, 95, 33, 87, 80, 90]
print(heapq.nlargest(3, grades))
# [110, 95, 90]

```

###### Dictionary and concept of zipping Dictionaries
```python
import heapq

stocks = {
    'Goog' : 520.54,
    'FB' : 76.45,
    'yhoo' : 39.28,
    'AMZN' : 306.21,
    'APPL' : 99.76
    }

# sorting according to values
zipped_1 = zip(stocks.values(), stocks.keys())
print(sorted(zipped_1))
# [(39.28, 'yhoo'), (76.45, 'FB'), (99.76, 'APPL'), (306.21, 'AMZN'), (520.54, 'Goog')]

#sorting according to keys
zipped_2 = zip(stocks.keys(), stocks.values())
print(sorted(zipped_2))
# [('AMZN', 306.21), ('APPL', 99.76), ('FB', 76.45), ('Goog', 520.54), ('yhoo', 39.28)]

```

###### The Map function.
```python
# Python code to apply a function on a list
income = [10, 30, 75]

def double_money(dollars):
    return dollars * 2

new_income = list(map(double_money, income))
print(new_income)
# [20, 60, 150]
```

######Check memory usage of your objects
```python
import sys

mylist = range(0, 10000)
print(sys.getsizeof(mylist))
# 48
```

###### Merging dictionaries
```python
dict1 = { 'a': 1, 'b': 2 }
dict2 = { 'b': 3, 'c': 4 }
merged = { **dict1, **dict2 }
print (merged)
# {'a': 1, 'b': 3, 'c': 4}
```

###### Split a string into a list
```python
mystring = "The quick brown fox"
mylist = mystring.split(' ')
print(mylist)
# ['The', 'quick', 'brown', 'fox']
```

###### Create a string from a list of strings
```python
mylist = ['The', 'quick', 'brown', 'fox']
mystring = " ".join(mylist)
print(mystring)
# 'The quick brown fox'
```

###### Ternary Operator For Conditional Assignment
```python
y = 2
x = "Success!" if (y == 2) else "Failed!"
print(x)
# Success!
```

###### Whether a number is divisible by another number
```python
def is_divisible(n, k):
  return n % k == 0
```

###### Whether a number is odd or even
```python
def is_even(n):
  return n % 2 == 0

def is_odd(n):
  return n % 2 != 0
```

###### Get the last digit of a number
```python
def last_digit(n):
  return n % 10

```

###### How to get the digits of an integer
```python
def digits(n):
  while n:
    yield n % 10
    n /= 10
```

###### Sum of all digits of a number
```python
def sum(n):
  s = 0
  while n:
    s += n % 10
    n /= 10
  return s

```

###### Number of digits in a number
```python
def length(n):
  # if n == 0: return 1
  s = 0
  while n:
    s += 1
    n /= 10
  return s
```

###### Reverse digits in a number
```python
def length(n):
  s = 0
  while n:
    s += 1
    n /= 10
  return s

def reverse(n):
  sum = 0
  k = 10 ** (length(n) - 1)
  while n:
    sum += k * (n % 10)
    n /= 10
    k /= 10
  return sum
```

###### Remove duplicates from an array
```python
def unique_stable(list):
  dupes = set()
  for val in list:
    if val not in dupes:
      dupes.add(val)
      yield val

```

###### Remove several elements from an array in a single pass
```python
def remove(list, values_to_remove):
  new_length = len(list)
  for index, value in enumerate(list):
    if index >= new_length:
      continue
    if value in values_to_remove:
      list[index] = list[new_length - 1]
      new_length -= 1
  return list[:new_length]
```

###### Arrays
```python
#Basic Operation
len(A)
A.append(42)
A.remove(2) #removes the first matching value, not a specific index
del A[0] #removes the item at a specific index
A.pop(0) #removes the item at a specific index and returns it.
A.insert(3,28)
a in A #Check if a value is present in an array
A.copy() vs A.deepcopy()
```

###### Strings
```python
#Basic Operation
s[3]
len(s)
s + t
s[2:4]
s in t
s.strip()
s.startswith(prefix)
s.endswith(suffix)
'Euclid,Axiom 5,Parallel Lines'.split(',')
3 * '01', ','.join(('Gauss', 'Prince of Hathematicians', '1777-1855'))
s.tolower()
```

###### Print all key and values in dictionary
```python
dictionary = {}
for key,val in dictionary.items():
	print (key, "=>", val)
```

###### Counting the frequency of elements from list into dictionary
```python
b = {}
for item in list:
	b[item] = b.get(item, 0) + 1
```

###### Imports
```python
import sys
print(sys.path)

import os
os.__file__

```

###### Slice a Sequence
```python
a = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Using a range, [start, end)
a[1:3] # [2, 4]
# Using a range with a step
a[1:9:2] # [2, 6, 10, 14]
# Leave out the start = an implicit start of 0
a[:5] # [0, 2, 4, 6, 8]
# Leave out the stop = an implicit end to the very last item
a[9:] # [18, 20]
# Entire list
a[:] #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

```

###### Access an Element in a Sequence Using the Reverse Index
```python
a = 'Hello World!'
# instead of using a[len(a)-1]
a[-1] # '!'
# in combination with slicing
a[-5:-1] #'orld'
```

###### Check if a Sequence Is Empty
```python
empty_list = [(), '', [], {}, set()]
for item in empty_list:
     if not item:
        print(f'Do something with the {type(item)}')

#Do something with the <class 'tuple'>
#Do something with the <class 'str'>
#Do something with the <class 'list'>
#Do something with the <class 'dict'>
#Do something with the <class 'set'>
```

###### List Comprehensions
```python
a = [1, 2, 3, 4, 5]
[x*2 for x in a] # [2, 4, 6, 8, 10]
[x*3 for x in a if x%2 == 1] #[3, 9, 15]
```

###### Set Comprehensions
```python
a = [1, -2, 2, -3, 3, 4, 4, 5, 5, 5]
{x*x for x in a} # {1, 4, 9, 16, 25}
```

###### Dict Comprehensions
```python
a = [1, 2, 3, 4, 5]
{x: x*x for x in a} #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

###### Generator Expression
```python
sum(x**2 for x in range(100)) #328350
max((x*x for x in range(100))) #9801
```

###### Unpack a Tuple
```python
items = (0, 'b', 'one', 10, 11, 'zero')
a, b, c, d, e, f = items
print(f) # zero
a, *b, c = items
print(b) # ['b', 'one', 10, 11]
*_, a, b = items
print(a) #11
```

###### Use Enumerate() In for Loops
```python
students = ('John', 'Mary', 'Mike')
for i, student in enumerate(students):
	print(f'Iteration: {i}, Student: {student}')

#Iteration: 0, Student: John
#Iteration: 1, Student: Mary
#Iteration: 2, Student: Mike
```

###### Use Reversed() In for Loops
```python
tasks = ['laundry', 'picking up kids', 'gardening', 'cooking']
for task in reversed(tasks):
	print(task)
```

###### The Zip() Function
```python
students = ('John', 'Mary', 'Mike')
ages = (15, 17, 16)
scores = (90, 88, 82, 17, 14)
for student, age, score in zip(students, ages, scores):
     print(f'{student}, age: {age}, score: {score}')
#John, age: 15, score: 90
#Mary, age: 17, score: 88
#Mike, age: 16, score: 82
zipped = zip(students, ages, scores)
a, b, c = zip(*zipped)
print(b) #(15, 17, 16)
```

###### Lambdas for Sorting
```python
students = [{'name': 'John', 'score': 98}, {'name': 'Mike', 'score': 94}, {'name': 'Jennifer', 'score': 99}]
sorted(students, key=lambda x: x['score'])
#[{'name': 'Mike', 'score': 94}, {'name': 'John', 'score': 98}, {'name': 'Jennifer', 'score': 99}]
```

###### Shorthand Conditional Assignment
```python
some_condition = True
# the expanded format
if some_condition:
    x = 5
else:
    x = 3
print(f'x is {x}') # x is 5
# the shorthand way
x = 5 if some_condition else 3
print(f'x is {x}') # x is 5
```

###### Membership Testing in a Collection
```python
a = ('one', 'two', 'three', 'four', 'five')
if 'one' in a:
    print('The tuple contains one.') # The tuple contains one.
b = {0: 'zero', 1: 'one', 2: 'two', 3: 'three'}
if 2 in b.keys():
	print('The dict has the key of 2.') #The dict has the key of 2.
```

###### Use Get() to Retrieve a Value in a Dictionary
```python
number_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three'}
number_dict[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 5
number_dict.get(5, 'five') #'five'
```

###### Get the Key Whose Value Is Maximal in a Dictionary
```python
model_scores = {'model_a': 100, 'model_z': 198, 'model_t': 150}
# workaround
keys, values = list(model_scores.keys()), list(model_scores.values())
keys[values.index(max(values))] # 'model_z'
# one-line
max(model_scores, key=model_scores.get) #'model_z'
```

###### Walrus Operator
```python
a = ['j', 'a', 'k', 'd', 'c']
if (n := len(a))%2 == 1:
	print(f'The number of letters is {n}, which is odd.') #The number of letters is 5, which is odd.
```

###### The Map() Function
```python
numbers = (1, 2, 4, 6)
indices = (2, 1, 0.5, 2)
# use map()
list(map(pow, numbers, indices)) # [1, 2, 2.0, 36]
# list comprehensions
[pow(x, y) for x, y in zip(numbers, indices)] # [1, 2, 2.0, 36]
```

###### The Filter() Function
```python
def good_word(x: str):
	has_vowels = not set('aeiou').isdisjoint(x.lower())
	long_enough = len(x) > 7
	good_start = x.lower().startswith('pre')
	return has_vowels & long_enough & good_start
words = ['Good', 'Presentation', 'preschool', 'prefix']
list(filter(good_word, words)) # ['Presentation', 'preschool']
```

###### Find Out the Most Frequent Element in a List
```python
winnings = ['John', 'Billy', 'Billy', 'Sam', 'Billy', 'John']
max(set(winnings), key = winnings.count) #'Billy'
```

###### Track the Frequencies of the Elements in a List
```python
winnings = ['John', 'Billy', 'Billy', 'Sam', 'Billy', 'John']
tracked = {item: winnings.count(item) for item in set(winnings)}
sorted(tracked.items(), key=lambda x: x[1], reverse=True) #[('Billy', 3), ('John', 2), ('Sam', 1)]
```

###### Use the With Keyword on a File
```python
with open('a_file.txt') as file:
	pass
file.closed # True
```

###### RECURSION
```python
# A stopping condition is required
#Canonical Factorials
def factorial(num):
    if num == 1:
        return 1
    return num*factorial(num-1)

#Sum of First N Integers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

```

###### Optimize Python Code in Jupyter Notebook
```python
#https://colab.research.google.com/drive/1QREeU5FIsS2GIgRJJCz2QSGZG892LIR6
%%time
sum_aggregate_1(df, 'name', 'value').sort_values('value', ascending=False).head()

! pip install line-profiler
%load_ext line_profiler
# %lprun -f [function to profile] [execution trigger]
# [function to profile]: sum_aggregate_1
# [execution trigger]: sum_aggregate_1(random_df, 'name', 'value')
%lprun -f sum_aggregate_1 sum_aggregate_1(random_df, 'name', 'value')

```

###### Unit Testing in Python
```python
#Generate a formatted full name
def formatted_name(first_name, last_name):
   full_name = first_name + ' ' + last_name
   return full_name.title()

import unittest
from name_function import formatted_name

class NamesTestCase(unittest.TestCase):

   def test_first_last_name(self):
       result = formatted_name("pete", "seeger")
       self.assertEqual(result, "Pete Seeger")
```

###### VENV
```python
$ python3 -m venv env
$ source env/bin/activate
$ which python
$ deactivate
```

###### PYENV
```python
pyenv install version
```

###### PIPENV
```python
pip install pipenv
pipenv env
pipenv install
```

###### Making Data Trees in Python
```python

from treelib import Node, Tree
tree = Tree()
tree.create_node("CEO","CEO") #root
tree.create_node("VP_1","VP_1",parent="CEO" )
tree.create_node("VP_2","VP_2",parent="CEO" )
tree.create_node("GM_1","GM_1",parent="VP_1" )
tree.create_node("GM_2","GM_2",parent="VP_2" )
tree.show()

from anytree import Node, RenderTree
ceo = Node("CEO") #root
vp_1 = Node("VP_1", parent=ceo)
vp_2 = Node("VP_2", parent=ceo)
gm_1 = Node("GM_1", parent=vp_1)
gm_2 = Node("GM_2", parent=vp_2)
for pre, fill, node in RenderTree(ceo):
    print("%s%s" % (pre, node.name))

from anytree import Node, RenderTree
from anytree.exporter import DotExporter
ceo = Node("CEO") #root
vp_1 = Node("VP_1", parent=ceo)
vp_2 = Node("VP_2", parent=ceo)
gm_1 = Node("GM_1", parent=vp_1)
gm_2 = Node("GM_2", parent=vp_2)
m_1 = Node("M_1", parent=gm_2)
DotExporter(ceo).to_picture("ceo.png")

```

###### Automatically Update Data Sources in Python
```python
#Update the Dataset from Website (URL)
import urllib.request
url = '<Your URL Here>'
output = '<Your output filename/location>'
urllib.request.urlretrieve(url, output)

#Update the Dataset from Git Repository
pip install gitpython
import git
repo = git.Repo('<your repository folder location>')
repo.remotes.origin.pull()
```

###### Docstring
```python
'''
A Python documentation string, aka docstring, is the first statement in the definition of a module, function, class, or method enclosed by triple double-quotes """.
'''

def foo():
	"""This function does nothing."""
	pass
print(foo.**doc**) # This function does nothing.
```

###### Pipey piping
```python
pip install pipey

from pipey import Pipeable

print(np.sum(np.tan([1,2,3])))

Tan = Pipeable(np.tan)
Sum = Pipeable(np.sum)
Print = Pipeable(print)

[1,2,3] >> Tan >> Sum >> Print
```

###### Data Classes in Python
```python
from dataclasses import dataclass, field

@dataclass(order=True)
class Vector:
    magnitude: float = field(init=False)
    x: int
    y: int

    def __post_init__(self):
        self.magnitude = (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(9, 12)
print(v1)  # output: Vector(magnitude=15.0, x=9, y=12)
v2 = Vector(8, 15)
print(v2)  # output: Vector(magnitude=17.0, x=8, y=15)
print(v2 > v1)  # output: True

@dataclass
class Vector:
    x: int
    y: int
    z: int


v = Vector(4, 5, 7)
print(asdict(v))  # output: {'x': 4, 'y': 5, 'z': 7}
print(astuple(v))  # output: (4, 5, 7)

from dataclasses import dataclass

@dataclass
class Card:
    rank: str
    suit: str
    
card = Card("Q", "hearts")

print(card == card)
# True

print(card.rank)
# 'Q'

print(card)
Card(rank='Q', suit='hearts')
```

###### Decorators
```python
# Define a decorator function
def show_start_end(func):
	def inner_func():
    	print(f"Before calling func {func.__name__}")
        func()
        print(f"After calling func {func.__name__}")
	return inner_func
    
# Declare a function that is decorated
@show_start_end
def say_hello():
   print(f"Hello, World!")

# Call the function
say_hello()
#Before calling func say_hello
#Hello, World!
#After calling func say_hello
```

###### Global Variables in Python
```python
def info():
    global value
    value = 5 
    print("The value is",value)
def test():
    print("The value is",value)
info() #5
test() #5
```


###### *args and **kwargs in Python
```python
def function(*args):
    for x in args:
        print(x)
function("Felix","Antony")
```

###### Lambda function in Python
```python
x = lambda a, b, c : a+b-c
print(x(5,6,3)) #8
```

###### Functions on lists
```python
### Sorting a list form low to high
list_1 = [7, 26, 34, 2, 12, 98, 56]
list_2 = sorted(list_1)
### Getting the max, min, and sum of a list
list_sum = sum(list_1) 
max_val = max(list_1)
min_val = min(list_1)
### Convert a string to a list where each element is a character
 list("bob")
["b", "o", "b"]
### You can quickly reverse a list
 list_1.reverse()
[56, 98, 12, 2, 34, 26, 7]
### Are any or all of the items in our list True?
 bool_list = [True, False, True, True]
 any(bool_list)
True
 all(bool_list)
False
### You can loop through a list's values AND indices simultaneously
for index, value in enumerate(list_1):
    "do stuff"
```

###### Playing smart with strings
```python
### Check if a string contains a substring
sentence = "Hi I'm Bob!"
if "Bob" in sentence:
    print("YES")
### Let's take care of those capital letters too, just in case the ### string for "bOb" looks a little bit different ...
if "bOb".lower() in sentence.lower():
    print("YES")
### These two will convert a string to lower and upper case letters
sentence.lower()
sentence.upper()
### Check the properties of your string
sentence.isalpha() # Alphabetic characters only (no symbols or nums)
sentence.isnumeric() # Numbers only
sentence.islower() # Is it all lower case?
sentence.isupper() # Is it all upper case?
### Clean up your string
sentence.capitalize() # First char is capitalized
sentence.lstrip() # Remove whitespace on left side
sentence.rstrip() # Remove whitespace on right side
sentence.strip() # Remove whitespace on both sides
### The .join() method can concatenate strings with a separator
### list --> string
 " ".join(["Bob","has","a","balloon"])
"Bob has a balloon"### The .split() method does the opposite of .join()
### string --> list
 "Bob has a balloon".split(" ")
["Bob","has","a","balloon"]
### The .replace() method can replace a substring with another
 "Bob has a balloon".replace("has", "is")
"Bob is a balloon"
```

###### Math functions
```python
import math
### Remainder
 math.fmod(12, 5)
2
### Getting both the faction and integer parts
 math.modf(96.12)
(0.1200000000, 96.0)
### Computes the Euclidean norm sqrt(x*x + y*y)
 hypot(2, 3)
3.6056
```

###### Chunking a list
```python
def batch(seq, size):
  return [
    seq[i:i + size]
    for i in range(0, len(seq), size)
  ]
  
INPUT_LIST = [1,2,3,4,5,6]
INPUT_SIZE = 3
print(batch(INPUT_LIST,INPUT_SIZE)) # [[1,2,3],[4,5,6]]
```

###### VirtualEnv
```python
# Install virtualenv
$ pip install virtualenv

# Activate and start virtualenv
$ virtualenv --system-site-packages -p python ./venv ; .\venv\Scripts\activate

# Generate requirements.txt from virtualenv
$ pip freeze -l > requirements.txt 

# Install libraries from requirements.txt
$ pip install -r requirements.txt
```

###### Docstring
```python
# Sphinx Style
def multiply(a, b, c=0):
    """Return sum of multiplication of all arguments.
 
    :param a: arg1
    :type a: int
    :param b: arg2
    :type b: int
    :param c: arg3, defaults to 0
    :type c: int, optional
    :raises ValueError: if arg1 is equal to arg2
    
    :rtype: int
    :return: multiplication of all arguments 
    """
    if a == b:
        raise ValueError('arg1 must not be equal to arg2')

    return a*b*c
```

###### Abstract Classes
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
a = Animal() 
# TypeError: Can't instantiate abstract class Animal with abstract methods move


class Animal():
    @abstractmethod
    def move(self):
        pass
a = Animal() # No errors

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        print('Animal moves')

class Cat(Animal):
    def move(self):
        super().move()
        print('Cat moves')

c = Cat()
c.move()

# Animal moves
# Cat moves
```

###### Sorting Objects by Multiple Keys
```python
import operator
people.sort(key=operator.itemgetter('age'))
people.sort(key=operator.itemgetter('name'))
```

###### Check memory usage of your objects
```python
import sys

mylist = range(0, 10000)
print(sys.getsizeof(mylist))
# 48
```

###### The attrs Package
```python
# pip install attrs

@attrs
class Person(object):
    name = attrib(default='John')
    surname = attrib(default='Doe')
    age = attrib(init=False)
    
p = Person()
print(p)
p = Person('Bill', 'Gates')
p.age = 60
print(p)

# Output: 
#   Person(name='John', surname='Doe', age=NOTHING)
#   Person(name='Bill', surname='Gates', age=60)
```

###### Merging dictionaries 
```python
dict1 = { 'a': 1, 'b': 2 }
dict2 = { 'b': 3, 'c': 4 }
merged = { **dict1, **dict2 }
print (merged)
# {'a': 1, 'b': 3, 'c': 4}
```

###### Find the Most Frequently Occurring Value
```python
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key = test.count))
# 4

from collections import Counter
Counter(test).most_common(1)
# [4: 4]

```

###### f-strings:
```python
# Add a coma :
print(f"{1000:,}")
   
>> 1,000
# Add a coma and display 2 decimal points:
print(f"${1000:,.2f}")
>> $1,000.00
# Express percentages with 2 decimal points:
sureness = 80/99

print(f"I am sure about this: {sureness:.2%}")
>> I am sure about this: 80.81%
# Show only 2 decimal places:
floaty = 10.2222222
print(f"floaty value is {floaty:.2f}")
>> floaty value is 10.22
# Round and show 2 decimals:
floaty = 10.2299999
print(f"floaty value is {round(floaty,2):.2f}")
>>floaty value is 10.23

#Tabular print with f-print
results = [10.22111, 30.33, 40.69999]
print ('\n'.join(f" Index: {i} Original: {k:>10}, Rounded: {k:>.2f}" for i, k in enumerate(results)))
```

###### Print tabular data
```python
pip install tabulate

from tabulate import tabulate

table = [["LexL","SuperMan",0.00],["Joker","HarleyQ",0.00],["Bane","Batman",0.00]]
headers = ["Villain", "Nemesis", "Success Rate %"]
print(tabulate(table, headers, tablefmt="fancy_grid", floatfmt=".1f"))

OUTPUT:
╒═══════════╤═══════════╤══════════════════╕
│ Villain   │ Nemesis   │   Success Rate % │
╞═══════════╪═══════════╪══════════════════╡
│ LexL      │ SuperMan  │              0.0 │
├───────────┼───────────┼──────────────────┤
│ Joker     │ HarleyQ   │              0.0 │
├───────────┼───────────┼──────────────────┤
│ Bane      │ Batman    │              0.0 │
╘═══════════╧═══════════╧══════════════════╛
```

###### Print tabular data to PDF
```python
pip install pdfkit

import pdfkit
from tabulate import tabulate

table = [["LexL","SuperMan",0.00],["Joker","HarleyQ",0.00],["Bane","Batman",0.00]]
headers = ["Villain", "Nemesis", "Success Rate %"]
exportTable = tabulate(table, headers, tablefmt="html", floatfmt=".1f")
pdfkit.from_string(exportTable, 'Villains.pdf')
```

###### Class and static methods
```python
class Dog:
	genus = "Canis"
	family = "Canidae"

	def __init__(self, breed, name):
         self.breed = breed
         self.name = name

	@classmethod
	def from_tag(cls, tag_info):
         breed = tag_info["breed"]
         name = tag_info["name"]
         return cls(breed, name)

	@staticmethod
	def can_bark():
	 	print("Yes. All dogs can bark.")

	def bark(self):
	 	print("The dog is barking.")
```

###### Private Attributes
```python
class Dog:
     def __init__(self, breed, name):
         self.breed = breed
         self.name = name
         self.__tag = f"{name} | {breed}"
 
dog = Dog("Rottweiler", "Ada")
 dog.name # 'Ada'
 dog.__tag 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Dog' object has no attribute '__tag'

 dog.__dict__
{'breed': 'Rottweiler', 'name': 'Ada', '_Dog__tag': 'Ada | Rottweiler'}
 dog._Dog__tag
'Ada | Rottweiler'
```

###### Protected Attributes
```python
class Dog:
     def __init__(self, breed, name):
         self.breed = breed
         self.name = name
         self.__tag = f"{name} | {breed}"
         self._nickname = name[0]
```

###### bin()
```python
number = 5
print(bin(number)) #0b101
```

###### namedtuple
```python
from collections import namedtuple
import math

Dot = namedtuple('Dot', 'x y')

p1, p2 = Dot(0,0), Dot(0, 5)

print(p1,p2) #(Dot(x=0, y=0), Dot(x=0, y=5))


```

###### deque
```python
from collections import deque

# creating a deque
improved_list = deque([1,2,3,4])
improved_list #deque([1, 2, 3, 4])

improved_list.appendleft(0)
improved_list #deque([0, 1, 2, 3, 4])

# poping at O(1)
improved_list.popleft() #0

improved_list # deque([1, 2, 3, 4])

# changing starting point , keeping the order
improved_list.rotate(1)
improved_list # deque([4, 1, 2, 3])


```

###### Generator
```python
g1 = (x*x for x in range(10))
print(type(g1))
print(next(g1))
print(next(g1))
# <type 'generator'>
# 0
# 1
```

###### Yield
```python

def fib(cnt):
    n, a, b = 0, 0, 1
    while n < cnt:
    	yield a
        a, b = b, a + b
        n = n + 1
        
g = fib(10)
for i in range(10):
    print (g.next())
    
# 0 1 1 2 3 5 8 13 21 34

```

###### Python Command Line Arguments
```python
# $ python main.py arg1 arg2

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    This script is going to create an employee profile. 
    """)
    parser.add_argument("name", help="Name of Employee")
    parser.add_argument("title", help="Job Title of Employee")
    parser.add_argument("--address", help="Address of Employee")

    args = parser.parse_args()

    NAME = args.name
    TITLE = args.title
    ADDRESS = args.address

    print("Name : " + NAME)
    print("Job Title : " + TITLE)
    print("Address : " + ADDRESS)
```

###### Python Code Dramatically Faster With Cython
```python
pip install Cython

cdef int i = 10

cdef int square(int x):
    return x ** 2
    
# Regular python
def factorial(n):
    if  n >= 1:
        return n * factorial(n - 1)
    return 1
    
# Cython
cpdef long fastfactorial(long n):
    if  n >= 1:
        return n * fastfactorial(n - 1)
    return 1
    
# Create a setup file

from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules = cythonize('fastfac.pyx'))

# Compile the code
python setup.py build_ext --inplace

from fastfac import fastfactorial
from fac import factorial
from timeit import timeit

print(timeit('fastfactorial(20)', globals=globals(), number=10000))  #output: 0.002164322999306023
print(timeit('factorial(20)', globals=globals(), number=10000))  #output: 0.18900858898996376

```

###### Splitting Words in a Line
```python
my_string = "This is a string in Python"
my_list = my_string.split(' ')
print(my_list)
```

###### List of words into a line
```python
my_list = ['This' , 'is' , 'a' , 'string' , 'in' , 'Python']
my_string = " ".join(my_list)
```

###### Find most frequent element in a list
```python
my_list = [1,2,3,1,1,4,2,1]
most_frequent = max(set(my_list),key=my_list.count)
print(most_frequent) # 1
```

###### Find Occurrence of all elements in list
```python
from collections import Counter
my_list = [1,2,3,1,4,1,5,5]
print(Counter(my_list)) #Counter({1: 3, 5: 2, 2: 1, 3: 1, 4: 1})
```

###### Checking for Anagram of Two strings
```python
from collections import Counter
my_string_1 = "RACECAR"
my_string_2 = "CARRACE"
if(Counter(my_string_1) == Counter(my_string_2)):
    print("Anagram")
else:
    print("Not Anagram")
# Anagram
```

###### Create Number Sequence with range
```python
my_list = list(range(2,20,2))
print(my_list) # [2, 4, 6, 8, 10, 12, 14, 16, 18]
```

###### Repeating the element multiple times
```python
my_list = [3]
my_list = my_list*5
print(my_list) # [3, 3, 3, 3, 3]
```

###### Ternary
```python
# Syntax: Statement1 if True else Statement2
age = 25
print("Eligible") if age>20 else print("Not Eligible") #Eligible
```

###### Convert Mutable into Immutable
```python
my_list = [1,2,3,4,5]
my_list = frozenset(my_list)
```

###### Rounding off with Floor and Ceil
```python
import math
my_number = 18.7
print(math.floor(my_number)) # 18
print(math.ceil(my_number)) # 19
```

###### Merging Two Dictionaries in Python
```python
dict_1 = {'One':1, 'Two':2}
dict_2 = {'Two':2, 'Three':3}
dictionary = {**dict_1, **dict_2}
print(dictionary) # {'One': 1, 'Two': 2, 'Three': 3}
```

###### Getting size of an object
```python
import sys
a = 5
print(sys.getsizeof(a)) # 28
```

###### Combining two lists into dictionary
```python
list_1 = ["One","Two","Three"]
list_2 = [1,2,3]
dictionary = dict(zip(list_1, list_2))
print(dictionary) # {'Two': 2, 'One': 1, 'Three': 3}
```

###### Calculating execution time for a program
```python
import time
start = time.clock()
for x in range(1000):
    pass
end = time.clock()
total = end - start
print(total) #0.00011900000000000105
```

###### Printing monthly calendar in python
```python
import calendar
print(calendar.month("2020","06"))
```

###### JSON
```python
import json
import pandas as pd

# Read JSON Data
# use the built-in json module
with open('students.json') as json_file:
    students0 = json.load(json_file)

# use the pandas module
with open('students.json') as json_file:
    students1 = pd.read_json(json_file, orient='index')

print(students0)
print(students1)

# Write JSON Data
# use the built-in json module
teacher = {'name': 'Mike', 'age': 50}
with open('teacher.json', 'w+') as file:
    json.dump(teacher, file)

# use the pandas module
activities = [['Mon', 'Basketball'], ['Wed', 'Soccer'], ['Sun', 'Karate']]
df = pd.DataFrame(activities, columns=['Day', 'Activity'])
with open('activities.json', 'w+') as file:
    df.to_json(file, orient='index')
```

###### Replace Substrings with .replace()
```python
sample = 'Python is kind of fun.'

print(sample.replace('kind of', 'super'))

# Returns:
# Python is super fun.
```

###### Format Strings with .upper(), .lower(), and .title()
```python
sample = 'THIS is a StRiNg'

print(sample.upper())
print(sample.lower())
print(sample.title())

# Returns:
# THIS IS A STRING
# this is a string
# This Is A String
```

###### Anagrams
```python
def anagram(word1, word2):
    if sorted(word1) == sorted(word2):
        print(f"{word1} and {word2} are anagrams!")
    else:
        print(f"{word1} and {word2} aren't anagrams!")

anagram('silent', 'listen')

# Returns:
# silent and listen are anagrams!
```

###### HEROKU
```python
# Sign In
$ heroku login -i

# Create Heroku Instance
$ heroku create

# Create Procfile(without extension)
# Procfile (run.py / my_awesome_app = Flask(__name__))
# Version 1
$ web: gunicorn run:my_awesome_app
# Version 2
$ web: sh setup.sh && streamlit run app.py

# Clone the repository
$ heroku git:clone -a coquitos-app
$ cd coquitos-app

# Deploy your changes
$ git add .
$ git commit -am "make it better"
$ git push heroku master

# Ensure that at least one instance of the app is running
$ heroku ps:scale web=1
```

###### RESTful APIs in Python
```python
'''
REQUEST
GET — Get a resource from a server.
POST — Create a new resource on the server.
PUT, PATCH — Update a request on the server.
DELETE — Delete a resource from the server.
'''

# Example
API = "https://maps.googleapis.com/maps/api/geocode/"
AUTH_KEY = "<YOUR KEY HERE>"
ADDR = "piazza+del+colosseo,+1,+rome"

RES = requests.get(f"{API}/json?address={ADDR}&key={AUTH_KEY}").json()
RES.json()  # returns a dictionary



# GET
import json
import requests
import urllib.parse

#reading in the JSON file
with open(‘volunteer_data.json’, ‘r’) as text_file_input:
    data=text_file_input.read()
#loading that file as a JSON object
obj = json.loads(data)

API_ENDPOINT = ‘https://registeredvolunteers.xyz.com/volunteer/{}/badge/{}'

#we pass on the arguments volunteerID and badgeID 
for i in obj:
     r=requests.get(API_ENDPOINT.format(urllib.parse.quote(i[‘volunteerID’]),i[‘badgeID’]))
     print(r.text)
#outside for loop
text_file_input.close()

output_json = json.loads(r.text)
#or directly use
r.json()

r.status_code
r.reason
```

###### Unofficial Windows Binaries for Python Extension Packages
```python
# https://www.lfd.uci.edu/~gohlke/pythonlibs/
```

###### Send email
```python
import yagmail
from dotenv import load_dotenv

sender_email = os.getenv('sender')
receiver_email = os.getenv('receiver')
passwordApp = os.getenv('password')
subject = 'Subject Line'

yag = yagmail.SMTP(user=sender_email, password=passwordApp)

contents = []

yag.send(receiver_email, subject, contents)
```

###### Concurrency
```python
import time
import multiprocessing

# A CPU heavy calculation, just
# as an example. This can be
# anything you like
def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, "is done")

def doit(n):
    heavy(500, n)

def pooled(n):
    # By default, our pool will have
    # numproc slots
    with multiprocessing.Pool() as pool:
       pool.map(doit, range(n))

start = time.time()
pooled(80)
end = time.time()
print("Took: ", end - start)
```

######  Pretty Print Data Structures in Python
```python
import pprint
pprint.pprint(my_dict)
```

###### Track Time for Nested Loops
```python
k = k+1
for outer_loop in tqdm_notebook(range(1,100,5),  desc='outer_loop', leave = True):
	for inner_loop in tqdm_notebook(range(1,100,5),  desc='inner_loop', leave = False):
		k+=100
```

###### Lazy Imports
```python
$ pip install pyforest
from pyforest import *
lazy_import() #List of all lazy imports
active_imports() #used imports
```

###### Download YouTube videos with youtube-dl
```python
$ pip install youtube-dl
youtube-dl <Your video link here>
```

###### Colorama
```python
$ pip install colorama

from colorama import init
from colorama inport Fore, Back, Style

init()

print(Fore.YELLOW)
print("This is a warning!")
print(Back.RED + Fore.WHITE + "This is an error!")
print(Back.RESET + Style.DIM + "Another error!")
print(Style.RESET_ALL)
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
```

###### 2D Table
```python
$ pip install tabulate

from tabulate import tabulate

table = [["Sun", 6000],["Earth",3000],["Mars",1000]]
print(tabulate(table))
```

###### ptpython - A better Python REPL
```python
# https://github.com/prompt-toolkit/ptpython
# https://pypi.org/project/ptpython/0.6/
$ pip install ptpython
$ ptpython

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```
###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```

###### TEMPLATE
```python

```




