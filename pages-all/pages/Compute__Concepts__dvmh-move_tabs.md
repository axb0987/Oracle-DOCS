# Moving a Dedicated Virtual Machine Host to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh-move_tabs.htm
- Fetched: 2026-09-05 01:49 CDT

# Moving a Dedicated Virtual Machine Host to a Different Compartment

To move a dedicated virtual machine host to a new compartment see the following steps.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh-move_tabs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh-move_tabs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh-move_tabs.htm#)
- 

- Navigate to the Dedicated Virtual Machine Hosts list page. If you need help finding the list page, see[Listing Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Concepts/dedicatedvmhosts_topic-Listing_a_Dedicated_Virtual_Machine_Host.htm).
- Select a dedicated virtual machine host.
- Select the option you see:
- Select Actions then Move Resource .
- Select Move Resource .
- Choose the destination compartment from the list.
- Select Move Resource .
- Optionally, move the instances that are placed on the dedicated virtual machine host to the new compartment.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/dedicated-vm-host/change-compartment.html)dedicated-vm-host change-compartment`command and required parameters to change the compartment for a dedicated virtual machine host:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to change the compartment for a dedicated virtual machine host:
- [ChangeDedicatedVmHostCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DedicatedVmHost/ChangeDedicatedVmHostCompartment)
