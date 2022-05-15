#Importing modules
import requests
from bs4 import BeautifulSoup
import lxml
from smtplib import SMTP

URL ="https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=bluetooth+speakers&_sacat=0"

headers={
    "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
}

MY_EMAIL ="munasinghehiruka@gmail.com"
PASSWORD ="Google Company"
response = requests.get(url=URL,headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html,"lxml")
#print(soup.prettify())

#Getting the price
heading = soup.find(name="span",class_="s-item__price").getText()
product_price = float(heading.split("$")[1])
print(product_price)


#Sending email
if product_price<25:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:E-bay Alert!\nBluetooth speakers are now available at below $25.\n{URL}"
        )

