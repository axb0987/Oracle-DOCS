# Upgrading the Kubernetes Version on Worker Nodes in a Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingworkernodes.htm
- Fetched: 2026-09-05 01:57 CDT

# Upgrading the Kubernetes Version on Worker Nodes in a Cluster

Find out about the different ways to upgrade the Kubernetes version on worker nodes in clusters you've created with Kubernetes Engine (OKE).

You upgrade managed nodes, self-managed nodes, and virtual nodes differently:
- Managed node upgrade: You upgrade worker nodes in one of the following ways:
- By performing an 'in-place' upgrade of a node pool in the cluster, specifying a more recent Kubernetes version for the existing node pool, and then cycling the nodes to either replace the boot volumes of the instances hosting existing worker nodes, or to terminate and replace existing worker nodes.
- By performing an 'in-place' upgrade of a node pool in the cluster, specifying a more recent Kubernetes version for the existing node pool, and then manually deleting and replacing each existing worker node with a new worker node.
- By performing an 'out-of-place' upgrade of a node pool in the cluster, replacing the original node pool with a new node pool for which you've specified a more recent Kubernetes version.

For more information about managed node upgrade, see[Upgrading Managed Nodes to a Newer Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode.htm). To roll back managed nodes in an existing managed node pool to an earlier available Kubernetes version, see[Rolling Back Managed Nodes to an Earlier Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_Rolling-Back.htm).
- Self-managed node upgrade: You upgrade self-managed nodes by replacing an existing self-managed node with a new self-managed node hosted on a new compute instance. For more information about self-managed node upgrade, see[Upgrading Self-Managed Nodes to a Newer Kubernetes Version by Replacing an Existing Self-Managed Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingselfmanagednodes.htm).
- Virtual node upgrade: You upgrade virtual nodes by upgrading the control plane nodes in a cluster. When you upgrade the Kubernetes version running on control plane nodes, the virtual nodes in every virtual node pool in the cluster are also automatically upgraded to that Kubernetes version. For more information about virtual node upgrade, see[Upgrading Virtual Nodes to a Newer Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingvirtualnodes.htm)
