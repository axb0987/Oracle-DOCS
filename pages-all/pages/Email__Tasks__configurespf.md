# Configuring SPF
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/configurespf.htm
- Fetched: 2026-09-05 02:01 CDT

# Configuring SPF

Configure Sender Policy Framework (SPF) to detect email spoofing and to send emails securely using Oracle Cloud Infrastructure Email Delivery service.

[About SPF](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/configurespf.htm#)

Sender Policy Framework (SPF) is used by email receivers to detect email spoofing. Using SPF, an email receiver can check if the Internet Protocol (IP) is explicitly authorized to send for that domain. SPF is implemented by publishing a special TXT record to a domain's DNS records. The TXT record declares which hosts are allowed to send mail on behalf of this domain. Receiving mail servers check the SPF records of sending domains to verify that the email's source IP address is authorized to send from that domain. Without SPF, a spam or phishing email can be "spoofed" to appear that the email comes from a legitimate domain. Domains that implement SPF are much more likely to block emails attempting to spoof your domain. For an overview of how SPF works, see[Sender Policy Framework](http://www.open-spf.org/Introduction). For details on SPF record syntax, see[SPF Record Syntax](http://www.open-spf.org/SPF_Record_Syntax).

Approved senders can use a DKIM-configured sending domain to become verified. See[Managing Approved Senders](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managingapprovedsenders.htm)for information on how to add an approved sender.

The Approved Senders section within the Console provides validation of an SPF record for each of your approved senders. SPF is required for subdomains of`oraclegovcloud.com`and recommended in other cases.

In your DNS setup, create a Text record (TXT) to store information about the SPF records and paste the following information into it based on the sending region:
Note  
  

- To add DNS records, the domain must be registered and available on the public Internet. DNS records must be added using the domain's registered DNS provider, which is the DNS system that the domain's nameservers point to.
- Don't add a subdomain or name in the SPF text records on an existing DNS zone.

Sending Region SPF Record
Americas`v=spf1 include:rp.oracleemaildelivery.com ~all`
Asia/Pacific`v=spf1 include:ap.rp.oracleemaildelivery.com ~all`
Europe`v=spf1 include:eu.rp.oracleemaildelivery.com ~all`
All Commercial Regions`v=spf1 include:rp.oracleemaildelivery.com include:ap.rp.oracleemaildelivery.com include:eu.rp.oracleemaildelivery.com ~all`
Government Regions
- For US Government Cloud with FedRAMP Authorization, see[SPF Record Syntax](https://docs.oracle.com/iaas/Content/gov-cloud/govfedramp.htm#govfedramp_topic-SPF).
- For US Federal Cloud with DISA Impact Level 5, see[SPF Record Syntax](https://docs.oracle.com/iaas/Content/gov-cloud/govfeddod.htm#govfeddod_topic-SPF).
- For Oracle UK Sovereign Cloud, see[SPF Record Syntax](https://docs.oracle.com/iaas/Content/uk-sovereign-cloud/home.htm#SPF-record-syntax).
Other Regions Use the following syntax for any other region:`v=spf1 include:rp.email.oci.<realm-public-domain>`
Examples for public domains of a few regions:
- OC8: rp.email.oci.jpsovereigncloud.jp
- OC19: rp.email.oci.oraclecloud.eu
- OC22: rp.email.oci.psn-pco.it
- OC23: rp.email.oci.oraclecloud23.com
- OC25: rp.email.oci.nricloud.jp
- OC35: rp.email.oci.oraclecloud35.com

The following is an example of a command used to view an SPF record:

```

```

Example output:
```

```
