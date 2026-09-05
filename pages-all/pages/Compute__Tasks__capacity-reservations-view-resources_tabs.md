# Viewing Capacity Configuration Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-view-resources_tabs.htm
- Fetched: 2026-09-05 01:50 CDT

# Viewing Capacity Configuration Resources

View the capacity configuration resources for a capacity reservation using the following steps.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-view-resources_tabs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-view-resources_tabs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-view-resources_tabs.htm#)
- 

- Navigate to the Capacity Reservations list page. If you need help finding the list page, see[Listing Capacity Reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/listing-capacity-reservations.htm).
- Select a capacity reservation.
- In the Capacity configurations section, you can see the total reserved capacity and the total used capacity for each configuration.
- (Optional) To see the instances that are created in the capacity reservation, select the option you see:
- Scroll down to Created instances .
- Under Resources , select Created instances .
- 

Use the[capacity reservations get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/capacity-reservation/get.html)command and required parameters to get information about a capacity configuration:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to get information about a capacity configuration for a capacity reservation:
- [GetComputeCapacityReservation](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/GetComputeCapacityReservation)
