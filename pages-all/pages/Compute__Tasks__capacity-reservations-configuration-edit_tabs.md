# Editing a Capacity Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-configuration-edit_tabs.htm
- Fetched: 2026-09-05 01:50 CDT

# Editing a Capacity Configuration

Edit a capacity configuration for a capacity reservation using the following steps.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-configuration-edit_tabs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-configuration-edit_tabs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-configuration-edit_tabs.htm#)
- 

- Navigate to the Capacity Reservations list page. If you need help finding the list page, see[Listing Capacity Reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/listing-capacity-reservations.htm).
- Select a capacity reservation.
- Under Capacity configurations , for a capacity configuration from the Actions menu (three dots), select Edit .
- For Count , enter a new value. The value must be greater than or equal to the number of instances in this configuration.
- Select Save changes .
- 

Use the[capacity reservations update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/capacity-reservation/update.html)command and required parameters to edit a capacity configuration:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to edit a capacity configuration for a capacity reservation:
- [UpdateComputeCapacityReservation](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/UpdateComputeCapacityReservation)
