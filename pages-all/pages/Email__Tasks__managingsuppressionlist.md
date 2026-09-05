# Managing Suppression List
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managingsuppressionlist.htm
- Fetched: 2026-09-05 02:01 CDT

# Managing Suppression List

As you begin to send email, Email Delivery automatically adds email addresses with bounce codes showing permanent failures, or user complaints to the suppression list to protect the sender reputation. Email Delivery doesn't send any messages to these recipients in the future.

Reasons for suppression include:
- Complaints
- Hard bounces
- Manual entries
- [List-Unsubscribe](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/list-unsubscribe.htm)requests

The suppression mechanism is critical to protect the reputation of all emails from this service as repeated attempts to send to an invalid recipient results in the sender being considered a spammer by various anti-spam technologies. As a result, you can't opt out from the suppression mechanism.

You can know when a recipient email address has been added to the Suppression List, by enabling logs on your email domains. Log entries are created when an email bounces, or a recipient unsubscribes or files a spam complaint. Bounce log entries include the bounce reason as well, so you can know why the email didn't go through. For more information, see[Enabling Logs for Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/enablelogs_using-the-console.htm).

Common examples of hard bounces include either a misspelled email address or an invalid address because someone leaving a company, changing email providers, and so on. Another example is when a distribution list or email alias has an invalid recipient in which case the entire email alias is suppressed. The correct action in the latter case is to remove the invalid recipient from the alias and then remove the distribution list or email alias from the suppression list.

Another example is where the receiving mail server has a bug or is otherwise misconfigured, and a valid recipient returns an error. If you have verified this is the case, you can remove the suppression.

We highly recommend that you don't send emails to suppressed email addresses before the reason for their initial hard bounce is figured out. In rare cases, such as a distribution list where a single bad address can affect the whole list, an address can be removed and used to send emails again. Hard-bounced addresses such as incorrectly spelled email addresses or spam complaints must never be emailed to as the negatives (potential IP or domain block-listing) far outweigh any positives.

## Best Practices
Best practice to avoid suppression:
- Ensure that the sending domain has a valid DKIM, so that the recipient domain's postmaster doesn't block the mails.
- If you use DL (Distribution list), ensure that invalid or incorrect email addresses aren't part of the DL before sending emails again to the DL.

Manually add an email address to the suppression list to prevent it from being part of your sending list. Users must setup SPF and DKIM to help recipient email addresses from being automatically added to the suppression list in most of the cases. For more information, see[Configuring SPF](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/configurespf.htm)and[Using the Console](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/configure-dkim-using-the-console.htm#console).

## Permissions and Policies

Users are required to have correct permissions to manage the suppression list. Currently, identity policies for suppression must be at the tenant level (not at the compartment level). The following is an example of the permission policy statement.
```

```

Suppressions are stored at the tenancy level. Therefore, any request requiring a`compartmentId`must provide the`tenancyId`as the`compartmentId`. For example:
```

```

For other policies required for Email sending, see[Managing Approved Senders](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managingapprovedsenders.htm)and[Create SMTP Credentials](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/gettingstarted_topic-create-smtp-credentials.htm#console). Also, for advanced policies, see[Advanced Policy Features](https://docs.oracle.com/iaas/Content/Identity/policiesadvfeatures/policyadvancedfeatures.htm).
You can perform the following suppression list management tasks:
- [Adding an Email Address to the Suppression List](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/managingsuppressionlist_topic-add_an_email_address_to_the_suppression_list.htm)
- [Deleting an Email Address from Suppression List](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/managingsuppressionlist_topic-delete_an_email_address_from_the_suppression_list.htm)
