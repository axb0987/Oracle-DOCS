# Deleting a Service Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-sgw.htm
- Fetched: 2026-09-05 02:43 CDT

# Deleting a Service Gateway

Delete a service gateway in a Virtual Cloud Network (VCN) to remove access to the Oracle Services Network (OSN).

Prerequisite: The service gateway doesn't have to block traffic, but there must not be a route table that lists it as a target.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-sgw.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-sgw.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-sgw.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Service Gateways section.
- Under Resources , select Service Gateways .
- From the Actions menu (three dots) for the gateway you want to delete, select Terminate .
- When prompted, confirm the deletion.
- 

Use the[network service-gateway delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/delete.html)command and required parameters to delete a service gateway:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/DeleteServiceGateway)
