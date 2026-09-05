# Managing Email Domains
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/configureemaildomains.htm
- Fetched: 2026-09-05 02:01 CDT

# Managing Email Domains

Set up important authentication measures for sending emails to ensure good email delivery reputation.

An email domain lets you set up important authentication measures for sending email, essential to ensure good email delivery reputation. An email domain also lets you set up logging for visibility into your email traffic. Your email domain needs to be a domain you own or control in DNS, because measures used to establish verification and authentication require a DNS record or similar actions. It requires to be the domain you plan to use for your[approved sender](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managingapprovedsenders.htm)email address for sending, and cannot be a public mailbox provider domain such as gmail.com or hotmail.com. After setting up email domains, it is recommended that you[create approved senders](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managingapprovedsenders.htm)and[configure SPF](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/configurespf.htm).
You can perform the following email domain management tasks:
- [Creating an Email Domain](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/configureemaildomains-create-an-email-domain.htm)
- [Deleting an Email Domain](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/configureemaildomains_delete_domains.htm)
- [Moving an Email Domain](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/configureemaildomains_moving_domain.htm)

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about policies for Email Delivery, see[Details For the Email Delivery Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/emailpolicyreference.htm).

To enable all operations on all email resources for a specific user group, use the following policy:
```

```
