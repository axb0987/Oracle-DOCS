# Integrating Sendmail with Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/sendmail.htm
- Fetched: 2026-09-05 02:01 CDT

# Integrating Sendmail with Email Delivery

Use Sendmail to send emails through the Email Delivery service.

## Configure Sendmail to Send Email Through Email Delivery

Sendmail is a general purpose internetwork email routing facility that supports many kinds of mail-transfer and delivery methods, including the Simple Mail Transfer Protocol used for email transport over the Internet. You can use Sendmail to send emails through Email Delivery. Before you use Sendmail you must configure Oracle Cloud Infrastructure Email Delivery in your Sendmail application.
Important  
  
These instructions contain sample code for your convenience and should be used as a reference. For client support, you must contact Sendmail customer support.
Note  
  

The steps below are for configuring Sendmail to send email through Oracle Cloud Infrastructure Email Delivery. These steps were tested on an Oracle Linux Server release 7.9 compute instance and Sendmail-8.14.7-6.el7.x86_64.

To enable Sendmail to integrate with Email Delivery:
- 

Make sure Email Delivery is configured to send email. See[Getting Started](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted.htm).
Note  
  

SMTP credentials are required to configure Sendmail to use Email Delivery. Be sure to note the user name and password when you generate the SMTP credentials.
- 

Run the following update and install commands:
```

```

- 

Update`/etc/mail/authinfo`. Run the following command:
```

```

Note  
  

If`/etc/mail/authinfo`doesn't exist, you can create it by running the command`sudo vi /etc/mail/authinfo`.

Add the following line:
```

```

- 

Generate the`/etc/mail/authinfo.db`file.

Run the following command:
```

```

- 

Add support for relaying to the Oracle Cloud Infrastructure Email Delivery SMTP endpoint.

Run the following command:
```

```

- 

Regenerate`/etc/mail/access.db`.

Run the following command:
```

```

- 

Create a backup of the`sendmail.cf`and`sendmail.mc`files.

Run the following command:
```

```

- 

Update the`/etc/mail/sendmail.mc`file.

Run the following command:
```

```

Find the`MAILER()`definitions.

Type`/MAILER`and press`ENTER`.

In Insert mode, add the following settings before any`MAILER()`definitions:
```

```

Disable Insert mode.
- 

Make Sendmail writeable.

Run the following command:
```

```

- 

Regenerate`sendmail.cf`.

Run the following command:
```

```

Note  
  

If you receive an error, such as "Command not found" or "No such file or directory," confirm that the m4 and sendmail packages are installed on your system.
- 

Reset permissions for sendmail.cf to read only.

Run the following command:
```

```

- 

Restart Sendmail.

Run the following command:
```

```

- 

Test the configuration by sending a test email.

Run the following command:
```

```

Enter the details of the email. After each line press`Enter`.

For example:
```

```

Press`Ctrl + D`to send the email.
- 

Verify receipt of the test email.
Note  
  

You can troubleshoot an issue by reviewing the Sendmail log on your mail server, located at`/var/log/mail.log`.

## More Information

For more information, see the[Sendmail Installation and Operation Guide](https://www.sendmail.org/~ca/email/doc8.9/op.html)
