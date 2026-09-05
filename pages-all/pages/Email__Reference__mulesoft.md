# Integrating MuleSoft Anypoint Studio with Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/mulesoft.htm
- Fetched: 2026-09-05 02:01 CDT

# Integrating MuleSoft Anypoint Studio with Email Delivery

Use MuleSoft Anypoint Studio to send emails through the Email Delivery service.

## Configure Anypoint Studio to Send Email Through Email Delivery

The MuleSoft Anypoint integration platform is a unified platform that offers a holistic approach to API design and development. The Anypoint Connector for Email (Email Connector) sends and retrieves email messages over standard email protocols.

To enable MuleSoft Anypoint to integrate with Email Delivery:
- Make sure Email Delivery is configured to send email. See[Getting Started](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted.htm).
Note  
  

SMTP credentials are required to configure Anypoint to use Email Delivery. Be sure to note the user name and password when you generate the SMTP credentials.
- Create a new Mule Project in Studio.
- Drag and drop an HTTP Listener Connector (or another trigger). This source initiates a flow when the HTTP Listener receives a request.
- Drag the Email Send operation to the right of the HTTP Listener.
- On the Send configuration screen, click the plus sign (+) next to the Connector configuration field.
- For Connection , select SMTP Connection .
- In the General tab, enter the following values.
- Host: Your SMTP Endpoint. See[Configuring SMTP Connection](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-Configure_the_SMTP_connection.htm)to retrieve this value.
- Port: 465 (recommended)
- User: SMTP Username
- Password: SMTP Password
- In the Advanced tab, under Properties , select Edit inline and add the following:
- Key: mail.smtp.starttls.enable
- Value: true
- Go back to the Send screen and set the following values:
- From address: Your approved sender.
- To address: Edit inline. Click to plus sign (+) to add new emails.
- Subject: The subject of your email.
- Content: The content of your email. For example,`"<h1>Test</h1>"`.
- ContentType: text/html
- Save and run the app.

## More Information

For more information, see[Sending Emails with Email Connectors](https://docs.mulesoft.com/email-connector/1.7/email-send)
