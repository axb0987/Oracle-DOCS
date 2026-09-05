# Creating a Dedicated Virtual Machine Host
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Creating_a_Dedicated_Virtual_Machine_Host.htm
- Fetched: 2026-09-05 01:49 CDT

# Creating a Dedicated Virtual Machine Host

You must create a dedicated virtual machine host in Compute before you can place any instances on it.

When creating a dedicated virtual machine host, you select an availability domain and fault domain to launch it in. All the VM instances that you place on the host are subsequently created in this availability domain and fault domain.

You also select a compartment when you create the host, but you can move the host to a new compartment later without impacting any of the instances placed on it. You can also create the instances in a different compartment than the host, or move them to different compartments after they have been launched.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Creating_a_Dedicated_Virtual_Machine_Host.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Creating_a_Dedicated_Virtual_Machine_Host.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_topic-Creating_a_Dedicated_Virtual_Machine_Host.htm#)
- 

- Navigate to the Dedicated Virtual Machine Hosts list page. If you need help finding the list page, see[Listing Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Concepts/dedicatedvmhosts_topic-Listing_a_Dedicated_Virtual_Machine_Host.htm).
- Select Create dedicated virtual machine host .
- Enter the following information:
- Name: Enter a name for the host. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- Create in compartment: Select the compartment to create the host in.
- Availability domain Select the availability domain for the host.
- Under the Dedicated host shape section:

Select the[shape](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../References/computeshapes.htm#dedicatedvmhost)to use for the host. Use the option you see:
- Select Edit shape . Select a shape. Select Select shape .
- Select the down arrow in the row for a host shape. Select a shape.
- Optionally, select the option you see:
- Fill in the following information:
- Fault domain: By leaving the default value, OCI selects the fault domain for the host. Otherwise, select your fault domain.
- Tags: Select the tags for this resource.
- Select Show Advanced Options . Then enter the following information:
- Fault domain: By leaving the default value, OCI selects the fault domain for the host. Otherwise, select your fault domain.
- Tags: Select the tags for this resource.
- Select Create .
- 

To create a dedicated virtual machine host, use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/dedicated-vm-host/create.html)dedicated-vm-host create`command:

```

```

Or use a JSON file.

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
Important  
  

It can take up to 15 minutes for the dedicated virtual machine host to be fully created. The host must be in the`ACTIVE`state before you can launch an instance.

To query the current state of a dedicated virtual machine host using the CLI, run the following command:

```

```

- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to create a dedicated virtual machine host:[CreateDedicatedVmHost](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DedicatedVmHost/CreateDedicatedVmHost)
