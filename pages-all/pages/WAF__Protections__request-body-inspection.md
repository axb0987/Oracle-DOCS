# HTTP Request Body Inspection for Web Application Firewall
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/request-body-inspection.htm
- Fetched: 2026-09-05 03:11 CDT

# HTTP Request Body Inspection for Web Application Firewall

Manage HTTP request body inspection in Web Application Firewall (WAF) to improve security.

HTTP request body inspection instructs the WAF policy to buffer the request body in memory and inspect it before sending the request headers and request body to the backend. If you don't enable HTTP request body inspection, the request body streams directly to the backends, provided the request headers didn't trigger any protection rules.

You can enable HTTP request body inspection when you add a request protection rule, or update an existing rule to include it. Only protection capabilities that support body inspection conditions can use this feature.

To configure body inspection settings:

- In the process of editing a protection rule, access the View and Edit Rules Settings dialog box.
- In the dialog box, specify the maximum number of bytes to inspect in the Maximum Number of Bytes Allowed field. You can inspect between 0 and 8,192 bytes. The specified number of bytes are inspected for each request body.
- If the message exceeds the limit, select an action from the Action taken if limit has been exceeded list.
Note  
  

Enabling this feature can result in latency of message traffic because of the additional time required to inspect the message body.

## Predefined actions

- Inspect Partial Body and Continue : The body is inspected up to the specified limit. No further action is taken if that limit is exceeded. This selection is equal to the "None" option.

The WAF body inspection feature lets protection rules inspect the request body. By default, request bodies are excluded from inspection, so you need to enable this feature. Because WAF can't inspect all request bodies—some might be too large—WAF inspects only up to a specified size limit. If a request body exceeds that limit, decide whether to block the request, or allow the rest of the body to be proxied if the start of the body doesn't contain attack vectors. WAF can then continue to balance traffic.
- Preconfigured 401 Response Code Action : Returns an HTTP response. You can define a different action each time that returns an HTTP response.

You can also create a custom action. For more information, see[Actions](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/../Actions/actions_management.htm#RateLimitinglManagement).

A request protection rule with body inspection appears as Enabled in the Body Inspection column of the Request Protections Rules list.

## Notes

- By default, request bodies are excluded from protection rules inspection. You must enable body inspection for rule-based analysis.
- Because WAF can't process all request bodies due to potential large sizes, WAF uses a cutoff size for inspection.
- You might want to block requests with large bodies or allow proxying if the beginning of the body is safe. WAF can then continue traffic management.
-
