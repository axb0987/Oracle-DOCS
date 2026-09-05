# Troubleshooting Edge Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/troubleshooting_edge_policies.htm
- Fetched: 2026-09-05 03:12 CDT

# Troubleshooting Edge Policies

Use troubleshooting information to identify and address common issues that can occur while working with Edge Policies.

## Application Is Slow When Enabling All Protection Rules

Each WAF rule adds CPU cycles to each transaction. The more rules that you enable, regardless of the action (DETECT or BLOCK), slows transaction, especially with large payload transactions. We recommend that you only enable the recommended WAF protection rules in DETECT mode and open a service request with[My Oracle Support](http://support.oracle.com/)requesting OCI Web Application Firewall tuning help before changing the rules to BLOCK. An expert can guide you through the process.

## "Authorization failed or requested resource not found" Error

When adding an IP address to the WAF IP Address List, this error can occur when you don't have the correct policies set up to create an address list. To create an address list,`manage`permissions are required for`waas-address-list`. If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about policies for WAF, see[Details for the WAF service](https://docs.oracle.com/iaas/Content/Identity/Reference/wafpolicyreference.htm).

## Increasing the Maximum Upstream Time to Live (TTL) for OCI WAF

The maximum upstream timeout for WAF can be increased up to 1,200 seconds (20 minutes). By default, the timeout is set to 300 seconds. If you need to increase it, create a service request in My Oracle Support with the following information:

- Tenancy ID
- Policy ID
- Webapp domain
- Upstream timeout time
- The reason why you need us to increase it

Note  
  
WAF has an internal 100-second timeout value (which isn't changeable) that drops the connection if the origin doesn't send any keep-alives, stating that origin is still working on a response "please wait." If the origin is sending keep-alives, you aren't able to reach this type of timeout because it always resets with keep-alive.

## Using an A Record Instead of the CNAME

We recommend that APEX domains point to the IP address based on your server location:
- US: 147.154.3.128
- EU: 147.154.225.212
- APAC: 192.29.50.64
- AUS: 192.29.152.173

## Configuring Value for the Origin Keep-Alive Timeout

WAF requires that the origin's (load balancer or web server) keep-alive timeouts are maintained for 301 seconds or more, as our upstream timeout value is 300 seconds. During this time, the connections are safely maintained while TCP is optimized. The network multiplexing methodology that our nodes use to maintain connectivity with the origin ensure that the connections are safely maintained while TCP is optimized. For more information, see[Getting Started with Edge Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#GettingStartedEdgePolicies).

## Supporting Palo Alto Firewall

- OCI requires Palo Alto firewall to enable Jumbo frames as part of our PMTUD format and our MTU of 9000.
- Refer to[Hanging Connection](https://docs.oracle.com/iaas/Content/Network/Troubleshoot/connectionhang.htm)for troubleshooting information.
- Refer to[Throughput troubleshooting with Palo Alto and OCI](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000POfpCAG)for Palo Alto's troubleshooting information.

## API Application Responding with a 5xx HTTP Status Code

Multiple factors can lead to a 5xx HTTP status code. Review the following information:

- The origin keep-alive timeout must be 301 seconds.

- Session persistency must be cookie-based.
- IP affinity is a best practice as our nodes work in a round robin scenario and every 10 minutes the node IP potentially changes within the same transaction.
- If you have multiple WAF rules enabled and the transaction includes a large payload, it causes the transaction to time out on the origin. The request is still in the WAF buffer and has been parsed before responding to the origin.
- One or more nodes aren't fully on the allowlist on the ingress rules from the origin side.
- One specific node is failing. In this case, immediately escalate the issue to our support team.

## Website Is Timing Out

- See[API Application Responding with a 5xx HTTP Status Code](https://docs.oracle.com/en-us/iaas/Content/WAF/troubleshooting_edge_policies.htm#troubleshooting_edge_policies__timeout)for a list of checkpoints.
- The timeout can also be related to the allowlist (Security Lists or NSG). Review the following information:
- Did you add the security lists to allow the OCI WAF nodes?
- Are the rules stateless?
- 

If the rules are stateless, did you add the respective egress rules?

Note  
  
When you add a stateless security rule, you're allowing only one side of the traffic (ingress or egress). To allow the complete traffic flow, add another rule on the other side (egress or ingress). Adding a stateful rule (which means just keeping the stateless option clear) allows both sides of the traffic without the requirement of adding an egress rule.

## Excluding Multiple Cookies That End with the Same String from Inspection by WAF Protection Rules

In the following example, alerts are received from WAF Protection from values under multiple cookies: 123_SessionID =bad_value1; 456_SessionID =bad_value2; 789_SessionID =bad_value3; ...

Instead of adding each cookie manually, you can group them in a regex format:

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Policies .
- Select the name of the WAF policy that you want to configure rule settings for. The WAF Policy overview appears.
- Select Protection Rules .
- Select the Rules tab.
- Find the protection rule that you want to apply the exclusion to.
- Select the Actions menu (three dots) and select Exclusions .
- In the Exclusions dialog box, enter the following criteria:
- Exclusion : Select request cookie values.
- Value : Enter /_SessionID$/. This value matches all cookies that end with _ SessionID triggering WAF rules with "bad_values."
- Select Save Changes .

## "Parameter 'from-json' must be in JSON format" Error
