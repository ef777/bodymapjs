# Importing all the required modules
from cgi import print_form
import http
from http.client import HTTPResponse
import json
from this import d
import time
from urllib.request import Request
from flask import (
    Flask,
    flash,
    request,
    redirect,
    url_for,
    render_template,
    abort
)
from bs4 import BeautifulSoup

import re 
import requests


app = Flask(__name__,
            static_folder='/home/lystra/Belgeler/body/static',
            template_folder='/home/lystra/Belgeler/body/templates')


@app.route("/", methods=["GET", "POST"])
def sorgusa():
    return render_template("index.html")


@app.route("/dataa", methods=["GET", "POST"])
def sorgula2():
    symptomWarning = request.form.get('symptomWarning')
    distributionHasQuestion = request.form.get('distributionHasQuestion')
    distributionId = request.form.get('distributionId')
    distributionSeverity = request.form.get('distributionSeverity')
    locId = request.form.get('locId')
    locName = request.form.get('locName')
    locParentId = request.form.get('locParentId')
    symptomName = request.form.get('symptomName')
    gelen=data2(symptomName=symptomName,locParentId=locParentId,locName=locName,locId=locId,distributionSeverity=distributionSeverity,distributionId=distributionId,distributionHasQuestion=distributionHasQuestion,symptomWarning=symptomWarning)
    print("Data type before reconstruction : ", type(gelen))
    gelen=Welcome6(True,gelen)
    result = welcome1_from_dict(json.loads(gelen.data))
    belirti= result.data[0].belirtiler
    brans= result.data[0].branch
    isim= result.data[0].name
    word=result.data[0].fore_word
    tablo2=result.data[0].tabular_group_code2
    tablo1=result.data[0].tabular_group_name1
    icd=result.data[0].icd_name
    tablo3=result.data[0].tabular_group_name3



    return render_template("index2.html", belirti=belirti,brans=brans,isim=isim,word=word,tablo2=tablo2,tablo1=tablo1,icd=icd,tablo3=tablo3)


@app.route("/data", methods=["GET", "POST"])
def sorgula():
    data = request.args.get('data')
    gelen=dataal(data)
    print("Data type before reconstruction : ", type(gelen))
    root = Root.from_dict(gelen)
    return render_template("index.html", data=root.data)
   

    

def dataal(a):

    import requests
    cookies = {
        'sid': 'c146d0cba71968fed5165cbbc0141e92',
        '_ga': 'GA1.2.422701626.1663604409',
        '_gid': 'GA1.2.1315639227.1663604409',
        '_gat': '1',
    }
    
    headers = {
        'authority': 'medulus.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'tr-TR,tr;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'sid=c146d0cba71968fed5165cbbc0141e92; _ga=GA1.2.422701626.1663604409; _gid=GA1.2.1315639227.1663604409; _gat=1',
        'origin': 'https://medulus.io',
        'referer': 'https://medulus.io/',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    
    json_data = {
        'robot': {
            'user': {
                'history': [],
                'info': {
                    'loc': '0,0',
                },
            },
            'session': '2e66c9ef-dd95-4493-be6a-c96ebc34b5c8',
            'body': {
                'age': 29,
                'sex': 'm',
                'hei': 185,
                'wei': 85,
            },
            'symptoms': [],
            'results': [],
            'alerts': [],
        },
        'q': a,
    }

    response = requests.post('https://medulus.io/api/symptom', cookies=cookies, headers=headers, json=json_data)
    jsonstring = json.loads(response.content)
   # print(jsonstring)
   # print("sonuc")
    return jsonstring



from typing import List
from typing import Any
from dataclasses import dataclass
@dataclass
class Datum:
    distributionHasQuestion: int
    distributionId: str
    distributionSeverity: str
    locId: str
    locName: str
    locParentId: str
    symptomName: str
    symptomWarning: str

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        _distributionHasQuestion = int(obj.get("distributionHasQuestion"))
        _distributionId = str(obj.get("distributionId"))
        _distributionSeverity = str(obj.get("distributionSeverity"))
        _locId = str(obj.get("locId"))
        _locName = str(obj.get("locName"))
        _locParentId = str(obj.get("locParentId"))
        _symptomName = str(obj.get("symptomName"))
        _symptomWarning = str(obj.get("symptomWarning"))
        return Datum(_distributionHasQuestion, _distributionId, _distributionSeverity, _locId, _locName, _locParentId, _symptomName, _symptomWarning)

@dataclass
class Root:
    data: List[Datum]
    success: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _data = [Datum.from_dict(y) for y in obj.get("data")]
        _success = True
        return Root(_data, _success)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)


#ikinci 

def data2  (distributionHasQuestion, distributionId, distributionSeverity, locId, locName, locParentId, symptomName, symptomWarning):
    import requests
    
    cookies = {
        'sid': '55cae254cf721a7a41632631123efa15',
        '_ga': 'GA1.2.216436767.1663614887',
        '_gid': 'GA1.2.1517082891.1663614887',
        '_gat': '1',
        'robot': '%7B%22user%22%3A%7B%22history%22%3A%5B%22ayak%22%5D%2C%22info%22%3A%7B%22loc%22%3A%220%2C0%22%7D%7D%2C%22session%22%3A%22e6b85780-b6a3-6e57-b9bf-1e39d4c8b760%22%2C%22body%22%3A%7B%22age%22%3A29%2C%22sex%22%3A%22m%22%2C%22hei%22%3A185%2C%22wei%22%3A85%7D%2C%22symptoms%22%3A%5B%7B%22sym%22%3A%7B%22distributionId%22%3A%22q9m0Wd5v%22%2C%22locId%22%3A%22NgG5w2yV%22%2C%22locParentId%22%3A%22QdW8pOmK%22%2C%22distributionHasQuestion%22%3A1%2C%22distributionSeverity%22%3A%22%22%2C%22locName%22%3A%22A%u015Filtendonlar%22%2C%22symptomName%22%3A%22%u015Ei%u015Fme%20-%20A%u015Filtendonlar%22%2C%22symptomWarning%22%3A%22%22%2C%22questions%22%3A%5B%7B%22questionId%22%3A%229J3y1B5L%22%2C%22questionSymptomId%22%3A%22%22%2C%22questionLocId%22%3A%22%22%2C%22questionText%22%3A%22Buz%20uygulad%u0131%u011F%u0131n%u0131zda%20iniyor%20mu%3F%22%2C%22questionType%22%3A%22YN%22%2C%22questionYesValue%22%3A327%2C%22questionNoValue%22%3A0%2C%22questionYesWarning%22%3A%22%22%2C%22questionNoWarning%22%3A%22%22%7D%5D%7D%7D%5D%2C%22results%22%3A%5B%5D%2C%22alerts%22%3A%5B%5D%7D',
    }
    
    headers = {
        'authority': 'medulus.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'tr-TR,tr;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'sid=55cae254cf721a7a41632631123efa15; _ga=GA1.2.216436767.1663614887; _gid=GA1.2.1517082891.1663614887; _gat=1; robot=%7B%22user%22%3A%7B%22history%22%3A%5B%22ayak%22%5D%2C%22info%22%3A%7B%22loc%22%3A%220%2C0%22%7D%7D%2C%22session%22%3A%22e6b85780-b6a3-6e57-b9bf-1e39d4c8b760%22%2C%22body%22%3A%7B%22age%22%3A29%2C%22sex%22%3A%22m%22%2C%22hei%22%3A185%2C%22wei%22%3A85%7D%2C%22symptoms%22%3A%5B%7B%22sym%22%3A%7B%22distributionId%22%3A%22q9m0Wd5v%22%2C%22locId%22%3A%22NgG5w2yV%22%2C%22locParentId%22%3A%22QdW8pOmK%22%2C%22distributionHasQuestion%22%3A1%2C%22distributionSeverity%22%3A%22%22%2C%22locName%22%3A%22A%u015Filtendonlar%22%2C%22symptomName%22%3A%22%u015Ei%u015Fme%20-%20A%u015Filtendonlar%22%2C%22symptomWarning%22%3A%22%22%2C%22questions%22%3A%5B%7B%22questionId%22%3A%229J3y1B5L%22%2C%22questionSymptomId%22%3A%22%22%2C%22questionLocId%22%3A%22%22%2C%22questionText%22%3A%22Buz%20uygulad%u0131%u011F%u0131n%u0131zda%20iniyor%20mu%3F%22%2C%22questionType%22%3A%22YN%22%2C%22questionYesValue%22%3A327%2C%22questionNoValue%22%3A0%2C%22questionYesWarning%22%3A%22%22%2C%22questionNoWarning%22%3A%22%22%7D%5D%7D%7D%5D%2C%22results%22%3A%5B%5D%2C%22alerts%22%3A%5B%5D%7D',
        'origin': 'https://medulus.io',
        'referer': 'https://medulus.io/',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    
    json_data = {
        'user': {
            'history': [
                'ayak',
            ],
            'info': {
                'loc': '0,0',
            },
        },
        'session': 'e6b85780-b6a3-6e57-b9bf-1e39d4c8b760',
        'body': {
            'age': 29,
            'sex': 'm',
            'hei': 185,
            'wei': 85,
        },
        'symptoms': [
            {
                'sym': {
                    'distributionId': distributionId,
                    'locId': locId,
                    'locParentId': locParentId,
                    'distributionHasQuestion': distributionHasQuestion,
                    'distributionSeverity': distributionSeverity,
                    'locName': locName,
                    'symptomName': symptomName,
                    'symptomWarning': symptomWarning,
                    'questions': [],
                },
         
            },
        ],
        'results': [],
        'alerts': [],
    }
    
    response = requests.post('https://medulus.io/api/examination', cookies=cookies, headers=headers, json=json_data)
    return response.content


    # To use this code, make sure you
#
#   import json
#
#ad then, to convert JSON from a string, do
#
#   result = welcome6_from_dict(json.loads(json_string))

from typing import List


class Datume:
    id: str
    weight: float
    name: str
    branch: str
    tabular_group_code1: str
    tabular_group_code2: str
    tabular_group_code3: str
    tabular_group_name1: str
    tabular_group_name2: str
    tabular_group_name3: str
    icd_code: str
    icd_name: str
    fore_word: None
    belirtiler: str

    def __init__(self, id: str, weight: float, name: str, branch: str, tabular_group_code1: str, tabular_group_code2: str, tabular_group_code3: str, tabular_group_name1: str, tabular_group_name2: str, tabular_group_name3: str, icd_code: str, icd_name: str, fore_word: None, belirtiler: str) -> None:
        self.id = id
        self.weight = weight
        self.name = name
        self.branch = branch
        self.tabular_group_code1 = tabular_group_code1
        self.tabular_group_code2 = tabular_group_code2
        self.tabular_group_code3 = tabular_group_code3
        self.tabular_group_name1 = tabular_group_name1
        self.tabular_group_name2 = tabular_group_name2
        self.tabular_group_name3 = tabular_group_name3
        self.icd_code = icd_code
        self.icd_name = icd_name
        self.fore_word = fore_word
        self.belirtiler = belirtiler


class Welcome6:
    success: bool
    data: List[Datume]
    def __init__(self, success: bool, data: List[Datume]) -> None:
        self.success = success
        self.data = data





# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome1_from_dict(json.loads(json_string))

from enum import Enum
from typing import Optional, Any, List, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str2(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float2(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_none2(x: Any) -> Any:
    assert x is None
    return x


def from_union2(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_float2(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_enum2(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_bool2(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list2(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class2(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Belirtiler(Enum):
    BAŞ_BAŞAĞRISI = "Baş; Başağrısı"
    BEL_AĞRISI = "Bel; Ağrısı"


class Datumi:
    id: str
    weight: float
    name: str
    branch: Optional[str]
    tabular_group_code1: Optional[str]
    tabular_group_code2: Optional[str]
    tabular_group_code3: Optional[str]
    tabular_group_name1: Optional[str]
    tabular_group_name2: Optional[str]
    tabular_group_name3: Optional[str]
    icd_code: Optional[str]
    icd_name: Optional[str]
    fore_word: None
    belirtiler:  Optional[str]

    def __init__(self, id: str, weight: float, name: str, branch: Optional[str], tabular_group_code1: Optional[str], tabular_group_code2: Optional[str], tabular_group_code3: Optional[str], tabular_group_name1: Optional[str], tabular_group_name2: Optional[str], tabular_group_name3: Optional[str], icd_code: Optional[str], icd_name: Optional[str], fore_word: None, belirtiler: Optional[str] ) -> None:
        self.id = id
        self.weight = weight
        self.name = name
        self.branch = branch
        self.tabular_group_code1 = tabular_group_code1
        self.tabular_group_code2 = tabular_group_code2
        self.tabular_group_code3 = tabular_group_code3
        self.tabular_group_name1 = tabular_group_name1
        self.tabular_group_name2 = tabular_group_name2
        self.tabular_group_name3 = tabular_group_name3
        self.icd_code = icd_code
        self.icd_name = icd_name
        self.fore_word = fore_word
        self.belirtiler = belirtiler

    @staticmethod
    def from_dict2(obj: Any) -> 'Datumi':
        assert isinstance(obj, dict)
        id = from_str2(obj.get("id"))
        weight = from_float2(obj.get("weight"))
        name = from_str2(obj.get("name"))
        branch = from_union2([from_none2, from_str2], obj.get("branch"))
        tabular_group_code1 = from_union2([from_none2, from_str2], obj.get("tabularGroupCode1"))
        tabular_group_code2 = from_union2([from_none2, from_str2], obj.get("tabularGroupCode2"))
        tabular_group_code3 = from_union2([from_none2, from_str2], obj.get("tabularGroupCode3"))
        tabular_group_name1 = from_union2([from_none2, from_str2], obj.get("tabularGroupName1"))
        tabular_group_name2 = from_union2([from_none2, from_str2], obj.get("tabularGroupName2"))
        tabular_group_name3 = from_union2([from_none2, from_str2], obj.get("tabularGroupName3"))
        icd_code = from_union2([from_none2, from_str2], obj.get("icdCode"))
        icd_name = from_union2([from_none2, from_str2], obj.get("icdName"))
        fore_word = from_none2(obj.get("foreWord"))
        belirtiler = from_str2(obj.get("belirtiler"))
        return Datumi(id, weight, name, branch, tabular_group_code1, tabular_group_code2, tabular_group_code3, tabular_group_name1, tabular_group_name2, tabular_group_name3, icd_code, icd_name, fore_word, belirtiler)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str2(self.id)
        result["weight"] = to_float2(self.weight)
        result["name"] = from_str2(self.name)
        result["branch"] = from_union2([from_none2, from_str2], self.branch)
        result["tabularGroupCode1"] = from_union2([from_none2, from_str2], self.tabular_group_code1)
        result["tabularGroupCode2"] = from_union2([from_none2, from_str2], self.tabular_group_code2)
        result["tabularGroupCode3"] = from_union2([from_none2, from_str2], self.tabular_group_code3)
        result["tabularGroupName1"] = from_union2([from_none2, from_str2], self.tabular_group_name1)
        result["tabularGroupName2"] = from_union2([from_none2, from_str2], self.tabular_group_name2)
        result["tabularGroupName3"] = from_union2([from_none2, from_str2], self.tabular_group_name3)
        result["icdCode"] = from_union2([from_none2, from_str2], self.icd_code)
        result["icdName"] = from_union2([from_none2, from_str2], self.icd_name)
        result["foreWord"] = from_none2(self.fore_word)
        result["belirtiler"] = to_enum2(Belirtiler, self.belirtiler)
        return result


class Welcome1:
    success: bool
    data: List[Datumi]

    def __init__(self, success: bool, data: List[Datumi]) -> None:
        self.success = success
        self.data = data

    @staticmethod
    def from_dict2(obj: Any) -> 'Welcome1':
        assert isinstance(obj, dict)
        success = from_bool2(obj.get("success"))
        data = from_list2(Datumi.from_dict2, obj.get("data"))
        return Welcome1(success, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["success"] = from_bool2(self.success)
        result["data"] = from_list2(lambda x: to_class2(Datumi, x), self.data)
        return result


def welcome1_from_dict(s: Any) -> Welcome1:
    return Welcome1.from_dict2(s)


def welcome1_to_dict(x: Welcome1) -> Any:
    return to_class2(Welcome1, x)
