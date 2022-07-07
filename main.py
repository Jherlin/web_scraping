import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# Create object to execute through chromedriver
driver = webdriver.Chrome(executable_path='C:/Users/Student/Desktop/chromedriver.exe')
# Open oxylabs website through chromedriver
driver.get('http://oxylabs.io/blog')
# Two empty list to keep our text data
results = []
other_results = []
# Store page source from website URL
content = driver.page_source
# Stores readable source code into soup
soup = BeautifulSoup(content)
# Quit instance of object
driver.quit()

# Loop iterates through elements with parent class attribute
for a in soup.findAll(attrs='css-1dmex2s e1kk1ckf2'):
    # Find tag where titles are stored
    name = a.find('h5')
    # if title does not exist add to list
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='css-1dmex2s e1kk1ckf2'):
    # find all p tags and return last p tag
    date = b.find_all('p')[-1]
    # if date does not exist add to list
    if date not in results:
        other_results.append(date.text)

# Creates table with two columns
df = pd.DataFrame({'Names': results, 'Dates': other_results})
# Export table as csv file
df.to_csv('names.csv', index=False, encoding='utf-8')
