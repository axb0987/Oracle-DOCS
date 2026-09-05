# Integrating Python with Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/python.htm
- Fetched: 2026-09-05 02:01 CDT

# Integrating Python with Email Delivery

Use Python to send emails through the Email Delivery service.

You can use Python to send emails through Email Delivery. Before you can send email you must configure Email Delivery in Python.

Important  
  
These instructions contain sample code for your convenience and should be used as a reference. For client support, you must contact Python. These steps were tested on an Oracle Linux Server release 7.9 compute instance and Python 3.6. These steps assume you are logged into an Oracle Linux instance. Other distributions of Linux may have different commands and file locations. Java applications (including JavaMail) must be updated to the latest version to ensure that the latest protocols, ciphers, and security patches are in compliance with Oracle's supported security policies and ciphers.

## Configure Python to Send Email Through Email Delivery

To enable Python to test the configuration of Email Delivery:
- Ensure Email Delivery is configured to send email. See[Getting Started](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted.htm).
Note  
  
The SMTP credentials are required to configure Python to use Email Delivery. Be sure to note the user name and password when you generate the SMTP credentials.
- Ensure Python is installed. The installation process differs depending on which operating system you are using. For example, run the following command to install Python on Oracle Linux:
```

```

- In a file editor such as vi, create a python script to test Email Delivery.

Run the following command:
```

```

- In the ociemail.py file, replace the variables with your own values.
For example:
```

```

Note  
  

- To use Python with port 25 or 587, change`smtplib.SMTP_SSL(HOST, PORT)`to`smtplib.SMTP(HOST, PORT)`.
- Python 2 and legacy email APIs should not be used with Email Delivery.
- In a file editor such as vi, create a file that contains the SMTP password. Run the following command and replace the contents with your SMTP password:
```

```

- To send a test email with Python, run the following command from the directory the script is located in:

```

```

## More Information

More Python script examples can be found on[GitHub](https://github.com/oracle/oci-python-sdk/blob/master/examples/email_service_example.py)
