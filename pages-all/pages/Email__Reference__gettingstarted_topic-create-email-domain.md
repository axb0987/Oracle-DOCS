# Creating an Email Domain
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-create-email-domain.htm
- Fetched: 2026-09-05 02:00 CDT

# Creating an Email Domain

Learn how to create a DNS email domain to send bulk emails from approved senders.

## Using the Console

- Open the navigation menu and select Developer Services . Under Application Integration , select Email Delivery . Under Email Delivery , select Email Domains .
- Select Create Email Domain .
- Enter your email domain name. This requires to be a domain you own or control in DNS, because measures used to establish verification and authentication require a DNS record update or similar actions. It requires to be the domain you plan to use for approved senders, and can't be a public mailbox provider domain such as gmail.com, hotmail.com, yahoo.com, or oracle.com.

Tags : If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .

Tip  
  
To send email from many addresses with the same domain:
- Configure DKIM for the domain providing authorization to send from the domain.
- When DKIM is active, create the approved sender @domain.com .
Warning  
  
If DKIM isn't active, you can't create the approved sender.

## Create a Custom Return Path

Note  
  
Setting up DKIM is more likely to improve your deliverability than a custom return path. As a result, we recommend you set up DKIM before or at the same time you set up a custom return path.

Email Delivery is required to process bounces to protect the reputation of our IP addresses and domain. Therefore, by default the Return Path is set to be that of our Bounce servers. Email Delivery offers a custom return path feature to improve inbox placement. To use this feature, you need to set up DNS records for your custom return path domain. The custom return path domain must either match the domain of your approved sender or be a subdomain of that domain.

Our suggested naming convention for a custom return path subdomain is`<REGIONKEY>.rp.<sending-domain>`. To prepare for use of this feature, provision SPF and MX records on the custom domain as follows:

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

## Domain-based Message Authentication, Reporting, and Conformance (DMARC)

DMARC is a technical specification created by a group of organizations that want to help reduce the potential for email-based abuse by solving long-standing operational, deployment, and reporting issues related to email authentication protocols. DMARC standardizes how email recipients perform email authentication using SPF and DKIM. This gives the sender the ability to have control of mail that doesn't pass authentication and tell the email recipients what to do with non authenticated mail.

To send and deliver email, DMARC checks both SPF and DKIM and requires at least one to pass. When you start using DMARC, it's a best practice to put a`p=none`policy in place and ensure that every legitimate sending application is aligned and authenticated correctly before considering a more aggressive policy. During any transition period where a new email-related service for the sending domain is evaluated, using a DMARC`p=none`policy and following this advice is recommended.
A[DMARC record](https://tools.ietf.org/html/rfc7489)is a DNS TXT record in the domain`_dmarc.<sending-domain>`with content similar to the following:
```

```

You must have an administrative INBOX service to receive DMARC reports (in the preceding example,`example.com`
