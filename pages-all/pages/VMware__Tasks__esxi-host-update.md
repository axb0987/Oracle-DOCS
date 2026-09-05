# Editing a VMware Solution SDDC ESXi Host
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-update.htm
- Fetched: 2026-09-05 03:08 CDT

# Editing a VMware Solution SDDC ESXi Host

Edit information for an ESXi host in an SDDC cluster in VMware Solution, such as its name or pricing interval.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-update.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, select the SDDC that contains the ESXi hosts that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the SDDC's details page, select vSphere clusters .
- Select the cluster that contains the ESXi hosts that you want to edit.
- On the cluster's details page, select ESXi hosts .
- Select the host that you want to edit.
- On the ESXi host's details page, select Edit .
- In the Edit ESXi host panel, update any of the following information:

- ESXi host name : Enter a new name for the host. The ESXi host name must be 1 to 25 characters, start with a letter, and contain only alphanumeric characters and hyphens (`-`). Hyphens can't be next to each other. Ensure that the name is unique within the SDDC. Avoid entering confidential information.
Important  
  
ESXi host names can have a maximum of 25 characters including the prefix. Host FQDNs can have a maximum of 64 characters total.
- Change next pricing interval : Select a new pricing interval for the host.
Important  
  
The new pricing interval doesn't take effect until the previous billing interval's end date and time. If you cancel the commitment before the end of the selected pricing interval, billing continues until the interval ends.
- Select deleted ESXi host for billing continuation : Select the compartment that contains the host you want, and then select the deleted host that you want for billing continuation. You can transfer the leftover billing commitment from a deleted host to an active host. Only deleted hosts with the same shape, and CPU as the active host are available for use. For more information, see[Transferring VMware Solution Billing Commitments](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/swap-billing.htm).
- Enable monitoring : Optionally enable monitoring and provide information about alarms and notifications. For more information, see[Configuring VMware Solution SDDC Notifications](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/vmware-notifications.htm).
- Perform one of the following actions depending on the option that you see:

- Select Update .
- Select Save Changes .
- 

Use the[esxi-host update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/esxi-host/update.html)command and required parameters to edit an ESXi host:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateEsxiHost](https://docs.oracle.com/iaas/api/#/en/vmware/latest/EsxiHost/UpdateEsxiHost)
