# FAQs for Custom Sender Address Scenarios
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/notifications/faqs_custom_sender_address_scenarios.htm
- Fetched: 2026-09-05 02:25 CDT

# FAQs for Custom Sender Address Scenarios

Learn how to address issues with the custom sender address when migrating to the Email Delivery service.

## If I'm using a custom sender address (and DKIM), do I have to make any changes after migrating to the Email Delivery service?

No, you're not required to perform any changes or take any actions. If you have currently configured DKIM in CNS, your data will be automatically be migrated to a secure service location to ensure notifications continue to work using the Email Delivery service.

## If I have an SPF configuration, do I have to make any changes after migrating to the Email Delivery service?

If you have configured[oracle.com](http://oracle.com/)SPF record. Then we recommend you to update -[Configuring SPF](https://docs.oracle.com/iaas/Content/Email/Tasks/configurespf.htm).

## What's the onboard process if I want to configure Email Authentication using DKIM?

Please follow the process at:[Configuring Email Authentication Settings for SPF and DKIM](https://docs.oracle.com/en-us/iaas/Content/Identity/notifications/configure-email-auth-spf-dkim.htm).

## What will be the email address verification process for customers who use a custom Sender's email address after migrating to the Email Delivery service?

Current Behavior with CNS: When you configure a custom Sender's email address, you can click the Check Status button on the Notifications page, which invokes CNS. CNS internally triggers an email to the email address that includes a verification link (for custom email domains, the email is sent to the Postmaster account of the email domain). While verification is pending from the customer, IAM continues to send email notifications using the default sender address. When you click the verification link, a browser opens and CNS registers your verification for the email address (or the email domain). IAM polls the CNS API on-demand to determine the verification status. Once CNS registers the customer's verification activity, the CNS API will respond to IAM with a verified status for the email domain. IAM then internally marks the sender's email address as Verified and uses the new sender address for subsequent email notifications in the customer's stripe.

New Behavior with Email Delivery Service: The Email Delivery service currently lacks the capability for customers to self-verify their email addresses (or email domains). Important: Because of this limitation, the Check Status feature in the IAM Notification settings will be deprecated following the migration to the Email Delivery service. If you wish to use custom email addresses, you will need to follow a new verification workflow by submitting a Service Request. The internal process for handling these Service Requests after the migration will be communicated to the Identity Support and Engineering teams.

## Will there be any changes to Email Template customizations?
