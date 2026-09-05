# Adding a Firewall to a Web Application Firewall Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/create_firewall.htm
- Fetched: 2026-09-05 03:10 CDT

# Adding a Firewall to a Web Application Firewall Policy

Add a firewall to a web application firewall (WAF) policy to create a logical link between the policy and an enforcement point, such as a load balancer.

You can generate security logs for your firewalls after you create your WAF policy. We recommend enabling security logs as it provides valuable insight into your WAF performance. For more information, see[Setting Up Firewall Logging](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/../Protections/setting_up_logging_analytics.htm#top).

Configure your load balancer with an HTTP listener. Fore more information, see[Listeners for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managinglisteners.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/create_firewall.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/create_firewall.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/create_firewall.htm#)
- 

- On the Policies list page, select the policy that you want to work with. If you need help finding the list page or the policy, see[Listing Web Application Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/../Policies/list_waf-policy.htm#top).
The policy's details page opens.
- From the details page, select Firewalls .
The Firewalls list opens. All firewalls are displayed in a table.
- From the Actions menu (three dots) for the firewall, select Add firewalls .
The Add firewalls panel opens.

## Firewall

Enter the following information:
- Firewall name : Enter the name of the firewall.
- Create in compartment : Select the compartment that contains the firewall you are creating.
- Load balancer compartment : Select the compartment containing the load balancer you want from the list.
- Load balancer : Select the load balancer from the list.

## Tags

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.

Select Add firewalls .

The firewall you created appears in the Firewalls list.
- 

Use the[oci waf web-app-firewall create-for-load-balancer](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waf/web-app-firewall/create-for-load-balancer.html)command and required parameters to add a firewall to a web application firewall policy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateWebAppFirewall](https://docs.oracle.com/iaas/api/#/en/waf/latest/WebAppFirewall/CreateWebAppFirewall)
