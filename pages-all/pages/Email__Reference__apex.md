# Integrating Oracle APEX with Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/apex.htm
- Fetched: 2026-09-05 02:00 CDT

# Integrating Oracle APEX with Email Delivery

Use Oracle APEX to send emails through the Email Delivery service.

## Configure Oracle APEX to Send Email Through Email Delivery

You can use the`APEX_MAIL`package to send emails from Oracle APEX applications deployed in Autonomous AI Transaction Processing. See[Autonomous AI Transaction Processing](https://docs.oracle.com/en/cloud/paas/atp-cloud/index.html)and[Provision Autonomous AI Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/autonomous-provision.html#GUID-0B230036-0A05-4CA3-AF9D-97A255AE0C08)for more information.

Important  
  
These instructions contain sample code for your convenience and should be used as a reference. For client support, you must contact Oracle APEX customer support. These steps were tested on an Oracle Linux Server release 7.9 compute instance.

Before you use`APEX_MAIL`you must configure Oracle Cloud Infrastructure Email Delivery in your APEX instance.

To enable`APEX_MAIL`functionality in your APEX instance in Autonomous AI Transaction Processing:
- Identify the SMTP connection endpoint for Email Delivery. You configure the endpoint as the SMTP Host in your APEX instance in Step 4. See[Configuring SMTP Connection](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-Configure_the_SMTP_connection.htm)for more information.
- Generate SMTP credentials for Email Delivery. Your APEX instance uses credentials to authenticate with Email Delivery servers when you send email. See[Create SMTP Credentials for a User](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-create-smtp-credentials.htm#console)for more information.
- Create an approved sender for Email Delivery. You need to complete this step for all email addresses you use as the "From" with`APEX_MAIL.SEND`calls, as the Application Email From Address in your apps, or in the`SMTP_FROM`instance parameter. See[Managing Approved Senders](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Tasks/managingapprovedsenders.htm)for more information.
- 
Note  
  
We recommend you create credential objects to store usernames and passwords and securely pass the credential objects to set SMTP Authentication. For more information, see[Use Credential Objects to set SMTP Authentication](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/smtp-send-mail.html#GUID-D1722017-2792-4366-A2A4-E859D03E3A60). Or, connect to your Autonomous AI Transaction Processing as ADMIN user using SQL client and configure the following SMTP parameters using`APEX_INSTANCE_ADMIN.SET_PARAMETER`:
- `SMTP_HOST_ADDRESS`: Specifies the SMTP connection endpoint from Step 1.
- `SMTP_USERNAME`Specifies the SMTP credential username from Step 2.
- `SMTP_PASSWORD`Specifies the SMTP credential password from Step 2.

For example:

```

```

- 

Send a test email using APEX SQL Workshop, SQL Commands specifying one of the approved senders from Step 3 as "From". For example:

```

```

- To monitor email delivery in your APEX instance:
- Sign in to APEX Administration Services.
- Open the Manage Instance page.
- 

Click the Mail Queue link in the Manage Meta Data section.

Or, query`APEX_MAIL_QUEUE`and`APEX_MAIL_LOG`views using a SQL client.

## More Information

- [Creating Applications with Oracle APEX in Autonomous AI Database](https://docs.oracle.com/en/cloud/paas/atp-cloud/atpug/application-express-autonomous-database.html#GUID-D078638E-4F59-46CA-A14D-DAEBE1514BE8)
- [APEX_MAIL](https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/atp-cloud/atpug&id=AEAPI-GUID-14F51C6D-CB82-4B38-AB6E-61C46E75596F)in Oracle APEX API Reference
- [APEX_INSTANCE_ADMIN](https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/atp-cloud/atpug&id=AEAPI-GUID-1A894D25-A884-466B-9B88-B10888B2FFEA)
