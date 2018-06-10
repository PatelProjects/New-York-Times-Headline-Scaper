import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text.encode("utf-8", "ignore"))

def replaceIt(string1):
    string2 = string1.replace('\\xe2\\x80\\x99', "'"). \
        replace('\\xc3\\xa9', 'e'). \
        replace('\\xe2\\x80\\x90', '-'). \
        replace('\\xe2\\x80\\x91', '-'). \
        replace('\\xe2\\x80\\x92', '-'). \
        replace('\\xe2\\x80\\x93', '-'). \
        replace('\\xe2\\x80\\x94', '-'). \
        replace('\\xe2\\x80\\x94', '-'). \
        replace('\\xe2\\x80\\x98', "'"). \
        replace('\\xe2\\x80\\x9b', "'"). \
        replace('\\xe2\\x80\\x9c', '"'). \
        replace('\\xe2\\x80\\x9c', '"'). \
        replace('\\xe2\\x80\\x9d', '"'). \
        replace('\\xe2\\x80\\x9e', '"'). \
        replace('\\xe2\\x80\\x9f', '"'). \
        replace('\\xe2\\x80\\xa6', '...'). \
        replace('\\xe2\\x80\\xb2', "'"). \
        replace('\\xe2\\x80\\xb3', "'"). \
        replace('\\xe2\\x80\\xb4', "'"). \
        replace('\\xe2\\x80\\xb5', "'"). \
        replace('\\xe2\\x80\\xb6', "'"). \
        replace('\\xe2\\x80\\xb7', "'"). \
        replace('\\xe2\\x81\\xba', "+"). \
        replace('\\xe2\\x81\\xbb', "-"). \
        replace('\\xe2\\x81\\xbc', "="). \
        replace('\\xe2\\x81\\xbd', "("). \
        replace('\\xe2\\x81\\xbe', ")")
        
    return string2
    
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(replaceIt(str(story_heading.a.text.replace("\n", " ").encode("utf-8").strip())).strip('b').strip("'"))
    else: 
        print(replaceIt(str(story_heading.contents[0].encode("utf-8").strip())).strip('b').strip("'"))
        
        
        