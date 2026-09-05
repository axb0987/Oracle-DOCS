# JavaScript Challenge for Edge Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/javascript_challenge.htm
- Fetched: 2026-09-05 03:10 CDT

# JavaScript Challenge for Edge Policies

Describes the use and management of the JavaScript challenge for an edge policy.

JavaScript challenge validates that the client can accept JavaScript with a binary decision. JavaScript challenge is generally the first level of bot mitigation, but not sufficient with more advanced bot tools, which require more advanced challenges. More functionality, like detecting Network Address Translation (NAT) traffic, can mitigate the risk of blocking legitimate user traffic from users behind a shared IP address.

The Action Threshold parameter defines the number of requests that fail the challenge before the action is taken. The requests that fail under this threshold are not logged. For example, if you set the JavaScript challenge action to Block and the Action Threshold to 10, and a client that does not accept JavaScript makes 11 requests within the Action Expire Time, the first 10 requests are allowed through to origin (assuming no other rules exist). Logs show one Block entry action taken for the JavaScript challenge.

You can perform the following JavaScript challenge management tasks:
- [Enabling and Editing the JavaScript Challenge](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/update_javascript_challenge.htm#top)
- [Getting the JavaScript Challenge's Details](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/get_javascript_challenge.htm#top)
