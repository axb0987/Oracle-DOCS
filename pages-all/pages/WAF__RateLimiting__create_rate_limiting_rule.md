# Adding a Rate Limiting Rule to a Web Application Firewall Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/RateLimiting/create_rate_limiting_rule.htm
- Fetched: 2026-09-05 03:11 CDT

# Adding a Rate Limiting Rule to a Web Application Firewall Policy

Add a rate limiting rule to allow the inspection of HTTP request properties and to limit the request frequency for each unique client IP address associated with web application firewall (WAF) policy.

## Using the Console

- On the Policies list page, select the policy that you want to work with. If you need help finding the list page or the policy, see[Listing Web Application Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/RateLimiting/../Policies/list_waf-policy.htm#top).
The policy's details page opens.
- From the details page, select Rate limiting .
All rate limiting rules are displayed in a table.
- From the Actions menu , select Add rate limiting rule .
The Add rate limiting rule panel opens.
- Enter the name of the rate limiting rule.

- Name : Enter a name for the rate limiting rule.

### Conditions (optional)

Specify the prerequisite conditions that must be met for the actions/rule actions to occur. The parameters displayed can vary depending on the values that you select for Condition type and Operator . Select + Another condition to add another condition linked to the first one using AND. Select X to delete the associated condition row.

(Optional) Enable Show basic controls to specify a condition in the box using the condition syntax. See[Understanding Conditions](https://docs.oracle.com/en-us/iaas/Content/WAF/RateLimiting/../Concepts/understanding_conditions.htm#understanding_conditions).

### Rate limiting configuration

Specify the following rate limitation settings:
- Requests limit : Enter the maximum number of requests made.
- Period in seconds : Enter the number of seconds passed.
- Action duration in seconds : Enter the duration of the action in seconds.

Select + Another rate limiting to add another rate limiting linked to the first one using AND. Select X to delete the associated rate limiting row.

### Rule action

Select an existing rule from the Action name list to follow when the preceding conditions are met:
- Preconfigured check action : Allows the running of rules and generates a log message that documents the result.
- Preconfigured 401 response code action : Returns a defined HTTP response. The response code configuration (headers and response page body) determines the HTTP response that's returned when this action is run.
- Header details : Select to display the HTTP response headers specified in the selected return HTTP response action.
- Response page body details : Select to display the HTTP response body specified in the selected "return HTTP response" action.

For more information, see[Actions for Web Application Firewalls](https://docs.oracle.com/en-us/iaas/Content/WAF/RateLimiting/../Actions/actions_management.htm#RateLimitinglManagement).

To add an action, select Create new action . Enter the following information:
- Rule action : Select an existing rule to be followed when the preceding conditions are met, or select Create new action to add one.
- Check : An action which doesn't stop the execution of rules in current module. Instead it generates a log message documenting result of rule execution.
- Return HTTP response : An action which cancels all further processing of an HTTP request or HTTP response and returns a predefined HTTP response that can be configured in the action definition.
- Header details : Select to display the HTTP response headers specified in the selected return HTTP response action.
- Response page body details : Select to display the HTTP response body specified in the selected "return HTTP response" action.

Select Add rate limiting rule .
