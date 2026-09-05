# Creating a Web Application Firewall Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/create_waf-policy.htm
- Fetched: 2026-09-05 03:11 CDT

# Creating a Web Application Firewall Policy

Create a web application firewall (WAF) policy.
When you create a policy, you're initially only creating the policy framework. After the policy is created, you build it out using the various resources available. Typically this includes providing basic, access control, rate limiting, and protection options as needed, and then select a firewall as the WAF policy enforcement point. For more information, see[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/getting_started_with_waf-policies.htm#before).

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/create_waf-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/create_waf-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/create_waf-policy.htm#)
- 

- On the Policies list page, select Create WAF policy . If you need help finding the list page or the policy, see[Listing Web Application Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/list_waf-policy.htm#top).
The Create policies panel opens.
- Enter the following information:

- Name : Enter a name for the WAF policy, or use the default name.
- Compartment : Select the compartment to contain the WAF policy.

## Tags

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.

Select Create .

The policy you created appears in the policy list. Select the policy from the list. The policy's details page opens.

Configure the following resources:

## Actions

For information on actions, see[Actions](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/../Actions/actions_management.htm#RateLimitinglManagement).

## Access Control Rules

For information on access control rules, see[Access Controls](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/../AccessControl/access_control_management.htm#AccessControlManagement).

## Rate Limiting Rules

For information on rate limiting rules, see[Rate Limiting Rules](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/../RateLimiting/rate_limiting_rule_management.htm#RateLimitinglManagement).

## Request Protection Rules

For information on rate limiting rules, see[Request Protection Rules](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/../Protections/protections_management.htm#WorkRequestManagement).

## Firewall

For information on rate limiting rules, see[Firewalls](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/../Firewall/firewall_management.htm#FirewallManagement)
- 

Use the[oci waf web-app-firewall-policy create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waf/web-app-firewall-policy/create.html)command and required parameters to create a web application firewall policy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateWebAppFirewallPolicy](https://docs.oracle.com/iaas/api/#/en/waf/latest/WebAppFirewallPolicy/CreateWebAppFirewallPolicy)
