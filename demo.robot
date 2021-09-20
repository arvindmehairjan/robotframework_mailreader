*** Settings ***
Documentation     A simple example of using a the Mailreader library.
Library           MailReader.py

*** Test Case ***
Test Email
    Send Email    test-message    test-subject    email_address    recipient    smtp_server    smtp_port    password
    
