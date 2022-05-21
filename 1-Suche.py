# -*- coding: utf-8 -*-
from multiprocessing import Pool
import requests
import os
from bs4 import BeautifulSoup

directory = "1-Suchess/"
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


search_items = {
    "Allgemeinmedizin (fachärztlich tätig)":"1",
    "Allgemeinmedizin/Praktischer Arzt":"2",
    "Anästhesiologie":"3",
    "Angiologie":"4",
    "Ärztliche Psychotherapie und Psychosomatische Medizin":"5",
    "Augenheilkunde":"6",
    "Chirurgie":"7",
    "Endokrinologie und Diabetologie":"8",
    "Fachwissenschaftler":"9",
    "Frauenheilkunde und Geburtshilfe":"10",
    "Gastroenterologie":"11",
    "Gefäßchirurgie":"12",
    "Gynäkologische Endokrinologie und Reproduktionsmedizin":"13",
    "Gynäkologische Onkologie":"14",
    "Hals-Nasen-Ohrenheilkunde":"15",
    "Hämatologie und Onkologie":"16",
    "Hausarzt":"17",
    "Haut- und Geschlechtskrankheiten":"18",
    "Humangenetik":"19",
    "Immunologie":"20",
    "Infektiologie":"21",
    "Innere Medizin (Facharzt)":"22",
    "Innere Medizin (Hausarzt)":"23",
    "Kardiologie":"24",
    "Kinder- und Jugendlichen-Psychotherapie":"25",
    "Kinder- und Jugendmedizin":"26",
    "Kinder- und Jugendpsychiatrie und -psychotherapie":"27",
    "Kinder- und Jugendpsychiatrie":"28",
    "Kinderchirurgie":"29",
    "Kinderendokrinologie und -diabetologie":"30",
    "Kindergastroenterologie":"31",
    "Kinderhämatologie und -onkologie":"32",
    "Kinderkardiologie":"33",
    "Kindernephrologie":"34",
    "Kinderpneumologie":"35",
    "Kinderradiologie":"36",
    "Kinderrheumatologie":"37",
    "Laboratoriumsmedizin":"38",
    "Lungen- und Bronchialheilkunde":"39",
    "Lungenarzt":"40",
    "Mikrobiologie und Infektionsepidemiologie":"41",
    "Mund-Kiefer-Gesichtschirurgie":"42",
    "Neonatologie":"43",
    "Nephrologie":"44",
    "Neurochirurgie":"45",
    "Neurologie":"46",
    "Neuropädiatrie":"47",
    "Nuklearmedizin":"48",
    "Orthopädie und Unfallchirurgie":"49",
    "Orthopädie":"50",
    "Pathologie":"51",
    "Phoniatrie und Pädaudiologie":"52",
    "Physikalische und Rehabilitative Medizin":"53",
    "Physiotherapie":"54",
    "Plastische Chirurgie":"55",
    "Plastische und Ästhetische Chirurgie":"56",
    "Pneumologie":"57",
    "Psychiatrie":"58",
    "Psychologische Psychotherapie":"59",
    "Psychotherapie":"60",
    "Radiologie":"61",
    "Rheumatologie":"62",
    "Spezielle Geburtshilfe und Perinatalmedizin":"63",
    "Sprach-, Stimm und kindliche Hörstörungen":"64",
    "Strahlentherapie":"65",
    "Thoraxchirurgie":"66",
    "Transfusionsmedizin":"67",
    "Unfallchirurgie":"68",
    "Urologie":"69",
    "Visceralchirurgie":"70"
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

        payload2 = {
            "javax.faces.partial.ajax": "true",
            "javax.faces.source": "listForm:tabs:table",
            "javax.faces.partial.execute": "listForm:tabs:table",
            "javax.faces.partial.render": "listForm:tabs:table",
            "listForm:tabs:table": "listForm:tabs:table",
            "listForm:tabs:table_pagination": "true",
            "listForm:tabs:table_first": "0",
            "listForm:tabs:table_rows": "100",
            "listForm:tabs:table_encodeFeature": "false",
            "listForm": "listForm",
            "listForm:tabs_activeIndex": "1",
            "javax.faces.ViewState": ""
        }
        payload3 = {
	        "listForm": "listForm",
	        "listForm:tabs:table:0:showDetail": "",
	        "listForm:tabs_activeIndex": "1",
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
        url1 = "https://asu.kvs-sachsen.de/arztsuche/pages/list.jsf"
        payload2["javax.faces.ViewState"] = inp["value"]
        r = s.post(url1, data = payload2)
        payload2["listForm:tabs:table:0:showDetail"] = ""
        for i in range(0,1):
            #payload3["listForm:tabs_activeIndex"] = str(i)
            r = s.post(url1, data = payload2)
            r = s.get("https://asu.kvs-sachsen.de/arztsuche/pages/detail.jsf")
            filename = filename.replace(".html", "_" + str(i) +".html")
            if (r.status_code >= 0):
                #print(payload2["javax.faces.ViewState"])
                #print(r.text)
                with open(directory + filename, 'w+') as f:
                    #print(r.text)
                    f.write(r.text)
            else:
                print("  failed  " + str(r.status_code))



if __name__ == '__main__':
    with open("PLZ_DE.csv", "r") as f:
        #zipcodes = [line.replace("\n", "").split(";")[0] for line in f.readlines()[1:]]
        zipcodes = ["1099,1129"]
    with Pool() as p:
        p.map(load_zipcode, zipcodes)