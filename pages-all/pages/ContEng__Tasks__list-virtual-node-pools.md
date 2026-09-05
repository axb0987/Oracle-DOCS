# Listing Virtual Node Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-node-pools.htm
- Fetched: 2026-09-05 01:58 CDT

# Listing Virtual Node Pools

Find out how to list virtual node pools using Kubernetes Engine (OKE).

You can list virtual node pools using the Console, the CLI, and the API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-node-pools.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-node-pools.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-node-pools.htm#)
- 

- On the Clusters list page, select the name of the cluster containing the virtual node pools you want to see. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab.

Node pools in the cluster are shown in tabular form. Virtual node pools are identified as virtual in the Node type column.
- To see more detail about a virtual node pool, select the name of the node pool and use the tabs on the details page.
- 

Use the[oci ce virtual-node-pool list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/list.html)command and required parameters to list virtual node pools:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListVirtualNodePools](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePoolSummary/ListVirtualNodePools)
