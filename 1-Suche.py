# -*- coding: utf-8 -*-
from multiprocessing import Pool
import winsound
import requests
import os
from bs4 import BeautifulSoup

directory = "1-Suche/"
if not os.path.exists(directory):
    os.makedirs(directory)

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43",
    "sec-ch-ua" : "\"Not A;Brand\";v=\"99\" , \"Chromium \";v= \"101\", \"Microsoft Edge \";v= \"101\"" ,
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"

}
def load_zipcode(zipcode):
    filename = str(zipcode) + ".html"
    if not os.path.isfile(directory+filename):
        print(filename)
        """
            "javax.faces.partial.ajax": "true",
            "javax.faces.source": "searchForm:plz",
            "javax.faces.partial.execute": "searchForm:plz",
            "javax.faces.partial.render": "searchForm:distance",
            "javax.faces.behavior.event": "focus",
            "javax.faces.partial.event": "focus",
        """
        payload = {
            "searchForm": "searchForm",
            "searchForm:lastName": "",
            "searchForm:firstName": "",
            "searchForm:location_input": "",
            "searchForm:street": "",
            "searchForm:plz_input": "0" +str(zipcode),
            "searchForm:distance_focus":"",
            "searchForm:distance_input": "-SAXONY-",
            "searchForm:location-postal-combination": "",
            "searchForm:p-common_collapsed": "false",
            "searchForm:specialismRoot": "search.subject.specialismRoot.any",
            "searchForm:specialismDetail:hiddenInput": "beliebig",
            "searchForm:specialismDetail:selectTree_selection": "0",
            "searchForm:additionalName_focus": "",
            "searchForm:additionalName_input": "-UNSELECTED-",
            "searchForm:permittedService:hiddenInput": "beliebig",
            "searchForm:permittedService:selectTree_selection": "0",
            "searchForm:p-subject_collapsed": "false",
            "searchForm:displayEmpowered": "no",
            "searchForm:p-empowerment_collapsed": "true",
            "searchForm:mon:select-mon_input": "on",
            "searchForm:tue:select-tue_input": "on",
            "searchForm:wed:select-wed_input": "on",
            "searchForm:thu:select-thu_input": "on",
            "searchForm:fri:select-fri_input": "on",
            "searchForm:sat:select-sat_input": "on",
            "searchForm:sun:select-sun_input": "on",
            "searchForm:select-all_input": "on",
            "searchForm:morning:select-morning_input": "on",
            "searchForm:afternoon:select-afternoon_input": "on",
            "searchForm:consultationType_focus": "",
            "searchForm:consultationType_input": "-UNSELECTED-",
            "searchForm:p-consultation_collapsed": "true",
            "searchForm:accessibility_focus": "",
            "searchForm:accessibility_input": "-UNSELECTED-",
            "searchForm:foreignLanguage_focus": "",
            "searchForm:foreignLanguage_input": "-UNSELECTED-",
            "searchForm:p-additional_collapsed": "true",
            "searchForm:searchButton": "",
            "javax.faces.ViewState": ""
        }

        s = requests.Session()
        url0 = "https://asu.kvs-sachsen.de/arztsuche/"
        r0 = s.get(url0)
        soup = BeautifulSoup(r0.text, "html.parser")
        inp = soup.find("input", attrs={"name":"javax.faces.ViewState"})
        #print(inp["value"])
        payload["javax.faces.ViewState"] = inp["value"]
        url = "https://asu.kvs-sachsen.de/arztsuche/pages/search.jsf"
        r = s.post(url, data=payload)
        if (r.status_code == 200):
            with open(directory + filename, 'w+') as f:
                #print(r.text)
                f.write(r.text)
        else:
            print("  failed  " + str(r.status_code))



if __name__ == '__main__':
    with open("PLZ_DE.csv", "r") as f:
        zipcodes = [line.replace("\n", "").split(";")[0] for line in f.readlines()[1:]]
    with Pool() as p:
        p.map(load_zipcode, zipcodes)
    winsound.Beep(440, 1000)