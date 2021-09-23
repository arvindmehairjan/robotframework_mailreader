*** Settings ***
Documentation     A simple example of using a the Mailreader library.
Library           MailReader

*** Test Case ***
Testing Email
    # Sending Emails
    Send Email    message    subject    email_address    recipient    smtp_server    port    password
    
    # Read your last email
    Read The Last Email    username    password
