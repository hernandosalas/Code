from selenium import webdriver
import chromedriver_autoinstaller
import os
import time
# chromedriver_autoinstaller.install(cwd=True) 
# # print(chromedriver_autoinstaller.get_chrome_version())
# # print(chromedriver_autoinstaller.utils.print_chromedriver_path())
# print(chromedriver_autoinstaller.utils.find_binary_in_path("chromedriver.exe"))
# # print(os.getcwd())

if os.path.isdir(os.getcwd()+'\\84'):
    chromedriver_path = os.getcwd()+'\\84\\' + 'chromedriver.exe'
elif os.path.isdir(os.getcwd()+'\\85'):
    chromedriver_path = os.getcwd()+'\\85\\' + 'chromedriver.exe'
elif os.path.isdir(os.getcwd()+'\\86'):
    chromedriver_path = os.getcwd()+'\\85\\' + 'chromedriver.exe'

time.sleep(0.5)
print (chromedriver_path)




