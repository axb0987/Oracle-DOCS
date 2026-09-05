# Details For Web Application Firewall Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_lbwaf.htm
- Fetched: 2026-09-05 02:37 CDT

# Details For Web Application Firewall Logs

Logging details for Web Application Firewall Logs (WAF Logs).

## Resources
- Web Application Firewall

## Log Categories

API value (ID): Console (Display Name) Description
all All Logs All WAF Logs

## Availability

WAF logs are available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Contents of a Web Application Firewall Log

A WAF log record contains the following fields:

Field Description Example
action The action taken by the WAF, which can be either "allow" if further processing of the request was allowed, or "block" if it wasn't.`allow`
clientAddr Client IP address. Nginx[$remote_addr](https://nginx.org/en/docs/http/ngx_http_core_module.html#var_remote_addr)variable.`192.168.0.33:7870`
countryCode Client ISO alpha-2 country code.`"ca"`
host In this order of precedence: host name from the request line, or host name from the “Host” request header field, or the server name matching a request. Nginx[$host](https://nginx.org/en/docs/http/ngx_http_core_module.html#var_host)variable.`192.168.0.103`
listenerPort Port of the server which accepted a request. Nginx[$server_port](https://nginx.org/en/docs/http/ngx_http_core_module.html#var_server_port)variable.`"80"`
request.httpVersion Request protocol, usually “HTTP/1.0”, “HTTP/1.1”, or “HTTP/2.0”. Nginx[$server_protocol](https://nginx.org/en/docs/http/ngx_http_core_module.html#var_server_protocol)variable.`"HTTP/1.1"`
request.id Unique request identifier generated from 16 random bytes, in hexadecimal. Nginx[$request_id](http://nginx.org/en/docs/http/ngx_http_core_module.html#var_request_id)variable.`"f8860949459e94181e650d4049615a01"`
request.method Request method, usually “GET” or “POST”. Nginx[$request_method](https://nginx.org/en/docs/http/ngx_http_core_module.html#var_request_method)variable.`“GET”`
request.path Full original request URI (with arguments). Nginx[$request_uri](https://nginx.org/en/docs/http/ngx_http_core_module.html#var_request_uri)variable.`"/console/css/%252e%252e%252fconsole.portal"`
requestProtection.matchedData Data that triggered rule actions when the request was inspected. The string contains data present in the URI, separated by a semicolon.`'Test_data_1;Test_data_2;Test_data_3'`
requestProtection.matchedIds String containing matched protection rule IDs and versions (for request inspection). When reporting, IDs are appended by 3 version symbols, so ID=123 and version=4 is reported as 123004. Entries are separated by a semicolon.`"9301000_v001;9301100_v001;9301100_v001;9300000_v001"`
requestProtection.matchedRules Rule names of request protection rules that matched when the request was inspected. The string contains rule names that are separated by a semicolon.`'Rule_name_1;Rule_name_2;Rule_name_3'`
responseProtection.matchedData Data that triggered rule actions (in the response inspection). The string contains data present in the URI, separated by a semicolon.`'Test_data_1;Test_data_2;Test_data_3'`
response.code Final response code sent to client. Nginx[$status](https://nginx.org/en/docs/http/ngx_http_core_module.html#var_status)variable.`"401"`
response.size Full response size (headers + body) in bytes. Nginx[$bytes_sent](https://nginx.org/en/docs/http/ngx_http_core_module.html#var_bytes_sent)variable.`"139"`
requestAccessControl.matchedRules Rule names of request access rules that have matched. Strings contain rule names that are separated by a semicolon.`'Rule_name_1;Rule_name_2;Rule_name_3'`
responseAccessControl.matchedRules Rule names of response access rules that have matched. Strings contain rule names that are separated by a semicolon.`'Rule_name_1;Rule_name_2;Rule_name_3'`
backendStatusCode Keeps a status code of the response obtained from the upstream server. Status codes of several responses are separated by commas and colons. This is an Nginx[$upstream_status](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#var_upstream_status)variable.`"200"`
responseProtection.matchedIds String containing matched protection rule IDs and versions (for request inspection). When reporting, IDs are appended by 3 version symbols, so ID=123 and version=4 is reported as 123004. Entries are separated by a semicolon.`'300_v004;25_v002;123_v001'`
responseProtection.matchedRules Rule names of response protection rules that have matched. Strings containing rule names that are separated by a semicolon, for example:`'Rule name 1;Rule name 2;Rule name 3'.``"Recomended Rules"`
requestRateLimiting.matchedRules Rule names of rate limiter rules that have matched. String containing rule names that are separated by a semicolon.`'Rule_name_1;Rule_name_2;Rule_name_3'.`
responseProvider
Contains information regarding where the response originates:
- From backend (origin).
- From some WAF module (module and rule name).
- From LB HTTP IP access rule.
- From LB HTTP method access rule.
- From LB redirect rule.`"requestProtection/Recomended Rules"`
timestamp ES timestamp of when the request was received, local time in the[ISO 8601](http://nginx.org/en/docs/http/ngx_http_log_module.html#var_time_iso8601)format.`"2021-12-02T08:39:05Z"`

## Sample Web Application Firewall Log
```

```
