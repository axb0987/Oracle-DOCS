# Changing the Shape to Use for Pods Running on Virtual Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengchangevirtualnodepoolpodshape.htm
- Fetched: 2026-09-05 01:54 CDT

# Changing the Shape to Use for Pods Running on Virtual Nodes

Find out how to update a virtual node pool's pod shape property to change the processor type on which to run pods, using Kubernetes Engine (OKE).

The type of processor used for pods running on virtual nodes in a virtual node pool is determined by the virtual node pool's pod shape property. Having created a virtual node pool, you might decide that you want pods to run on a different type of processor.

You can change the type of processor by performing an out-of-place node pool update. When you perform an out-of-place update, you replace the original virtual node pool with a new node pool that has the required pod shape.

You first create a new virtual node pool and specify the pod shape you require. Next, you drain existing virtual nodes in the original virtual node pool to prevent new pods from starting and to delete existing pods. Then, you delete the original virtual node pool.

When new pods start, they run on new virtual nodes in the new virtual node pool, and use the new pod shape you specified.

For more information and detailed instructions, see[Performing an Out-of-Place Virtual Node Update by Replacing an Existing Virtual Node Pool with a New Virtual Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingvirtualnodesupdatedprops_topic-Performing_an_OutofPlace_Virtual_Node_Update_by_Replacing_an_Existing_Node_Pool_with_a_New_Node_Pool.htm)
