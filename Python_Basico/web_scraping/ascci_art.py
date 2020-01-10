# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

b_url="http://artii.herokuapp.com/"

def fonts():
    fuentes=[]
    r=requests.get("http://artii.herokuapp.com/fonts_list")
    if r.status_code != 200:
        return f"Error: {r.status_code}: {r.text}"
    else:
        soup=BeautifulSoup(r.content, "html.parser")
        t=soup.get_text().split("\n")
        for i in t:
            fuentes.append(i)
    return fuentes

def asciify(text, font=None):
    f_text=text.split(" ")
    f_text="+".join(f_text)
    if font:
        url_ext=f"make?text={f_text}&font={font}"
    else:
        url_ext=f"make?text={f_text}"
    r=requests.get(b_url + url_ext)
    if r.status_code != 200:
        return f"Error: {r.status_code}: {r.text}"
    return r.text

def run():
    while True:
        texto=str(input("INTRODUZCA EL TEXTO A CONVERTIR: "))
        fon=fonts()
        for i in range(len(fon)):
            print(asciify(texto, fon[i]))
        break

if __name__=="__main__":
    run()