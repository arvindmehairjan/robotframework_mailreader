# robotframework_mailreader

This is a library for Robot Framework to read the last mail of your inbox and to send emails.

## Installation

You can install the Robot Framework library by running the following command:

<code>pip install robotframework-mailreader</code>

## Usage

Below you find an example how you can use the library:

```
*** Settings ***
Documentation     A simple example of using a the Mailreader library.
Library           MailReader

*** Test Case ***
Testing Email
    # Sending Emails
    Send Email    message    subject    email_address    recipient    smtp_server    port    password
    
    # Read your last email
    Read The Last Email    email_address    password
```
