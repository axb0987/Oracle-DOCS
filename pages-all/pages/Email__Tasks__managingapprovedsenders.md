# Managing Approved Senders
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managingapprovedsenders.htm
- Fetched: 2026-09-05 02:01 CDT

# Managing Approved Senders

Learn about managing approved senders using the Email Delivery service.

An approved sender must be set up for all "From:" addresses sending mail through Oracle Cloud Infrastructure, or mail is rejected. An approved sender is associated with a compartment and only exists in the region where the approved sender was configured. That is, if you create an approved sender in the US West (Phoenix) region, you cannot send email through the US East (Ashburn) region with that sender.

Use of multiple addresses in the email From header is discouraged. If you use multiple addresses, it increases the possibility that your mail is placed in a spam folder or discarded (because of DMARC From alignment rules). The performance of your emails is reduced because all addresses have to be authorized as approved senders. A best practice for the SMTP envelope From address is to match the header From address when you submit mail to Email Delivery. If you use mismatched addresses, it reduces the performance of your emails because both addresses need to be authorized as approved senders. Certain future platform features will not be available if you use mismatched addresses.

The approved senders that you add must use a domain name that you own and control. The following sending domains cannot be used to create approved senders:
- `@oracle.com`- This sending domain name is reserved for Oracle employee and corporate system use.
- `@*.oraclevcn.com`- This domain name is reserved for private use within an Oracle Cloud Infrastructure VCN. Email sending domains must have SPF and DKIM records that can be resolved on the public internet, and`oraclevcn.com`is only reachable within private Oracle Cloud Infrastructure networks. Use of this sending domain results in delivery delays, failures, and a possible blocklist addition.
- `@gmail.com`,`@hotmail.com`,`@yahoo.com`, and other public mailbox service providers - You cannot use a sending domain from a public mailbox service provider such as gmail, hotmail, icloud, yahoo, and so on. These providers tend to have restrictive DMARC records and will not delegate permission to third-party Email Delivery services (through SPF and DKIM records). Use of these sending domains results in delivery delays, failures, and a possible blocklist addition.

The following sending domain is problematic for use as an approved sender:
- `@oraclecloud.com`- This sending domain name is reserved for Oracle Cloud system use.

Approved senders should not be created in the root compartment. If approved senders exist in the root compartment, you're required to create a policy to manage approved senders in the entire tenant. Creating approved senders in a compartment other than the root allows the policy to be specific to that compartment.
You can perform the following approved senders management tasks:
- [Creating an Approved Sender](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/managingapprovedsenders_topic-create_an_approved_sender.htm)
- [Deleting an Approved Sender](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/managingapprovedsenders_topic-To_delete_an_approved_sender.htm)
- [Moving an Approved Sender](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/managingapprovedsenders_topic-move_an_approved_sender_to_a_different_compartment.htm)
- [Managing Tags for an Approved Sender](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/managingapprovedsenders_topic-manage_tags_for_an_approved_sender.htm)
