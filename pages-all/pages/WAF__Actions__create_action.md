# Adding a Web Application Firewall Action
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Actions/create_action.htm
- Fetched: 2026-09-05 03:09 CDT

# Adding a Web Application Firewall Action

Add an action to a web application firewall (WAF) policy.

## Using the Console

- On the Policies list page, select the policy that you want to work with. If you need help finding the list page or the policy, see[Listing Web Application Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Actions/../Policies/list_waf-policy.htm#top).
The policy's details page opens.
- From the details page, select Actions .
The Actions list opens. All actions are displayed in a table.
- From the Actions menu , select Add action .
The Add action panel opens.
- Enter the following information:

- Name : Enter a name for the action.
- 
Type : Specify the action type:
- Allow : Skips all remaining rules in the current module.
- Check : Doesn't stop the running of rules. Instead it generates a log message that documents the result of running the rules.
- Return HTTP response : Returns a defined HTTP response.

If you select this type, then provide the following values:
- Response code : Select the HTTP response.
- Headers : Enter optional header information:
- Header name : Enter the name of the header.

Header value : Enter the associated value of the header.
- 

Response page body : Provides details about an error, including the cause and further instructions, if needed. Enter the HTTP response body, for example a JSON error response:
```

```

You can enable Dynamic text support to add variables in the page body. The following variable is supported:
```

```

The request ID can help you with tracking and managing a request by providing a unique request identifier exposed in HTTP request and response headers.

When the request ID is enabled, the default header name X-Request-Id is included in the HTTP request header from the load balancer to the backend and HTTP header responses.

The following example provides an HTTP response body with dynamic text support enabled:
```

```

-
