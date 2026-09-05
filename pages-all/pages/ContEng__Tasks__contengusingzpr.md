# Adding Security Attributes to Cluster-Related Resources and Applying ZPR Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm
- Fetched: 2026-09-05 01:57 CDT

# Adding Security Attributes to Cluster-Related Resources and Applying ZPR Policies

Find out how to add ZPR security attributes to cluster-related resources and how to apply Zero Trust Packet Routing (ZPR) policies with Kubernetes Engine (OKE).

Using Zero Trust Packet Routing (ZPR) with Kubernetes Engine enables you to implement fine-grained, least-privilege access control over interactions between cluster-related resources and other OCI resources. ZPR is especially useful in environments where sensitive data or critical operations are distributed across multiple OCI resources, and strict separation and control of resource access is required. Using ZPR helps you to mitigate risks associated with unauthorized access and ensure that only explicitly permitted traffic flows between protected resources, supporting both compliance needs and organizational security policies.

You can use Zero Trust Packet Routing (ZPR) along with network security groups and security lists to manage network access to OCI resources . To do this, define ZPR policies that govern how resources communicate with each other, and then add ZPR security attributes to those resources. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).

The use of ZPR is optional. You can continue to use OKE without assigning ZPR security attributes. Existing network security controls, such as network security groups, security lists, and Kubernetes network policies, continue to work with OKE. ZPR adds another layer of network enforcement for resources that have security attributes and matching ZPR policies.
Caution  
  
If an endpoint has a Zero Trust Packet Routing (ZPR) security attribute, traffic to the endpoint must satisfy ZPR policies and also all network security group and security list rules. For example, if you are already using NSGs and you add a security attribute to an endpoint without also creating a ZPR policy that allows the required traffic, traffic to the endpoint is blocked. From then onward, a ZPR policy must explicitly allow traffic to the endpoint.

When migrating existing clusters to use ZPR, create and test the required ZPR policies before removing existing network security group or security list rules. By default, resources with ZPR security attributes cannot communicate with resources that do not have ZPR security attributes unless a ZPR policy explicitly allows that traffic.

To use ZPR with Kubernetes Engine, you add security attributes to supported cluster-related resources in a tenancy where ZPR is available. Having added a security attribute to a resource, the resource can only access other OCI resources if access is allowed by a ZPR policy.

Security attributes are defined in a security attribute namespace. To add a security attribute to a cluster-related resource, an IAM policy must grant the group to which you belong access to the namespace in which the security attribute is defined. For more information, see[Required IAM policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#contengusingzpr_topic_permissions).

To enable a cluster-related resource with ZPR security attributes to access another resource, a suitable ZPR policy must exist. If security attributes have also been added to the other resource, create a ZPR policy that allows access to endpoints with those security attributes. If the other resource does not have ZPR security attributes, or cannot have ZPR security attributes because the resource type is not supported by ZPR, create a ZPR policy that allows access by using a supported IP address, CIDR block, or service endpoint expression. Without a suitable ZPR policy, access is blocked at the network level and connection errors might occur. For more information, see[Required ZPR policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#contengusingzpr_topic_ziprpolicy).

Note the following points:
- To see the cluster-related resources to which security attributes have been added, use the ZPR Console page (see[Listing Protected Resources](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/list-protected-resources.htm)in the ZPR documentation).
- Having added security attributes to a cluster-related resource, you can use tools such as the Network Path Analyzer, where supported, to help debug any network connectivity issues.
- If a security attribute is deleted from the security attribute namespace (using the ZPR Console, CLI, or API) after it has been added to a cluster-related resource, remove the deleted security attribute from the resource. Otherwise, ZPR policies that reference the deleted security attribute might no longer allow the expected traffic.

The way in which you add or remove security attributes to or from supported cluster-related resources depends on the resource, as shown in the following table:

Resource Where to apply security attributes How to apply security attributes Result
Cluster's Kubernetes API endpoint Console, CLI, API Set the Endpoint security attribute property of the cluster (`securityAttributes`in the API) Security attributes apply only to the cluster's Kubernetes API endpoint. These attributes do not apply to worker nodes, pods, load balancers, or other cluster resources. See[Adding Security Attributes to a Cluster's Kubernetes API Endpoint](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#contengusingzpr_topic_adding-attributes-to-api-endpoint).
Primary VNICs of managed node compute instances Console, CLI, API Set the VNIC Security Attribute property of the node pool's primary VNIC (`securityAttributes`in the API) Security attributes apply to the primary VNICs of the compute instances that back managed nodes in the node pool. These attributes are used for node-level traffic, such as kubelet traffic, Oracle Cloud Agent traffic, and traffic from pods that use the host network. See[Adding Security Attributes to Primary VNICs of Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#contengusingzpr_topic_adding-attributes-to-nodepool-primary-vnic).
Secondary VNICs of managed node compute instances Console, CLI, API Set the VNIC Security Attribute property of the node pool's secondary VNIC(s) (`securityAttributes`in the API) Security attributes apply to the secondary VNICs of the compute instances that back managed nodes in the node pool. If you define multiple secondary VNICs for a managed node pool, all secondary VNICs in the node pool must use the same set of security attributes. See[Adding Security Attributes to Secondary VNICs of Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#contengusingzpr_topic_adding-attributes-to-nodepool-secondary-vnics).
Self-managed node pod traffic Compute instance creation Specify ZPR security attributes for the secondary VNICs when creating the compute instance. Do not specify ZPR security attributes for secondary VNICs in an instance configuration. Security attributes apply to the secondary VNICs used for pod traffic. See[Working with Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithselfmanagednodes.htm).
Kubernetes services of type`LoadBalancer`Annotation in service manifest Add the`oci.oraclecloud.com/security-attributes`annotation to the service manifest. Kubernetes Engine provisions load balancers and network load balancers with the security attributes. See[Adding Security Attributes to Load Balancers and Network Load Balancers Provisioned for Kubernetes Services of Type LoadBalancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#contengusingzpr_topic_adding-attributes-to-services-type-loadbalancer).
Native ingress controller load balancers Annotation in the`IngressClass`manifest Add the`oci-native-ingress.oraclecloud.com/security-attributes`annotation to the manifest. The OCI native ingress controller provisions load balancers with the specified security attributes. See[Adding Security Attributes to Load Balancers Provisioned by the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#contengusingzpr_topic_adding-attributes-to-native-ingress-controller-lbs).
File Storage mount target created by the CSI volume plugin Parameter in`StorageClass`manifest Add the`securityAttributes`parameter to the manifest. The CSI volume plugin creates the mount target with the specified security attributes. See[Adding Security Attributes to File Storage Service Mount Targets Created by the CSI Volume Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#contengusingzpr_topic_adding-attributes-to-fss-mount-targets).

Note that ZPR security attributes are not inherited by all resources in a cluster. You assign security attributes separately for each supported resource type. Cluster endpoint security attributes apply only to the Kubernetes API endpoint. Node pool security attributes apply to the node and pod VNICs for nodes in that node pool. Load balancers, native ingress load balancers, and File Storage mount targets require their own security attribute configuration.

## Prerequisites and Limitations

Before using Zero Trust Packet Routing (ZPR) with Kubernetes Engine, review the following prerequisites and limitations:
- ZPR security attributes are supported with managed node pools and self-managed nodes, but not with virtual node pools.
- ZPR security attributes are supported when creating clusters and when updating existing clusters, provided the cluster’s Kubernetes API endpoint is integrated into your own VCN (known as a "VCN-native cluster"). You cannot use ZPR security attributes with clusters whose Kubernetes API endpoints are not integrated into your own VCN. See[Migrating to VCN-Native Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm).
- The Kubernetes cluster must use the OCI VCN-Native Pod Networking CNI plugin for pod networking. ZPR security attributes are not supported with clusters that use the flannel CNI plugin. In addition, the version of the OCI VCN-Native Pod Networking CNI plugin must support ZPR security attributes. If the add-on version does not support ZPR security attributes, Kubernetes Engine prevents you from using ZPR or fails the node launch before the compute instance is created.
- The Kubernetes cluster must be running Kubernetes version 1.32 or later.
- Appropriate security attribute namespaces, containing the ZPR security attributes that you want to assign to OKE resources, must already exist. You create and manage security attribute namespaces and security attributes in the Zero Trust Packet Routing (ZPR) service. See[Creating a Security Attribute Namespace](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-security-attribute-namespace.htm)and[Creating a Security Attribute](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-security-attribute.htm).
- Appropriate ZPR policies that allow the required traffic must already exist. Assigning the same security attributes to two resources does not automatically allow them to communicate. You must create ZPR policies that allow the required communication paths. You create and manage ZPR policies in the Zero Trust Packet Routing (ZPR) service (see[Creating a ZPR Policy](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-zpr-policy.htm)).
- Appropriate IAM permissions to use the required ZPR security attribute namespaces must exist. OCI IAM enforces access to security attributes for cluster-related resources such as Kubernetes API endpoints, node VNICs, and load balancers. For more information, see[Required IAM policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#contengusingzpr_topic_permissions).
- 

If you assign security attributes to load balancers, network load balancers, or pod VNICs, the required IAM policies must also allow the Kubernetes Engine components that provision those resources to attach the specified security attributes. For example, the Cloud Controller Manager and OCI native ingress controller require a suitable IAM policy to attach the requested security attributes to the resources that they create, such as:

```

```

For more information, see[Required IAM policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#contengusingzpr_topic_permissions).
- ZPR does not replace Kubernetes network policies, and does not enforce traffic between pods on the same worker node. To control pod-to-pod traffic within a cluster, including traffic between pods on the same worker node, use Kubernetes network policies.
- ZPR security attributes are supported when provisioning persistent volume claims with File Storage service file systems, but not with Block Volume service block volumes.

## Required IAM policies

### IAM policy required to add security attributes to cluster-related resources

Before you can add a security attribute to a cluster-related resource, an IAM policy must grant the group to which you belong permission to use the security attribute namespace containing the security attribute. For example, using the following syntax:
```

```

If you use the policy statement`Allow group <group-name> to use security-attribute-namespaces in tenancy`to give users access to security attribute namespaces, note that this policy statement gives the group permission to use all security attribute namespaces in the tenancy. If you consider this to be too permissive, then you can restrict the security attribute namespaces to which the group has access by including a where clause in the statement. For example:
```

```

Note that if you do include a where clause, you must also include a second statement in the policy to enable the group to inspect all security attribute namespaces in the tenancy (when using the Console). For example:
```

```

When security attributes have been added to a cluster-related resource, the resource can only access other OCI resources if access is allowed by a ZPR policy.

Note that if a suitable IAM policy to use the security attribute namespace does not exist, you cannot add the security attribute to a cluster-related resource. The security attribute is not shown in the Console, and attempts to add the security attribute using the OCI CLI or the API fail.

### IAM policies required to enable clusters and node pools to access security attribute namespaces

When you add security attributes to a cluster resource or a node pool resource, a suitable IAM policy must grant the cluster or the node pool access to the necessary security attribute namespaces. For example:

```

```

```

```

## Required ZPR policies

### ZPR policies required to enable cluster-related resources to access other resources

When you add a security attribute to a cluster-related resource, the resource can only access other resources if a ZPR policy grants access to those resources.

If a suitable ZPR policy does not already exist, you have to create one. For example, using the following syntax:

```

```

where:
- `<vcn-security-attribute>`is a security attribute (and value) that has been added to the VCN in which the resource's subnet resides. For example,`VCN-Network:myVCN`.
- `<application-security-attribute>`is the security attribute (and value) that you have added to the cluster-related resource. For example,`oke-cluster:myclusterA`
- `<destination-security-attribute>`is a security attribute (and value) that has been added to the resource that you want the cluster-related resource to access. For example,`DB-Server:App1`

For example:
```

```

For more information about ZPR policies, syntax, and examples, see[Zero Trust Packet Routing Policy](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/zpr-policy-overview.htm)in the ZPR documentation.

### ZPR policies required when security attributes are added to primary VNICs of managed nodes

When you specify ZPR security attributes for the primary VNICs of compute instances that back managed nodes in a managed node pool, the following additional ZPR policies are required to enable the managed nodes to join the cluster:

```

```

```

```

```

```

## Adding Security Attributes to a Cluster's Kubernetes API Endpoint

You can add ZPR security attributes to the Kubernetes API endpoint when you create a cluster, or by updating an existing cluster. Cluster endpoint security attributes apply only to the Kubernetes API endpoint. These security attributes do not apply to worker nodes, pods, load balancers, or other cluster-related resources.

Before adding security attributes to the Kubernetes API endpoint, make sure a ZPR policy allows authorized clients to access the endpoint. For example, create a ZPR policy that allows access from clients that use`kubectl`.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#)
- 

To add security attributes to a new cluster's Kubernetes API endpoint when creating the cluster using the Console, see[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm).

To add or remove security attributes to or from an existing cluster's Kubernetes API endpoint using the Console:
- On the Clusters list page, select the cluster with the Kubernetes API endpoint that you want to add or remove security attributes to or from. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).

The Security tab shows the security attributes that have already been added to the cluster's Kubernetes API endpoint (if any).
- 

To add a security attribute to the cluster's Kubernetes API Endpoint:
- On the Security tab, select Add , and in the Add security attributes dialog:
- Select the security attribute namespace that contains the security attribute.
- Select the security attribute.
- Enter the security attribute value.
- If you want to add multiple security attributes to the cluster's Kubernetes API endpoint, select Add and select additional security attributes (up to a maximum of five).
- Select Add security attributes .
- 

To remove a security attribute from the cluster's Kubernetes API endpoint:
- On the Security tab, select Delete from the Actions menu (three dots) beside the security attribute you want to delete.
- Confirm that you want to delete the security attribute.

The security attributes shown on the cluster's Security tab now apply to the cluster's Kubernetes API endpoint.
- 

Use the[oci ce cluster create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/create.html)command and required parameters to create a cluster:

```

```

Use the[oci ce cluster update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update.html)command and required parameters to update a cluster:

```

```

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use these API operations to add or remove security attributes to or from a cluster's Kubernetes API endpoint:
- [CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster)
- [UpdateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster)

## Adding Security Attributes to Primary VNICs of Managed Nodes

You can specify ZPR security attributes for the primary VNICs of the compute instances that back managed nodes in a managed node pool. You specify these security attributes when creating a managed node pool, or by updating an existing managed node pool. The primary VNIC security attributes apply to new compute instances that start in the node pool. These security attributes are used for node-level traffic, such as kubelet traffic, Oracle Cloud Agent traffic, and traffic from pods that use the host network. These security attributes do not apply to the secondary VNICs used for pod traffic, or to other cluster-related resources.

When you update the security attributes for a managed node pool, the changes apply only to new worker nodes. Existing worker nodes and their VNICs aren’t updated. To apply the updated security attributes to existing workloads, replace the worker nodes in the node pool (see[Terminating and Replacing Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-worker-node-top.htm)). Note that boot volume replacement doesn’t apply updated node pool security attributes. The worker nodes must be replaced.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#)
- 

To add security attributes to the primary VNICs of managed nodes when creating a new cluster using the Console, see[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm).

To add security attributes to the primary VNICs of managed nodes when creating a new managed node pool using the Console, see[Creating a Managed Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-node-pool.htm).

To add or remove security attributes for the primary VNICs of managed nodes in an existing managed node pool using the Console:
- On the Clusters list page, select the name of the cluster you want to modify. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab, and then select the name of the node pool that you want to modify.

The Security tab shows the security attributes that have been configured for the primary VNICs of managed nodes in the node pool, if any.
- 

To add a security attribute for the primary VNICs of managed nodes:
- On the Security tab, in the Primary VNIC security attributes section, select Add , and in the Add security attributes dialog:
- Select the security attribute namespace that contains the security attribute.
- Select the security attribute.
- Enter the security attribute value.
- If you want to add multiple security attributes to the node pool's primary VNIC, select Add and select additional security attributes (up to a maximum of five).
- Select Add security attributes .
- 

To remove a security attribute from the node pool's primary VNIC:
- On the Security tab, in the Primary VNIC security attributes section, select Delete from the Actions menu (three dots) beside the security attribute you want to delete.
- Confirm that you want to delete the security attribute.

The security attributes shown on the node pool's Security tab now apply to the primary VNICs of new worker nodes that start in the node pool.
- 

Use the[oci ce node-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/create.html)command and required parameters to add a managed node pool:

```

```

Use the[oci ce node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/update.html)command and required parameters to update a managed node pool:

```

```

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use these API operations to add or remove security attributes to or from a managed node pool's primary VNIC:
- [CreateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/CreateNodePool)
- [UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool)

## Adding Security Attributes to Secondary VNICs of Managed Nodes

You can specify ZPR security attributes for the secondary VNICs of the compute instances that back managed nodes in a managed node pool. You specify these security attributes when creating a managed node pool, or by updating an existing managed node pool. In clusters that use the OCI VCN-Native Pod Networking CNI plugin, secondary VNICs are used for pod traffic. These security attributes do not apply to the primary VNICs used for node-level traffic, or to other cluster-related resources.

Note that if you define multiple secondary VNICs for a managed node pool, you must specify the same security attributes for all of the secondary VNICs in the node pool.

We recommend that you plan workload placement before assigning security attributes to secondary VNICs. Kubernetes Engine applies pod security attributes at the node pool level, so workloads that require different security profiles should run in different node pools.

When you update the security attributes for a managed node pool, the changes apply only to new worker nodes. Existing worker nodes and their VNICs aren’t updated. To apply the updated security attributes to existing workloads, replace the worker nodes in the node pool (see[Terminating and Replacing Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-worker-node-top.htm)). Note that boot volume replacement doesn’t apply updated node pool security attributes. The worker nodes must be replaced.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm#)
- 

To add security attributes to the secondary VNICs of managed nodes when creating a new cluster using the Console, see[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm).

To add security attributes to the secondary VNICs of managed nodes when creating a new managed node pool using the Console, see[Creating a Managed Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-node-pool.htm).

To add or remove security attributes for the secondary VNICs of managed nodes in an existing managed node pool using the Console:
- On the Clusters list page, select the name of the cluster you want to modify. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab, and then select the name of the node pool that you want to modify.

The Security tab shows the security attributes that have been configured for the secondary VNICs of managed nodes in the node pool, if any.
- 

To add a security attribute for the secondary VNICs of managed nodes:
- On the Security tab, in the Secondary VNIC security attributes section, select Add , and in the Add security attributes dialog:
- Select the security attribute namespace that contains the security attribute.
- Select the security attribute.
- Enter the security attribute value.
- If you want to add multiple security attributes to the node pool's secondary VNIC, select Add and select additional security attributes (up to a maximum of five).
- Select Add security attributes .
- 

To remove a security attribute from the node pool's secondary VNIC:
- On the Security tab, in the Secondary VNIC security attributes section, select Delete from the Actions menu (three dots) beside the security attribute you want to delete.
- Confirm that you want to delete the security attribute.

The security attributes shown on the node pool's Security tab now apply to the secondary VNICs of new worker nodes that start in the node pool.
- 

Use the[oci ce node-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/create.html)command and required parameters to add a managed node pool:

```

```

Use the[oci ce node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/update.html)command and required parameters to update a managed node pool:

```

```

For a complete list of flags and variable options for OCI CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use these API operations to add or remove security attributes to or from a managed node pool's secondary VNIC(s):
- [CreateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/CreateNodePool)
- [UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool)

## Adding Security Attributes to Load Balancers and Network Load Balancers Provisioned for Kubernetes Services of Type LoadBalancer

You can use the`oci.oraclecloud.com/security-attributes`annotation to specify the ZPR security attributes that Kubernetes Engine adds to the load balancers and network load balancers it provisions for services of type`LoadBalancer`. For more information, see[Specifying ZPR Security Attributes for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#lb-securityattributes).

## Adding Security Attributes to Load Balancers Provisioned by the OCI Native Ingress Controller

You can use the`oci-native-ingress.oraclecloud.com/security-attributes`annotation in the`IngressClass`manifest to specify the ZPR security attributes that the OCI native ingress controller adds to the load balancers it provisions. For more information, see[Specifying ZPR Security Attributes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_addingzprsecurityattributes).

## Adding Security Attributes to File Storage Service Mount Targets Created by the CSI Volume Plugin

You can use the`securityAttributes`parameter in the`StorageClass`manifest to specify the ZPR security attributes that the CSI volume plugin adds to the File Storage service mount targets it creates. For more information, see[Provisioning PVCs on the File Storage Service](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm)
