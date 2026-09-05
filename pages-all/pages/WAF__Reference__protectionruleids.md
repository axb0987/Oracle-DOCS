# Supported Protection Rules
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Reference/protectionruleids.htm
- Fetched: 2026-09-05 03:11 CDT

# Supported Protection Rules

Learn about the purpose of each protection rule type.

The Oracle Cloud Infrastructure WAF service supports many protection rule types. The following list provides a brief explanation of the purpose of each protection rule type.

## Protection Rules

Rule ID/Key

Name

Description
90001 Filter Profanity Detects profanity used in request headers and body.
90002 United States Social Security Number Leakage Detects leakage of US SSN in C3 body and headers.
90004 Executable file upload attempt Detects attempts to upload executable files through input forms.
90005 Brazilian Social Security Number (CPF) Leakage Detects leakage of Brazilian CPF in response body and headers.
90006 Credit card leakage in request: GSA SmartPay Detects GSA SmartPay credit card numbers in user input.
90007 Credit card leakage in request: MasterCard Detects MasterCard credit card numbers in user input.
90008 Credit card leakage in request: Visa Detects Visa credit card numbers in user input.
90009 Credit card leakage in request: American Express Detects American Express credit card numbers in user input.
90010 Credit card leakage in request: Diners Club Detects Diners Club credit card numbers in user input.
90011 Credit card leakage in request: enRoute Detects enRoute credit card numbers in user input.
90012 Credit card leakage in request: Discover Detects Discover credit card numbers in user input.
90013 Credit card leakage in request: JCB Detects JCB credit card numbers in user input.
90014 Credit card leakage in response: GSA SmartPay Detects GSA SmartPay credit card numbers sent from site to user.
90015 Credit card leakage in response: MasterCard Detects MasterCard credit card numbers sent from site to user.
90016 Credit card leakage in response: Visa Detects Visa credit card numbers sent from site to user.
90017 Credit card leakage in response: American Express Detects American Express credit card numbers sent from site to user.
90018 Credit card leakage in response: Diners Club Detects Diners Club credit card numbers sent from site to user.
90019 Credit card leakage in response: enRoute Detects enRoute credit card numbers sent from site to user.
90020 Credit card leakage in response: Discover Detects Discover credit card numbers sent from site to user.
90021 Credit card leakage in response: JCB Detects JCB credit card numbers sent from site to user.
90022 Credit card Track 1 data leakage Detects credit card track 1 data in the response body.
90023 Credit card Track 2 data leakage Detects credit card track 2 data in the response body.
90024 Credit card PAN leakage Detects credit card primary account number in the response body.
90025 visitorTracker_isMob malware detection Detects and/or blocks visitorTracker_isMob malware.
120123 Joomla! Core CVE-2015-8562 Remote Code Execution Vulnerability Prevention Detects Joomla! Core CVE-2015-8562 Remote Code Execution Vulnerability payload.
120133 Canadian Social Identification Number (SIN) leakage Detects leakage of Canadian SIN in response body and headers.
900032 HTTP Parameter Polution (HPP) detection Rule Detects requests that have multiple arguments with the same name indicative of HPP attack.
911100 Restrict HTTP Request Methods Allows only request methods specified by the configurable "Allowed http methods" parameter.
920021, 920022, 920023 Credit card PAN leakage Detects credit card primary account number in the response body.
920100 Invalid HTTP Request Line Invalid HTTP Request Line.
920120 File Name Validation Detects multipart/form-data file name evasion attempts.
920160 Content-Length Header Validation Detects if content-length HTTP header is not numeric.
920170 GET/HEAD Requests Validation Detects if GET/HEAD requests contain request body by checking for content-length header, since it is not a common practice.
920171 GET/HEAD Requests Validation Detects if GET/HEAD requests contain request body by checking for Transfer-Encoding header since it is not a common practice.
920180 Content-Length Header Validation Detects if content-length and Transfer-Encoding headers are provided with every POST request.
920190 Range Header Validation This rule inspects the Range request header to see if it starts with 0.
920200, 920201 Range Header Validation Detects range header inconsistencies and invalid formatting.
920220, 920240 Check URL encodings There are two different chained rules. We need to separate them as we are inspecting two different variables - REQUEST_URI and REQUEST_BODY. For REQUEST_BODY, we only want to run the @validateUrlEncoding operator if the content-type is application/x-www-form-urlencoding.
920230 Detect multiple url encoding Detection of multiple url encodings.
920260 Disallow use of full-width unicode as decoding evasions may be possible. This rule looks for full-width encoding by looking for %u followed by 2 'f' characters and then 2 hex characters. It is a vulnerability that affected IIS circa 2007.
920270 Restrict type of characters sent This rule uses the @validateByteRange operator to restrict the request payloads.
920280 Missing/Empty Host Header Missing/Empty Host Header.
920300 Missing Accept Header Detection of missing accept header.
920310, 920311 Empty Accept Header Checks if an Accept header exists, but has an empty value. Also detects an empty Accept header if there is no user agent.
920320 Missing User-Agent header Detection of missing user-agent header.
920330 Empty User-Agent Header Detects empty request user-agent header.
920350 Invalid HTTP Request Line Invalid HTTP Request Line.
920360 Limit length of argument names Detects HTTP requests argument name length exceeding the configurable "Max length of argument name" value.
920370 Limit argument value length Detects HTTP requests arugment values exceeding the configurable "Max argument value length" parameter.
920380 Number of Arguments Limits Detects HTTP requests with number of arguments exceeding the configurable "Max amount of arguments" value.
920390 Limit arguments total length Detects HTTP requests arugment length exceeding the configurable "Max argument length" parameter.
920400 Limit file size Limits the size of a file by checking Content-Length Header for a varible max_file_size.
920410 Limit combined file size Limits the size of combined files by checking Content-Length Header for a varible combined_file_sizes.
920420 Check content-type header against allow list Restrict Content Types by checking the variable allowed_request_content_type.
920430 Request protocol version restriction Restrict protocol versions by using the variable allowed_http_versions.
920440 Restriction by file extension Restrict file extensions using the variable restricted_extensions.
920450 Restricted HTTP headers The use of certain headers is restricted. They are listed in the variable restricted_headers.
920470 Restrict Content Type Restrict Content Types by checking the content-type header.
920480 Charset restriction in content-type Restrict charset in Content Types by checking the variable allowed_request_content_type_charset.
920500 Detect backup or working files Detect backup or working files.
921110 HTTP Request Smuggling Looks for CR/LF characters in combination with HTTP / WEBDAV.
921120, 921130 HTTP Response Splitting Looks for CR/LF characters, may cause problems if the data is returned in a respones header and may be interpreted by an intermediary proxy server and treated as two separate responses.
921140 HTTP Header Injection These rules look for Carriage Return (CR) %0d and Linefeed (LF) %0a characters, on their own or in combination with header field names. These characters may cause problems if the data is returned in a respones header and interpreted by the client.
921150, 921160 Argument Newline Detection Detect newlines in argument names.
921151 Newline in GET Args Detect newlines in GET arguments which may point to HTTP header injection attacks.
921190 HTTP Splitting This rule detect \n or \r in the REQUEST FILENAME.
930100 Directory Traversal Attacks Directory Traversal Attacks, Encoded, /../ and Payloads.
930110 Directory Path Traversal Attacks Directory Path Traversal Attack /../ and Payloads.
930120 OS File Access Attempt OS File Access Attempt, Cookies and Arguments.
930130 Restricted File Access Restricted File Access. Detects attempts to retrieve application source code, metadata, credentials and version control history possibly reachable in a web root.
931100 Remote File Inclusion (RFI) Attempt: RFI Attack URL Parameter using IP Address Remote File Inclusion (RFI). These rules look for common types of Remote File Inclusion (RFI) attack methods. Possible RFI Attack: URL Parameter using IP Address.
931110 Remote File Inclusion (RFI) Attempt: RFI Attack: Common RFI Vulnerable Parameter Name used w/URL Payload Remote File Inclusion (RFI). These rules look for common types of Remote File Inclusion (RFI) attack methods. Possible RFI Attack: Common RFI Vulnerable Parameter Name used w/URL Payload.
931120 Remote File Inclusion (RFI) Attempt: RFI Attack: URL Payload Used w/Trailing Question Mark Character (?) Remote File Inclusion (RFI). These rules look for common types of Remote File Inclusion (RFI) attack methods. Possible RFI Attack: URL Payload Used w/Trailing Question Mark Character (?)
931130 Remote File Inclusion (RFI) Attempt: RFI Attack: Off-Domain Reference/Link Remote File Inclusion (RFI). These rules look for common types of Remote File Inclusion (RFI) attack methods. Possible RFI Attack: Off-Domain Reference/Link
932100 Remote Command Execution (RCE) Attempt: RCE Unix Command Injection Remote Command Execution (RCE) Attempt: RCE Unix Command Injection the vulnerability exists when an application executes a shell command without proper input escaping/validation.
932105 Remote Command Execution (RCE) Attempt: RCE Unix Command Injection Remote Command Execution (RCE) Attempt: RCE Unix Command Injection the vulnerability exists when an application executes a shell command without proper input escaping/validation.
932106 Unix Command Injection Detects several Unix command injections (and its attempts of obfuscation and evasion). The vulnerability exists when an application executes a shell command without proper input escaping/validation.
932110 Remote Command Execution (RCE) Attempt: RCE Windows command injection Remote Command Execution (RCE) Attempt: RCE This rule Detects Windows shell command injections. If you are not running Windows, it is safe to disable this rule.
932115 Remote Command Execution (RCE) Attempt: RCE Windows command injection Remote Command Execution (RCE) Attempt: RCE This rule Detects Windows shell command injections. If you are not running Windows, it is safe to disable this rule.
932120 Remote Command Execution (RCE) Attempt: RCE Windows PowerShell, cmdlets and options Remote Command Execution (RCE) Attempt: RCE Detect some common PowerShell commands, cmdlets and options.These commands should be relatively uncommon in normal text, but potentially useful for code injection. If you are not running Windows, it is safe to disable this rule.
932130 Remote Command Execution (RCE) Attempt: Unix shell expressions Remote Command Execution (RCE) Attempt: RCE Unix Shell Expression Found. Detects the following patterns which are common in Unix shell scripts and oneliners: Command substitution, Parameter expansion, Process substitution, Arithmetic expansion
932140 Remote Command Execution (RCE) Attempt: RCE Windows FOR, IF commands Remote Command Execution (RCE) Attempt: RCE Windows FOR/IF Command Found. This rule Detects Windows command shell FOR and IF commands. If you are not running Windows, it is safe to disable this rule.
932150 Remote Command Execution (RCE) Attempt: RCE Unix direct remote command execution Remote Command Execution (RCE) Attempt: RCE Direct Unix Command execution Found.This case is different from command injection (rule 932100), where a command string is appended (injected) to a regular parameter, and then passed to a shell unescaped.
932160 Remote Command Execution (RCE) Attempt: RCE Unix shell snippets Remote Command Execution (RCE) Attempt: RCE Unix Shell Code Found. Detect some common sequences found in shell commands and scripts.
932170 Remote Command Execution (RCE) Attempt: Shellshock vulnerability (CVE-2014-6271 and CVE-2014-7169) Remote Command Execution (RCE) Attempt: RCE Detect exploitation of "Shellshock" GNU Bash RCE vulnerability. Based on ModSecurity rules created by Red Hat.
932171 Remote Command Execution (RCE) Attempt: Shellshock vulnerability (CVE-2014-6271 and CVE-2014-7169) Remote Command Execution (RCE) Attempt: RCE Detect exploitation of "Shellshock" GNU Bash RCE vulnerability. Based on ModSecurity rules created by Red Hat.
932180 Restricted File Upload Detects attempts to upload a file with a forbidden filename. Many application contain Unrestricted File Upload vulnerabilities. These might be abused to upload configuration files or other files that affect the behavior of the web server, possibly causing remote code execution.
932190 Remote Command Execution - OS File Access Attempt A Remote Command Execution (RCE) could be exploited bypassing rule 93012032 (OS File Access Attempt) by using wildcard characters. Keep in mind that this rule could lead to many false positives.
933100 PHP Injection Attacks: PHP Open Tag Found PHP Injection Attacks: Detects PHP open tags "&lt;?" and "&lt;?php". Also Detects "[php]", "[/php]" and "[\php]" tags used by some applications to indicate PHP dynamic content.
933110 PHP Injection Attacks: PHP Script Uploads PHP Injection Attacks: Block file uploads with PHP extensions (.php, .php5, .phtml and so on), also block files with just dot (.) characters after the extension. Many application contain Unrestricted File Upload vulnerabilities. Attackers may use such a vulnerability to achieve remote code execution by uploading a .php file.Some AJAX uploaders use the nonstandard request headers X-Filename, X_Filename, or X-File-Name to transmit the file name to the server; scan these request headers as well as multipart/form-data file names.
933111 PHP Injection Attacks: PHP Script Uploads: Superfluous extension PHP Injection Attacks: PHP Script Uploads - Superfluous extension. Block file uploads with PHP extensions (.php, .php5, .phtml and so on) anywhere in the name, followed by a dot.
933120 PHP Injection Attacks: PHP Configuration Directives PHP Injection Attacks: Configuration Directive Found
933130 PHP Injection Attacks: PHP Variables PHP Injection Attacks: Variables Found
933131 PHP Injection Attacks: PHP Variables - Common Variable Indexes PHP Injection Attacks: Common Variable Indexes
933140 PHP Injection Attacks: PHP I/O Streams PHP Injection Attacks: Variables Found. The "php://" syntax can be used to refer to various objects, such as local files (for LFI), remote urls (for RFI), or standard input/request body. Its occurrence indicates a possible attempt to either inject PHP code or exploit a file inclusion vulnerability in a PHP web app.
933150 PHP Injection Attacks: High-Risk PHP Function Names PHP Injection Attacks: High-Risk PHP Function Names, Approx. 40 words highly common to PHP injection payloads and extremely rare in natural language or other contexts. Examples: 'base64_decode', 'file_get_contents'.
933151 PHP Injection Attacks: Medium-Risk PHP Function Names PHP Injection Attacks: Medium-Risk PHP Function Names, Medium-Risk PHP injection payloads and extremely rare in natural language or other contexts.
933160 PHP Injection Attacks: High-Risk PHP Function Calls PHP Injection Attacks: High-Risk PHP Function Calls, some PHP function names have a certain risk of false positives, due to short names, full or partial overlap with common natural language terms, uses in other contexts, and so on. Some examples are 'eval', 'exec', and 'system'.
933161 PHP Injection Attacks: PHP Functions - Low-Value PHP Function Calls PHP Injection Attacks: PHP Functions - Low-Value PHP Function Calls. Most of these function names are likely to cause false positives in natural text or common parameter values, such as 'abs', 'copy', 'date', 'key', 'max', 'min'. Therefore, these function names are not to be used if high false positives are expected.
933170 PHP Injection Attacks: PHP Object Injection PHP Injection Attacks: PHP Object Injection, is an application level vulnerability that could allow an attacker to perform different kinds of malicious attacks, such as Code Injection, SQL Injection, Path Traversal and Application Denial of Service, depending on the context. The vulnerability occurs when user-supplied input is not properly sanitized before being passed to the unserialize() PHP function.
933180 PHP Injection Attacks: PHP Functions - Variable Function Calls PHP Injection Attacks: PHP Functions - Variable Function Calls, PHP 'variable functions' provide an alternate syntax for calling PHP functions. An attacker may use variable function syntax to evade detection of function names during exploitation of a remote code execution vulnerability.
933190 PHP Injection Attacks: PHP Closing Tag Found PHP Injection Attacks: PHP Closing Tag Found.
933200 PHP Injection Attacks: PHP Wrappers PHP Injection Attacks: PHP Wrappers, PHP comes with many built-in wrappers for various URL-style protocols for use with the filesystem functions such as fopen(), copy(), file_exists() and filesize(). Abusing of PHP wrappers like phar://, zlib://, glob://, rar://, zip://, and so on... could lead to LFI and expect:// to RCE.
933210 PHP Injection Attacks: PHP Functions - Variable Function Prevent Bypass PHP Injection Attacks: PHP Functions - Variable Function Calls. This rule blocks bypass filter payloads.
934100 Insecure unserialization Remote Code Execution Detects generic Remote Code Executions on Insecure unserialiazation. Detects CVE-2017-5941
941100 Cross-Site Scripting (XSS) Attempt: Libinjection - XSS Detection Cross-Site Scripting (XSS) Attempt: Detects XSS Libinjection
941101 Cross-Site Scripting (XSS) Attempt: SS Attack Detected via libinjection Cross-Site Scripting (XSS) Attempt: SS Attack Detected via libinjection
941110 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 1 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 1. Script tag based XSS vectors, e.g., &lt;script&gt; alert(1)&lt;/script&gt;
941120 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 2 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 2. XSS vectors making use of event handlers like onerror, onload and so on, e.g., &lt;body onload="alert(1)"&gt;
941130 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 3 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 3. XSS vectors making use of Attribute Vectors
941140 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 4 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 4. XSS vectors making use of javascript URI and tags, e.g., &lt;p style="background:url(javascript:alert(1))"&gt;
941150 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 5 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 5. HTML attribues - src, style and href
941160 Cross-Site Scripting (XSS) Attempt: NoScript XSS Filters Cross-Site Scripting (XSS) Attempt: NoScript XSS Filters, NoScript InjectionChecker - HTML injection
941170 Cross-Site Scripting (XSS) Attempt: NoScript XSS Filters Cross-Site Scripting (XSS) Attempt: NoScript XSS Filters, NoScript InjectionChecker - Attributes injection
941180 Cross-Site Scripting (XSS) Attempt: Blacklist Keywords from Node-Validator Cross-Site Scripting (XSS) Attempt: Blacklist Keywords from Node-Validator
941190 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941200 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941210 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941220 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941230 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941240 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941250 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941260 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941270 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941280 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941290 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941300 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941310 Cross-Site Scripting (XSS) Attempt: US-ASCII encoding bypass listed on XSS filter evasion Cross-Site Scripting (XSS) Attempt: US-ASCII encoding bypass listed on XSS filter evasion.
941320 Cross-Site Scripting (XSS) Attempt: HTML Tag Handler Cross-Site Scripting (XSS) Attempt: HTML Tag Handler
941330 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941340 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
941350 Cross-Site Scripting (XSS) Attempt: UTF-7 encoding XSS filter evasion for IE Cross-Site Scripting (XSS) Attempt: UTF-7 encoding XSS filter evasion for IE.
941360 Cross-Site Scripting (XSS) Attempt: Defend against JSFuck and Hieroglyphy obfuscation of Javascript code Cross-Site Scripting (XSS) Attempt: Defend against JSFuck and Hieroglyphy obfuscation of Javascript code.
941370 Cross-Site Scripting (XSS) Attempt: Prevent 94118032 bypass by using JavaScript global variables Cross-Site Scripting (XSS) Attempt: Prevent 94118032 bypass by using JavaScript global variables.
941380 Cross-Site Scripting (XSS) Attempt: Defend against AngularJS client side template injection Cross-Site Scripting (XSS) Attempt: Defend against AngularJS client side template injection.
942100 SQL Injection (SQLi) Libinjection Detection SQL Injection (SQLi) Attempt: SQLi Filters via libinjection.
942101 SQL Injection (SQLi) Libinjection SQL Injection (SQLi) Attempt: Detects SQLi using libinjection.
942110 SQL Injection (SQLi) String termination/ Statement ending injection SQL Injection (SQLi) Attempt: String termination/ Statement ending injection detection also detects CVE-2018-2380.
942120 SQL Injection (SQLi) SQL operators SQL Injection (SQLi) Attempt: SQL operators detection also detects CVE-2018-2380.
942130 SQL Injection (SQLi) SQL Tautologies SQL Injection (SQLi) Attempt: SQL Tautologies detection
942140 SQL Injection (SQLi) Detect DB Names SQL Injection (SQLi) Attempt: SQLi Filters via DB Names
942150 SQL Injection (SQLi) SQL Function Names SQL Injection (SQLi) Attempt: SQL Function Names detection also detects CVE-2018-2380.
942160 SQL Injection (SQLi) PHPIDS SQLi Filters SQL Injection (SQLi) Attempt: SQLi Filters via PHPIDS.
942170 SQL Injection (SQLi) SQL benchmark and sleep injections SQL Injection (SQLi) Attempt: SQL benchmark and sleep injection detection.
942180 SQL Injection (SQLi) Basic SQL auth bypass SQL Injection (SQLi) Attempt: Basic SQL authentication bypass detection.
942190 SQL Injection (SQLi) MSSQL code execution and info gathering SQL Injection (SQLi) Attempt: MSSQL code execution and info gathering detection.
942200 SQL Injection (SQLi) MySQL comment-/space-obfuscated injections and backtick termination SQL Injection (SQLi) Attempt: MySQL comment-/space-obfuscated injections and backtick termination detection.
942210 SQL Injection (SQLi) chained SQL injection attempts SQL Injection (SQLi) Attempt: chained SQL injection attempts detection.
942220 SQL Injection (SQLi) Integer overflow attacks SQL Injection (SQLi) Attempt: Integer Overflow attack detection.
942230 SQL Injection (SQLi) Conditional SQL injections SQL Injection (SQLi) Attempt: Conditional SQL injection detection.
942240 SQL Injection (SQLi) MYSQL charset/ MSSQL DOS SQL Injection (SQLi) Attempt: MYSQL charset/ MSSQL DOS detection.
942250 SQL Injection (SQLi) Merge / Execute / Immediate injections SQL Injection (SQLi) Attempt: MERGE / EXECUTE / IMMEDIATE injections detection.
942251 SQL Injection (SQLi) SQL HAVING queries SQL Injection (SQLi) Attempt: Detects SQL HAVING queries.
942260 SQL Injection (SQLi) basic SQL auth bypass SQL Injection (SQLi) Attempt: basic SQL authentication bypass detection.
942270 SQL Injection (SQLi) Common SQLi attacks for various dbs SQL Injection (SQLi) Attempt: Common attacks against msql, oracle, and other dbs detection.
942280 SQL Injection (SQLi) pg_sleep injection/ waitfor delay/ database shutdown SQL Injection (SQLi) Attempt: pg_sleep injection/ waitfor delay attack/ database shutdown detection.
942290 SQL Injection (SQLi) MongoDB SQLi SQL Injection (SQLi) Attempt: MongoDB SQL injection detection.
942300 SQL Injection (SQLi) MySQL comments, conditions and ch(a)r injections SQL Injection (SQLi) Attempt: MySQL comments, conditions and ch(a)r injections detection.
942310 SQL Injection (SQLi) chained SQL injection SQL Injection (SQLi) Attempt: chained SQL injection detection.
942320 SQL Injection (SQLi) MYSQL/ PostgreSQL stored procedure and function injection SQL Injection (SQLi) Attempt: MYSQL/ PostgreSQL stored procedure and function injection detection.
942330 SQL Injection (SQLi) classic SQL injection probings SQL Injection (SQLi) Attempt: classic SQL injection probings detection.
942340 SQL Injection (SQLi) basic SQL auth bypass attempts SQL Injection (SQLi) Attempt: basic SQL authentication bypass attempts detection.
942350 SQL Injection (SQLi) MYSQL UDF/ data structure manipulation SQL Injection (SQLi) Attempt: MYSQL UDF/ data structure manipulation detection.
942360 SQL Injection (SQLi) Concatenated SQLi and SQLLFI SQL Injection (SQLi) Attempt: Concatenated SQLi and SQLLF detection.
942361 SQL Injection (SQLi) basic SQL injection based on keyword alter or union SQL Injection (SQLi) Attempt: basic SQL injection based on keyword alter or union detection.
942370 SQL Injection (SQLi) classic SQL injection probings SQL Injection (SQLi) Attempt: classic SQL injection probings detection also detects CVE-2018-2380.
942380 SQL Injection (SQLi) SQL injection SQL Injection (SQLi) Attempt: SQL injection detection.
942390 SQL Injection (SQLi) SQL injection SQL Injection (SQLi) Attempt: SQL injection detection.
942400 SQL Injection (SQLi) SQL injection SQL Injection (SQLi) Attempt: SQL injection detection.
942410 SQL Injection (SQLi) SQL injection SQL Injection (SQLi) Attempt: SQL injection detection also detects CVE-2018-2380.
942420 SQL Injection (SQLi) SQL Injection Character Anomaly Usage SQL Injection (SQLi) Attempt: Detects when there is an excessive use of meta-characters within a single parameter payload.
942421 SQL Injection (SQLi) SQL Injection Character Anomaly Usage SQL Injection (SQLi) Attempt: Detects SQL Injection Character Anomaly Usage.
942430 SQL Injection (SQLi) Restricted SQL Character Anomaly Detection SQL Injection (SQLi) Attempt: This rules attempts to gauge when there is an excessive use of meta-characters within a single parameter payload. Also detects CVE-2018-2380.
942431 SQL Injection (SQLi) Restricted SQL Character Anomaly Detection SQL Injection (SQLi) Attempt: Restricted SQL Character Anomaly Detection also detects CVE-2018-2380.
942432 SQL Injection (SQLi) Restricted SQL Character Anomaly Detection SQL Injection (SQLi) Attempt: Restricted SQL Character Anomaly Detection also detects CVE-2018-2380.
942440 SQL Injection (SQLi) SQL Comment Sequence SQL Injection (SQLi) Attempt: Detects SQL Comment Sequence.
942450 SQL Injection (SQLi) SQL Hex Evasion Methods SQL Injection (SQLi) Attempt: Detects SQL Hex Evasion Methods.
942460 SQL Injection (SQLi) Repetitive Non-Word Characters SQL Injection (SQLi) Attempt: Detects when multiple (4 or more) non-word characters are repeated in sequence.
942470 SQL Injection (SQLi) SQL injection SQL Injection (SQLi) Attempt: SQL injection detection.
942480 SQL Injection (SQLi) SQL injection SQL Injection (SQLi) Attempt: SQL injection detection.
942490 SQL Injection (SQLi) classic SQL injection probings SQL Injection (SQLi) Attempt: Detects classic SQL injection probings.
942500 SQL Injection (SQLi) in-line comments SQL Injection (SQLi) Attempt: In-line comments detection.
942510 SQL Injection (SQLi) SQLi bypass: backticks SQL Injection (SQLi) Attempt: Detects quotes and backticks can be used to bypass SQLi detection.
942511 SQL Injection (SQLi) SQLi bypass: quotes SQL Injection (SQLi) Attempt: Detects quotes and backticks which can be used to bypass filters.
943100 Session Fixation cookie in HTML Detects Cookie Values in HTML which could be a session fixation attack
943110 Session Fixation Off-Domain Referer in SessionID Detects SessionID Parameter Name with Off-Domain Referer
943120 Session Fixation No Referer in SessionID Detects SessionID Parameter Name with No Referer
944100 Java attack Attempt: Apache Struts and Oracle WebLogic vulnerabilities Java attack Attempt: Apache Struts and Oracle WebLogic vulnerabilities
944110, 944120 Java attack Attempt: Apache Struts and Oracle WebLogic vulnerabilities and detect processbuilder or runtime calls Java attack Attempt: Apache Struts and Oracle WebLogic vulnerabilities, Java deserialization
944130 Java attack Attempt: Apache Struts and Oracle WebLogic vulnerabilities Java attack Attempt: Apache Struts and Oracle WebLogic vulnerabilities
944200 Java attack Attempt:Detect exploitation of "Java deserialization" Apache Commons Java attack Attempt: Detect exploitation of "Java deserialization" Apache Commons
944210 Java attack Attempt:Detecting possibe base64 text to match encoded magic bytes \xac\xed\x00\x05 with padding encoded in base64 strings are rO0ABQ KztAAU Cs7QAF Java attack Attempt: Detecting possibe base64 text to match encoded magic bytes \xac\xed\x00\x05 with padding encoded in base64 strings are rO0ABQ KztAAU Cs7QAF
944240 Java attack Attempt:Remote Command Execution: Java serialization Java attack Attempt: Remote Command Execution: Java serialization
944250 Java attack Attempt:SAP CRM Java vulnerability CVE-2018-2380 Java attack Attempt: SAP CRM Java vulnerability CVE-2018-2380
944300 Java attack Attempt:Interesting keywords for possibly RCE on vulnerable classess and methods base64 encoded Java attack Attempt: Interesting keywords for possibly RCE on vulnerable classess and methods base64 encoded
950001, 959070, 959071, 959072, 950908, 959073 Common SQL Injections Detects common SQL injection attacks
950002 Common system command access attempt Detect access attempts to common system commands, such as map, telnet, ftp, rcms, and cmd.
950005 Common system files access attempt Detects access attempts to common system files, such as access, passwd, groupm global.asa, httpd.conf, boot.ini, /and so on.
950006 Injection for common system commands Detects injections for common system commands such as telnet, map, blocalgroup, ftp, rcmd, echo, cmd, chmod, passwd, and mail.
950007 Blind SQL injection Detects common blind SQL injection attacks.
950008 ColdFusion Admin Functions Injection Detects injection of ColdFusion undocumented admin functions.
950009, 950003, 950000 Session fixation Session Fixation is an attack technique that forces a user's session ID to an explicit value. Depending on the functionality of the target web site, a number of techniques can be utilized to "fix" the session ID value. These techniques range from Cross-site Scripting exploits to peppering the web site with previously made HTTP requests. After a user's session ID has been fixed, the attacker will wait for that user to login. Once the user does so, the attacker uses the predefined session ID value to assume the same online identity.
950010 LDAP Injection Detects common LDAP data constructions injections.
950011 SSI Injection Detects common Server-Side-Include format data injections.
950012 HTTP Request Smuggling Detects specially crafted requests that under certain circumstances could be seen by the attacked entities as two different sets of requests. This allows certain requests to be smuggled through to a second entity without the first one realizing it.
950018 UPDF XSS Injection Detects submitted links that contains the # fragment in a query_string.
950019 Email Injection Detects mail command Injections targeting mail servers and webmail applications that construct IMAP/SMTP statements from user-supplied input that is not properly sanitized.
950103 Path/directory traversal Detects path traversal attempts, also known as directory traversal or "../" attacks.
950107, 950109, 950108 URL Encodings Validation Detects URL encoding inconsistencies, encoding abuse and invalid formatting.
950110, 950921, 950922 Trojan, Backdoor and Webshell Access Attempts Detects when an attacker attempts to access trojan, backdoor or webshell web page.
950116 Unicode Encoding/Decoding Validation Blocks full-width Unicode encoding as decoding evasions could be possible.
950117 URL Contains an IP Address Detects a common RFI attack, when URL contains an IP address.
950118 PHP include() function Detects a common RFI php include() function attacks.
950119 Data ends with question mark(s) (?) Detects a common RFI attack, when data ends with question mark(s) (?).
950120 Host doesn't match localhost Detects a common RFI attack, when Host Doesn't Match Local Host.
950801 UTF Encoding Validation Detects UTF encoding inconsistencies and invalid formatting.
950901 SQL Tautologies Detects common SQL tautologies attacks.
950907 OS Command Injection Detects OS command injection in an application to elevate privileges, execute arbitrary commands, compromise the underlying operating system and install malicious toolkits such as those to participate in botnet attacks.
950910, 950911 HTTP Response Splitting Detects Carriage Return + Linefeed characters in the response header that could cause attacked entities to interpret it as two separate responses instead of one.
958000 addimport XSS attack Detects usage of addimport in request, cookies, or arguments.
958001 document cookie XSS attack Detects usage of document.cookie in request, cookies, or arguments.
958002 execscript XSS attack Detects usage of execscript in request, cookies, or arguments.
958003 fromcharcode XSS attack Detects usage of fromcharcode in request, cookies, or arguments.
958004 innerhtml XSS attack Detects usage of innerhtml in request, cookies, or arguments.
958005 cdata XSS attack Detects usage of cdata in request, cookies, or arguments.
958006 body background XSS attack Detects usage of &lt;body background in request, cookies, or arguments.
958007 onload XSS attack Detects usage of onload in request, cookies, or arguments.
958008 input type image XSS attack Detects usage of &lt;input type image in request, cookies, or arguments.
958009 import XSS attack Detects usage of import in request, cookies, or arguments.
958010 activexobject XSS attack Detects usage of activexobject in request, cookies, or arguments.
958011 background-image: XSS attack Detects usage of background-image: in request, cookies, or arguments.
958012 copyparentfolder XSS attack Detects usage of copyparentfolder in request, cookies, or arguments.
958013 createtextrange XSS attack Detects usage of createtextrange in request, cookies, or arguments.
958016 getparentfolder XSS attack Detects usage of getparentfolder in request, cookies, or arguments.
958017 getspecialfolder XSS attack Detects usage of getspecialfolder in request, cookies, or arguments.
958018 href javascript: XSS attack Detects usage of href javascript: in request, cookies, or arguments.
958019 href schell XSS attack Detects usage of href schell in request, cookies, or arguments.
958020 href vbscript: XSS attack Detects usage of href vbscript: in request, cookies, or arguments.
958022 livescript: XSS attack Detects usage of livescript: in request, cookies, or arguments.
958023 lowsrc javascript: XSS attack Detects usage of lowsrc javascript: in request, cookies, or arguments.
958024 lowsrc shell XSS attack Detects usage of lowsrc shell in request, cookies, or arguments.
958025 lowsrc vbscript XSS attack Detects usage of lowsrc vbscript in request, cookies, or arguments.
958026 mocha: XSS attack Detects usage of mocha: in request, cookies, or arguments.
958027 onabort XSS attack Detects usage of onabort in request, cookies, or arguments.
958028 settimeout XSS attack Detects usage of settimeout in request, cookies, or arguments.
958030 src http: XSS attack Detects usage of src http: in request, cookies, or arguments.
958031 javascript: XSS attack Detects usage of javascript: in request, cookies, or arguments.
958032 src and shell XSS attack Detects usage of src and shell in request, cookies, or arguments.
958033 vbscript: XSS attack Detects usage of vbscript: in request, cookies, or arguments.
958034 style bexpression XSS attack Detects usage of style bexpression in request, cookies, or arguments.
958036 type application x-javascript XSS attack Detects usage of type application x-javascript in request, cookies, or arguments.
958037 type application x-vbscript XSS attack Detects usage of type application x-vbscript in request, cookies, or arguments.
958038 type text ecmascript XSS attack Detects usage of type text ecmascript in request, cookies, or arguments.
958039 type text javascript XSS attack Detects usage of type text javascript in request, cookies, or arguments.
958040 type text jscript XSS attack Detects usage of type text jscript in request, cookies, or arguments.
958041 type text vbscript XSS attack Detects usage of type text vbscript in request, cookies, or arguments.
958045 url javascript: XSS attack Detects usage of url javascript: in request, cookies, or arguments.
958046 url shell XSS attack Detects usage of &lt;url shell in request, cookies, or arguments.
958047 url vbscript: XSS attack Detects usage of url vbscript: in request, cookies, or arguments.
958049 ?meta XSS attack Detects usage of ?meta in request, cookies, or arguments.
958051 ?script XSS attack Detects usage of &lt; ?script in request, cookies, or arguments.
958052 alert XSS attack Detects usage of alert in request, cookies, or arguments.
958054 lowsrc and http: XSS attack Detects usage of lowsrc and http: in request, cookies, or arguments.
958056 iframe src XSS attack Detects usage of iframe src in request, cookies, or arguments.
958057 ?iframe XSS attack Detects usage of ?iframe in request, cookies, or arguments.
958059 asfunction: XSS attack Detects usage of asfunction: in request, cookies, or arguments.
958295 Connection Header Validation Detects connection header inconsistencies and invalid formatting
958404 onerror XSS attack Detects usage of onerror in request, cookies, or arguments.
958405 onblur XSS attack Detects usage of onblur in request, cookies, or arguments.
958406 onchange XSS attack Detects usage of onchange in request, cookies, or arguments.
958407 onclick XSS attack Detects usage of onclick in request, cookies, or arguments.
958408 ondragdrop XSS attack Detects usage of ondragdrop in request, cookies, or arguments.
958409 onfocus XSS attack Detects usage of onfocus in request, cookies, or arguments.
958410 onkeydown XSS attack Detects usage of onkeydown in request, cookies, or arguments.
958411 onkeypress XSS attack Detects usage of onkeypress in request, cookies, or arguments.
958412 onkeyup XSS attack Detects usage of onkeyup in request, cookies, or arguments.
958413 onload XSS attack Detects usage of onload in request, cookies, or arguments.
958414 onmousedown XSS attack Detects usage of onmousedown in request, cookies, or arguments.
958415 onmousemove XSS attack Detects usage of onmousemove in request, cookies, or arguments.
958416 bonmouseout XSS attack Detects usage of bonmouseout in request, cookies, or arguments.
958417 bonmouseover XSS attack Detects usage of bonmouseover in request, cookies, or arguments.
958418 onmouseup XSS attack Detects usage of onmouseup in request, cookies, or arguments.
958419 onmove XSS attack Detects usage of onmove in request, cookies, or arguments.
958420 onresize XSS attack Detects usage of onresize in request, cookies, or arguments.
958421 onselect XSS attack Detects usage of onselect in request, cookies, or arguments.
958422 onsubmit XSS attack Detects usage of onsubmit in request, cookies, or arguments.
958423 onunload XSS attack Detects usage of onunload in request, cookies, or arguments.
959151, 958976, 958977 php code injection Detects a common injections attack, when request contain any php code e.g. "&lt;\?&gt;"
960000 File Name Validation Detects multipart/form-data file name evasion attempts.
960007, 960008 Missing Host Header Detects missing request host header.
960009, 960006 Missing User-Agent Header Detects missing request user-agent header.
960010 Restrict HTTP Content Types Allows only such content types as: application/x-www-form-urlencoded, multipart/form-data, text/xml, application/xml, application/x-amf, application/json
960011 GET/HEAD Requests Validation Detects if GET/HEAD requests contain request body, since it is not a common practice.
960012 Content-Length Header Validation Detects if content-length header is provided with every POST request.
960013 Require Content-Length to be provided with every HTTP/1.1 POST request that has no Transfer-Encoding header Detect HTTP/1.1 request that do not comply with HTTP 1.1 spec by having no Content-Length header when Transfer-Encoding is also absent.
960014 URI Validation Ensures that URI and canonical server name are matching.
960015, 960021 Missing Accept Header Detects missing request accept header.
960016 Content-Length Header Validation Detects if content-length HTTP header is not numeric.
960017 Host Header Is IP Address Detects if host header is a numeric IP address as it could be an indicative of automated client access.
960020 Pragma Header Validation Ensures that pragma, cache-control headers and HTTP protocol version supplied by the client are matching.
960022 Expect Header Validation Ensures that expect header and HTTP protocol version supplied by the client are matching.
960024 Repeatative Non-Word Chars Attempts to identify when four or more non-word characters are repeated in sequence.
960032 Restrict HTTP Request Methods Allows only request methods specified by the configurable "Allowed http methods" parameter.
960034 Restrict HTTP Protocol Versions Allows only HTTP protocol versions HTTP/1.0 and HTTP/1.1.
960208 Values Limits Detects HTTP requests with value length exceeding the configurable "Max length of argument" parameter.
960209 Arguments Limits Detects HTTP requests with argument name length exceeding the 100 symbols.
960335 Number of Arguments Limits Detects HTTP requests with number of arguments exceeding the configurable "Max amount of arguments" value.
960341 Total Arguments Limits Detects HTTP requests with total length of all arguments exceeding the configurable "Max total argument length" parameter.
960901, 960018 Character Set Validation Ensures that only specific character set(s) is used.
960902 Content-Encoding Header Validation Ensures that identity is not specified in content-encoding header.
960904 Missing Content-Type Header Detects missing content-type header or if combination of content-length and content-type headers is invalid.
960911 Request Line Format Validation against the HTTP RFC Uses rule negation against the regex for positive security. The regex specifies the proper construction of URI request lines such as: "http:" "//" host [ ":" port ] [ abs_path [ "?" query ]]. It also outlines proper construction for CONNECT, OPTIONS and GET requests.
960912 Malformed request bodies Checks for Request body parsing errors.
960914 Strict Multipart Parsing Checks By default be strict with what we accept in the multipart/form-data request body. If the rule below proves to be too strict for your environment, consider changing it to Off.
960915 Multipart Unmatched Boundary Check Checks for signs of evasions during file upload requests.
970002 Statistics pages information leakage Detects statistics pages information leakage.
970003 SQL errors information leakage Detects SQL errors information leakage.
970004, 970904 IIS errors information leakage Detects IIS errors information leakage.
970007 Zope information leakage Detects Zope information leakage.
970008 ColdFusion information leakage Detects ColdFusion information leakage.
970009 PHP information leakage Detects PHP information leakage.
970010 ISA server existence revealed Detects if ISA server existence revealed.
970011 File and/or directory names leakage Detects file and/or directory names leakage.
970012, 970903 MS Office document properties leakage Detects MS Office document properties leakage.
970013 Directory listing information leakage Detects directory listing information leakage.
970014 ASP/JSP source code leakage Detects ASP/JSP source code leakage.
970015, 970902 PHP source code leakage Detects PHP source code leakage.
970016 ColdFusion source code leakage Detects ColdFusion source code leakage.
970018 IIS default location revealed Detects if IIS default location revealed.
970021 Weblogic information leakage Detects Weblogic information leakage.
970118 Microsoft OLE DB Provider Error page leakage Detects Microsoft OLE DB Provider for SQL Server error page.
970901 5XX Status code information leakage Detects if application generates 500-level status code, for example, 500 Internal Server Error, 501 Not Implemented...505 HTTP Version Not Supported.
973300, 973301, 973302 Common direct HTML injection Detects tags that are the most common direct HTML injection points.
973306 Embedding javascript in style attribute Detects embedding javascript in style attribute.
973307 Embedded Scripts Within JavaScript Fragments Detects common JavaScript fragments like fromcharcode, alert, eval that can be used for attacks.
973309, 973308 CSS Fragments attacks Detects common CSS fragments attacks like &lt;div style="background-image: url(javascript:...)"&gt; or &lt;img style="x:expression(document.write(1))"&gt;
973310 Embedded Scripts Within Alert Fragments Detects attacks like alert('xss'), alert("xss"), alert(/xss/).
973311 String.fromCharCode(88,83,83) attacks Detects String.fromCharCode(88,83,83) attacks.
973312 '';!--"&lt;XSS&gt;=&amp;{()} Attacks Detects '';!--"&lt;XSS&gt;=&amp;{()} attacks.
973313 &amp;{alert('xss')} attacks Detects &amp;{alert('xss')} attacks.
973314 Doctype Entity inject Detects Doctype Entity inject attacks.
973331, 973315, 973330, 973327, 973326, 973346, 973345, 973324, 973323, 973322, 973348, 973321, 973320, 973318, 973317, 973347, 973335, 973334, 973333, 973344, 973332, 973329, 973328, 973316, 973325, 973319 Internet Explorer XSS Filters Detects common IE XSS attacks.
973336 Embedding Scripts Within Scripts Detects script tag based XSS vectors, for example, &lt;script&gt; alert(1)&lt;/script&gt;.
973337, 973303 Embedded Scripts Within Event Handlers Detects event handler based XSS vectors, for example, &lt;body onload="alert(1)"&gt;.
973338, 973304, 973305 Embedded Scripts Within URI Schemes Detects "data", "javascript", "src" or other URI schemes/attributes based XSS vectors, for example, &lt;p style="background:url(javascript:alert(1))"&gt;
981004 Potential Obfuscated Javascript, fromCharCode Detects excessive fromCharCode Javascript in Output.
981005 Potential Obfuscated Javascript, Eval+Unescape Detects Potential Eval+Unescape in response.
981006 Potential Obfuscated Javascript, Unescape Detects Potential Unescape in response.
981007 Potential Obfuscated Javascript, Heap Spray Detects Potential Heap Spray in response.
981078, 920019, 920005, 920007, 920009, 920011, 920013, 920015, 920017 Credit card leakage in request Detects primary credit card numbers (Visa, MasterCard, GSA SmartPay, Americal Express, Diners Club, enRoute, Discover, JCB) in user input.
981080, 920020, 920006, 920008, 920010, 920012, 920014, 920016, 920018 Credit card leakage in response Detects primary credit card numbers (Visa, MasterCard, GSA SmartPay, Americal Express, Diners Club, enRoute, Discover, JCB) sent from site to user.
981136 Generic XSS attacks Detects common XSS attacks embedded within non-script elements, for example, jscript onsubmit copyparentfolder document javascript meta onchange onmove onkeydown onkeyup activexobject onerror onmouseup ecmascript bexpression onmouseover vbscript.
981172, 981173 SQL Character Anomaly Scoring Attempts to gauge when there is an excessive use of meta-characters within a single parameter payload.
981177, 981000, 981001, 981003 IFrame Injection Detects iframe injections that could execute malicious code to steal data, redirect to malware infected sites, load malware, and so on.
981227 Request URI Validation Detects invalid URI in request.
981231 SQL Comment Sequences Detects common SQL comment sequences, for example, DROP/*comment*/sampletable.
981240 MySQL comments, conditions Detects MySQL comments, conditions and ch(a)r injections.
981241 Conditional SQL injection attempts Detects conditional SQL injection attempts.
981242, 981243 Ð¡lassic SQL injection probings Detects classic SQL injection probings.
981244, 981245, 981246 SQL authentication bypass attempts Detects basic SQL authentication bypass attempts.
981247 Concatenated basic SQL injection and SQLLFI attempts Detects concatenated basic SQL injection and SQLLFI attempts.
981248, 981249 Chained SQL injection attempts Detects chained SQL injection attempts.
981250 SQL benchmark and sleep injection attempts Detects SQL benchmark and sleep injection attempts including conditional queries.
981251 MySQL UDF injection Detects MySQL UDF injection and other data/structure manipulation attempts.
981252 MySQL charset switch and MSSQL DoS attempts Detects MySQL charset switch and MSSQL DoS attempts.
981253 MySQL and PostgreSQL stored procedure/function injections Detects MySQL and PostgreSQL stored procedure/function injections.
981254 PostgreSQL pg_sleep injection Detects PostgreSQL pg_sleep injection, waitfor delay attacks and database shutdown attempts.
981255 MSSQL code execution Detects MSSQL code execution and information gathering attempts.
981256 MATCH AGAINST, MERGE, EXECUTE IMMEDIATE and HAVING Detects MATCH AGAINST, MERGE, EXECUTE IMMEDIATE and HAVING injections.
981257 MySQL comment-/space-obfuscated Detects MySQL comment-/space-obfuscated injections and backtick termination.
981260 SQL Hex Evasion Methods Detects SQL hex encoding evasion attacks.
981270 MongoDB SQL injection Detects basic MongoDB SQL injection attempts.
981272 SQL injection using sleep() or benchmark() Detects blind SQL injection tests using sleep() or benchmark() functions.
981276 Common attack string for mysql, oracle Detects common attack string for mysql, oracle and others
981277 Integer overflow attacks Detects integer overflow attacks.
981300, 981301, 981302, 981303, 981304, 981305, 981306, 981307, 981308, 981309, 981310, 981311, 981312, 981313, 981314, 981315, 981316, 981317 SQL Keyword Anomaly Scoring Detects common SQL keywords anomalies.
981318 String Termination/Statement Ending Identifies common initial SQLi probing requests where attackers insert/append quote characters to the existing normal payload to see how the app/db responds.
981319 SQL Operators Detects common SQL operators injection attacks.
981320 DB Names Detects common DB names injection attacks.
1000000, 1000001, 1000002, 1000003, 1000004 Shellshock exploit attempt Detects the the ability to unintentionally execute commands in Bash. CVE-2014-6271
2017100 Apache Struts 2 Multipart parser CVE-2017-5638 Remote Code Execution Vulnerability Prevention Detects Apache Jakarta CVE-2017-5638 Remote Code Execution Vulnerability payload.
2018100 CVE-2018-6389 WordPress Parameter Resource Consumption Remote DoS WordPress Parameter Resource Consumption Remote DoS on jquery-ui-core.
2100019 /_layouts/scriptresx.ashx sections Parameter XSS Microsoft SharePoint /_layouts/scriptresx.ashx sections Parameter XSS
2100023 /owssrv.dll List Parameter XSS Microsoft SharePoint /owssrv.dll List Parameter XSS
2100026 _layouts/Chart/WebUI/WizardList.aspx skey Parameter XSS Microsoft SharePoint _layouts/Chart/WebUI/WizardList.aspx skey Parameter XSS
2100027 _layouts/themeweb.aspx XSS Microsoft SharePoint _layouts/themeweb.aspx ctl00$PlaceHolderMain$ctl82$customizeThemeSection$accent6 Parameter XSS
2100028 _layouts/inplview.aspx ListViewPageUrl Parameter XSS Microsoft SharePoint _layouts/inplview.aspx ListViewPageUrl Parameter XSS
2100032 owssrv.dll View Parameter XSS Microsoft SharePoint owssrv.dll View Parameter XSS
2100033 NewForm.aspx TextField_spSave Parameter XSS Microsoft SharePoint NewForm.aspx TextField_spSave Parameter XSS
2100034 /Lists/Calendar/calendar.aspx CalendarDate Parameter XSS Microsoft SharePoint /Lists/Calendar/calendar.aspx CalendarDate Parameter XSS
2100035 _layouts/Picker.aspx XSS Microsoft SharePoint _layouts/Picker.aspx ctl00$PlaceHolderDialogBodySection$ctl04$hiddenSpanData Parameter XSS
2100048 _layouts/help.aspx cid0 Parameter XSS Microsoft SharePoint _layouts/help.aspx cid0 Parameter XSS
2100062 _layouts/ScriptResx.ashx name Parameter LFI Microsoft SharePoint _layouts/ScriptResx.ashx name Parameter LFI
2100063 _layouts/OSSSearchResults.aspx k Parameter XSS Microsoft SharePoint _layouts/OSSSearchResults.aspx k Parameter XSS
2100069 wiki pages multiple Parameter XSS Microsoft SharePoint wiki pages multiple Parameter XSS (CVE-2013-3180)
2100070 /Lists/Links/AllItems.aspx XSS Microsoft SharePoint /Lists/Links/AllItems.aspx ctl00$m$g_2085a7 32_4692_4d3e_99d2_4d90ea5108d2$ctl00$ctl05$ctl00$ctl00$ctl00$ctl04$ctl00$ctl00$UrlFieldUrl Parameter XSS
2100082 Drupal - pre-auth SQL Injection Vulnerability A malicious user can inject arbitrary SQL queries, and thereby control the complete Drupal site. This leads to a code execution as well. Drupal 7.32 fixed this bug.
2100083 Gerber WebPDM XSS Vulnerability Cross-Site Scripting Vulnerability in Gerber WebPDM Product Data Management System
2100084 Gerber WebPDM SQL Injection Vulnerability SQL Injection Vulnerability in Gerber WebPDM Product Data Management System
2100085 High X-SharePointHealthScore Microsoft SharePoint High X-SharePointHealthScore - Potential DoS Attack/Availability Risk
2100086 Response Header Found Microsoft SharePoint SharePointError Response Header Found
2100087 x-virus-infected Response Header Found Microsoft SharePoint x-virus-infected Response Header Found
2100088 Rights Management (IRM) Error Response Header Found Microsoft SharePoint Information Rights Management (IRM) Error Response Header Found
2100089 /_layouts/mobile/editform.aspx XSS Microsoft SharePoint /_layouts/mobile/editform.aspx XSS
2100090 Microsoft OWA X-OWA-Error Response Header Found Microsoft OWA X-OWA-Error Response Header Found
2200924 IRC Botnet Attacks Detects common IRC Botnet Attack Commands
2250117, 2250118, 2250119 Common RFI attacks Detects a common types of Remote File Inclusion (RFI) attack
2250120 Local File Inclusion Attacks Detects common local file inclusion attacks like my $dir = "../../../../../../../../../../../../../"; or "http://".$site.$bug.$dir."/proc/self/environ%0000";
2250121 Local File Inclusion ENV Attack in User-Agent Detects Local File Inclusion ENV Attack in User-Agent
2250122 PHP Injection Attack Detects common php injection attacks like "send-contactus=1&amp;author_name=[php]eval(base64_decode('".$code."'))%3Bdie%28%29%3B%5B%2Fphp%5D"
2250123 XML-RPC PHP Injection Attack Detects common XML-RPC PHP Injections like $exploit .= "echo'j13mb0t';".$code."echo'j13mb0t';exit;/*&lt;/name&gt;&lt;/value&gt;&lt;/param&gt;&lt;/params&gt;&lt;/methodCall&gt;";
2250124 Botnet SQL Injection Attack Detects Botnet SQL Injections like $sql=$situs."-1".$cmn."union".$cmn."select".$cmn."0x6c6f67696e70776e7a".$inyection.$cfin;
2250125 osCommerce File Upload Detects osCommerce file upload attacks like "http://".$site."admin/file_manager.php/login.php";
2250126 Oscommerce File Disclosure And Admin ByPass Detects Oscommerce File Disclosure And Admin ByPass
2250127 e107 Plugin my_gallery Exploit Detects e107 Plugin my_gallery Exploit "http://".$site."e107_plugins/my_gallery/image.php?file=../../e107_config.php"
2250128 Opencart Remote File Upload Vulnerability Detects Opencart Remote File Upload Vulnerability.
2250129 Zen Cart local file disclosure vulnerability Detects Zen Cart local file disclosure vulnerability.
2200925, 2200926 Detects HOIC DoS Tool requests Detects HOIC DoS Tool requests.
9300000 Local File Inclusion (LFI) Collaborative Group - LFI Filter Categories Local File Inclusion (LFI) Attempt: Directory Traversal Attacks - OS File Access.
9320000 Remote Code Execution (RCE) Collaborative Group - Unix RCE Filter Categories Remote Code Execution (RCE) Attempt: RCE Filters for Unix.
9320001 Remote Code Execution (RCE) Collaborative Group - Windows RCE Filter Categories Remote Code Execution (RCE) Attempt: RCE Filters for Windows.
9330000 PHP Injection Attacks Collaborative Group - PHP Filters Categories PHP Injection Attempt: PHP Filters - Detects PHP open tags "&lt;?", "&lt;?php", "[php]", "[/php]" and "[\php]" - PHP Script Uploads, PHP Config Directives, PHP Functions, PHP Object Injection.
9410000 Cross-Site Scripting (XSS) Collaborative Group - XSS Filters Categories Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 1.
9420000 SQL Injection (SQLi) Collaborative Group - SQLi Filters Categories SQL Injection (SQLi) Attempt: SQLi Filters via libinjection - Detect Database names - PHPIDS - Converted SQLI Filters.
9958291, 958230, 958231 Range Header Validation This rule inspects the Range request header to see if it starts with 0.
20182056 CVE-2003-1567 CVE-2004-2320 CVE-2010-0360 TRACE &amp; CONNECT Attempts TRACE Method attempt
92010032 Request Line Format Validation against the HTTP RFC Uses rule negation against the regex for positive security. The regex specifies the proper construction of URI request lines such as: "http:" "//" host [ ":" port ] [ abs_path [ "?" query ]]. It also outlines proper construction for CONNECT, OPTIONS and GET requests.
92035032 Host Header Is IP Address Detects if host header is a numeric IP address as it could be an indicative of automated client access.
93010032 Local File Inclusion (LFI) - Directory Traversal - Encoded Payloads Local File Inclusion (LFI) Attempt: Directory Traversal Attacks - Encoded Payloads
93011032 Local File Inclusion (LFI) - Directory Traversal - Decoded Payloads Local File Inclusion (LFI) Attempt: Directory Traversal Attacks - Decoded Payloads
93012032 Local File Inclusion (LFI) - OS File Access Local File Inclusion (LFI) Attempt: OS File Access
93013032 Local File Inclusion (LFI) - Restricted File Access Local File Inclusion (LFI) Attempt: Restricted File Access
93110032 Remote File Inclusion (RFI) Attempt: RFI Attack URL Parameter using IP Address Remote File Inclusion (RFI). These rules look for common types of Remote File Inclusion (RFI) attack methods. Possible RFI Attack: URL Parameter using IP Address
93111032 Remote File Inclusion (RFI) Attempt: RFI Attack: Common RFI Vulnerable Parameter Name used w/URL Payload Remote File Inclusion (RFI). These rules look for common types of Remote File Inclusion (RFI) attack methods. Possible RFI Attack: Common RFI Vulnerable Parameter Name used w/URL Payload
93112032 Remote File Inclusion (RFI) Attempt: RFI Attack: URL Payload Used w/Trailing Question Mark Character (?) Remote File Inclusion (RFI). These rules look for common types of Remote File Inclusion (RFI) attack methods. Possible RFI Attack: URL Payload Used w/Trailing Question Mark Character (?)
93113032 Remote File Inclusion (RFI) Attempt: RFI Attack: Off-Domain Reference/Link Remote File Inclusion (RFI). These rules look for common types of Remote File Inclusion (RFI) attack methods. Possible RFI Attack: Off-Domain Reference/Link
93210032 Unix Command Injection Detects several Unix command injections (and its attempts of obfuscation and evasion). The vulnerability exists when an application executes a shell command without proper input escaping/validation. This rule is also triggered by an Oracle WebLogic Remote Command Execution exploit.
93210532 Unix Command Injection Detects several Unix command injections (and its attempts of obfuscation and evasion). The vulnerability exists when an application executes a shell command without proper input escaping/validation.
93211032 Windows Command Injection This rule Detects Windows shell command injections (and its attempts of obfuscation and evasion). The vulnerability exists when an application executes a shell command without proper input escaping/validation.
93211532 Windows Command Injection This rule Detects Windows shell command injections (and its attempts of obfuscation and evasion). The vulnerability exists when an application executes a shell command without proper input escaping/validation.
93212032 Windows PowerShell Injection - cmdlets and options Detect some common PowerShell commands, cmdlets and options. These commands should be relatively uncommon in normal text, but potentially useful for code injection.
93213032 Unix Shell Script Expressions and Oneliners. Detects common Unix Shell Expressions used in Shell Scripts and Oneliners, such as "$(foo), ${foo}, &lt;(foo), &gt;(foo), $((foo)), among others"
93214032 Windows Command Shell Injection - FOR and IF commands This rule Detects Windows command shell FOR and IF commands.
93215032 Unix Direct Remote Command Execution Detects Unix commands at the start of a parameter (direct RCE). Example: foo=wget%20www.example.com. This case is different from command injection (rule 93210032), where a command string is appended (injected) to a regular parameter, and then passed to a shell unescaped. This rule is also triggered by an Oracle WebLogic Remote Command Execution exploit.
93216032 Unix Shell Snippets Injection Detect some common sequences found in shell commands and scripts. This rule is also triggered by an Apache Struts Remote Code Execution, and Oracle WebLogic Remote Command Execution exploits.
93217032, 93217132 GNU Bash RCE Shellshock Vulnerability (CVE-2014-6271 and CVE-2014-7169) Detect exploitation of "Shellshock" GNU Bash RCE vulnerability. Based on ModSecurity rules created by Red Hat.
93310032 PHP Injection Attacks: PHP Open Tag Found PHP Injection Attacks: Detects PHP open tags "&lt;?" and "&lt;?php". Also Detects "[php]", "[/php]" and "[\php]" tags used by some applications to indicate PHP dynamic content.
93311032 PHP Injection Attacks: PHP Script Uploads PHP Injection Attacks: Block file uploads with PHP extensions (.php, .php5, .phtml and so on), also block files with just dot (.) characters after the extension. Many application contain Unrestricted File Upload vulnerabilities. Attackers may use such a vulnerability to achieve remote code execution by uploading a .php file.Some AJAX uploaders use the nonstandard request headers X-Filename, X_Filename, or X-File-Name to transmit the file name to the server; scan these request headers as well as multipart/form-data file names.
93311132 PHP Injection Attacks: PHP Script Uploads - Superfluous extension PHP Injection Attacks: PHP Script Uploads - Superfluous extension. Block file uploads with PHP extensions (.php, .php5, .phtml and so on) anywhere in the name, followed by a dot.
93312032 PHP Injection Attacks: PHP Configuration Directives PHP Injection Attacks: Configuration Directive Found
93313032 PHP Injection Attacks: PHP Variables PHP Injection Attacks: Variables Found
93313132 PHP Injection Attacks: PHP Variables - Common Variable Indexes PHP Injection Attacks: Common Variable Indexes
93314032 PHP Injection Attacks: PHP I/O Streams PHP Injection Attacks: Variables Found. The "php://" syntax can be used to refer to various objects, such as local files (for LFI), remote urls (for RFI), or standard input/request body. Its occurrence indicates a possible attempt to either inject PHP code or exploit a file inclusion vulnerability in a PHP web app.
93315032 PHP Injection Attacks: High-Risk PHP Function Names PHP Injection Attacks: High-Risk PHP Function Names, Approximately 40 words highly common to PHP injection payloads and extremely rare in natural language or other contexts. Examples: 'base64_decode', 'file_get_contents'.
93315132 PHP Injection Attacks: Medium-Risk PHP Function Names PHP Injection Attacks: Medium-Risk PHP Function Names, Medium-Risk PHP injection payloads and extremely rare in natural language or other contexts. This includes most PHP functions and keywords.
93316032 PHP Injection Attacks: High-Risk PHP Function Calls PHP Injection Attacks: High-Risk PHP Function Calls, some PHP function names have a certain risk of false positives, due to short names, full or partial overlap with common natural language terms, uses in other contexts, and so on. Some examples are 'eval', 'exec', and 'system'.
93316132 PHP Injection Attacks: PHP Functions - Low-Value PHP Function Calls PHP Injection Attacks: PHP Functions - Low-Value PHP Function Calls. Most of these function names are likely to cause false positives in natural text or common parameter values, such as 'abs', 'copy', 'date', 'key', 'max', 'min'. Therefore, these function names are not scanned in lower paranoia levels or if high false positives are expected.
93317032 PHP Injection Attacks: PHP Object Injection PHP Injection Attacks: PHP Object Injection, is an application level vulnerability that could allow an attacker to perform different kinds of malicious attacks, such as Code Injection, SQL Injection, Path Traversal and Application Denial of Service, depending on the context. The vulnerability occurs when user-supplied input is not properly sanitized before being passed to the unserialize() PHP function.
93318032 PHP Injection Attacks: PHP Functions - Variable Function Calls PHP Injection Attacks: PHP Functions - Variable Function Calls, PHP 'variable functions' provide an alternate syntax for calling PHP functions. An attacker may use variable function syntax to evade detection of function names during exploitation of a remote code execution vulnerability.
94110032 Cross-Site Scripting (XSS) Attempt: Libinjection - XSS Detection Cross-Site Scripting (XSS) Attempt: Detects XSS Libinjection.
94110132 Cross-Site Scripting (XSS) Attempt: SS Attack Detected via libinjection Cross-Site Scripting (XSS) Attempt: SS Attack Detected through libinjection.
94111032 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 1 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 1. Script tag based XSS vectors, for example, &lt;script&gt; alert(1)&lt;/script&gt;
94112032 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 2 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 2. XSS vectors making use of event handlers like onerror, onload and so on, for example, &lt;body onload="alert(1)"&gt;
94113032 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 3 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 3. XSS vectors making use of Attribute Vectors
94114032 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 4 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 4. XSS vectors making use of javascript URI and tags, for example, &lt;p style="background:url(javascript:alert(1))"&gt;
94115032 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 5 Cross-Site Scripting (XSS) Attempt: XSS Filters - Category 5. HTML attribues - src, style, and href
94116032 Cross-Site Scripting (XSS) Attempt: NoScript XSS Filters Cross-Site Scripting (XSS) Attempt: NoScript XSS Filters, NoScript InjectionChecker - HTML injection
94117032 Cross-Site Scripting (XSS) Attempt: NoScript XSS Filters Cross-Site Scripting (XSS) Attempt: NoScript XSS Filters, NoScript InjectionChecker - Attributes injection
94118032 Cross-Site Scripting (XSS) Attempt: Blacklist Keywords from Node-Validator Cross-Site Scripting (XSS) Attempt: Blacklist Keywords from Node-Validator
94119032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94120032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94121032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94122032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94123032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94124032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94125032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94126032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94127032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94128032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94129032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94130032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94131032 Cross-Site Scripting (XSS) Attempt: US-ASCII encoding bypass listed on XSS filter evasion Cross-Site Scripting (XSS) Attempt: US-ASCII encoding bypass listed on XSS filter evasion
94132032 Cross-Site Scripting (XSS) Attempt: HTML Tag Handler Cross-Site Scripting (XSS) Attempt: HTML Tag Handler
94133032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94134032 Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer Cross-Site Scripting (XSS) Attempt: XSS Filters from IE
94135032 Cross-Site Scripting (XSS) Attempt: UTF-7 encoding XSS filter evasion for IE Cross-Site Scripting (XSS) Attempt: UTF-7 encoding XSS filter evasion for IE.
201710271 CVE-2017-10271 Oracle WebLogic Remote Code Execution in versions (10.3.6.0.0, 12.1.3.0.0, 12.2.1.1.0 and 12.2.1.2.0) Oracle WebLogic remote code execution in versions (10.3.6.0.0, 12.1.3.0.0, 12.2.1.1.0 and 12.2.1.2.0) - CVE-2017-10271
201821375 CVE-2012-0209, Remote Execution Backdoor Attempt Against Horde Remote Execution Backdoor Attempt Against Horde
201821438 CVE-2012-1723, CVE-2012-1889, CVE-2012-4681, Blackhole exploit kit JavaScript carat string splitting with hostile applet Blackhole exploit kit JavaScript carat string splitting with hostile applet
201822063 CVE-2012-1823, CVE-2012-2311, CVE-2012-2335, CVE-2012-2336, PHP-CGI remote file include attempt PHP-CGI remote file include attempt
201826834 CVE-2012-4681, CVE-2012-5076, CVE-2013-2423, Sweet Orange exploit kit landing page in.php base64 uri Sweet Orange exploit kit landing page in.php base64 uri
201826947 CVE-2013-2423, DotkaChef/Rmayana/DotCache exploit kit inbound java exploit download DotkaChef/Rmayana/DotCache exploit kit inbound java exploit download
201826948 CVE-2013-1493, DotkaChef/Rmayana/DotCache exploit kit inbound java exploit download DotkaChef/Rmayana/DotCache exploit kit inbound java exploit download
201827040 CVE-2013-0422, CVE-2013-2423, Styx exploit kit plugin detection connection jorg Styx exploit kit plugin detection connection jorg
201841409 CVE-2017-3823, CVE-2017-6753, Cisco WebEx explicit use of web plugin Cisco WebEx explicit use of web plugin
201843811 CVE-2017-9812, Kaspersky Linux File Server WMC directory traversal attempt Kaspersky Linux File Server WMC directory traversal attempt
201843812 CVE-2017-9812, Kaspersky Linux File Server WMC directory traversal attempt Kaspersky Linux File Server WMC directory traversal attempt
201843813 CVE-2017-9813, Kaspersky Linux File Server WMC cross site scripting attempt Kaspersky Linux File Server WMC cross site scripting attempt
201846316 CVE-2018-7600, CVE-2018-7602, Drupal 8 remote code execution attempt Drupal 8 remote code execution attempt
201846451 CVE-2018-7600, CVE-2018-7602, Drupal unsafe internal attribute remote code execution attempt Drupal unsafe internal attribute remote code execution attempt
201919781 CVE-2019-19781 Citrix Application Delivery Controller(ADC) Path Traversal Vulnerability SERVER-WEBAPP Citrix ADC NSC_USER directory traversal attempt. Versions (10.5, 11.1, 12.0, 12.1, and 13.0) - CVE-2019-19781
201939743 SERVER-WEBAPP Dell SonicWall GMS set_time_config XMLRPC method command injection attempt SERVER-WEBAPP Dell SonicWall GMS set_time_config XMLRPC method command injection attempt
201945493 SERVER-WEBAPP Seagate Personal Cloud getLogs.psp command injection attempt SERVER-WEBAPP Seagate Personal Cloud getLogs.psp command injection attempt
201945494 SERVER-WEBAPP Seagate Personal Cloud uploadTelemetry.psp command injection attempt SERVER-WEBAPP Seagate Personal Cloud uploadTelemetry.psp command injection attempt
201945495 SERVER-WEBAPP Seagate Personal Cloud getLogs.psp command injection attempt SERVER-WEBAPP Seagate Personal Cloud getLogs.psp command injection attempt
201945496 SERVER-WEBAPP Seagate Personal Cloud uploadTelemetry.psp command injection attempt SERVER-WEBAPP Seagate Personal Cloud uploadTelemetry.psp command injection attempt
201945526 SERVER-WEBAPP AsusWRT vpnupload.cgi unauthenticated NVRAM configuration modification attempt SERVER-WEBAPP AsusWRT vpnupload.cgi unauthenticated NVRAM configuration modification attempt
201945911 SERVER-WEBAPP ManageEngine Applications Manager testCredential.do command injection attempt SERVER-WEBAPP ManageEngine Applications Manager testCredential.do command injection attempt
201945912 SERVER-WEBAPP ManageEngine Applications Manager testCredential.do command injection attempt SERVER-WEBAPP ManageEngine Applications Manager testCredential.do command injection attempt
201945913 SERVER-WEBAPP ManageEngine Applications Manager testCredential.do command injection attempt SERVER-WEBAPP ManageEngine Applications Manager testCredential.do command injection attempt
201945984 SERVER-WEBAPP Joomla component Jimtawl 2.2.5 arbitrary PHP file upload attempt SERVER-WEBAPP Joomla component Jimtawl 2.2.5 arbitrary PHP file upload attempt
201946024 SERVER-WEBAPP multiple vendor calendar application id parameter SQL injection attempt SERVER-WEBAPP multiple vendor calendar application id parameter SQL injection attempt
201946025 SERVER-WEBAPP multiple vendor calendar application id parameter SQL injection attempt SERVER-WEBAPP multiple vendor calendar application id parameter SQL injection attempt
201946026 SERVER-WEBAPP EventManager page.php sql injection attempt SQL injection attempt SERVER-WEBAPP EventManager page.php sql injection attempt SQL injection attempt
201946027 SERVER-WEBAPP EventManager page.php sql injection attempt SQL injection attempt SERVER-WEBAPP EventManager page.php sql injection attempt SQL injection attempt
201946028 SERVER-WEBAPP Joomla JE PayperVideo extension SQL injection attempt SERVER-WEBAPP Joomla JE PayperVideo extension SQL injection attempt
201946029 SERVER-WEBAPP Joomla jextn-classifieds SQL injection attempt SERVER-WEBAPP Joomla jextn-classifieds SQL injection attempt
201946030 SERVER-WEBAPP Joomla jextn-classifieds SQL injection attempt SERVER-WEBAPP Joomla jextn-classifieds SQL injection attempt
201946041 SERVER-WEBAPP Joomla Component JMS Music 1.1.1 SQL injection attempt SERVER-WEBAPP Joomla Component JMS Music 1.1.1 SQL injection attempt
201946042 SERVER-WEBAPP Joomla Component JMS Music 1.1.1 SQL injection attempt SERVER-WEBAPP Joomla Component JMS Music 1.1.1 SQL injection attempt
201946043 SERVER-WEBAPP Joomla Component JMS Music 1.1.1 SQL injection attempt SERVER-WEBAPP Joomla Component JMS Music 1.1.1 SQL injection attempt
201946044 SERVER-WEBAPP Joomla Component JMS Music 1.1.1 SQL injection attempt SERVER-WEBAPP Joomla Component JMS Music 1.1.1 SQL injection attempt
201946045 SERVER-WEBAPP Joomla Component JMS Music 1.1.1 SQL injection attempt SERVER-WEBAPP Joomla Component JMS Music 1.1.1 SQL injection attempt
201946046 SERVER-WEBAPP Joomla Component JMS Music 1.1.1 SQL injection attempt SERVER-WEBAPP Joomla Component JMS Music 1.1.1 SQL injection attempt
201946062 SERVER-WEBAPP Joomla JEXTN Membership extension SQL injection attempt SERVER-WEBAPP Joomla JEXTN Membership extension SQL injection attempt
201946063 SERVER-WEBAPP Joomla JEXTN Membership extension SQL injection attempt SERVER-WEBAPP Joomla JEXTN Membership extension SQL injection attempt
201946064 SERVER-WEBAPP Joomla JEXTN Membership extension SQL injection attempt SERVER-WEBAPP Joomla JEXTN Membership extension SQL injection attempt
201946087 SERVER-WEBAPP Joomla JEXTN Reverse Auction extension SQL injection attempt SERVER-WEBAPP Joomla JEXTN Reverse Auction extension SQL injection attempt
201946088 SERVER-WEBAPP Joomla JEXTN Reverse Auction extension SQL injection attempt SERVER-WEBAPP Joomla JEXTN Reverse Auction extension SQL injection attempt
201946089 SERVER-WEBAPP Joomla JEXTN Reverse Auction extension SQL injection attempt SERVER-WEBAPP Joomla JEXTN Reverse Auction extension SQL injection attempt
201946303 SERVER-WEBAPP Antsle antman authentication bypass attempt SERVER-WEBAPP Antsle antman authentication bypass attempt
201946316 SERVER-WEBAPP Drupal 8 remote code execution attempt SERVER-WEBAPP Drupal 8 remote code execution attempt
201946333 SERVER-WEBAPP Joomla DT Register SQL injection attempt SERVER-WEBAPP Joomla DT Register SQL injection attempt
201946334 SERVER-WEBAPP Joomla DT Register SQL injection attempt SERVER-WEBAPP Joomla DT Register SQL injection attempt
201946337 SERVER-WEBAPP Joomla Saxum Picker SQL injection attempt SERVER-WEBAPP Joomla Saxum Picker SQL injection attempt
201946338 SERVER-WEBAPP Joomla Saxum Picker SQL injection attempt SERVER-WEBAPP Joomla Saxum Picker SQL injection attempt
201946451 SERVER-WEBAPP Drupal unsafe internal attribute remote code execution attempt SERVER-WEBAPP Drupal unsafe internal attribute remote code execution attempt
201946509 SERVER-WEBAPP Unitrends Enterprise Backup API command injection attempt SERVER-WEBAPP Unitrends Enterprise Backup API command injection attempt
201946510 SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt
201946511 SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt
201946512 SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt
201946513 SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt
201946514 SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt
201946515 SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt
201946516 SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt
201946517 SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt SERVER-WEBAPP Belkin N750 F9K1103 wireless router command injection attempt
201946624 SERVER-WEBAPP GPON Router authentication bypass and command injection attempt SERVER-WEBAPP GPON Router authentication bypass and command injection attempt
201946625 SERVER-WEBAPP GPON Router authentication bypass and command injection attempt SERVER-WEBAPP GPON Router authentication bypass and command injection attempt
201946626 SERVER-WEBAPP GPON Router authentication bypass and command injection attempt SERVER-WEBAPP GPON Router authentication bypass and command injection attempt
201946627 SERVER-WEBAPP GPON Router authentication bypass and command injection attempt SERVER-WEBAPP GPON Router authentication bypass and command injection attempt
201946665 SERVER-WEBAPP Digital Guardian Management Console arbitrary file upload attempt SERVER-WEBAPP Digital Guardian Management Console arbitrary file upload attempt
201946666 SERVER-WEBAPP Digital Guardian Management Console arbitrary file upload attempt SERVER-WEBAPP Digital Guardian Management Console arbitrary file upload attempt
201946773 SERVER-WEBAPP Nagios XI SQL injection attempt SERVER-WEBAPP Nagios XI SQL injection attempt
201946774 SERVER-WEBAPP NagiosXI SQL injection attempt SERVER-WEBAPP NagiosXI SQL injection attempt
201946775 SERVER-WEBAPP Nagios XI command injection attempt SERVER-WEBAPP Nagios XI command injection attempt
201946776 SERVER-WEBAPP Nagios XI command injection attempt SERVER-WEBAPP Nagios XI command injection attempt
201946777 SERVER-WEBAPP Nagios XI command injection attempt SERVER-WEBAPP Nagios XI command injection attempt
201946778 SERVER-WEBAPP Nagios XI command injection attempt SERVER-WEBAPP Nagios XI command injection attempt
201946779 SERVER-WEBAPP Nagios XI database settings modification attempt SERVER-WEBAPP Nagios XI database settings modification attempt
201946823 SERVER-WEBAPP Spring Security OAuth remote code execution attempt SERVER-WEBAPP Spring Security OAuth remote code execution attempt
201946828 SERVER-WEBAPP D-Link DIR-620 index.cgi command injection attempt SERVER-WEBAPP D-Link DIR-620 index.cgi command injection attempt
201946829 SERVER-WEBAPP D-Link DIR-620 index.cgi command injection attempt SERVER-WEBAPP D-Link DIR-620 index.cgi command injection attempt
201946849 SERVER-WEBAPP IBM QRadar SIEM command injection attempt SERVER-WEBAPP IBM QRadar SIEM command injection attempt
201946850 SERVER-WEBAPP IBM QRadar SIEM ForensicsAnalysisServlet authentication bypass attempt SERVER-WEBAPP IBM QRadar SIEM ForensicsAnalysisServlet authentication bypass attempt
201946851 SERVER-WEBAPP IBM QRadar SIEM command injection attempt SERVER-WEBAPP IBM QRadar SIEM command injection attempt
201946852 SERVER-WEBAPP IBM QRadar SIEM command injection attempt SERVER-WEBAPP IBM QRadar SIEM command injection attempt
201946886 SERVER-WEBAPP Quest KACE Systems Management Appliance ajax_email_connection_test.php command injection attempt SERVER-WEBAPP Quest KACE Systems Management Appliance ajax_email_connection_test.php command injection attempt
201946921 SERVER-WEBAPP Quest DR Series Disk Backup Login.pm command injection attempt SERVER-WEBAPP Quest DR Series Disk Backup Login.pm command injection attempt
201946997 SERVER-WEBAPP XiongMai NVR login.htm buffer overflow attempt SERVER-WEBAPP XiongMai NVR login.htm buffer overflow attempt
201947041 SERVER-WEBAPP Quest KACE Systems Management Appliance download_agent_installer.php command injection attempt SERVER-WEBAPP Quest KACE Systems Management Appliance download_agent_installer.php command injection attempt
201947042 SERVER-WEBAPP Quest KACE Systems Management Appliance download_agent_installer.php command injection attempt SERVER-WEBAPP Quest KACE Systems Management Appliance download_agent_installer.php command injection attempt
201947348 SERVER-WEBAPP QNAP QCenter API set_VM_passwd command injection attempt SERVER-WEBAPP QNAP QCenter API set_VM_passwd command injection attempt
201947349 SERVER-WEBAPP QNAP QCenter API set_VM_passwd command injection attempt SERVER-WEBAPP QNAP QCenter API set_VM_passwd command injection attempt
201947386 SERVER-WEBAPP Oracle WebLogic Server unauthenticated modified JSP access attempt SERVER-WEBAPP Oracle WebLogic Server unauthenticated modified JSP access attempt
201947387 SERVER-WEBAPP Oracle WebLogic Server potential unauthenticated reconnaissance attempt SERVER-WEBAPP Oracle WebLogic Server potential unauthenticated reconnaissance attempt
201947388 SERVER-WEBAPP Oracle WebLogic Server potential precursor to keystore attack attempt SERVER-WEBAPP Oracle WebLogic Server potential precursor to keystore attack attempt
201947389 SERVER-WEBAPP Oracle WebLogic Server arbitrary JSP file upload attempt SERVER-WEBAPP Oracle WebLogic Server arbitrary JSP file upload attempt
201947390 SERVER-WEBAPP Oracle WebLogic Server arbitrary JSP file upload attempt SERVER-WEBAPP Oracle WebLogic Server arbitrary JSP file upload attempt
201947391 SERVER-WEBAPP QNAP QCenter API set_VM_network command injection attempt SERVER-WEBAPP QNAP QCenter API set_VM_network command injection attempt
201947392 SERVER-WEBAPP QNAP QCenter API set_VM_network command injection attempt SERVER-WEBAPP QNAP QCenter API set_VM_network command injection attempt
201947393 SERVER-WEBAPP QNAP QCenter API command injection attempt SERVER-WEBAPP QNAP QCenter API command injection attempt
201947423 SERVER-WEBAPP QNAP QCenter API date_config command injection attempt SERVER-WEBAPP QNAP QCenter API date_config command injection attempt
201947497 SERVER-WEBAPP Joomla CheckList extension SQL injection attempt SERVER-WEBAPP Joomla CheckList extension SQL injection attempt
201947498 SERVER-WEBAPP Joomla CheckList extension SQL injection attempt SERVER-WEBAPP Joomla CheckList extension SQL injection attempt
201947501 SERVER-WEBAPP Joomla ProjectLog search SQL injection attempt SERVER-WEBAPP Joomla ProjectLog search SQL injection attempt
201947502 SERVER-WEBAPP Joomla ProjectLog search SQL injection attempt SERVER-WEBAPP Joomla ProjectLog search SQL injection attempt
201947506 SERVER-WEBAPP Sitecore CMS default.aspx directory traversal attempt SERVER-WEBAPP Sitecore CMS default.aspx directory traversal attempt
201947507 SERVER-WEBAPP Sitecore CMS default.aspx directory traversal attempt SERVER-WEBAPP Sitecore CMS default.aspx directory traversal attempt
201947508 SERVER-WEBAPP Sitecore CMS default.aspx directory traversal attempt SERVER-WEBAPP Sitecore CMS default.aspx directory traversal attempt
201947514 SERVER-WEBAPP Quest NetVault Backup Server checksession authentication bypass attempt SERVER-WEBAPP Quest NetVault Backup Server checksession authentication bypass attempt
201947543 SERVER-WEBAPP MicroFocus Secure Messaging Gateway enginelist.php SQL injection attempt SERVER-WEBAPP MicroFocus Secure Messaging Gateway enginelist.php SQL injection attempt
201947544 SERVER-WEBAPP MicroFocus Secure Messaging Gateway enginelist.php SQL injection attempt SERVER-WEBAPP MicroFocus Secure Messaging Gateway enginelist.php SQL injection attempt
201947545 SERVER-WEBAPP MicroFocus Secure Messaging Gateway command injection attempt SERVER-WEBAPP MicroFocus Secure Messaging Gateway command injection attempt
201947576 SERVER-WEBAPP Cobub Razor channel name SQL injection attempt SERVER-WEBAPP Cobub Razor channel name SQL injection attempt
201947577 SERVER-WEBAPP Cobub Razor channel name SQL injection attempt SERVER-WEBAPP Cobub Razor channel name SQL injection attempt
201947579 SERVER-WEBAPP Joomla Aist id SQL injection attempt SERVER-WEBAPP Joomla Aist id SQL injection attempt
201947580 SERVER-WEBAPP Joomla Aist id SQL injection attempt SERVER-WEBAPP Joomla Aist id SQL injection attempt
201947581 SERVER-WEBAPP GitStack unauthenticated REST API add user attempt SERVER-WEBAPP GitStack unauthenticated REST API add user attempt
201947582 SERVER-WEBAPP GitStack unauthenticated REST API repository modification attempt SERVER-WEBAPP GitStack unauthenticated REST API repository modification attempt
201947583 SERVER-WEBAPP GitStack unauthenticated REST API repository modification attempt SERVER-WEBAPP GitStack unauthenticated REST API repository modification attempt
201947649 SERVER-WEBAPP Apache Struts remote code execution attempt SERVER-WEBAPP Apache Struts remote code execution attempt
201947655 SERVER-WEBAPP Joomla PostInstall Message SQL injection attempt SERVER-WEBAPP Joomla PostInstall Message SQL injection attempt
201947672 SERVER-WEBAPP TerraMaster NAS logtable.php command injection attempt SERVER-WEBAPP TerraMaster NAS logtable.php command injection attempt
201947767 SERVER-WEBAPP ClipBucket file_uploader command injection attempt SERVER-WEBAPP ClipBucket file_uploader command injection attempt
201947768 SERVER-WEBAPP ClipBucket beats_uploader arbitrary PHP file upload attempt SERVER-WEBAPP ClipBucket beats_uploader arbitrary PHP file upload attempt
201947769 SERVER-WEBAPP ClipBucket photo_uploader arbitrary PHP file upload attempt SERVER-WEBAPP ClipBucket photo_uploader arbitrary PHP file upload attempt
201947770 SERVER-WEBAPP ClipBucket edit_account arbitrary PHP file upload attempt SERVER-WEBAPP ClipBucket edit_account arbitrary PHP file upload attempt
201947771 SERVER-WEBAPP ClipBucket vote_channel SQL injection attempt SERVER-WEBAPP ClipBucket vote_channel SQL injection attempt
201947772 SERVER-WEBAPP ClipBucket commonAjax SQL injection attempt SERVER-WEBAPP ClipBucket commonAjax SQL injection attempt
201947794 SERVER-WEBAPP Trend Micro Email Encryption Gateway SQL injection attempt SERVER-WEBAPP Trend Micro Email Encryption Gateway SQL injection attempt
201947795 SERVER-WEBAPP Trend Micro Email Encryption Gateway SQL injection attempt SERVER-WEBAPP Trend Micro Email Encryption Gateway SQL injection attempt
201947796 SERVER-WEBAPP Trend Micro Email Encryption Gateway SQL injection attempt SERVER-WEBAPP Trend Micro Email Encryption Gateway SQL injection attempt
201947797 SERVER-WEBAPP Trend Micro Email Encryption Gateway SQL injection attempt SERVER-WEBAPP Trend Micro Email Encryption Gateway SQL injection attempt
201947799 SERVER-WEBAPP Trend Micro Email Encryption Gateway SQL injection attempt SERVER-WEBAPP Trend Micro Email Encryption Gateway SQL injection attempt
201947800 SERVER-WEBAPP Trend Micro Email Encryption Gateway SQL injection attempt SERVER-WEBAPP Trend Micro Email Encryption Gateway SQL injection attempt
201947817 SERVER-WEBAPP SoftNAS StorageCenter snserv.php command injection attempt SERVER-WEBAPP SoftNAS StorageCenter snserv.php command injection attempt
201947818 SERVER-WEBAPP SoftNAS StorageCenter snserv.php command injection attempt SERVER-WEBAPP SoftNAS StorageCenter snserv.php command injection attempt
201947819 SERVER-WEBAPP SoftNAS StorageCenter snserv.php command injection attempt SERVER-WEBAPP SoftNAS StorageCenter snserv.php command injection attempt
201947858 SERVER-WEBAPP Joomla CW Tags Searchtext SQL injection attempt SERVER-WEBAPP Joomla CW Tags Searchtext SQL injection attempt
201947859 SERVER-WEBAPP Joomla CW Tags Searchtext SQL injection attempt SERVER-WEBAPP Joomla CW Tags Searchtext SQL injection attempt
201947861 SERVER-WEBAPP Opsview Web Management Console testnotification command injection attempt SERVER-WEBAPP Opsview Web Management Console testnotification command injection attempt
201947863 SERVER-WEBAPP Opsview Web Management Console test_rancid_connection command injection attempt SERVER-WEBAPP Opsview Web Management Console test_rancid_connection command injection attempt
201947864 SERVER-WEBAPP Opsview Web Management Console test_rancid_connection command injection attempt SERVER-WEBAPP Opsview Web Management Console test_rancid_connection command injection attempt
201947865 SERVER-WEBAPP Opsview Web Management Console test_rancid_connection command injection attempt SERVER-WEBAPP Opsview Web Management Console test_rancid_connection command injection attempt
201948004 SERVER-WEBAPP Navigate CMS login.php SQL injection attempt SERVER-WEBAPP Navigate CMS login.php SQL injection attempt
201948061 SERVER-WEBAPP pfSense status_interfaces.php command injection attempt SERVER-WEBAPP pfSense status_interfaces.php command injection attempt
201948070 SERVER-WEBAPP WP plugin Wechat Broadcast directory traversal attempt SERVER-WEBAPP WP plugin Wechat Broadcast directory traversal attempt
201948071 SERVER-WEBAPP WP plugin Wechat Broadcast remote file inclusion attempt SERVER-WEBAPP WP plugin Wechat Broadcast remote file inclusion attempt
201948097 SERVER-WEBAPP D-Link DIR-816 syslogIp command injection attempt SERVER-WEBAPP D-Link DIR-816 syslogIp command injection attempt
201948098 SERVER-WEBAPP D-Link DIR-816 syslogIp command injection attempt SERVER-WEBAPP D-Link DIR-816 syslogIp command injection attempt
201948099 SERVER-WEBAPP D-Link DIR-816 syslogIp command injection attempt SERVER-WEBAPP D-Link DIR-816 syslogIp command injection attempt
201948126 SERVER-WEBAPP Joomba component Timetable Schedule 3.6.8 SQL injection attempt SERVER-WEBAPP Joomba component Timetable Schedule 3.6.8 SQL injection attempt
201948141 SERVER-WEBAPP D-Link DIR-816 diagnosis command injection attempt SERVER-WEBAPP D-Link DIR-816 diagnosis command injection attempt
201948142 SERVER-WEBAPP D-Link DIR-816 diagnosis command injection attempt SERVER-WEBAPP D-Link DIR-816 diagnosis command injection attempt
201948143 SERVER-WEBAPP D-Link DIR-816 diagnosis command injection attempt SERVER-WEBAPP D-Link DIR-816 diagnosis command injection attempt
201948161 SERVER-WEBAPP Joomba component Article Factory Manager SQL injection attempt SERVER-WEBAPP Joomba component Article Factory Manager SQL injection attempt
201948165 SERVER-WEBAPP Joomla Component Swap Factory SQL injection attempt SERVER-WEBAPP Joomla Component Swap Factory SQL injection attempt
201948166 SERVER-WEBAPP Joomla Component Swap Factory SQL injection attempt SERVER-WEBAPP Joomla Component Swap Factory SQL injection attempt
201948172 SERVER-WEBAPP D-Link DIR-816 form2systime.cgi command injection attempt SERVER-WEBAPP D-Link DIR-816 form2systime.cgi command injection attempt
201948173 SERVER-WEBAPP D-Link DIR-816 form2systime.cgi command injection attempt SERVER-WEBAPP D-Link DIR-816 form2systime.cgi command injection attempt
201948174 SERVER-WEBAPP D-Link DIR-816 form2systime.cgi command injection attempt SERVER-WEBAPP D-Link DIR-816 form2systime.cgi command injection attempt
201948193 SERVER-WEBAPP Joomba component AlphaIndex Dictionaries SQL injection attempt SERVER-WEBAPP Joomba component AlphaIndex Dictionaries SQL injection attempt
201948194 SERVER-WEBAPP Joomba component AlphaIndex Dictionaries SQL injection attempt SERVER-WEBAPP Joomba component AlphaIndex Dictionaries SQL injection attempt
201948195 SERVER-WEBAPP Joomla Component Collection Factory SQL injection attempt SERVER-WEBAPP Joomla Component Collection Factory SQL injection attempt
201948196 SERVER-WEBAPP Joomla component Reverse Auction Factory SQL injection attempt SERVER-WEBAPP Joomla component Reverse Auction Factory SQL injection attempt
201948256 SERVER-WEBAPP Rubedo CMS Directory Traversal Attempt directory traversal attempt SERVER-WEBAPP Rubedo CMS Directory Traversal Attempt directory traversal attempt
201948263 SERVER-WEBAPP Blueimp jQuery File Upload arbitrary PHP file upload attempt SERVER-WEBAPP Blueimp jQuery File Upload arbitrary PHP file upload attempt
201948266 SERVER-WEBAPP Teltonika RUT9XX autologin.cgi command injection attempt SERVER-WEBAPP Teltonika RUT9XX autologin.cgi command injection attempt
201948267 SERVER-WEBAPP Teltonika RUT9XX autologin.cgi command injection attempt SERVER-WEBAPP Teltonika RUT9XX autologin.cgi command injection attempt
201948268 SERVER-WEBAPP Teltonika RUT9XX hotspotlogin.cgi command injection attempt SERVER-WEBAPP Teltonika RUT9XX hotspotlogin.cgi command injection attempt
201948269 SERVER-WEBAPP Teltonika RUT9XX hotspotlogin.cgi command injection attempt SERVER-WEBAPP Teltonika RUT9XX hotspotlogin.cgi command injection attempt
201948270 SERVER-WEBAPP Teltonika RUT9XX autologin.cgi command injection attempt SERVER-WEBAPP Teltonika RUT9XX autologin.cgi command injection attempt
201948271 SERVER-WEBAPP Teltonika RUT9XX hotspotlogin.cgi command injection attempt SERVER-WEBAPP Teltonika RUT9XX hotspotlogin.cgi command injection attempt
201948273 SERVER-WEBAPP Cockpit CMS media API directory traversal attempt SERVER-WEBAPP Cockpit CMS media API directory traversal attempt
201948274 SERVER-WEBAPP Cockpit CMS media API directory traversal attempt SERVER-WEBAPP Cockpit CMS media API directory traversal attempt
201948413 SERVER-WEBAPP ManageEngine Applications Manager editDisplaynames.do SQL injection attempt SERVER-WEBAPP ManageEngine Applications Manager editDisplaynames.do SQL injection attempt
201948414 SERVER-WEBAPP ManageEngine Applications Manager editDisplaynames.do SQL injection attempt SERVER-WEBAPP ManageEngine Applications Manager editDisplaynames.do SQL injection attempt
201948415 SERVER-WEBAPP ManageEngine Applications Manager editDisplaynames.do SQL injection attempt SERVER-WEBAPP ManageEngine Applications Manager editDisplaynames.do SQL injection attempt
201948443 SERVER-WEBAPP Nagios XI magpie_debug.php command argument injection attempt SERVER-WEBAPP Nagios XI magpie_debug.php command argument injection attempt
201948744 SERVER-WEBAPP TRENDnet TEW-673GRU apply.cgi start_arpping command injection attempt SERVER-WEBAPP TRENDnet TEW-673GRU apply.cgi start_arpping command injection attempt
201948815 SERVER-WEBAPP Kibana Console for Elasticsearch local file inclusion attempt SERVER-WEBAPP Kibana Console for Elasticsearch local file inclusion attempt
201948837 SERVER-WEBAPP ThinkPHP 5.0.23/5.1.31 command injection attempt SERVER-WEBAPP ThinkPHP 5.0.23/5.1.31 command injection attempt
201948839 SERVER-WEBAPP Wifi-Soft Unibox diagnostic_tools_controller.php command injection attempt SERVER-WEBAPP Wifi-Soft Unibox diagnostic_tools_controller.php command injection attempt
201948840 SERVER-WEBAPP Wifi-Soft Unibox diagnostic_tools_controller.php command injection attempt SERVER-WEBAPP Wifi-Soft Unibox diagnostic_tools_controller.php command injection attempt
201948843 SERVER-WEBAPP Wifi-Soft Unibox ping.php command injection attempt SERVER-WEBAPP Wifi-Soft Unibox ping.php command injection attempt
201949498 SERVER-WEBAPP Jenkins Groovy metaprogramming remote code execution attempt SERVER-WEBAPP Jenkins Groovy metaprogramming remote code execution attempt
201949499 SERVER-WEBAPP Jenkins Groovy metaprogramming remote code execution attempt SERVER-WEBAPP Jenkins Groovy metaprogramming remote code execution attempt
201949537 SERVER-WEBAPP elFinder PHP connector arbitrary PHP file upload attempt SERVER-WEBAPP elFinder PHP connector arbitrary PHP file upload attempt
201949645 SERVER-WEBAPP Wordpress image edit directory traversal attempt SERVER-WEBAPP Wordpress image edit directory traversal attempt
201949646 SERVER-WEBAPP Wordpress image edit directory traversal attempt SERVER-WEBAPP Wordpress image edit directory traversal attempt
201949647 SERVER-WEBAPP Wordpress image edit directory traversal attempt SERVER-WEBAPP Wordpress image edit directory traversal attempt
201949714 SERVER-WEBAPP Horde Groupware Webmail Contact Management add.php arbitrary PHP file upload attempt SERVER-WEBAPP Horde Groupware Webmail Contact Management add.php arbitrary PHP file upload attempt
201949861 SERVER-WEBAPP Microsoft SharePoint EntityInstanceIdEncoder remote code execution attempt SERVER-WEBAPP Microsoft SharePoint EntityInstanceIdEncoder remote code execution attempt
201950168 SERVER-WEBAPP Atlassian Confluence Data Center and Server directory traversal attempt SERVER-WEBAPP Atlassian Confluence Data Center and Server directory traversal attempt
201950170 SERVER-WEBAPP Atlassian Confluence Data Center and Server directory traversal attempt SERVER-WEBAPP Atlassian Confluence Data Center and Server directory traversal attempt
201950275 SERVER-WEBAPP Microsoft SharePoint EntityInstanceIdEncoder remote code execution attempt SERVER-WEBAPP Microsoft SharePoint EntityInstanceIdEncoder remote code execution attempt
201950323 SERVER-WEBAPP Crestron AM platform command injection attempt SERVER-WEBAPP Crestron AM platform command injection attempt
201950324 SERVER-WEBAPP Crestron AM platform command injection attempt SERVER-WEBAPP Crestron AM platform command injection attempt
201950708 SERVER-WEBAPP WordPress Rencontre plugin cross site scripting attempt SERVER-WEBAPP WordPress Rencontre plugin cross site scripting attempt
201950709 SERVER-WEBAPP WordPress Rencontre plugin SQL injection attempt SERVER-WEBAPP WordPress Rencontre plugin SQL injection attempt
201950711 SERVER-WEBAPP WordPress Rencontre plugin SQL injection attempt SERVER-WEBAPP WordPress Rencontre plugin SQL injection attempt
201950732 SERVER-WEBAPP CyberArk Enterprise Password Vault XML external entity injection attempt SERVER-WEBAPP CyberArk Enterprise Password Vault XML external entity injection attempt
2019000513 JavaScript Object Notation (JSON) - Failed to parse Request Body JSON Failed to parse Request Body
2019272501, 2019272502, 2019272503, 2019272504 CVE-2019-2725 and CVE-2019-2729 Oracle WebLogic Remote Code Execution in versions (10.3.6.0.0, 12.1.3.0.0, 12.2.1.3.0) Oracle WebLogic remote code execution in versions (10.3.6.0.0, 12.1.3.0.0, 12.2.1.3.0) - CVE-2019-2725 - CVE-2019-2729
2025497061 CVE-2025-49706 Sharepoint High-fidelity detection for ToolPane auth bypass for CVE-2025-49706.
2025497062 CVE-2025-49706 Sharepoint High-fidelity detection for ToolPane Exploit Parameter Detection for CVE-2025-49706.
2025497063 CVE-2025-49706 Sharepoint High-fidelity detection for Malicious Web Shell Upload for CVE-2025-49706.
2025497064 CVE-2025-49706 Sharepoint High-fidelity detection for Post-Compromise - Access to Shells for CVE-2025-49706.
202553771 Microsoft SharePoint ToolShell Authentication Bypass (CVE-2025-53771) Detection of ToolShell Auth Bypass via ToolPane.aspx and spoofed SignOut.aspx Referer
