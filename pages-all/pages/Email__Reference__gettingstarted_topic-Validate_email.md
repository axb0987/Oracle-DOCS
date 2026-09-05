# Validating Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-Validate_email.htm
- Fetched: 2026-09-05 02:00 CDT

# Validating Email Delivery

Learn how to use the Oracle Cloud Infrastructure Logging service to validate whether an email is delivered.

Use the OCI Logging service to search for the Email Delivery service logs and validate whether your email is delivered.

## Using the Console

- Open the navigation menu and click Observability &amp; Management . Under Logging , select Search .
- In the Custom Filters , you can start typing to automatically display filter settings, along with operators. For example, entering`d`displays filters starting with that letter. Use the up or down arrow keys to select from the list, or continue typing to enter what you want to filter on. For example,`data.recipient =testing@tester.com`.

Two logs are displayed based on the emails sent to`testing@tester.com`. One that confirms the email was received by OCI Email Delivery service`(action = Accepted)`and one that confirms the email was relayed to the mailbox provider`(action = relayed)`.

Because no bounce log exists (action = bounce) for this email, the recipient's mailbox provider accepted responsibility for the message and delivered it to the recipient if it met the recipient domain's policy
- To see log event details, use the expansion list arrow across a listed log. For more information, see[email service log documentation](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_emaildelivery.htm#details_for_emaildelivery)
