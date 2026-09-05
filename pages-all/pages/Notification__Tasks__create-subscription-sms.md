# Creating an SMS Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-sms.htm
- Fetched: 2026-09-05 02:49 CDT

# Creating an SMS Subscription

Create an SMS subscription in Notifications.

Note  
  
SMS subscriptions are limited to the OC1 commercial realm.

SMS subscriptions are enabled only for messages sent by the following Oracle Cloud Infrastructure services: Announcements, Monitoring, and Connector Hub. SMS messages sent by unsupported services are dropped. See[Cause: Unsupported resource used for SMS](https://docs.oracle.com/iaas/Content/Notification/Tasks/troubleshootingnotifications.htm#sms-unsupported-method).

Message contents and appearance vary by message type. See[SMS alarm messages](https://docs.oracle.com/iaas/Content/Monitoring/alarm-message-examples.htm#sms)and[SMS connector messages](https://docs.oracle.com/iaas/Content/connector-hub/message-examples.htm#top__sms).

By providing your phone number, you are opting-in to receive recurring SMS notifications for your organization. Reply STOP to opt-out at any time. Message and data rates may apply.

## Before You Begin

If SMS messages come from a phone number in another country, international SMS capabilities are required. We continuously add support for more countries so that more users can receive SMS messages from local phone numbers.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-sms.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-sms.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-sms.htm#)
- 

These steps show how to open the Create subscription panel from the details page for the topic that you want to add the subscription to. You can also open this panel from the[Subscriptions list page , specifying the topic in the panel: Select Create subscription , and then select a Subscription topic .

- On the Topics list page, select the topic that you want to work with. If you need help finding the list page or the topic, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- On the topic's details page, select Subscriptions .
- Select Create subscription .
- In the Create subscription panel, for Protocol , select SMS .
- Select the country for the phone number.
See the table following these steps.
- Enter the phone number, using[E.164 format](https://www.itu.int/rec/T-REC-E.164/en).
Example:`+14255550100`
- Select Create .

Notifications creates the SMS subscription and sends a confirmation URL to its endpoint. The confirmation URL is valid for three (3) days. The subscription is pending until confirmation is received.
- 

Use the[oci ons subscription create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/create.html)command and required parameters to create an SMS subscription:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[CreateSubscription](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/CreateSubscription)operation to create an SMS subscription.

Example:
```

```

## Available Countries and Regions

You can use Notifications to send SMS messages to the following countries and regions:

Country or region ISO code
Australia`AU`
Brazil`BR`
Canada`CA`
Chile`CL`
China`CN`
Costa Rica`CR`
Croatia`HR`
Czechia`CZ`
France`FR`
Germany`DE`
Hungary`HU`
India`IN`
Ireland`IE`
Israel`IL`
Japan`JP`
Lithuania`LT`
Mexico`MX`
Netherlands`NL`
New Zealand`NZ`
Norway`NO`
Philippines`PH`
Poland`PL`
Portugal`PT`
Romania`RO`
Saudi Arabia`SA`
Singapore`SG`
South Africa`ZA`
South Korea`KR`
Spain`ES`
Sweden`SE`
Switzerland`CH`
Ukraine`UA`
United Arab Emirates`AE`
United Kingdom`GB`
United States`US`

## What's Next

To activate the new SMS subscription, follow the instructions[received on the phone](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm#sms).

Although a new subscription must be in the same compartment as its parent topic, you can move it to another compartment after creation. See[Moving a Subscription to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/change-compartment-subscription.htm)
