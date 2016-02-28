import os.path, time
import blog

source="ril_export.html" 
print("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" />")
print("<!-- Source:",source+str(time.ctime(os.path.getmtime(source))),"-->")


items=[] 
for line in open(source):
    line = line.strip()
    if "<li>" in line:
        items.append(blog.item(line)) 

tags = [ "veda", "skolstvi", "vyzvy", "akce", 
         "ai", "kyber", "robotika", "genetika",
         "mozek", "klima", "pocasi", "tools",
         "ruzne" ] 

names = [ "Věda", "Školství", "Výzvy", "Akce",
          "Umělá inteligence", "Kybernetická bezpečnost", 
          "Robotika", "Genetika",
          "Mozek", "Klimatologie", "Počasí", "Užitečné nástroje",
          "Různé" ] 

for t in range(len(tags)):
    print("<!--",tags[t],"-->")
    tag_items = [ x for x in items if x.tag == tags[t] ] 
    if not tag_items:
        print("<!-- dneska nic :( -->")
    else:
        print("<b>",names[t],"</b>")
        print("<ul>")
        for i in tag_items: print(i) 
        print("</ul>")
