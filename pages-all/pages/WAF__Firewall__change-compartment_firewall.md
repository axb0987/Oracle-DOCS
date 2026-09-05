# Moving Firewalls in a Web Application Firewall Policy to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/change-compartment_firewall.htm
- Fetched: 2026-09-05 03:10 CDT

# Moving Firewalls in a Web Application Firewall Policy to a Different Compartment

Move a firewall contained within a web application firewall policy to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/change-compartment_firewall.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/change-compartment_firewall.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/change-compartment_firewall.htm#)
- 

- On the Policies list page, select the policy that you want to work with. If you need help finding the list page or the policy, see[Listing Web Application Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/../Policies/list_waf-policy.htm#top).
The policy's details page opens.
- From the details page, select Firewalls .
The Firewalls list opens. All firewalls are displayed in a table.
- From the Actions menu (three dots) for the firewall, select Move resource .
The Move resource panel opens.
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci waf web-app-firewall change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waf/web-app-firewall/change-compartment.html)command and required parameters to move a firewall contained within a web application firewall policy between compartments:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeWebAppFirewallCompartment](https://docs.oracle.com/iaas/api/#/en/waf/latest/WebAppFirewall/ChangeWebAppFirewallCompartment)
