from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

page = urllib.request.urlopen("https://www.flipkart.com/search?q=iphone%2013&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

soup = BeautifulSoup(page, "html.parser")

P_Name = []
P_Price = []
P_Rating = []
P_Features = []

for i in soup.findAll("div", class_="_3pLy-c row"):
    get_Product_Name = i.find("div", attrs={"class": "_4rR01T"})
    get_Price = i.find("div", attrs={"class": "_30jeq3 _1_WHN1"})
    get_Rating = i.find("div", attrs={"class": "_3LWZlK"})
    get_Features = i.find("div", attrs={"class": "fMghEO"})
    P_Name.append(get_Product_Name.text)
    P_Price.append(get_Price.text)
    P_Rating.append(get_Rating.text)
    P_Features.append(get_Features.text)

Data = pd.DataFrame({'Product Name': P_Name, 'Price': P_Price, 'Rating': P_Rating, 'Features': P_Features})

print(Data.head())
Data.to_csv("Results.csv")