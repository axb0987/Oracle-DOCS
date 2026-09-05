# Applying an Action to a Protection Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/apply_action_to_protection_rule.htm
- Fetched: 2026-09-05 03:11 CDT

# Applying an Action to a Protection Rule

Use the Web Application Firewall Edge policies to apply an action to a protection rule.

## Using the Console

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.

All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:
- State
- Name
- Policy Type : Select Edge Policy .
- Select the edge policy that you want to configure rule settings for.

The edge policy's details page opens.
- On the policy details page, under Edge policy , select Protection rules .
- Select the Rules tab, and then find the protection rule you that want to apply an action to.
Tip  
  
You can use the Rule ID to find a protection rule.
- Select the Actions menu (three dots) for the rule and select one of the following options:
- Detect : Matching requests generate an alert and the request is proxied.
- Block : Matching requests are blocked.
- Off : The rule is disabled.
- Exclusions : Exclusions are set to specify the types of requests that are bypassed by the protection rule. If a request matches any of the set exclusions, the protection rule doesn't run for that request.
- In the Exclusions dialog box, enter the following criteria:
- Exclusion : Select request cookie values, request cookie names, request parameters, or request parameter names.
- Value : Enter the value for the selected exclusion.
- Select Save changes .

The protection rule action is added to the list to be published. For more information, see[WAF Protection Rules](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/wafprotectionrules.htm#WAF_Protection_Rules)
