# Integrating Oracle Enterprise Manager with Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/OEM.htm
- Fetched: 2026-09-05 02:00 CDT

# Integrating Oracle Enterprise Manager with Email Delivery

Use Oracle Enterprise Manager to send emails through the Email Delivery service.

## Configure Oracle Enterprise Manager to Send Email Through Email Delivery

You can use Oracle Enterprise Manager to send emails through Email Delivery. Before you use Oracle Enterprise Manager, you must configure Oracle Cloud Infrastructure Email Delivery in your Oracle Enterprise Manager application.

Important  
  
These instructions contain sample code for your convenience and should be used as a reference. For client support, you must contact Oracle Enterprise Manager customer support. These steps were tested on an Oracle Linux Server release 7.9 compute instance.
Note  
  

For information on installing Oracle Enterprise Manager, see[Setting Up Oracle Enterprise Manager on Oracle Cloud Infrastructure](https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.3.1/emoci/index.html).

To enable Oracle Enterprise Manager to integrate with Email Delivery:
- 

Make sure Email Delivery is configured to send email. See[Getting Started](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted.htm).
Note  
  

The SMTP credentials are required to configure Oracle Enterprise Manager to use Email Delivery. Be sure to note the user name and password when you generate the SMTP credentials.
- In Oracle Enterprise Manager, go to the Setup menu and click Initial Setup Console .
- In the Initial Setup Console section, click Configure Mail Servers in the navigation pane.
- In the Sender Identify section, click Edit .
- Enter the name of the administrator or system that should send the email notifications and the email address from which the notifications should be sent, and then click OK .
- In the Outgoing Mail (SMTP) Servers section, click Create .
- Enter the mail server host name, the mail server credentials, and the encryption method to be used, and then click OK .
- Select the outgoing mail server you wish to test and select Test Mail Server . Note the confirmation message in the console and verify that you received the test email in your inbox.
Note
