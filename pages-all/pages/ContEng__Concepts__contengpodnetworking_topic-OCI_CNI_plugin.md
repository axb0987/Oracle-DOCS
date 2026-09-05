# Using the OCI VCN-Native Pod Networking CNI plugin for pod networking
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm
- Fetched: 2026-09-05 01:53 CDT

# Using the OCI VCN-Native Pod Networking CNI plugin for pod networking

Find out about the OCI VCN-Native Pod Networking CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine (OKE).

The OCI VCN-Native Pod Networking CNI plugin provides IP addresses to pods from a VCN's CIDR block. The OCI VCN-Native Pod Networking CNI plugin enables other resources within the same subnet (or a different subnet) to communicate directly with pods in a Kubernetes cluster. Pod IP addresses are directly routable from other VCNs connected (peered) to that VCN, and from on-premise networks.

Since pods are directly routable, you can use 'native' VCN functionality to:
- Control access to and from pods using security rules defined as part of network security groups (recommended) or security lists. The security rules apply to all pods in all the worker nodes connected to the pod subnet specified for a node pool. See[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)and[Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm).
- Observe the traffic to, from, and between pods using VCN flow logs for troubleshooting and compliance auditing purposes. See[VCN Flow Logs](https://docs.oracle.com/iaas/Content/Network/Concepts/vcn-flow-logs.htm).
- Route incoming requests to pods based on routing policies specified by routing rules and route tables. See[VCN Route Tables](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).

When using the OCI VCN-Native Pod Networking CNI plugin, worker nodes are connected to two subnets specified for the node pool:
- Worker Node Subnet: The worker node subnet supports communication between processes running on the cluster control plane (such as kube-apiserver, kube-controller-manager, kube-scheduler) and processes running on the worker node (such as kubelet, kube-proxy). The worker node subnet can be private or public, and can be a regional subnet (recommended) or on different AD-specific subnets (one in each availability domain in the region).
- Pod Subnet: The pod subnet supports communication between pods and direct access to individual pods using private pod IP addresses. The pod subnet must be private, and must be a regional subnet. The pod subnet enables pods to communicate with other pods on the same worker node, with pods on other worker nodes, with OCI services (through a service gateway) and with the internet (through a NAT gateway). You specify a single pod subnet for all the pods running on worker nodes in a node pool. You can specify the same pod subnet, or different pod subnets, for different node pools in a cluster. You can specify the same pod subnet for node pools in different clusters.

The worker node subnet and the pod subnet must be in the same VCN. In some situations, the worker node subnet and the pod subnet can be the same subnet (see[Maximum Number of VNICs and Pods Supported by Different Shapes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_vnics_pods_shapes)). If the worker node subnet and the pod subnet are the same subnet, Oracle recommends defining security rules in network security groups (rather than in security lists) to route network traffic to worker nodes and pods. The worker node subnet and the pod subnet are in addition to the Kubernetes API endpoint subnet and any load balancer subnets defined for the cluster.

When using the OCI VCN-Native Pod Networking CNI plugin, worker nodes use a primary VNIC for node traffic and one or more secondary VNIC profiles for pod networking. You can attach multiple secondary VNIC profiles and configure subnet, NSGs, and pod IP allocation settings for each profile by setting`ipCount`. The combined`ipCount`across all configured secondary VNIC profiles on a node can be up to 256. If you need more than 32 IPs per VNIC, configure pod subnets with two CIDR blocks as a capacity-planning recommendation.

If the shape you select for the node pool supports multiple VNIC attachments, you can attach multiple secondary VNIC profiles for pod networking. For each secondary VNIC profile, specify the subnet and the number of pod IPs to allocate using`ipCount`. Optionally, define`applicationResources`on secondary VNIC profiles when workloads must be pinned to a single selected profile.

You can specify the maximum number of pods that you want to run on a single worker node in a node pool, up to a limit of 256. The limit of 256 is the maximum number of IP addresses that can be assigned to a worker node. Select a shape that supports sufficient VNIC attachments and ensure the pod IP capacity is sized appropriately using the`ipCount`values configured for the secondary VNIC profiles. If you define Application Resources on secondary VNIC profiles, a pod can request a single Application Resource to pin to one selected profile and must include the required toleration for the node taint. If you deploy multi-interface pods, attach additional interfaces using Multus and NADs, and do not combine Multus network annotations with pod-level Application Resource requests in the same pod spec. For more information, see[Maximum Number of VNICs and Pods Supported by Different Shapes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_vnics_pods_shapes)and[Attaching Multiple Secondary VNICs for Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengAttaching_Multiple_VNICs.htm).

Note that node pools that expose Application Resources are tainted to prevent pods without explicit Application Resource requests from scheduling on those nodes. Pods that request an Application Resource must include a matching toleration.

If you want to conserve the pod subnet's address space, lower the maximum number of pods you want to run on a single worker node, and thereby reduce the number of IP addresses that are pre-allocated in the pod subnet.

Note the following when using the OCI VCN-Native Pod Networking CNI plugin:
- You can use the OCI VCN-Native Pod Networking CNI plugin with both virtual node pools and managed node pools.
- You can use the OCI VCN-Native Pod Networking CNI plugin with self-managed nodes, provided the cluster's control plane nodes are running Kubernetes version 1.27.10 (or later). For more information, see[Working with Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengworkingwithselfmanagednodes.htm).
- You can only use the OCI VCN-Native Pod Networking CNI plugin with clusters running Kubernetes 1.22 or later (see[Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm)). For more information, see[Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking.htm).
- If you are using the OCI VCN-Native Pod Networking CNI plugin and you want to specify an OKE image as the base image for worker nodes, do not select an OKE image released before June 2022.
- If you are using the OCI VCN-Native Pod Networking CNI plugin and you want to route traffic from an on-premise network to a pod, note that the pod's IP address is not persistent if the pod is recreated. For example, an Nginx pod might initially have 10.0.0.5 as its IP address, but if the pod is deleted and recreated, the pod might have a different IP address (such as 10.0.0.8).
- Service mesh products (such as Istio) are supported regardless of the CNI plugin you are using for pod networking (either the OCI VCN-Native Pod Networking CNI plugin or the flannel CNI plugin). Worker nodes must be running Kubernetes 1.26 (or later).
- Zero Trust Packet Routing (ZPR) security attributes are supported for managed node pools and self-managed nodes in clusters that use the OCI VCN-Native Pod Networking CNI plugin. ZPR security attributes are not supported for virtual node pools or for clusters that use the flannel CNI plugin for pod networking. For more information, see[Adding Security Attributes to Cluster-Related Resources and Applying ZPR Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengusingzpr.htm).

## Security Rules for Worker Nodes and Pods

When using the OCI VCN-Native Pod Networking CNI plugin for pod networking, certain security rules are required for the pod subnet and the worker node subnet. See[Security Rules for Pod Subnets](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig__section_rules_for_pod_subnets).

## How pod scheduling works with multiple secondary VNIC profiles

If a pod requests an Application Resource, an admission webhook validates the request and the scheduler selects a node that exposes the matching Extended Resource with available capacity. The CNI allocates a pod IP from the selected secondary VNIC profile, and the pod uses that selected profile as its primary network path. Each pod can request only one Application Resource in this pod-level scheduling model.

For multi-interface pods, attach additional interfaces using Multus and NADs. Define interface selection in the NAD configuration (for example, using a`deviceSelector`), and do not combine Multus network annotations with pod-level Application Resource requests in the same pod spec. Note that multi-interface pod networking using Multus requires the OCI VCN-Native Pod Networking CNI plugin version 3.2.0 or later.

## Maximum Number of VNICs and Pods Supported by Different Shapes

The maximum number of VNICs (and therefore the maximum number of pods) for worker nodes in a node pool depends on the shape you select for the node pool.

To find out the maximum number of VNICs for a particular shape, see[Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm).

To calculate the maximum number of pods in a node pool of a particular shape, use the following equation:
```

```

Note that when secondary VNIC profiles are configured for pod networking, pod capacity depends on the configured number of IP addresses (ipCount) across the secondary VNIC profiles, the effective kubelet max-pods value, and compute shape VNIC limits. If you use Application Resources, capacity for a pod that requests an Application Resource depends on the selected secondary VNIC profile. For multi-interface pods, capacity planning must also consider the number of additional interfaces attached using Multus and NADs.

## Additional IAM policy to access resources with IPv6 addresses

To use the OCI VCN-Native Pod Networking CNI plugin where a cluster's related resources (such as Kubernetes API endpoint, load balancer, and worker nodes) have IPv6 addresses, include a policy statement similar to the following in an IAM policy:

```

```

## Additional IAM Policy when a Cluster and its Related Resources are in Different Compartments

To use the OCI VCN-Native Pod Networking CNI plugin in the uncommon scenario where a cluster's related resources (such as node pools, VCN, and VCN resources) are in a different compartment to the cluster itself, you must include policy statements similar to the following in an IAM policy:
```

```

```

```

```

```

If you consider these policy statements to be too permissive, you can restrict the permissions to explicitly specify the compartment to which the related resources belong, and/or to explicitly specify the cluster that has related resources in a different compartment. For example:
```

```

```

```

```

```

where:
- `<compartment-ocid-of-nodepool>`is the OCID of the compartment to which nodepools and compute instances belong.
- `<compartment-ocid-of-network-resources>`is the OCID of the compartment to which the VCN and subnets belong.

## Updating the OCI VCN-Native Pod Networking CNI plugin

When you specify VCN-native pod networking as a cluster's network type, the cluster and its node pools initially run the latest version of the OCI VCN-Native Pod Networking CNI plugin.

Updates to the OCI VCN-Native Pod Networking CNI plugin are released periodically.

In OCI VCN-Native Pod Networking CNI plugin versions prior to version 2.3.0 (August 2025), you can specify that you want Oracle to deploy the updates on the cluster automatically. Alternatively, you can specify that you want to choose the version to deploy. If you decide to choose a version (and the version is prior to version 2.3.0), you are taking responsibility for keeping the add-on up-to-date. The OCI VCN-Native Pod Networking CNI plugin uses the`RollingUpdate`update strategy, so existing CNI plugin pods are terminated automatically, and new pods are created running the new CNI plugin version (for more information about the`RollingUpdate`update strategy, see[DaemonSet Update Strategy](https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/#daemonset-update-strategy)in the Kubernetes documentation). The updates are applied when the worker nodes are next rebooted.

In OCI VCN-Native Pod Networking CNI plugin version 2.3.0 (August 2025) and later versions, CNI plugin updates are never deployed on the cluster automatically. The OCI VCN-Native Pod Networking CNI plugin uses the`OnDelete`update strategy, so the CNI plugin can only be updated by explicitly deleting the CNI plugin pods (for more information about the`OnDelete`update strategy, see[DaemonSet Update Strategy](https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/#daemonset-update-strategy)in the Kubernetes documentation). This approach avoids unexpected restarts of CNI plugin pods during cluster updates. Version 2.3.0 also introduces a validating admission policy that restricts the deletion of CNI plugin pods. To update the CNI plugin to a newer version when using version 2.3.0 or later, adopt one of the following techniques:
- (recommended) Provision new nodes in the cluster: When you provision new nodes in the cluster, they automatically receive CNI plugin pods running the latest CNI plugin version. You can optionally drain and remove nodes with CNI plugin pods that are running older versions.
- Update existing nodes in the cluster: You can update the CNI plugin version on existing nodes by deleting the existing CNI plugin pods. You have to remove the validating admission policy that restricts CNI plugin pod deletion, delete the existing CNI plugin pods, and then restore the policy. The DaemonsetController recreates the CNI plugin pods, running the latest CNI plugin version. Follow these steps:
- Identify the CNI plugin pods of the existing nodes to update, by entering:
```

```

- Delete the validating admission policy to enable you to delete the CNI plugin pods as follows:
- 

Save the validating admission policy and the validating admission policy binding as`vap-policy.yaml`and`vap-binding.yaml`so that you can restore them later, by entering the following commands:
```

```

```

```

- Delete the validating admission policy and the validating admission policy binding, by entering the following commands:
```

```

```

```

- Delete the CNI plugin pods that you identified previously, by entering the following command for each pod:
```

```

- Restore the validating admission policy and policy binding that you previously deleted, using the`vap-policy.yaml`and`vap-binding.yaml`files you created earlier, by entering the following commands::
```

```

```

```

To determine whether updates have been deployed and are waiting to be applied, inspect the`vcn-native-ip-cni`Daemonset logs by entering:
```

```

Interpret the response to the command as follows:
- If there is output in response to the command, updates to the OCI VCN-Native Pod Networking CNI plugin have been deployed to the worker nodes associated with the pods shown in the response, but the updates are waiting to be applied. In CNI plugin versions prior to version 2.3.0, the updates will be applied when the worker nodes are next rebooted. In CNI plugin version version 2.3.0 and later, the updates will be applied when the CNI plugin pods are deleted and recreated (when new nodes are provisioned; or when you have manually removed the validating admission policy, explicitly deleted the CNI plugin pods).
-
