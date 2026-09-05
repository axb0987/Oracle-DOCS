# Editing a VMware Solution SDDC Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-edit.htm
- Fetched: 2026-09-05 03:08 CDT

# Editing a VMware Solution SDDC Cluster

Edit a cluster in an SDDC in VMware Solution.

You can change the cluster's name or change monitoring configuration.

To work with ESXi hosts in the cluster, see the following pages:
- [Creating a VMware Solution SDDC ESXi Host](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-create.htm)
- [Editing a VMware Solution SDDC ESXi Host](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-update.htm)
- [Deleting a VMware Solution SDDC ESXi Host](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/esxi-host-delete.htm)

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-edit.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-edit.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-edit.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, select the SDDC that contains the cluster that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the SDDC's details page, select vSphere clusters .
- Select the cluster that you want to edit.
- On the cluster's details page, perform one of the following actions depending on the option that you see:

- Edit Cluster
- Edit
The Edit cluster panel opens.
- (Optional) Update the settings you want to change.

- Display name : Optionally change the cluster name. The cluster name must be 1 to 22 characters, start with a letter, and contain only non-accented letters, numbers, and hyphens (`-`). Hyphens can't be next to each other. Avoid entering confidential information.
- Optional: Select any available add-ons:
- VMware vDefend Firewall License allocation compartment: Select the target compartment.
- VMware vDefend Firewall License allocation: Select the license allocation.

For more information on license allocations see[Listing VMware Solution License Allocations](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-list.htm).
- Tags: Edit or add tags.
- Notifications

Configure Enable monitoring : Optionally enable monitoring and provide information about alarms and notifications. For more information, see[Configuring VMware Solution SDDC Notifications](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/vmware-notifications.htm).
- Select Update .
- 

Use the[cluster update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/cluster/update.html)command and required parameters to update a cluster:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateCluster](https://docs.oracle.com/iaas/api/#/en/vmware/latest/Cluster/UpdateCluster)
