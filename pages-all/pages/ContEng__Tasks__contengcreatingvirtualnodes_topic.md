# Creating Virtual Nodes and Virtual Node Pools in a New Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingvirtualnodes_topic.htm
- Fetched: 2026-09-05 01:55 CDT

# Creating Virtual Nodes and Virtual Node Pools in a New Cluster

Find out how to create virtual nodes and virtual node pools in a new cluster using Kubernetes Engine (OKE).

You can create virtual nodes by creating a virtual node pool in a new cluster. You can only create virtual nodes and virtual node pools in enhanced clusters.

See also[Creating a Virtual Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-virtual-node-pool.htm).

You can create virtual nodes and virtual node pools using the Console, the CLI, and the API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingvirtualnodes_topic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingvirtualnodes_topic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingvirtualnodes_topic.htm#)
- 

To create a cluster with a virtual node pool and virtual nodes using the Console:
- Follow the instructions in[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm)to create a new cluster.
- On the Network setup page, specify VCN-native pod networking as the network type for the cluster.
- On the Node pools page, specify a Name and Compartment for the virtual node pool you want to create.
- Specify the Node type: of worker nodes in this node pool as Virtual .
- Define the virtual node pool:

- Specify configuration details for the virtual node pool:
- Node placement configuration:
- Availability domain: An availability domain in which to place virtual nodes.
- Fault domains: (Optional) One or more fault domains in the availability domain in which to place virtual nodes.

When the virtual nodes are created, they are distributed as evenly as possible across the availability domains and fault domains you select. Consider the following recommendations:
- Set Node count to a minimum of three. In regions with multiple availability domains, distribute nodes across the availability domains. In regions with a single availability domain, distribute nodes across the fault domains.
- Do not specify fault domains (in other words, leave Fault domains empty) to allow virtual nodes to create pods in any fault domain that has available compute capacity. This approach is recommended if you do not require fine-grained control over placement and want to avoid potential capacity constraints.
- To support high availability, specify three rows for node placement configuration. In regions with multiple availability domains, have one row per availability domain. In regions with a single availability domain, have one row per fault domain.
- Node count: The number of virtual nodes to create in the virtual node pool, placed in the availability domains you select, and in the regional subnet (recommended) or AD-specific subnet you specify for each availability domain.
- 

Pod shape: The shape to use for pods running on virtual nodes in the virtual node pool. The shape determines the processor type on which to run the pod.

Only those shapes available in your tenancy that are supported by Kubernetes Engine are shown. See[Supported Images (Including Custom Images) and Shapes for Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengimagesshapes.htm).

Note that you explicitly specify the CPU and memory resource requirements for virtual nodes in the pod spec (see[Assign Memory Resources to Containers and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/)and[Assign CPU Resources to Containers and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/)in the Kubernetes documentation).
- Virtual node communication:
- Subnet compartment: The compartment in which the virtual node subnet resides.
- Subnet: A regional subnet (recommended) or AD-specific subnet configured to host virtual nodes. If you specified load balancer subnets, the virtual node subnets must be different. The subnets you specify can be private (recommended) or public, and can be regional (recommended) or AD-specific. We recommend that the pod subnet and the virtual node subnet are the same subnet (in which case, the virtual node subnet must be private). See[Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#subnetconfig).
- Use security rules in Network Security Group (NSG): Control access to the virtual node subnet using security rules defined for one or more network security groups (NSGs) that you specify (up to a maximum of five). You can use security rules defined for NSGs instead of, or as well as, those defined for security lists (NSGs are recommended). For more information about the security rules to specify for the NSG, see[Security Rules for Worker Nodes and Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_pods_security_rules).
- Pod communication: Pods running on virtual nodes use VCN-native pod networking. Specify how pods in the node pool communicate with each other using a pod subnet:
- Subnet compartment: The compartment in which the pod subnet resides.
- Subnet: A regional subnet configured to host pods. The pod subnet you specify for virtual nodes must be private. We recommend that the pod subnet and the virtual node subnet are the same subnet (in which case, Oracle recommends defining security rules in network security groups rather than in security lists). See[Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#subnetconfig).
- Use security rules in Network Security Group (NSG): Control access to the pod subnet using security rules defined for one or more network security groups (NSGs) that you specify (up to a maximum of five). You can use security rules defined for NSGs instead of, or as well as, those defined for security lists (NSGs are recommended). For more information about the security rules to specify for the NSG, see[Security Rules for Worker Nodes and Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_pods_security_rules).

For more information about pod communication, see[Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking.htm).
- 

Either accept the defaults for advanced virtual node pool options, or select Advanced options and specify alternatives as follows:
- Node pool tags: (Optional) One or more tags to add to the virtual node pool. Tagging enables you to group disparate resources across compartments, and also enables you to annotate resources with your own metadata. See[Tagging Kubernetes Cluster-Related Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengtaggingclusterresources.htm).
- Kubernetes labels: (Optional) One or more labels (in addition to a default label) to add to virtual nodes in the virtual node pool to enable the targeting of workloads at specific node pools. For more information, see[Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)in the Kubernetes documentation.
- Kubernetes taints: (Optional) One or more taints to add to virtual nodes in the virtual node pool. Taints enable virtual nodes to repel pods, thereby ensuring that pods do not run on virtual nodes in a particular virtual node pool. Note that you can only apply taints to virtual nodes. For more information, see[Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)in the Kubernetes documentation.
- Select Next to review the details you entered for the new cluster.
- Select Create cluster to create the new cluster.
- 

Use the[oci ce cluster create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/create.html)and[oci ce virtual-node-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/create.html)commands (and required parameters) to create a new cluster with a virtual node pool and virtual nodes:

- Create a new cluster, specifying the OCI VCN-Native Pod Networking CNI plugin for pod networking:

```

```

For example:

```

```

- Obtain the OCID of the new cluster for use in the next step.
- Create a new virtual node pool in the cluster:

```

```

where:
- `<ad-name>`is the name of the availability domain in which to place virtual nodes. To find out the availability domain name to use, run:

```

```

- `<shape-name>`is one of`Pod.Standard.E3.Flex`,`Pod.Standard.E4.Flex`.

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateVirtualNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/CreateVirtualNodePool)
