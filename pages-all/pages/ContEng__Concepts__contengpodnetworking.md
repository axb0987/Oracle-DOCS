# Pod Networking
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking.htm
- Fetched: 2026-09-05 01:53 CDT

# Pod Networking

Find out about communication to and from pods on worker nodes in clusters created using Kubernetes Engine (OKE).

The Kubernetes networking model assumes pods have unique and routable IP addresses within a cluster. In the Kubernetes networking model, pods use those IP addresses to communicate with each other, with the cluster's control plane nodes, with pods on other clusters, with other services (such as storage services), and with the internet. Kubernetes has adopted the Container Network Interface (CNI) specification for network resource management. The CNI consists of a specification and libraries for writing plugins to configure network interfaces in Linux containers, along with a number of supported plugins.

Kubernetes clusters use CNI plugins to implement network connectivity for pods running on worker nodes. CNI plugins configure network interfaces, provision IP addresses, and maintain connectivity.
When creating a Kubernetes cluster with Kubernetes Engine, the network type you select for the cluster determines the CNI plugin that is used for pod networking:
- if you select VCN-native pod networking as the network type, the OCI VCN-Native Pod Networking CNI plugin is used for pod networking (see[Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm))
- if you select Flannel overlay as the network type, the flannel CNI plugin is used for pod networking (see[Using the flannel CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-flannel_CNI_plugin.htm))

All the node pools in a cluster use the same CNI plugin. After a cluster has been created, you cannot change the CNI plugin you originally selected for it. The CNI plugin used for pod networking is considered an essential cluster add-on. When you specify a cluster's network type, the cluster and its node pools initially use the latest version of the corresponding CNI plugin. Updates to the CNI plugins are released periodically. In the case of the flannel CNI plugin (and versions of the OCI VCN-Native Pod Networking CNI plugin prior to version 2.3.0), you can specify that you want Oracle to deploy the updates on the cluster automatically, or you can specify that you want to choose the version to deploy. If you decide to choose the version, you are taking responsibility for keeping the add-on up-to-date. See[Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengconfiguringclusteraddons.htm).

You can use Calico to implement Kubernetes NetworkPolicy resources. Network policies increase the granularity of cluster security by using labels to select pods and to define rules that specify what traffic is allowed to the selected pods. Calico is an open source networking and network security solution for containers, virtual machines, and native host-based workloads. See[Example: Installing Calico and Setting Up Network Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengsettingupcalico.htm).

You can use the OCI VCN-Native Pod Networking CNI plugin with both virtual node pools and managed node pools. You can use the flannel CNI plugin with managed node pools.

You can use both the OCI VCN-Native Pod Networking CNI plugin and the flannel CNI plugin with self-managed nodes. For more information, see[Working with Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengworkingwithselfmanagednodes.htm).

Note that you can only use the OCI VCN-Native Pod Networking CNI plugin with clusters running Kubernetes 1.22 or later. In releases prior to July 2022, the clusters you created with Kubernetes Engine always used the flannel CNI plugin for pod networking. In releases after July 2022, the OCI VCN-Native Pod Networking CNI plugin is the default if you use the Console to create clusters (running Kubernetes 1.22 or later). However, when using the 'Custom Create' workflow, you can also choose to create clusters that use the flannel CNI plugin. The flannel CNI plugin continues to be the default if you use the API, although you can choose to use the OCI VCN-Native Pod Networking CNI plugin.

For very large environments, especially clusters running more than 5,000 nodes, we recommend the Cilium CNI plugin as the preferred networking layer. Its eBPF-based dataplane is designed for high-scale Kubernetes networking, reducing reliance on traditional iptables-based packet handling and enabling more efficient service routing, policy enforcement, and traffic visibility. For more information, see[Use Cilium to Provide Networking Services in Oracle Cloud Infrastructure Container Engine for Kubernetes](https://docs.oracle.com/en/learn/oke-flannel-to-cilium-cni-plugin/index.html)
