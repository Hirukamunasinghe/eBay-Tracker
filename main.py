#Importing modules
import requests
from bs4 import BeautifulSoup
import lxml
from smtplib import SMTP

URL ="https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=bluetooth+speakers&_sacat=0"
headers ={
    "Authorization":"Bearer <accessToken>",
    "Accept-Encoding":"application/gzip",
    "Accept-Language":"fr-CA",
    "Accept-Charset":"utf-8",
    "X-EBAY-C-MARKETPLACE-ID":"EBAY_US",
    "X-EBAY-C-ENDUSERCTX":"affiliateCampaignId=<ePNCampaignId>,"
                          "affiliateReferenceId=<referenceId>,"
                          "contextualLocation=country=<2-digitCountryCode>,"
                          "zip=<zipCode>,"
                          "deviceId=<riskCorrelationId>"
}
MY_EMAIL ="munasinghehiruka@gmail.com"
PASSWORD ="Google Company"
response = requests.get(headers=headers,url=URL)
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

