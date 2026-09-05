# Configuring SMTP Connection
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-Configure_the_SMTP_connection.htm
- Fetched: 2026-09-05 02:00 CDT

# Configuring SMTP Connection

Review the SMTP information and TLS requirements to configure the SMTP connection in your system.

## Using the Console

- Open the navigation menu and select Developer Services . Under Application Integration , select Email Delivery .
- Under Email Delivery , select Configuration . The SMTP sending information panel displays the following information:

- Public endpoint: The public endpoint used to send an email to, for this region.
- SMTP ports: The SMTP ports used to accept an email. Email Delivery supports TLS on port 465.
Note  
  
Port 465 is the standard submissions port. It negotiates Transport Layer Security (TLS) when the connection starts, instead of using STARTTLS. This approach provides a slightly more efficient encryption setup.
- 

Security: This field indicates if TLS, the standard means of performing encryption in transit for emails, is being used. Customers must encrypt emails while it's in transit to the Oracle Cloud Infrastructure Email Delivery service. Encrypted emails are protected from being read during transit.
Tip
