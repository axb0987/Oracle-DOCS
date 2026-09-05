# Changing the Shape of an Instance on a Dedicated Virtual Machine Host
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh_changing_shape_dedicated_virtual_machine_host.htm
- Fetched: 2026-09-05 01:49 CDT

# Changing the Shape of an Instance on a Dedicated Virtual Machine Host

Change the shape of instances on a dedicated virtual machine host.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh_changing_shape_dedicated_virtual_machine_host.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh_changing_shape_dedicated_virtual_machine_host.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh_changing_shape_dedicated_virtual_machine_host.htm#)
- 

You can change the shape of an instance on a dedicated virtual machine host using the following steps.
- Navigate to the Dedicated Virtual Machine Hosts list page. If you need help finding the list page, see[Listing Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Concepts/dedicatedvmhosts_topic-Listing_a_Dedicated_Virtual_Machine_Host.htm).
- Select a the dedicated virtual machine host to see the details page.
- Select the option you see:
- Select the Hosted instances tab.
- Under Resources , select Hosted instances .
- From the Actions menu (three dots), select the hosted instance to change.
- The instance details are displayed.
- Select the option you see:
- Select Actions then More actions then Edit .
- Select More actions then Edit .
- Select the option you see:
- Scroll down to the Shape Summary section.
- Select Edit shape .
- From the Shape summary select and change the options as needed. Options include:
- Shape series
- Shape name
- Number of OCPUs
- Amount of memory
Note  
  
Only shapes that support dedicated version machine host are displayed.
- After making your shape selections, select Save changes .
Important  
  
For Dense I/O shapes , select the I understand that local storage will be deleted box to confirm local storage is deleted and cannot be recovered when the change is made.
- Select Reboot instance to start the shape change process.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html)instance update`command and required parameters to update an instance.
```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)
