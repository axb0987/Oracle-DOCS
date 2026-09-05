# Creating a VMware Solution SDDC ESXi Host
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-create.htm
- Fetched: 2026-09-05 03:08 CDT

# Creating a VMware Solution SDDC ESXi Host

Create an ESXi host in an SDDC cluster in VMware Solution.

Note  
  
A single host SDDC is restricted to one cluster containing one ESXi host. If a single host SDDC already has a host, you can't create any more hosts.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-create.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, select the SDDC that you want to add an ESXi host to. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the SDDC's details page, select vSphere clusters .
- Select the cluster that you want to add an ESXi host to.
- On the cluster's details page, select ESXi hosts .
- Select Create ESXi host .
- In the Create ESXi host panel, enter the following information:

Important  
  
An SDDC or ESXi host which has failed provisioning doesn't get billed until provisioning succeeds.

## Create ESXi Host

- ESXi host name (optional): Enter a name for the new host that helps to identify it later.The ESXi host name must be 1 to 25 characters, start with a letter, and contain only alphanumeric characters and hyphens (`-`). Hyphens can't be next to each other. Avoid entering confidential information.
Important  
  
ESXi host names can have a maximum of 25 characters including the prefix. Host FQDNs can have a maximum of 64 characters total.
- Release name : Select an appropriate release name to match your vCenter version.

## Shape

Select a shape to use for ESXi hosts in the SDDC. A shape is a template that decides the number of CPUs, amount of memory, and other resources allocated to a newly created instance. If you select a shape with an AMD processor, select the number of cores. See[Supported Shapes](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#supported-shapes)for more information.

## Tags

Select Tags to add tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)for details.

## Capacity type

Select a capacity type to use when the ESXi hosts are created.
- On-demand capacity provisions the compute capacity when the host is created.
- Capacity reservation uses capacity that's counted against an existing reservation. Select a compartment and the name of a reservation. For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm).
Note  
  
Capacity reservation isn't supported for an SDDC that uses many availability domains.

## Pricing Interval Commitment

The dialog you see depends on the license type selected.

### Bring your own license

Select the BYOL details.
- Compartment : Select the compartment that contains your license allocation.
- License allocation: Select the license allocation for this resource.

Select You are responsible at all times for maintaining active and compliant VMware software licenses and versions on all OCVS hosts .

### License-included

Select the pricing interval to apply to the ESXi hosts. Choices include:
- Hourly
- Monthly
- One year
- Three year

Select Pricing interval must be confirmed to continue .

For more information about available pricing intervals, see[Billing Options](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#billing-options).
Note  
  
Select a deleted host for billing continuation (optional): When you create a host, you can reuse the leftover billing commitment from a deleted host. Only deleted hosts with the same shape, CPU, and SKU as you selected for the new host are available for use. If you don't see the deleted host that you want, try changing the shape selection. For more information, see[Transferring VMware Solution Billing Commitments](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/swap-billing.htm).

## Create ESXi Host

Select ESXi host details (optional): View or change VMware software version, compartment, SSH key, availability domain, and VLANs.

When you're satisfied with the properties for this host, select Create ESXi host .
- 

Use the[esxi-host create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/esxi-host/create.html)command and required parameters to create an ESXi host:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
Important  
  
An SDDC or ESXi host which has failed provisioning doesn't get billed until provisioning succeeds.
- 

Run the[CreateEsxiHost](https://docs.oracle.com/iaas/api/#/en/vmware/latest/EsxiHost/CreateEsxiHost)operation to create an ESXi host.
Important
