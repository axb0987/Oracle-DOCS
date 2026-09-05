# Listing Web Application Firewall Policy Firewalls in a Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/list_firewall.htm
- Fetched: 2026-09-05 03:10 CDT

# Listing Web Application Firewall Policy Firewalls in a Compartment

View a list of the firewalls contained in a web application firewall policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/list_firewall.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/list_firewall.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/list_firewall.htm#)
- 

- On the Policies list page, select the policy that you want to work with. If you need help finding the list page or the policy, see[Listing Web Application Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/../Policies/list_waf-policy.htm#top).
The policy's details page opens.
- From the details page, select Firewalls .
The Firewalls list opens. All firewalls are displayed in a table.
- To view the firewalls in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the firewalls in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a firewall to open its details page, where you can view its status and perform other tasks.

To perform an action on a firewall directly from the list table, select an available option from the Actions menu in the row for that firewall
- View details :[Open the details page for the firewall](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/get_firewall.htm#top).
- Delete :[Delete the firewall](https://docs.oracle.com/en-us/iaas/Content/WAF/Firewall/delete_firewall.htm#top).
- Copy OCID : Copy the OCID of the firewall to the clipboard.

To add a firewall, select Add firewalls from the Actions menu .

To delete more than one firewall at a time, select the checkboxes next to the firewall names and then select Delete .
- 

Use the[oci waf web-app-firewall list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waf/web-app-firewall/list.html)command and required parameters to list the web application firewall policy firewalls in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListWebAppFirewalls](https://docs.oracle.com/iaas/api/#/en/waf/latest/WebAppFirewall/ListWebAppFirewalls)
