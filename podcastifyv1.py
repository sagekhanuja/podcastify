##podcastify

import requests
from bs4 import BeautifulSoup
from gtts import gTTS

url = str(input("please input the link of an news article: "))

language = str(input("please input your language (e.g. English -> en): "))

output_file_name = str(input("what would you like the file to be called? "))

try:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    article = ""

    for paragraph in soup.find_all('p'):
        article += paragraph.text + " "

    print("transcribing article")
    output = gTTS(text = article, lang = language, slow = False)

    print(article)
    print("characters : "  + str(len(article)))

    print("saving article")
    output.save(output_file_name)

except:
    print("script failed to execute, please try again")


