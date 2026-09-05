# Deleting Capacity Reservations
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-delete.htm
- Fetched: 2026-09-05 01:50 CDT

# Deleting Capacity Reservations

Permanently delete a capacity reservation.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-delete.htm#)
- 

- Navigate to the Capacity Reservations list page. If you need help finding the list page, see[Listing Capacity Reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/listing-capacity-reservations.htm).
- Select the capacity reservation you want to delete.
- Either[terminate (delete) all the instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm)in the capacity reservation, or[move the instances out of the capacity configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-moving-out_tabs.htm).
- Select Delete , and then confirm when prompted.

To track the progress of the operation and[troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#instance-work-requests)that might occur when deleting an instance pool, use the associated[work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
- 

Use the[capacity reservations delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/capacity-reservation/delete.html)command and required parameters to delete capacity reservations:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to delete a capacity reservation:
- [DeleteComputeCapacityReservation](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/DeleteComputeCapacityReservation)
Note
