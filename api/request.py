from requests.structures import CaseInsensitiveDict
from requests import request
from json.decoder import JSONDecodeError
from justext import justext, get_stoplist

class API:
    __OBJECT=None;
    def __new__(cls):
        if(not API.__OBJECT):
            API.__OBJECT=object.__new__(cls)
        return API.__OBJECT

    @property
    def getObject(self):
        return API.__OBJECT

    def callApi(self,*,url:str,method:str,data:str,token:str='',count:int=1)->None:
        head=None;
        if token:
            head = CaseInsensitiveDict()
            head["Authorization"] = "Bearer {}".format(token)
        for i in range(count):
            with request(method,url, json=data,headers=head) as response:
                try:
                    return response.json()
                except JSONDecodeError as rje:
                    html=str(rje)
                    html=html[html.find('<html lang="en">'):html.find('</html>')+8]
                    for i in justext(html,stoplist=get_stoplist("English")):
                        print(i.text)
