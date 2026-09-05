# Listing Virtual Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-nodes.htm
- Fetched: 2026-09-05 01:58 CDT

# Listing Virtual Nodes

Find out how to list the virtual nodes in a virtual node pool using Kubernetes Engine (OKE).

You can list the virtual nodes in a virtual node pool using the Console, the CLI, and the API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-nodes.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-nodes.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-nodes.htm#)
- 

- On the Clusters list page, select the name of the cluster containing the virtual node pool with the virtual nodes you want to see. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab.

Node pools in the cluster are shown in tabular form. Virtual node pools are identified as virtual in the Node type column.
- Select the name of the virtual node pool containing the virtual nodes you want to see, to show the details page.
- Select the Virtual nodes tab.

Virtual nodes in the virtual node pool are shown in tabular form.
- 

Use the[oci ce virtual-node-pool list-virtual-nodes](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/list-virtual-nodes.html)command and required parameters to list virtual nodes in a virtual node pool:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListVirtualNodes](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/ListVirtualNodes)
