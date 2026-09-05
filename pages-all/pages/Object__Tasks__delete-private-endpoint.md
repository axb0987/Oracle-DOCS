# Deleting a Private Endpoint from Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/delete-private-endpoint.htm
- Fetched: 2026-09-05 02:50 CDT

# Deleting a Private Endpoint from Object Storage

Remove an Object Storage private endpoint from your Oracle Cloud Infrastructure tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/delete-private-endpoint.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/delete-private-endpoint.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/delete-private-endpoint.htm#)
- 

- On the Private endpoints list page, select the Object Storage private endpoint that you want to work with. If you need help finding the list page or the Object Storage private endpoint, see[Listing Private Endpoints in Object Storage](https://docs.oracle.com/iaas/Content/Object/Tasks/list-private-endpoint.htm).
- From the Actions menu for the private endpoint, select Delete .
- When prompted, confirm the deletion.

The Object Storage private endpoint you deleted no longer appears in the list after it's deletion is complete.
- 

Use the[oci os private-endpoint delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/private-endpoint/delete.html)command and required parameters to delete a private endpoint from Object Storage:

```

```

for example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the following API operation:
```

```
