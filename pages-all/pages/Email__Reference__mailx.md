# Integrating Mailx with Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/mailx.htm
- Fetched: 2026-09-05 02:01 CDT

# Integrating Mailx with Email Delivery

Use Mailx to send emails through the Email Delivery service.

## Configure Mailx to Send Email Through Email Delivery

Mailx is a UNIX utility program for sending and receiving mail, also known as a Mail User Agent program. You can use Mailx to send emails through Email Delivery. Before you use Mailx, you must configure Oracle Cloud Infrastructure Email Delivery in your Mailx application.

Use these instructions only if no mail transfer agent (MTA), such as Postfix or Sendmail, is in use on the system. If you're configuring an MTA, follow the configuration instructions for that program and leave the Mailx settings at their defaults. This makes Mailx use the local MTA program to send outbound mail.

Important  
  
These instructions contain sample code for your convenience and needs to be used as a reference. For client support, you must contact Mailx customer support.
Note  
  

These steps assume you're signed in to an Oracle Linux instance. Other distributions of Linux might have different commands and file locations. These steps were tested on an Oracle Linux Server release 7.9 compute instance and Mailx version 12.5 7/5/10.

To enable Mailx to integrate with Email Delivery:
- 

Ensure that Email Delivery is configured to send email. See[Getting Started](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted.htm).
Note  
  

The SMTP credentials are required to configure Mailx to use Email Delivery. Be sure to note the username and password when you generate the SMTP credentials.
- 

Update the Mailx`.mailrc`file.

To open the`.mailrc`file, run the following command:
```

```

Add the following information to the end of the file:
```

```

- 

Test the configuration by sending a test email.

Run the following command:
```

```

## Troubleshooting

"Error in certificate: Peer's certificate issuer has been marked as not trusted" occurs when sending email

To troubleshoot this issue, complete the following steps:
- Run the following command to view the certificate chain:
```

```
Example output:
```

```

- Extract the certificate that signed your domain. In this example, this is the last certificate (`2 s:/C=US/O=DigiCert Inc/OU=www.digicert.com/CN=DigiCert Global Root G2`). Copy and paste the certificate into a separate`DigiCert.pem`file, including the`BEGIN CERTIFICATE`and`END CERTIFICATE`fields.
- Install the certificate into the Centos NSSDB database. Replace "`DigiCert Global Root G2"`in the following example with your certificate:
```

```

To view the certificate, use the following command:
```

```

## More Information

For network security services, see the[Mailx](https://linux.die.net/man/1/mailx)
