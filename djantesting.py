
from selenium import webdriver
from time import sleep
import requests

def login(usr, psw):
        driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)

def extractLinks(sitelink):
    elems = driver.find_elements_by_xpath("//a[@href]")
    linksLst = []
    for elem in elems:
        linksLst.append(elem.get_attribute("href"))
    print("linksList", linksLst)
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
    print("comLinks", comLinks)
    print("errLinks", errLinks)
    return (comLinks, errLinks)


sitelink = input("link : ")
loginBool = input("Does login exists : ")
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(sitelink)



if loginBool == "True" or loginBool == "T" or loginBool == "t" or loginBool =="true":
    usr = input("username : ")
    psw = input("password : ")
    login(usr, psw)
    
extl = extractLinks(sitelink)
cl, errl = checkStatus(extl)