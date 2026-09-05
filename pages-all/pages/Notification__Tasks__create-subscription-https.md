# Creating an HTTPS (Custom URL) Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-https.htm
- Fetched: 2026-09-05 02:49 CDT

# Creating an HTTPS (Custom URL) Subscription

Create an HTTPS (Custom URL) subscription in Notifications.

## Before You Begin

Ensure that the URL endpoint that you plan to use for the subscription meets the following requirements: Authentication Only Basic Access Authentication is supported. For more information, see[RFC-2617: HTTP Authentication: Basic and Digest Access Authentication](https://datatracker.ietf.org/doc/html/rfc2617). You can specify a username and password in the URL, as in`https://user:password@domain.com`or`https://user@domain.com`. In the URL, encode (escape) the characters noted at[RFC-3986: Uniform Resource Identifier (URI): Generic Syntax](https://datatracker.ietf.org/doc/html/rfc3986). Certificates Only valid certificate authority (CA) certificates are trusted. No self-signed certificates are allowed. Encryption As with any subscription protocol, data in the endpoint (including username and password if supplied in the URL) is encrypted in transit over the SSL connection established when using HTTPS, and at rest in the service database. POST calls The endpoint that you provide must accept POST calls. The Notifications service uses POST calls to send messages to HTTPS (custom URL) endpoints.
Note  
  
Connection and read timeouts for HTTPS (custom URL) deliveries are both fixed at 5 seconds. To avoid delivery failures, your endpoint must complete the TLS handshake and begin returning a response body within this window. Public accessibility

The endpoint for the HTTPS (Custom URL) subscription must be publicly accessible.

Notifications doesn't support private endpoints for HTTPS (Custom URL) subscriptions. Notifications makes an HTTP POST request to your endpoint through the public internet when you create an HTTPS (Custom URL) subscription in a topic.

To check if your endpoint is publicly accessible, make a sample POST request from your local machine.

Example:
```

```

If your endpoint is publicly accessible, then the command returns the following HTTP status code:
```

```
Unauthorized header

The client service must be able to support the`HTTP/1.1 401 Unauthorized header`response. When your endpoint receives an unauthenticated request, it should return that response with a`WWW-Authenticate`header. The header value should contain the keyword`Basic`and other optional parameters supported in[RFC-2617: HTTP Authentication: Basic and Digest Access Authentication](https://datatracker.ietf.org/doc/html/rfc2617).

Example:
```

```

Query parameters aren't allowed in URLs. Custom HTTP header parameters aren't supported. When sending a message to the URL endpoint, the Notifications service adds[standard metadata to the HTTP request in the header](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Concepts/notificationoverview.htm#hownw).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-https.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-https.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription-https.htm#)
- 

These steps show how to open the Create subscription panel from the details page for the topic that you want to add the subscription to. You can also open this panel from the[Subscriptions list page , specifying the topic in the panel: Select Create subscription , and then select a Subscription topic .

- On the Topics list page, select the topic that you want to work with. If you need help finding the list page or the topic, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- On the topic's details page, select Subscriptions .
- Select Create subscription .
- In the Create subscription panel, for Protocol , select HTTPS (Custom URL) .
- Enter the URL that you want to use as the endpoint, using the following format:

```

```

Note  
  
Ensure that the URL meets the requirements provided at the beginning of this help topic. Query parameters aren't permitted in URLs.
- Select Create .

Notifications creates the HTTPS (Custom URL) subscription and sends a confirmation URL to its endpoint. The confirmation URL is valid for three (3) days. The subscription is pending until confirmation is received.
- 

Use the[oci ons subscription create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/subscription/create.html)command and required parameters to create an HTTPS (Custom URL) subscription:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[CreateSubscription](https://docs.oracle.com/iaas/api/#/en/notification/latest/Subscription/CreateSubscription)operation to create an HTTPS (Custom URL) subscription.

## What's Next

To activate the new subscription, navigate to the[confirmation URL](https://docs.oracle.com/iaas/Content/Notification/Tasks/confirm-subscription.htm#https)that was sent to the HTTPS endpoint.

Although a new subscription must be in the same compartment as its parent topic, you can move it to another compartment after creation. See[Moving a Subscription to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/change-compartment-subscription.htm)
