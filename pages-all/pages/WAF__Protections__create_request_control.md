# Adding a Web Application Firewall Request Protection Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/create_request_control.htm
- Fetched: 2026-09-05 03:11 CDT

# Adding a Web Application Firewall Request Protection Rule

Add a request protection rule to a web application firewall policy.

## Using the Console

- On the Policies list page, select the WAF policy that you want to add the request protection rule to. If you need help finding the list page or the policy, see[Listing Web Application Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/../Policies/list_waf-policy.htm#top).
- From the details page, select Protections .
The Protections list opens. All request protections rules are displayed in a table.
- From the Actions menu , select Add request protection rule .
The Add protection rule panel opens.

### Conditions (optional)

Specify the prerequisite conditions that need to be met for the rule action to occur. See[Understanding Conditions](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/../Concepts/understanding_conditions.htm#understanding_conditions)for more information on how to author the conditions for your access rule.

Enable Show basic controls to switch to the advanced builder mode.

### Rule action

Select an existing rule from the Action name list to follow when the preceding conditions are met:
- Preconfigured check action : Allows the running of rules and generates a log message that documents the result.
- Preconfigured 401 response code action : Returns a defined HTTP response. The response code configuration (headers and response page body) determines the HTTP response that's returned when this action is run.

For more information, see[Actions for Web Application Firewalls](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/../Actions/actions_management.htm#RateLimitinglManagement).

To add an action, select Create new action . Enter the following information:
- Preconfigured check action : Allows the running of rules and generates a log message that documents the result.
- Preconfigured 401 response code action : Returns a defined HTTP response. The response code configuration (headers and response page body) determines the HTTP response that's returned when this action is run.
- Header details : Select to display the HTTP response headers specified in the selected return HTTP response action.
- Response page body details : Select to display the HTTP response body specified in the selected "return HTTP response" action.

For more information, see[Actions for Web Application Firewalls](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/../Actions/actions_management.htm#RateLimitinglManagement).
- Check : An action which doesn't stop the execution of rules in current module. Instead it generates a log message documenting result of rule execution.
- Return HTTP response : An action which cancels all further processing of an HTTP request or HTTP response and returns a predefined HTTP response that can be configured in the action definition.
- Header details : Select to display the HTTP response headers specified in the selected return HTTP response action.
- Response page body details : Select to display the HTTP response body specified in the selected "return HTTP response" action.

### Body inspection

- Body inspection : Select Enable body inspection to allow the HTTP request body to undergo inspection to ensure that request body content conforms to all the specified protection capabilities in the protection rule. For more information, see[HTTP Request Body Inspection for Web Application Firewall](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/protections_management.htm#request-body-inspection).
- Protection capabilities list: Displays all protection capabilities associated with the protection rule and their information. This information includes the key number, the capability name, collaborative status, any applied tags, and the action used.
Note  
  
Protection capabilities aren't necessarily run in the order they're listed here.

Select Choose protection capabilities .

In the Choose protection capabilities window, enter the following information:
- Filter by tags : Select one or more filters to limit the protection capabilities displayed.
- Filter by version : Select one or more versions to limit the protection capabilities displayed.
- Reset all filters : Select to remove all user-inputted filters.
- Protections list: Check each protection that you want to apply to the rule.

Select Choose protection capabilities to apply the protections you selected to the rule and close the window.

In the Add protection rule window, select the checkbox for one or more protection capability, select the Actions menu at the top of the table, and select any of the following commands:
- 

View and edit protection capability settings : View setting information such as allowed HTTP methods, header information, and argument information. Select Edit to update the following settings:
- Allowed HTTP methods : Select the HTTP methods allowed by the protection capability 911100: Restrict HTTP Request Methods.
- Maximum HTTP request header length : Enter the maximum header length allowed in an HTTP request by the protection capability 9200024: Limit length of request header size.
- Maximum HTTP request headers : Enter the maximum number of headers allowed in an HTTP request by the protection capability 9200014: Limit Number of Request Headers.
- Maximum number of arguments : Enter the maximum number of arguments allowed by the protection capability 920380: Number of Arguments Limits.
- Maximum single argument length : Enter the maximum argument length allowed by the protection capability 920370: Limit argument value length.
- Maximum total argument length : Enter the maximum total combined length of all arguments allowed by the protection capability 920390: Limit arguments total length.
- Change action : Use a different action for the selected protection capabilities. For more information, see[Actions for Web Application Firewalls](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/../Actions/actions_management.htm#RateLimitinglManagement).
- Delete : Delete the selected protection capabilities. Confirm when prompted.

For each entry in the Protection capabilities list, you can select the following from the Actions menu (three dots) in the row for that entry:
- View details : Opens the Capability details panel to view the name, description, version, and collaborative status of the protection capability.
- Change action : Opens the Change action panel to select a different action for the protection capability. See[Actions for Web Application Firewalls](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/../Actions/actions_management.htm#RateLimitinglManagement)for more information.
- Exclusions : Opens the Exclusions panel to specify the types of request that the protection rules bypass. If a request matches any of the set exclusions, the protection rules are run for that request. Select the type and corresponding value for each exclusion entry.
- Override weight and threshold : Opens the Override weight and threshold panel to view the default collaborative capability weight and threshold. To override default values, select Override weights and threshold and enter new values.

Select Add request protection rule .
