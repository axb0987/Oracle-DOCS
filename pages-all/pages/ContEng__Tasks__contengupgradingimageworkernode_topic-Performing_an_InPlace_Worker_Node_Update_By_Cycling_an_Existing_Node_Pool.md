# Performing an In-Place Worker Node Update by Cycling Nodes in an Existing Node Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-Performing_an_InPlace_Worker_Node_Update_By_Cycling_an_Existing_Node_Pool.htm
- Fetched: 2026-09-05 01:56 CDT

# Performing an In-Place Worker Node Update by Cycling Nodes in an Existing Node Pool

Find out how to update the properties of worker nodes in a node pool by changing properties of the existing node pool, and then cycling the nodes, using Kubernetes Engine (OKE).
Note  
  
You can only cycle nodes to perform an in-place worker node update when using enhanced clusters. See[Working with Enhanced Clusters and Basic Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenhancedclusters.htm).

You can cycle nodes with both virtual machine shapes and bare metal shapes.

This section applies to managed nodes only.

You can update the properties of worker nodes in a node pool by changing properties of the existing node pool, and then cycling the nodes. When you cycle the nodes, you select one of the following options:
- Replace boot volume: Kubernetes Engine automatically cordons and drains existing worker nodes. The boot volume of the instance hosting each worker node is then replaced, without terminating the instance. When instances return to a Running state, updates to supported properties are applied to the worker nodes they host. For more information, see[Updating Worker Nodes in an Existing Node Pool by Replacing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-InPlace_Worker_Node_Update_By_Cycling_and_Replacing_Boot_Volumes.htm).
- Replace nodes: Kubernetes Engine automatically cordons, drains, and terminates existing worker nodes, and creates new worker nodes. When new worker nodes are started in the existing node pool, they have the updated properties you specified. For more information, see[Updating Worker Nodes in an Existing Node Pool by Terminating and Replacing Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-InPlace_Worker_Node_Update_By_Cycling_and_Replacing_Nodes.htm)
