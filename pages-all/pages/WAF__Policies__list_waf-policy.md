# Listing Web Application Firewall Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/list_waf-policy.htm
- Fetched: 2026-09-05 03:11 CDT

# Listing Web Application Firewall Policies

View a list of the web application firewall policies in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/list_waf-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/list_waf-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/list_waf-policy.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Policies .
The Policies list page opens. All policies are displayed in a table.

The list indicates the name, policy type (WAF Policy or Edge Policy), status, and created date and time (UTC date timestamp) information for each policy.
- To view the WAF policies in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

Note  
  
To access the legacy WAF Edge policies, select the Manage Legacy Edge WAF Policies link above the Search and Filter box. The Edge policies list page opens. For more information, see[Edge Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/../EdgePolicyResources/legacy_waf.htm#legacy_waf).

## Filtering List Results

Use filters to limit the WAF policies in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a WAF policy to open its details page, where you can view its status and perform other tasks.

To perform an action on a WAF policy directly from the list table, select an available option from the Actions menu in the row for that WAF policy:
- View details : Open the details page for the WAF policy.
- Open support request : Open the Support Request panel, in which you can access support options. See[Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
- Delete :[Delete the WAF policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/delete_waf-policy.htm#top).
- Move resource :[Move the WAF policy to another compartment](https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/change-compartment_waf-policy.htm#top).
- Manage tags : Add one or more tags to the WAF policy. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Copy OCID : Copy the OCID of the WAF policy to the clipboard.

To create a WAF policy, select Create WAF policy .

To delete more than one WAF policy at a time, select the checkboxes next to the WAF policy names and then select Delete .
- 

Use the[oci waf web-app-firewall-policy list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waf/web-app-firewall-policy/list.html)command and required parameters to list web application firewall policies in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListWebAppFirewallPolicies](https://docs.oracle.com/iaas/api/#/en/waf/latest/WebAppFirewallPolicy/ListWebAppFirewallPolicies)
