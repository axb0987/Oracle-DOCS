# Creating a Capacity Reservation
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-create_tabs.htm
- Fetched: 2026-09-05 01:50 CDT

# Creating a Capacity Reservation

To create a capacity reservation see the following steps.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-create_tabs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-create_tabs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-create_tabs.htm#)
- 

Capacity is allocated when the reservation is created. If sufficient capacity isn't available to complete the request, the capacity reservation is created with as many instances as possible. For example, if you request 50 instances and only 40 are available, a capacity reservation with 40 instances is created. If no capacity is available, a reservation with capacity for zero instances is made. If the requested shape does not exist in the region, the reservation is not made, and an error occurs.

To see how much capacity is reserved, after the reservation request completes,[view capacity usage](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-view-resources_tabs.htm)in the Console or use the[GetComputeCapacityReservation](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/GetComputeCapacityReservation)operation. To know when the capacity reservation request is complete, use[work requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm).

Creating a capacity reservation consists of the following pages:
- 1. Add basic details
- 2. Add capacity configurations
- Review and create reservation
Note  
  
Run each of the workflows in order. You can return to a previous page by selecting Previous .

## 1. Add basic details

- Navigate to the Capacity Reservations list page. If you need help finding the list page, see[Listing Capacity Reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/listing-capacity-reservations.htm).
- Select Create capacity reservation .
- On the Add basic details page, do the following:
- Name: Enter a name for the capacity reservation. Avoid entering confidential information.
- Compartment: Select the compartment for the reservation and all instances created with this reservation.
- Availability domain: Select the availability domain for the reservation and all instances created with this reservation.
- Make this capacity reservation the default for this availability domain: To make this the default reservation, select the check box. If selected, when an instance is created in this availability domain, it counts against this reservation, regardless of which compartment the instance is in. If a different capacity reservation is already set as the default in this availability domain, this capacity reservation replaces it as the default.
- (Optional) Select the option you see:
- Advanced options: Select Advanced options to add tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Show tagging options: Select Show tagging options to add tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Select Next .

## 2. Add capacity configurations

On the Add capacity configurations page, create one or more capacity configurations. Do the following:
- Fault domain: By default select First available to allow OCI to select the fault domain. Alternately, enter a fault domain.
- Shape: Select the shape to use for instances created against this capacity configuration. If you select a flexible shape, enter values for Cores and Memory (GB) .
- NVMe drives: (If available) Select the number of drives.
- Count: Enter the total number of instances that can be created with this capacity configuration.
- To add additional capacity configurations for shapes, select the option you see:
- Add shape
- + Another shape
- Select Next .

## Review and create reservation

Review the capacity reservation and capacity configuration information, and then select Create .
- 

Use the[capacity reservations create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/capacity-reservation/create.html)command and required parameters to create a capacity reservation:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to create a capacity reservation:
- [CreateComputeCapacityReservation](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/CreateComputeCapacityReservation)
