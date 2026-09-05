# Updating Virtual Node Pool Properties
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingvirtualnodepool.htm
- Fetched: 2026-09-05 01:55 CDT

# Updating Virtual Node Pool Properties

Find out how to modify properties of existing virtual node pools using Kubernetes Engine (OKE).

You can change the following properties of a virtual node pool:
- the name of the node pool
- the number of virtual nodes in the node pool, and the availability domains and fault domains in which to place them
- the subnet configured to host virtual nodes, and the network security group to control access to the virtual node subnet
- the subnet configured to host pods, and the network security group to control access to the pod subnet
- Kubernetes labels and taints to enable the targeting of workloads at specific node pools

For information about how to change these properties, see[Updating a Virtual Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-virtual-node-pool.htm).

You can also change the type of processor used for pods running on virtual nodes by specifying a different pod shape for a virtual node pool. For more information, see[Changing the Shape to Use for Pods Running on Virtual Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengchangevirtualnodepoolpodshape.htm)
