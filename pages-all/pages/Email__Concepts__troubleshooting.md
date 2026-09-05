# Troubleshooting Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/troubleshooting.htm
- Fetched: 2026-09-05 02:00 CDT

# Troubleshooting Email Delivery

Use troubleshooting information to identify and address common issues that can occur while working Email Delivery.

This topic provides troubleshooting solutions for problems you might encounter using Email Delivery.

## Common Errors Returned by Email Delivery

### API Errors

For a complete list of common API email delivery errors returned by all the services for Oracle Cloud Infrastructure, see[API Errors](https://docs.oracle.com//iaas/Content/API/References/apierrors.htm).

### Common SMTP Errors Returned by Email Delivery

The following table lists the common errors returned by the Email Delivery SMTP service.

SMTP Status Code Error Code Description
254`4.7.1 Suppression for user <user ocid> to <recpt>`Message has been accepted but a status code was returned indicating suppression.

Enhanced Status Code 4.7.1 indicated a persistent transient failure ([RFC3463](https://www.iana.org/go/rfc3463)).
421`Timeout waiting for data from client`
421`4.4.0 Problem attempting to execute commands. Please try again later`
421`Too many connections, try again later`
421`Too many auth failures, try again later`IP based throttle; triggered by repetitive use of invalid SMTP credentials or non-approved sender.
421`4.3.0 Mail system failure, closing transmission channel`
451`Server error`An unexpected error has occurred during the SMTP conversation.
451`Error in Processing`An unexpected error has occurred during the SMTP conversation.
452`System storage error`The server is unable to persist the message in its delivery queue.
455`Maximum messages sent per minute reached : limit is <limit>`The SMTP send burst rate (of messages accepted per minute period) has been exceeded.
455`Maximum messages sent per day reached : limit is <limit>`The SMTP daily send rate (of messages accepted per 24 hour period) has been exceeded.
501`Invalid command argument, not a valid Base64 string`

The base64 encoded AUTH (PLAIN) secret is invalid.
501`Invalid command argument, does not contain NUL`The base64 encoded AUTH (PLAIN) secret does not contain NUL field separator(s).
501`Invalid command argument, does not contain the second NUL`The base64 encoded AUTH (PLAIN) secret does not contain second NUL field separator(s).
503`Need RCPT command`The SMTP client tried to start sending the body of an email message without identifying any email recipients through the required SMTP RCPT command (RFC 5321).
504`Method not supported`The client has attempted to use an unsupported AUTH mechanism with our service.
504`AUTH mechanism mismatch`The client has sent an invalid AUTH command to our service.
552`Exceeds byte limit`The message has exceeded the size limit enforced by the service (see server response to EHLO for size restriction).
535`Authentication credentials invalid`Authentication of the SMTP user has failed.
535`Authentication required`The client has sent commands that require SMTP authentication succeeded before the service is able to process (that is, commands are being sent out of order).
535`Authorization failed: address <address> not authorized`

Authorization of the address (either in the envelope or message) has failed for the SMTP user.

The approved sender does not exist, the`use email-family`policy does not specify the compartment containing the approved sender, or the user with the SMTP credentials is not in a group with the`use email-family`policy. See[Create SMTP Credentials](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/../Reference/gettingstarted_topic-create-smtp-credentials.htm#console)for more information.
553`<address> Invalid email address`The RFC-822 Internet Address sent by the client is invalid.
554`Message parse error`The RFC-2822 Internet Message is invalid (and unable to be parsed by the server).

Message without any headers or header is larger than 256 KB.

### Common HTTPS Errors Returned by Email Delivery

The following table lists the common errors returned by the Email Delivery HTTPS service.

HTTPS Status Code HTTPS Designation Error Code Examples
200 The action was successful The response contains the response parameters.
400 InvalidParameter Message ID not formed according to RFCs.
400 InvalidParameter Email Address can't be null or empty.
400 InvalidParameter Invalid Internet Address : &lt;address&gt;
400 InvalidParameter maxItems: 50, for recipients across the To:, CC: and BCC: fields.
400 InvalidParameter Header Key can't be null or empty
400 InvalidParameter Custom Mail Header Keys should be ASCII only &lt;header&gt;
400 InvalidParameter &lt;header&gt; is a reserved mail header which is not allowed
400 MissingParameter Required attribute sender compartmentId cannot be empty or null.
400 MissingParameter Required attribute subject can't be empty or null.
400 MissingParameter Required attribute sender can't be empty or null.
400 MissingParameter Required attribute recipients must contain either to , cc or bcc recipients.
400 MissingParameter Required attribute body(html/text) is missing. Request must contain either bodyText or bodyHtml
400 LimitExceeded Maximum messages sent per minute reached : limit is &lt;&gt;Maximum messages sent per day reached : limit is &lt;&gt;
404 NotAuthorizedOrNotFound Authorization failed: address &lt;Sender Email Address&gt; not authorized or not found
409[ResourceLocked](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm#apierrors_409__409_resourcelocked)The requested resource is locked. This is usually because the resource is in active use, or because modifying the resource will cause another resource to stop functioning.
413 Request Entity Too Large Message exceeds byte limit : limit is &lt;&gt;
429 Too many requests Too many requests received. Wait and try again.
500 Internal server error Internal Server Error

## Undelivered Emails Issues

Identify and fix issues that prevent your emails from getting delivered.

The following issues can cause an email to be undelivered:
- The recipient is on the Suppression List.
- An authentication failure or an issue with the format of the email message occurred. For example, if the SMTP "From" address is not the same as the "From" address in the email body, the email is rejected. The addresses must match and be an Approved Sender. Refer to your sending application's logs to review any issues.
- Use of multiple addresses in the email From header is discouraged. If you use multiple addresses, it increases the possibility that your mail is placed in a spam folder or discarded (because of Domain-based Message Authentication, Reporting, and Conformance (DMARC) From alignment rules). The performance of your emails is reduced because all addresses have to be authorized as approved senders. A best practice for the SMTP envelope From address is to match the header From address when you submit mail to Email Delivery. If you use mismatched addresses, it reduces the performance of your emails because both addresses need to be authorized as approved senders. Certain future platform features will not be available if you use mismatched addresses.
- Lack of Domain Keys Identified Mail (DKIM).
- View the "dkimSelector" applied to your mail via the[Public Logging](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_emaildelivery.htm)feature.

DKIM and DMARC can help authenticate your email to help ensure that your emails get delivered to your recipients' inboxes. For more information, see[More Options to Increase Deliverability](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/../Reference/deliverabilitybestpractices_topic-bestpractices.htm#options).

See[Best Practices](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/../Reference/deliverabilitybestpractices_topic-bestpractices.htm)to learn about recommendations that can help lower your email bounce rate, stay off blocklists, lower your complaint rate, and improve your email sender reputation.

If you're unable to resolve the issue, you can go to My Oracle Support and create a service request. See[Open a support service request](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm)for more information.

## Connectivity Issues

Note  
  
Email Delivery does not prohibit connectivity from any source IP range. Any IP that attempts to connect to Email Delivery will be accepted.

Refer to[Configuring SMTP Connection](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/../Reference/gettingstarted_topic-Configure_the_SMTP_connection.htm)for a list of regional endpoints to establish SMTP connections for sending.

### Issue Connecting to Email Delivery Endpoints

Fix connectivity issues that prevent you from connecting to endpoint network ports.

- Ensure that you have the correct endpoint DNS name or IP address for the region and that you have been allowlisted to use the endpoint.
- Test connectivity to the endpoint using any of the supported ports: 25, 587, or 465. Use a utility such as telnet (port 25 + 587) or openssl (port 465) to attempt to connect to the port manually.
- Open a command prompt.
- Use the following command to test the network connection.

```

```

For example:

```

```

The port is open and the test is successful if you see a "Connected to" message. If you are unable to connect to the ports using telnet, you are experiencing a network connectivity issue.

### Issue Connecting to a Recipient Email Domain

Fix connectivity issues that prevent you from connecting to the mail server for a recipient email address, such as gmail.com, outlook.com, or a company's email server.

Perform the following steps to determine whether you are able to communicate with the email recipient's mail server. Email Delivery delivers mail to recipient email servers over port 25, so this is the port to test in this case. If you are unable to connect successfully, the recipient email server may be offline, misspelled, or otherwise unreachable, and Email Delivery likely will not be able to connect either.
- Connect to an external MTA such as Google's mail exchangers.
- Open a command prompt.
- Use the following command to retrieve one of Google's MX server records.

```

```

- Use the following command to test connectivity to the endpoint port 25 against Google's MX servers.

```

```

If you are unable to connect to an MX server for Google or another domain you are testing, the mail server for that domain is likely offline, or you may not have correct network configuration to reach them over port 25. Be sure to check that your network setup support this; if it does, then the domain's mail servers may be down or offline, or the domain may be misspelled.

If you can connect to a recipient email server on port 25 but cannot connect to Email Delivery public SMTP endpoints on the same port, try port 587 or 465, or create a service request with My Oracle Support with this information.

## TLS Errors when Integrating with Postfix

Fix TLS errors that prevent you from integrating with Postfix.

- 
If you are encountering TLS errors when attempting to integrate Postfix with Email Delivery, ensure that the following setting is removed from the Postfix`main.cf`file, as it has been deprecated:
```

```

- 
Use the following setting instead to turn on TLS (available in Postfix 2.3 and later):
```

```
This setting tells Postfix to use STARTTLS support when connecting to remote SMTP servers such as OCI Email Delivery. If you want to enforce the use of TLS so that all outbound Postfix relaying uses encryption, use the following setting:
```

```

For more information, see[Postfix TLS Support](http://www.postfix.org/TLS_README.html).

## Inactive DKIM Key

Fix the inactive DKIM key in your email domain's DNS.

To activate your DKIM key, you must provision a DNS CNAME record at this location in your Email Domain's DNS:
```

```

However, different DNS providers have different user interfaces to specify the location of a DNS record. Some user interfaces accept the full DNS path by default and these will work well. Some user interfaces are relative to the zone by default, so if you paste in the entire string without the trailing period, the user interface will provision the wrong location and that will leave your DKIM key in a "Needs Attention" state. Avoid entries like this:
```

```

If your Email Domain is the same as your DNS zone name and if your provider only accepts a zone-relative name, use this DNS CNAME location:
```

```

If your Email Domain is in a subdomain of your zone and if your provider only accepts a zone-relative name, use this DNS CNAME location:
```

```

## Service Limits Issues

For Email Delivery limits issues, see[Email Delivery Service Capabilities and Limits](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/overview.htm#Service)and[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.

## Data Privacy

Protect the sender's and recepient's data privacy when an email is sent.

### How does OCI Email Delivery Protect a Sender's and Recipient's Data Privacy?

To protect a sender's and recipient's data privacy when an email is in transit:
- TLS 1.2 is required when sending email from your application to Email Delivery.
- TLS encrypts data when Email Delivery relays emails to the recipient, provided the recipient supports TLS.
- Email body content is stored while in transit only.
- Email header data is logged internally for two weeks.
- If the sender enables logs, the OCI Logging service stores the email service logs. Log data retention policies are defined by the user.
