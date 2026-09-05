# Request Protection Rules for Web Application Firewall
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/protections_management.htm
- Fetched: 2026-09-05 03:11 CDT

# Request Protection Rules for Web Application Firewall

Learn how to add and manage request protection rules for web application firewall policies.

Web Application Firewall protects your web applications against threats. Web Application Firewall is a regional-based service that is attached to an enforcement point. Use Web Application Firewall protection capabilities to protect your critical web applications against malicious cyberattacks. You can use the protection capabilities to set up rules that are compared against incoming requests to determine if the request contains an attack payload. If it is determined that a request is an attack, Web Application Firewall blocks or alerts you to that request. These attacks are varied and include threats such as SQL injection, cross-site scripting, and HTML injection—all of which the Web Application Firewall protection capabilities can detect and block.

Web Application Firewall protection is a toolkit designed for web application monitoring, logging, and access control. The toolkit lets you decide how to take advantage of all the protection capabilities available. This flexibility is a core element of Web Application Firewall protection, as OCI is constantly pushing updates to increase the security scope of protection capabilities.

Custom protection rules aren't available for the Web Application Firewall policy.

You can perform the following protections tasks:

[List the request protection rules in a compartment](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/list_request_protection_rules.htm#top).

[Create a new request protection rule](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/create_request_control.htm#top).

[View the details of a request protection rule](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/get_request_protection_rule.htm#top).

[Update the settings of a protection rule](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/update_request_protection_rule.htm#top).

[Delete a request protection rule from the policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/delete_request_protection_rule.htm#top).

[List the capabilities for a request protection rule](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/list_protection-capability.htm#top).

[List the filtering tags for a request protection rule](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/list_protection-capability_group-tags.htm#top).

[View the settings for a request protection rule](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/get-protection-rule-settings.htm#top).

## How Request Protection Rules Work

The core principles of Web Application Firewall protection capabilities are:
- Passiveness : You decide which capabilities are required, therefore you have full control.
- Flexibility : The Oracle Web Application Firewall security team has curated a list of protection capabilities that address both Open Web Application Security Project (OWASP) top 10 and critical CVE's for popular web applications.
- Quality not quantity : Web Application Firewall protection rules is a dedicated module designed to inspect HTTP traffic that works with the other WAF features (for example, access control).
- Predictability : Having full control of the Web Application Firewall protection capabilities allows you to control the results expected. You can define and tune your protection rules and leave the setup unattended, knowing that it keeps working as it was configured.

Protection rules match web traffic to rule conditions and determine the action to be taken when the conditions are met.

The Web Application Firewall policy has approximately[490 rules](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/protections_management.htm#WorkRequestManagement)and contains only the newest versions of the rules. WAF policy includes only rules based on CRS 3.0 and later.
Note  
  
We continuously update and optimize existing rules, in addition to creating rules. Because of vulnerability concerns, we can't provide the mitigation pattern for rules.

## Exclusions

Sometimes a protection rule can trigger a false positive. You can configure an exception if the request(s) generating the false positive have a particular argument or cookie that can be used to identify that request be excluded from the action normally taken on the rule. You can create exclusions using the OCI Console or through the API. Use the following exclusion parameters:

Name Value
REQUEST_COOKIES Cookie Value
ARGS Argument (Query Parameter or POST/PUT data)

## HTTP Request Body Inspection for Web Application Firewall

Manage HTTP Request Body Inspection in Web Application Firewall.

HTTP request body inspection instructs the web application firewall policy to buffer the request body in memory and inspect it before sending the request headers and the buffered request body to the backend. If HTTP request body inspection does not occur, the request body is always streamed to the backends (assuming the request headers have not triggered any protection rules).

You can enable the HTTP request body inspection feature when you add your request protection rule, or update an existing protection rule to include it. Only those protection capabilities that have body inspection conditions can use this feature.

You can configure the body inspection settings by accessing the View and Edit Rules Settings dialog box through the process of editing of the protection rule. See[Editing a Request Protection Rule](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/update_request_protection_rule.htm#top)for more information. In the View and Edit Rules Settings dialog box, specify how many bytes in each request body are to be inspected in the Maximum Number of Bytes Allowed field. The inspection amount ranges from 0 to 8192 bytes. The initial number of bytes you specify here are inspected for each request body. If the number of message bytes exceeds the limit you set, you can select a resulting action from the Action taken if limit has been exceeded list. The pre-defined actions are:
- 

Inspect Partial Body and Continue : The body is inspected to the specified size limit. No further action is taken if that limit is exceeded. This selection is equal to the "None" selection.
- 

Preconfigured 401 Response Code Action : This is a dynamic action. Each time you can define a different set of actions, but they all are going to be with the "Return HTTP Response" type.

You can also create a custom action. See[Actions](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/../Actions/actions_management.htm#RateLimitinglManagement)for more information.

A request protection rule using body inspection is indicated as being Enabled in the Request Protections Rules list under the Body Inspection column.
Note  
  

Enabling this feature can result in latency of message traffic because of the additional time required to inspect the message body.

## Protection Capabilities Tuning

This basic WAF tuning information outlines the fundamentals of rule tuning, log inspection, and setting up capability exclusions. Tuning can be beneficial for the following reasons:
- Reduces the chance of blocking a legitimate request.
- Protects against standard web application attacks.
- Protects against specific web application attacks.
- Reduces the amount of scanning, which leads to better performance.

The following table shows protection capabilities terms and definitions.

Protection Capabilities Definitions

Term

Definition

Tuning

The process in which the customer's engineer or analyst modifies protection capabilities and actions to allow the application server to be protected but remain functional. There exists a balance between locking down the application server and allowing the application server to perform its duties. The best tuning takes an intimate knowledge of the application server being protected and protection capabilities available to protect that application server.

False positive

A false positive occurs when a protection capability is matched against an HTTP transaction and the HTTP transaction is a legitimate (non-malicious) transaction.

Exclusion

A modification to a protection capability that allows the value or value name of a cookie or HTTP argument to be ignored.

### Collaborative Protection Capabilities

You can use special protection capabilities tagged as "collaborative" to limit false positives. The collaborative capabilities operate differently from the other protection capabilities.

Collaborative protection capabilities use a scoring and threshold system to evaluate traffic. Individual capabilities work by matching elements of the HTTP transaction and the capability signature. If a match is made, the rule performs its action (for example, detecting or blocking).

Each of the collaborative capabilities uses a group of individual capabilities. The collaborative protection capabilities require multiple matches of elements of the HTTP transaction with individual rules to perform their actions.

For collaborative capabilities to perform their actions, elements of the HTTP transaction must match the individual capabilities in the collaborative group, related to the weight versus thresholds being set on the collaborative capabilities, as follows:

- Weight : A number representing how much an individual capability contributes toward the collaborative capability threshold.
- Threshold : The minimum sum of weights from individual capabilities that the collaborative capability matches.
Note  
  
You can change the weight and threshold values as needed.

When an exclusion is added within the collaborative protection capability, the exclusion applies to all individual capabilities within the collaborative capability.

Example

A collaborative capability key with ID 9420000 - SQL Injection (SQLi) Collaborative Group - SQLi Filters Categories checks the incoming HTTP request for certain types of SLQ injections. This collaborative capability is made up of several capabilities, such as 9421000 , 9421400 , 9421600 , each with a default weight value of 4.

If this collaborative capability is enabled (9420000), for every incoming HTTP request, WAF runs each individual capability (9421000, 9421400, 9421600) that makes up the collaborative capability separately, to find matched capabilities.

After the rules are processed, the matched capabilities are used, their weights are added (in this case is 4+4+4 = 12), and the sum is checked against the threshold (10). Because the HTTP request matched the individual capabilities that make up the collaborative capability (9420000), the collaborative capability is marked as triggered. If logging is configured, the matched capability is logged. Depending on how the capability is configured, an HTTP response is returned. For more information, see[Protection Capabilities Reference](https://docs.oracle.com/iaas/api/#/en/waf/latest/ProtectionCapability/).

#### Collaborative Protection Capability Keys

The following list provides collaborative protection capability keys:
- 9300000 - Local File Inclusion (LFI) Collaborative Group - LFI Filter Categories
- 9320000 - Remote Code Execution (RCE) Collaborative Group - UNIX RCE Filter Categories
- 9320001 - Remote Code Execution (RCE) Collaborative Group - Windows RCE Filter Categories
- 9330000 - PHP Injection Attacks Collaborative Group - PHP Filters Categories
- 9410000 - Cross-Site Scripting (XSS) Collaborative Group - XSS Filters Categories
- 9420000 - SQL Injection (SQLi) Collaborative Group - SQLi Filters Categories

#### Other Protection Capabilities

The following list provides protection capabilities that are "noisy," with some descriptions and recommendations to help you understand what the capability is trying to match. Exclusions cannot be applied to some of these keys.

Capability Key Capability Name Notes

920310

920311 Missing Accept Header

Even when requests without accept headers do not mean a violation of the HTTP protocol, requests without accept headers are most often not genuine requests.

The rule might be alerting for API or custom application requests.

To avoid scanning API or custom application requests, collect a list of the well-known applications that send traffic through and request custom rules.

For more information, see RFC 7231, section-5.3.2.

920280 Missing Host Header As described in RFC 7230, section-5.4 "A server must respond with a 400 (Bad Request) status code to any HTTP/1.1 request message that lacks a Host header field and to any request message that contains more than one Host header field or a Host header field with an invalid field-value." This is an essential method of protection and at the same time ensures that WAF servers properly identify which WAF policy the request is intended for. Since WAF requires a host header to pass traffic to the proper origin, this rule might cause a high rate of false positives.

920320

920330 Missing User-Agent Header

This rule prevents unidentified users from accessing your web application. User-Agent is one of the request headers defined in various RFCs that provides user information. Even when a request contains a user agent, it does not imply it comes from a real human. This rule works as a first level of mitigation for "dummy" attacks that originate from possible bots or "non-RFC compliant" applications.

Note: Some APIs might not include the User-Agent header. If API requests are expected, ensure you add the API IP address to the allowlist or have a custom WAF rule that excludes this traffic from being inspected.

For more information, see RFC 7231, section-5.5.3.

This rule is an indicator of bad or malicious traffic, but it is possible legitimate applications do not have a User-Agent. Ask application owners to use User-Agents when applicable.

920170

920171 GET/HEAD Requests Validation

As described in RFC 7231, section-4.3.1 and section-4.3.2, HEAD and GET are HTTP methods intended to retrieve information from the origin server. Even when not forbidden by the RFC, sending body or payload through these types of methods is not a common practice. Usually it is caused by improperly defined applications not following the best practices of the RFC and can be used by malicious users as a bypass technique.

It is also defined in RFC 2616, section-4.3 "if the request method does not include defined semantics for an entity-body, then the message-body should be ignored when handling the request."

920180 Missing Content-Type Header As defined under RFC 2616, section-7.2.1, "Any HTTP/1.1 message containing an entity-body should include a Content-Type header field defining the media type of that body." If this best practice is not followed, it could lead to MIME-type sniffing attacks.

911100 Allowed HTTP methods

The default allowed HTTP methods are GET, HEAD, POST, and OPTIONS.

OPTIONS is known as an insecure method because it is highly used by attackers to gather up information from the origin server. This method is also required by some applications to work properly.

If this method is not required, create a service request with My Oracle Support to disable it.

Other methods can also be added as required with a service request.

920380 Max amount of arguments

RFC does not enforce the number of arguments that a request must have, but using many arguments could be a method used by malicious users attempting to overflow a web application.

To protect against these types of attacks, we recommend limiting the maximum number of ARGs allowed per request.

The default value is 255.

920370 Max length of an argument

RFC does not enforce the length per argument that a request must have, but using large argument length could be a method used by malicious users attempting to overflow a web application.

To protect against these types of attacks, we recommend limiting the maximum length of ARGs allowed per request.

The default value is 400.

920390 Max total argument length

RFC does not enforce the total (combined) argument size that a request must have, but large combined argument values could be a method used by malicious users attempting to overflow a web application. To protect against these types of attacks, we recommend limiting the maximum combined argument value allowed per request.

The default value is 64000.

920350 Host Header Is IP Address This rule does not usually trigger, as WAF needs a host header to send traffic to the origin.
941120 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 2

This rule takes a long time to process if there is a large payload.

For example, a payload with 64,005 bytes takes around 32 seconds to process.

## Protection Rules

Protection rules match web traffic to rule conditions and determine the action to be taken when the conditions are met.

WAF policy has approximately[490 rules](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/protections_management.htm#WorkRequestManagement)and contains only the newest versions of the rules. WAF policy includes only rules based on CRS 3.0 and later.
Note  
  
We continuously update and optimize existing rules, in addition to creating rules. Because of vulnerability concerns, we can't provide the mitigation pattern for rules.

Custom protection rules aren't available for WAF policy.

## Protection Capabilities

The following table lists protection capabilities supported by WAF. For the most up-to-date listing, view the Web Application Firewall protection capabilities in the OCI Console. See[Listing Web Application Firewall Protection Capabilities](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/list_protection-capability.htm#top).

Capability Key Version Name Description
944300 1 Java attack Attempt: Interesting keywords for possibly RCE on vulnerable classes and methods base64 encoded Java attack Attempt: Interesting keywords for possibly RCE on vulnerable classes and methods base64 encoded
944260 1 Java attack Attempt Java attack Attempt: Malicious class-loading payload
944250 1 Java attack Attempt: SAP CRM Java vulnerability CVE-2018-2380 Java attack Attempt: SAP CRM Java vulnerability CVE-2018-2380
944240 1 Java attack Attempt: Remote Command Execution: Java serialization Java attack Attempt: Remote Command Execution: Java serialization
944210 1 Java attack Attempt: Detecting possible base64 text to match encoded magic bytes \xac\xed\x00\x05 with padding encoded in base64 strings are rO0ABQ KztAAU Cs7QAF Java attack Attempt: Detecting possible base64 text to match encoded magic bytes \xac\xed\x00\x05 with padding encoded in base64 strings are rO0ABQ KztAAU Cs7QAF
944200 1 Java attack Attempt: Detect exploitation of "Java deserialization" Apache Commons Java attack Attempt: Detect exploitation of "Java deserialization" Apache Commons
944152 1 Log4J / Log4Shell Defense This rule addresses exploits against the Log4J library described in several CVEs. It checks for existence of `${`.
944151 1 Log4J / Log4Shell Defense Log4J / Log4Shell Defense: This rule addresses exploits against the Log4J library described in several CVEs.
944150 1 Log4J / Log4Shell Defense This rule addresses exploits against the Log4J library described in several CVEs. It detects Nested use of ${, use of ${jndi:... without the closing bracket.
944140 1 Java Script Uploads: Block file uploads with filenames ending in Java scripts Java Script Uploads: Block file uploads with filenames ending in Java scripts (.jsp, .jspx), scan nonstandard request headers
944130 2 Java attack Attempt: Apache Struts and Oracle WebLogic vulnerabilities Java attack Attempt: Apache Struts and Oracle WebLogic vulnerabilities

944110

944120 1 Java attack Attempt: Apache Struts and Oracle WebLogic vulnerabilities and detect processbuilder or runtime calls Java attack Attempt: Apache Struts and Oracle WebLogic vulnerabilities, Java deserialization
944100 1 Java attack Attempt: Apache Struts and Oracle WebLogic vulnerabilities Java attack Attempt: Apache Struts and Oracle WebLogic vulnerabilities
943120 1 Session Fixation No Referer in SessionID Detects SessionID Parameter Name with No Referer
943110 1 Session Fixation Off-Domain Referer in SessionID Detects SessionID Parameter Name with Off-Domain Referer
943100 1 Session Fixation cookie in HTML Detects Cookie Values in HTML which could be a session fixation attack
942511 2 SQL Injection (SQLi) SQLi bypass: quotes SQL Injection (SQLi) Attempt: Detects quotes and backticks which can be used to bypass filters.
942510 2 SQL Injection (SQLi) SQLi bypass: backticks SQL Injection (SQLi) Attempt: Detects quotes and backticks can be used to bypass SQLi detection.
942500 1 SQL Injection (SQLi) In-line comments SQL Injection (SQLi) Attempt: In-line comments detection
942490 1 SQL Injection (SQLi) classic SQL injection probings SQL Injection (SQLi) Attempt: Detects classic SQL injection probings
942480 2 SQL Injection (SQLi) SQL injection SQL Injection (SQLi) Attempt: SQL injection detection
942470 2 SQL Injection (SQLi) SQL injection SQL Injection (SQLi) Attempt: SQL injection detection
942460 1 SQL Injection (SQLi) Repetitive Non-Word Characters SQL Injection (SQLi) Attempt: Detects when multiple (4 or more) non-word characters are repeated in sequence.
942450 2 SQL Injection (SQLi) SQL Hex Evasion Methods SQL Injection (SQLi) Attempt: Detects SQL Hex Evasion Methods
942440 2 SQL Injection (SQLi) SQL Comment Sequence SQL Injection (SQLi) Attempt: Detects SQL Comment Sequence
942432 1 SQL Injection (SQLi) Restricted SQL Character Anomaly Detection SQL Injection (SQLi) Attempt: Restricted SQL Character Anomaly Detection also detects CVE-2018-2380
942431 1 SQL Injection (SQLi) Restricted SQL Character Anomaly Detection SQL Injection (SQLi) Attempt: Restricted SQL Character Anomaly Detection also detects CVE-2018-2380
942430 1 SQL Injection (SQLi) Restricted SQL Character Anomaly Detection SQL Injection (SQLi) Attempt: This rules attempts to gauge when there is an excessive use of meta-characters within a single parameter payload. Also detects CVE-2018-2380
942421 1 SQL Injection (SQLi) SQL Injection Character Anomaly Usage SQL Injection (SQLi) Attempt: Detects SQL Injection Character Anomaly Usage
942420 1 SQL Injection (SQLi) SQL Injection Character Anomaly Usage SQL Injection (SQLi) Attempt: Detects when there is an excessive use of meta-characters within a single parameter payload.
942410 2 SQL Injection (SQLi) SQL injection SQL Injection (SQLi) Attempt: SQL injection detection also detects CVE-2018-2380
942400 2 SQL Injection (SQLi) SQL injection SQL Injection (SQLi) Attempt: SQL injection detection
942390 2 SQL Injection (SQLi) SQL injection SQL Injection (SQLi) Attempt: SQL injection detection
942380 2 SQL Injection (SQLi) SQL injection SQL Injection (SQLi) Attempt: SQL injection detection
942370 2 SQL Injection (SQLi) classic SQL injection probings SQL Injection (SQLi) Attempt: classic SQL injection probings detection, also detects SAP CRM Java vulnerability CVE-2018-2380
942362 1 SQL Injection (SQLi) Concatenated SQLi and SQLLFI SQL Injection (SQLi) Attempt: Concatenated SQLi and SQLLF detection
942361 1 SQL Injection (SQLi) basic SQL injection based on keyword alter or union SQL Injection (SQLi) Attempt: basic SQL injection based on keyword alter or union detection
942360 3 SQL Injection (SQLi) Concatenated SQLi and SQLLFI SQL Injection (SQLi) Attempt: Concatenated SQLi and SQLLF detection
942350 3 SQL Injection (SQLi) MYSQL UDF/ data structure manipulation SQL Injection (SQLi) Attempt: MYSQL UDF/ data structure manipulation detection
942340 2 SQL Injection (SQLi) basic SQL auth bypass attempts SQL Injection (SQLi) Attempt: basic SQL authentication bypass attempts detection
942330 3 SQL Injection (SQLi) classic SQL injection probings SQL Injection (SQLi) Attempt: classic SQL injection probings detection
942320 2 SQL Injection (SQLi) MYSQL/ PostgreSQL stored procedure and function injection SQL Injection (SQLi) Attempt: MYSQL/ PostgreSQL stored procedure and function injection detection
942310 2 SQL Injection (SQLi) chained SQL injection SQL Injection (SQLi) Attempt: chained SQL injection detection
942300 2 SQL Injection (SQLi) MySQL comments, conditions and ch(a)r injections SQL Injection (SQLi) Attempt: MySQL comments, conditions and ch(a)r injections detection
942290 1 SQL Injection (SQLi) MongoDB SQLi SQL Injection (SQLi) Attempt: MongoDB SQL injection detection
942280 2 SQL Injection (SQLi) pg_sleep injection/ waitfor delay/ database shutdown SQL Injection (SQLi) Attempt: pg_sleep injection/ waitfor delay attack/ database shutdown detection
942270 1 SQL Injection (SQLi) Common SQLi attacks for various dbs SQL Injection (SQLi) Attempt: Common attacks against msql, oracle, and other dbs detection
942260 3 SQL Injection (SQLi) basic SQL auth bypass SQL Injection (SQLi) Attempt: basic SQL authentication bypass detection
942251 2 SQL Injection (SQLi) SQL HAVING queries SQL Injection (SQLi) Attempt: Detects SQL HAVING queries
942250 2 SQL Injection (SQLi) Merge / Execute / Immediate injections SQL Injection (SQLi) Attempt: MERGE / EXECUTE / IMMEDIATE injections detection
942240 2 SQL Injection (SQLi) MYSQL charset/ MSSQL DOS SQL Injection (SQLi) Attempt: MYSQL charset/ MSSQL DOS detection
942230 2 SQL Injection (SQLi) Conditional SQL injections SQL Injection (SQLi) Attempt: Conditional SQL injection detection
942220 2 SQL Injection (SQLi) Integer overflow attacks SQL Injection (SQLi) Attempt: Integer Overflow attack detection
942210 3 SQL Injection (SQLi) chained SQL injection attempts SQL Injection (SQLi) Attempt: chained SQL injection attempts detection, also triggers SAP CRM Java vulnerability CVE-2018-2380
942200 2 SQL Injection (SQLi) MySQL comment-/space-obfuscated injections and backtick termination SQL Injection (SQLi) Attempt: MySQL comment-/space-obfuscated injections and backtick termination detection and also triggers SAP CRM Java vulnerability CVE-2018-2380
942190 2 SQL Injection (SQLi) MSSQL code execution and info gathering SQL Injection (SQLi) Attempt: MSSQL code execution and info gathering detection
942180 2 SQL Injection (SQLi) Basic SQL auth bypass SQL Injection (SQLi) Attempt: Basic SQL authentication bypass detection
942170 2 SQL Injection (SQLi) SQL benchmark and sleep injections SQL Injection (SQLi) Attempt: SQL benchmark and sleep injection detection
942160 2 SQL Injection (SQLi) PHPIDS SQLi Filters SQL Injection (SQLi) Attempt: SQLi Filters via PHPIDS
942151 1 SQL Injection (SQLi) SQL Function Names SQL Injection (SQLi) Attempt: SQL Function Names detection also detects CVE-2018-2380
942150 2 SQL Injection (SQLi) SQL Function Names SQL Injection (SQLi) Attempt: SQL Function Names detection also detects SAP CRM Java vulnerability CVE-2018-2380
942140 3 SQL Injection (SQLi) Detect DB Names SQL Injection (SQLi) Attempt: SQLi Filters via DB Names
942131 1 SQL Injection (SQLi) SQL Tautologies SQL Injection (SQLi) Attempt: Boolean-based SQL injection detection or SQL Tautologies detection using inequalities
942130 3 SQL Injection (SQLi) SQL Tautologies SQL Injection (SQLi) Attempt: SQL Tautologies detection using equalities or Boolean-based SQL injection detection
942120 2 SQL Injection (SQLi) SQL operators SQL Injection (SQLi) Attempt: SQL operators detection also detects CVE-2018-2380
942110 1 SQL Injection (SQLi) String termination/ Statment ending injection SQL Injection (SQLi) Attempt: String termination/ Statment ending injection detection also detects CVE-2018-2380
942101 1 SQL Injection (SQLi) Libinjection SQL Injection (SQLi) Attempt: Detects SQLi using libinjection
942100 1 SQL Injection (SQLi) Libinjection Detection SQL Injection (SQLi) Attempt: SQLi Filters via libinjection
9420000 2 SQL Injection (SQLi) Collaborative Group - SQLi Filters Categories SQL Injection (SQLi) Attempt: SQLi Filters via libinjection - Detect Database names - PHPIDS - Converted SQLI Filters.
941380 1 Cross-Site Scripting (XSS) Attempt: Defend against AngularJS client side template injection Cross-Site Scripting (XSS) Attempt: Defend against AngularJS client side template injection
941370 1 Cross-Site Scripting (XSS) Attempt: Prevent 94118032 bypass by using JavaScript global variables Cross-Site Scripting (XSS) Attempt: Prevent 94118032 bypass by using JavaScript global variables
941360 1 Cross-Site Scripting (XSS) Attempt: Defend against JSFuck and Hieroglyphy obfuscation of Javascript code. Cross-Site Scripting (XSS) Attempt: Defend against JSFuck and Hieroglyphy obfuscation of Javascript code.
941350 3 Cross-Site Scripting (XSS) Attempt: UTF-7 encoding XSS filter evasion for IE Cross-Site Scripting (XSS) Attempt: UTF-7 encoding XSS filter evasion for IE
941340 2 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941330 3 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941320 2 Cross-Site Scripting (XSS) Attempt: HTML Tag Handler Cross-Site Scripting (XSS) Attempt: HTML Tag Handler
941310 3 Cross-Site Scripting (XSS) Attempt: US-ASCII encoding bypass listed on XSS filter evasion Cross-Site Scripting (XSS) Attempt: US-ASCII encoding bypass listed on XSS filter evasion
941300 2 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941290 2 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941280 2 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941270 2 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941260 2 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941250 2 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941240 3 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941230 2 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941220 2 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941210 2 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941200 2 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941190 3 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941180 3 Cross-Site Scripting (XSS) Attempt: Blacklist Keywords from Node-Validator Cross-Site Scripting (XSS) Attempt: Blacklist Keywords from Node-Validator
941170 3 Cross-Site Scripting (XSS) Attempt: NoScript XSS Filters Cross-Site Scripting (XSS) Attempt: NoScript XSS Filters, NoScript InjectionChecker - Attributes injection
941160 3 Cross-Site Scripting (XSS) Attempt: NoScript XSS Filters Cross-Site Scripting (XSS) Attempt: NoScript XSS Filters, NoScript InjectionChecker - HTML injection
941150 2 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 5 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 5. HTML attributes - src, style and href
941140 3 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 4 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 4. XSS vectors making use of javascript URI and tags, e.g., &lt;p style="background:url(javascript:alert(1))"&gt;
941130 4 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 3 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 3. XSS vectors making use of Attribute Vectors
941120 4 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 2 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 2. XSS vectors making use of event handlers like onerror, onload, etc., e.g., &lt;body onload="alert(1)"&gt;
941181 1 Cross-Site Scripting (XSS) Attempt: Blacklist Keywords from Node-Validator Cross-Site Scripting (XSS) Attempt: Blacklist Keywords from Node-Validator
941110 2 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 1 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 1. Script tag based XSS vectors, e.g., &lt;script&gt; alert(1)&lt;/script&gt;
941101 3 Cross-Site Scripting (XSS) Attempt: Referer Header Attack Detected via libinjection Cross-Site Scripting (XSS) Attempt: On Referer Header XSS Attack Detected via libinjection
941100 2 Cross-Site Scripting (XSS) Attempt: Libinjection - XSS Detection Cross-Site Scripting (XSS) Attempt: Detects XSS Libinjection
9410000 3 Cross-Site Scripting (XSS) Collaborative Group - XSS Filters Categories Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 1.
934131 1 JavaScript Prototype Pollution Detects JavaScript Prototype Pollution
934130 1 JavaScript prototype pollution injection attempts Detects JavaScript prototype pollution injection attempts.
934120 1 Server-Side Request Forgery Attack PL2 rules adds SSRF capture for common evasion techniques
934110 1 Server-Side Request Forgery Attack Detects generic Server-Side Request Forgery Attacks.
934100 2 Insecure unserialization Remote Code Execution Detects generic Remote Code Executions on Insecure unserialiazation. Detects CVE-2017-5941
933210 2 PHP Injection Attacks: PHP Functions - Variable Function Prevent Bypass PHP Injection Attacks: PHP Functions - Variable Function Calls, This rule blocks bypass filter payloads.
933200 1 PHP Injection Attacks: PHP Wrappers PHP Injection Attacks: PHP Wrappers, PHP comes with many built-in wrappers for various URL-style protocols for use with the filesystem functions such as fopen(), copy(), file_exists() and filesize(). Abusing of PHP wrappers like phar://, zlib://, glob://, rar://, zip://, etc... could lead to LFI and expect:// to RCE.
933190 1 PHP Injection Attacks: PHP Closing Tag Found PHP Injection Attacks: PHP Closing Tag Found.
933180 2 PHP Injection Attacks: PHP Functions - Variable Function Calls PHP Injection Attacks: PHP Functions - Variable Function Calls, PHP 'variable functions' provide an alternate syntax for calling PHP functions. An attacker may use variable function syntax to evade detection of function names during the exploitation of a remote code execution vulnerability.
933170 2 PHP Injection Attacks: PHP Object Injection PHP Injection Attacks: PHP Object Injection, is an application-level vulnerability that could allow an attacker to perform different kinds of malicious attacks, such as Code Injection, SQL Injection, Path Traversal and Application Denial of Service, depending on the context. The vulnerability occurs when user-supplied input is not properly sanitized before being passed to the unserialize() PHP function.
933161 2 PHP Injection Attacks: PHP Functions - Low-Value PHP Function Calls PHP Injection Attacks: PHP Functions - Low-Value PHP Function Calls. Most of these function names are likely to cause false positives in natural text or common parameter values, such as 'abs', 'copy', 'date', 'key', 'max', 'min'. Therefore, these function names are not scanned in lower paranoia levels or if high false positives are expected.
933160 2 PHP Injection Attacks: High-Risk PHP Function Calls PHP Injection Attacks: High-Risk PHP Function Calls, some PHP function names have a certain risk of false positives, due to short names, full or partial overlap with common natural language terms, uses in other contexts, et cetera. Some examples are 'eval', 'exec', 'system'.
933151 3 PHP Injection Attacks: Medium-Risk PHP Function Names PHP Injection Attacks: Medium-Risk PHP Function Names, Medium-Risk PHP injection payloads, and extremely rare in natural language or other contexts. This includes most PHP functions and keywords.
933150 3 PHP Injection Attacks: High-Risk PHP Function Names PHP Injection Attacks: High-Risk PHP Function Names, Approx. 40 words highly common to PHP injection payloads and extremely rare in natural language or other contexts. Examples: 'base64_decode', 'file_get_contents'.
933140 2 PHP Injection Attacks: PHP I/O Streams PHP Injection Attacks: Variables Found. The "php://" syntax can be used to refer to various objects, such as local files (for LFI), remote urls (for RFI), or standard input/request body. Its occurrence indicates a possible attempt to either inject PHP code or exploit a file inclusion vulnerability in a PHP web app.
933131 2 PHP Injection Attacks: PHP Variables - Common Variable Indexes PHP Injection Attacks: Common Variable Indexes
933130 3 PHP Injection Attacks: PHP Variables PHP Injection Attacks: Variables Found
933120 3 PHP Injection Attacks: PHP Configuration Directives PHP Injection Attacks: Configuration Directive Found
933111 2 PHP Injection Attacks: PHP Script Uploads - Superfluous extension PHP Injection Attacks: PHP Script Uploads - Superfluous extension. Block file uploads with PHP extensions (.php, .php5, .phtml etc) anywhere in the name, followed by a dot.
933110 2 PHP Injection Attacks: PHP Script Uploads

PHP Injection Attacks: Block file uploads with PHP extensions (.php, .php5, .phtml etc), also block files with just dot (.) characters after the extension. Many applications contain Unrestricted File Upload vulnerabilities. Attackers may use such a vulnerability to achieve remote code execution by uploading a .php file.

Some AJAX uploaders use the nonstandard request headers X-Filename, X_Filename, or X-File-Name to transmit the file name to the server scan these request headers as well as multipart/form-data file names.
933100 3 PHP Injection Attacks: PHP Open Tag Found PHP Injection Attacks: Detects PHP open tags "&lt;?" and "&lt;?php". Also detects "[php]", "[/php]" and "[\php]" tags used by some applications to indicate PHP dynamic content.
9330000 2 PHP Injection Attacks Collaborative Group - PHP Filters Categories PHP Injection Attempt: PHP Filters - Detects PHP open tags "&lt;?", "&lt;?php", "[php]", "[/php]" and "[\php]" - PHP Script Uploads, PHP Config Directives, PHP Functions, PHP Object Injection.
932321 1 Remote Command Execution: POP3 Command Execution This rule prevents execution of POP3 related system commands.
932320 1 Remote Command Execution: POP3 Command Execution This rule prevents execution of POP3 related system commands.
932311 1 Remote Command Execution: IMAP4 Command Execution. This rule prevents execution of IMAP4 related system commands.
932310 1 Remote Command Execution: IMAP Command Execution This rule prevents execution of IMAP4 related system commands.
932301 1 Remote Command Execution: SMTP Command Execution This rule prevents execution of SMTP related system commands.
932300 1 Remote Command Execution: SMTP Command Execution This rule prevents execution of SMTP related system commands.
932210 1 Remote Command Execution: Blocks SQLite System Command Execution like .system and .shell This rule prevents execution of SQLite CLI commands like .system and .shell.
932200 2 Block Remote Code Execution Bypass Attacks Blocks Remote Code Execution Bypass Attacks using different Techniques as uninitialized variables, string concatenations, and globbing patterns.
932190 2 Remote Command Execution - OS File Access Attempt Wildcard bypass attempt A Remote Command Execution (RCE) could be exploited bypassing rule 930120 (OS File Access Attempt) by using wildcard characters. Consider this rule could lead to many false positives.
932180 2 Restricted File Upload Detects attempts to upload a file with a forbidden filename. Many applications contain Unrestricted File Upload vulnerabilities. These might be abused to upload configuration files or other files that affect the behavior of the web server, possibly causing remote code execution.

932170

932171 2 GNU Bash RCE Shellshock Vulnerability (CVE-2014-6271 and CVE-2014-7169) Detect exploitation of "Shellshock" GNU Bash RCE vulnerability. Based on ModSecurity rules created by Red Hat.
932160 3 Unix Shell Snippets Injection Detects some common sequences found in shell commands and scripts. This rule is also triggered by an Apache Struts Remote Code Execution CVE-2017-9805, and Oracle WebLogic Remote Command Execution exploits CVE-2017-10271.
932150 3 Unix Direct Remote Command Execution Detects Unix commands at the start of a parameter (direct RCE). Example: foo=wget%20www.example.com. This case is different from command injection (rule 93210032), where a command string is appended (injected) to a regular parameter, and then passed to a shell unescaped. This rule is also triggered by an Oracle WebLogic Remote Command Execution exploit CVE-2017-10271.
932140 2 Windows Command Shell Injection - FOR and IF commands This rule detects Windows command shell FOR and IF commands.
932131 1 Unix Shell Script Expressions and Oneliners Detects common Unix Shell Expressions used in Shell Scripts and Oneliners, such as "$(foo), ${foo}, &lt;(foo), &gt;(foo), $((foo)), among others"
932130 3 Unix Shell Script Expressions and Oneliners. Detects common Unix Shell Expressions used in Shell Scripts and Oneliners, such as "$(foo), ${foo}, &lt;(foo), &gt;(foo), $((foo)), among others"
932120 3 Windows PowerShell Injection - cmdlets and options Detect some common PowerShell commands, cmdlets, and options. These commands should be relatively uncommon in normal text, but potentially useful for code injection.
932115 3 Windows Command Injection This rule detects Windows shell command injections (and its attempts of obfuscation and evasion). The vulnerability exists when an application executes a shell command without proper input escaping/validation. This rule is also triggered by an Oracle WebLogic Remote Command Execution exploit CVE-2017-10271.
932110 3 Windows Command Injection This rule detects Windows shell command injections (and its attempts of obfuscation and evasion). The vulnerability exists when an application executes a shell command without proper input escaping/validation.
932106 2 Unix Command Injection Detects several Unix command injections (and its attempts of obfuscation and evasion). The vulnerability exists when an application executes a shell command without proper input escaping/validation.
932105 3 Unix Command Injection Detects several Unix command injections (and its attempts of obfuscation and evasion). The vulnerability exists when an application executes a shell command without proper input escaping/validation.
932101 1 Command Injection Attack Detects Command Injection Attempts.
932100 3 Unix Command Injection Detects several Unix command injections (and its attempts of obfuscation and evasion). The vulnerability exists when an application executes a shell command without proper input escaping/validation. This rule is also triggered by an Oracle WebLogic Remote Command Execution exploit CVE-2017-10271.
9320001 2 Remote Code Execution (RCE) Collaborative Group - Windows RCE Filter Categories Remote Code Execution (RCE) Attempt: RCE Filters for Windows.
9320000 2 Remote Code Execution (RCE) Collaborative Group - Unix RCE Filter Categories Remote Code Execution (RCE) Attempt: RCE Filters for Unix.
931130 3 Remote File Inclusion (RFI) Attempt: RFI Attack: Off-Domain Reference/Link Remote File Inclusion (RFI). These rules look for common types of Remote File Inclusion (RFI) attack methods. Possible RFI Attack: Off-Domain Reference/Link
931120 2 Remote File Inclusion (RFI) Attempt: RFI Attack: URL Payload Used w/Trailing Question Mark Character (?) Remote File Inclusion (RFI). These rules look for common types of Remote File Inclusion (RFI) attack methods. Possible RFI Attack: URL Payload Used w/Trailing Question Mark Character (?)
931110 3 Remote File Inclusion (RFI) Attempt: RFI Attack: Common RFI Vulnerable Parameter Name used w/URL Payload Remote File Inclusion (RFI). These rules look for common types of Remote File Inclusion (RFI) attack methods. Possible RFI Attack: Common RFI Vulnerable Parameter Name used w/URL Payload
931100 3 Remote File Inclusion (RFI) Attempt: RFI Attack URL Parameter using IP Address Remote File Inclusion (RFI). These rules look for common types of Remote File Inclusion (RFI) attack methods. Possible RFI Attack: URL Parameter using IP Address
930130 2 Local File Inclusion (LFI) - Restricted File Access Local File Inclusion (LFI) Attempt: Restricted File Access
930120 2 Local File Inclusion (LFI) - OS File Access Local File Inclusion (LFI) Attempt: OS File Access
930110 3 Local File Inclusion (LFI) - Directory Traversal - Decoded Payloads Local File Inclusion (LFI) Attempt: Directory Traversal Attacks - Decoded Payloads
930100 3 Local File Inclusion (LFI) - Directory Traversal - Encoded Payloads Local File Inclusion (LFI) Attempt: Directory Traversal Attacks - Encoded Payloads
9300000 2 Local File Inclusion (LFI) Collaborative Group - LFI Filter Categories Local File Inclusion (LFI) Attempt: Directory Traversal Attacks - OS File Access.
921200 1 LDAP Injection This is a rule trying to prevent LDAP injection.
921190 1 HTTP Splitting This rule detect \n or \r in the REQUEST FILENAME.
921151 1 Newline in GET Args Detect newlines in GET arguments which may point to HTTP header injection attacks.

921150

921160 2 Argument Newline Detection Detect newlines in argument names.
921140 1 HTTP Header Injection These rules look for Carriage Return (CR) %0d and Linefeed (LF) %0a characters, on their own or in combination with header field names. These characters may cause problems if the data is returned in a response header and interpreted by the client.

921120

921130 2 HTTP Response Splitting Looks for CR/LF characters, may cause problems if the data is returned in a response header and may be interpreted by an intermediary proxy server and treated as two separate responses.
921110 3 HTTP Request Smuggling Looks for CR/LF characters in combination with HTTP / WEBDAV
920521 1 Invalid Accept-Encoding Header Detects invalid Accept-Encoding Headers
920520 1 Accept-Encoding Header Longer than 50 Characters This rule matches against requests that have more than 50 characters in the Accept-Encoding header value.
920510 1 Invalid Cache-Control Value Description: Rule detects invalid values in the cache-control header
920500 1 Detect backup or working files Detect backup or working files.
920490 1 Bypass Content-Type Header with x-up-devcap-post-charset Detection of Content-Type bypass with x-up-devcap-post-charset header
920480 1 Charset restriction in content-type Restrict charset in Content Types by checking the variable allowed_request_content_type_charset.
920470 3 Restrict Content-Type Restrict Content Types by checking the content-type header
920450 2 Restricted HTTP headers The use of certain headers is restricted. They are listed in the variable restricted_headers.
920440 1 Restriction by file extension Restrict file extensions using the variable restricted_extensions.
920430 1 Request protocol version restriction Restrict protocol versions by using the variable allowed_http_versions.
920420 2 Check content-type header against allow list Restrict Content Types by checking the variable allowed_request_content_type.
920410 1 Limit combined file size Limits the size of combined files by checking Content-Length Header for a variable combined_file_sizes
920400 1 Limit file size Limits the size of a file by checking Content-Length Header for a variable max_file_size
920390 1 Limit arguments total length detects HTTP requests argument length exceeding the configurable "Max argument length" parameter
920380 1 Number of Arguments Limits detects HTTP requests with a number of arguments exceeding the configurable "Max amount of arguments" value
920370 1 Limit argument value length detects HTTP requests argument values exceeding the configurable "Max argument value length" parameter
920360 1 Limit length of argument names detects HTTP requests argument name length exceeding the configurable "Max length of argument name" value
920350 3 Host Header Is IP Address Detects if the host header is a numeric IP address as it could be indicative of automated client access
920341 1 Missing Content-Type Header in request body Detects requests that have content but no Content-Type header
920340 1 Empty Content-Type Header with Request Body Checks if the Content-Type header is present on a request that has a Content-Length Value
920330 1 Empty User-Agent Header detects empty request user-agent header
920320 1 Missing User-Agent header Detection of missing user-agent header

920310

920311 1 Empty Accept Header Checks if an Accept header exists, but has an empty value. Also, detect an empty Accept header if there is no user agent.
920300 2 Missing Accept Header Detection of missing accept header.
920290 1 Missing Host Header This rule checks for the presence of a host header or an empty host header.
920280 1 Missing/Empty Host Header Missing/Empty Host Header
920272 1 Low Range Printable Characters Detects requests that contain printable characters in the low range
920271 1 Nonprinting characters in request This rule checks for nonprinting characters in the request
920270 1 Restrict type of characters sent This rule uses the @validateByteRange operator to restrict the request payloads.
920260 1 Disallow use of full-width unicode as decoding evasions may be possible. This rule looks for full-width encoding by looking for %u followed by 2 'f' characters and then 2 hex characters. It is a vulnerability that affected IIS circa 2007.
920230 1 Detect multiple url encoding Detection of multiple URL encodings.

920220

920240 1 Check URL encodings There are two different chained rules. We need to separate them as we are inspecting two different variables - REQUEST_URI and REQUEST_BODY. For REQUEST_BODY, we only want to run the @validateUrlEncoding operator if the content-type is application/x-www-form-urlencoding.
920210 1 Check duplicate or conflicting headers. This rule inspects the Connection header and looks for duplicates of the keep-alive and close options.

920200

920201 1 Range Header Validation This rule inspects the Range request header to see if it starts with 0.
920190 2 Range Header Validation This rule inspects the Range request header to see if it starts with 0.
920181 1 Transfer Encoding Validation Detects if content-length and Transfer-Encoding headers are present which breaks RFC
920180 2 Content-Length Header Validation Detects if content-length and Transfer-Encoding headers are provided with every POST request
920171 1 GET/HEAD Requests Validation detects if GET/HEAD requests contain request body by checking for Transfer-Encoding header since it is not a common practice
920170 1 GET/HEAD Requests Validation detects if GET/HEAD requests contain request body by checking for content-length header since it is not a common practice
920160 1 Content-Length Header Validation Detects if content-length HTTP header is not numeric
920120 2 File Name Validation Detects multipart/form-data file name evasion attempts
920100 3 Request Line Format Validation against the HTTP RFC Uses rule negation against the regex for positive security. The regex specifies the proper construction of URI request lines such as: "http:" "//" host [ ":" port ] [ abs_path [ "?" query ]]. It also outlines proper construction for CONNECT, OPTIONS and GET requests.
9200024 2 Limit length of request header size detects size of http request header length
9200024 1 Limit length of request header size detects size of http request header length
9200014 2 Limit Number of Request Headers detects if there are more headers then the desired amount
9200014 1 Limit Number of Request Headers detects if there are more headers then the desired amount
913120 1 Check URL args and filenames for Vulnerability Scanners This rule inspects the URL arguments/ filenames for vulnerability scanner identifiers.
913110 1 Check HTTP Headers for Vulnerability Scanners This rule inspects HTTP headers for vulnerability scanner identifiers.
913102 1 Check User-Agent for Web Crawlers/Bots This rule inspects the User-Agent header for Web Crawlers/ Bots identifiers.
913101 1 Check User-Agent for Generic/Scripting This rule inspects the User-Agent header for generic/ scripting identifiers.
913100 1 Check User-Agent for Vulnerability Scanners This rule inspects the User-Agent header for vulnerability scanner identifiers.
911100 1 Restrict HTTP Request Methods allows only request methods specified by the configurable "Allowed http methods" parameter
46451 1 CVE-2018-7600, CVE-2018-7602, Drupal unsafe internal attribute remote code execution attempt Drupal unsafe internal attribute remote code execution attempt
46316 1 CVE-2018-7600, CVE-2018-7602, Drupal 8 remote code execution attempt Drupal 8 remote code execution attempt
43813 1 CVE-2017-9813, Kaspersky Linux File Server WMC cross site scripting attempt Kaspersky Linux File Server WMC cross site scripting attempt
43812 1 CVE-2017-9812, Kaspersky Linux File Server WMC directory traversal attempt Kaspersky Linux File Server WMC directory traversal attempt
43811 1 CVE-2017-9812, Kaspersky Linux File Server WMC directory traversal attempt Kaspersky Linux File Server WMC directory traversal attempt
41409 1 CVE-2017-3823, CVE-2017-6753, Cisco WebEx explicit use of web plugin Cisco WebEx explicit use of web plugin

202260581 1

GitLab project import vulnerability allows remote code execution attacks

GitLab project import vulnerability allows remote code execution attacks.

202260329 1

Atlassian Jira Seraph vulnerability exploited auth bypass attempt via specially crafted HTTP request

Atlassian Jira Seraph vulnerability exploited auth bypass attempt via specially crafted HTTP request.

202260328 1

Atlassian Jira Seraph vulnerability exploited auth bypass attempt via specially crafted HTTP request

Atlassian Jira Seraph vulnerability exploited auth bypass attempt via specially crafted HTTP request.
202258721 1 Grafana Directory Traversal Vulnerability Grafana Directory Traversal Vulnerability
202258715 1 Zoho ManageEngine ServiceDesk Plus remote code execution (RCE) vulnerability Zoho ManageEngine ServiceDesk Plus remote code execution (RCE) vulnerability
202258714 1 Zoho ManageEngine ServiceDesk Plus Remote Code Execution (RCE) Vulnerability Zoho ManageEngine ServiceDesk Plus remote code execution (RCE) vulnerability
202258696 1 Zoho ManageEngine ServiceDesk Plus arbitrary file upload vulnerability Zoho ManageEngine ServiceDesk Plus arbitrary file upload vulnerability
202258638 1 Microsoft Exchange Server remote code execution attack Microsoft Exchange Server remote code execution attack
202258637 1 Microsoft Exchange Server Remote Code Execution (RCE) Vulnerability Microsoft Exchange Server Remote Code Execution (RCE) Vulnerability
202258447 1 Apache Druid Remote Code Execution (RCE) Vulnerability Apache Druid Remote Code Execution (RCE) Vulnerability
202258422 1 BQE BillQuick Web Suite SQL Injection Vulnerability BQE BillQuick Web Suite SQL injection vulnerability
202258421 1 BQE BillQuick Web Suite SQL Injection Vulnerability BQE BillQuick Web Suite SQL injection vulnerability

202259388 1 Spring Cloud Function Remote Code Execution (RCE) Vulnerability Spring Cloud Function Remote Code Execution (RCE) Vulnerability.
202257983 1 Microsoft Exchange autodiscover server side request forgery attempt Microsoft Exchange autodiscover server side request forgery attempt.

202257907 1

Microsoft Exchange autodiscover server side request forgery attempt

Microsoft Exchange autodiscover server side request forgery attempt.

202257906 1

Microsoft Exchange autodiscover server side request forgery attempt

Microsoft Exchange autodiscover server side request forgery attempt.
20224794 1 The AAWP WordPress plugin can be used to abuse trusted domains to load malware or other files through it to bypass firewall rules in companies The AAWP WordPress plugin can be used to abuse trusted domains to load malware or other files through it to bypass firewall rules in companies
20224230 1 SQLi vulnerabilities for WordPress plugins (WP-Statistics, SiteGround Security, Prestashop totadministrativemandate) SQLi vulnerabilities for WordPress plugins

202237042 1

Zimbra mboximport functionality vulnerable to directory traversal and remote code execution via extracted files from ZIP archive

Zimbra mboximport functionality vulnerable to directory traversal and remote code execution via extracted files from ZIP archive.

202235405 1

Zoho ManageEngine Password Manager Pro vulnerable to unauthenticated remote code execution

Zoho ManageEngine Password Manager Pro vulnerable to unauthenticated remote code execution.

202234265 1

Django Trunc() and Extract() database functions subject to SQL injection if untrusted data is used as a kind/lookup_name value

Django Trunc() and Extract() database functions subject to SQL injection if untrusted data is used as a kind/lookup_name value.
202229105 1 Zoho ManageEngine Desktop Central directory traversal vulnerability Zoho ManageEngine Desktop Central directory traversal vulnerability
202224112 1 Apache APISIX Remote Code Execution (RCE) Vulnerability This vulnerability allows an attacker to abuse the batch-requests plugin sending requests to bypass the IP restriction of Admin API
202223944 1 Apache ShenYu Authentication Bypass Vulnerability This vulnerability allows users to access /plugin api without authentication.
202222965 1 Spring MVC or Spring WebFlux Application Remote Code Execution (RCE) Vulnerability A Spring MVC or Spring WebFlux application running on JDK 9+ may be vulnerable to remote code execution (RCE) via data binding.
202222963 1 Spring Cloud Function Remote Code Execution (RCE) Vulnerability This vulnerability allows malicious users to provide a specially crafted SpEL as a routing-expression that may result in remote code execution and access to local resources
202222947 1 Spring Cloud Gateway Spring Code Injection Vulnerability This vulnerability allows remote attackers to make a maliciously crafted request that could allow arbitrary remote execution on the remote host where the Gateway Actuator endpoint is enabled
202222930 1 Mingsoft MCMS Remote Code Execution (RCE) Vulnerability Mingsoft MCMS Remote Code Execution (RCE) Vulnerability
202222536 1 SAP Internet Communication Manager Request Smuggling and Request Concatenation Vulnerability SAP Internet Communication Manager Request Smuggling and Request Concatenation Vulnerability
202221907 1 CVE-2022-21907 HTTP Protocol Stack Remote Code Execution Vulnerability CVE-2022-21907 HTTP Protocol Stack Remote Code Execution Vulnerability
202221661 1 CVE-2022-21661 WordPress Core SQL injection Vulnerability This vulnerability allows remote attackers to disclose sensitive information on affected installations of WordPress Core (older versions than 5.8.3)
202201388 1 CVE-2022-1388 F5 BIG-IP iControl REST Authentication Vulnerability This vulnerability may allow an unauthenticated attacker with network access to the BIG-IP system through the management port and/or self IP addresses to execute arbitrary system commands
202158301 1 Alibaba Nacos AuthFilter servlet filter backdoor potential authentication bypass Alibaba Nacos potential authentication bypass attempt exploiting backdoor on AuthFilter servlet
202158300 1 Alibaba Nacos AuthFilter servlet filter backdoor potential authentication bypass Alibaba Nacos potential authentication bypass attempt exploiting backdoor on AuthFilter servlet
202158273 1 QNAP HBS 3 vulnerability authorization bypass attempt QNAP HBS 3 vulnerability authorization bypass attempt
202158217 1 VMware vCenter Server file upload vulnerability remote code execution VMware vCenter Server file upload vulnerability remote code execution
202158201 1 Zoho ManageEngine ADSelfService Plus REST API authentication bypass Zoho ManageEngine ADSelfService Plus REST API authentication bypass
202158169 1 Microsoft Windows Open Management Infrastructure remote code execution Microsoft Windows Open Management Infrastructure remote code execution
202158112 1 Microsoft SharePoint vulnerability exploited remote code execution Microsoft SharePoint vulnerability exploited remote code execution
202158111 1 Microsoft SharePoint vulnerability exploited remote code execution Microsoft SharePoint vulnerability exploited remote code execution
202158094 1 Atlassian Confluence OGNL injection vulnerability exploited remote code execution Atlassian Confluence OGNL injection vulnerability exploited remote code execution
202158093 1 Atlassian Confluence OGNL injection vulnerability exploited remote code execution Atlassian Confluence OGNL injection vulnerability exploited remote code execution
202158066 1 Nagios XI vulnerability exploited command injection attack Nagios XI vulnerability exploited command injection attack
202158065 1 Nagios XI vulnerability exploited command injection attack Nagios XI vulnerability exploited command injection attack
202158058 1 Realtek Jungle SDK vulnerability exploited command injection attack Realtek Jungle SDK vulnerability exploited command injection attack
202158057 1 Realtek Jungle SDK vulnerability exploited command injection attack Realtek Jungle SDK vulnerability exploited command injection attack
202158056 1 Realtek Jungle SDK vulnerability exploited command injection attack Realtek Jungle SDK vulnerability exploited command injection attack
202158054 1 Realtek Jungle SDK vulnerability exploited command injection attack Realtek Jungle SDK vulnerability exploited command injection attack
202158053 1 Realtek Jungle SDK vulnerability exploited command injection attack Realtek Jungle SDK vulnerability exploited command injection attack
202158052 1 Realtek Jungle SDK vulnerability exploited command injection attack Realtek Jungle SDK vulnerability exploited command injection attack
202157983 1 Microsoft Exchange Elevation of Privilege Vulnerability autodiscover server side request forgery Microsoft Exchange Elevation of Privilege Vulnerability autodiscover server side request forgery
202157932 1 ExifTool DjVu file format improper neutralization command injection attack ExifTool DjVu file format improper neutralization command injection attack
202157931 1 ExifTool DjVu file format improper neutralization command injection attack ExifTool DjVu file format improper neutralization command injection attack
202157921 1 Apache OFBiz XMLRPC unsafe deserialization RCE attack Apache OFBiz XMLRPC unsafe deserialization RCE attack
202157913 1 ForgeRock AM server deserialization vulnerability remote code execution ForgeRock AM server deserialization vulnerability remote code execution
202157912 1 ForgeRock AM server deserialization vulnerability remote code execution ForgeRock AM server deserialization vulnerability remote code execution
202157910 1 Microsoft SharePoint Server RCE vulnerability remote code execution attack Microsoft SharePoint Server RCE vulnerability remote code execution attack
202157909 1 Microsoft Exchange Elevation of Privilege Vulnerability autodiscover server side request forgery Microsoft Exchange Elevation of Privilege Vulnerability autodiscover server side request forgery
202157908 1 Microsoft Exchange Elevation of Privilege Vulnerability autodiscover server side request forgery Microsoft Exchange Elevation of Privilege Vulnerability autodiscover server side request forgery
202157907 1 Microsoft Exchange Elevation of Privilege Vulnerability autodiscover server side request forgery Microsoft Exchange Elevation of Privilege Vulnerability autodiscover server side request forgery
202157906 1 Microsoft Exchange Elevation of Privilege Vulnerability server side request forgery Microsoft Exchange Elevation of Privilege Vulnerability server side request forgery
202157898 1 SolarWinds Network Performance Monitor insecure deserialization SolarWinds Network Performance Monitor insecure deserialization
202157872 1 Facade Ignition remote code execution attack Facade Ignition remote code execution attack
202157836 1 Nagios XI vulnerability exploited command injection attack Nagios XI vulnerability exploited command injection attack
202157835 1 Nagios XI vulnerability exploited command injection attack Nagios XI vulnerability exploited command injection attack
202157720 1 VMWare vSphere Client insufficient input validation remote code execution VMWare vSphere Client insufficient input validation remote code execution
202157549 1 Microsoft Windows HTTP protocol stack remote code execution attack Microsoft Windows HTTP protocol stack remote code execution attack
202157548 1 Microsoft SharePoint remote code execution attack Microsoft SharePoint remote code execution attack
202157487 1 Microsoft Exchange MeetingHandler remote code execution attack Microsoft Exchange MeetingHandler remote code execution attack
202157482 1 ManageEngine OpManager vulnerable to Directory Traversal attacks ManageEngine OpManager vulnerable to Directory Traversal attacks
202157481 1 ManageEngine OpManager vulnerable to Directory Traversal attacks ManageEngine OpManager vulnerable to Directory Traversal attacks
202157454 1 Exploiting Pulse Connect Secure vulnerability, URI access attempt Exploiting Pulse Connect Secure vulnerability, URI access attempt
202157450 1 F5 WAF/BIG-IP ASM virtual server crafted http response trigger buffer overflow F5 WAF/BIG-IP ASM virtual server crafted http response trigger buffer overflow
202157449 1 F5 TMM crafted IPv6 URI normalization buffer overflow attack F5 TMM crafted IPv6 URI normalization buffer overflow attack
202157439 1 VMware View Planner arbitrary file upload attempt to logupload Application VMware View Planner arbitrary file upload attempt to logupload Application
202157438 1 VMware View Planner arbitrary file upload attempt to logupload Application VMware View Planner arbitrary file upload attempt to logupload Application
202157437 1 VMware View Planner logupload vulnerability exploited Remote Code Execution attack VMware View Planner logupload vulnerability exploited Remote Code Execution attack
202157436 1 VMware View Planner logupload vulnerability exploited Remote Code Execution attack VMware View Planner logupload vulnerability exploited Remote Code Execution attack
202157433 1 VMware vRealize Operations Manager API vulnerability exploited to steal admin credentials VMware vRealize Operations Manager API vulnerability exploited to steal admin credentials
202157426 1 Zend and laminas-http frameworks deserialization vulnerability streamName PHP object injection Zend and laminas-http frameworks deserialization vulnerability streamName PHP object injection
202157337 1 F5 iControl REST interface unauthenticated RCE vulnerability exploited ssrf attempt F5 iControl REST interface unauthenticated RCE vulnerability exploited ssrf attempt
202157298 1 F5 iControl REST interface unauthenticated remote command execution vulnerability F5 iControl REST interface unauthenticated remote command execution vulnerability
202157276 1 Microsoft SharePoint Server RCE Vulnerability exploited potential deserialization Microsoft SharePoint Server RCE Vulnerability exploited potential deserialization
202157275 1 Microsoft SharePoint Server RCE Vulnerability attachment upload deserialization Microsoft SharePoint Server RCE Vulnerability attachment upload deserialization
202157252 1 Microsoft Exchange Server vulnerability exploited arbitrary file write Microsoft Exchange Server vulnerability exploited arbitrary file write
202157246 1 Microsoft Exchange Server RCE vulnerability arbitrary file write attempt Microsoft Exchange Server RCE vulnerability arbitrary file write attempt
202157245 1 Microsoft Exchange Server vulnerability exploited arbitrary file write Microsoft Exchange Server vulnerability exploited arbitrary file write
202157243 1 Microsoft Exchange Server vulnerability exploited server side request forgery Microsoft Exchange Server vulnerability exploited server side request forgery
202157241 1 Microsoft Exchange Server vulnerability exploited server side request forgery Microsoft Exchange Server vulnerability exploited server side request forgery
202157229 1 Remote code execution vulnerability in VMware vSphere Client's vCenter Server plugin Remote code execution vulnerability in VMware vSphere Client's vCenter Server plugin
202157108 1 Microsoft SharePoint Server RCE vulnerability exploited XML external entity injection Microsoft SharePoint Server RCE vulnerability exploited XML external entity injection
202157097 1 Cisco RV Series Routers vulnerability exploited stack buffer overflow attack Cisco RV Series Routers vulnerability exploited stack buffer overflow attack
202157094 1 Cisco RV Series Routers vulnerable to command injection attacks Cisco RV Series Routers vulnerable to command injection attacks
202157092 1 Cisco RV Series Routers vulnerability exploited Remote code Execution Cisco RV Series Routers vulnerability exploited Remote code Execution
202157091 1 Cisco RV Series Routers vulnerable to command injection attacks Cisco RV Series Routers vulnerable to command injection attacks
202157088 1 Cisco RV Series Routers vulnerable to command injection attacks Cisco RV Series Routers vulnerable to command injection attacks
202157087 1 Cisco RV Series Routers vulnerable to command injection attacks Cisco RV Series Routers vulnerable to command injection attacks
202157076 1 Cisco RV Series Routers vulnerability exploited Remote code Execution Cisco RV Series Routers vulnerability exploited Remote code Execution
202157074 1 Cisco RV Series Routers vulnerability exploited Directory Traversal attack Cisco RV Series Routers vulnerability exploited Directory Traversal attack
202157072 1 Cisco RV Series Routers directory traversal attack to modify sensitive files Cisco RV Series Routers directory traversal attack to modify sensitive files
202156990 1 Apache Unomi OGNL MVEL malicious scripts remote command execution via /context.json endpoint Apache Unomi OGNL MVEL malicious scripts remote command execution via /context.json endpoint
202156989 1 Apache OpenMeetings NetTest service exploited to craft DOS attacks Apache OpenMeetings NetTest service exploited to craft DOS attacks
202156936 1 Nagios XI ajaxhelper allows malicious command injection via cmdsubsys Nagios XI ajaxhelper allows malicious command injection via cmdsubsys
202156934 1 Nagios XI ajaxhelper allows malicious command injection via cmdsubsys Nagios XI ajaxhelper allows malicious command injection via cmdsubsys
202156905 1 WordPress Easy WP SMTP plugin debug log file access attempt WordPress Easy WP SMTP plugin debug log file access attempt
202156865 1 Microsoft Sharepoint Server remote code execution Microsoft Sharepoint Server remote code execution
202156846 1 Cisco Jabber protocol vulnerable to cross-site scripting Cisco Jabber protocol vulnerable to cross-site scripting
202156845 1 Cisco Jabber protocol vulnerable to cross-site scripting Cisco Jabber protocol vulnerable to cross-site scripting
202156825 1 SolarWinds Orion API vulnerable to authentication bypass attacks SolarWinds Orion API vulnerable to authentication bypass attacks
202156824 1 Citrix SD-WAN Unauthenticated remote code execution with root privileges Citrix SD-WAN Unauthenticated remote code execution with root privileges
202156823 1 Citrix SD-WAN Unauthenticated remote code execution with root privileges Citrix SD-WAN Unauthenticated remote code execution with root privileges
202156800 1 LifeRay deserialization of untrusted data allows remote code execution via JSON web services (JSONWS) LifeRay deserialization of untrusted data allows remote code execution via JSON web services (JSONWS)
202156799 1 LifeRay deserialization of untrusted data allows remote code execution via JSON web services (JSONWS) LifeRay deserialization of untrusted data allows remote code execution via JSON web services (JSONWS)
202156626 1 rConfig vulnerable to command injection via lib/crud/search.crud.php nodeId parameter rConfig vulnerable to command injection via lib/crud/search.crud.php nodeId parameter
202156624 1 rConfig vulnerable to command injection via lib/crud/search.crud.php nodeId parameter rConfig vulnerable to command injection via lib/crud/search.crud.php nodeId parameter
202156604 1 Microsoft Dynamics NAV vulnerable to Remote Code Execution Microsoft Dynamics NAV vulnerable to Remote Code Execution
202156560 1 Microsoft SharePoint Remote Code Execution Vulnerability external ImportWeb Microsoft SharePoint Remote Code Execution Vulnerability external ImportWeb
202156558 1 Microsoft Dynamics 365 for Finance and Operations vulnerable to Remote Code Execution Microsoft Dynamics 365 for Finance and Operations vulnerable to Remote Code Execution
202156557 1 Microsoft Dynamics 365 for Finance and Operations vulnerable to Remote Code Execution Microsoft Dynamics 365 for Finance and Operations vulnerable to Remote Code Execution
202156554 1 Microsoft Exchange Remote Code Execution Vulnerability exploited deserialization attempt Microsoft Exchange Remote Code Execution Vulnerability exploited deserialization attempt
202156551 1 Ruckus vulnerable to remote command injection via /service/v1/createUser Ruckus vulnerable to remote command injection via /service/v1/createUser
202156550 1 Ruckus vRioT authentication bypass exploiting API backdoor hardcoded into validate_token.py Ruckus vRioT authentication bypass exploiting API backdoor hardcoded into validate_token.py
202156545 1 rConfig SQL injection attack via commands.inc.php searchColumn parameter rConfig SQL injection attack via commands.inc.php searchColumn parameter
202156533 1 Advantech WebAccess/NMS Directory Traversal Attack CVE-2020-10619 Advantech WebAccess/NMS Directory Traversal Attack CVE-2020-10619
202156532 1 Advantech WebAccess/NMS Directory Traversal Attack CVE-2020-10619 Advantech WebAccess/NMS Directory Traversal Attack CVE-2020-10619
202156524 1 Joomla Core Featured Article vulnerable to SQL injection attacks Joomla Core Featured Article vulnerable to SQL injection attacks
202156523 1 Joomla Core Featured Article vulnerable to SQL injection attacks Joomla Core Featured Article vulnerable to SQL injection attacks
202156434 1 IBM Spectrum Protect Plus and IBM Spectrum Scale vulnerable to remote command injection IBM Spectrum Protect Plus and IBM Spectrum Scale vulnerable to remote command injection
202156428 1 IBM Spectrum Protect Plus vulnerable to remote command injection attacks IBM Spectrum Protect Plus vulnerable to remote command injection attacks
202156427 1 IBM Spectrum Protect Plus vulnerable to remote command injection attacks IBM Spectrum Protect Plus vulnerable to remote command injection attacks
202156423 1 Cisco Security Manager xdmProxy Directory Traversal attack Cisco Security Manager xdmProxy Directory Traversal attack
202156421 1 Cisco Security Manager resultsFrame Directory Traversal attack Cisco Security Manager resultsFrame Directory Traversal attack
202156420 1 Cisco Security Manager resultsFrame Directory Traversal attack Cisco Security Manager resultsFrame Directory Traversal attack
202156419 1 Cisco Security Manager SampleFileDownloadServlet Directory Traversal attack Cisco Security Manager SampleFileDownloadServlet Directory Traversal attack
202156417 1 Cisco Security Manager SampleFileDownloadServlet Directory Traversal attack Cisco Security Manager SampleFileDownloadServlet Directory Traversal attack
202156415 1 Cisco Security Manager XmpFileDownloadServlet Directory Traversal attack Cisco Security Manager XmpFileDownloadServlet Directory Traversal attack
202156414 1 Cisco Security Manager XmpFileDownloadServlet Directory Traversal attack Cisco Security Manager XmpFileDownloadServlet Directory Traversal attack
202156408 1 Cisco Security Manager vulnerable CsJaasServiceServlet access detected Cisco Security Manager vulnerable CsJaasServiceServlet access detected
202156405 1 Cisco Security Manager XmpFileUploadServlet Directory Traversal attack Cisco Security Manager XmpFileUploadServlet Directory Traversal attack
202156404 1 Cisco Security Manager vulnerability exploited XmpFileUploadServlet arbitrary file upload Cisco Security Manager vulnerability exploited XmpFileUploadServlet arbitrary file upload
202156321 1 IBM Spectrum Protect Plus credentials reset CVE-2020-4208 IBM Spectrum Protect Plus credentials reset CVE-2020-4208
202156305 1 Microsoft SharePoint Remote Code Execution Vulnerability Microsoft SharePoint Remote Code Execution Vulnerability
202156304 1 Microsoft SharePoint Remote Code Execution Vulnerability Microsoft SharePoint Remote Code Execution Vulnerability
202156303 1 Microsoft Sharepoint machineKey information disclosure Microsoft Sharepoint machineKey information disclosure
202156201 1 Oracle WebLogic Server vulnerablity exploited command injection attack Oracle WebLogic Server vulnerability exploited command injection attack
202156200 1 Oracle WebLogic Server vulnerablity exploited command injection attack Oracle WebLogic Server vulnerability exploited command injection attack
202156188 1 Citrix Gateway plug-in vulnerability allows attacker to modify arbitrary files Citrix Gateway plug-in vulnerability allows attacker to modify arbitrary files
202156186 1 Citrix Gateway plug-in vulnerability allows attacker to modify arbitrary files Citrix Gateway plug-in vulnerability allows attacker to modify arbitrary files
202156155 1 MobileIron Core &amp; Connector vulnerable to remote code execution MobileIron Core &amp; Connector vulnerable to remote code execution
202156154 1 MobileIron Core &amp; Connector vulnerable to remote code execution MobileIron Core &amp; Connector vulnerable to remote code execution
202156134 1 Microsoft SharePoint Remote Code Execution Vulnerability Microsoft SharePoint Remote Code Execution Vulnerability
202156070 1 Microsoft SharePoint Remote Code Execution Vulnerability Microsoft SharePoint Remote Code Execution Vulnerability
202155918 1 IBM Spectrum Protect Plus vulnerable to remote code execution IBM Spectrum Protect Plus vulnerable to remote code execution
202155838 1 Wordpress Nexos theme vulnerable to SQL injection via 'side-map/?search_order= SQL Injection' Wordpress Nexos theme vulnerable to SQL injection via 'side-map/?search_order= SQL Injection'
202155836 1 Wordpress Nexos theme vulnerable to SQL injection via 'side-map/?search_order= SQL Injection' Wordpress Nexos theme vulnerable to SQL injection via 'side-map/?search_order= SQL Injection'
202155821 1 Ruby on Rails command injection vulnerability exploited Ruby on Rails command injection vulnerability exploited
202155797 1 Wordpress plugin WP Database Reset allows malicious user to reset any table to initial set-up state Wordpress plugin WP Database Reset allows malicious user to reset any table to initial set-up state
202155778 1 Wordpress File Manager plugin elFinder allows to upload and execute malicious arbitrary PHP code Wordpress File Manager plugin elFinder allows to upload and execute malicious arbitrary PHP code
202155743 1 Rockwell Automation FactoryTalk Diagnostics remote code execution Rockwell Automation FactoryTalk Diagnostics remote code execution
202154824 1 Intellian Aptus Web OS command Injection via cgi-bin/libagent.cgi Intellian Aptus Web OS command Injection via cgi-bin/libagent.cgi
202154675 1 Rockwell FactoryTalk View SE project directory Directory Traversal Attack Rockwell FactoryTalk View SE project directory Directory Traversal Attack
202154672 1 Rockwell FactoryTalk View SEA vulnerable to Remote Code Execution attacks Rockwell FactoryTalk View SEA vulnerable to Remote Code Execution attacks
202154649 1 Apache Kylin vulnerable to OS command injection via REST API Apache Kylin vulnerable to OS command injection via REST API
202154617 1 GeoVision Door Access Control devices hardcoded root password, adopting identical passwords in all devices GeoVision Door Access Control devices hardcoded root password, adopting identical passwords in all devices
202154596 1 WordPress unauthenticated privilege-escalation vulnerability in bbPress plugin WordPress unauthenticated privilege-escalation vulnerability in bbPress plugin
202154574 1 SAP NetWeaver AS LM Configuration Wizard auth bypass SAP NetWeaver AS LM Configuration Wizard auth bypass
202154573 1 SAP NetWeaver AS LM Configuration Wizard authentication bypass SAP NetWeaver AS LM Configuration Wizard authentication bypass
202154511 1 Remote Code Execution vulnerability in .NET Framework, Microsoft SharePoint, and Visual Studio Remote Code Execution vulnerability in .NET Framework, Microsoft SharePoint, and Visual Studio
202154484 1 F5 BIG-IP Traffic Management User Interface Remote Code Execution (RCE) vulnerability in undisclosed pages F5 BIG-IP Traffic Management User Interface Remote Code Execution (RCE) vulnerability in undisclosed pages
202154319 1 VMWare Cloud Director vulnerable to malicious code Injection VMWare Cloud Director vulnerable to malicious code Injection
202154273 1 Centreon tool 19.10 OS command injection attack Centreon tool 19.10 OS command injection attack
202154272 1 Centreon tool 19.10 OS command injection attack Centreon tool 19.10 OS command injection attack
202154197 1 TP-Link devices vulnerable to Command Injection attacks TP-Link devices vulnerable to Command Injection attacks
202154196 1 TP-Link devices vulnerable to Command Injection attacks TP-Link devices vulnerable to Command Injection attacks
202153885 1 Grandstream UCM6200 series vulnerable to unauthenticated SQL injection attack Grandstream UCM6200 series vulnerable to unauthenticated SQL injection attack
202153866 1 Microsoft SharePoint Remote Code Execution Vulnerability Microsoft SharePoint Remote Code Execution Vulnerability
202153592 1 DrayTek multiple products command injection attack via cgi-bin/mainfunction.cgi URI DrayTek multiple products command injection attack via cgi-bin/mainfunction.cgi URI
202153591 1 DrayTek multiple products command injection attack via cgi-bin/mainfunction.cgi URI DrayTek multiple products command injection attack via cgi-bin/mainfunction.cgi URI
202153567 1 WordPress ThemeREX Addons plugin malicious PHP code injection attempt WordPress ThemeREX Addons plugin malicious PHP code injection attempt
202153566 1 WordPress ThemeREX Addons plugin malicious PHP code injection attempt WordPress ThemeREX Addons plugin malicious PHP code injection attempt
202153558 1 Codesys V3 web server before 3.5.15.40 vulnerable to buffer overflow Codesys V3 web server before 3.5.15.40 vulnerable to buffer overflow
202153547 1 TP LINK TL-WR849N remote command execution vulnerability exploited TP LINK TL-WR849N remote command execution vulnerability exploited
202153509 1 Zyxel NAS devices command injection vulnerability exploited Zyxel NAS devices command injection vulnerability exploited
202153507 1 Zyxel NAS devices command injection vulnerability exploited Zyxel NAS devices command injection vulnerability exploited
202153506 1 Horde Groupware Webmail data import remote code execution via CSV data Horde Groupware Webmail data import remote code execution via CSV data
202153505 1 Horde Groupware Webmail data import remote code execution via CSV data Horde Groupware Webmail data import remote code execution via CSV data
202153435 1 Zoho ManageEngine Desktop Central Directory Traversal Attack Zoho ManageEngine Desktop Central Directory Traversal Attack
202153433 1 Zoho ManageEngine Desktop Central Directory Traversal Attack Zoho ManageEngine Desktop Central Directory Traversal Attack
202153347 1 Microsoft Exchange Memory Corruption Vulnerability exploited remote code execution attack Microsoft Exchange Memory Corruption Vulnerability exploited remote code execution attack
202153346 1 Microsoft Exchange Memory Corruption Vulnerability exploited remote code execution attack Microsoft Exchange Memory Corruption Vulnerability exploited remote code execution attack
202153256 1 Microsoft SQL Server Reporting Services Remote Code Execution Vulnerability Microsoft SQL Server Reporting Services Remote Code Execution Vulnerability
202153063 1 Microsoft Exchange Server Elevation of Privilege Vulnerability Microsoft Exchange Server Elevation of Privilege Vulnerability
202151833 1 vBulletin remote command injection via crafted subWidgets in ajax/render/widget_tabbedcontainer_tab_panel vBulletin remote command injection via crafted subWidgets in ajax/render/widget_tabbedcontainer_tab_panel
202151620 1 vBulletin remote command injection via crafted subWidgets in ajax/render/widget_tabbedcontainer_tab_panel vBulletin remote command injection via crafted subWidgets in ajax/render/widget_tabbedcontainer_tab_panel
202151586 1 Docker daemon API vulnerability exploited arbitrary code execution Docker daemon API vulnerability exploited arbitrary code execution
202144228 1 CVE-2021-44228 Apache Log4j2 arbitrary code execution attempt Apache Log4j2 arbitrary code execution attempt
202142670 1 Sourcecodester Engineers Online Portal vulnerability in php via dashboard_teacher.php unrestricted upload Sourcecodester Engineers Online Portal vulnerability in php via dashboard_teacher.php unrestricted upload
202142669 1 Sourcecodester Engineers Online Portal vulnerability in php via dashboard_teacher.php unrestricted upload Sourcecodester Engineers Online Portal vulnerability in php via dashboard_teacher.php unrestricted upload
202142321 1 Microsoft Exchange Server Remote Code Execution Vulnerability Microsoft Exchange Server Remote Code Execution Vulnerability
202142013 1 Path Traversal and Remote Code Execution in Apache HTTP Server 2.4.49 and 2.4.50 (incomplete fix of CVE-2021-41773) Path Traversal and Remote Code Execution in Apache HTTP Server 2.4.49 and 2.4.50 (incomplete fix of CVE-2021-41773)
202137343 1 Nagios XI path traversal vulnerability exploited in AutoDiscovery component below version 5.8.5 Nagios XI path traversal vulnerability exploited in AutoDiscovery component below version 5.8.5
202133044 1 Dahua Authentication Bypass Vulnerability Dahua Authentication Bypass Vulnerability
202132305 1 WebSVN Remote Code Execution (RCE) Vulnerability WebSVN Remote Code Execution (RCE) Vulnerability
202129592 1 Apache Struts OGNL evaluation vulnerable to remote code execution attacks Apache Struts OGNL evaluation vulnerable to remote code execution attacks
202126085 Atlassian Confluence server- Pre-Authorization Arbitrary File Read Affected versions of Atlassian Confluence Server allow remote attackers to view restricted resources via a Pre-Authorization Arbitrary File Read vulnerability. The affected versions are before version 7.4.10, and from version 7.5.0 before 7.12.3.
202125297 1 Nagios XI version xi-5.7.5 vulnerable to OS Command Injection Attacks Nagios XI version xi-5.7.5 vulnerable to OS Command Injection Attacks
202125296 1 Nagios XI version xi-5.7.5 vulnerable to OS Command Injection Attacks Nagios XI version xi-5.7.5 vulnerable to OS Command Injection Attacks
202125282 1 SaltStack Salt salt.wheel.pillar_roots.write method before 3002.5 vulnerable to directory traversal attack SaltStack Salt salt.wheel.pillar_roots.write method before 3002.5 vulnerable to directory traversal attack
202121242 1 OneDev AttachmentUploadServlet Remote Code Execution Attack OneDev AttachmentUploadServlet Remote Code Execution Attack

2020590201

2020590202 1 CVE-2020-5902 F5 Big IP Remote Code Execution in versions (15.0.0-15.1.0.3, 14.1.0-14.1.2.5, 13.1.0-13.1.3.3, 12.1.0-12.1.5.1, and 11.6.1-11.6.5.1) F5 Big IP remote code execution in versions (15.0.0-15.1.0.3, 14.1.0-14.1.2.5, 13.1.0-13.1.3.3, 12.1.0-12.1.5.1, and 11.6.1-11.6.5.1) - CVE-2020-5902
201950732 1 XML external entity vulnerability in Password Vault Web Access (PVWA) of CyberArk Enterprise Password Vault XML external entity vulnerability in Password Vault Web Access (PVWA) of CyberArk Enterprise Password Vault
201950711 1 WordPress Rencontre plugin SQL Injection attack via rencontre_widget.php WordPress Rencontre plugin SQL Injection attack via rencontre_widget.php
201950709 1 WordPress Rencontre plugin SQL Injection attack via rencontre_widget.php WordPress Rencontre plugin SQL Injection attack via rencontre_widget.php
201950708 1 WordPress Rencontre plugin allows Cross Site Scripting attack via rencontre_widget.php WordPress Rencontre plugin allows Cross Site Scripting attack via rencontre_widget.php
201950324 1 Crestron AM platform vulnerable to command injection via file_transfer.cgi Crestron AM platform vulnerable to command injection via file_transfer.cgi
201950323 1 Crestron AM platform vulnerable to command injection via file_transfer.cgi Crestron AM platform vulnerable to command injection via file_transfer.cgi
201950275 1 Remote Code Execution in Microsoft SharePoint CVE-2019-0604 Remote Code Execution in Microsoft SharePoint CVE-2019-0604
201950170 1 Atlassian Confluence Data Center and Server vulnerable to Path Traversal attacks Atlassian Confluence Data Center and Server vulnerable to Path Traversal attacks
201950168 1 Atlassian Confluence Data Center and Server vulnerable to Path Traversal attacks Atlassian Confluence Data Center and Server vulnerable to Path Traversal attacks
201949861 1 Remote Code Execution in Microsoft SharePoint CVE-2019-0604 Remote Code Execution in Microsoft SharePoint CVE-2019-0604
201949714 1 Horde Groupware Webmail Remote code execution via /Form/Type.php malicious image upload Horde Groupware Webmail Remote code execution via /Form/Type.php malicious image upload
201949647 1 Wordpress directory traversal attack modifying _wp_attached_file CVE-2019-8942 Wordpress directory traversal attack modifying _wp_attached_file CVE-2019-8942
201949646 1 Wordpress directory traversal attack modifying _wp_attached_file CVE-2019-8942 Wordpress directory traversal attack modifying _wp_attached_file CVE-2019-8942
201949645 1 Wordpress directory traversal attack modifying _wp_attached_file CVE-2019-8942 Wordpress directory traversal attack modifying _wp_attached_file CVE-2019-8942
201949537 1 elFinder before 2.1.48 has command injection vulnerability in PHP connector elFinder before 2.1.48 has command injection vulnerability in PHP connector
201949499 1 Remote code execution on the Jenkins master JVM CVE-2019-1003002 Remote code execution on the Jenkins master JVM CVE-2019-1003002
201949498 1 Remote code execution on the Jenkins master JVM CVE-2019-1003002 Remote code execution on the Jenkins master JVM CVE-2019-1003002
201948843 1 Wifi-Soft Unibox Command Injection attack via diagnostic_tools_controller Wifi-Soft Unibox Command Injection attack via diagnostic_tools_controller
201948840 1 Wifi-Soft Unibox Command Injection attack via diagnostic_tools_controller Wifi-Soft Unibox Command Injection attack via diagnostic_tools_controller
201948839 1 Wifi-Soft Unibox Command Injection attack via diagnostic_tools_controller Wifi-Soft Unibox Command Injection attack via diagnostic_tools_controller
201948837 1 ThinkPHP 5.0.23/5.1.31 vulnerable command injection attack ThinkPHP 5.0.23/5.1.31 vulnerable command injection attack
201948815 1 Kibana Console plugin vulnerable local file inclusion attack Kibana Console plugin vulnerable local file inclusion attack
201948744 1 TRENDnet TEW-673GRU start_arpping vulnerability exploited command injection attack via apply.cgi TRENDnet TEW-673GRU start_arpping vulnerability exploited command injection attack via apply.cgi
201948443 1 Nagios XI command injection attack via crafted HTTP request Nagios XI command injection attack via crafted HTTP request
201948414 1 ManageEngine Applications Manager SQL injection attack via editDisplaynames.do ManageEngine Applications Manager SQL injection attack via editDisplaynames.do
201948413 1 ManageEngine Applications Manager SQL injection attack via editDisplaynames.do ManageEngine Applications Manager SQL injection attack via editDisplaynames.do
201948273 1 Cockpit CMS media API directory traversal attack Cockpit CMS media API directory traversal attack
201948269 1 OS command injection vulenrability in Teltonika RUT9XX hotspotlogin.cgi OS command injection vulnerability in Teltonika RUT9XX hotspotlogin.cgi
201948268 1 OS command injection vulenrability in Teltonika RUT9XX hotspotlogin.cgi OS command injection vulnerability in Teltonika RUT9XX hotspotlogin.cgi
201948267 1 OS command injection vulenrability in Teltonika RUT9XX autologin.cgi OS command injection vulnerability in Teltonika RUT9XX autologin.cgi
201948266 1 OS command injection vulenrability in Teltonika RUT9XX autologin.cgi OS command injection vulnerability in Teltonika RUT9XX autologin.cgi
201948263 1 Blueimp jQuery-File-Upload Unauthenticated arbitrary file upload Blueimp jQuery-File-Upload Unauthenticated arbitrary file upload
201948256 1 Rubedo CMS Directory Traversal vulnerability in theme component Rubedo CMS Directory Traversal vulnerability in theme component
201948196 1 Joomla component Reverse Auction Factory vulnerable SQL injection attack via filter_order_Dir, cat or filter_letter parameter Joomla component Reverse Auction Factory vulnerable SQL injection attack via filter_order_Dir, cat or filter_letter parameter
201948195 1 Joomla Component Collection Factory vulnerable SQL injection attack via filter_order or filter_order_Dir parameter Joomla Component Collection Factory vulnerable SQL injection attack via filter_order or filter_order_Dir parameter
201948194 1 Joomla component AlphaIndex Dictionaries vulnerable SQL injection attack via letter parameter Joomla component AlphaIndex Dictionaries vulnerable SQL injection attack via letter parameter
201948193 1 Joomla component AlphaIndex Dictionaries vulnerable SQL injection attack via letter parameter Joomla component AlphaIndex Dictionaries vulnerable SQL injection attack via letter parameter
201948173 1 D-Link DIR-816 devices command injection attempt via /goform/form2systime.cgi D-Link DIR-816 devices command injection attempt via /goform/form2systime.cgi
201948172 1 D-Link DIR-816 devices command injection attempt via /goform/form2systime.cgi D-Link DIR-816 devices command injection attempt via /goform/form2systime.cgi
201948165 1 Joomla Component Swap Factory vulnerable SQL injection attack via filter_order_Dir or filter_order parameter Joomla Component Swap Factory vulnerable SQL injection attack via filter_order_Dir or filter_order parameter
201948161 1 Joomla component Article Factory Manager vulnerable SQL injection attack via via start_date, m_start_date, or m_end_date parameter Joomla component Article Factory Manager vulnerable SQL injection attack via via start_date, m_start_date, or m_end_date parameter
201948143 1 D-Link DIR-816 devices command injection attempt via /goform/Diagnosis D-Link DIR-816 devices command injection attempt via /goform/Diagnosis
201948141 1 D-Link DIR-816 devices command injection attempt via /goform/Diagnosis D-Link DIR-816 devices command injection attempt via /goform/Diagnosis
201948126 1 Joomla component Timetable Schedule 3.6.8 vulnerable SQL injection attack via eid parameter Joomla component Timetable Schedule 3.6.8 vulnerable SQL injection attack via eid parameter
201948098 1 D-Link DIR-816 devices command injection attempt via /goform/sylogapply syslogIp D-Link DIR-816 devices command injection attempt via /goform/sylogapply syslogIp
201948097 1 D-Link DIR-816 devices command injection attempt via /goform/sylogapply syslogIp D-Link DIR-816 devices command injection attempt via /goform/sylogapply syslogIp
201948071 1 WordPress Wechat Broadcast plugin Directory Traversal via Image.php url parameter WordPress Wechat Broadcast plugin Directory Traversal via Image.php url parameter
201948070 1 WordPress Wechat Broadcast plugin Directory Traversal via Image.php url parameter WordPress Wechat Broadcast plugin Directory Traversal via Image.php url parameter
201948061 1 pfSense status_interfaces.php command injection attack pfSense status_interfaces.php command injection attack
201948004 1 Navigate CMS login.php SQL injection attack to bypass auth via navigate-user cookie Navigate CMS login.php SQL injection attack to bypass auth via navigate-user cookie
201947864 1 Command Injection attack via Opsview Monitor Web Management Console test_rancid_connection Command Injection attack via Opsview Monitor Web Management Console test_rancid_connection
201947863 1 Command Injection attack via Opsview Monitor Web Management Console test_rancid_connection Command Injection attack via Opsview Monitor Web Management Console test_rancid_connection
201947861 1 Opsview Web Management Console testnotification command injection attack Opsview Web Management Console testnotification command injection attack
201947859 1 Joomla CW Tags vulnerable SQL injection attack via searchtext array parameter Joomla CW Tags vulnerable SQL injection attack via searchtext array parameter
201947858 1 Joomla CW Tags vulnerable SQL injection attack via searchtext array parameter Joomla CW Tags vulnerable SQL injection attack via searchtext array parameter
201947818 1 Command Injection vulnerability in SoftNAS StorageCenter snserv.php Command Injection vulnerability in SoftNAS StorageCenter snserv.php
201947817 1 Command Injection vulnerability in SoftNAS StorageCenter snserv.php Command Injection vulnerability in SoftNAS StorageCenter snserv.php
201947800 1 Trend Micro Email Encryption Gateway SQL injection attack via search script Trend Micro Email Encryption Gateway SQL injection attack via search script
201947799 1 Trend Micro Email Encryption Gateway SQL injection attack via search script Trend Micro Email Encryption Gateway SQL injection attack via search script
201947797 1 SQL injection attempt exploiting vulnerability in Trend Micro Email Encryption Gateway SQL injection attempt exploiting vulnerability in Trend Micro Email Encryption Gateway
201947796 1 SQL injection attempt exploiting vulnerability in Trend Micro Email Encryption Gateway SQL injection attempt exploiting vulnerability in Trend Micro Email Encryption Gateway
201947795 1 SQL injection attempt exploiting vulnerability in Trend Micro Email Encryption Gateway SQL injection attempt exploiting vulnerability in Trend Micro Email Encryption Gateway
201947794 1 SQL injection attempt exploiting vulnerability in Trend Micro Email Encryption Gateway SQL injection attempt exploiting vulnerability in Trend Micro Email Encryption Gateway
201947771 1 ClipBucket SQL injection attack via actions/vote_channel.php or ajax/commonAjax.php ClipBucket SQL injection attack via actions/vote_channel.php or ajax/commonAjax.php
201947768 1 Malicious file upload attempt to ClipBucket beats_uploader or photo_uploader or edit_account.php Malicious file upload attempt to ClipBucket beats_uploader or photo_uploader or edit_account.php
201947767 1 ClipBucket file_uploader vulnerable to command injection ClipBucket file_uploader vulnerable to command injection
201947672 1 Command Injection attack exploiting vulnerability in TerraMaster TOS logtable.php Command Injection attack exploiting vulnerability in TerraMaster TOS logtable.php
201947655 1 Joomla SQL injection vulnerability in postinstall message Joomla SQL injection vulnerability in postinstall message
201947649 1 Apache Struts vulnerable to Remote Code Execution Apache Struts vulnerable to Remote Code Execution
201947583 1 GitStack unauthenticated REST API potential add user GitStack unauthenticated REST API potential add user
201947582 1 GitStack unauthenticated REST API potential repository modification GitStack unauthenticated REST API potential repository modification
201947581 1 GitStack unauthenticated REST API add user via username and password fields to rest/user/ 'URI' GitStack unauthenticated REST API add user via username and password fields to rest/user/ 'URI'
201947580 1 Joomla Aist component vulnerable SQL injection attack via id parameter Joomla Aist component vulnerable SQL injection attack via id parameter
201947579 1 Joomla Aist component vulnerable SQL injection attack via id parameter Joomla Aist component vulnerable SQL injection attack via id parameter
201947577 1 Cobub Razor SQL injection attack via channel_name Cobub Razor SQL injection attack via channel_name
201947576 1 Cobub Razor SQL injection attack via channel_name Cobub Razor SQL injection attack via channel_name
201947545 1 MicroFocus Secure Messaging Gateway command injection attack MicroFocus Secure Messaging Gateway command injection attack
201947544 1 MicroFocus Secure Messaging Gateway vulnerable enginelist.php SQL injection attack MicroFocus Secure Messaging Gateway vulnerable enginelist.php SQL injection attack
201947543 1 MicroFocus Secure Messaging Gateway vulnerable enginelist.php SQL injection attack MicroFocus Secure Messaging Gateway vulnerable enginelist.php SQL injection attack
201947514 1 Authentication bypass attempt exploiting vulnerability in Quest NetVault Backup Server via checksession parameter Authentication bypass attempt exploiting vulnerability in Quest NetVault Backup Server via checksession parameter
201947507 1 Sitecore.NET Log Viewer application vulnerable to directory traversal attacks Sitecore.NET Log Viewer application vulnerable to directory traversal attacks
201947506 1 Sitecore.NET 'Log Viewer' application vulnerable to directory traversal attacks Sitecore.NET 'Log Viewer' application vulnerable to directory traversal attacks
201947502 1 Joomla ProjectLog component vulnerable SQL injection attack via search parameter Joomla ProjectLog component vulnerable SQL injection attack via search parameter
201947501 1 Joomla ProjectLog component vulnerable SQL injection attack via search parameter Joomla ProjectLog component vulnerable SQL injection attack via search parameter
201947498 1 Joomla SQL injection attack via title_search, tag_search, name_search, description_search, or filter_order parameter Joomla SQL injection attack via title_search, tag_search, name_search, description_search, or filter_order parameter
201947497 1 Joomla SQL injection attack via title_search, tag_search, name_search, description_search, or filter_order parameter. Joomla SQL injection attack via title_search, tag_search, name_search, description_search, or filter_order parameter.
201947423 1 QNAP QCenter API command injection attack via date_config QNAP QCenter API command injection attack via date_config
201947393 1 QNAP QCenter API command injection attack via date_config QNAP QCenter API command injection attack via date_config
201947391 1 Command injection vulnerability in networking of QNAP Q center Virtual Appliance Command injection vulnerability in networking of QNAP Q center Virtual Appliance
201947389 1 Oracle WebLogic Server vulnerability exploited arbitrary JSP file upload Oracle WebLogic Server vulnerability exploited arbitrary JSP file upload
201947387 1 Oracle WebLogic Server potential unauthenticated reconnaissance attempt Oracle WebLogic Server potential unauthenticated reconnaissance attempt
201947386 1 Oracle WebLogic Server vulnerability exploitaion allows unauthenticated attacker to compromise weblogic server Oracle WebLogic Server vulnerability exploitaion allows unauthenticated attacker to compromise weblogic server
201947349 1 QNAP QCenter API command injection attack via change password QNAP QCenter API command injection attack via change password
201947348 1 QNAP QCenter API command injection attack via change password QNAP QCenter API command injection attack via change password
201947041 1 Quest KACE Systems Management Appliance vulnerable to command injection attack via download_agent_installer.php Quest KACE Systems Management Appliance vulnerable to command injection attack via download_agent_installer.php
201946997 1 Buffer overflow in XiongMai NVR login.htm Buffer overflow in XiongMai NVR login.htm
201946921 1 Quest DR Series Disk Backup vulnerable allows command injection attacks Quest DR Series Disk Backup vulnerable allows command injection attacks
201946886 1 Quest KACE Systems Management Appliance ajax_email_connection_test.php command injection attack Quest KACE Systems Management Appliance ajax_email_connection_test.php command injection attack
201946852 1 IBM QRadar SIEM forensicsanalysisServlet command injection attack IBM QRadar SIEM forensicsanalysisServlet command injection attack
201946851 1 IBM QRadar SIEM forensicsanalysisServlet command injection attack IBM QRadar SIEM forensicsanalysisServlet command injection attack
201946850 1 IBM QRadar SIEM forensicsanalysisServlet Authentication bypass attack IBM QRadar SIEM forensicsanalysisServlet Authentication bypass attack
201946829 1 D-Link DIR-620 devices command injection attack via index.cgi D-Link DIR-620 devices command injection attack via index.cgi
201946828 1 D-Link DIR-620 devices command injection attack via index.cgi D-Link DIR-620 devices command injection attack via index.cgi
201946823 1 Spring Security OAuth Remote Code Execution attack Spring Security OAuth Remote Code Execution attack
201946779 1 Nagios XI database settings modification Nagios XI database settings modification
201946777 1 Nagios XI command injection attack Nagios XI command injection attack
201946775 1 Nagios XI command injection attack Nagios XI command injection attack
201946774 1 Nagios XI SQL injection attack via selInfoKey1 parameter Nagios XI SQL injection attack via selInfoKey1 parameter
201946773 1 Nagios XI SQL injection attack via selInfoKey1 parameter Nagios XI SQL injection attack via selInfoKey1 parameter
201946666 1 Digital Guardian Management Console arbitary file upload allows remote code execution Digital Guardian Management Console arbitary file upload allows remote code execution
201946665 1 Digital Guardian Management Console arbitary file upload allows remote code execution Digital Guardian Management Console arbitary file upload allows remote code execution
201946627 1 GPON Router Command Injection attack via dest_host parameter GPON Router Command Injection attack via dest_host parameter
201946626 1 GPON Router Command Injection attack via dest_host parameter GPON Router Command Injection attack via dest_host parameter
201946625 1 GPON Router Command Injection attack via dest_host parameter GPON Router Command Injection attack via dest_host parameter
201946624 1 GPON Router Command Injection attack via dest_host parameter GPON Router Command Injection attack via dest_host parameter
201946516 1 Belkin N750 F9K1103 wireless router command injection attack via proxy.cgi Belkin N750 F9K1103 wireless router command injection attack via proxy.cgi
201946514 1 Belkin N750 F9K1103 wireless router command injection attack via proxy.cgi Belkin N750 F9K1103 wireless router command injection attack via proxy.cgi
201946512 1 Belkin N750 F9K1103 wireless router command injection attack via twonky_command.cgi Belkin N750 F9K1103 wireless router command injection attack via twonky_command.cgi
201946510 1 Belkin N750 F9K1103 wireless router command injection attack via twonky_command.cgi Belkin N750 F9K1103 wireless router command injection attack via twonky_command.cgi
201946509 1 Unitrends Enterprise Backup vulnerability exploited command injection attack via /api/hosts parameters using backquotes Unitrends Enterprise Backup vulnerability exploited command injection attack via /api/hosts parameters using backquotes
201946451 1 Drupal remote code execution attack exploiting multiple attack vectors on its website Drupal remote code execution attack exploiting multiple attack vectors on its website
201946338 1 Joomla Saxum Picker vulnerable SQL injection attack via publicid parameter Joomla Saxum Picker vulnerable SQL injection attack via publicid parameter
201946337 1 Joomla Saxum Picker vulnerable SQL injection attack via publicid parameter Joomla Saxum Picker vulnerable SQL injection attack via publicid parameter
201946334 1 Joomla DT Register vulnerable SQL injection attack via a task=edit&amp;id= request Joomla DT Register vulnerable SQL injection attack via a task=edit&amp;id= request
201946333 1 Joomla DT Register vulnerable SQL injection attack via a task=edit&amp;id= request Joomla DT Register vulnerable SQL injection attack via a task=edit&amp;id= request
201946316 1 Drupal 8 allows remote attackers to execute arbitrary code Drupal 8 allows remote attackers to execute arbitrary code
201946303 1 Antsle antman Authentication bypass via invalid characters in username and password parameters Antsle antman Authentication bypass via invalid characters in username and password parameters
201946088 1 Joomla JEXTN Reverse Auction extension vulnerable SQL injection attack via view=products&amp;uid= '' Joomla JEXTN Reverse Auction extension vulnerable SQL injection attack via view=products&amp;uid= ''
201946087 1 Joomla JEXTN Reverse Auction extension vulnerable SQL injection attack via view=products&amp;uid= '' Joomla JEXTN Reverse Auction extension vulnerable SQL injection attack via view=products&amp;uid= ''
201946063 1 Joomla JE PayperVideo extension vulnerable SQL injection attack via usr_plan parameter Joomla JE PayperVideo extension vulnerable SQL injection attack via usr_plan parameter
201946062 1 Joomla JE PayperVideo extension vulnerable SQL injection attack via usr_plan parameter Joomla JE PayperVideo extension vulnerable SQL injection attack via usr_plan parameter
201946042 1 Joomla Component JMS Music 1.1.1 vulnerable SQL injection attack via search with keyword, artist, or username parameter Joomla Component JMS Music 1.1.1 vulnerable SQL injection attack via search with keyword, artist, or username parameter
201946041 1 Joomla Component JMS Music 1.1.1 vulnerable SQL injection attack via search with keyword, artist, or username parameter Joomla Component JMS Music 1.1.1 vulnerable SQL injection attack via search with keyword, artist, or username parameter
201946030 1 Joomla jextn-classifieds vulnerable SQL injection attack view=boutique&amp;sid= '' Joomla jextn-classifieds vulnerable SQL injection attack view=boutique&amp;sid= ''
201946029 1 Joomla jextn-classifieds vulnerable SQL injection attack view=boutique&amp;sid= '' Joomla jextn-classifieds vulnerable SQL injection attack view=boutique&amp;sid= ''
201946028 1 Joomla JE PayperVideo extension vulnerable SQL injection attack via usr_plan parameter Joomla JE PayperVideo extension vulnerable SQL injection attack via usr_plan parameter
201946025 1 SQL Injection exists in Event Manager 1.0 via event.php id parameter or page.php slug parameter SQL Injection exists in Event Manager 1.0 via event.php id parameter or page.php slug parameter
201946024 1 SQL Injection exists in Event Manager 1.0 via event.php id parameter or page.php slug parameter SQL Injection exists in Event Manager 1.0 via event.php id parameter or page.php slug parameter
201945984 1 Joomla component Jimtawl 2.2.5 vulnerable arbitrary PHP file upload via view=upload&amp;task=upload&amp;pop=true&amp;tmpl=component Joomla component Jimtawl 2.2.5 vulnerable arbitrary PHP file upload via view=upload&amp;task=upload&amp;pop=true&amp;tmpl=component
201945913 1 Zoho ManageEngine Applications Manager public endpoint testCredential.do vulnerable to Remote Code Execution Zoho ManageEngine Applications Manager public endpoint testCredential.do vulnerable to Remote Code Execution
201945911 1 Zoho ManageEngine Applications Manager public endpoint testCredential.do vulnerable to Remote Code Execution Zoho ManageEngine Applications Manager public endpoint testCredential.do testCredential.do vulnerable to Remote Code Execution
201945526 1 NVRAM configuration modification attempt via AsusWRT vpnupload.cgi NVRAM configuration modification attempt via AsusWRT vpnupload.cgi
201945493 1 Seagate Personal Cloud vulnerable to command injection via getLogs.psp uploadtelemetry.psp functions Seagate Personal Cloud vulnerable to command injection via getLogs.psp uploadtelemetry.psp functions
201939743 1 SonicWall GMS command injection attack via parameters pass to XML-RPC calls SonicWall GMS command injection attack via parameters pass to XML-RPC calls

2019272501

2019272502

2019272503

2019272504 1 CVE-2019-2725 and CVE-2019-2729 Oracle WebLogic Remote Code Execution in versions (10.3.6.0.0, 12.1.3.0.0, 12.2.1.3.0) CVE-2019-2725 and CVE-2019-2729 Oracle WebLogic Remote Code Execution in versions (10.3.6.0.0, 12.1.3.0.0, 12.2.1.3.0)
201919781 1 CVE-2019-19781 Citrix Application Delivery Controller(ADC) Path Traversal Vulnerability Citrix ADC NSC_USER directory traversal attempt. Versions (10.5, 11.1, 12.0, 12.1, and 13.0) - CVE-2019-19781
2018100 1 CVE-2018-6389 WordPress Parameter Resource Consumption Remote DoS WordPress Parameter Resource Consumption Remote DoS on jquery-ui-core
2017100 1 Apache Struts 2 Multipart parser CVE-2017-5638 Remote Code Execution Vulnerability Prevention Detects Apache Jakarta CVE-2017-5638 Remote Code Execution Vulnerability payload
