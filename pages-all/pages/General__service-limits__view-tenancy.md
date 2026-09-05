# Viewing a Tenancy's Limits and Usage
- Source: https://docs.oracle.com/en-us/iaas/Content/General/service-limits/view-tenancy.htm
- Fetched: 2026-09-05 02:13 CDT

# Viewing a Tenancy's Limits and Usage

View limits and usage for a tenancy in Oracle Cloud Infrastructure.

For default limits, see[Limits by Service](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/default.htm). This information is also helpful if you don't yet have a tenancy or a user account for the Console, or if you don't find a particular limit listed.

For Multicloud limits, see[Quotas and Service Limits for Multicloud](https://docs.oracle.com/iaas/Content/multicloud/quotas-limits.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/view-tenancy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/view-tenancy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/view-tenancy.htm#)
- 

You can view a tenancy's limits and usage (by region) in the Console. Be aware of the following considerations:
- The Console might not display limits and usage information for all the Oracle Cloud Infrastructure services or resources.
- The usage level listed for a particular resource type could be greater than the limit if the limit was reduced after the resources were created.
- If all the resource limits are listed as 0, this means your account has been suspended. For help,[contact Oracle Support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).

To view limits and usage:

- Open the navigation menu and select Governance &amp; Administration . Under Tenancy Management , select Limits, Quotas and Usage .

The Limits, Quotas and Usage list page opens.
- Use filters to select the service, subscription, scope, and compartment. You can also select the resource, if available.

If you see Edit filters , select it and use the Edit filters panel to make your selections.
Note  
  
The Subscription field is only selectable for certain combinations of service and scope. For example, when selecting the Database service and a particular Scope , a &lt;subscription_ID&gt; - &lt;subscription_name&gt; subscription can be selected, and the Limits, Quotas and Usage page reloads to display the limits specific to the associated subscription.

All service limits for the selected filters are displayed in a table with the following information:
- Description
- Limit Name
- Status : Current state of the limit, such as active or deprecated.
- Service Limit : The limit total.
- Usage : How much of the limit resource has been used.
- Available : The limit remainder ( Service Limit value minus Usage value).
- (Optional) If you see Show deprecated limits , select it to show deprecated limits. If you don't see this option, deprecated limits are already included in the list.

## Filtering List Results

Use filters to further limit the service limits in the list.

From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

To perform an action on a service limit directly from the list table, select an available option from the Actions menu in the row for that service limit:
- Create quota policy stub :[Create a quota policy stub](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm#top__quickstart)for the service limit.
- Open support request : Open the Support Request panel, in which you can access support options. See[Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
- 

Use the[oci limits resource-availability get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/limits/resource-availability/get.html)command and required parameters to list information for the specified compartment, limit, and service:

```

```

If the scope type of the limit is AD (availability domain), then include the`--availability-domain`parameter:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetResourceAvailability](https://docs.oracle.com/iaas/api/#/en/limits/latest/ResourceAvailability/GetResourceAvailability)operation to list limits for the specified service, scope, and compartment.

## Fractional Usage and Availability

Some resources can have fractional usage and availability, and the Service Limits API reflects this accordingly. If the resource is a fractional one, usage reflects the rounded up value of the fractional usage, and for availability, the rounded down value of the fractional availability. As a result, these fractional availability and usage attributes help indicate the most accurate usage and availability.

For example, if a resource has 2.4 used, 4.6 available, the following API response is returned:
```

```

For more information, see the`available`and`used`attributes in the[ResourceAvailability Reference](https://docs.oracle.com/iaas/api/#/en/limits/latest/ResourceAvailability/)
