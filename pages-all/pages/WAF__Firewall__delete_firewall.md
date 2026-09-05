# Deleting a Firewall from a Web Application Firewall Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/delete_firewall.htm
- Fetched: 2026-09-05 03:10 CDT

# Deleting a Firewall from a Web Application Firewall Policy

Remove a firewall from a web application firewall policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/delete_firewall.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/delete_firewall.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/delete_firewall.htm#)
- 

- On the Policies list page, select the policy that you want to work with. If you need help finding the list page or the policy, see[Listing Web Application Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/../Policies/list_waf-policy.htm#top).
The policy's details page opens.
- From the details page, select Firewalls .
The Firewalls list opens. All firewalls are displayed in a table.
- From the Actions menu (three dots) for the firewall, select Delete .
- When prompted, confirm the deletion.
- 

Use the[oci waf web-app-firewall delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waf/web-app-firewall/delete.html)command and required parameters to delete a firewall from a web application firewall policy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteWebAppFirewall](https://docs.oracle.com/iaas/api/#/en/waf/latest/WebAppFirewall/DeleteWebAppFirewall)
