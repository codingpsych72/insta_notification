
import smtplib

from smtplib import SMTP
from InstagramAPI import InstagramAPI
username_insta=input("\nenter insta username\n")
password_insta=input("\nenter insta password\n")
username_email=input("\nenter email id\n")
password_email=input("\nenter email password\n")
credentials=InstagramAPI(username_insta,password_insta)
credentials.login()
credentials.getRecentActivity()
get_recent_activity_response=credentials.LastJson

def mail(self):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(username_email, password_email)
    server.sendmail(username_email, username_email, text)

for notifcation in get_recent_activity_response['old_stories']:
    text = notifcation['args']['text']
mail(text)


