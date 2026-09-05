# Getting a Virtual Node Pool's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node-pool.htm
- Fetched: 2026-09-05 01:57 CDT

# Getting a Virtual Node Pool's Details

Find out how to get details of a specific virtual node pool using Kubernetes Engine (OKE).

You can get details of a specific virtual node pool using the Console, the CLI, and the API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node-pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node-pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node-pool.htm#)
- 

To get details of a virtual node pool in a cluster using the Console:
- On the Clusters list page, select the name of the cluster containing the virtual node pool for which you want to see detailed information. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab.

Node pools in the cluster are shown in tabular form. Virtual node pools are identified as virtual in the Node type column.
- Select the name of the virtual node pool for which you want to see detailed information.
- 

Use the[oci ce virtual-node-pool get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/get.html)command and required parameters to get details of a virtual node pool:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetVirtualNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/GetVirtualNodePool)
