# Replacing a VMware Solution SDDC Failed ESXi Host
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-replace.htm
- Fetched: 2026-09-05 03:08 CDT

# Replacing a VMware Solution SDDC Failed ESXi Host

If an ESXi host in an SDDC in VMware Solution fails because of hardware issues, you can start a workflow to replace it.

SDDCs are customer-managed after provisioning, so the host replacement procedure requires that you also perform specific actions in the SDDC.
Important  
  
After you start the host replacement workflow, you must perform the required steps within a 24-hour period, or you're billed for both the failed host and the replacement.

The configuration and pricing interval of the replacement host duplicates the failed host as it existed at the time of its initial deployment.

## Using the Console

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, select the SDDC that contains the failed ESXi host. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the SDDC's details page, select vSphere clusters .
- Select the cluster that contains the failed ESXi host.
- On the cluster's details page, select the failed ESXi host.
- From the the Actions menu (three dots) for the host, select Replace host .
- In the Replace host panel update the following:

- Release name: Select an appropriate release name to match your vCenter version.
- Licenses
- VMware Cloud Foundation License allocation compartment: Select the target compartment.
- VMware Cloud Foundation License allocation: Select the license allocation.

For more information on license allocations see[Listing VMware Solution License Allocations](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-list.htm).
- Select Acknowledge and proceed and then perform one of the following actions depending on the option that you see:

- Select Replace host .
- Select Confirm .

A work request to create a new host is created. You can view the work request by selecting Work requests . Host provisioning can take up to one hour.
Tip  
  
To cancel the replacement, go to the cluster's details page and select Cancel replacement in the Host replacement in progress notification.
- After the new host is provisioned, remove the failed host from the SDDC, and add the replacement host. You must complete this step within 24 hours after the new host is provisioned.
- Mark the replacement process as complete:
- On the Software-Defined Data Centers list page, select the SDDC that contains the replaced ESXi host. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the SDDC's details page, find the Remove failed host notification, and select Mark as complete .
