# Adding a Request Control Rule to a Web Application Firewall Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/AccessControl/create_access_rule_request_control.htm
- Fetched: 2026-09-05 03:09 CDT

# Adding a Request Control Rule to a Web Application Firewall Policy

Add a request control rule to allow, check, and return HTTP requests to a web application firewall (WAF) policy.

## Using the Console

- On the Policies list page, select the policy that you want to work with. If you need help finding the list page or the policy, see[Listing Web Application Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessControl/../Policies/list_waf-policy.htm#top).
The policy's details page opens.
- From the details page, select Access control .
- Find the Request access section.
All request access rules are displayed in a table.
- From the Actions menu , select Add request access rule .
The Add request access rule panel opens.
- Enter the name of the request access rule.

### Conditions

Specify the prerequisite conditions that must be met for the rule action to occur. The parameters displayed can vary depending on the values that you select for Condition type and Operator . Select + Another condition to add another condition linked to the first one using AND. Select X to delete the associated condition row.

(Optional) Enable Show basic controls to specify a condition in the box using the condition syntax. See[Understanding Conditions](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessControl/../Concepts/understanding_conditions.htm#understanding_conditions).

### Rule action

Select an existing rule from the Action rule list to follow when the preceding conditions are met.
- Preconfigured check action : Allows the running of rules and generates a log message that documents the result.
- Preconfigured allow action : Skips all remaining rules in the current module.
- Preconfigured 401 response code action : Returns a defined HTTP response. The response code configuration (headers and response page body) determines the HTTP response that's returned when this action is run.
- Header details : Select to display the HTTP response headers specified in the selected return HTTP response action.
- Response page body details : Select to display the HTTP response body specified in the selected "return HTTP response" action.

For more information, see[Actions for Web Application Firewalls](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessControl/../Actions/actions_management.htm#RateLimitinglManagement).

Select Create new action to add an action. Enter the following information:
- Check : Allows the running of rules and generates a log message documenting the result.
- Allow : Skips all remaining rules in the current module.
- Return HTTP response : Returns a defined HTTP response. The response code configuration (headers and response page body) determines the HTTP response that's returned when this action is run.
- Select Headers to display the HTTP response headers specified in the selected Return HTTP response action.
- Select Response page body to display the HTTP response body specified in the selected "Return HTTP response" action.

For more information, see[Actions for Web Application Firewalls](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessControl/../Actions/actions_management.htm#RateLimitinglManagement).

Select Add request access rule .
