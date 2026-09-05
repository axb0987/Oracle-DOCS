# Sending an Email
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-Begin_sending_email.htm
- Fetched: 2026-09-05 02:00 CDT

# Sending an Email

Learn to use the Email Delivery service by configuring Oracle Cloud and third-party applications to send an email.

## Using the Console

Ensure that you have completed the following steps to send an email using the Email Delivery.

- [Create a group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm#To)or use an existing group in the tenancy. Users of this group are allowed to manage the Email Delivery service.
- [Create a user](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingusers.htm#create_user)and[add the user to the group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingusers.htm#add_user), or add existing users to the group.
- [Create user permissions](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-create-policy.htm#console).
- Set up[HTTPS email submission](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Concepts/email-submission-using-https.htm)or create[SMTP credentials](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-Configure_the_SMTP_connection.htm#smtp)and set up[SMTP email submissions](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Concepts/email-submission-using-smtp.htm).
- [Create email domain](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-create-email-domain.htm).
- [Enable logs for troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Tasks/enablelogs_using-the-console.htm).
- Configure[SPF](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Tasks/configurespf.htm),[DKIM](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Tasks/configure-dkim-using-the-console.htm), and[create an approved sender](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-Create_an_approved_sender.htm).
- [Configure Oracle or third-party applications](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-Configuring_ThirdParty_Applications.htm)and send email.
If you run into issues, go to[Troubleshooting Email Delivery](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Concepts/troubleshooting.htm).

## Using the API

Configure the Email Delivery service using REST API.

Instructions for the[REST API](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/)are included in topics throughout this guide. For a list of available SDKs, see[SDKs and Other Tools](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

## Using the SDK

Configure the Email Delivery service using SDK.

The Email Delivery SDK is available in several programming languages. For information on installing and configuring the Oracle Cloud Infrastructure SDKs, see[Developer Tools and Resources](https://docs.oracle.com/iaas/Content/devtoolshome.htm).

Examples of SDK usage can be found on GitHub, including:
- [Example: Email Delivery SDK for Java](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/EmailServiceExample.java)
- [Example: Email Delivery SDK for Python](https://github.com/oracle/oci-python-sdk/blob/master/examples/email_service_example.py)
- [Example: Email Delivery SDK for Ruby](https://github.com/oracle/oci-ruby-sdk/blob/master/examples-oci/email_service_example.rb)
- [Example: Email Delivery SDK for Go](https://github.com/oracle/oci-go-sdk/blob/master/email/email_client.go)

## Volume Testing and Sending to Email Aliases

Perform volume testing to maintain our sender reputation and yours.

To perform volume testing, use the following best practices:
- If large volume emails are sent to valid email addresses, these get rejected by receivers and result in a large amount of hard bounces negatively affecting IP reputation. For testing bounce processing, send small amounts of emails to a domain that doesn't have an MX record, in other words, the domain doesn't exist.
- 
Note  
  
To help you learn and manage the habits that affect your sending reputation, see[Email Deliverability](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/deliverabilitybestpractices.htm).

Sending to Email Aliases - When sending email to an alias, the alias is considered one recipient. When sending email to a distribution group or list set up in an email client such as Apple Mail or Outlook, a separate email is sent for each recipient in the group.

## Shared IP or Dedicated IP

When moving providers, one of the key decisions while managing email is to choose between dedicated IPs and shared IPs to send emails. The correct way to begin is to send emails through shared IPs.

### Why are Shared IPs Preferred?

Common among email service providers, shared IPs are made up of a group of IP addresses that many different companies send through.

Using this method, customers with great sending reputations indirectly make it easier for other reputable senders who are trying to get into the inbox and build up their own reputation while doing so.

Shared IP pools are also the primary option for senders who either don't have the volume or consistent sending patterns to maintain their own dedicated IPs but are trying to build up that volume over time. Both are buoys for building and maintaining a good to, hopefully, great sending reputation.

Even if a sender starts on a shared IP range, that doesn't mean shared IPs are the only option for them forever. Given the right amount of volume and best practices for email marketing, a graduation plan can be established.

### More on our Shared Pools

[OCI Email Delivery](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../home.htm)has several shared IP pools based on both the type of email sent and the volume. All our pools are curated to avoid any issues and for migration of senders into other pools because of volume constraints or a ramp onto dedicated IPs.

You might understandably have some concerns and risks with sending pools. Another sender can hit a blocklist that makes the IP reputation dip or traffic can see an unexpected surge that causes some delays. However, with proper management by the teams such as ours that oversee those IPs, those issues are minimalized with the benefits far outweighing any potential negatives.

### Why not Dedicated IPs?

Dedicated IPs are dedicated and exclusive for that sender's email only. Depending on volume, a sender can have one dedicated IP or several. They allow large volume senders to better maintain control over their own sending reputation and to have more control over allowlisting.
The following criteria must be met to be a good candidate for dedicated IPs:
- 

A certain level of high-quality monthly email volume needs to be maintained to build a sending reputation on dedicated IPs. If the volume isn't consistent every month, shared IPs help ease the issue.
- 

Consistency and cadence with that level of email is necessary to both build and maintain an IP reputation. If the sender doesn't have a regular schedule for bulk or marketing deploys, shared IPs help ease the issue.
-
