# Upgrading a VMware Solution SDDC From V7 to V8
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/upgrade8.htm
- Fetched: 2026-09-05 03:07 CDT

# Upgrading a VMware Solution SDDC From V7 to V8

You can upgrade the VMware software in an SDDC from version 7 to version 8.

When the upgrade becomes available, a message and Upgrade button is provided on the details page of the SDDC that you use to begin the workflow when you're ready. The upgrade workflow is a combination of automated processes and prompts for manual processes that you must perform in a specific order. The upgrade workflow doesn't let you proceed in the upgrade until each step has been completed. Before you begin the upgrade, review the steps carefully to be sure you understand the process.
Important  
  
The steps on this page provide an overview of the upgrade process. If you require a detailed explanation of each step, see:[Upgrade an Oracle Cloud VMware Solution Software-Defined Data Center from 7.x to 8.x](https://docs.oracle.com/en/learn/upgrade-ocvs-sddc-7-to-8/). Administrators must complete the VMware recommended steps before terminating the old instances.
Warning  
  
Upgrading a VMware Solution SDDC requires an experienced administrator. If you are unsure of the steps required for the upgrade process, please refer to:[Upgrade an Oracle Cloud VMware Solution Software-Defined Data Center from 7.x to 8.x](https://docs.oracle.com/en/learn/upgrade-ocvs-sddc-7-to-8/). Administrators must complete the VMware recommended steps before terminating the old instances.
Important  
  
You can't upgrade an SDDC and its hosts directly from version 6 to version 8. You must first[upgrade from version 6 to version 7](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/upgrade7.htm), then[upgrade again from version 7 to version 8](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/upgrade8.htm).

Prerequisites
Follow these prerequisite steps to ensure compatibility and protect against potential data loss:
- 

Check upgrade compatibility
Use the[VMware Upgrade Path Interoperability Matrix](https://interopmatrix.vmware.com/Upgrade)to verify support for the upgrade path:
- VMware ESXi : Upgrading from[7.0u3 to 8.0u2](https://interopmatrix.vmware.com/Upgrade?productId=1)
- VMware vCenter Server : Upgrading from[7.0.3 to 8.0.2](https://interopmatrix.vmware.com/Upgrade?productId=2)
- VMware NSX : Upgrading from[3.2.2 to 4.1.2](https://interopmatrix.vmware.com/Upgrade?productId=912)
- 

Perform necessary backups

Before you upgrade, be sure that you have backups of all SDDC components. This step is crucial to restore configurations if the upgrade fails or if you have issues with any of the virtual machines (VMs). Backups provide the necessary restore points to address any issues that might arise during or after the upgrade process.
- SDDC components backup : Follow the VMware backup procedure documentation for[vCenter Server Configuration](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vcenter.install.doc/GUID-8C9D5260-291C-44EB-A79C-BFFF506F2216.html),[NSX Configuration](https://docs.vmware.com/en/VMware-NSX/4.0/administration/GUID-E6181BF1-2CB7-4870-B508-BFAF5B47D702.html), and[vDS Switch Configuration Backup](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.networking.doc/GUID-BE48C292-F222-4095-BCF8-D6444A785E16.html).
- ESXi host configuration Backup : Back up all the[configuration of ESXi hosts](https://knowledge.broadcom.com/external/article/313510/how-to-back-up-and-restore-the-esxi-host.html)in the SDDC.
- VM Backups : Use the backup tool you prefer to create backups of all VMs in the SDDC.
- 

Verify unified management cluster size

Verify that the management cluster is configured with at least four hosts. Having the correct number of hosts allows seamless upgrades and is especially important for NSX. If the cluster only has three hosts, consider adding a fourth host or manually managing VM migrations during the upgrade.
- 

Verify administrative privileges

Verify that you have the necessary administrative privileges within OCI, vCenter, NSX Manager, and HCX Manager. These permissions are required for managing SDDC resources, including hosts, clusters, network configurations, and datastores. For more information on configuring privileges for OCI VMware Solution, see[VMware Solution Identity and Access Management (IAM) Policies](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Reference/iam-policy-reference.htm).
- 

Verify environment compatibility

Verify that all VMware and third-party products in the environment are compatible and compliant with the new VMware version, verifying interoperability across all integrated systems.

## Using the Console

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- Upgrade the SDDC:
- On the Software-Defined Data Centers list page, select the SDDC that you want to upgrade. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/sddc-list.htm).
- In the upgrade notification at the top of the SDDC's details page, select Upgrade .
- In the Upgrade SDDC panel, select the new version.
- Select Upgrade .
- Upgrade the SDDC management cluster:
- On the Software-Defined Data Centers list page, select the SDDC that contains the management cluster that you want to upgrade. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/sddc-list.htm).
- On the SDDC's details page, select vSphere clusters .
- Select the management cluster.
- In the upgrade notification at the top of the management cluster's details page, select Upgrade
- In the Upgrade Cluster panel, select the new version.
- Select Upgrade .
- Upgrade vCenter:
- Go back to the management cluster's details page:

- On the Software-Defined Data Centers list page, select the SDDC that contains the vCenter that you want to upgrade. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/sddc-list.htm).
- On the SDDC's details page, select vSphere clusters .
- Select the management cluster.
- In the upgrade notification at the top of the management cluster's details page, select the option that you see:

- Download updated binaries and licenses
- Get updated binaries and licenses
The Binaries and licenses details panel opens, listing binaries and licenses. Each binary has a download option and each key has a copy option.
Note  
  
Binaries must be downloaded within 7 days of selecting this option.
- After downloading, visit vCenter and update the licenses and binaries with the updated versions in the following order:

- NSX components
- vCenter server appliance
- vSphere cluster
- When you're finished, go back to the management cluster's details page:

- On the Software-Defined Data Centers list page, select the SDDC that contains the management cluster. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/sddc-list.htm).
- On the SDDC's details page, select vSphere clusters .
- Select the management cluster.
- On the details page, select I have updated the binaries and licenses in vCenter . Then, select Next .
- Upgrade the ESXi hosts in the management cluster:
- On the Software-Defined Data Centers list page, select the SDDC that contains the management cluster that you want to upgrade. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/sddc-list.htm).
- On the SDDC's details page, select vSphere clusters .
- Select the management cluster.
- In the management cluster upgrade notification on the management cluster's details page, select Upgrade cluster hosts .
- In the Upgrade Status list, perform one of the following actions depending on the option that you see:

- From the Actions menu (three dots) for the cluster that you want to upgrade, select Update software version .

This option is available when VMware software version lists a version number in orange for that cluster.

Then, in the panel listing hosts in the cluster, from the Actions menu (three dots) for the host that you want to upgrade, select Update software version .

The Upgrade ESXi Host panel opens.
- Select the Upgrade available link for a host in the list.

A list of all hosts in the management cluster with an available upgrade appears.
- Licenses

Select the following:
- VMware Cloud Foundation License allocation compartment: Select the target compartment.
- VMware Cloud Foundation License allocation: Select the license allocation.

For more information on license allocations see[Listing VMware Solution License Allocations](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/license-allocation-list.htm).
- Notifications

(Optional) Select Enable monitoring to enable notifications for the host. For more information, see[Configuring VMware Solution SDDC Notifications](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/vmware-notifications.htm).
- Select I understand that I must delete the old host after the new host is successfully created, or I will be charged for both hosts , then select Upgrade .
- Repeat steps a-e for each host in the management cluster.

Caution  
  
Upgrading more than one host at a time can impact SDDC performance.
- When all ESXi hosts in the cluster have been successfully upgraded, delete the old hosts.

Important  
  
The new hosts use the hourly billing rate and begin billing as soon as they're active. After the old host is deleted, the new host is updated to use the billing interval of the old host. Be sure to delete old hosts in a timely manner to avoid unnecessary charges. You can't undo deleting an old host.
- [Navigate to the management cluster's details page.](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/cluster-get.htm)
- A notification appears in the management cluster's details page that the old host has been upgraded. In the notification, select the name of the old host.
- In the old host's details page, select Terminate .
- Select Terminate ESXi host to confirm.
Note  
  
Old hosts that still need to be deleted have a status of Needs attention in the ESXi hosts lists.
- When the upgrade is complete for all hosts in the management cluster, upgrade each workload cluster and its ESXi hosts in turn:
- Use the instructions in step 2 to upgrade the workload cluster.
- Use the instructions in step 4 to upgrade the workload cluster hosts.

Note  
  
You can't proceed to upgrading workload clusters until hosts in the management cluster have completed upgrading, and you delete the old hosts.

Tip  
  

- Upgrading SDDCs, clusters, and hosts can take a significant amount of time. Here are some ways you can view progress:
- In the SDDC details page, select Upgrade Status to view hosts being upgraded.
- Select Work Requests to view details about the work request associated with an upgrade.
-
