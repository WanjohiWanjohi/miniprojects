import requests
from bs4 import BeautifulSoup


url = 'http://kenyalaw.org/kl/index.php?id=8380'

response = requests.get(url)


# parse text
soup = BeautifulSoup(response.text , 'html.parser')

links = soup.find_all('a')
i = 0

for link in links:
    if ('.pdf' in link.get('href' , [])):
        i+=1
        print('Downloading file:' , i)

        #get response object

        response = requests.get(link.get('href'))

        #Write content in pdf file
        pdf = open('pdf'+str(i)+".pdf" , 'wb')

        pdf.write(response.content)
        pdf.close()
        print('FIle' , i , "downloaded")