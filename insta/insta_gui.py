import kivy
import kivy.app
import kivy.uix.textinput,kivy.uix.boxlayout,kivy.uix.label,kivy.uix.button
import os
from InstagramAPI import InstagramAPI
import smtplib
from smtplib import SMTP
from smtplib import SMTP
# Now access the texture of the label and use it wherever and
# however you may please.


class ggly(kivy.app.App):
    def build(self):
        self.boxy=kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        self.textinput1=kivy.uix.textinput.TextInput(text="enter insta userid")
        self.textinput2 = kivy.uix.textinput.TextInput(text="enter insta password")
        self.textinput3=kivy.uix.textinput.TextInput(text="enter email-id")
        self.textinput4 = kivy.uix.textinput.TextInput(text="enter email password")
        self.butty=kivy.uix.button.Button(text="login")
        self.butty = kivy.uix.button.Button(text="login")
        self.butty.bind(on_press=self.login_me)
        self.boxy.add_widget(self.textinput1)
        self.boxy.add_widget(self.textinput2)
        self.boxy.add_widget(self.textinput3)
        self.boxy.add_widget(self.textinput4)
        self.boxy.add_widget(self.butty)
        return self.boxy
    def login_me(self,name):
        noti=[]
        credentials=InstagramAPI(self.textinput1.text,self.textinput2.text)
        credentials.login()
        credentials.getRecentActivity()
        get_response=credentials.LastJson
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        uname=self.textinput3.text
        passwrd=self.textinput4.text
        server.login(uname,passwrd)
        for notification in get_response['old_stories']:
            info=notification['args']['text']
        server.sendmail(uname,uname,info)
        print("completed")




if __name__=="__main__":
    a=ggly()
    a.run()
