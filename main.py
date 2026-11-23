import os
##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

MY_EMAIL= os.environ.get("MY_EMAIL")
MY_PASSWORD= os.environ.get("MY_PASSWORD")

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now=dt.datetime.now()
day=now.day
month=now.month

birthdays=pd.read_csv("birthdays.csv")
for index, row in birthdays.iterrows():
    if row["month"]==month and row["day"]==day:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letters=["letter_1.txt","letter_2.txt","letter_3.txt"]
        random_letter=random.choice(letters)
        with open(random_letter,"r") as f:
            reader=f.read()
            name_update=reader.replace("[NAME]",row["name"])
            print(name_update)
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com',587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=row["email"],msg=f"Subject: Happy Birthday Sathi!!\n\n{name_update}")





