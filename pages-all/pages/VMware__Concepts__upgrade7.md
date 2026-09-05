# Upgrading a VMware Solution SDDC from V6 to V7
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/upgrade7.htm
- Fetched: 2026-09-05 03:07 CDT

# Upgrading a VMware Solution SDDC from V6 to V7

You can upgrade the VMware software in an SDDC from version 6 to version 7.

There are significant architectural changes to the platform from vSphere version 6.x to 7.x. To perform the upgrade, the workflow provisions a new vSphere 7.0 SDDC and ESXi hosts on OCI VMware Solution and uses VMware HCX to migrate workloads to the new vSphere 7 SDDC. During the upgrade workflow two more VLANs are required for provisioning and migration. You can[create the VLANs](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/vlan-create.htm)before you start the workflow, or let the workflow create them for you.

Important  
  
The upgrade workflow creates new, upgraded ESXi hosts to replace the old hosts. The new hosts use the hourly billing rate and begin billing as soon as they're active. The workflow requires you to delete the old hosts after you verify that the new hosts are functioning correctly. After the old host is deleted, the new host is updated to use the billing interval of the old host. Be sure to delete old hosts in a timely manner to avoid unnecessary charges. See[Transferring VMware Solution Billing Commitments](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/swap-billing.htm)for more information.

Important  
  
You can't upgrade an SDDC and its hosts directly from version 6 to version 8. You must first[upgrade from version 6 to version 7](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/upgrade7.htm), then[upgrade again from version 7 to version 8](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/upgrade8.htm).

## Using the Console

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

Optionally, create two more VLANs that the workflow can use for provisioning and migration. For more information, see[Managing Layer 2 Networking Resources for a VMware Solution SDDC](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/ocvsmanagingl2net.htm).

- On the Software-Defined Data Centers list page, select the SDDC that you want to upgrade. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/sddc-list.htm).
- In the upgrade notification on the SDDC's details page, select Upgrade .
- In the Upgrade SDDC panel, enter the required information:
- Select the new version.
- Update network: You can either select VLANs for provisioning and migration that have already been created, or the workflow can create them for you.
- If you select Select existing VLANs, select a replication and a provisioning VLAN.
- If you select Create new VLANs , specify the following information:

- Create in compartment: Select a compartment for the VLANs. Be sure it's a compartment that you have permission to work in.
- Name: Enter a friendly name for the VLAN. Avoid entering confidential information.
- CIDR: Enter an available CIDR block in the selected VCN for the SDDC management CIDR.
- Route table name: Enter a friendly name for the route table used for mapping VLAN traffic.
- Network security group (NSG) name: Enter a friendly name for the NSG associated with the VLAN.
- 

(Optional) Select Show NSG details to view or edit the information for the network security group for each VLAN.
- Select Upgrade .
- When the SDDC upgrade is complete, a notification appears in the SDDC details page where you can download updated licenses and binaries:
- Select Get updated binaries and licenses .
- After downloading, visit vCenter and update the licenses and binaries with the updated versions. See[VMware Upgrade Documentation](https://docs.vmware.com/en/VMware-Validated-Design/6.2/sddc-upgrade/GUID-C9304835-A31C-4F6B-A7A7-07DFAA70D993.html)for more information.
- When you're finished, check I have updated the binaries and licenses in vCenter and select Next .
- Upgrade the ESXi hosts:
- Select a host in the list.
- In the host's Upgrade notification, select Upgrade .
- In the Upgrade ESXi host page, select on-demand or use capacity reservations . For more information, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm).
- (Optional) Enable notifications for the host. See[Configuring VMware Solution SDDC Notifications](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/vmware-notifications.htm)for more information.
- Check I understand that I must delete the old host after the new host is successfully created, or I will be charged for both hosts , then select Upgrade .
Upgrading a host can take time. Select Work Requests to view the progress of the upgrade.
- When the upgrade has successfully been completed for each host, delete the old hosts.

Important  
  
The new hosts use the hourly billing rate and begin billing as soon as they're active. After the old host is deleted, the new host is updated to use the billing interval of the old host. Be sure to delete old hosts in a timely manner to avoid unnecessary charges.
- A notification appears in the SDDC Details page that the old hosts have been upgraded. In the notification, select the name of an old host.
-
