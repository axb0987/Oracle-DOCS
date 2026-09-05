# Upgrading Managed Nodes to a Newer Kubernetes Version
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode.htm
- Fetched: 2026-09-05 01:56 CDT

# Upgrading Managed Nodes to a Newer Kubernetes Version

Find out about the different ways to upgrade the Kubernetes version on managed nodes in clusters you've created with Kubernetes Engine (OKE).
Note  
  

This section applies to managed nodes only. For information about upgrading self-managed nodes, see[Upgrading Self-Managed Nodes to a Newer Kubernetes Version by Replacing an Existing Self-Managed Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingselfmanagednodes.htm).

This section describes upgrading managed nodes to a newer Kubernetes version. To roll back managed nodes in an existing managed node pool to an earlier available Kubernetes version, see[Rolling Back Managed Nodes to an Earlier Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_Rolling-Back.htm).

You can upgrade the version of Kubernetes running on the managed nodes in a cluster in the following ways:
- Perform an 'in-place' upgrade, by specifying a more recent Kubernetes version for new managed nodes starting in the existing node pool, and then cycling the nodes. First, you modify the existing node pool's properties to specify the more recent Kubernetes version. Then, you cycle the nodes in the node pool. When you cycle the nodes, you select one of the following options:
- Replace boot volume: Kubernetes Engine automatically cordons and drains existing worker nodes. The boot volume of the instance hosting each worker node is then replaced, without terminating the instance. When instances return to a Running state, the worker nodes they host are running the more recent Kubernetes version you specified.
- Replace nodes: Kubernetes Engine automatically cordons, drains, and terminates existing worker nodes, and creates new worker nodes. When new worker nodes are started in the existing node pool, they run the more recent Kubernetes version you specified.

For more information, see[Performing an In-Place Managed Node Kubernetes Upgrade by Cycling Nodes in an Existing Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode_topic-Performing_an_InPlace_Worker_Node_Upgrade_by_Cycling_an_Existing_Node_Pool.htm).
- Perform an 'in-place' upgrade, by specifying a more recent Kubernetes version for new managed nodes starting in the existing node pool, and then manually deleting and replacing each existing node with a new managed node. First, you modify the existing node pool's properties to specify the more recent Kubernetes version. Then, you delete each managed node in turn, selecting appropriate cordon and drain options to prevent new pods starting and to delete existing pods. You start a new managed node to take the place of each managed node you delete. When new managed nodes are started in the existing node pool, they run the more recent Kubernetes version you specified. See[Performing an In-Place Managed Node Kubernetes Upgrade by Manually Deleting and Replacing Nodes in an Existing Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode_topic-Performing_an_InPlace_Worker_Node_Upgrade_by_Updating_an_Existing_Node_Pool.htm).
- Perform an 'out-of-place' upgrade, by replacing the original node pool with a new node pool. First, you create a new node pool with a more recent Kubernetes version. Then, you drain existing managed nodes in the original node pool to prevent new pods starting, and to delete existing pods. Finally, you delete the original node pool. When new managed nodes are started in the new node pool, they run the more recent Kubernetes version you specified. See[Performing an Out-of-Place Managed Node Kubernetes Upgrade by Replacing an Existing Node Pool with a New Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode_topic-Performing_an_OutofPlace_Worker_Node_Upgrade_by_Replacing_an_Existing_Node_Pool_with_a_New_Node_Pool.htm).

Note that in all cases:
- The more recent Kubernetes version you specify for the managed nodes in the node pool must be compatible with the Kubernetes version running on the control plane nodes in the cluster. See[Upgrading Clusters to Newer Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengaboutupgradingclusters.htm).
-
