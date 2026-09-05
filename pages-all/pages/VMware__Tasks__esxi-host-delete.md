# Deleting a VMware Solution SDDC ESXi Host
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-delete.htm
- Fetched: 2026-09-05 03:08 CDT

# Deleting a VMware Solution SDDC ESXi Host

Delete (terminate) an ESXi host and remove it from a cluster in the SDDC in VMware Solution.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-delete.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, select the SDDC that contains the ESXi hosts that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the SDDC's details page, select vSphere clusters .
- Select the cluster that contains the ESXi host that you want to delete.
- On the cluster's details page, select ESXi hosts .
- From the the Actions menu (three dots) for the host, select Terminate ESXi host .
- In the Terminate ESXi Host panel, follow the prompts to confirm termination, and select Terminate ESXi host .
- 

Use the[esxi-host delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/esxi-host/delete.html)command and required parameters to delete an ESXi host and remove it from the SDDC:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteEsxiHost](https://docs.oracle.com/iaas/api/#/en/vmware/latest/EsxiHost/DeleteEsxiHost)
