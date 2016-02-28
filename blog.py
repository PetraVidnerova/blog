from __future__ import print_function
import sys
import re 
import urllib.request as url 
from bs4 import BeautifulSoup

class item:

    def short_source(self,href):
        sources = [ ("sciencebusiness","sciencebusiness"), 
                    ("metodikahodnoceni.blogspot.cz","Daniel Műnich"),
                    ("ceskapozice","ceskapozice"), 
                    ("czelo","czelo"), 
                    ("tacr","tacr"), 
                    ("vyzkum.cz","vyzkum.cz"),
                    ("iforum","iFORUM"), 
                    ("vesmir","Vesmir"), 
                    ("www.cas.cz","cas.cz"), 
                    ("technet.idnes","technet"),
                    ("zpravy.idnes","iDNES"),
                    ("abicko.avcr","AkaBullet"),
                    ("ihned","HN"),
                    ("rozhlas.cz/meteor","meteor"),
                    ("ceskenoviny","ČN"),
                    ("data.avcr","avcr"),
                    ("patecnici","Pátečníci"),
                    ("zive.cz","živě"),
                    ("popsci","popsci"),
                    ("rozhlas.cz","rozhlas"),
                    ("neuroskeptic","neuroskeptic"),
                    ("technologyreview","technologyreview"),
                    ("mff.cuni.cz","MFF"),
                    ("gacr.cz","GAČR"),
                    ("vedazije.cz","vedazije"),
                    ("ssc.cas.cz","ssc.cas"),
                    ("discovery.com","discovery"),
                    ("blog.oup.com","blog.oup"),
                    ("mit.edu","MIT News"),
                    ("it4i.cz","it4i"),
                    ("jcmf.cz","jcmf"),
                    ("denik.cz","Deník.cz"),
                    ("reuters.com","reuters"),
                    ("nature.com","nature"),
                    ("discovermagazine.com","discovermagazine"),
                    ("nationalgeographic","NationalGeographic"),
                    ("lidovky.cz","lidovky"),
                    ("salon.com","salon.com"),
                    ("geekwire.com","geekwire"),
                    ("washingtonpost.com","WashingtonPost"),
                    ("dispatch.com","dispatch.com"),
                    ("huffingtonpost.com","HuffingtonPost"),
                    ("computerweekly.com","computerweekly"),
                    ("britishcouncil","BritishCouncil"),
                    ("msmt","MŠMT"), 
                    ("vtm","vtm"),
                    ("avobloguje","AVObloguje"),
                    ("pitt.edu","pitt.edu"),
                    ("sciencenews.org","sciencenews") ]
        # Go through sources and return first match. 
        for s in sources:
            if re.findall(s[0],href): return s[1] 
        return("?")

    def make_title(self):
        print("Downloading",self.href,file=sys.stderr)
        webpage = url.urlopen(self.href).read()
        soup = BeautifulSoup(webpage,"lxml") 
        self.title = soup.title.string  

    def reduce_title(self):
        del_strings = [ "| AVObloguje", "| Nationality Rooms", "| University of Pittsburgh",
                        "- iDNES.cz", "- Živě.cz", "- Science News", "| Meteor", "| Popular Science" 
                        "| CZELO | Česká styčná kancelář pro výzkum, vývoj"        ] 
        for s in del_strings:
            self.title = self.title.replace(s,"") 

    def __init__(self,line):
        self.href = re.findall("href=\"(.*?)\"",line)[0] 
        self.title = re.findall("<a href=.*>(.*?)</a>",line)[0] 
        if "http" in self.title:
            self.make_title()
        self.reduce_title() 
        self.tag =  re.findall("\ tags=\"(.*?)\"",line)[0]
        self.src = self.short_source(self.href) 

    def __str__(self):
        return '<li><a href=\"'+self.href+'\">'+self.title+'</a> <small>('+self.src+')</small></li>'

