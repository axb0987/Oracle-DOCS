# Protection Rules Tuning
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/waftuning.htm
- Fetched: 2026-09-05 03:10 CDT

# Protection Rules Tuning

Use Web Application Firewall for protection rules tuning.

This basic WAF tuning information outlines the fundamentals of rule tuning, log inspection, and setting up rule exclusions. Tuning a WAF policy can be beneficial for the following reasons:
- Reduces the chance of blocking a legitimate request.
- Protects against standard web application attacks.
- Protects against specific web application attacks.
- Reduces the amount of scanning, which leads to better performance.

The following table shows production rules terms and definitions.

Protection Rules Definitions
Term Definition

Tuning

The process in which an engineer or analyst modifies protection rules and actions to allow the application server to be protected but remain functional. There is a balance between locking down the application server and allowing the application server to perform its duties. The best tuning takes an intimate knowledge of the application server being protected and protection rules available to protect that application server.

False positive

A false positive occurs when a protection rule is matched against an HTTP transaction and the HTTP transaction is a legitimate (non-malicious) transaction.

Exclusion A modification to a protection rule that allows the value or value name of a cookie or HTTP argument to be ignored.

Oracle Recommendation Engine (ORE)

The ORE aids in the optimization of your WAF security profile by letting you enable all rules that do not trigger during an initial recommendation period.

## Overview of WAF Protection Rules

WAF protects your web applications against threats. WAF is cloud-based and supports over 500 rule sets, and rule sets for the Open Web Application Security Project (OWASP). Use these rules to protect your critical web applications against malicious cyberattacks. These rules are compared against incoming requests to determine if the request contains an attack payload. If it determines that the request is an attack, WAF blocks or alerts you to that request. These attacks are varied and include threats such as SQL injection, cross-site scripting, and HTML injection—all of which can be detected and blocked by the WAF rule sets.
WAF protection is a toolkit designed for real-time web application monitoring, logging, and access control. The toolkit lets you decide how you want to take advantage of all the protection rules available instead. This flexibility is a core element of WAF protection rules, as we are constantly pushing updates to increase the security scope of our rules.
Note  
  
WAF protection rules add extra CPU cycles to each transaction, therefore, we recommended enabling only the rules designed for your web application topology.

To identify and defend web applications against attacks, WAF protection rules run checks on any request to the webserver and all associated responses from the server against the set of rules. After the checks succeed, the HTTP request is sent to the website to retrieve the relevant content. If checks fail instead, the appropriate predefined actions are initiated.

The core principles of WAF protection rules are as follows:
- Passiveness: You decide which rules are required, therefore you have full control.
- Flexibility: WAF protection rules were created by a security expert who provided over 250 rules and the capacity to introduce custom protection rules.
- Quality not quantity: WAF protection rules are a dedicated module designed to inspect HTTP traffic that works with the other WAF features (for example, access control and bot management).
- Predictability: Having full control of the WAF protection rules allows you to control the results expected. You can define and tune your protection rules and leave the setup unattended, knowing that it keeps working as it was configured.

## Onboarding and Initial Tuning

First, you need to have some knowledge about the web application for the tuning process. Otherwise, you might enable Linux-specific rules for your Windows server or origin and rules unnecessarily scan your traffic causing performance degradation. The ORE helps you by providing a solid and secure set of protection rules. The recommendation period is a configurable setting with a default of 10 days. We recommend increasing this value to 15 days to get a large sample of logs for normal traffic on the web application. Approximately twenty-four hours after your WAF policy is created, protection rule recommendations will appear in the recommendations tab. The recommendations are rules picked by WAF experts to cover the OWASP Top Ten. These recommended rules have been selected because they typically produce the least number of false positives and still provide good protection.

### Changing the Recommendation Period and Accepting the Recommendations

By following the steps below, you enable the recommended rules in detect mode. After the rules are in detect mode, we advise waiting 15 days before changing them to block mode.
Note  
  
During the assessment period, all the rules are in detect mode. Detect mode means that there will not be any blocking by protection rules. We recommend performing user acceptance testing and normal application use to help with the tuning process by generating logs. Review logs and check for false positives while the rules are in detect mode. By checking logs that trigger for protection rules, it gives you an idea of what traffic would cause a block when the rules are turned to block mode. During the assessment period, the application should receive as close to normal or production-like traffic as possible. Normal traffic shows you which rules trigger through logs, and false positives can be filtered out.

[To change the recommendations period](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/waftuning.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the edge policy you want to configure rule settings for.

The edge policy's details page opens.
- Select Protection Rules .

The Protection rules panel opens.
- Select the Settings tab.
- Select Edit Rule Settings .

The Edit Rule Settings panel opens.
- Increase the Recommendations Period from 10 to 15 days.
- Select Save Changes .

[To accept the recommendations](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/waftuning.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the edge policy you want to configure rule settings for.

The edge policy's details page opens.
- Select Protection Rules .

The Protection rules panel opens.
- Select the Recommendations tab.

The Recommendations panel opens.
- Select Accept Recommendations .
- Select Unpublished Changes .
- Select Publish All .
- In the Publish Changes panel, select Publish All .

### Using the API to Query for Specific Logs

The API provides the most options for filtering rules. The following are examples of how to use the CLI to filter logs.

- To filter logs by protection rule ID:

```

```

- To filter logs by rule type (for example, protection or access rule types):
```

```

- To filter logs by request URL:
```

```

## Setting Up Log Analytics

Log Analytics helps you to narrow down the protection rules that require attention. Use the following information to set up the Log Analytics service with WAF. See[Security Insights for your web apps with OMC Log Analytics](https://blogs.oracle.com/managementcloud/security-insights-for-your-web-apps-with-omc-log-analytics)for more information.

### Creating Exclusions in Protection Rules

Reviewing logs is a critical part of the tuning process. Logs show us which rule was matched and what part of the HTTP transaction it was matched against. Refer to the following table for samples of logs and how to use them to create an exclusion.

The protectionRuleDetections object in WafLog provides a map of protection rule keys to detection message details. The following table shows four possible exclusions that can be set up for a protection rule.

Log value Exclusion value Description
ARGS Request parameters Used for values of a specific argument.
ARGS_NAMES Request parameters names Used for the name of the argument.
REQUEST_COOKIES Request cookie values Used for values of a specific cookie.
REQUEST_COOKIES_NAMES Request cookie names Used for the name of the cookie.

### Sample Exclusions with Logs

The following section provides raw log samples and examples of what the exclusion value should be for each rule.

- Rule ID 9411000 - ARGS

In this example, the Matched Data was found within the ARGS:foo argument. The exclusion is for rule id 9411000. The exclusion to create is for Request Parameters with a value of foo .
```

```

- Rule ID 9411000 - ARGS_NAMES

In this example, the Matched Data was found within the ARGS_NAMES argument. The exclusion is for rule id 9411000. The exclusion to create is for Request Parameters Names with a value of &lt;script&gt;xss .
```

```

- Rule ID 9411100

In this example, the Matched Data was found within the REQUEST_COOKIES:a argument. The exclusion is for rule id 9411100. The exclusion to create is for Request Cookie Values with a value of a .
```

```

[To create exclusions](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/waftuning.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the edge policy you want to configure rule settings for.

The edge policy's details page opens.
- Select Protection Rules .

The Protection rules panel opens.
- Select the Rules tab.
- Find the protection rule you want to apply an action to.
- Select the Actions menu (three dots) and select Exclusions . Include the exclusions using the information you obtain from the preceding Sample Exclusions with Logs section.
- Select Save Changes .
- Select Unpublished Changes .
- Select Publish All .
- In the Publish Changes dialog box, select Publish All .

## More Information on Protection Rules

### Individual Protection Rules Versus Collaborative Protection RulesTo limit false positives, there are special protection rules that are tagged as "collaborative". These rule groups operate differently than the rest of the protection rules, as they use a scoring and threshold system to evaluate traffic. Individual rules work by matching elements of the HTTP transaction against the rule signature. If a match is made, the rule performs its action (for example, detecting or blocking). Each of the collaborative protection rules uses a group of individual rules. The collaborative protection rules require multiple matches of elements of the HTTP transaction against individual rules to perform its action (for example, detecting or blocking). For a collaborative rule to perform its action, at least three elements of the HTTP transaction must match against the individual rules in the collaborative group. After the exclusion is added within the collaborative protection rule group, it will apply to all the rules within it. The following is a list of the collaborative protection rule IDs.

### Collaborative Protection Rule IDs
- 9300000 - Local File Inclusion (LFI) Collaborative Group - LFI Filter Categories
- 9320000 - Remote Code Execution (RCE) Collaborative Group - UNIX RCE Filter Categories
- 9320001 - Remote Code Execution (RCE) Collaborative Group - Windows RCE Filter Categories
- 9330000 - PHP Injection Attacks Collaborative Group - PHP Filters Categories
- 9410000 - Cross-Site Scripting (XSS) Collaborative Group - XSS Filters Categories
- 9420000 - SQL Injection (SQLi) Collaborative Group - SQLi Filters Categories

### Request Body Inspection Rule IDs
The following rules require response body inspection to be enabled. Remember that response body inspection delays the transaction, as it scans all the information within it. Enable only the required rules.
```

```

### No Exception Rules
The following rules create different raw log values than ARGS, ARGS_NAMES, REQUEST_COOKIE, and REQUEST_COOKIE_VALUE. Exclusions do not exist for these rules, since the rules are based on if the element is present or not. For example, if the content-type header is present, the only option to exclude this rule is to open a service request with[My Oracle Support](http://support.oracle.com/)to ask for a custom WAF rule that excludes any of the following rules.
```

```

These rules are easily spotted, as the log values are REQUEST_URI, REQUEST_PROTOCOL, and REQUEST_HEADERS.

### Other Protection Rules

The following is a list of protection rules that are "noisy", with some descriptions and recommendations which help you understand what the rule is trying to match. Exclusions can't be applied to some of these rules.

Rule ID Rule Name Notes
981318 String Termination/Statement Ending

This rule is important, as it alerts for any escaping character detected within any input field and queryString [ARGS] or cookie.

Review the validations taken at the application side and ensure it only allows the proper input characters, for example, letters and numbers.

If another input value is required, an exclusion to the rule can be applied in the WAF and let it through.

960015

960021 Missing Accept Header

Even when requests without accept headers do not mean a violation of the HTTP protocol, requests without accept headers are most often not genuine requests.

The rule might be alerting for API or custom application requests.

To avoid scanning API or custom application requests, collect a list of the well-known applications that send traffic through and request custom rules.

For more information, see RFC 7231, section-5.3.2.

960007

960008 Missing Host Header As described in RFC 7230, section-5.4 "A server must respond with a 400 (Bad Request) status code to any HTTP/1.1 request message that lacks a Host header field and to any request message that contains more than one Host header field or a Host header field with an invalid field-value." This is an essential method of protection and at the same time ensures that WAF servers properly identify which WAF policy the request is intended for. Since WAF requires a host header to pass traffic to the proper origin, this rule might cause a high rate of false positives.

960009

960006 Missing User-Agent Header

This rule prevents unidentified users from accessing your web application. User-Agent is one of the request headers defined in various RFCs that provides user information. Even when a request contains a user agent, it does not imply it comes from a real human. This rule works as a first level of mitigation for "dummy" attacks that originate from possible bots or "non-RFC compliant" applications.

Note: Some APIs might not include the User-Agent header. If API requests are expected, ensure you add the API IP address to the allowlist or have a custom WAF rule that excludes this traffic from being inspected.

For more information, see RFC 7231, section-5.5.3.

This rule is an indicator of bad or malicious traffic, but it is possible legitimate applications do not have a User-Agent. Ask application owners to use User-Agents when applicable.
960011 GET/HEAD Requests Validation

As described in RFC 7231, section-4.3.1 and section-4.3.2, HEAD and GET are HTTP methods intended to retrieve information from the origin server. Even when not forbidden by the RFC, sending body or payload through these types of methods is not a common practice. Usually it is caused by improperly defined applications not following the best practices of the RFC and can be used by malicious users as a bypass technique.

It is also defined in RFC 2616, section-4.3 "if the request method does not include defined semantics for an entity-body, then the message-body should be ignored when handling the request."
960904 Missing Content-Type Header As defined under RFC 2616, section-7.2.1, "Any HTTP/1.1 message containing an entity-body should include a Content-Type header field defining the media type of that body." If this best practice is not followed, it could lead to MIME-type sniffing attacks.
960032 Allowed HTTP methods

The default allowed HTTP methods are GET, HEAD, POST, and OPTIONS.

OPTIONS is known as an insecure method because it is highly used by attackers to gather up information from the origin server. This method is also required by some applications to work properly.

If this method is not required, create a service request with My Oracle Support to disable it.

Other methods can also be added as required with a service request.
960335 Max amount of arguments

RFC does not enforce the number of arguments that a request must have, but using many arguments could be a method used by malicious users attempting to overflow a web application.

To protect against these types of attacks, we recommend limiting the maximum number of ARGs allowed per request.

The default value is 255.
960208 Max length of an argument

RFC does not enforce the length per argument that a request must have, but using large argument length could be a method used by malicious users attempting to overflow a web application.

To protect against these types of attacks, we recommend limiting the maximum length of ARGs allowed per request.

The default value is 400.
960341 Max total argument length

RFC does not enforce the total (combined) argument size that a request must have, but large combined argument values could be a method used by malicious users attempting to overflow a web application. To protect against these types of attacks, we recommend limiting the maximum combined argument value allowed per request.

The default value is 64000.
92035032 Host Header Is IP Address This rule does not usually trigger, as WAF needs a host header to send traffic to the origin.
941120 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 2

This rule takes a long time to process if there is a large payload.
