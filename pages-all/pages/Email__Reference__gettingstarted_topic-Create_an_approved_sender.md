# Creating an Approved Sender
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-Create_an_approved_sender.htm
- Fetched: 2026-09-05 02:00 CDT

# Creating an Approved Sender

Learn how to create an approved sender who can send emails using the OCI Email Delivery service.

An approved sender must be set up for all "From:" addresses sending mail through Oracle Cloud Infrastructure, or mail is rejected. An approved sender is associated with a compartment and only exists in the region where the approved sender was configured. That's, if you create an approved sender in the US West (Phoenix) region, you can't send email through the US East (Ashburn) region with that sender.

Best Practices : Approved senders must not be created in the root compartment. If approved senders exist in the root compartment, you're required to create a policy to manage approved senders in the entire tenant. Creating approved senders in a compartment other than the root ensures that the policy is specific to that compartment.

Use of multiple addresses in the email From header is discouraged. If you use multiple addresses, it increases the possibility that your mail is placed in a spam folder or discarded (because of DMARC From alignment rules). The performance of your emails is reduced because all addresses have to be authorized as approved senders. A best practice for the SMTP envelope From address is to match the header From address when you submit mail to Email Delivery. If you use mismatched addresses, it reduces the performance of your emails because both addresses need to be authorized as approved senders. Certain future platform features will not be available if you use mismatched addresses.

## Using the Console

- Open the navigation menu and select Developer Services . Under Application Integration , select Email Delivery . Under Email Delivery , select Approved Senders . Ensure that you're in the correct compartment. The user must be in a group with permissions to manage`approved-senders`in this compartment.
- Select Create Approved Sender .
- In the Create Approved Sender dialog box, provide the following information:

- Enter the email address that you want to list as an approved sender.
- (Optional) Add tags to organize resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask the administrator.
- Select Create Approved Sender .
The email address is added to Approved Senders list.

Tip  
  
Approved senders are unique to regions. If you try to create a duplicate approved sender within a region, the service returns a 409 Conflict error.
Note  
  
When an approved sender is created, it might not be immediately available for use. To work around this specific issue, we recommend that you create an approved sender and try to immediately use it. If an SMTP authorization failure occurs, perform a retry with backoff.
Tip  
  

Email Delivery supports "approved domains" enabling you to create a single Approved Sender to cover all addresses sharing the same domain. To achieve this:
- [Configure DKIM for the Email Domain](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Tasks/managing_dkim-setup_email_domain_with_dkim.htm), providing authorization to send from that domain.
-
