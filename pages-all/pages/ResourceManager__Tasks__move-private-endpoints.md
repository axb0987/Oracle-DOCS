# Moving a Private Endpoint to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/move-private-endpoints.htm
- Fetched: 2026-09-05 02:56 CDT

# Moving a Private Endpoint to a Different Compartment

Move a Resource Manager private endpoint to another compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/move-private-endpoints.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/move-private-endpoints.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/move-private-endpoints.htm#)
- 

- On the Private endpoints list page, select the private endpoint that you want to work with. If you need help finding the list page or the private endpoint, see[Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-private-endpoints.htm).
- On the private endpoint's details page, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/private-endpoint/change-compartment.html)oci resource-manager private-endpoint change-compartment`command to move a private endpoint to another compartment.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Use the[ChangePrivateEndpointCompartment](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpoint/ChangePrivateEndpointCompartment)
