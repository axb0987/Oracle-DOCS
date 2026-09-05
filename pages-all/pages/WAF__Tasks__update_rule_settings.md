# Updating Protection Settings for an Edge Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/update_rule_settings.htm
- Fetched: 2026-09-05 03:11 CDT

# Updating Protection Settings for an Edge Policy

Use Web Application Firewall to update protection settings for Edge policies.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/update_rule_settings.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/update_rule_settings.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/update_rule_settings.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.

All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:
- State
- Name
- Policy Type : Select Edge Policy .
- Select the name of the edge policy you want to update rule settings for.

The edge policy's details page opens.
- On the policy details page, under Edge policy , select Protection rules .
- Select the Settings tab.
- Select Edit rule settings .
- In the Edit rule settings dialog box, enter the following information:
- Block action : The action taken on malicious requests blocked by WAF.
- Block response code : Provides information indicating why the request was blocked.
- Max number of arguments : The maximum number of arguments allowed in the request. The recommended setting is 255.
- Max length of argument : The maximum argument length allowed in the request. The recommended setting is 400.
- Max total argument length : The maximum argument length for all arguments in the request. The recommended setting is 64000.
- Max response size (kilobytes): The maximum response size. The recommended setting is 1024.
- Recommendations period : The period in days to analyze for recommended actions.
- Allowed HTTP methods : The list of allowed HTTP protocol methods.
- Enable response inspect: Select to enable response inspection.
- Select Save changes .

The accepted protection rules are added to the list to be published. For more information, see[WAF Protection Rules](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/wafprotectionrules.htm#WAF_Protection_Rules).
- 

This task is not available in the CLI.
- 

Run the[UpdateProtectionSettings](https://docs.oracle.com/iaas/api/#/en/waas/latest/ProtectionSettings/UpdateProtectionSettings)
