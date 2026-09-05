# Listing Private Endpoints
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm
- Fetched: 2026-09-05 02:56 CDT

# Listing Private Endpoints

List private endpoints in Resource Manager.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm#)
- 

- Open the navigation menu and select Developer Services . Under Resource Manager , select Private Endpoints .
The Private endpoints list page opens. All private endpoints in the selected compartment are displayed in a table.
- To view the private endpoints in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the private endpoints in the list.
- To filter the list by tag, select add next to Tag filters .

## Actions

In the list table, select the name of a private endpoint to open its details page, where you can view its status and perform other tasks.

To perform an action on a private endpoint directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that private endpoint:
- View private endpoint details :[Open the details page for the private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoints.htm).
- View security attributes : View the private endpoint's security attributes. For information about security attributes, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
- Add security attributes :[Add or delete security attributes for an endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-private-endpoint-security.htm). For information about security attributes, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
- Delete private endpoint :[Delete the private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-private-endpoints.htm).

To create a private endpoint, select Create private endpoint .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/private-endpoint/list.html)oci resource-manager private-endpoint list`command to list private endpoints.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[ListPrivateEndpoints](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpointSummary/ListPrivateEndpoints)
