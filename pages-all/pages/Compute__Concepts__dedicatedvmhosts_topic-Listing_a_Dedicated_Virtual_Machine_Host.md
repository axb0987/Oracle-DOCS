# Listing Dedicated Virtual Machine Hosts
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Listing_a_Dedicated_Virtual_Machine_Host.htm
- Fetched: 2026-09-05 01:49 CDT

# Listing Dedicated Virtual Machine Hosts

List the dedicated virtual machine hosts in a compartment and virtual machine instances on that host.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Listing_a_Dedicated_Virtual_Machine_Host.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Listing_a_Dedicated_Virtual_Machine_Host.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Listing_a_Dedicated_Virtual_Machine_Host.htm#)
- 

List the dedicated virtual machine hosts using the following steps.
- Open the navigation menu.
- Select Compute , under Compute , select Dedicated Virtual Machine Hosts .
- 

To view the resources in a different compartment, use the Compartment filter to switch compartments.
Note  
  
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- Select a dedicated virtual machine host to display the details page.

#### To View Hosted Instances

To see the virtual machines on a host, follow these steps.
- Select a dedicated virtual machine host. The Details page is displayed.
- Select the option you see:
- Select the Hosted Instances tab.
- Under Resources , select Hosted Instances .
- The virtual machines hosted on this dedicated virtual machine host are listed.
- 

To list the available dedicated virtual machine hosts, use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/dedicated-vm-host/list.html)dedicated-vm-host list`command:

```

```

To list the instances running on a dedicated virtual machine host, use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/dedicated-vm-host-instance/list.html)dedicated-vm-host-instance list`command:

```

```

Or use a JSON file.

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to create a capacity reservation:[ListDedicatedVmHostInstances](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DedicatedVmHostInstanceSummary/ListDedicatedVmHostInstances)
