# List-Unsubscribe
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/list-unsubscribe.htm
- Fetched: 2026-09-05 02:01 CDT

# List-Unsubscribe

List-Unsubscribe is an industry-standard email feature that provides recipients with a simplified way to opt-out of receiving further emails from a sender, using their email client. It uses special email headers to provide participating email clients with a method to send unsubscribe requests. It is a best practice for senders to include these headers in the email to decrease spam complaint rates, and increase overall engagement.

Major mailbox providers Gmail and Yahoo implemented new policies to require List-Unsubscribe and the newer one-click unsubscribe standard. With this in place, email that's not compliant with the standard can be marked as spam.

To help our customers achieve and maintain high sender reputation, OCI Email Delivery implements List-Unsubscribe in all emails. This ensures compliance with this best practice, and with the new Gmail and Yahoo policies particularly.

OCI Email Delivery implements the HTTP method of List-Unsubscribe, which is required for the new one-click standard as follows:
- Sender submits an email for delivery. If the email doesn't have an HTTPS List-Unsubscribe URL already set, Email Delivery replaces any existing header with a one-click unsubscribe link. Otherwise, the unsubscribe headers are left alone.
- Email Delivery attempts delivery of the email.
- In the delivered email, if the recipient clicks unsubscribe or similar link in their email client interface, the email client sends an HTTPS unsubscribe web request to Email Delivery and no further interaction is required by the recipient.
Note  
  
The unsubscribe link in the email client interface isn't to be confused with an unsubscribe link in the body content. See[How does List-Unsubscribe differ from an unsubscribe link in the email body content?](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/list-unsubscribe.htm#list-unsubscribe__list1)
- Email Delivery receives and processes the unsubscribe request.
- The recipient is added to the suppression list with reason UNSUBSCRIBE .
- Email Delivery increments the EmailsListUnsubscribed metric for the Approved Sender and sending Email Domain, to account for the unsubscribe request.
- If[OutboundRelayed logging is enabled](https://docs.oracle.com/iaas/Content/Email/Reference/dashboard-topic-enabling-logging.htm#:~:text=Using%20the%20Console&text=Under%20Application%20Integration%2C%20click%20Email,Click%20Enable%20Logging.)for the sender Email Domain, an unsubscribe log record is written. The userAgent field in the log record has the email client and the OS information used to submit the unsubscribe request.
Note  
  
Custom headers aren't included in unsubscribe logging records now. If this is an issue, we suggest implementing your own List-Unsubscribe as explained in the following[section](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/list-unsubscribe.htm#list-unsubscribe__list3).
- Senders can remove the recipient from the suppression list if the unsubscribe request was unintentional.

## How does List-Unsubscribe differ from an unsubscribe link in the email body content?

List-Unsubscribe requests are initiated through the email client's own interface (web-based, application-based, etc.) and use the pre-defined SMTP email headers to know where the request should be sent. This is handled by Email Delivery, or can be implemented by customers instead if desired (see below). List-Unsubscribe requests for Email Delivery-placed headers are handled as noted in the process above, and result in addition of the recipient to the suppression list, and metrics/logs updated as well.

Unsubscribe links in body content are fully handled by customer senders and are just as important for good sender reputation. They provide another, potentially more specific method for unsubscribing a recipient from a particular list or segment of list (all managed by the customer sender). Unsubscribe requests from body content links, however, do not result in a suppression list addition and do not show up in metrics and logs.

With the new Gmail and Yahoo policies now in effect, and considering existing industry best practices for good email sending reputation, customers should embrace both methods of unsubscribe.

## What is the scope of each unsubscribe request?

At this time, List-Unsubscribe requests received by Email Delivery result in the recipient being added to the suppression list. Since the suppression list is global to the whole tenancy, and Email Delivery doesn't take into account the sender address or any other special data points (such as custom headers), the recipient will be effectively unsubscribed from all further mailings. This may not be ideal for some customers who use their tenancy to email on behalf of different email lists or other companies. The best option to work around this is to implement your own List-Unsubscribe, so you have the option to specify things such as email list ID or other data points important to a more specific, targeted unsubscribe.

## Can I implement my own List-Unsubscribe?
Yes! Email Delivery will add the required headers only if they're not already present in submitted emails. To implement your own List-Unsubscribe, set up an HTTPS handler to receive the requests, then add the following headers to the submitted emails (replace the sample URL as appropriate for your solution):
```

```

The URL above is an example and you must replace with a URL that points to your HTTP handler, and that ideally contains information needed to unsubscribe the particular recipient from the appropriate email list you want. You can use other data points as well as you see fit, to ensure the unsubscribe request is targeted appropriately.
Note
