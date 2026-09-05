# Example: Installing Calico and Setting Up Network Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupcalico.htm
- Fetched: 2026-09-05 01:56 CDT

# Example: Installing Calico and Setting Up Network Policies

Find out how to install Calico and set up network policies on a cluster you've created using Kubernetes Engine (OKE).

The Kubernetes networking model assumes containers (pods) have unique and routable IP addresses within a cluster. In the Kubernetes networking model, containers communicate with each other using those IP addresses, regardless of whether the containers are deployed on the same node in a cluster or on a different node. Kubernetes has adopted the Container Network Interface (CNI) specification for network resource management. The CNI consists of a specification and libraries for writing plugins to configure network interfaces in Linux containers, along with a number of supported plugins.

By default, pods accept traffic from any source. To enhance cluster security, pods can be 'isolated' by selecting them in a network policy (the Kubernetes NetworkPolicy resource). A network policy is a specification of how groups of pods are allowed to communicate with each other and other network endpoints. NetworkPolicy resources use labels to select pods and to define rules that specify what traffic is allowed to the selected pods. If a NetworkPolicy in a cluster namespace selects a particular pod, that pod will reject any connections that are not allowed by any NetworkPolicy. Other pods in the namespace that are not selected by a NetworkPolicy will continue to accept all traffic. For more information about network policies, see[the Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/).

Network policies are implemented by the CNI network provider. Simply creating the NetworkPolicy resource without a CNI network provider to implement it will have no effect. Note that not all CNI network providers implement the NetworkPolicy resource.

When you create clusters with Kubernetes Engine, you select a Network type . The Network type you select determines the CNI network provider and associated CNI plugin that is used for pod networking, as follows:
- VCN-native pod networking: Uses the OCI VCN-Native Pod Networking CNI plugin to connect worker nodes to pod subnets in an Oracle Cloud Infrastructure VCN. As a result, pod IP addresses within a VCN are directly routable from other VCNs connected (peered) to that VCN, and from on-premise networks. See[Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm).
- Flannel overlay: Uses the flannel CNI plugin to encapsulate communication between pods in the flannel overlay network, a simple private overlay virtual network that attaches IP addresses to containers. The pods in the private overlay network are only accessible from other pods in the same cluster. See[Using the flannel CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-flannel_CNI_plugin.htm).

Both the OCI VCN-Native Pod Networking CNI plugin and the flannel CNI plugin support standard pod networking in Kubernetes. However, enforcing Kubernetes network policies requires an additional solution. Kubernetes Engine supports network policy enforcement through integration with the Calico network policy engine when using the OCI VCN-Native Pod Networking CNI plugin. Note that Kubernetes Engine does not support the use of the Calico network policy engine with the flannel CNI plugin. If you want a cluster to support network policies and you selected Flannel overlay as the Network type when you created the cluster, you must replace flannel with Calico as the overlay CNI (see[Installing Calico in place of the flannel CNI plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupcalico.htm#contengsettingupcalico_topic_Installing_Calico_instead_of_flannel)).

Kubernetes network policies and Zero Trust Packet Routing (ZPR) are complementary. ZPR is not an implementation of the Kubernetes NetworkPolicy resource. Use Kubernetes network policies, enforced by a network policy engine such as Calico, to control traffic between pods in a cluster. Use ZPR to enforce network access policies in the OCI network fabric, based on ZPR security attributes assigned to supported OCI resources used by Kubernetes Engine.

You can use Kubernetes network policies and ZPR together, along with network security groups and security lists. For example, you can use Calico to enforce Kubernetes network policies for pod-to-pod traffic in a cluster, and use ZPR to enforce layer 4 access control for traffic between cluster-related resources and other OCI resources. For more information about Kubernetes Engine and ZPR, see[Adding Security Attributes to Cluster-Related Resources and Applying ZPR Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm).

Calico is an open source networking and network security solution for containers, virtual machines, and native host-based workloads. For more information about Calico, see the[Calico documentation](https://projectcalico.docs.tigera.io/about/about-calico).
Note  
  

- You can use Calico with managed node pools, but not with virtual node pools.
- 

If you have created a cluster and selected flannel overlay as the Network type , you can install Calico in place of the flannel CNI plugin (see[Installing Calico in place of the flannel CNI plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupcalico.htm#contengsettingupcalico_topic_Installing_Calico_instead_of_flannel)). However, note that changing the CNI plugin from flannel to Calico only applies to new nodes that are subsequently created in the cluster. Therefore, we recommend that you do not replace flannel with Calico on clusters that already have existing worker nodes.
- Installing the Calico network policy engine alongside the flannel CNI plugin causes network issues. For this reason, Kubernetes Engine does not support the installation of Calico alongside the flannel CNI plugin.

## Calico Compatibility

The table lists the versions of the Calico network plugin that Oracle has successfully tested on clusters created using Kubernetes Engine. Oracle only supports Calico versions that have been successfully tested. For each Calico version, the table shows the Kubernetes version that was running on clusters in successful tests.

For more information, see[Example: Installing Calico and Setting Up Network Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengsettingupcalico.htm).

Calico Version Tested (and supported) on clusters running Kubernetes 1.34? Tested (and supported) on clusters running Kubernetes 1.35? Tested (and supported) on clusters running Kubernetes 1.36?
`3.25.1`(not tested) (not tested) (not tested)
`3.26.1`(not tested) (not tested) (not tested)
`3.26.4`(not tested) (not tested) (not tested)
`3.27.2`(not tested) (not tested) (not tested)
`3.28.0`(not tested) (not tested) (not tested)
`3.28.2`(not tested) (not tested) (not tested)
`3.29.2`(not tested) (not tested) (not tested)
`3.30.0`(not tested) (not tested) (not tested)
`3.30.3`Yes (not tested) (not tested)
`3.31.5`(not tested) Yes (not tested)
`3.32.0`(not tested) (not tested) Yes

## Installing Calico in place of the flannel CNI plugin

Having created an enhanced cluster using Kubernetes Engine (using either the Console or the API) and selected flannel overlay as the Network type , you can subsequently install Calico on the cluster to support network policies.

Before you install Calico in place of the flannel CNI plugin, you must first disable the flannel CNI plugin. Note that changing the CNI plugin from flannel to Calico only applies to new nodes that are subsequently created in the cluster. Therefore, we recommend that you do not replace flannel with Calico on clusters that already have existing worker nodes.

For convenience, Calico installation instructions are included below. Note that Calico installation instructions vary between Calico versions. For information about installing different versions of Calico, always refer to the[Calico installation documentation](https://docs.tigera.io/calico/latest/getting-started/kubernetes/).
- 

Disable the flannel CNI plugin cluster add-on. See[Disabling (and Removing) a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm).
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- Remove the flannel daemonset from the kube-system namespace by entering:

```

```

- 

In a terminal window, download the Calico manifest for the Kubernetes API datastore by entering:

```

```

Note that the url differs, according to the version of Calico that you want to install.
- If you have selected an Oracle Linux 8 image for worker nodes in the cluster, set an additional environment variable in the`calico.yaml`file as follows:
- Open the`calico.yaml`file in a text editor of your choice.
- 

Add the following environment variable to the`env`section for the`calico-node`container in the manifest of the`calico-node`DaemonSet manifest:
```

```

- Save and close the modified`calico.yaml`file.
- 

Install and configure Calico by entering the following command:

```

```

## Installing Calico alongside the OCI VCN-Native Pod Networking CNI plugin

Having created a cluster using Kubernetes Engine (using either the Console or the API) and selected VCN-native pod networking as the Network type , you can subsequently install Calico on the cluster alongside the OCI VCN-Native Pod Networking CNI plugin to support network policies.

For convenience, Calico installation instructions are included below. Note that Calico installation instructions vary between Calico versions. For information about installing different versions of Calico, always refer to the[Calico installation documentation](https://docs.tigera.io/calico/latest/getting-started/kubernetes/).
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- 

In a terminal window, download the Calico policy-only manifest for the Kubernetes API datastore by entering:

```

```

Note that the url differs, according to the version of Calico that you want to install.
- The`calico-policy-only.yaml`file includes Calico components that are not required when using Calico alongside the OCI VCN-Native Pod Networking CNI plugin, so you have to remove these components. You also have to set some additional environment variables.
- Open the`calico-policy-only.yaml`file in a text editor of your choice.
- Remove the`initContainers`section from the manifest of the`calico-node`DaemonSet.
- Remove the following from the`env`section for the`calico-node`container from the manifest of the`calico-node`DaemonSet:
```

```

- Remove the following`envFrom`section for the`calico-node`container from the manifest of the`calico-node`DaemonSet:
```

```

- Remove the following volumes from the`volumes`section of the manifest of the`calico-node`DaemonSet:
- `cni-bin-dir`
- `cni-net-dir`
- `cni-log-dir`

Before you make the change, the`volumes`section of the`calico-node`DaemonSet manifest looks like this:
```

```

After you have made the change, check that the`volumes`section of the`calico-node`DaemonSet manifest looks like this:
```

```

- Remove the following volume mounts from the`volumeMounts`section for the`calico-node`container in the manifest of the`calico-node`DaemonSet:
- `cni-net-dir`, including the associated comment`# For maintaining CNI plugin API credentials.`
- `cni-log-dir`

Before you make the change, the`volumeMounts`section looks like this:
```

```

After you have made the change, check that the`volumeMounts`section looks like this:
```

```

- Add the following environment variables for the`calico-node`container in the manifest of the`calico-node`DaemonSet:
- `FELIX_INTERFACEPREFIX="oci"`
- `NO_DEFAULT_POOLS="true"`
- `FELIX_CHAININSERTMODE="Append"`
- `FELIX_IPTABLESMANGLEALLOWACTION="Return"`
- `FELIX_IPTABLESBACKEND="NFT"`Note: Only add this environment variable if you have selected an Oracle Linux 8 image for worker nodes in the cluster.

Before you make the change, the`calico-node`container environment variables (`env:`) section of the`calico-node`DaemonSet manifest looks like this:
```

```

After you have made the change, check that the`calico-node`container environment variables (`env:`) section of the`calico-node`DaemonSet manifest looks like this:
```

```

- Save and close the modified`calico-policy-only.yaml`file.
- 

Install and configure Calico by entering the following command:

```

```

## Setting up Network Policies

Having installed Calico on a cluster you've created with Kubernetes Engine, you can create Kubernetes NetworkPolicy resources to isolate pods as required.

For NetworkPolicy examples and how to use them, see the Calico documentation and specifically:
- [Kubernetes policy, demo](https://projectcalico.docs.tigera.io/security/tutorials/kubernetes-policy-demo/kubernetes-demo)
- [Kubernetes policy, basic tutorial](https://projectcalico.docs.tigera.io/security/tutorials/kubernetes-policy-basic)
- [Kubernetes policy, advanced tutorial](https://docs.tigera.io/calico/latest/network-policy/get-started/kubernetes-policy/kubernetes-policy-advanced)
