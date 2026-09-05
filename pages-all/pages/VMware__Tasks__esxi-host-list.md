# Listing a VMware Solution SDDC's ESXi Hosts
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-list.htm
- Fetched: 2026-09-05 03:08 CDT

# Listing a VMware Solution SDDC's ESXi Hosts

Use VMware Solution to view a list of all ESXi hosts in a specific SDDC.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-list.htm#)
- 

- On the Software-Defined Data Centers list page, select the SDDC that contains the ESXi hosts that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the SDDC's details page, select vSphere clusters .
- Select the cluster that contains the ESXi hosts that you want to work with.
- On the cluster's details page, select ESXi hosts .
- 

Note  
  
In terms of implementation, an ESXi host is a Compute instance that is configured with the chosen bundle of VMware software. Each`EsxiHost`object has its own OCID (`id`), and a separate attribute for the OCID of the Compute instance (`computeInstanceId`). When filtering the list of ESXi hosts, you can specify the OCID of the Compute instance, not the ESXi host OCID.

Use the[esxi-host list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/esxi-host/list.html)command and required parameters to view all ESXi hosts in an SDDC:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListEsxiHosts](https://docs.oracle.com/iaas/api/#/en/vmware/latest/EsxiHostSummary/ListEsxiHosts)
