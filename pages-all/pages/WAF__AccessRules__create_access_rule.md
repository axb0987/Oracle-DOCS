# Adding an Access Rule to an Edge Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/create_access_rule.htm
- Fetched: 2026-09-05 03:09 CDT

# Adding an Access Rule to an Edge Policy

Use Web Application Firewall to add an access rule to an Edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/create_access_rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/create_access_rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/create_access_rule.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- On the Policies page, select the compartment that contains the policy.
- (Optional) Filter the listed policies by name, state (status), policy type ( Edge policy ), or creation date.
- Select the name of the Edge policy to which you want to add an access rule.
- On the policy details page, under Edge policy , select Access control .
- Select the Access rules tab.
The Access rules list appears. For more information, see[Access Rules for Edge Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/../Tasks/access-rules.htm#access_rules).
- Select Add access rule .
- Provide the following information:

- Name : Enter a name for the access rule.
- Action : Select one of the following options to determine the response to a request when the rule is matched:
- Log and allow : A log is created for all matched requests and no further action is taken.
- Detect only : A detection alert is created for all matched requests and no further action is taken.
- Block : All matched requests are blocked and a browser page for the selected response code is returned.
- Block action : Select the action that's taken when a matching request is blocked.
- Block response code : Select a response code that's returned when the request has been blocked. The response code provides information indicating why the request was blocked. The default response code is 403 Forbidden.
- Redirect : All matched requests are redirected. Complete the following options:
- Redirect status code : Select the status code returned in response to redirect requests from the list.
- Redirect URL : Enter the URL address to redirect the request to.
- Bypass : Select one or more challenges to bypass. If you don't specify a challenge, all challenges are bypassed.
- Show CAPTCHA : Select this option to show a CAPTCHA for all matched requests and take no further action. Enter the following information:
- CAPTCHA title : Enter the text for the CAPTCHA page title.
- CAPTCHA header : Enter the text that appears before the CAPTCHA image (for example, "I am not a robot").
- CAPTCHA footer text : Enter the text to display after the CAPTCHA input box and before the submit button.
- CAPTCHA submit button : Enter the text for the Submit button (for example, "Yes, I am human.").
- Conditions : Select the condition that must be met before the rule is matched and specify the details of the condition. Select +Additional condition to add other conditions.
- Header manipulation(s) : Complete the following information:
- Action : Select the action to apply to the request.
- Header name : Enter the HTTP header name of the request.
- Header value : Enter the HTTP header value of the request.
- Select Add access rule .

The access rule is added to the list.

For changes to take effect, you must publish them. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/../Bot/publishing_changes.htm#PublishChanges).
- 

Enter the following command and required parameters.

```

```

The`access-rules`value is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.

Create an access rule by adding a new access rule object to the list without a`key`property specified. A key is generated for the new access rule upon update.

See the CLI online help for a list of optional parameters:

```

```

See the Oracle Cloud Infrastructure documentation for a complete description of the[oci waas access-rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/access-rule/update.html)command.
- 

Use the[UpdateAccessRules](https://docs.oracle.com/iaas/api/#/en/waas/latest/AccessRule/UpdateAccessRules)operation to add an address rule using the API.

Create an access rule by adding a new access rule object to the list without a`key`
