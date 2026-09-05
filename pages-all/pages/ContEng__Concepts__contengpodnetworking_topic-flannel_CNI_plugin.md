# Using the flannel CNI plugin for pod networking
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-flannel_CNI_plugin.htm
- Fetched: 2026-09-05 01:53 CDT

# Using the flannel CNI plugin for pod networking

Find out about using the flannel CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine (OKE).

The flannel CNI plugin provides pod networking without using IP addresses from a VCN's CIDR block. Communication between pods is encapsulated in the flannel overlay network, a simple private overlay virtual network that satisfies the requirements of the Kubernetes networking model by attaching IP addresses to containers. The pods in the private overlay network are only accessible from other pods in the same cluster. For more information about flannel, see the[flannel documentation](https://github.com/flannel-io/flannel).

The flannel overlay network uses its own CIDR block to provision pods and worker nodes with IP addresses. The flannel CIDR block is not shared between clusters, so you can specify the same flannel CIDR block for multiple clusters. The default flannel CIDR block is large enough to support 65,534 pods and 512 worker nodes, and can be increased in size to support many more. Moreover, the number of pods per worker node is not determined by the node shape. Therefore, consider using the flannel CNI plugin if the density of pods per node presents an obstacle to the use of the OCI VCN-Native Pod Networking CNI.

You can use the flannel CNI plugin with managed node pools but not with virtual node pools.

You can use the flannel CNI plugin with self-managed nodes. For more information, see[Working with Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengworkingwithselfmanagednodes.htm).

Note that configuring secondary VNICs for pod networking using Application Resources is not supported when using the flannel CNI plugin for pod networking.
