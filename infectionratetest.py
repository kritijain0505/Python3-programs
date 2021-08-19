import os
import webscraping as wp
import pywhatkit
import smtplib
import requests
from bs4 import BeautifulSoup
clear = lambda: os.system('cls')
clear()
count=int(0)


print("\n\n ******************** INFECTION RATE TEST ********************* ")
print('\t\t\t\t\t\t\t By Kriti')
wp.get_covid_data()
print("\n\n FILL YOUR BASIC DATEILS :-")
name=input("\n\t Please enter your name  :- ")
age=int(input("\t Please Enter your age :-"))
if age<=13 or age>=50 :
    count +=1
fage=str(age)
gender=input("\t Please enter your gender (M/F) :-")
address=input("\t Please enter your address :- ")
mphone=input("\t Please enter your Contact number :- ")
fphone=str("+91"+mphone)
yemail=input("\t Please enter your email :- ")
print("\n\n\t Thank you for responding ")
clear = lambda: os.system('cls')
clear()
print("\n\n ******************** INFECTION RATE TEST ********************* ")
print('\t\t\t\t\t\t\t By Kriti')
print("Plese enter your some medical details :- ")
temp=int(input("\t Plese enter your Body temperature(in C ) :- "))
if temp>=38 :
    count +=1
bp=int(input("\t Please enter your Blood Pressure(in mmHg ) :- "))
if bp>=129 :
    count +=1
oxy=int(input("\t Please enetr your Oxygen saturation(in % ) :- "))
if oxy<=70 :
    count +=1
sug=int(input("\t Plese enter your last suger report(in mg/dL ) :- "))
if sug>=140 :
    count +=1
ques=input("\t If getting smell & taste press'Y' or if not press'N' :- ")
if(ques=='n' or ques=='N'):
    count +=1
mhis=input("\t Please enter any medical histry if no press 'N' :- ")
print(" \n\n Now answer few question correctly :- ")
que1=input("\t Do you have any travel history across INDIA between jan to mar?(y/n)\n Ans:-")
if(que1=='y' or que1=='Y'):
    count +=1

que2=input("\t Do you came in contact with any covid infected parson?(y/n)\nAns:- ")
if(que2=='y' or que2=='Y'):
    count +=1
que3=input("\t Is there any covid patient in the range of 1 km?(y/n)\nAns:-  ")
if(que3=='y' or que3=='Y'):
    count +=1
que4=input("\t Are you suffering of any kind of diseases like CANCER,DIABETES or LUNGS DISEASES?(y/n)\nAns:- ")
if(que4=='y' or que4=='Y'):
    count +=1
que5=input("\t If you are suffering from any one write y\n\t1) Dry cough \n\t2) Shortness of breath \n\t3) Headaches \n\t4) Aches and Pains \n\t5) Sore throat \n\t6) fatigue \n\t7) Diarrhea  \nAns:- ")
if(que5=='y' or que5=='Y'):
    count +=1

report=float(count*float(9.09091))
freport=str(report)

messgae="--------------------------------REPORT-----------------------------\n\n \t NAME = "+ name + "\t\t AGE = " + fage + "\t GENDER =  " + gender + "\n \t CONTACT NO = " + mphone +"\t\t ADDRESS = " + address +"\n\n \t Your rate of infection is "+ freport +"\n\n STAY SAFE PLEASE WHERE A MASK AND MAINTAIN SOCIAL DSTANCING \n\n Test done by Kriti "
print (messgae)
print(" ENETR THE CORRECT CHOICE  /n \t 1. Send report through WhatsApp  2. Through Email ")
x=int(input("Option :-  "))
if (x==1):
    print("ENTER THE TIME AT WHICH YOU WANT TO SEND THE MESSAGE :- ")
    hour=int(input("Enter the Hour( in 24 format ):-  "))
    minu=int(input("Enter the minute :-  "))
    pywhatkit.sendwhatmsg(fphone,messgae,hour,minu,10,'true','chrome')
    print(" MESSAGE SUCCESFULLY SENT ")
#if(x==2):
   #server.login("btrendy19@gmail.com","Trendy2020@")
   # server.sendmail("btrendy19@gmail.com","harsola.kriti29@gmail.com",messgae)
   # server.quit()

else:
    os._exit(0)

print("THANK YOU FOR USING KRITI TESTING TOOL ")