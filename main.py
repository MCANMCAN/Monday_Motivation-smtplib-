## monday motivation mail if the day of the week is monday "
## You should face some authorization problems due to email provider security issues. please contact me if you would like to test. 
import smtplib 
import random 
import datetime as dt
days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
my_email = input(f"input your gmail address :")      
my_password = input(f"input your password for {my_email} :")
def send_quote_mail(quote) : 
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection :# connects email provider 
        connection.starttls() #starts secure connection 
        connection.login(user=my_email,password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test19931993@yahoo.com",
            msg=f"Subject:{days[0]} Motivation.\n\nQuote of the day :) \n {quote}") 

now = dt.datetime.now()
today = now.weekday()
if today == 0 : 
    with open("quotes.txt") as file:
        lines =[line.rstrip('\n') for line in file.readlines() ] 
    #print(lines)
    quote_no = random.randint(0,len(lines)) 
    send_quote_mail(lines[quote_no])
