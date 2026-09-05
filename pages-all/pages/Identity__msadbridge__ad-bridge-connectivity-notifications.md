# AD Bridge Connectivity Notifications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/ad-bridge-connectivity-notifications.htm
- Fetched: 2026-09-05 02:24 CDT

# AD Bridge Connectivity Notifications

Learn about notifications that IAM sends to the tenant admin when connectivity between AD bridge and the IAM server is broken, and also when it is restored.

## Notifications sent when connectivity of AD Bridge with IAM server is broken

Oracle sends notifications to the tenant admin when connectivity between AD bridge and the IAM server is broken. Connectivity could be broken for any of a number of reasons, for example if the AD bridge is stopped, or if the IAM is stopped on the Windows machine.

The notifications have the email subject: Connectivity to AD bridge &lt;windows machine name&gt; is unreachable.

## Notifications sent when connectivity of AD bridge with IAM is restored

Similarly, when connectivity is restored, an email is sent from Oracle to the tenant administrator.

The notifications have the email subject: Connectivity to AD bridge &lt;windows machine name&gt; is restored.
