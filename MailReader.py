from robot.api.deco import keyword, library
import smtplib
from email.message import EmailMessage

@library
class MailReader(object):
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'

    @keyword('Get The Last Email')
    def get_last_email(self, user, password, mailbox, subject):
        """
        Get the subject of the last email of the given account.
        | get_last_email | user=email_adress | password=password | mailbox=mailbox | subject=subject
        """
        enter_credentials = Credentials(user, password)
        account = Account(mailbox, credentials=enter_credentials, autodiscover=True)
        account.inbox.filter(subject__contains=subject)
        for item in account.inbox.filter(subject__contains=subject).order_by('-datetime_received')[
                    :1]:
            return str(item.account), item.to_recipients, item.subject, item.datetime_received.strftime("%d-%m-%Y %H:%M:%S")

    @keyword('Send Email')
    def send_email(self, message, subject, email_address, recipient, smtp_server, port, password):
        msg = EmailMessage()
        msg.set_content(message)

        msg['Subject'] = subject
        msg['From'] = email_address
        msg['To'] = recipient
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.login(email_address, password)
        server.send_message(msg)
        server.close()


    