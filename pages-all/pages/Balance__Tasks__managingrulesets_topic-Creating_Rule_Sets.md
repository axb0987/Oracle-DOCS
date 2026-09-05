# Creating a Load Balancer Rule Set
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Creating_Rule_Sets.htm
- Fetched: 2026-09-05 01:41 CDT

# Creating a Load Balancer Rule Set

Create a rule set composed of actions that are applied to traffic of a load balancer's listener.

For prerequisite information, see[Rule Sets for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Creating_Rule_Sets.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Creating_Rule_Sets.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Creating_Rule_Sets.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Policies and find the Rule sets section.
- Select Create rule set .
- Enter the following information:

- Name : Specify a friendly name for the rule set. The name must be unique, and can't be changed after the rule is created.
- Specify access control rules : Select to add access control rules.
- IP address CIDR : Enter the IP address CIDR block from which access is allowed.
- Specify access method rules : Select to add access method rules.
- Allowed methods : From the list, select the HTTP methods to allow. You can select several methods.
- Specify URL redirect rules : Select to add URL redirect rules.
- Source path : Specify the incoming path string that triggers the redirect rule. For example,`/video`.
- Match type : Select the match condition to apply when evaluating an incoming path string. The available match types are:
- FORCE_LONGEST_PREFIX_MATCH: The system looks for a redirect rule path string with the best, longest match of the beginning part of the incoming URL path.
- EXACT_MATCH: The incoming URL path must exactly match the specified path string.
- PREFIX_MATCH: The beginning part of the incoming URL path must exactly match the specified path string.
- SUFFIX_MATCH: The ending part of the incoming URL path must exactly match the specified path string.
- Redirect to : Specify a value for at least one URL component field. Any component fields that you do not modify retain the incoming URL's values.

Optionally, select the Switch to full URL link to enter the redirect URL manually.
Important  
  
Failure to specify a value for at least one URL component field can result in a redirect loop.
- Protocol : Specify the HTTP protocol to use in the redirect URL. Valid values are:
- {protocol}
- HTTPS
- HTTP
- Host : Specify a valid domain name (hostname) or IP address for the redirect URL. All redirect URL tokens are valid for this property.
- Port : Specify the communication port to use in the redirect URL. Valid values include integers from 1 to 65535.
- Path : The HTTP URL path to use in the redirect URL. All redirect URL tokens are valid for this property. If the path string doesn't begin with the`{path}`token, it must begin with the slash character`/`.
- Query : Specify the query string to use in the redirect URL. All redirect URL tokens are valid for this property. If the query string doesn't begin with the`{query}`token, it must begin with the question mark`?`character.
- Response code : Specify the HTTP status code to return when the incoming request is redirected. The default response code is 302 found .

Valid response codes for redirection from the standard HTTP specification are:
- `301 Moved Permanently`
- `302 Found`
- `303 See Other`
- `307 Temporary Redirect`
- `308 Permanent Redirect`
- Specify request header rules : Select to add request header rules.
- Order : If you have several rules, you can select the up or down arrows to move the corresponding rule.
- Action : Select the action that the rule applies. Available actions include:
- Add request header :

Adds the specified header and value to the incoming request. If the specified header is already present, the system replaces it. If more than one header with the same name is present, the system removes all and adds one header corresponding to the specified header and value.
- Extend request header :

Adds the specified prefix or suffix to the incoming request. Provide a prefix value, a suffix value, or both when you select this action. The system doesn't support this rule for headers with several values.
- Remove request header : These rules apply only to HTTP or HTTP2 headers.

Removes the specified header. If the same header appears more than once in the request, the load balancer removes all occurrences of the specified header.
- Header : A header name that conforms to RFC 7230.

The system doesn't distinguish between underscore ("_") and dash ("-") characters in headers. It treats example_header_name and example-header-name as identical. We recommend that you don't rely on underscore or dash characters to uniquely distinguish header names.
- Value : (Add rules only.) A header value that conforms to RFC 7230.
- Prefix : (Extend rules only.) A character string to add to the beginning of the existing header name. The resulting header must conform to RFC 7230.
- Suffix : (Extend rules only.) A character string to add to the end of the existing header name. The resulting header must conform to RFC 7230.
- Specify response header rules : Select to add response header rules.
- Order : If you have multiple rules, you can select the up or down arrows to move the corresponding rule.
- Action : Select the action that the rule applies. Available actions include:
- Add response header

Adds the specified header and value to the outgoing response. If the specified header is already present, the system replaces it. If more than one header with the same name is present, the system removes all of them and adds one header corresponding to the specified header and value.
- Extend response header

Adds the specified prefix or suffix to the incoming request. Provide a prefix value, a suffix value, or both when you choose this action. The system does not support this rule for headers with multiple values.
- Remove response header : These rules apply only to HTTP or HTTP2 headers.

Removes the specified header. If the same header appears more than once in the response, the load balancer removes all occurrences of the specified header.
- Header : A header name that conforms to RFC 7230.

The system doesn't distinguish between underscore and dash characters in headers. For example, example_header_name and example-header-name are treated as equal. We recommend that you don't rely on underscore or dash characters to uniquely distinguish header names.
- Value : (Add rules only.) A header value that conforms to RFC 7230.
- Prefix : (Extend rules only.) A character string to add to the beginning of the existing header name. The resulting header must conform to RFC 7230.
- Suffix : (Extend rules only.) A character string to add to the end of the existing header name. The resulting header must conform to RFC 7230.
- Specify HTTP header rules : Select to specify HTTP header options for a listener.
- HTTP header buffer size : Select one of the following buffer sizes for the HTTP header from the list: None, 8k, 16k, 32k, 64k.
- Allow invalid characters in HTTP header : Select to allow periods (".") and underscores ("_") in the HTTP header.
- Specify max listener connections rules : Select to specify the maximum connections an IP address can make to a listener. Set at least one of the following configurations or you can't create a max listener rule:
- Set a uniform max listener connections rule used across all IPs : Select to create a rule that specifies a maximum number of connections an IP address can make to a listener. Specify the maximum number of connections in the Max connections box. If a value isn't specified, then only the IP addresses you list here are limited.
- Set custom max listener connections rules for specific IPs : Select to override the uniform maximum number of listener connections you applied if you selected the preceding option. Select the CIDRs or range of IP addresses that are exempt from the universal connection limit in the CIDRs/IP addresses list. Then specify the maximum number of connections for this select list of exempted CIDRs and IP addresses.

You can only have a maximum of three custom rules, but each one can have several IP addresses. If you don't specify a custom max listener connections number for an IP address, it uses the uniform max connection rule.
- Select Submit .
After you create a rule set, the set becomes available for use with the associated load balancer's listeners. See[Creating a Listener](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Creating_Listeners.htm)to apply the rule set.
- 

Use the[oci lb rule-set create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/rule-set/create.html)command and required parameters to create a rule set for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateRuleSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/RuleSet/CreateRuleSet)
