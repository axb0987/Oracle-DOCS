# Creating a Managed Node Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-node-pool.htm
- Fetched: 2026-09-05 01:57 CDT

# Creating a Managed Node Pool

Find out how to create a managed node pool using Kubernetes Engine (OKE).

You can create managed node pools when you create a new cluster using the Console (see[Creating Kubernetes Clusters Using Console Workflows](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm)).

You can also create new managed node pools in an existing cluster to scale up the cluster (see[Adding Node Pools to Scale Up Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingnodepools_topic.htm)).

You can create new managed node pools using the Console, the CLI, and the API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-node-pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-node-pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-node-pool.htm#)
- 

You can create managed node pools using the Console:
- When you create a new cluster using one of the Console workflows (see[Creating Kubernetes Clusters Using Console Workflows](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm)).
- When you want to scale up an existing cluster by adding additional node pools (see[Adding Node Pools to Scale Up Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingnodepools_topic.htm)).
- 

Use the[oci ce node-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/create.html)command and required parameters to scale up a cluster by adding a managed node pool:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/CreateNodePool)
