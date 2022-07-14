
from tkinter import Tk, Label, Button, Entry, OptionMenu, Checkbutton, StringVar, BooleanVar, Text, W, N, NW, DISABLED, NORMAL,END
from constant.variable import METHOD_TYPES
from constant.button_and_text_name import *
from api.request import API;
from json import dumps, loads
from validators import url

class PostMan(Tk):
    def __init__(self):
        super().__init__(className=APPLICATION_TITLE)
        self.__initialApplication();

        self.mainloop();

    def __initialApplication(self):
        self.geometry(APPLICATION_SIZE);
        self.minsize(*tuple(map(lambda x: int(x), APPLICATION_SIZE.split("x"))));

        # API METHOD TYPE
        self.api_method_option = StringVar();
        self.api_method_option.set(GET);
        # TOKEN ENTRY FIELD ENABLE OR DISABLED
        self.token_radio_value = StringVar();
        self.token_radio_value.set(NORMAL);
        # API RESPONSE
        self.api_response_value = StringVar();

        self.__packAndBind(Entry(self, name=URL_ENTRY), row=0, column=0, ipadx=210, ipady=8, pady=10);
        self.__packAndBind(OptionMenu(self, self.api_method_option, *METHOD_TYPES), row=0, column=1);
        self.__packAndBindWithEventListener(event=Button(self, text=EXECUTE, name=BUTTON, bg=GREEN),
                                            function=self.__callAPI, row=0, column=2);

        # FOR TOKEN INPUT FIELD ENABLE OR DISABLE
        self.__packAndBind(Entry(self, name=TOKEN_ENTRY, state=DISABLED), row=1, column=0, ipady=8, ipadx=210);
        self.__packAndBindWithEventListener(
            event=Checkbutton(self, text=TOKEN, variable=self.token_radio_value, onvalue=DISABLED, offvalue=NORMAL,
                              bg=GREEN), function=self.__radioONOFF, row=1, column=1);
        self.__packAndBind(Text(self, name=RESPONSE_TEXT), row=2, column=0);
        self.__packAndBind(
            event=Checkbutton(self, text=APPEND_RESPONSE_DATA, onvalue=DISABLED, offvalue=NORMAL, bg=RED), row=2,
            column=1,sticky=N, pady=25);

    def __packAndBind(self,event,**kwarg)->None:
        event.grid(kwarg);

    def __packAndBindWithEventListener(self,*,event,function,**kwarg)->None:
        self.__bindButtonEvent(event,function);
        self.__packAndBind(event,**kwarg);

    def __bindButtonEvent(self,button,function_name)->None:
        button.bind('<Button-1>',function_name);
        button.bind('<Button-2>', function_name);
        button.bind('<Button-3>', function_name);
        button.bind('<space>', function_name);
        button.bind('<Return>', function_name);
        button.bind('<KP_Enter>', function_name);

    def __callAPI(self,event)->None:
        nameWidget=self.nametowidget;
        url=nameWidget(URL_ENTRY);
        token=nameWidget(TOKEN_ENTRY);
        method=self.api_method_option.get();
        data=loads(nameWidget(RESPONSE_TEXT).get(1.0, END)) if method in METHOD_TYPES[1:-1] else None;
        if self.__validateEntry(url,token,nameWidget(BUTTON),nameWidget(TOKEN_ENTRY)['state']):
            response=API().callApi(url=url.get(), method=method,token=token.get(),data=data);
            nameWidget(RESPONSE_TEXT).insert(END,dumps(response,indent=4));

    def __radioONOFF(self,event)->None:
        self.nametowidget(TOKEN_ENTRY)['state']=self.token_radio_value.get();

    def __validateEntry(self,request_url,token,button,token_entry)->bool:
        flag = True;
        if not url(request_url.get()):
            request_url['highlightbackground']=RED;
            flag = False;
        else:
            request_url['highlightbackground']=GREEN;
        if token_entry==NORMAL and not token.get():
            token['highlightbackground']=RED;
            flag = False;
        elif token_entry==NORMAL:
            token['highlightbackground']=GREEN;
        if not flag:
            button.configure(bg=YELLOW);
            return flag;
        button.configure(highlightbackground=GREEN);
        return flag;



if __name__ =='__main__':
    PostMan();
