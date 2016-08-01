from __future__ import print_function
import sys
import re
import urllib.request as url
from bs4 import BeautifulSoup

SOURCES = []
DEL_STRINGS = [] 

# Load sources from file.
with open("sources.txt", encoding="utf-8") as sourcefile:
    for line in sourcefile:
        source, abbrev = line.split(None, 2)
        SOURCES.append((source, abbrev))

with open("del_strings.txt", encoding="utf-8") as delfile:
    for line in delfile:
        DEL_STRINGS.append(line.strip())
        


class item:

    def __init__(self, line):
        """ Extract href, title, tag and source. """

        self.href = re.findall(r'href="(.*?)"', line)[0]
        self.title = re.findall(r'<a href=.*>(.*?)</a>', line)[0]

        if "http" in self.title or self.title == "undefined":
            self.make_title()

        self.reduce_title()

        self.tag = re.findall(r' tags="(.*?)"', line)[0]
        self.src = self.short_source()



    def short_source(self):
        """ Go through sources and return first match. """

        for source, abbrev in SOURCES:
            if re.search(source, self.href):
                return abbrev
        return("?")


    def make_title(self):
        """ Download the webpage and extract title. """

        print("Downloading", self.href, file=sys.stderr)
        try:
            webpage = url.urlopen(self.href).read() 
            soup = BeautifulSoup(webpage, "lxml")

            # extract encoding from <meta charset=".*"/>  
            #encoding = soup.findAll("meta", attrs={"charset" : re.compile(".*")})[0].get("charset")
            
            self.title = soup.title.string

        except:
            self.title = "no title"


    def reduce_title(self):
        """ Delete the extra stuff from title. """

        for s in DEL_STRINGS:
            self.title = self.title.replace(s, "")


    def __str__(self):
        return '<li><a href=\"' + self.href + '\">' + self.title + '</a> <small>(' + self.src + ')</small></li>'
