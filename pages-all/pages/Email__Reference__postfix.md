# Integrating Postfix with Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/postfix.htm
- Fetched: 2026-09-05 02:01 CDT

# Integrating Postfix with Email Delivery

Use Postfix to send emails through the Email Delivery service.

## Configure Postfix to Send Email Through Email Delivery

Postfix is a free and open source mail transfer agent that routes and delivers electronic mail. It is released under the IBM Public License 1.0 which is a free software license, and might already be installed. To learn more about Postfix, see the[Postfix website](http://www.postfix.org/). You can use Postfix to send emails through Email Delivery. Before you use Postfix, you must configure Oracle Cloud Infrastructure Email Delivery in Postfix application.
Important  
  
These instructions contain sample code for your convenience and use them as a reference. For client support, contact Postfix customer support. These steps were tested on an Oracle Linux Server release 7.9 compute instance and Postfix version 2.10.1.
Note  
  

The paths and commands used in the following procedure for specifying file locations are specific to Ubuntu/Debian. The file paths or editing commands might differ depending on the OS you're using. The changes to the configuration files are the same.

To enable Postfix to integrate with Email Delivery:
- 

Ensure Email Delivery is configured to send email. See[Getting Started](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted.htm).
Note  
  

The SMTP credentials are required to configure Postfix to use Email Delivery. Be sure to note the SMTP username and SMTP password when you generate the SMTP credentials, which appear in User Settings. Those specific values, and not your OCI user identity, is required for configuration. If you have lost the password credential for your SMTP Credential, you need to create a new set of credentials.
- 

To open the`main.cf`file, run the following command:
```

```

Add the following information to the end of the file:

```

```

- 

Email Delivery requires secure TLS encryption ( transport level security ) for all SMTP email submissions. Use the[smtp_tls_security_level setting](https://www.postfix.org/postconf.5.html#smtp_tls_security_level)to have Postfix use STARTTLS support when connecting to remote SMTP servers such as OCI Email Delivery:
```

```

To enforce the use of TLS for all remote server communications, use the following setting:
```

```

Note  
  
By default, the Postfix client assumes that the maximum allowed message size is that received in the initial Extended HELO (EHLO) response. This will always be our deployment default of 2 MB. If you have a higher maximum message size limit, you must configure the Postfix client to ignore this default value. Edit`the /etc/postfix/main.cf`file and add the following:
```

```

- 

Update`relayhost`to include your SMTP connection endpoint and port and then save or update the file. For example, to send messages through the new default mail submission port 465, use:

```

```

Note  
  
For the correct endpoint value, consult the[Authentication and Connection Endpoints](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Concepts/overview.htm#SMTP_Authentication_and_Connection_Endpoints). We recommend port 465, so append ":465" to the end of the endpoint you need as provided in the example.
- 

Create the`sasl_passwd`file in the same directory as`main.cf`.

Run the following command:
```

```

- 

Add your relay host and port by entering:
```

```

where:
- `server`is your relay host and`port`is 465.
- `user`is the SMTP username that you created and`pass`is the password you received when you generated your SMTP credentials.
- 

Give the permissions in the password file.

Run the following command:
```

```

- 

Generate the password hash.

Run the following command:
```

```

- 

Reload Postfix.

Run the following command:
```

```

- 

Test the configuration by sending a test email.

Run the following command:
```

```

Note  
  
Some versions of mail and mailx support neither the -r switch to set the sender in the email, or the -a switch to create additional headers. In these cases, the sender is determined by the operating system and can be overridden by various other means. If you would like to override the system-generated email addresses in this case, you can use rewrite rules located in /etc/postfix/header_checks.

A`status=sent (250 Ok)`message in the log indicates that the email was sent successfully.
Note  
  

In some environments, using SASL authentication requires the following RPM package:`cyrus-sasl-plain`. See the[PostFix website](http://www.postfix.org/SASL_README.html)for further documentation on configuring SASL authentication.

## More Information

- See the[Postfix website](http://www.postfix.org/)for more information on Postfix configuration.
- See[smtp_tls_security_level](https://www.postfix.org/postconf.5.html#smtp_tls_security_level)for more information on the default SMTP TLS security level for the Postfix SMTP client.
- See[smtpd_use_tls](https://www.postfix.org/postconf.5.html#smtpd_use_tls)for more information on STARTTLS support to remote SMTP clients. This feature was introduced in Postfix version 2.2 but deprecated since version 2.3.
- See[TLS Errors when Integrating with Postfix](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Concepts/troubleshooting.htm#TLS)
