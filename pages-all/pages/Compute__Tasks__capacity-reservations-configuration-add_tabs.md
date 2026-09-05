# Adding a Capacity Configuration
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-configuration-add_tabs.htm
- Fetched: 2026-09-05 01:50 CDT

# Adding a Capacity Configuration

Add a capacity configuration to a capacity reservation using the following steps.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-configuration-add_tabs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-configuration-add_tabs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-configuration-add_tabs.htm#)
- 

- Navigate to the Capacity Reservations list page. If you need help finding the list page, see[Listing Capacity Reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/listing-capacity-reservations.htm).
- Select a capacity reservation.
- Under Capacity configurations , select Add capacity configuration .
- Enter the configuration data:
- Fault domain: Select First available to allow OCI to select the fault domain. Alternately, enter a fault domain.
- Shape: Select the shape to use for instances created against this capacity configuration. If you select a flexible shape, enter values for Cores and Memory (GB) .
- NVMe drives: (If available) Select the number of drives.
- Count: Enter the total number of instances that can be created with this capacity configuration.
- To add additional capacity configurations for shapes, select the option you see:
- Add shape
- + Another shape
- Select Add configuration .
- 

Use the[capacity reservations update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/capacity-reservation/update.html)command and required parameters to create a capacity reservation:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to add a capacity configuration to a capacity reservation:
- [UpdateComputeCapacityReservation](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/UpdateComputeCapacityReservation)
