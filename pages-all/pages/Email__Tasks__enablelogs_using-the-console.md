# Enabling Logs for Troubleshooting
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/enablelogs_using-the-console.htm
- Fetched: 2026-09-05 02:01 CDT

# Enabling Logs for Troubleshooting

Email Delivery integrates with the Logging service to provide service logs for Email Domains. Email Domain Logs provide detailed information on email submission, relaying or delivery, and recipient interaction (including bounces, spam complaint, unsubscribes, and engagement).

You can enable logs with the[Deliverability Dashboard page](https://docs.oracle.com/iaas/Content/Email/Reference/dashboard-topic-enabling-logging.htm), on the Console details page for any Email Domain, or[through the Logging service itself](https://docs.oracle.com/iaas/Content/Logging/Task/enabling_logging.htm).

Enabling email service logs for a sending domain before sending an email ensures that a log is generated whenever an email is sent from that email domain.

When a user doesn't receive an email sent to their email domain, the missing email can be tracked through the generated email service log when the email was sent provided they had enabled email service logs before sending the email.

To enable logs using the details page of an Email Domain:
- Open the navigation menu and select Developer Services . Under Application Integration , select Email Delivery . Under Email Delivery , select Email Domains .
- Select the name of the email domain where you want to enable logs. We recommend that you enable logs for all domains.
Note  
  
If you don't see the expected domain, check that you're in the proper compartment.
- On the Email Domains Details page, under Email Domains , Select Logs . The Logs section lists the categories Outbound Accepted and Outbound Relayed .
- To enable Outbound Accepted or Outbound Relayed logs, from the Actions menu (three dots) of Outbound Accepted or Outbound Relayed , select Enable log .
Note  
  

See the[Logging Details for Email Delivery page](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_emaildelivery.htm)in the OCI Console for detailed information and example log records for each of the supported log categories. You can search these logs using the[Deliverability Dashboard](https://cloud.oracle.com/messaging/email/dashboard), or the more powerful[Logging Search page](https://docs.oracle.com/iaas/Content/Logging/Concepts/searchinglogs.htm). OCI also offers an[API method for searching logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/using_the_api_searchlogs.htm)
