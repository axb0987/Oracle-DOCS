# Editing a Web Application Firewall Request Protection Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/update_request_protection_rule.htm
- Fetched: 2026-09-05 03:11 CDT

# Editing a Web Application Firewall Request Protection Rule

Update a request protection rule contained within a web application firewall policy.

## Using the Console

- On the Policies list page, select the policy that you want to work with. If you need help finding the list page or the policy, see[Listing Web Application Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/../Policies/list_waf-policy.htm#top).
The policy's details page opens.
- From the details page, select Protections .
All request protections rules are displayed in a table.
- Select the request protection rule that you want to work with.
The request protection rule's details page opens.
- Select Manage request protection rules .
The Manage request protection rules panel opens.
- Select Edit .
The Edit protection rule panel opens.
- Update the firewall settings as needed. For descriptions of the protections rule settings, see[Adding a Web Application Firewall Request Protection Rule](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/create_request_control.htm#top).
- To edit multiple rules at once, select the checkboxes for one or more rules, select the Actions menu at the top of the table, and then select one of the following options:

- View and edit rules settings : Apply the following settings to any request protection rule that has HTTP body inspection enabled:
- Maximum number of bytes allowed : Specify the number of bytes in each HTTP message body that undergoes inspection. Value ranges from 0 - 8192.
- Action taken if limit has been exceeded : Select an action from the list that occurs if the size of the message body exceeds your specified maximum number of bytes allowed. The pre-defined actions are:
- Inspect partial body and continue : The body is inspected to the specified size limit. No further action is taken if that limit is exceeded. This selection is equal to the "None" selection.
- Pre-configured 401 Response Code Action : This is a dynamic action. Each time you can define a different set of actions, but they all are going to be with the "Return HTTP Response" type.
- Return HTTP response : This option is disabled.

You can also create a custom action. For more information, see[Actions](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/../Actions/actions_management.htm#RateLimitinglManagement).
- Enable body inspection : Enables inspection of the HTTP message body.
- Disable body inspection : Disables inspection of the HTTP message body.
- Delete : Removes the selected request protection rules from the web application firewall policy.

For more information on the HTTP body inspection feature, see[HTTP Request Body Inspection for Web Application Firewall](https://docs.oracle.com/en-us/iaas/Content/WAF/Protections/protections_management.htm#request-body-inspection).
-
