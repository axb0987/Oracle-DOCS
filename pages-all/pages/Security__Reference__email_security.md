# Securing Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/email_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Email Delivery

The Email Delivery service offers an SMTP endpoint, secured by a password generated in the Console. The SMTP password is required for sending emails using Email Delivery. Oracle recommends that you create a separate IAM user for SMTP. This user must have manage permissions for`approved-senders`and`suppressions`resource types. Oracle recommends that you securely store the SMTP credential, and periodically rotate it. For more information about generating an SMTP credential for Email Delivery, see[Create SMTP Credentials](https://docs.oracle.com/iaas/Content/Email/Reference/gettingstarted_topic-create-smtp-credentials.htm).

For Email Delivery best practices, including managing your sender reputation and help for avoiding being blocklisted, see[Email Deliverability](https://docs.oracle.com/iaas/Content/Email/Reference/deliverabilitybestpractices.htm).  

- [Creating SMTP Credentials](https://docs.oracle.com/iaas/Content/Email/Reference/gettingstarted_topic-create-smtp-credentials.htm)
