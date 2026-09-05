# Moving an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/inst-move.htm
- Fetched: 2026-09-05 01:51 CDT

# Moving an Instance

Move a Compute instance to another Oracle Cloud Infrastructure compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/inst-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/inst-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/inst-move.htm#)
- 

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).
- Select an instance.
- Select the option you see:
- From Actions , select More actions then select Move Resource .
- From More actions select Move Resource .
- Select the destination compartment from the list.
- Select Move Resource .
Tip  
  
If alarms are monitoring the instance, update the alarms to reference the new compartment. See[Updating an Alarm After Moving a Resource](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm)for more information.
- 

Use the[instance change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/change-compartment.html)command and required parameters to move an instance to a new compartment:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to move an instance to another compartment:
- [ChangeInstanceCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/ChangeInstanceCompartment)
