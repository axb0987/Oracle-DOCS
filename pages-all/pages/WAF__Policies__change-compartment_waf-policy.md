# Moving a Web Application Firewall Policy to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/change-compartment_waf-policy.htm
- Fetched: 2026-09-05 03:11 CDT

# Moving a Web Application Firewall Policy to a Different Compartment

Move a web application firewall (WAF) policy to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/change-compartment_waf-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/change-compartment_waf-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/change-compartment_waf-policy.htm#)
- 

- On the Policies list page, find the policy that you want to work with. If you need help finding the list page or the policy, see[Listing Web Application Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/list_waf-policy.htm#top).
- From the Actions menu for the policy, select t Move resource .
The Move resource panel opens.
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci waf web-app-firewall-policy change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waf/web-app-firewall-policy/change-compartment.html)command and required parameters to move a web application firewall policy between compartments:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeWebAppFirewallPolicyCompartment](https://docs.oracle.com/iaas/api/#/en/waf/latest/WebAppFirewallPolicy/ChangeWebAppFirewallPolicyCompartment)
