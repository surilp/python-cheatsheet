import urllib.request

web_url = urllib.request.urlopen("http://www.google.com")
print(web_url.getcode())
print(web_url.read())

import json

url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

web_url = urllib.request.urlopen(url)
print(web_url.getcode())
data = web_url.read()
print(data)
json_data = json.loads(data)
print(json)

if "title" in json_data["metadata"]:
    print(json_data["metadata"]["title"])

# html parser

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data: str) -> None:
        pass

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        pass

    def handle_data(self, data: str) -> None:
        pass


parser = MyHTMLParser()
with open("file.txt", 'r') as file:
    content = file.read()
    parser.feed(content)  # once feed is called all func in MyHTMLParser is called automatically

# xml
import xml.dom.minidom

doc = xml.dom.minidom.parse("path.xml")
print(doc.nodeName)
print(doc.firstChild.tagName)

skills = doc.getElementsByTagName("skill")
print(skills.length)
for skill in skills:
    print(skill.getAttribute("name"))

# create new tag
newSkill = doc.createElement("skill")
newSkill.setAttribute("name", "jQuery")
doc.firstChild.appendChild(newSkill)
