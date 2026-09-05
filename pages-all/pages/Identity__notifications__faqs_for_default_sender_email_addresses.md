# FAQs for Default Sender Address Scenarios
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/notifications/faqs_for_default_sender_email_addresses.htm
- Fetched: 2026-09-05 02:25 CDT

# FAQs for Default Sender Address Scenarios

Learn how to address issues with the default sender address when migrating to the Email Delivery service.

## What will be the default Sender's email address be after Identity Domains migrates to the Email Delivery service?

For OC1, the default email address will be`no-reply@identity.oci.oraclecloud.com`.

For DRCC and Gov realms, the default email address will be`no-reply@identity.oci.<public-realm-domain>`. To determine the`<public-realm-domain>`for a given realm, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).

## Do I have to manually change the sender from no-reply@oracle.com to no-reply@identity.oci.oraclecloud.com?

No, the Identity service will automatically apply the change for those customers who are currently using`no-reply@oracle.com`as the 'from sender address'.

## Do I have to make any change in my email client?

If you've applied rules or filters for emails originating from`no-reply@oracle.com`(at the recipient email server), we recommend that you update the rules to include`no-reply@identity.oci.oraclecloud.com`.

## Will existing OCI customers who currently use only the Email Delivery Service be impacted by this migration?

No, existing customers who use the Email Delivery Service will experience no interruptions in their usage.

## Does this impact my use of the Email Delivery Service for email notifications?

No, the change will not affect your existing Email Delivery Service configuration or usage.

## Will there be any changes to Email Template customizations?
