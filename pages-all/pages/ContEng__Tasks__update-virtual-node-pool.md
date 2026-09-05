# Updating a Virtual Node Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-virtual-node-pool.htm
- Fetched: 2026-09-05 01:58 CDT

# Updating a Virtual Node Pool

Find out how to update a virtual node pool using Kubernetes Engine (OKE).

For general information about updating node pools, see[Modifying Node Pool and Worker Node Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingnodepool.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-virtual-node-pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-virtual-node-pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-virtual-node-pool.htm#)
- 

- On the Clusters list page, select the name of the cluster that you want to modify. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab, and then select the name of the virtual node pool that you want to modify.

On the Virtual node pool details tab, information about the virtual node pool is displayed, including the following details:
- The status of the node pool.
- The node pool's OCID.
- The type of the worker nodes in the node pool (virtual).
- The configuration currently used when starting new virtual nodes in the node pool, including the following details:
- The version of Kubernetes to run on worker nodes.
- The shape to use for worker nodes.
- The availability domains, fault domains, and different regional subnets (recommended) or AD-specific subnets hosting worker nodes.
- 

Change virtual node pool and virtual node properties as follows:

- From the Actions menu, select Edit and specify:
- Name: A different name for the node pool. Avoid entering confidential information.
- Node count: A different number of virtual nodes to create in the virtual node pool, placed in the availability domains you select, and in the regional subnet (recommended) or AD-specific subnet you specify for each availability domain. See[Scaling Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengscalingnodepools.htm).
- Node placement configuration:
- Availability domain: An availability domain in which to place virtual nodes.
- Fault domains: (Optional) One or more fault domains in the availability domain in which to place virtual nodes.

When the virtual nodes are created, they are distributed as evenly as possible across the availability domains and fault domains you select. Consider the following recommendations:
- Set Node count to a minimum of three. In regions with multiple availability domains, distribute nodes across the availability domains. In regions with a single availability domain, distribute nodes across the fault domains.
- Do not specify fault domains (in other words, leave Fault domains empty) to allow virtual nodes to create pods in any fault domain that has available compute capacity. This approach is recommended if you do not require fine-grained control over placement and want to avoid potential capacity constraints.
- To support high availability, specify three rows for node placement configuration. In regions with multiple availability domains, have one row per availability domain. In regions with a single availability domain, have one row per fault domain.
- Virtual node communication:
- Subnet compartment: The compartment in which the virtual node subnet resides.
- Subnet: A different regional subnet (recommended) or AD-specific subnet configured to host virtual nodes. If you specified load balancer subnets, the virtual node subnets must be different. The subnets you specify can be private (recommended) or public, and can be regional (recommended) or AD-specific. We recommend that the pod subnet and the virtual node subnet are the same subnet (in which case, the virtual node subnet must be private). For more information, see[Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#subnetconfig).
- Use security rules in Network Security Group (NSG): Control access to the virtual node subnet using security rules defined for one or more network security groups (NSGs) that you specify (up to a maximum of five). You can use security rules defined for NSGs instead of, or as well as, those defined for security lists (NSGs are recommended). For more information about the security rules to specify for the NSG, see[Security Rules for Worker Nodes and Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_pods_security_rules).
- Pod communication:
- Subnet compartment: The compartment in which the pod subnet resides.
- Subnet: A different regional subnet configured to host pods. The pod subnet you specify for virtual nodes must be private. We recommend that the pod subnet and the virtual node subnet are the same subnet (in which case, Oracle recommends defining security rules in network security groups rather than in security lists). For more information, see[Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#subnetconfig).
- Use security rules in Network Security Group (NSG): Control access to the pod subnet using security rules defined for one or more network security groups (NSGs) that you specify (up to a maximum of five). You can use security rules defined for NSGs instead of, or as well as, those defined for security lists (NSGs are recommended). For more information about the security rules to specify for the NSG, see[Security Rules for Worker Nodes and Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_pods_security_rules).

For more information about pod communication, see[Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking.htm).
- Kubernetes labels: (Optional) One or more labels (in addition to a default label) to add to virtual nodes in the virtual node pool to enable the targeting of workloads at specific node pools. For more information, see[Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)in the Kubernetes documentation.
- Kubernetes taints: (Optional) One or more taints to add to virtual nodes in the virtual node pool. Taints enable virtual nodes to repel pods, and so ensure that pods don't run on virtual nodes in a particular virtual node pool. You can apply taints only to virtual nodes. For more information, see[Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)in the Kubernetes documentation.
- Select Update to save the updated properties.
- Use the Kubernetes labels and taints tab to see labels and taints applied to virtual nodes.
- Use the Virtual Nodes tab to see information about specific worker nodes in the virtual node pool.
- Use the Work requests tab to perform the following tasks:
- Get the details of a particular work request for the virtual node pool resource.
- List the work requests for the virtual node pool resource.

For more information, see[Viewing Work Requests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm).
- Use the Tags tab to add or modify the tags applied to the virtual node pool. Tagging enables you to group disparate resources across compartments, and enables you to annotate resources with your own metadata. For more information, see[Tagging Kubernetes Cluster-Related Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources.htm).
- 

Use the[oci ce virtual-node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/update.html)command and required parameters to update a virtual node pool:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateVirtualNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/UpdateVirtualNodePool)
