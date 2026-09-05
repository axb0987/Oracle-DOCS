# Known Issues for Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/known_issue.htm
- Fetched: 2026-09-05 02:00 CDT

# Known Issues for Email Delivery

These known issues have been identified in Email Delivery

## JavaMail issues occur when many recipients are set in an email and one or more of the email addresses are suppressed

Details: When sending email to many recipients with a client using the JavaMail library, if one or more of the email addresses is on the suppression list, the Email Delivery service returns a 254 SMTP status code. This error indicates an email was submitted with a recipient address that's suppressed.

The JavaMail library can accept a list of recipients and send only the valid ones by setting the sendPartial flag. However, this code can't detect the new server status code for suppression and drop the suppressed addresses; instead, it stops the entire send and returns an exception. Applications need to catch this exception and remove the suppressed recipient from the recipient list to send to the valid recipients from the set only. That's, the application code can catch`com.sun.mail.smtp.SMTPAddressFailedException`and call`ex.getAddress()`with the exception object to get the addresses to remove, and resubmit with those removed.

Workaround: Actively monitor your suppression lists and update your sending lists, so that suppressed addresses aren't part of your email submission lists. For more information, see[Managing Suppression List](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/../Tasks/managingsuppressionlist.htm).

JavaMail was retired and moved to a replacement library called AngusMail, where developers fixed this issue in that library as of version 1.0.0 released in January 2022. For more details, visit their[changelog page for this release](https://github.com/eclipse-ee4j/angus-mail/compare/1.0.0-M1...1.0.0). Note that the bug #7 is the fix for this issue. AngusMail implements the JakartaMail specification and replaces JavaMail, so we recommend AngusMail for Java developers.

Direct link to this issue:[JavaMail issues occur when multiple recipients are set in an email and one or more of the email addresses are suppressed](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/known_issue.htm#javamail)

## Error occurs when attempting to add a suppression from a compartment other than root

Details: In the Console, if you select a compartment other than root and then navigate to the Email Suppression list, the following error will occur when you attempt to add a suppression:
```

```

Workaround: Navigate to the Approved Senders page, select the root compartment, and then return to the Email Suppression list.

Direct link to this issue:[Error occurs when attempting to add a suppression from a compartment other than root](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/known_issue.htm#suppressions)

## Unable to access SMTP credentials for older federated tenancies

Details: Federated users are supported for Email Delivery with the exception of older tenancies that do not use System for Cross-domain Identity Management (SCIM). SCIM will be the standard for all identity information access. All tenancies after Dec 2018 are SCIM.

Workaround: Ask an administrator in your Oracle Cloud Infrastructure tenancy to create a new user in the Console to be used with the Email Delivery service. Logging into the Console directly (not federated) will allow access to User Settings and SMTP Credentials.

Direct link to this issue:[Unable to access SMTP credentials for older federated tenancies](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/known_issue.htm#smtp)
