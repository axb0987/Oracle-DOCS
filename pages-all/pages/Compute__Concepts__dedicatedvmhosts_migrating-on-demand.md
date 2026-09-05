# Managing On-Demand Reboot Migration for Dedicated Virtual Machine Hosts
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_migrating-on-demand.htm
- Fetched: 2026-09-05 01:49 CDT

# Managing On-Demand Reboot Migration for Dedicated Virtual Machine Hosts

You can migrate instances on an OCI dedicated virtual machine host on-demand using the console, CLI, or API. First, select an existing dedicated virtual machine host or set up a new dedicated virtual machine host to serve as the destination host for migrating instances. Then, using the desired method, start the migration process.

Warning  
  
Reboot migration for Dedicated Virtual Machine Hosts is not supported across different availability domains.
Tip  
  
Some downtime is associated with a dedicated virtual machine host as each instance must be stopped and rebooted on the new destination host. You can see the migration process using the work request feature.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_migrating-on-demand.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_migrating-on-demand.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts_migrating-on-demand.htm#)
- 

To migrate a dedicated virtual machine host instance using the console, follow these steps.
- Navigate to the Dedicated Virtual Machine Hosts list page. If you need help finding the list page, see[Listing Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Concepts/dedicatedvmhosts_topic-Listing_a_Dedicated_Virtual_Machine_Host.htm).
- Select the source dedicated virtual machine host.
- The instance details are displayed.
- Select the option you see:
- Select Actions then More actions then Migrate Instance .
- Select More Actions , then select Migrate instance .
- Select the destination dedicated virtual machine host using the host list provide or by specifying the host OCID.
- Select Migrate .
Important  
  
If the selected instance has local NVME on a dense I/O shape, the local storage is deleted during the migration process. In this case, a prompt is provided to confirm the deletion of local resources.
Note  
  
To monitor the migration process, select Work Requests . A job is created for the migration. The progress for that migration is shown in the console.

When the migration is complete, a message is displayed in the console. The destination host shows the new instance, while the old instance doesn't show up in the source host.

Repeat this process for each instance you want to migrate to the destination host.
- 

Use the[instance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html)command and required parameters to update an instance.
```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)
