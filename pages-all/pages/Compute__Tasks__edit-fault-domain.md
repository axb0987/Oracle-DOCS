# Editing the Fault Domain for an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-fault-domain.htm
- Fetched: 2026-09-05 01:51 CDT

# Editing the Fault Domain for an Instance

You can change the fault domain where a virtual machine (VM) instance is placed.

A fault domain is a grouping of hardware and infrastructure that is distinct from other fault domains in the same availability domain. By properly leveraging fault domains you can increase the availability of applications running on Oracle Cloud Infrastructure. For more information and best practices, see[Fault Domains](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/bestpracticescompute.htm#Fault).

For permissions, see[Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-permissions).

## Supported Shapes

You can change the fault domain for instances that use these shapes:
- VM.Standard1 series
- VM.Standard.B1 series
- VM.Standard2 series
- VM.Standard3.Flex
- VM.Standard4.Ax.Flex
- VM.Standard.E2 series
- VM.Standard.E3.Flex
- VM.Standard.E4.Flex
- VM.Standard.E5.Flex
- VM.Standard.E6.Flex
- VM.Standard.E6.Ax.Flex
- VM.Standard.A4.Flex
- VM.Standard.A4.Ax.Flex
- VM.GPU3 series
- VM.GPU.A10 series
- VM.Optimized3.Flex

These shapes cannot be edited:
- VM.Standard.E2.1.Micro
- VM.GPU2 series
- VM.DenseIO1 series
- VM.DenseIO2 series
- VM.DenseIO.E4.Flex
- VM.DenseIO.E5.Flex
- VM.DenseIO.E6.Ax.Flex
- VM instances that run on dedicated virtual machine hosts
- Bare metal shapes

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-fault-domain.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-fault-domain.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-fault-domain.htm#)
- 

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).
- Select an instance.
- Select the option you see:
- Select Actions then More actions then Edit .
- Select More actions then Edit .
- Select the option you see:
- Edit the Fault domain field and select a new fault domain.
- Select Edit fault domain . Then, select a new fault domain.
- Select Save changes .

If the instance is running, it's rebooted. Confirm when prompted.
- 

Use the[instance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html)command and required parameters to update an instance:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute Service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).

- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to change the fault domain for an instance:
- [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)
