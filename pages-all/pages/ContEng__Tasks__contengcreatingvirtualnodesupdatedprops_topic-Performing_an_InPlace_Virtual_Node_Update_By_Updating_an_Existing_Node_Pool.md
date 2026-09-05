# Performing an In-Place Virtual Node Update by Reducing Node Count to Zero, Updating Node Properties, and then Increasing Node Count
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingvirtualnodesupdatedprops_topic-Performing_an_InPlace_Virtual_Node_Update_By_Updating_an_Existing_Node_Pool.htm
- Fetched: 2026-09-05 01:55 CDT

# Performing an In-Place Virtual Node Update by Reducing Node Count to Zero, Updating Node Properties, and then Increasing Node Count

Find out how to update the properties of virtual nodes in a virtual node pool by changing properties of the existing virtual node pool, using Kubernetes Engine (OKE).

You can update the properties of virtual nodes in a virtual node pool by changing properties of the existing virtual node pool.

You reduce the existing virtual node pool's Node count property to zero and save the change. Then you update the existing node pool's virtual node properties as required. Finally, you increase the virtual node pool's Node count property to the required size. When the new virtual nodes are started in the existing virtual node pool, they have the updated properties you specified.

## Using the Console

To perform an 'in-place' update of a virtual node pool in a cluster:
- On the Clusters list page, select the name of the cluster where you want to update virtual node properties. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- 

Select the Node pools tab, and then select the name of the virtual node pool where you want to update virtual node properties.
- 

On the Virtual node pool details tab, from the Actions menu, select Edit and set Node count to 0 (zero).
- 

Select Update to save the change.

Existing virtual nodes in the virtual node pool are removed.
- 

From the Actions menu, select Edit and update the properties for virtual nodes as required.
- 

Select Update to save the changes.
- 

From the Actions menu, select Edit and set Node count to the number of virtual nodes that you require in the virtual node pool.
- 

Select Update to save the change.
