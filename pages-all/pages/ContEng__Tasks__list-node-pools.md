# Listing Managed Node Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-node-pools.htm
- Fetched: 2026-09-05 01:58 CDT

# Listing Managed Node Pools

Find out how to list managed node pools using Kubernetes Engine (OKE).

You can list managed node pools using the Console, the CLI, and the API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-node-pools.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-node-pools.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-node-pools.htm#)
- 

- On the Clusters list page, select the name of the cluster containing the node pools you want to see. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab.

Node pools in the cluster are shown in tabular form.
- To see more detail about an individual node pool, select the name of the node pool and use the tabs on the details page.
- 

Use the[oci ce node-pool list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/list.html)command and required parameters to list managed node pools:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListNodePools](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePoolSummary/ListNodePools)
