from bs4 import BeautifulSoup
import requests
import csv

page = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(page.text, 'html.parser')


#finds quotes based on the span tag in inspect element and saves it as a list
quotes = soup.find_all('span', attrs={'class':'text'})

#now the samse for authors
authors = soup.find_all('small', attrs={'class':'author'})

#now we can print the quotes and authors 
for q in quotes:
    print(q.text)

for a in authors:
    print(a.text)

#let's combine them

for quote, author in zip(quotes, authors):
    print(f'{quote.text} - by this person: {author.text}')


#we can also save this info as a cvv:

#file = open('scraped_quotes.csv', 'w')
#writer = csv.writer(file)

#creating the columns:

#writer.writerow(['quotes', 'authors'])

#and using our for loop to write our info as we iterate it

'''for quote, author in zip(quotes, authors):
    print(f'{quote.text}, {author.text}')
    writer.writerow([quote.text, author.text])'''

#and making sure we close our file
#file.close()



