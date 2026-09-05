# Integrating MailKit with Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/mailkit.htm
- Fetched: 2026-09-05 02:01 CDT

# Integrating MailKit with Email Delivery

Use MailKit to send emails through the Email Delivery service.

## Configure MailKit to Send Email Through Email Delivery

MailKit is an open source cross-platform email framework for .NET applications. As[SmtpClient](https://docs.microsoft.com/en-us/dotnet/api/system.net.mail.smtpclient?view=net-5.0#remarks)is no more a suggested approach to send mails in .NET applications, you can instead use MailKit to send and receive emails through Email Delivery. Before you use MailKit, set up a sample MailKit code and test it with the Email Delivery configuration.

Important  
  
The following instructions contain sample code for your convenience and must be used as a reference.

To set up MailKit sample code and test the Email Delivery configuration:
- 

Ensure that Email Delivery is configured to send email. See[Getting Started](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted.htm).
Note  
  

The SMTP credentials are required to configure MailKit to use Email Delivery. Be sure to note the user name and password when you generate the SMTP credentials.
- 

To create a project in Visual Studio Code:
- Create a project space by creating a folder by the name OCIEmail.
- Open the OCIEmail folder in VS Code File &gt; Open Folder.
- Open the terminal window (ctrl + ~).
- To create the project template and add the dependency of MailKit, run the following commands in the terminal.
```

```

Expand your project in the VS Code Explorer window.
- Replace the contents of the Program.cs file with the following code block:
```

```

Important Guidelines:
- 

If using port 465 :

Use`client.Connect(host, port, true)`for a direct SSL/TLS connection.
- 

If using port 25 or 587 :

Use`client.Connect(host, port, SecureSocketOptions.StartTls)`.

Make sure you have`using MailKit.Security;`at the top.
- 
Replace the following parameters with your own values in the Program.cs file:
- FROM - Replace with your sender email address. Ensure that this email address is added to the Approved Senders list in Email Delivery.
- TO - Replace with your recipient email address.
- SMTP credentials - Replace`<smtp username>`and`<smtp password>`with your Oracle Cloud Infrastructure SMTP username and password generated in the console.
- HOST - Replace with the Email Delivery SMTP endpoint. For example, smtp.us-ashburn-1.oraclecloud.com.
- Save the changes and run the following command to send the mail:
```

```

- Review the output. If the email is successfully sent, the console displays Email sent successfully! Otherwise, it displays an error message.
-
