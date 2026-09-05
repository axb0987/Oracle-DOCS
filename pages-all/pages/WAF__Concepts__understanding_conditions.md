# Understanding Conditions
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/understanding_conditions.htm
- Fetched: 2026-09-05 03:10 CDT

# Understanding Conditions

Understand and compose conditions for rules associated with WAF policies.

WAF uses the JMESPath language as a rule condition language. JMESPath is a query language for JSON (see[https://jmespath.org/specification.html](https://jmespath.org/specification.html)[JMESPath selectors](https://jmespath.org/specification.html)) that you can use to write JMESPath expressions, where each expression takes a JSON document as an input (the input document) and returns a transformed or new JSON document (the output document).

In WAF, each rule accepts a JMESPath expression as the condition. HTTP requests or HTTP responses (depending on the type of rule) trigger WAF rules. When evaluating a rule, the WAF service evaluates the JMESPath expression (the condition) of the rule and provides an input JSON document, which includes the details of the HTTP request or HTTP response that triggered the evaluation. Then, the result of the evaluated JMESPath expression is used to determine whether or not to run the action specified in the rule.

The return value of JMESPath conditions in WAF is converted to a boolean value. The following values are converted to "false":

- Empty list: []
- Empty object: {}
- Empty string: ""
- False boolean: false
- Null value: null All other values are converted to "true." True means that the action of a rule is run and false means that the action isn't run.

You can create a JMESPath condition with up to 1,024 characters.

Example

URL path conditions
```

```

HTTP request method conditions
```

```

HTTP request header conditions
```

```

Multiple conditions
```

```

## Input JSON Document Structure

When evaluating JMESPath expressions, WAF provides an input JSON document, which includes the details of the HTTP request or HTTP response that triggered the evaluation. The input JSON document is always a JSON object.

Example

For an HTTP request with the following details:
- 

Source IP address and port: 129.146.10.1:48152
- 

Country code that the source IP address belongs to: US
- 

ASN that the source IP address belongs to: 31898
- 

Destination IP address and port: 205.147.88.0:80
- 

Destination host: example.com
- 

Protocol: HTTP/1.1
```

```

The following JSON input document is generated and passed to JMESPath expressions:
```

```

Reference

connection.source.address

Category

Value

Type

string

Description

A string containing the TCP source IP address. IPv6 addresses are represented in their canonical form, according to[RFC 5952](https://datatracker.ietf.org/doc/html/rfc5952).

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

"10.0.0.1", "1.2.3.4"

connection.source.port

Category

Value

Type

number

Description

TCP source port

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

49152

connection.source.geo.countryCode

Category

Value

Type

string | null

Description

ISO 3166-1 alpha-2 country code of the country, which the source IP address belongs to. Can be null when the country isn't known.

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

"US"

connection.source.routing.asn

Category

Value

Type

number | null

Description

The ASN (autonomous system number) to which the source IP address belongs to. Can be null when the IP address is private.

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

2122, 1278

connection.destination.address

Category

Value

Type

string

Description

A string containing the TCP destination IP address.

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

"10.0.0.1"

connection.destination.port

Category

Value

Type

number

Description

TCP destination port

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

80

connection.protocol

Category

Value

Type

string

Description

The protocol of the connection, either "http" or "https."

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

"https"

http.request.host

Category

Value

Type

string

Description

The value of the HTTP request "Host" header. The "Host" request header specifies the host and port number of the server to which the request is being sent.

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

"http://www.example.com", "api.example.com:8080"

http.request.method

Category

Value

Type

string

Description

The HTTP request method

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

"GET", "POST"

http.request.version

Category

Value

Type

string

Description

HTTP protocol version

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

"1.1", "2.0"

http.request.url.path

Category

Value

Type

string

Description

The absolute path part of the HTTP request target. Doesn't include the query part. Always starts with a "/".

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

"/api/v1", "/index.html", "/"

http.request.url.query

Category

Value

Type

string

Description

The query parameters of the HTTP request target, without the prefix.

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

"foo=bar&amp;multi=1&amp;multi=2", "multi=one&amp;multi=two&amp;multi=3&amp;encoded=two%20words", ""

http.request.url.queryParameters

Category

Value

Type

object

Description

The query part of the HTTP request target, parsed into an object structure, where:
- 

Key: the name of a query parameter.
- 

Value: list of values with the "key" as their name.

Keys and values are unescaped according to URL escaping rules.

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

Query part of the HTTP request target

Parsed object structure

?param1=a&amp;param2=b&amp;param3=c
```

```

?multi=one&amp;multi=two&amp;multi=3&amp;encoded+key=two%20words
```

```

http.request.url.queryParameters

Category

Value

Type

string

Description

The query prefix of the HTTP request target.

If a query string is present, it is always "?".

If no query string is present, it contains an empty string.

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

"?", ""

http.request.headers

Category

Value

Type

object

Description

The HTTP request headers parsed into an object structure, where:
- 

Key: name of the header converted to lower case.
- 

Value: list of header values with the "key" as their name.

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

Raw HTTP request headers

Parsed object structure

```

```

```

```

http.request.cookies

Category

Value

Type

object

Description

The HTTP cookies that were passed using the "Cookie" HTTP request header, parsed into an object structure, where:
- 

Key: name of the cookie.
- 

Value: list of cookie values with the "key" as their name.

Available in

requestAccessControl, requestRateLimiting, requestProtection, responseAccessControl, responseProtection
Example values

Value of the HTTP request header "Cookie"

Parsed object structure

```

```

```

```

http.response.code

Category

Value

Type

number

Description

HTTP response code

Available in

responseAccessControl, responseProtection
Example values

200

http.response.headers

Category

Value

Type

object

Description

The HTTP response headers parsed into an object structure, where:
- 

Key: name of the header converted to lower case.
- 

Value: list of header values with the "key" as their name.

Available in

responseAccessControl, responseProtection
Example values

Raw HTTP response headers

Parsed object structure

```

```

```

```

## Case-Insensitive String Matching

In addition to string matching functions supported by default in JMESPath, WAF adds support for four functions that can match strings case-insensitively:
- i_equals (case-insensitive variant of the == operator);
- i_contains (case-insensitive variant of the contains function);
- i_starts_with (case-insensitive variant of the starts_with function);
- i_ends_with (case-insensitive variant of the ends_with function).

## i_equals

```

```
Returns true if strings $left and $right are equal, when compared case-insensitively (both $left and $right strings are converted to lower case, only English letters are converted to lower case). Otherwise, returns false.

Given Expression Result
"string" i_equals(@, 'string') true
"string" i_equals(@, 'STRING') true
"string" i_equals(@, 'sTrInG') true
"STRING" i_equals(@, 'string') true
"string" i_equals(@, 'other_string') false

## i_contains

```

```
Case-insensitive variant of the contains function.

If the provided $subject is a string, this function returns true if the string contains the provided $search argument, when compared case-insensitively (both $left and $right strings are converted to lower case, only English letters are converted to lower case). Otherwise, this function returns false.

If $subject is an array, this function returns true if at least one of the elements in the array is equal to the provided $search value, otherwise it returns false.

If $search is a string - comparison is done using the same logic as in i_equals() function: case-insensitive comparison (both the individual $subject array element and $search strings are converted to lower case, only English letters are converted to lower case).

If $search isn't a string - comparison is done using the standard == operator.

Given Expression Result
"foobarbaz" i_contains(@, 'bar') true
"foobarbaz" i_contains(@, 'BAR') true
"foobarbaz" i_contains(@, 'bAr') true
"foobarbaz" i_contains(@, 'foo') false
["a", "b"] i_contains(@, `a`) true
["foo", "bar"] i_contains(@, `b`) false
["foo", "bar"] i_contains(@, `BAR`) true

## i_starts_with

```

```
Returns true if the $subject starts with the $prefix, when compared case-insensitively (both $left and $right strings are converted to lower case, only English letters are converted to lower case). Otherwise, this function returns false.

Given Expression Result
"foobarbaz" i_starts_with(@, 'foo') true
"foobarbaz" i_starts_with(@, 'FOO') true
"foobarbaz" i_starts_with(@, 'fOo') true
"foobarbaz" i_starts_with(@, 'bar') false

## i_ends_with

```

```
Returns true if the $subject ends with the $suffix, when compared case-insensitively (both $left and $right strings are converted to lower case, only English letters are converted to lower case). Otherwise, this function returns false.

Given Expression Result
"foobarbaz" i_ends_with(@, 'baz') true
"foobarbaz" i_ends_with(@, 'BAZ') true
"foobarbaz" i_ends_with(@, 'bAz') true
"foobarbaz" i_ends_with(@, 'bar') false

## IP Address Matching

WAF adds support for multiple functions that can match an IP address against a list of CIDR ranges or WAF Network Address List resources:
- 

address_in (matches an IP address against a list of CIDR ranges);
- 

address_in_network_address_list (matches an IP address against a WAF Network Address List resource);
- 

vcn_address_in_network_address_list (matches an IP address with a VCN ID against a WAF Network Address List resource).

## address_in
```

```

Returns true if the given $ip_address is contained in at least one of the CIDR subnets specified in $cidr_subnets. Otherwise, returns false.

$ip_address must be a string containing an IP address.

$cidr_subnets must be an array of strings containing one CIDR subnet each.

Given Expression Result

```

```
address_in(connection.source.address, ['1.1.0.0/16', '2.2.0.0/16']) true
address_in(connection.source.address, ['3.3.0.0/16']) false

## address_in_network_address_list

```

```
Returns true if the given $ip_address is contained in at least one of the provided Network Address Lists (a WAF resource containing a list of CIDR subnets). Otherwise, returns false.

$ip_address must be a string containing an IP address.

$nal_id arguments must be an array of strings, referencing WAF NetworkAddressList resources by ID. All referenced NetworkAddressLists must be of type: "ADDRESSES".

Example 1

Item Details
Given input
```

```

Given NALs

ocid1.webappfirewallnetworkaddresslist...a:
- 1.1.0.0/16
- 2.2.0.0/16
Expression address_in_network_address_list(connection.source.address, ['ocid1.webappfirewallnetworkaddresslist...a'])
Result true Example 2

Item Details
Given input
```

```

Given NALs

ocid1.webappfirewallnetworkaddresslist...a:
- 1.1.0.0/16
- 2.2.0.0/16

ocid1.webappfirewallnetworkaddresslist...b:
- 3.3.0.0/16
Expression address_in_network_address_list(connection.source.address, ['ocid1.webappfirewallnetworkaddresslist...b'])
Result false

## vcn_address_in_network_address_list

```

```
Returns true if the given $ip_address in VCN $vcn_id is contained in at least one of the provided Network Address Lists (a WAF resource containing a list of CIDR subnets). Otherwise, returns false.

$ip_address must be a string containing an IP address.

$vcn_id must be a string containing an OCID of a VCN.

$nal_ids must be an array of strings, referencing WAF NetworkAddressList resources by ID. All referenced NetworkAddressLists must be of type: "VCN_ADDRESSES". Example 1

Item Details
Given input
```

```

Given NALs

ocid1.webappfirewallnetworkaddresslist...a:
- 10.0.0.0/16 in ocid1.vcn...a
- 10.1.0.0/16 in ocid1.vcn...b
Expression
```

```

Result

true Example 2

Item Details
Given input
```

```

Given NALs

ocid1.webappfirewallnetworkaddresslist...b:
- 10.0.0.0/16 in ocid1.vcn...c
Expression vcn_address_in_network_address_list( connection.source.address, connection.paResource.vcnOcid, ['ocid1.webappfirewallnetworkaddresslist...b'] )
