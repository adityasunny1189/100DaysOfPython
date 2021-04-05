import smtplib

my_email = "aditya9102833743@gmail.com"
my_password = "Adisunny1234"
friend_email = "adityapathak1189@gmail.com"
message = "Subject:Hello\n\nThis is the body of message"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=friend_email, msg=message)
