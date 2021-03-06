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

## License

Copyright (c) 2021 - Arvind Mehairjan

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.