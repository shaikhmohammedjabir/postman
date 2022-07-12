
from api.request import API;
from constant.variable import METHOD_TYPES
from constant.button_and_text_name import *
from tkinter import Tk, Label, Button, Entry, OptionMenu, Checkbutton, StringVar, BooleanVar, Text, W, DISABLED, NORMAL


class PostMan(Tk):
    def __init__(self):
        super().__init__(className=" PostMan")
        self.geometry('800x600');

        # API METHOD TYPE
        self.api_method_option=StringVar();
        self.api_method_option.set(GET);
        #TOKEN ENTRY FIELD ENABLE OR DISABLED
        self.token_radio_value=StringVar();


        self.__packAndBind(OptionMenu(self,self.api_method_option,*METHOD_TYPES),row=0,column=0);
        self.__packAndBind(Entry(self),row=0,column=1,ipadx=200,ipady=8,pady=10);
        self.__packAndBindWithEventListener(event=Button(self, text=EXECUTE),function=self.__callAPI,row=0, column=2);
        # self.__bindButtonEvent(execute,self.__callAPI)

        #FOR TOKEN INPUT FIELD ENABLE OR DISABLE
        self.__packAndBind(Label(self,text=TOKEN),row=1,column=0);
        self.__packAndBindWithEventListener(event=Checkbutton(self,variable=self.token_radio_value,onvalue=NORMAL,offvalue=DISABLED),function=self.__radioONOFF,row=1,column=1,sticky=W);
        self.__packAndBind(Entry(self),row=2, column=1,ipady=8,ipadx=200,pady=10,sticky=W);
        self.__packAndBind(Text(self),row=3,column=1,columnspan=3);

        self.mainloop()

    def __packAndBind(self,event,**kwarg):
        event.grid(kwarg)

    def __packAndBindWithEventListener(self,*,event,function,**kwarg):
        self.__bindButtonEvent(event,function)
        event.grid(kwarg)

    def __bindButtonEvent(self,button,function_name):
        button.bind('<Button-1>',function_name);
        button.bind('<Button-2>', function_name);
        button.bind('<Button-3>', function_name);
        button.bind('<space>', function_name);
        button.bind('<Return>', function_name);
        button.bind('<KP_Enter>', function_name);

    def __callAPI(self,event):
        print("api called",event)

    def __radioONOFF(self,event):
        print("radio called",event)

if __name__ =='__main__':
    PostMan();
    # token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMWQwMTg4MzEtNmE2ZC00NDk1LTgyM2YtZDIzYTkzZjBmYjUzIiwicm9sZSI6IkNBTkRJREFURSIsImlhdCI6MTY1NzE3MzIzMSwiZXhwIjoxNjU5NzY1MjMxfQ.9adHISBJFuy2etm8SmHqtHxKPdOcl-CDiMQ0AfmlPYE"
    # api=API()
    # api.callApi(url="http://54.84.50.14:8080/api/v1/candidate/profile", method="GET",token=token)
