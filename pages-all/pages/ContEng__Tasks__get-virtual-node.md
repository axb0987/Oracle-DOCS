# Getting a Virtual Node's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node.htm
- Fetched: 2026-09-05 01:57 CDT

# Getting a Virtual Node's Details

Find out how to get the details of a virtual node in a virtual node pool using Kubernetes Engine (OKE).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node.htm#)
- 

- On the Clusters list page, select the name of the cluster that contains the virtual node for which you want to see detailed information. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab, and select the name of the virtual node pool that contains the virtual node.
- Select the Virtual nodes tab.
- Select the arrow beside the virtual node for which you want to see detailed information.
- 

Use the[oci ce virtual-node-pool get-virtual-node](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/get-virtual-node.html)command and required parameters to get the details of a virtual node in a virtual node pool:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetVirtualNode](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/GetVirtualNode)
