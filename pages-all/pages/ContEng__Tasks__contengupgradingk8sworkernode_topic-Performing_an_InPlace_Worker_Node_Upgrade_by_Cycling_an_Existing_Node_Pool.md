# Performing an In-Place Managed Node Kubernetes Upgrade by Cycling Nodes in an Existing Node Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode_topic-Performing_an_InPlace_Worker_Node_Upgrade_by_Cycling_an_Existing_Node_Pool.htm
- Fetched: 2026-09-05 01:56 CDT

# Performing an In-Place Managed Node Kubernetes Upgrade by Cycling Nodes in an Existing Node Pool

Find out how to upgrade the Kubernetes version on managed nodes in a node pool by changing properties of the existing node pool, and then cycling the nodes, using Kubernetes Engine (OKE).
Note  
  
You can cycle nodes to perform an in-place managed node Kubernetes upgrade when using enhanced clusters only. See[Working with Enhanced Clusters and Basic Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenhancedclusters.htm).

You can cycle nodes with both virtual machine shapes and bare metal shapes.

This section applies to managed nodes only. For information about upgrading self-managed nodes, see[Upgrading Self-Managed Nodes to a Newer Kubernetes Version by Replacing an Existing Self-Managed Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingselfmanagednodes.htm).

You can upgrade the version of Kubernetes running on managed nodes in a node pool by specifying a more recent Kubernetes version for the existing node pool, and then cycling the nodes. When you cycle the nodes, you select one of the following options:
- Replace boot volume: Kubernetes Engine automatically cordons and drains existing worker nodes. The boot volume of the instance hosting each worker node is then replaced, without terminating the instance. When instances return to a Running state, the worker nodes they host are running the more recent Kubernetes version you specified. For more information, see[Upgrading Managed Nodes by Replacing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-InPlace_Worker_Node_Upgrade_By_Cycling_and_Replacing_Boot_Volumes.htm).
- Replace nodes: Kubernetes Engine automatically cordons, drains, and terminates existing worker nodes, and creates new worker nodes. When new worker nodes are started in the existing node pool, they run the more recent Kubernetes version you specified. For more information, see[Upgrading Managed Nodes by Terminating and Replacing Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-InPlace_Worker_Node_Upgrade_By_Cycling_and_Replacing_Nodes.htm)
