# Creating a Virtual Node Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-virtual-node-pool.htm
- Fetched: 2026-09-05 01:57 CDT

# Creating a Virtual Node Pool

Find out how to create a virtual node pool using Kubernetes Engine (OKE).

You can create virtual node pools when you create a new enhanced cluster using the Console (see[Creating Kubernetes Clusters Using Console Workflows](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm)and[Creating Virtual Nodes and Virtual Node Pools in a New Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingvirtualnodes_topic.htm)).

You can also create new virtual node pools in an existing enhanced cluster to scale up the cluster (see[Adding Node Pools to Scale Up Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingnodepools_topic.htm)).

You can create new virtual node pools using the Console, the CLI, and the API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-virtual-node-pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-virtual-node-pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-virtual-node-pool.htm#)
- 

You can create virtual node pools using the Console:
- When you create a new enhanced cluster using one of the Console workflows (see[Creating Kubernetes Clusters Using Console Workflows](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm)).
- When you want to scale up an existing enhanced cluster by adding additional node pools (see[Adding Node Pools to Scale Up Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingnodepools_topic.htm)).
- 

Use the[oci ce virtual-node-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/create.html)command and required parameters to scale up an enhanced cluster by adding a virtual node pool:

```

```

where:
- `<ad-name>`is the name of the availability domain in which to place virtual nodes. To find out the availability domain name to use, run:

```

```

- `<shape-name>`is one of`Pod.Standard.E3.Flex`,`Pod.Standard.E4.Flex`.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateVirtualNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/CreateVirtualNodePool)
