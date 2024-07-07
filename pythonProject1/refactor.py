import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"
class Email:
    def __init__(self, email, password, subject, recipients, message, header):

        self.email = email
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header


    #send message
    def send_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))

        ms = smtplib.SMTP(GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.email, self.password)
        ms.sendmail(self.email,
                    ms, msg.as_string())

        ms.quit()
        #send end


    #recieve
    def recieve(self):
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self.email, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        self.email.message_from_string(raw_email)
        mail.logout()
        #end recieve
if __name__ == '__main__':

    email_1 = Email(
            email='login@gmail.com',
            password='qwerty',
            subject='Subject',
            recipients=['vasya@email.com', 'petya@email.com'],
            message='Message',
            header=None
            )