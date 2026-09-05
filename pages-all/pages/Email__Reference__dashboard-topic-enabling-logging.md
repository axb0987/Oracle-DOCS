# Enabling Logs using the Deliverability Dashboard
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/dashboard-topic-enabling-logging.htm
- Fetched: 2026-09-05 02:00 CDT

# Enabling Logs using the Deliverability Dashboard

Email Delivery integrates with the Logging service to provide service logs for Email Domains. Email Domain Logs provide detailed information on email submission, relaying/delivery, and recipient interaction (including bounces, spam complaints, unsubscribes, and engagement).

You can enable logs with the[Deliverability Dashboard page](https://cloud.oracle.com/messaging/email/dashboard), on the web Console details page for any Email Domain, or[through the Logging service itself](https://docs.oracle.com/iaas/Content/Logging/Task/enabling_logging.htm).

To enable logs using the Deliverability Dashboard:
- Open the navigation menu and select Developer Services . Under Application Integration , select Email Delivery . Under Email Delivery , select Deliverability Dashboard .
- Scroll to Deliverability Logs .
- Select Compartment filter if it’s not already chosen. If logs are not enabled for any Email Domain, a banner appears.
- Select Enable logging for domains . The Enable Resource Logging panel appears
- Under Select Resource section, choose the compartment that contains the Email Domain(s) to log.
- Choose to enable logs for all Email Domains or only for specific domains. If you choose specific domains, select them.
- Under Logs Location and Configuration , select the compartment and Log Group to store your logs.
- Select whether to create a new Log Group or use an existing one. If using an existing group, select it.
- Under Advanced options , you can optionally specify a retention policy.
- If you use Tags , specify them.
- Select Enable . The log or logs are created as specified.
Note  
  
New logs only include events that occur after logging is enabled. Events that occurred before enabling logs are not included.
Note  
  

See the[Logging Details for Email Delivery page](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_emaildelivery.htm)in the OCI Console for detailed information and example log records for each of the supported log categories. You can search these logs using the[Deliverability Dashboard](https://cloud.oracle.com/messaging/email/dashboard), or the more powerful[Logging Search page](https://docs.oracle.com/iaas/Content/Logging/Concepts/searchinglogs.htm). OCI also offers an[API method for searching logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/using_the_api_searchlogs.htm)
