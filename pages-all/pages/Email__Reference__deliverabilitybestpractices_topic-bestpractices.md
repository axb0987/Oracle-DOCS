# Best Practices
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/deliverabilitybestpractices_topic-bestpractices.htm
- Fetched: 2026-09-05 02:00 CDT

# Best Practices

These email deliverability best practices help you both learn and manage the habits that affect your sending reputation which, in turn, can help more email get delivered.

By following these recommendations, senders can lower both bounce and complaint rates, stay off blocklists, and improve your company's sending reputation.

[Implement an Opt-in Process](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/deliverabilitybestpractices_topic-bestpractices.htm#)

The opt-in process is how recipients subscribe to your bulk/marketing lists which gives you permission to send them email. Only send messages to subscribers who have opted-in to your mailing list, avoiding buying or renting lists at all costs.

There are two types of opt-in methods. Note that these methods apply to bulk/marketing email as transactional emails are sent based on an action that requires proof:
- 

Single opt-in (unconfirmed): A user provides their email address and gives the sender permission to receive relevant messages. After the address is provided, messages can be sent without confirming the email address belongs to the user who provided it. The risks in using single opt-in are exposure to list bombing through a targeted attack on a signup form, and by those signing up email addresses that don't belong to them.
- Double opt-in (confirmed): A user provides their email address, but before the first campaign is sent, they receive a confirmation email to the address that signed up. That email requires action from the account owner to confirm that future messages are wanted, most frequently done with a verification click. The double opt-in method ensures that the address was not added without consent and keeps electronic proof if future data privacy inquiries or audits arise.

[Purge Unengaged Users](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/deliverabilitybestpractices_topic-bestpractices.htm#)

One of the easiest and best ways to help keep your marketing lists clean is to remove unengaged users: those addresses which haven't opened or clicked within an email in a certain amount of time. Unengagement is a strong indication that the recipient is no longer interested in your content or that the account has been abandoned.

Remove recipients who have not engaged with your email in a timeframe defined by your business model but no longer than two years. By doing so, you show major inbox providers that you are keeping an updated database which helps boost your sending reputation. You also avoid the potential of hitting spam traps as some mailbox providers convert inactive inboxes to help prevent scraping of email addresses.

[Database Cleanliness](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/deliverabilitybestpractices_topic-bestpractices.htm#)

Keeping an overall clean and up-to-date database is important in addition to removing unengaged users. The best way to keep a clean database is to sync with Email Delivery using API calls so any hard bounces, unsubscribes, and suppressions are marked as such.

That constant sync helps lessen processing time when sending emails, ensures that your database is always updated, and minimizes the chance you send to an address that you should no longer be sending to.

[Evaluate Your Sending Frequency](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/deliverabilitybestpractices_topic-bestpractices.htm#)

Sending too many emails in a short time might aggravate your recipients, causing them to either unsubscribe or mark your campaigns as spam. By regularly reviewing your strategies, open rates, and other key metrics, you can reduce list fatigue and better learn how they want to engage with you.

Offer the ability to reduce the amount of emails they receive (for example, yearly, quarterly, or monthly), giving you a better chance at retention rather than them unsubscribing altogether. Recipient tastes and wants for email changes over time. Ensure that you're changing with it.

[Provide an Easily Accessible Unsubscribe URL](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/deliverabilitybestpractices_topic-bestpractices.htm#)

Don't attempt to hide your unsubscribe link as by doing so, you only further encourage your recipients to click the spam button, further hurting your reputation. Some providers will also hold it against you in their algorithm if you use a light color for your unsubscribe link and language.

If someone wants to be removed from your list, make the link easy to find and include it in both the header and footer. Offer a single-click unsubscribe option in addition to a preference center where they can reduce the frequency of emails, opt in to a different list, and so on.

[Other Best Practices in the Email Industry](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/deliverabilitybestpractices_topic-bestpractices.htm#)

The Messaging, Malware and Mobile Anti-Abuse Working Group (M3AAWG) publishes resources to help you follow best practices for sending email. We recommend these resources if you want to establish and maintain a strong sending reputation:
- 

[Sending Domains Best Practices](https://www.m3aawg.org/SendingDomsBCP)
- 

[Other Published Best Practices from M3AAWG](https://www.m3aawg.org/published-documents)

## CAN-SPAM, GDPR, CASL, and Privacy Laws

Knowing how to handle, process and market to consumer data in a legally permissible way is a must.

There are several regulatory measures and laws that help protect consumers around the world. One of the oldest is[the CAN-SPAM Act](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business), a piece of U.S. legislation that established requirements for "commercial" email.

Not using deceptive subject lines, honoring unsubscribes quickly, and having a physical address in the footer of emails are just some of the requirements outlined with violations resulting in fines.

Similarly, there is also[CASL](https://crtc.gc.ca/eng/com500/guide.htm), a Canadian-based anti-spam set of laws that was heavily based on CAN-SPAM. While based in Canada, the law applies to those who email Canadian residents.

Data privacy has become a hot topic in the last few years which is why knowing about the General Data Privacy Regulation ([GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)) is key. Active in 2018, the law regulates data privacy and protection in the European Union and has become a model for other countries' privacy laws.

Oracle Cloud Hosting and Delivery Policy

Often, the[Oracle Cloud Hosting and Delivery Policy](http://www.oracle.com/us/corporate/contracts/ocloud-hosting-delivery-policies-3089853.pdf)is more stringent than some of these industry requirements. It is important that you review Oracle policies before using the service.

Discussing your approach to data privacy and regulation with the appropriate personnel within your company is highly recommended.

## Troubleshooting Undelivered Emails

The following issues can cause an email to be undelivered:
- The recipient is on the Suppression List.
- An authentication failure or an issue with the format of the email message occurred. For example, if the SMTP "From" address is not the same as the "From" address in the email body, the email is rejected. The addresses must match and be an Approved Sender. Refer to your sending application's logs to review any issues.
- Use of multiple addresses in the email From header is discouraged. If you use multiple addresses, it increases the possibility that your mail is placed in a spam folder or discarded (because of DMARC From alignment rules). The performance of your emails is reduced because all addresses have to be authorized as approved senders. A best practice for the SMTP envelope From address is to match the header From address when you submit mail to Email Delivery. If you use mismatched addresses, it reduces the performance of your emails because both addresses need to be authorized as approved senders. Certain future platform features will not be available if you use mismatched addresses.
- Lack of[SPF](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Tasks/configurespf.htm)or[DomainKeys Identified Mail (DKIM)](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/deliverabilitybestpractices_topic-bestpractices.htm#options__dkim).

If you are unable to resolve the issue, you can go to My Oracle Support and create a service request. See[Open a support service request](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm)for more information.

## More Options to Increase Deliverability

### DomainKeys Identified Mail (DKIM)

DKIM is an authentication framework you can set up to help ensure good email delivery reputation. See[Managing DKIM](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Tasks/configuredkim.htm)for instructions on setting up DKIM.

### SPF

A Sender Policy Framework (SPF) lets domain owners identify servers they have approved to send emails on behalf of their domain. In Oracle integration's case, domain owners need to approve OCI as an approved sender and to add a record for it in their domain. See[Configuring SPF](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Tasks/configurespf.htm)for more information.

### Domain-based Message Authentication, Reporting, and Conformance (DMARC)

DMARC is a technical specification created by a group of organizations that want to help reduce the potential for email-based abuse by solving long-standing operational, deployment, and reporting issues related to email authentication protocols. DMARC standardizes how email recipients perform email authentication using SPF and DKIM. This gives the sender the ability to have control of mail that doesn't pass authentication and tell the email recipients what to do with non authenticated mail.

DMARC checks both SPF and DKIM and requires one to pass to send and deliver email. When you start using DMARC, it's a best practice to put a`p=none`policy in place and ensure that every legitimate sending application is aligned and authenticated correctly before considering a more aggressive policy. During any transition period where a new email-related service for the sending domain is evaluated, using a DMARC`p=none`policy and following this advice is recommended.
A[DMARC record](https://tools.ietf.org/html/rfc7489)is a DNS TXT record in the domain`_dmarc.<sending-domain>`with content similar to the following:
```

```

You must have an administrative INBOX service to receive DMARC reports (in the preceding example,`example.com`is your INBOX provider). Currently, Email Delivery doesn't offer INBOX service or automated DMARC report processing. If you don't want to manage and process DMARC reports, don't create a DMARC record.

### Create a Custom Return Path

Note  
  
Setting up DKIM is more likely to improve your deliverability than a custom return path. As a result, we recommend that you set up DKIM before or at the same time you set up a custom return path.

Email Delivery is required to process bounces to protect the reputation of our IP addresses and domain. Therefore, by default the Return Path is set to be that of our Bounce servers. Email Delivery offers a custom return path feature to improve inbox placement. To use this feature, you need to set up DNS records for your custom return path domain. The custom return path domain must either match the domain of your approved sender or be a subdomain of that domain.

For more information, see[Managing Custom Return Path](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Tasks/managing_custom_return_path.htm).

Our suggested naming convention for a custom return path subdomain is`<REGIONKEY>.rp.<sending-domain>`. To prepare for use of this feature, provision either SPF and MX records both or CNAME record on the custom domain as follows:

CNAME for Custom Return Path Domain

Create a CNAME with key as return path domain and value as regional bounce domain. The CNAME key value pair will be present in response of create custom return path request.

MX Record for Custom Domain

The following record syntax applies to commercial regions only:
```

```

Custom return path is regional. Adding REGION IDENTIFIER to the entry is imperative to avoid confusion. For more information about regions, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

SPF Record for Custom Return Path Domain

Sending Region SPF Record
Americas`v=spf1 include:rp.oracleemaildelivery.com ~all`
Asia/Pacific`v=spf1 include:ap.rp.oracleemaildelivery.com ~all`
Europe`v=spf1 include:eu.rp.oracleemaildelivery.com ~all`
All Commercial Regions`v=spf1 include:rp.oracleemaildelivery.com include:ap.rp.oracleemaildelivery.com include:eu.rp.oracleemaildelivery.com ~all`
Government Regions
- For US Government Cloud with FedRAMP Authorization, see[SPF Record Syntax](https://docs.oracle.com/iaas/Content/gov-cloud/govfedramp.htm#govfedramp_topic-SPF).
- For US Federal Cloud with DISA Impact Level 5, see[SPF Record Syntax](https://docs.oracle.com/iaas/Content/gov-cloud/govfeddod.htm#govfeddod_topic-SPF).
- For Oracle UK Sovereign Cloud, see[SPF Record Syntax](https://docs.oracle.com/iaas/Content/uk-sovereign-cloud/home.htm#SPF-record-syntax).

Note  
  
You must complete the DNS updates on your domain before the setup can be completed by Oracle Cloud Infrastructure.

After DNS changes are complete,[create a custom return path](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Tasks/creating_custom_return_path.htm)
