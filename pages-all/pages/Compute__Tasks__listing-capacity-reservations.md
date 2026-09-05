# Listing Capacity Reservations
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/listing-capacity-reservations.htm
- Fetched: 2026-09-05 01:51 CDT

# Listing Capacity Reservations

Get a list of the Compute Capacity Reservations in an Oracle Cloud Infrastructure compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/listing-capacity-reservations.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/listing-capacity-reservations.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/listing-capacity-reservations.htm#)
- 

- 

Open the navigation menu and select Compute . Under Compute , select Capacity Reservations .

The Capacity Reservations list page opens. All existing capacity reservations in the selected compartment are displayed in a list table.
- 

To view the resources in a different compartment, use the Compartment filter to switch compartments.
Note  
  
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

Optionally, you can do the following with a capacity reservation from the list.
- Select an capacity reservation to view the details page.
- From the Actions menu, create and edit capacity reservations, create and stop instances in a capacity reservation, and move instances in and out of capacity reservations.
- 

Use the[capacity reservations list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/capacity-reservation/instance/list.html)command and required parameters to list instances:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to list capacity reservations:
- [ListCapacityReservations](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/ListComputeCapacityReservations)
