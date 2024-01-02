#WEB SCRAPING
import pip
pip.main(["install","send2trash"])
pip.main(["install","requests"])
pip.main(["install","lxml"])
pip.main(["install","bs4"])
import requests
import bs4
import lxml
result=requests.get("https://en.wikipedia.org/wiki/AK-47")
#result.text #has the source code
soup=bs4.BeautifulSoup(result.text,"lxml")
#print(soup) #prints the inspect thing
texts=soup.select("p")
#print(texts) #prints the strings with <p>
for x in range(len(texts)):
    print(texts[x].getText())
#soup.select("div") All elements with div tag
#soup.select("#some_id") elements with id some_id
#soup.select('some_class') elements with class some_class
#soup.select('div span')  Elements named span iwthin div
#soup.select('div>span') elements named span within div directly
res=requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup=bs4.BeautifulSoup(res.text,"lxml")
for item in soup.select(".wikitable"):
    print(item.getText())

res= requests.get("https://en.wikipedia.org/wiki/AK-47")
soup=bs4.BeautifulSoup(res.text,"lxml")
print(soup.select(".thumbimage"))
two_gun=soup.select(".thumbimage")[0]
print(two_gun["src"])
image_link=requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/AKMS_and_AK-47_DD-ST-85-01270.jpg/220px-AKMS_and_AK-47_DD-ST-85-01270.jpg")
print(image_link.content) #binary value of image
f=open("guns.jpg","wb")#write binary
f.write(image_link.content)
f.close()

requests.get("http://books.toscrape.com/catalogue/page-1.html")
base_url="http://books.toscrape.com/catalogue/page-{}.html"
res=requests.get(base_url.format(1))
soup=bs4.BeautifulSoup(res.text,"lxml")
products=soup.select(".product_pod")
example=products[0]
print("star-rating Three" in str(example))
print(example.select(".star-rating.Three"))#use dots instead of space
print(example.select("a"))
print(example.select("a")[1]["title"])
two_star=[]
#for n in range(1,51):
#    scrape_url=base_url.format(n)
#    res=requests.get(scrape_url)
#    soup=bs4.BeautifulSoup(res.text,"lxml")
#    books=soup.select(".product_pod")
#    for book in books:
#        if len(book.select(".star-rating.Two"))!=0:
#            two_star.append(book.select("a")[1]["title"])
print(two_star)
