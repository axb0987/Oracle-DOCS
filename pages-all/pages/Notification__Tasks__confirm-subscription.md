# Confirming a Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm
- Fetched: 2026-09-05 02:49 CDT

# Confirming a Subscription

Confirm a subscription in Notifications. Confirmation isn't required for function subscriptions.

Navigate to the confirmation URL that's sent to the subscription's endpoint and follow the provided instructions.

The confirmation URL is valid for three (3) days. For steps to generate a new confirmation URL, see[Resending the Confirmation URL for a Subscription](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/resend-confirmation-subscription.htm).

For more information to find the confirmation URL, see the heading for the relevant subscription type (protocol).

## Email Confirmation URL

Search email for the text`To confirm this subscription`(used in the confirmation message).

## Function Confirmation URL

No confirmation URL exists. Confirmation isn't required for function subscriptions.

## HTTPS (Custom URL) Confirmation URL

Find the confirmation URL in the request header or body of the subscription confirmation message (request of content-type: "application/json") that's sent to the endpoint.
- 

In the request header, see the value of the`X-OCI-NS-ConfirmationURL`field.

Example request header:
```

```

See also[Standard header metadata](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#hownw__header).
- 

In the request body, see the value of the`ConfirmationURL`key.

Example ConfirmationURL key and value (request body):
```

```

## PagerDuty Confirmation URL

Incident titled "Oracle Notification Service Subscription Confirmation."

Example of confirmation incident (at the time this document was published)

## Slack Confirmation URL

Search the Slack channel for the text`To confirm the subscription`(used in the confirmation message).

## SMS Confirmation URL

Note  
  
Missing an SMS confirmation message? See[Cause: International SMS capabilities are missing](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm#sms-intl).

Search for the confirmation message that was sent to the phone number. The message sender and content depends on the country code of the recipient phone number.
- 

+1 country code:

Message sender: US-registered 10-digit long code number.

Message content:`REPLY 'CONFIRM <short-topic-id> ' to confirm subscription.`

&lt;short-topic-id&gt; is the short code of the topic that the SMS subscription was added to. The short code is used to identify the topic in messages sent to SMS subscriptions. Each short code contains six case-insensitive alphanumeric characters.
- 

Other country codes:

Message sender:
- If alphanumeric sender is supported:`OCINotify`
- If alphanumeric sender isn't supported: US-registered 10-digit long code number.

Message content:
```

```
