import requests
from bs4 import BeautifulSoup
 
r = requests.get('http://www.nytimes.com')
r_html = r.text
soup = BeautifulSoup(r_html)

filename = raw_input("File to save to: ")

with open(filename, 'w') as f:
  for story_heading in soup.find_all(class_="story-heading"): 
      if story_heading.a: 
          f.write(story_heading.a.text.replace("\n", " ").strip())
      else: 
          f.write(story_heading.contents[0].strip())