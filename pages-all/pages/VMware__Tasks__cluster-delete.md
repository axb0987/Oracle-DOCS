# Deleting a VMware Solution SDDC Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-delete.htm
- Fetched: 2026-09-05 03:08 CDT

# Deleting a VMware Solution SDDC Cluster

Delete (terminate) a cluster in a VMware Solution SDDC.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/cluster-delete.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, select the SDDC that contains the cluster that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the SDDC's details page, select vSphere clusters .
- From the Actions menu (three dots) for the cluster, select Terminate .
The Terminate SDDC Cluster panel opens.
- To delete networking resources, select Terminate Networking Resources .
- To delete datastore resources, select Delete datastore resources .
This option is shown only when the SDDC contains a cluster that uses a standard shape. For other shapes, the option isn't relevant.
- Follow the prompts to confirm termination, and select Terminate all .
- 

Use the[cluster delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/cluster/delete.html)command and required parameters to delete a cluster:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteCluster](https://docs.oracle.com/iaas/api/#/en/vmware/latest/Cluster/DeleteCluster)
