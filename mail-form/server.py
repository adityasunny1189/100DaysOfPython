from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sender_email = request.form['sender_email']
        receiver_emails = request.form['receiver_email']
        receiver_email_list = receiver_emails.split(' ')
        sender_password = request.form['sender_password']
        subject = request.form['subject']
        message = request.form['message']
        msg = f'Subject:{subject}\n\n{message}'
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=sender_email, password=sender_password)
            for receiver_email in receiver_email_list:
                connection.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=msg)
            return f'Mail Sent'
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
