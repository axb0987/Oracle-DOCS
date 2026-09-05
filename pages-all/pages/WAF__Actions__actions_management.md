# Actions for Web Application Firewalls
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Actions/actions_management.htm
- Fetched: 2026-09-05 03:09 CDT

# Actions for Web Application Firewalls

Learn how to add and manage actions for web application firewall policies.

Actions are objects that represent one of the following:
- Allow : An action, which upon matching rule, skips all remaining rules in the current module.
- Check : An action which doesn't stop the execution of rules in current module. Instead it generates a log message documenting result of rule execution.
- Return HTTP response : An action which terminates all further processing of an HTTP request or HTTP response and returns a predefined HTTP response that can be configured in the action definition.

When this action is run in an HTTP request rule, it prevents the HTTP request from being forwarded to a backend. Instead of returning the HTTP response from the backend, the HTTP response that was defined in the action is returned. This action is typically used to block HTTP requests matching specific criteria. When this action is run in an HTTP response rule, it prevents the original HTTP response from the backend from being sent back to the client. Instead, the HTTP response is replaced by the one defined in the action.

For this action, you can add details for the response page body, such as cause and further instructions. You can also enable Dynamic text support to add the`RequestID`variable in the page body. The request ID can help you with tracking and managing a request by providing a unique request identifier exposed in HTTP request and response headers.

You can perform the following actions management tasks:
- [List the actions for a policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Actions/list_actions.htm#top).
- [Add an action to the policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Actions/create_action.htm#top).
- [View the details of an action](https://docs.oracle.com/en-us/iaas/Content/WAF/Actions/get_action.htm#top).
- [Update the settings of a policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Actions/update_action.htm#top).
- [Delete an action from a policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Actions/delete_action.htm#top)
