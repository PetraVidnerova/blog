import os.path
import time
import blog

SOURCE = "ril_export.html"
print("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" />")
print("<!-- Source:", SOURCE +
      str(time.ctime(os.path.getmtime(SOURCE))), "-->")

# create list of blog items 
items = []
for line in open(SOURCE):
    line = line.strip()
    if "<li>" in line:
        items.append(blog.item(line))


# create list of categories - pairs (tag, caption) 
CATEGORIES = [] 
with open("category.txt", encoding="utf-8") as cfile:
    for line in cfile:
        line = line.strip() 
        if line:
            words = line.split(None) 
            tag = words[0]
            caption = " ".join(words[1:])
            CATEGORIES.append((tag, caption))


# go through categories and for each tag find 
# corresponding items and print the group 
# with caption 
for tag, caption in CATEGORIES:
    print("<!--", tag, "-->")

    # find all items for the given tag 
    tag_items = (x for x in items if x.tag == tag)
    if not tag_items:
        print("<!-- dneska nic :( -->")
    else:
        # list items 
        print("<b>", caption, "</b>")
        print("<ul>")
        for item in tag_items:
            print(item)
        print("</ul>")
