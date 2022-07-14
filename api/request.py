from requests.structures import CaseInsensitiveDict
from requests import request
from json.decoder import JSONDecodeError

class API:
    __OBJECT=None;
    def __new__(cls):
        if(not API.__OBJECT):
            API.__OBJECT=object.__new__(cls)
        return API.__OBJECT

    @property
    def getObject(self):
        return API.__OBJECT

    def callApi(self,*,url:str,method:str,data:str,token:str,count:int=1)->None:
        head=None;
        if token:
            head = CaseInsensitiveDict()
            head["Authorization"] = "Bearer {}".format(token)
            print(head)
        for i in range(count):
            with request(method,url, json=data,headers=head) as response:
                try:
                    return response.json()
                except JSONDecodeError as rje:
                    return rje
