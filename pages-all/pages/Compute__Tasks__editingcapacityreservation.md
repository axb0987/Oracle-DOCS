# Changing the Capacity Reservation for an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/editingcapacityreservation.htm
- Fetched: 2026-09-05 01:51 CDT

# Changing the Capacity Reservation for an Instance

You can move instances into or out of[capacity reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)without having to rebuild your instances. Capacity reservations let you reserve instances in advance so that the capacity is available for your workloads when you need it.

For permissions, see[Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-permissions).

## Before You Begin

To move an instance into a capacity reservation, you must have an existing capacity reservation. For steps to create capacity reservations, see[Capacity Reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/editingcapacityreservation.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/editingcapacityreservation.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/editingcapacityreservation.htm#)
- 

Use the Console to move an instance into or out of capacity reservations.

## To move instances into a capacity reservation

- Navigate to the Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).
- Select an instance.
- Select the option you see:
- Actions then More Actions then Edit .
- More Actions then Edit .
- Select Show advanced options , and then select the Placement tab.
- Select the Apply a capacity reservation checkbox.
- For Capacity reservation , select the capacity reservation that you want to move the instance into.
- Select Save changes .

## To move instances out of a capacity reservation

- Navigate to the Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).
- Select an instance.
- Select the option you see:
- Actions then More Actions then Edit .
- More Actions then Edit .
- Select Show advanced options , and then select the Placement tab.
- Clear the Apply a capacity reservation checkbox.
- Select Save changes .
- 

Use the[instance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html)command and required parameters to update an instance:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute Service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).

- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to move instances into and out of capacity reservations:
- [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)
