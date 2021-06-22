import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

#Assign driver variable a value equal to the file path of the driver executable
driver = webdriver.Firefox(executable_path='/home/vtrujil/Desktop/PythonProjects/GTDS/geckodriver')
#Assign URl to scrape
driver.get('https://owasp.org/www-project-top-ten/')

#Create empty list to store data
results = []

#Adding page source to content variable
content = driver.page_source
#Load content of page into BeautifulSoup. This analyzes HTML as nested data structure,
# allowing for selection of its elements using various selectors
soup = BeautifulSoup(content, features="html.parser")

#Loops through all elements returned, filtering by the provided class
main = soup.find(attrs={'id': 'sec-main'})

risks = BeautifulSoup(main.prettify(), features="html.parser")
for risk in risks.find_all('strong'):
    results.append(risk.string)
    
for x in results:
    print(x)

#Creates variable and turns object into two-dimensional data table
#Names is column and 'results' is list to be printed out
df = pd.DataFrame({'Names': results})

#Moves data of variable 'df' to specified file type
#First param assigns name to file, index used to assign specific starting numbers
#encoding used to save data in specific format
df.to_csv('names.csv', index=False, encoding='utf-8')