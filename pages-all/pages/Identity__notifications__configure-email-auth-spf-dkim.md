# Configuring Email Authentication Settings for SPF and DKIM
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/notifications/configure-email-auth-spf-dkim.htm
- Fetched: 2026-09-05 02:25 CDT

# Configuring Email Authentication Settings for SPF and DKIM

If you have configured a non-Oracle domain as the From Email Address for your notifications, then you must configure the email authentication settings for Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM) so that you can certify the domain. Oracle Support must help with the configuration.

- You create a service request. See[Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
- Oracle configures SPF. Add an SPF record to the domain of the`from`address to include the Oracle Cloud Infrastructure email delivery domain. The SPF record statement to be configured is documented here:[Configuring SPF](https://docs.oracle.com/iaas/Content/Email/Tasks/configurespf.htm).
- Oracle registers DKIM. Send Oracle DKIM information. In the Service Request in My Oracle Cloud Support , include the following details:
- IDCS domain name
- from address: The domain name that will be used to send emails.
- selector name: Oracle generates a default. Check whether your DNS/email team requires a specific format.
- The Identity support team will provide CNAME record and value that can be used in your DNS set up for your email domain configuration.
Note  
  
To add DNS records, the domain must be registered and available on the public Internet. DNS records must be added using the domain's registered DNS provider, which is the DNS system that the domain's nameservers point to.
Note
