# Access Rules for Edge Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/access-rules.htm
- Fetched: 2026-09-05 03:11 CDT

# Access Rules for Edge Policies

Use Web Application Firewall to manage access rules within an Edge policy.

As a WAF administrator, you can define explicit actions for requests that meet various conditions. Conditions use various operations and regular expressions. A rule action can be set to log and allow, detect, block, redirect, bypass, or show a CAPTCHA for all matched requests.

The following information provides the available conditions for an access rule.

Criteria Type Criteria
URL Define one or more criteria based on:
- URL is
- URL is not
- URL starts with
- URL does not start with
- URL part ends with
- URL part does not end with
- URL part contains
- URL part does not contain
- URL regex
- URL does not match regex

The URL regex matching uses Perl-compatible regular expressions.

The URL-based matching in access rules is for a location on the same domain, for example, "/login.php". To target a full absolute URL, you can use a combination of header matching (Host: www.example.com) and URL "/login.php".
IP Address Define one or more criteria based on:
- IP Address is
- IP Address is not
- IP Address in Address List
- IP Address not in Address List

These values can be a valid IPv4 address, subset, or CIDR notation for a range. IP Address criteria can be used to restrict incoming traffic specific to both IP addresses and CIDR ranges. IPv6 is not yet supported.

See[IP Address Lists for Edge Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/ipaddresslist.htm#ip_address_list)for information on how to create a list of IP addresses that can be used in the access rule.
Country/Region Define one or more criteria based on:
- Country/Region is
- Country/Region is not

For the API, use a two letter country code.
User Agent Identify the browser client.
- User Agent is
- User Agent is not
HTTP Header Evaluate as criteria:
- HTTP Header contains

Enter the HTTP Header contains value with colon-delimited &lt;name&gt;:&lt;value&gt;. You can't use wild cards.
HTTP Method Evaluate as criteria:
- HTTP method is
- HTTP method is not

Available methods include GET, POST, PUT, DELETE, HEAD, CONNECT, OPTIONS, TRACE, and PATCH.

When working with access rules, consider the following information:
- For the sequence of processing "Access Rules" versus "IP Whitelist" tabs, IP whitelist is triggered first. If the IP address isn't in the IP address allowlist, the sequence moves to access rules.
- WAF supports the following HTTP redirect response codes:
- 301 - Moved permanently : Use this response code if your website was permanently moved to the redirection URL and you want search engines to index it.
- 302 - Temporary redirect : Use this response code if a certain URL has been changed to a different address for a short amount of time.
- You can only include CAPTCHA as a full page and not as an inline component in the website.
- You can reorder access rules only by using the API to manually reorder the rules that are listed.
- You can't reorder access rules when you create an access rule with the BLOCK action.
-
