from __future__ import print_function
import sys
import re
import urllib.request as url
from bs4 import BeautifulSoup

SOURCES = []

# Load sources from file.
with open("sources.txt") as sourcefile:
    for line in sourcefile:
        source, abbrev = line.split(None, 2)
        SOURCES.append(source, abbrev)

DEL_STRINGS = []
with open("del_strings.txt") as delfile:
    for line in delfile:
        line.strip()
        DEL_STRINGS.append(line)


class item:

    def short_source(self, href):
        # Go through sources and return first match.
        for source, abbrev in SOURCES:
            if re.search(source, href):
                return abbrev
        return("?")

    def make_title(self):
        print("Downloading", self.href, file=sys.stderr)
        try:
            webpage = url.urlopen(self.href).read()
            soup = BeautifulSoup(webpage, "lxml")
            self.title = soup.title.string
        except:
            self.title = "no title"

    def reduce_title(self):
        for s in DEL_STRINGS:
            self.title = self.title.replace(s, "")

    def __init__(self, line):
        self.href = re.findall("href=\"(.*?)\"", line)[0]
        self.title = re.findall("<a href=.*>(.*?)</a>", line)[0]
        if "http" in self.title or self.title == "undefined":
            self.make_title()
        self.reduce_title()
        self.tag = re.findall("\ tags=\"(.*?)\"", line)[0]
        self.src = self.short_source(self.href)

    def __str__(self):
        return '<li><a href=\"' + self.href + '\">' + self.title + '</a> <small>(' + self.src + ')</small></li>'
