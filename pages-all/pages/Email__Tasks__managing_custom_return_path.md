# Managing Custom Return Path
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_custom_return_path.htm
- Fetched: 2026-09-05 02:01 CDT

# Managing Custom Return Path

Use custom return path to improve your inbox placement and monitor email bounces when bulk emails are sent.

A return path address is an SMTP address used by email senders to receive notifications about email bounces. It is the email address in the hidden header of an email where bounce notifications are sent. Email Delivery uses the return path address to process the bounces and protect the reputation of your IP addresses and domain. Therefore, by default the return path is set to be that of our Bounce servers.

Use custom return paths to override the default return path set in outgoing emails and brand the emails with your own domain to increase sending reputation.
To set up a custom return path, ensure that:
- Custom return path domain is a subdomain of your email domain.
- Either DKIM is set up for your email domain or your email domain is verified.
Note  
  

- To check if your email domain is verified or not, see[creating an email domain](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/configureemaildomains-create-an-email-domain.htm#console).
- To register your domain with OCI, see[Managing Your Domains](https://docs.oracle.com/iaas/Content/GSG/Concepts/managing_your_domains.htm).
- DNS records for the custom return path domain is set up.
- Verify the custom return path domain within your domain's DNS settings.
- Add CNAME record and CNAME value to the DNS zone of your email sending domain for the custom return path to become active. For more information, see[Creating Custom Return Path](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/creating_custom_return_path.htm).
- Update DNS records within 72 hours of creating the custom return path record. If the required DNS record isn't created within 72 hours, then custom return path record state is automatically updated to Failed . To create a new custom return path with same return path domain, delete the failed custom return path record.
Use the following operations to manage custom return path:
- [Creating Custom Return Path](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/creating_custom_return_path.htm)
- [Viewing Custom Return Path](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/viewing_custom_return_path.htm)
- [Deleting Custom Return Path](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/deleting_custom_return_path.htm)

## Required IAM Policy

Learm about the required policies to manage custom return path.

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about policies for Email Delivery, see[Details For the Email Delivery Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/emailpolicyreference.htm).

To enable all operations on all email resources for a specific user group, use the following policy:
```

```
