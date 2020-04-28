
from selenium import webdriver
from time import sleep
import requests

def login(usr, psw):
        driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(usr)
        driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(psw)
        driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)

def extractLinks(sitelink):
    elems = driver.find_elements_by_xpath("//a[@href]")
    linksLst = []
    for elem in elems:
        linksLst.append(elem.get_attribute("href"))
    return(linksLst)

def checkStatus(el):
    comLinks = []
    errLinks = []

    for l in el:
        if l.startswith("http") or l.startswith("https"):
            res = requests.get(l)
            if res.status_code == 200 :
                comLinks.append([l, res.status_code])
            else:
                errLinks.append([l, res.status_code])
    return (comLinks, errLinks)


sitelink = input("link : ")
loginBool = input("Does login exists (Y/N): ")
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(sitelink)



# if loginBool == "True" or loginBool == "T" or loginBool == "t" or loginBool =="true" or 
if loginBool =="Y" or loginBool =="y":
    usr = input("username : ")
    psw = input("password : ")
    login(usr, psw)
    
extl = extractLinks(sitelink)
cl, errl = checkStatus(extl)