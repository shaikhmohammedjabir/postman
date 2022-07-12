
from api.request import API;
from constant.variable import METHOD_TYPES
from tkinter import Tk, Label, Button, Entry, OptionMenu, Checkbutton, StringVar, BooleanVar, Text, W, DISABLED, NORMAL


class PostMan(Tk):
    def __init__(self):
        super().__init__(className=" PostMan")
        self.geometry('800x600');

        api_method_option=StringVar();

        token_radio_value=StringVar();
        token_radio_value.set(NORMAL);
        api_method_option.set('GET');

        OptionMenu(self,api_method_option,*METHOD_TYPES).grid(row=0,column=0);
        Entry(self).grid(row=0,column=1,ipadx=200,ipady=8);
        Button(self, text="execute", command=lambda: print(token_radio_value.get())).grid(row=0, column=2);

        #FOR TOKEN INPUT FIELD ENABLE OR DISABLE
        Label(self,text="Token").grid(row=1,column=0);
        Checkbutton(self,variable=token_radio_value,onvalue=DISABLED,offvalue=NORMAL,command=lambda:print(token_radio_value)).grid(row=1,column=1,sticky=W);
        # Entry(self,state=token_radio_value).grid(row=2, column=1,ipady=8,ipadx=200,sticky=W);
        Text(self).grid(row=2,column=1,columnspan=3);


        self.mainloop()


if __name__ =='__main__':
    PostMan();
    # token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMWQwMTg4MzEtNmE2ZC00NDk1LTgyM2YtZDIzYTkzZjBmYjUzIiwicm9sZSI6IkNBTkRJREFURSIsImlhdCI6MTY1NzE3MzIzMSwiZXhwIjoxNjU5NzY1MjMxfQ.9adHISBJFuy2etm8SmHqtHxKPdOcl-CDiMQ0AfmlPYE"
    # api=API()
    # api.callApi(url="http://54.84.50.14:8080/api/v1/candidate/profile", method="GET",token=token)