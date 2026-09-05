# Moving a Log Group Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-logging-log-group.htm
- Fetched: 2026-09-05 02:37 CDT

# Moving a Log Group Between Compartments

Move a log group to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-logging-log-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-logging-log-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-logging-log-group.htm#)
- 

When you move a log group to a new compartment, all the logs in the log group move with the log group to the new compartment. After you move the log group to the new compartment, the policies in the new compartment apply immediately, and they affect access to the log group and any logs the log group contains.

For more information, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
Note  
  
You can't move, edit, or delete the default log group.

- On the Log groups list page, find the log group that you want to work with. If you need help finding the list page or the log group, see[Listing Log Groups](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/../Task/list-logging-log-group.htm).
- To view the log groups in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- From the Actions menu (three dots) for the log group, select Move resource .
The Move resource panel opens.
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci logging log-group change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log-group/change-compartment.html)command and required parameters to move a log group between compartments:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ChangeLogGroupCompartment](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogGroup/ChangeLogGroupCompartment)
