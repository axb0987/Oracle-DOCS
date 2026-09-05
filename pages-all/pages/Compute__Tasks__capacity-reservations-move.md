# Moving a Capacity Reservation
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-move.htm
- Fetched: 2026-09-05 01:50 CDT

# Moving a Capacity Reservation

Move a capacity reservation to another compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-move.htm#)
- 

- Navigate to the Capacity Reservations list page. If you need help finding the list page, see[Listing Capacity Reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/listing-capacity-reservations.htm).
- Select the capacity reservation.
- Select the option you see:
- Actions then Move resource .
- Move resource .
- Choose the destination compartment from the list.
- Select Move resource .
- 

Use the[capacity reservations changecompartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/capacity-reservation/change-compartment.html)command and required parameters to move a capacity reservation to a different compartment:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to move a capacity reservation to a different compartment:
- [ChangeComputeCapacityReservationCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/ChangeComputeCapacityReservationCompartment)
