# Integrating JavaMail with Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/javamail.htm
- Fetched: 2026-09-05 02:00 CDT

# Integrating JavaMail with Email Delivery

Use JavaMail to send emails through the Email Delivery service.

JavaMail provides a platform-independent and protocol-independent framework to build mail and messaging applications. Before you use JavaMail, you must configure Email Delivery and take note of your SMTP sending information and SMTP credentials. This guide uses the Eclipse IDE and the JavaMail API to send email through Email Delivery.

Important  
  
These instructions contain sample code for your convenience and should be used as a reference. For client support, you must contact JavaMail customer support. These steps were tested on an Oracle Linux Server release 7.9 compute instance and Java 8 and 11. Java applications (including JavaMail) must be updated to the latest version to ensure that the latest protocols, ciphers, and security patches are in compliance with Oracle's supported security policies and ciphers.

## Configure JavaMail to Send Email Through Email Delivery

To enable JavaMail to test the configuration of Email Delivery:
- 

Ensure Email Delivery is configured to send email. See[Getting Started](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted.htm).
Note  
  

The SMTP credentials are required to configure JavaMail to use Email Delivery. Be sure to note the user name and password when you generate the SMTP credentials.
- Open a browser and go to[https://github.com/javaee/javamail/releases](https://github.com/javaee/javamail/releases).
- Under Downloads , select javax.mail.jar to download the latest version of JavaMail.
- Create a project in Eclipse by performing the following steps:
- In Eclipse, open the File menu. Select New , and then click Java Project .
- In the Create a Java Project dialog box, enter a project name, and then click Next .
- In the Java Settings dialog box, select the Libraries tab.
- Click Add External JARs .
- In the JAR Selection dialog box, browse to the folder in which you downloaded JavaMail. Select the javax.mail.jar file, and then click Open .
- In the Java Settings dialog box, click Finish .
- In Eclipse, in the Package Explorer window, expand your project.
- Under your project, right-click the src directory, select New , and then click Class .
- In the New Java Class dialog box, enter "OCIemail" in the Name field and then click Finish .
- 

Enter the following code in OCIemail.java to send a test email with JavaMail:
```

```

- 

In the OCIemail.java file, replace the following with your own values:
Note  
  

Email addresses are case-sensitive. Ensure that the addresses are the same as the ones you entered in Approved Senders in the console.
- FROM - Replace with your sender email address. This email address must be added to the Approved Senders list in Email Delivery first.
- TO - Replace with your recipient email address.
- SMTP credentials - Replace smtp_username and smtp_password with your Oracle Cloud Infrastructure SMTP username and password generated in the console.
- HOST - Replace with the Email Delivery SMTP endpoint. For example, smtp.us-ashburn-1.oraclecloud.com.
- 

Refer to the requirements for[configuring SMTP connection](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-Configure_the_SMTP_connection.htm)with Email Delivery. TLSv1.2 is required for Email Delivery. Some default settings of[Javamail](https://javaee.github.io/javamail/)need to be disabled. For example, JavaMail authorizes in a certain order. The default authorization order is "LOGIN PLAIN DIGEST-MD5 NTLM". Since Email Delivery authorizes as "PLAIN", "LOGIN" needs to be disabled. For example, the following code is entered in OCIemail.java file to configure the SMTP connection:
```

```

- Open the File menu and click Save .
- To build the project, open the Project menu and then select Build Project . If this option is disabled, you may have automatic building enabled.
- To start the program and send the email, open the Run menu and then click Run .
- Review the output. If the email was successfully sent, the console displays "Email sent successfully!" Otherwise, it displays an error message.
- Log into the recipient inbox to verify receipt of the email.

## More Information

- See the[JavaMail](https://javaee.github.io/javamail/#API_Documentation)documentation for more information.
- There is a known issue that can cause an error. See[JavaMail issues occur when many recipients are set in an email and one or more of the email addresses are suppressed](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/known_issue.htm#javamail)
