# Rule Sets for Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets.htm
- Fetched: 2026-09-05 01:41 CDT

# Rule Sets for Load Balancers

Use rule sets composed of actions that are applied to traffic of a load balancer's listener.

A rule set is a named set of rules associated with a load balancer and applied to one or more listeners on that load balancer. To apply a rule set to a listener, you first create the rule set that contains the rules. Rules are objects that represent actions applied to traffic at a load balancer listener. The rule set becomes a part of the load balancer's configuration. You can specify the rule set to use when you create or update a listener for the load balancer.

You can include the following types of rules in a rule set:

[Access control rules](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets.htm#AccessControlRules), which restrict access to application resources based on the source of the request.

[Access method rules](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets.htm#AccessMethodRules), which specify the permitted HTTP methods.

[URL redirect rules](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets.htm#URLRedirectRules), which route incoming HTTP requests to a different destination URL.

[Request and response header rules](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets.htm#RequestResponsHeaderRules), which add, alter, or remove HTTP request or response headers.

[HTTP header rules](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets.htm#HTTPHeaderRules), which specify the size of the HTTP header and which characters are permitted within the headers.

[Max listener connection rules](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets.htm#max-listener-connection-rules), which specify the maximum IP connections for a listener.
Note  
  
Rule sets apply only to HTTP listeners.

Apply an existing rule set when you edit a listener. You can apply the same rule set to several listeners on the same load balancer.

Rule sets aren't shared between load balancers. To use the same set of rules on another load balancer, you must create a new, identical rule set under that load balancer.

Up to 20 rules are allowed in a rule set. You can associate a maximum of 50 rules with a load balancer.

You can perform the following path route set management tasks:

[List the rule sets for a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-rule-set.htm)

[Create a new rule set for a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Creating_Rule_Sets.htm)

[Get a rule set's details.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_rule_set.htm)

[Edit a rule set's settings.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Editing_Rule_Sets.htm)

[Delete a rule set from a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Deleting_Rule_Sets.htm)

For more information about managing load balancer listeners, see[Listeners](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners.htm).

## Access Control Rules

Access control rules permit access to application resources based on user-specified IP address or address range match conditions. If you don't specify any access control rules, the default rule is to allow all traffic. If you add access control rules, the load balancer denies any traffic that doesn't match the rules.

The service accepts only classless inter-domain routing (CIDR) format (`x.x.x.x/y or x:x::x/y`) strings for the match condition.

Specify`0.0.0.0/0`or`::/0`to match all incoming traffic.
Note  
  
Only US Government Cloud regions permit IPv6 values.

## Access Method Rules

Access method rules specify the HTTP methods allowed at the associated listener. The load balancer doesn't forward a disallowed request to the backend servers and returns a`405 Method Not Allowed`response with a list of the allowed methods. You can associate only one list of allowed methods with a particular listener.

By default, you can specify only the standard HTTP methods defined in the[HTTP Method Registry](http://www.iana.org/assignments/http-methods/http-methods.xhtml). The list of HTTP methods is extensible. If you need to configure custom HTTP methods, contact[My Oracle Support](http://support.oracle.com/)to remove the restriction from your tenancy. Your backend application must be able to handle the specified methods.

The following list shows the default HTTP methods:

Default HTTP Methods

ACL BASELINE-CONTROL BIND
CHECKIN CHECKOUT CONNECT
COPY DELETE GET
HEAD LABEL LINK
LOCK MERGE MKACTIVITY
MKCALENDAR MKCOL MKREDIRECTREF
MKWORKSPACE MOVE OPTIONS
ORDERPATCH PATCH POST
PRI PROPFIND PROPPATCH
PUT REBIND REPORT
SEARCH TRACE UNBIND
UNCHECKOUT UNLINK UNLOCK
UPDATE UPDATEREDIRECTREF VERSION-CONTROL

## URL Redirect Rules

URL redirect rules specify how to route incoming HTTP requests to a different destination URL. URL redirect rules apply only to HTTP listeners. You configure each redirect rule for a particular listener and a specified path. A listener can have only one redirect rule for a particular incoming URL path.

When you create a URL redirect rule, you specify the path string and match condition the service uses to evaluate an incoming URL for redirection. You also define the redirect URL and response code.

### Incoming Path String Evaluation

You specify the path string, or pattern, to evaluate in the incoming URL. For example:
```

```

You also specify the match condition to apply when evaluating the incoming URL for redirection. The available match types are:
- FORCE_LONGEST_PREFIX_MATCH

The system looks for a redirect rule path string with the best, longest match of the beginning part of the incoming URL path.
- EXACT_MATCH

The incoming URL path must exactly match the specified path string.
- PREFIX_MATCH

The beginning part of the incoming URL path must exactly match the specified path string.
- SUFFIX_MATCH

The ending part of the incoming URL path must exactly match the specified path string.
Note  
  
The incoming URL path string can't include a query.

### Redirection URL Construction

You define the redirect URL applied to the original request. URL redirect rules recognize the following URL components:
```

```

You can specify a literal string or provide a token for any component. Tokens extract values from the incoming HTTP request URL. Tokens are case-sensitive. For example,`{host}`is a valid token, but`{HOST}`is not.
- Protocol

The HTTP protocol to use in the redirect URL. Valid values are HTTP and HTTPS.

The`{protocol}`token extracts the protocol from the incoming HTTP request URL. It is the only valid token for this property.
- Host

The valid domain name or IP address to use in the redirect URL.

The`{host}`token extracts the host from the incoming HTTP request URL. All URL Redirect tokens are valid for this property. You can use any token more than once.

Curly braces {} are valid in this property only to surround tokens.
- Port

The communication port to use in the redirect URL. Valid values include integers from 1 to 65535.

The`{port}`token extracts the port from the incoming HTTP request URL. It is the only valid token for this property.
- Path

The HTTP URL path to use in the redirect URL. To omit the path from the redirect URL, set this value to an empty string.

The`{path}`token extracts the path string from the incoming HTTP request URL. All URL Redirect tokens are valid for this property. You can use any token more than once.

If the path string doesn't begin with the`{path}`token, it must begin with a forward slash / .
- Query

The query string to use in the redirect URL. To omit all incoming query parameters from the redirect URL, set this value to an empty string.

The`{query}`token extracts the query string from the incoming HTTP request URL. All URL Redirect tokens are valid for this property. You can use any token more than once.

If the query string doesn't begin with the`{query}`token, it must begin with a question mark? .

You can specify several query parameters as a single string. Separate each query parameter with an ampersand &amp; .

If the specified query string results in a redirect URL ending with ? or &amp; , the last character is truncated. For example, if the incoming URL is`http://host.com:8080/documents`and the query property value is`?lang=en&{query}`, the redirect URL is`http://host.com:8080/documents?lang=en`. The system truncates the final ampersand &amp; because the incoming URL included no value to replace the`{query}`token.
Important  
  
Failure to specify a value for at least one URL component field can result in a redirect loop.

### Manual Redirect URL Construction

The Console provides text entry fields for each URL component. You can also manually specify the full redirect URL.

You can retain the literal characters of a token when you specify values for the path and query properties of the redirect URL. Use a backslash \ as the escape character for the \ , { , and } characters. For example, if the incoming HTTP request URL is`/video`, the path property value`/example{path}123\{path\}`appears in the constructed redirect URL as`/example/video123{path}`.

Some path and query string examples:
- /example/video/123 appears as`/example/video/123`in the redirect URL.
- /example{path} appears as`/example/video/123`in the redirect URL when`/video/123`is the path in the incoming HTTP request URL.
- {path}/123 appears as`/example/video/123`in the redirect URL when`/example/video`is the path in the incoming HTTP request URL.
- {path}123 appears as`/example/video123`in the redirect URL when`/example/video`is the path in the incoming HTTP request URL.
- /{host}/123 appears as`/example.com/123`in the redirect URL when`example.com`is the hostname in the incoming HTTP request URL.
- /{host}/{port} appears as`/example.com/123`in the redirect URL when`example.com`is the hostname and`123`is the port in the incoming HTTP request URL.
- /{query} appears as`/lang=en`in the redirect URL when the query is`lang=en`in the incoming HTTP request URL.
- lang=en&amp;time_zone=PST appears as`lang=en&time_zone=PST`in the redirect URL.
- {query} appears as`lang=en&time_zone=PST`in the redirect URL when`lang=en&time_zone=PST`is the query string in the incoming HTTP request. If the incoming HTTP request has no query parameters, the`{query}`token renders as an empty string.
- lang=en&amp;{query}&amp;time_zone=PST appears as`lang=en&country=us&time_zone=PST`in the redirect URL when`country=us`is the query string in the incoming HTTP request. If the incoming HTTP request has no query parameters, this value renders as`lang=en&time_zone=PST`.
- protocol={protocol}&amp;hostname={host} appears as`protocol=http&hostname=example.com`in the redirect URL when the protocol is`http`and the hostname is`example.com`in the incoming HTTP request.
- port={port}&amp;hostname={host} appears as`port=8080&hostname=example.com`in the redirect URL when the port is`8080`and the hostname is`example.com`in the incoming HTTP request URL.

### Response Code

You can specify the HTTP status code to return when the incoming request is redirected. Valid response codes for redirection from the standard HTTP specification are:
- `301 Moved Permanently`
- `302 Found`
- `303 See Other`
- `307 Temporary Redirect`
- `308 Permanent Redirect`

The default value is`302 Found`.

## Request and Response Header Rules

Request and response header rules add, alter, or remove HTTP request or response headers. These rules can help you pass metadata to your backend servers to do things like:
- Identify which listener sent a request.
- Notify a backend server about SSL termination.

Examples of how rule sets can help you enhance site security include:
- Adding headers to prevent external domains from iframing your site.
- Removing debug headers, such as "Server," sent by backend servers. This action helps you hide the implementation details of your backend.
- Adding the "strict-transport-security" header, with a proper value, to responses. This header helps guarantee that access to your site is HTTPS only.
- Adding the "x-xss-protection" header with a proper value. This header helps you enforce the cross-site scripting (XSS) protection built into modern browsers.
- Adding the "x-content-type" header with a proper value. This header helps you prevent attacks based on content type shifting.
Note  
  
Adding or removing the built-in Host header or one of the X-Headers as described in HTTP "X-" Headers does not remove or override the header value. Instead, performing these actions can append other values or duplicate the header.

### Example: Notify WebLogic that the Load Balancer Terminated SSL

You can configure your load balancer to perform SSL termination. Often, your backend applications require notification of this action. For example, HTTPS[WebLogic](https://www.oracle.com/middleware/technologies/weblogic.html)e-commerce online transaction processing looks for the`WL-Proxy-SSL`header to confirm that a request came in over SSL. You can use rule sets to add this header at the load balancer listener.
Note  
  
For security reasons, WebLogic ignores this header unless you check the WebLogic Plugin Enabled box in WebLogic's Administration Console.

- Create a rule set with the following settings. See[Creating a Rule Set](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Creating_Rule_Sets.htm)for more information.

- Select the Add Request Header option from the Action list.
- Enter`WL-Proxy-SSL`as the Header name.
- Set the header Value :
- If your load balancer is configured to perform SSL termination, set this value to "true."
- If the SSL termination point is in the web server where the plugin operates, set this value to "false."
- Create a listener, or edit an existing listener, and add the new rule set. See[Listeners](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners.htm)for more information.

## HTTP Header Rules

HTTP header rules specify the size of the HTTP header and which characters are permitted within the headers.
- The HTTP header rule HTTP header buffer size increases the size of a buffer used for reading HTTP client request header and backend server response from the default 8 KB up to 64 KB. The buffer is used for the overflow control. Each request or response header line needs to fit into this buffer. Therefore, applications using large HTTP header lines need to tune this parameter.
- The HTTP header rule Allow invalid characters in HTTP header allows numerals, hyphens, and underscores to be included in HTTP headers.

For more information on implementing HTTP header rules, see[Creating a Rule Set](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Creating_Rule_Sets.htm).

## Max Listener Connection Rules

The max listener connect rule lets you apply both a uniform maximum number of listener connections for all IP addresses, and also specify overrides to that uniform value for individual IP addresses you identify.
- You can set a default maximum connections value that applies to all IP addresses that don't have specific maximums set. If you don't set this default maximum value, there's no limit to the number of connections that an IP can make to a listener.
- You can also set maximum values for one or more IP addresses that override the default maximum connections value.

For more information on implementing max listener connect rules, see[Creating a Rule Set](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Creating_Rule_Sets.htm)
