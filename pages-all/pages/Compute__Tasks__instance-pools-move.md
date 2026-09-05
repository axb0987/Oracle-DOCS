# Moving an Instance Pool to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-move.htm
- Fetched: 2026-09-05 01:51 CDT

# Moving an Instance Pool to a Different Compartment

After you create an instance pool, you can move it to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-move.htm#)
- 

- Navigate to the Instance pools list page. If you need help finding the list page, see[Listing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instance-pools-list.htm).
- Select the instance pool that you're interested in.
- Select the option you see:
- Actions then Move resource .
- More actions then Move resource .
- Choose the destination compartment from the list.
- Select Move resource . Your instance pools is moved to the new compartment.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/3.56.1/oci_cli_docs/cmdref/compute-management/instance-pool/change-compartment.html)instance-pool change-compartment`command to move a instance pool to another compartment:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to move an instance pool to a different compartment:
- [ChangeInstancePoolCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/ChangeInstancePoolCompartment)
