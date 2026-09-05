# Routing Policy Language for Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/routing_policy_conditions.htm
- Fetched: 2026-09-05 01:40 CDT

# Routing Policy Language for Load Balancers

Learn how to write routing policy condition statements that guide a load balancer's routing behavior.

To control how incoming requests to resources like web servers are routed, you must create policies. These policies take a general form of "If this, then forward traffic to a backend set." The backend set must be one you have already created.

Routing policies work in the following ways:
- Each HTTP request is evaluated against the rules.
- The rules are run in the order that's defined in the policy.
- Each rule has at least one condition and a backend set.
- If the HTTP request condition matches a rule, the request is forwarded to the backend set defined for the rule. The other rules in the policy are skipped and the request isn't evaluated against them.
- Only the action`FORWARD_TO_BACKENDSET`is used in routing policies.

## Example: One Path Rule

Here's an example of a routing policy rule set that contains only one path-based rule:
```

```

This example shows the following elements:
- 

The rule set is enclosed in curly brackets`{ }`and contains a name for the rule set, the language version number, and a name for the set of rules.
- 

The rule set name in the example is`"BasicPathBasedPolicy"`. Rules in the set are contained inside square brackets.
- 

The sole rule in the set is named`"Documents_rule"`.
- 

The condition for the rule says that if`any`of the conditions are met, then perform the action in`"actions"`.
- 

The condition compares the incoming HTTP request URL path with`/documents`. The comparison is`eq`meaning equals, which could also be written as`=`.
- 

In the condition statement`(i '/documents')`declares that`'/documents'`is case-insensitive.
- 

When the condition is met, the action taken is to forward the request to a specific backend set, in this case "backendSetForDocuments." This backend set must exist for the rule to be valid.

The rule can be paraphrased as "If the requested URL path is an exact match for`/documents`then forward the request to the backend set`backendSetForDocuments`.

## Example: Two Simple Path Rules

Here's an example of a routing policy rule set that contains two simple path-based rules. An incoming query is sent to a different backend set based on the request URL path, and forwarding happens if either the first condition or the second condition is met. Multiple rules are evaluated in their order in the policy. If a query happens to match both of these conditions, the action is performed on the first one matched and the second match is skipped.
```

```

## Example: One Rule with Two Conditions

The next policy has one rule with two conditions (each condition is separated by a comma). The first condition examines the request headers, and the second condition examines the request's query string:
```

```

The rule now requires that two conditions are both true to forward a request to a backend set, since it begins with the all keyword. The conditions for the rule can be paraphrased as "If the requested user-agent value in the header is set to mobile and the department value in the header is HR , then forward to the specified backend set.

## Example: Two Rules

The final example shows two rules. Each rule has a different action, and both rules have two conditions. Importantly, the second rule begins with the keyword any , meaning that only one of the two conditions needs to be true to trigger the action. If more than two conditions specified, if any one of them is true the action is triggered.
```

```

## Rule Conditions

The rule conditions are written in the form of predicates. Multiple predicates can be used in one condition, using combinators. The two combinators:`any()`and`all()`behave like a logical OR or AND. A combinator can also be negated by putting the keyword not before it. A simple predicate can be expressed as:
```

```

A condition for a rule that must match if the HTTP request URL path starts with`/foo/bar`would be:
```

```

More details about the available matchers are in[Matchers](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/routing_policy_conditions.htm#routing_policy_conditions_matchers).

More details about the available variables are in[Variables](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/routing_policy_conditions.htm#routing_policy_conditions_variables).

Syntax for multiple predicates
```

```

For example:
```

```

### Condition Examples

Here are more examples of how conditions can be used. Here are more details on the exact syntax and functionality.
- To match an HTTP request if its URL path starts with`/category/element`:
```

```

- To match an HTTP request if its URL path starts with`/category`or ends with`/id`:
```

```

- To match an HTTP request if a`User-Agent`request header is present:
```

```

- To match an HTTP request if the header`User-Agent`has the value`Some User Agent`:
```

```

- To match an HTTP request if the URL query string has a case-sensitive key`search`, for example as in the URL`https://www.example.com/category/?search=item+foo%20bar&page=1`:
```

```

- To match an HTTP request if the URL query string has a case-sensitive key`search`(case-sensitively) with a case-insensitive value`item+foo%20bar`, for example as in the URL:`https://www.domain.com/category/?search=item+foo%20bar&page=1`
```

```

Matching for URL query (both keys and values) must be done using URL unescaped versions of their values.
- To case-insensitively match an HTTP request for a cookie named`tastycookie`:
```

```

- To case-insensitively match an HTTP request for a cookie named`tastycookie`that contains the case-sensitive value`strawberry`:
```

```

## Matchers

Multiple matchers are available to use in conditions.

### String Matchers

The next table lists the matchers that operate on string values. Some matchers have alternative variants, meaning any of those variants can be used interchangeably for that matcher.

The examples for each matcher all match the`http.request.url.path`containing`/category/element/id`:

Name Alternatives Description Example
`eq``=, ==, equal, equals`Matches if values on the left-hand and right-hand side of the matcher are equal.`http.request.url.path eq "/category/element/id"`
`ew`Matches if the value on the left-hand side ends with the value on the right-hand side.`http.request.url.path ew '/id'`
`sw`Matches if the value on the left-hand side starts with the value on the right-hand side.`http.request.url.path sw '/category'`
`not eq``!=, not equal, not equals`Matches if values on the left-hand and right-hand side of the matcher are not equal.`http.request.url.path neq '/some/other/path'`
`not ew`Matches if the value on the left-hand side does not end with the value on the right-hand side.`http.request.url.path not ew '/not_id'`
`not sw`Matches if the value on the left-hand side does not start with the value on the right-hand side.`http.request.url.path not sw '/not_category'`

### Partial Matchers

Some of the variables used in the rules contain arbitrary key-value maps of data when the rules are run. For example`http.request.headers`contains the HTTP request headers. For more details on the available maps, see[Variables](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/routing_policy_conditions.htm#routing_policy_conditions_variables).

The matchers`in`and`not in`can be used to check if a map variable contains a specific key. It depends on the variable what the key actually represents.

The syntax for checking if a map variable contains a specific key is:
```

```

- `<key>`must be either a case-sensitive or case-insensitive string.
- The right-hand side value must be in parentheses.

For example, this condition matches if the HTTP request has a cookie with the name`Foo`:
```

```

## Values

The values used in predicates can be either constant values or variables which are evaluated at runtime.

### Constants

The rules support string constants written between single-quotes.

Example:
```

```

#### String case-sensitivity

String matching uses case-sensitive comparisons by default.

For example, if the HTTP request URL path for some request is /foo then the following predicate would not match for that request, because case-sensitive string comparison is used:
```

```

Case-insensitive matching is done if at least one of the compared values is a case-insensitive string. The syntax for a case insensitive string is:
```

```

For example, these strings are all case-insensitive and are therefore equivalent, when used in predicates:
```

```

In comparison to the original example - this predicate does match, because it uses case-insensitive comparison:
```

```

#### String Case-Sensitivity

String matching uses case-sensitive comparisons by default.

For example, if the HTTP request URL path for some request is`/foo`then the following predicate would not match for that request, because case-sensitive string comparison is used:
```

```

Case-insensitive matching is done if at least one of the compared values is a case-insensitive string. The syntax for a case insensitive string is:
```

```

For example, these strings are all case-insensitive and are therefore the same, when used in predicates:
```

```

In comparison to the original example, this predicate does match, because it uses case-insensitive comparison:
```

```

### Variables

Variables are used in conditions to match against some particular value of the HTTP request. The actual values for each variable are decided when the rules are run, during each individual HTTP request.

#### Map Type Variables

Some variables contain arbitrary key-value maps of request data, for example request headers or cookies. For each key, there can be one or more values. For example, there can be several request headers with the same name.

Typically, map variables can be used in rules these ways:
- To check if a map has a specific key.
- To check if a map has a specific key with a specific value.

Checking if a map has a specific key:

Checking if a map variable has a specific key is done with the`in`matcher. For more details, refer to[Routing Policy Language for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/routing_policy_conditions.htm).

For example:
```

```

This condition matches if the HTTP request has a cookie with the name`Foo`.

Checking if a map has a specific key with a specific value:

Checking if a map has a specific key with a specific value is done using bracket`[]`notation to get the values at a specific key. The syntax for using bracket notation is:
```

```

The`<key>`must be specified as a case-sensitive or case-insensitive string.

The actual check for a specific value is done using the`eq`matcher to check if`any`of the values at that key are equal to that specific value. The predicate matches if at least one of the values at that key match that specific value.

Examples:
- To match if any value of the header`header-name`equals`header-value`:
```

```

Header`name`is compared case-insensitively, but header`value`is compared case-sensitively.
- To match if any value of the cookie "cookie-name" equals`cookie-value`:
```

```

The`not eq`matcher can be used to check that`none`of the values at that key are equal to a specific value.

Examples:
- To match if no value of the header`header-name`equals`header-value`:
```

```

Header name is compared case-insensitively. Header value is compared case-sensitively.
- To match if no value of the cookie "cookie-name" equals`cookie-value`:
```

```

#### All Available Variables

The variables available to be used in the conditions are:

Name Description Example
`http.request.headers`A map containing HTTP request headers.

This map has some special behavior - the keys (header names) must be case-insensitive strings. Using case-sensitive strings for`http.request.headers`keys in predicates aren't allowed.
- Correct usage:
```

```

- Incorrect usage:
```

```

`http.request.url.path`HTTP request URL path. This is the request URL, without protocol, domain, port, and query string.
`http.request.url.query`A map containing HTTP request URL query elements. If the request URL doesn't have a query (doesn't have the`?`character) or if the query is empty (the`?`character is the last one in the URL), this map is empty.

The query is parsed to produce the`http.request.url.query`map, by taking the query string part of the URL (which is the part after the first`?`character) and splitting it into key-value pairs, by treating these characters as special:
- `&`character is the separator between different key-value pairs
- `=`character is the separator between the key and value (inside a key-value pair)

The first`?`character present in the URL marks the beginning of the query string. If extra`?`characters appear after the first one, they're treated the same as any other character, without any special handling.

Inside a key-value pair, the first = character present separates the key from the value. If extra = characters are present, they're treated as being part of the value.

Keys and values are unescaped according to URL escaping rules. URL:`https://www.domain.com/path?key=value&key=%61&another%20key=another+value`

The`http.request.url.query`data for a request with this URL would look like this expressed as JSON:
```

```

In this example, both key and value are matched case-sensitively. So if instead of`key=value`the URL contained`KEY=value`or`key=VALUE`the condition would not match.

However, a key-value pair from the URL query string isn't added to the`http.request.url.query`map in these cases:
- If a`=`character isn't present in a key-value pair

Example:

URL:`https://www.example.com/path?no_key"`

In this case, the query string element`no_key`isn't present in the`http.request.url.query`map.
- If the left-hand side of the = character is empty (the key isn't specified)

Example: URL:`https://www.domain.com/path?=no_value`

In this case, the query string element`no_value`isn't present in the`http.request.url.query`map.

If the right-hand side of the`=`character is empty, then the value for that key-value pair is an empty string`''`.

http.request.cookies A map containing HTTP request cookies, parsed from the`"Cookie"`request header as called out in[RFC-6265](https://tools.ietf.org/html/rfc6265), where the key is a cookie name and the value is the corresponding cookie value. If the`"Cookie"`request header isn't present in the request - this map is empty.

#### Examples

An incoming HTTP/1.1 request looks like this (request line and headers):
```

```

Then the variables available for rules would be populated with data from this request as follows:(the data for structured variables is shown in JSON format)
```

```

Here are some examples how we could match this request:
- If we wanted to match requests to domain`www.domain.com`and URL paths that start with`/category/`, we would use a condition like this:
```

```

- To match requests where the URL path is exactly`/category/some_category`or request query element`action=search`:
```

```

- To match requests that have a query string element named`query`with value`search terms`(after URL unescaping):
```

```

- To match requests that have cookie`cookie_a`but don't have cookie`cookie_c`:
```

```
