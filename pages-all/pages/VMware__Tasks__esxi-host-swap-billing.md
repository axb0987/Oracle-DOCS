# Swapping Billing Between Active VMware Solution SDDC Hosts
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-swap-billing.htm
- Fetched: 2026-09-05 03:08 CDT

# Swapping Billing Between Active VMware Solution SDDC Hosts

Swap billing between the active hosts in an SDDC in VMware Solution.

Over time, you might have many hosts in the SDDCs, all with different billing commitments and end dates. You can transfer billing commitments between hosts in the same or different SDDC according to the business and organization requirements. For more information, see[Transferring VMware Solution Billing Commitments](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/swap-billing.htm).

You can swap billing between active hosts. For more information, see[Transferring VMware Solution Billing Commitments](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/swap-billing.htm).

## Using the Console

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, select the SDDC that contains the ESXi host that you want to swap billing for. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the SDDC's details page, select vSphere clusters .
- Select the cluster that contains the ESXi host that you want to swap billing for.
- On the cluster's details page, select ESXi hosts .
- From the the Actions menu (three dots) for the host, select Swap billing .
- In the Billing swap panel, select the compartment that contains the host you want, and then select the host you want. The host list includes those that have billing amounts available for swap.
-
