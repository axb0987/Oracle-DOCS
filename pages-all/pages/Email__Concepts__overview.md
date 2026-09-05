# Overview of Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/overview.htm
- Fetched: 2026-09-05 02:00 CDT

# Overview of Email Delivery

The Oracle Cloud Infrastructure Email Delivery service provides a fast and reliable managed solution for sending secured, high-volume marketing and transactional emails.

The Email Delivery service provides tools necessary to send application-generated email for mission-critical communications such as receipts, fraud detection alerts, identity verification, and password resets.

The platform is optimized for bulk or marketing and transactional email, and not for personal correspondence email.

Oracle Cloud Infrastructure's Email Deliverability team manages the platform using key deliverability metrics to ensure the best sending reputation possible for your emails.

The following items are provided to you when you send emails using the Email Delivery service:
- Unique mailbox provider SMTP configurations on our Mail Transfer Agents (MTA)
- Bounce collection
- User complaint collection
- Email authentication standards
- Deliverability performance

When you use Email Delivery, we become the outbound email server. If you have an existing email server, you can keep it and configure it to send through Email Delivery. The Email Delivery service takes care of the feedback loops and platform reputation automatically.

## Email Delivery Service Components

Email Delivery uses the components described in this section. APPROVED SENDERS An Approved Sender is a resource that equates to the "From" address. An approved sender is associated with a compartment and only exists in the region where the approved sender was configured. If you need to have the same approved sender in another region, it must be created in the other region. For example, if you create an approved sender in the US West (Phoenix) region, you can't send email through the US East (Ashburn) region. SUPPRESSION LIST The Suppression List is included on Email Delivery Console user interface and from the API. Email Delivery automatically adds email addresses with bounce codes showing permanent failures or user complaints to the suppression list to protect sender reputation. Email Delivery doesn't send any messages to these recipients in the future. Reasons for suppression include:
- Complaints
- Hard bounces
- Manual entries
- List-unsubscribe requests SPF AUTHENTICATION

Sender Policy Framework (SPF) is used by email receivers to detect email spoofing. Using SPF, an email receiver can check if the Internet Protocol (IP) is explicitly authorized to send for that domain. SPF is implemented by publishing a special TXT record to a domain's DNS records. The TXT record declares which hosts are allowed to send mail on behalf of this domain. Receiving mail servers check the SPF records of sending domains to verify that the email's source IP address is authorized to send from that domain. Without SPF, a spam or phishing email can be "spoofed" to appear that the email comes from a legitimate domain. Domains that implement SPF are much more likely to block emails attempting to spoof your domain. For an overview of how SPF works, see[Sender Policy Framework](http://www.open-spf.org/Introduction). For details on SPF record syntax, see[SPF Record Syntax](http://www.open-spf.org/SPF_Record_Syntax).

## Regions and Availability Domains

SMTP credentials can be used for any region, as identities are global assets. However, approved senders (your "From" address) must be configured within each region you plan to use for Email Delivery. To configure approved senders within each region, select a region from the Region menu in the Console and create an approved sender. Configure your application to send email to the endpoint of that region where you created the approved sender, using the global SMTP credentials. The sending application is not required to be located in the region where email is sent from, however, we recommend that it is local or as close as possible for performance reasons.

For more information, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

### Configuring a New Region

To start sending emails from a new region, remember the following points:
- An approved sender must be created in the new region.
- SMTP credentials are global, however, we recommend that you generate SMTP credentials for a new user (without the OCI Console access) in the new region so that the credentials aren't shared with other regions. Ensure that the user has the correct privileges.
- Emails must be sent to the new regional SMTP connection endpoint.
- The suppression list and approved senders are regional Email Delivery assets.

For example, if an email sent from the US West (Phoenix) region bounces, the recipient email address are added to the US West (Phoenix) region suppression list. This recipient would not be added to other region suppression lists. If you're sending email from different regions, approved senders must be created in each region.
- SPF must be set up on each subdomain. For example, in your DNS setup, create a TXT record for notification.eu-frankfurt-1.oraclecloud.com and paste the following information from the dialog box into the record:`v=spf1 include:eu.rp.oracleemaildelivery.com ~all`

## Ways to Access Oracle Cloud Infrastructure

You can access Oracle Cloud Infrastructure (OCI) by using the[Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm)(a browser-based interface),[REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or[OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To access the[Console](https://cloud.oracle.com/), you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select Infrastructure Console . You are prompted to enter your cloud tenant, your user name, and your password.

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

Email Delivery supports all OCI native authentication mechanisms, see[OCI SDK Authentication Methods](https://docs.oracle.com/iaas/Content/API/Concepts/sdk_authentication_methods.htm).

## Authentication and Connection Endpoints

Email Delivery supports all OCI native authentication mechanisms when using HTTPS email submissions. For more information, see[OCI SDK Authentication Methods](https://docs.oracle.com/iaas/Content/API/Concepts/sdk_authentication_methods.htm). It also supports the AUTH PLAIN command when using SMTP authentication. If the sending application isn't flexible with the AUTH command, an SMTP proxy/relay can be used. For more information about the AUTH command, see[AUTH Command and its Mechanisms](https://www.samlogic.net/articles/smtp-commands-reference-auth.htm).

To know the regional endpoints, ports, or security details for establishing HTTPS or SMTP connections, see HTTPS sending information and SMTP sending information on the Console. For more information, see,[Configuring HTTPS Connection](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/email-submission-configure-https-connection.htm)and[Configuring SMTP Connection](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/../Reference/gettingstarted_topic-Configure_the_SMTP_connection.htm).

## Monitoring Resources

You can monitor the health, capacity, and performance of your Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)and[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).

For information about available Email Delivery service metrics and how to view them, see[Email Delivery Metrics](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/../Reference/metricsalarms.htm).

## Email Delivery Service Capabilities and Limits

For a list of applicable limits and[instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm), see[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm). To set compartment-specific limits on a resource or resource family, administrators can use[compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).

Customers that sign up for a free Oracle Cloud trial are limited to:
- A volume of 200 emails per day where an email is defined as either a single recipient in the TO:, CC:, or BCC: fields, or a 2 MB chunk of data.

Email examples:
- 

A single request with 10 recipients (TO:, CC:, or BCC:) equals 10 emails.
- 

A 10 MB email sent to a single recipient is equal to 10 MB divided by 2 MB per email. This equals 5 emails.
- 

A single email request with a message size of 10 MB sent to 10 recipients is equal to 10 MB divided by 2 MB per email multiplied by 10 recipients. This equals 50 emails.
- 2,000 approved senders.
- Each user is limited to a maximum of two SMTP credentials.
- Sending rates are limited to 10 emails per minute.
- Inline attachments and external attachments.
- 2 MB maximum message size including base64 encoding and headers

Enterprise accounts are limited to:
- A volume of 50,000 emails per day where an email is defined as either a single recipient in the TO:, CC:, or BCC: fields or a 2 MB chunk of data.

Email examples:
- A single request with 10 recipients (TO:, CC:, or BCC:) equals 10 emails.
- A 10 MB email sent to a single recipient is equal to 10 MB divided by 2 MB per email. This equals 5 emails.
- A single email request with a message size of 10 MB sent to 10 recipients is equal to 10 MB divided by 2 MB per email multiplied by 10 recipients. This equals 50 emails. This limit applies to unique recipients among all emails sent. For example, a single email sent to 100 recipients would count the same as 100 individual emails each sent to a single recipient.
- 10,000 approved senders.
- Sending rates are limited to 18,000 emails per minute.
- Inline attachments and external attachments.
- 2 MB maximum message size including base64 encoding and headers

Email Delivery, by default, supports messages up to 2 MB, inclusive of message headers, body, and attachments. Each 2 MB of data counts toward your daily sending volume and sending rate limits. For example, a 10 MB counts as five emails.

For any email limit increase, SPF and DKIM are required for your sending domain and approved sender. See[Configuring SPF](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/../Tasks/configurespf.htm)and[Configuring DKIM](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/../Tasks/configure-dkim-using-the-console.htm).

Based on your requirement, you can request for limit increase up to a maximum of 60 MB for message size .

To open a service request to increase the limit, see[Creating a Limit Increase Request](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm). Your increase request is evaluated by the following information you provide:
- What are your current sending domains?
- Do your sending practices meet the requirements of CAN-SPAM and CASL?
- Briefly describe the type of email you' will be sending. For example, are the emails marketing, bulk, newsletters, transactional, notifications, and so on?
- Do you send emails related to payday loans or credit card offers?
- Do you send emails on behalf of other companies?
- How do the recipients sign up to receive these emails? Specify any domains they might sign up on.
- Are there any other methods that are used to collect email addresses?
- How many emails do you want to send per month?
- Which ESP supplier are you using to send your emails?
- What is the maximum number of messages you need to send in a burst capacity (within a specific timeframe)?
- What is the maximum size of your messages?
- What is the number of emails sent per day that is over 2 MB?
- Are your recipients Oracle email addresses (for example, test.user@oracle.com)?
- Which email delivery region do you intend to use to send email through?

Note  
  
The Email Delivery platform supports higher volume limits. Limits are set as a safeguard for our customers' reputation. To open a service request to increase the email sending limit, see[Creating a Limit Increase Request](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm).

For any email limit increase, SPF and DKIM are required for your sending domain and approved sender. See[Configuring SPF](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/../Tasks/configurespf.htm)and[Configuring DKIM](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/../Tasks/configure-dkim-using-the-console.htm).

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about policies for Email Delivery, see[Details For the Email Delivery Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/emailpolicyreference.htm).

Permissions are required for managing and using approved senders and the suppression list. For example:
- To enable all operations on approved senders for a specific user group:
```

```

- To enable all operations on suppressions for a specific user group:
```

```

Note  
  

If you're using SMTP credentials of users who aren't in the "Default" Identity Domain, you need to include the name of your Identity Domain in your policy statement. For more information, see[How Policies Work (with Identity Domains)](https://docs.oracle.com/iaas/Content/Identity/policieshow/how-policies-work.htm).

## Dedicated IP Addresses

When you create an Email Delivery service account, by default, your emails are sent from IP addresses shared with other Oracle customers.

Email Delivery supports IPs addresses dedicated to you, for complete control over your reputation. Both a shared IP or dedicated IP strategy can provide excellent delivery depending on your needs and mail stream characteristics. For more information about shared IP, see[Shared IP or Dedicated IP](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/../Reference/gettingstarted_topic-Begin_sending_email.htm#shared_or_dedicated_ip).

When using a dedicated pool of Oracle owned IP addresses, only your mail is sent from them.

Note  
  
Our deliverability experts review all dedicated IP requests to ensure the best deliverability for your situation. Dedicated IP addresses may not be advised for lower volume or more sporadic email sending, as this does not support a good sending reputation and therefore can cause an impact to your email deliverability.

Dedicated IP addresses are ideal for senders who:
- Send large volumes of mail on a consistent basis to sustain their own IP reputation. Sending a large volume of mail consistently is what Internet Service Providers (ISPs) automated filters use to assign a reputation to your IP address. This is one of the key inputs into whether your messages are delivered into the inbox, spam folder, or temporarily rejected.
- Want complete control of their sending reputation AND understand email delivery best practices. When you are the only sender on an IP, it insulates your reputation from other senders. This can be good or bad depending on your sending practices and consistent hygiene.
- Have large volumes, different mail streams, and want to build unique reputations for each. Dedicated IPs enable you to build separate IP reputations based on different types of mail streams like transactional messages versus bulk marketing mail. If you have the volume to support it, isolating these mail streams can reduce the risk of delivery challenges for more critical message types.

Dedicated IP addresses are likely not a good fit for senders who:
- Send mail inconsistently at low volumes preventing an ISP reputation from being assigned. To build an IP reputation, ISPs prefer a predictable mail cadence with enough email volume to assign a reputation. Failing to meet this requirement could lead to delivery challenges. Sending in a shared IP pool with many smaller senders will provide the ISP with a large volume of consistent mail.
- Do not understand email best practices, which could lead to poor-reputation delivery challenges. Sending in a shared IP pool with other customers that is managed by Oracle can be less risky for an email novice.

Your mail characteristics (volume, burst rates, reputation, and so on) will vary your dedicated IP strategy. Our teams are trained on dedicated IP strategies and ready to support your needs. If you need help with your configuration, you can go to[My Oracle Support](http://support.oracle.com/)and create a service request.

## Tagging Resources

You can apply tags to resources to help you organize them according to business needs. You can apply tags at the time you create a resource, or you can update the resource later with tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

Email Delivery supports applying tags to approved senders.

## Integration with Oracle Cloud Infrastructure Services

Email Delivery audits the following events:
- Creating a sender (CreateSender)
- Deleting a sender (DeleteSender)
- Retrieving details about a sender (ListSenders)

To view logs for events in the Email Delivery service, your user must be in a group with the ability to view all of the Audit event logs in the tenancy. For more information, see[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm)
