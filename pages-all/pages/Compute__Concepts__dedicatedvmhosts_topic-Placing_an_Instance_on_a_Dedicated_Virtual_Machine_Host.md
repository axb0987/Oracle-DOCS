# Placing Instances on a Dedicated Virtual Machine Host
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Placing_an_Instance_on_a_Dedicated_Virtual_Machine_Host.htm
- Fetched: 2026-09-05 01:49 CDT

# Placing Instances on a Dedicated Virtual Machine Host

You place an instance on a dedicated virtual machine host at the time that you create the instance.

## Listing the Dedicated Virtual Machine Hosts That Have Capacity

The dedicated virtual machine host must have[sufficient capacity](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm#optimize-capacity)for the shape of instance that you want to create. In the Console, when you create an instance, you can only select from the dedicated virtual machine hosts that have enough capacity for the shape that you specify.

You can use the API, CLI, or SDKs to determine which dedicated virtual machine hosts have capacity for a particular shape. Use the[ListDedicatedVmHosts Instance: Change Instance Compartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DedicatedVmHostSummary/ListDedicatedVmHosts)API operation, passing the name of the shape that you want to use when launching the instance. For flexible shapes, you can also include the minimum number of OCPUs and amount of memory you want to provision.

The following example shows how to use the CLI to return all the dedicated virtual machine hosts with enough capacity for you to place an instance using the`VM.Standard.E4.Flex`shape with 8 OCPUs and 10 GB memory:

```

```

## Checking the Capacity of a Dedicated Virtual Machine Host

To inspect detailed capacity information for a specific dedicated virtual machine host, including capacity-bin details, use the OCI CLI Compute`dedicated-vm-host get`command. For example:

```

```

For more information, see[Optimizing Capacity on a Dedicated Virtual Machine Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm#optimize-capacity).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Placing_an_Instance_on_a_Dedicated_Virtual_Machine_Host.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Placing_an_Instance_on_a_Dedicated_Virtual_Machine_Host.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Placing_an_Instance_on_a_Dedicated_Virtual_Machine_Host.htm#)
- 

To place an instance on a dedicated host, follow these steps using the Console or API.
- Follow the steps to[create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/launchinginstance.htm), until the Placement section.
- In the Placement section, select Show advanced options .
- For Capacity type , select Dedicated host .
- Select the dedicated virtual machine host that you want to place the instance on.
- Finish configuring the instance, and then select Create .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html)instance launch`command and required parameters to create an instance:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance)operation to create the instance, passing the OCID of the dedicated virtual machine host in the`dedicatedVmHostId`
