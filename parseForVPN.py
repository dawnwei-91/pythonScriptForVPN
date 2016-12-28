#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import re

index=1
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getResult(html):
    regName = r'(\w+\.\w+\.\w+)<'
    comName = re.compile(regName)
    resName = re.findall(comName,html)

    regPort = r'\xe7\xab\xaf\xe5\x8f\xa3:(\d+)</h4'
    comPort = re.compile(regPort)
    resPort = re.findall(comPort,html)

    regPass = r'\xe5\xaf\x86\xe7\xa0\x81:(\d+)</h4'
    comPass = re.compile(regPass)
    resPass = re.findall(comPass,html)
   
   
    return resName, resPort,resPass

def changeLocal(inFo,i=0):
    textLocal=open('C:\Users\Wei\Desktop\gui-config.json','r')
    readText=textLocal.read()
    textLocal.close()

#    print readText
    regName1 = r'"server" : "(\w+\.\w+\.\w+)"'
    comName1 = re.compile(regName1)
    resName1 = re.findall(comName1,readText)

    regPort1 = r'"server_port" : (\d+),'
    comPort1 = re.compile(regPort1)
    resPort1 = re.findall(comPort1,readText)

    regPass1 = r'"password" : "(\d+)"'
    comPass1 = re.compile(regPass1)
    resPass1 = re.findall(comPass1,readText)
#   print resName1, resPort1, resPass1
    text1=readText.replace(resName1[0],inFo[0][i].upper())
    text2=text1.replace(resPort1[0],inFo[1][i])
    text3=text2.replace(resPass1[0],inFo[2][i])
#   print text3
    textHand=open('C:\Users\Wei\Desktop\gui-config.json','w')
    textHand.write(text3)
    textHand.close()


html = getHtml("http://www.ishadowsocks.info/")
inFo = getResult(html)


changeLocal(inFo,index)
