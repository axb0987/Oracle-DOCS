# Setting up an Email Domain with DKIM
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-setup_email_domain_with_dkim.htm
- Fetched: 2026-09-05 02:01 CDT

# Setting up an Email Domain with DKIM

Learn about the process to set up a sending domain with DKIM.

Here's the general process for setting up a sending domain with DKIM:
- Create the email domain, if it doesn't exist already: An[email domain](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/configureemaildomains.htm)lets you set up important authentication measures for sending email, essential to ensure good email delivery reputation. See[Creating an Email Domain](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/configureemaildomains-create-an-email-domain.htm).
- Configure DKIM: Configure DKIM for this email domain. This is an important step to help ensure email is delivered and reaches the inbox. See[Configuring DKIM](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/configure-dkim-using-the-console.htm).
- Add the DKIM record to customer's DNS setup: Provide the system generated CNAME record and value generated in step 2 to the customer's DNS administrator to publish them at the customer's DNS provider.

To know which DNS system to use, consult the nameservers for the domain. OCI DNS (see[Zones](https://docs.oracle.com/iaas/Content/DNS/Tasks/managingdnszones.htm)) would be used only if the domain's nameservers point to OCI. If your DNS setup resides with another provider, see their documentation for adding records to your domain. See the following documentation links for several common providers:
- [Dreamhost](https://www.dreamhost.com/)
- [GoDaddy](https://www.godaddy.com/help/add-a-cname-record-19236)
- [HostGator](https://www.hostgator.com/)
- [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/317/2237/how-do-i-add-txtspfdkimdmarc-records-for-my-domain)
- [Names.co.uk](https://www.names.co.uk/support/articles/changing-your-domains-dns-settings/)
- [Wix](https://support.wix.com/en/article/adding-or-updating-cname-records-in-your-wix-account)

The following diagram illustrates how a sender domain DNS server can be used to store the CNAME record that contains the DKIM key that points back to OCI DNS. This setup is preferred as it makes key rotation easier. However, if needed, you can request the key and directly store the key.
[

The following diagram illustrates how a DKIM key can be stored directly in a DNS setup.
[
- Set up approved senders: Approved senders must be set up for all "From:" addresses sending mail through Oracle Cloud Infrastructure, or mail is rejected. Setting up approved senders is essential to ensure good email delivery reputation. The DKIM key set up for the domain is automatically associated with ALL approved senders in that domain. Approved senders can use a DKIM-configured sending domain to become verified. See[Managing Approved Senders](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managingapprovedsenders.htm)for more information. Only approved senders with the exact domain including subdomain will be signed by your new key. For example,`noreply@sample.com`will not gain the dkim key associated with`mysubdomain.sample.com`
