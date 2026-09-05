# Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm
- Fetched: 2026-09-05 01:54 CDT

# Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow

Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine (OKE).

To create a cluster with explicitly defined settings and existing network resources in the 'Custom Create' workflow using Kubernetes Engine:
- On the Clusters list page, select Create cluster . If you need help finding the list page, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- In the Create cluster dialog, select Custom create and select Proceed .
- 

On the Create cluster page, either just accept the default configuration details for the new cluster, or specify alternatives as follows:
- Name: The name of the new cluster. Either accept the default name or enter a name of your choice. Avoid entering confidential information.
- Compartment: The compartment in which to create the new cluster.
- 

Kubernetes version: The version of Kubernetes to run on the cluster's control plane nodes. Either accept the default version or select a version of your choice. Amongst other things, the Kubernetes version you select determines the default set of admission controllers that are turned on in the created cluster (see[Supported Admission Controllers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengadmissioncontrollers.htm)).

Available Kubernetes version numbers are shown in`x.y`format, where`x`is a major version, and`y`is a minor version. Having selected a Kubernetes version in`x.y`format, you can optionally select Show patch versions and specify a supported patch version for the major.minor version you selected. However, we recommend you simply select a Kubernetes version in`x.y`format, to enable Kubernetes Engine to automatically select the most recent supported patch version for the minor version. For more information, see[Kubernetes Versions and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengupgradeoverview.htm).

Note the list of Kubernetes versions includes preview versions provided for early access testing and validation purposes only. These preview versions have ".0" as the patch version number (for example, 1.34.0). Preview versions are not intended for production workloads, and might contain issues without known workarounds. We do not recommend using preview versions for production workloads.
- 

Either accept the defaults for advanced cluster options, or select Advanced options and set the options as follows:
- 

Image verification: Specify whether to only allow the deployment of images from Oracle Cloud Infrastructure Registry that have been signed by particular master encryption keys. To enforce the use of signed images, select Enable image verification policies on this cluster , and then specify the encryption key and the vault that contains it. See[Enforcing the Use of Signed Images from Registry](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengenforcingsignedimagesfromocir.htm).
- 

Kubernetes secrets encryption: Specify how to encrypt Kubernetes secrets at rest in the etcd key-value store for the cluster:
- Encrypt using an Oracle-managed key: Encrypt Kubernetes secrets in the etcd key-value store using a master encryption key that is managed by Oracle.
- 

Encrypt using a key that you manage: Encrypt Kubernetes secrets in the etcd key-value store using a master encryption key (stored in the Vault service) that you manage. If you select this option, specify:
- Choose a vault: The vault that contains the master encryption key, from the list of vaults in the specified compartment. By default, the compartment is the one in which you are creating the cluster, but you can select a different compartment.
- Choose a key: The name of the master encryption key, from the list of keys in the specified compartment. By default, the compartment is the one in which you are creating the cluster, but you can select a different compartment. Note that you cannot change the master encryption key after the cluster has been created.

Note that if you want to manage the master encryption key, a suitable key, dynamic group, and policy must already exist before you can create the cluster. For more information, see[Encrypting Kubernetes Secrets at Rest in Etcd](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengencryptingdata.htm).
- 

Pod Security Policies: (Kubernetes versions prior to 1.25) Specify whether to control the operations that pods are allowed to perform on the cluster by enforcing pod security policies:
- Not Enforced: Do not enforce pod security policies.
- Enforced: Do enforce pod security policies, by enabling the PodSecurityPolicy admission controller. Only pods that meet the conditions in a pod security policy are accepted by the cluster. For more information, see[Using Pod Security Policies with Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingpspswithoke.htm).
Caution  
  

It is very important to note that when you enable a cluster's PodSecurityPolicy admission controller, no application pods can start on the cluster unless suitable pod security policies exist, along with roles (or clusterroles) and rolebindings (or clusterrolebindings) to associate pods with policies. You will not be able to run application pods on a cluster with an enabled PodSecurityPolicy admission controller unless these prerequisites are met.

We strongly recommend you use PodSecurityPolicy admission controllers as follows:
- Whenever you create a new cluster, enable the Pod Security Admission Controller.
- Immediately after creating a new cluster, create pod security policies, along with roles (or clusterroles) and rolebindings (or clusterrolebindings).
- Configure cluster add-ons: (Enhanced clusters only) Enable or disable specific add-ons, select add-on versions, opt into and out of automatic updates by Oracle, and manage add-on specific customizations. Select Edit from the Actions menu (three dots) beside a cluster add-on, and set configuration options as appropriate. See[Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm).
- OpenID Connect (OIDC) Discovery: (Enhanced clusters only) Specify whether to enable the cluster for OIDC Discovery. Select Enable OIDC discovery to enable application pods running on the cluster to authenticate using OIDC Discovery when accessing APIs hosted on an external cloud provider. See[Authorizing Pods to Access Non-OCI Resources Using OpenID Connect (OIDC) Discovery](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengOpenIDConnect-Discovery.htm).
- Tagging: Specify whether to add Cluster tags to the cluster, Initial load balancer tags to load balancers created by Kubernetes services of type LoadBalancer, and Initial block volume tags to block volumes created by Kubernetes persistent volume claims. Tagging enables you to group disparate resources across compartments, and also enables you to annotate resources with your own metadata. See[Tagging Kubernetes Cluster-Related Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources.htm).
- 

Select Next and specify the existing network resources to use for the new cluster on the Network setup page:
- Network type: Specify how pods running on nodes in the cluster communicate with each other, with the cluster's control plane nodes, with pods on other clusters, with other services (such as storage services), and with the internet (see[Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking.htm)). Select one of the following options:
- VCN-native pod networking: Select this option to connect nodes in a Kubernetes cluster to pod subnets in an Oracle Cloud Infrastructure VCN. As a result, pod IP addresses within a VCN are directly routable from other VCNs connected (peered) to that VCN, and from on-premise networks. You can create both virtual nodes and managed nodes if you select this option. See[Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm).
- Flannel overlay: Select this option to encapsulate communication between pods in the flannel overlay network, a simple private overlay virtual network that satisfies the requirements of the Kubernetes networking model by attaching IP addresses to containers. The pods in the private overlay network are only accessible from other pods in the same cluster. You can create managed nodes (but not virtual nodes) if you select this option. See[Using the flannel CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-flannel_CNI_plugin.htm).
- VCN: Select the existing virtual cloud network that has been configured for cluster creation and deployment, from the list of VCNs in the specified compartment. By default, the compartment is the one in which you are creating the cluster, but you can select a different compartment. See[VCN Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#vcnconfig).
- Kubernetes API endpoint subnet: Select a regional subnet to host the cluster's Kubernetes API endpoint, from the list of subnets in the specified compartment. By default, the compartment is the one in which you are creating the cluster, but you can select a different compartment. The subnet you specify can be public or private. The Kubernetes API endpoint is always assigned a private IP address. If you specify a public subnet, you can optionally expose the Kubernetes API endpoint to the internet by assigning a public IP address to the endpoint (as well as the private IP address). To simplify access management, Oracle recommends the Kubernetes API endpoint is in a different subnet to worker nodes and load balancers. For more information, see[Kubernetes Cluster Control Plane and Kubernetes API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengclustersnodes.htm#processes).
- Use security rules in Network Security Group (NSG): Control access to the cluster's Kubernetes API endpoint using security rules defined for one or more network security groups (NSGs) that you specify. You can use security rules defined for NSGs instead of, or as well as, those defined for security lists (NSGs are recommended). For more information about the security rules to specify for the NSG, see[Security Rules for the Kubernetes API Endpoint](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#securitylistconfig__section_jsz_kqw_r4b).
- Automatically assign public IPv4 address: If you selected a public subnet for the Kubernetes API endpoint, you can optionally expose the endpoint to the internet by assigning a public IP address to the endpoint. If you do not assign a public IP address, update route rules and security rules to enable access to the endpoint using a service gateway and a NAT gateway (see[Kubernetes API Endpoint Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#subnetconfig__section_kcm_v2b_s4b)).
- Automatically assign IPv6 address from subnet prefixes: If you selected an IPv4/IPv6 dual stack subnet for the Kubernetes API endpoint, you can optionally assign an IPv6 address to the endpoint to make the cluster a dual stack cluster. If you select this option, the IPv6 address for the endpoint is automatically chosen from the first IPv6 prefix assigned to the subnet. For more information, see[Enabling Clusters for IPv4 and IPv6](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng_ipv4-and-ipv6.htm).
- 

Load balancer subnets: Optionally, select existing subnets that have been configured to host load balancers, from the list of subnets in the specified compartment. By default, the compartment is the one in which you are creating the cluster, but you can select a different compartment. Load balancer subnets must be different from worker node subnets, can be public or private, and can be regional (recommended) or AD-specific. You don't have to specify any load balancer subnets. However, if you do specify load balancer subnets, the number of load balancer subnets to specify depends on the region in which you are creating the cluster and whether the subnets are regional or AD-specific.

If you are creating a cluster in a region with three availability domains, you can specify:
- Zero or one load balancer regional subnet (recommended).
- Zero or two load balancer AD-specific subnets. If you specify two AD-specific subnets, the two subnets must be in different availability domains.

If you are creating a cluster in a region with a single availability domain, you can specify:
- Zero or one load balancer regional subnet (recommended).
- Zero or one load balancer AD-specific subnet.

See[Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#subnetconfig).
- 

Either accept the defaults for advanced network options, or select Advanced options and specify alternatives as follows:
- Endpoint security attributes: One or more (up to a maximum of five) ZPR security attributes to add to the cluster's Kubernetes API endpoint.

If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.

See also[Adding Security Attributes to Cluster-Related Resources and Applying ZPR Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm)
- Kubernetes service CIDR block: The available group of IPv4 network addresses that can be exposed as Kubernetes services (ClusterIPs), expressed as a single, contiguous IPv4 CIDR block. For example,`10.96.0.0/16`. The IPv4 CIDR block you specify must not overlap with the IPv4 CIDR block for the VCN. For a dual stack cluster, you can also specify a Kubernetes service IPv6 prefix . See[IPv4 CIDR Blocks and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengcidrblocks.htm).
- Kubernetes service IPv6 prefix: When creating a dual stack cluster, the available group of IPv6 network addresses that can be exposed as Kubernetes services (ClusterIPs), expressed as a single, contiguous IPv6 CIDR block. For example,`fd00:eeee:eeee:0001::/108`. The IPv6 CIDR block you specify must not overlap with the IPv6 CIDR block for the VCN. For a dual stack cluster, you can also specify a Kubernetes service CIDR block . See[Enabling Clusters for IPv4 and IPv6](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng_ipv4-and-ipv6.htm).
- Pods CIDR block: If you selected Flannel overlay: as the Network Type , the available group of network addresses that can be allocated to pods running in the cluster, expressed as a single, contiguous IPv4 CIDR block. For example,`10.244.0.0/16`. The CIDR block you specify must not overlap with the CIDR blocks for subnets in the VCN, and can be outside the VCN CIDR block. For a dual stack cluster, you can specify both an IPv4 CIDR block and an IPv6 CIDR block (separated by a comma). Do not specify a CIDR block if you selected VCN-native pod networking as the cluster's Network type . See[IPv4 CIDR Blocks and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengcidrblocks.htm).
- 

Select Next and specify configuration details for the first node pool in the cluster on the Node Pools page:
- Name: A name of your choice for the new node pool. Avoid entering confidential information.
- Compartment: The compartment in which to create the new node pool.
- Node Type: If you selected VCN-native pod networking: as the Network Type , specify the type of worker nodes in this node pool (see[Virtual Nodes and Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengclustersnodes.htm#contengclustersnodes_topic-Provisioned_Virtual_Nodes)). Select one of the following options:
- Managed: Select this option when you want to have responsibility for managing the worker nodes in the node pool. Managed nodes run on compute instances (either bare metal or virtual machine) in your tenancy. As you are responsible for managing managed nodes, you have the flexibility to configure them to meet your specific requirements. You are responsible for upgrading Kubernetes on managed nodes, and for managing cluster capacity.
- Virtual: Select this option when you want to benefit from a 'serverless' Kubernetes experience. Virtual nodes enable you to run Kubernetes pods at scale without the operational overhead of upgrading the data plane infrastructure and managing the capacity of clusters.

For more information, see[Comparing Virtual Nodes with Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingvirtualwithmanagednodes_topic.htm).
- 

Kubernetes Version: (Managed node pools only) The version of Kubernetes to run on each managed node in the managed node pool. By default, the version of Kubernetes specified for the control plane nodes is selected. The Kubernetes version on worker nodes must be either the same version as that on the control plane nodes, or an earlier version that is still compatible. See[Kubernetes Versions and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengupgradeoverview.htm).

Available Kubernetes version numbers are shown in`x.y`format, where`x`is a major version, and`y`is a minor version. Having selected a Kubernetes version in`x.y`format, you can optionally select Show patch versions and specify a supported patch version for the major.minor version you selected. However, we recommend you simply select a Kubernetes version in`x.y`format, to enable Kubernetes Engine to automatically select the most recent supported patch version for the minor version. For more information, see[Kubernetes Versions and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengupgradeoverview.htm).
If you specify an OKE image for worker nodes, the Kubernetes version you select here must be the same as the version of Kubernetes in the OKE image.

Note the list of Kubernetes versions includes preview versions provided for early access testing and validation purposes only. These preview versions have ".0" as the patch version number (for example, 1.34.0). Preview versions are not intended for production workloads, and might contain issues without known workarounds. We do not recommend using preview versions for production workloads.
- 

If you selected VCN-native pod networking as the Network Type and Managed as the Node Type , or if you selected Flannel overlay: as the Network Type :
- Specify configuration details for the managed node pool:
- Node Placement Configuration:
- Availability domain: An availability domain in which to place worker nodes.
- Worker node subnet: A regional subnet (recommended) or AD-specific subnet configured to host worker nodes from the list of subnets in the specified compartment. By default, the compartment is the one in which you are creating the cluster, but you can select a different compartment. If you specified load balancer subnets, the worker node subnets must be different. The subnets you specify can be private (recommended) or public. See[Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#subnetconfig).
- Fault domains: (Optional) One or more fault domains in the availability domain in which to place worker nodes.

Optionally select Advanced options to specify a capacity type to use (see[Managing Worker Node Capacity Types](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmanagingcapacitytypes.htm)). If you specify a capacity reservation, note that the node shape, availability domain, and fault domain in the managed node pool's placement configuration must match the capacity reservation's instance type, availability domain, and fault domain respectively. See[Using Capacity Reservations to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmakingcapacityreservations.htm). If you specify a compute host group, the compute host group must be active, must use the same shape as the node pool, and must be in the same availability domain as the placement configuration. See[Using Compute Host Groups to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusinghostgroups.htm).

When the worker nodes are created, they are distributed as evenly as possible across the availability domains and fault domains you select. If you don't select any fault domains for a particular availability domain, the worker nodes are distributed as evenly as possible across all the fault domains in that availability domain.

If the node pool uses a compute cluster, do not specify fault domains. All worker nodes in the managed node pool are created in the availability domain that contains the compute cluster. See[Using Compute Clusters to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcomputeclusters.htm).
- Network Launch Type: Optionally select the networking launch type for worker node networking. If you do not select a value, PARAVIRTUALIZED is used as the default.

In most cases, select PARAVIRTUALIZED . Select VFIO only when the selected shape and image support hardware-assisted SR-IOV networking and your workload requires it. Select E1000 only when required for compatibility with an image or workload that does not support paravirtualized networking. Support for each launch type depends on the selected compute shape and image.
- Primary VNIC: (VCN-native pod networking only) Optionally specify one or more (up to a maximum of five) ZPR security attributes to add to the primary VNIC of worker nodes in the node pool.

If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.

See also[Adding Security Attributes to Cluster-Related Resources and Applying ZPR Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm)
- Configure Secondary VNICs for nodes: (VCN-native pod networking only) Optionally define one or more secondary VNICs. For more information, see[Attaching Multiple Secondary VNICs for Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengAttaching_Multiple_VNICs.htm).
- 

Node shape: The shape to use for worker nodes in the managed node pool. The shape determines the number of CPUs and the amount of memory allocated to each managed node. To change the default shape, select Change shape .

Only those shapes available in your tenancy that are supported by Kubernetes Engine are shown. If you select a flexible shape, you can explicitly specify the number of CPUs and the amount of memory. See[Supported Images (Including Custom Images) and Shapes for Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengimagesshapes.htm).

If you specify a compute cluster for the managed node pool, select a node shape that supports RDMA and compute clusters. See[Using Compute Clusters to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcomputeclusters.htm).
- 

Image: The image to use on worker nodes in the managed node pool. An image is a template of a virtual hard drive that determines the operating system and other software for the managed node pool.

To change the default image, select Change image . In the Browse all images window, choose an Image source and select an image as follows:
- 

OKE Worker Node Images: Recommended. Provided by Oracle and built on top of platform images. OKE images are optimized to serve as base images for worker nodes, with all the necessary configurations and required software. Select an OKE image if you want to minimize the time it takes to provision worker nodes at runtime when compared to platform images and custom images.

OKE image names include the version number of the Kubernetes version they contain. Note that if you specify a Kubernetes version for the node pool, the OKE image you select here must have the same version number as the node pool's Kubernetes version.
- Platform images: Provided by Oracle and only contain an Oracle Linux operating system. For Kubernetes versions earlier than 1.35, select a platform image if you want Kubernetes Engine to download, install, and configure required software when the compute instance hosting a worker node boots up for the first time.

In clusters running Kubernetes version 1.35 (and later), the use of platform images (both OL7 platform images and OL8 platform images) is not recommended. We strongly recommend the use of OKE images for all new deployments and upgrades.

See[Supported Images (Including Custom Images) and Shapes for Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengimagesshapes.htm).
- Node count: The number of worker nodes to create in the managed node pool, placed in the availability domains you select, and in the regional subnet (recommended) or AD-specific subnet you specify for each availability domain.
- Use security rules in Network Security Group (NSG): Control access to the node pool using security rules defined for one or more network security groups (NSGs) that you specify (up to a maximum of five). You can use security rules defined for NSGs instead of, or as well as, those defined for security lists (NSGs are recommended). For more information about the security rules to specify for the NSG, see[Security Rules for Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#securitylistconfig__section_rules_for_worker_nodes).
- 

Boot volume : Configure the size and encryption options for managed node boot volumes:
- To specify a custom size for the boot volume, select Specify a custom boot volume size and enter a custom size from 50 GB to 32 TB. The specified size must be larger than the default boot volume size for the selected image. See[Custom Boot Volume Sizes](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm#Custom)for more information.

Note that if you increase the boot volume size, you also need to extend the partition for the boot volume (the root partition) to take advantage of the larger size. See[Extending the Partition for a Boot Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/extendingbootpartition.htm). Oracle Linux platform images include the`oci-utils`package. You can use the`[](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-growfs)oci-growfs`command from that package in a custom cloud-init script to extend the root partition and then grow the file system. For more information, see[Extending the Root Partition of Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengextendingrootpartitionmanually.htm).
- For VM instances, you can optionally select Use in-transit encryption . For[bare metal instances](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption__bm)that support in-transit encryption, it is enabled by default and is not configurable. See[Block Volume Encryption](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption)for more information about in-transit encryption. If you are using your own Vault service encryption key for the boot volume, then this key is also used for in-transit encryption. Otherwise, the Oracle-provided encryption key is used.
- Boot volumes are encrypted by default, but you can optionally use your own Vault service encryption key to encrypt the data in this volume. To use the[Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)for your encryption needs, select Encrypt this volume with a key that you manage . Select the vault compartment and vault that contains the master encryption key that you want to use, and then select the master encryption key compartment and master encryption key. If you enable this option, this key is used for both data at rest encryption and in-transit encryption.
Important  
  
The Block Volume service does not support encrypting volumes with keys encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When using your own keys, you must use keys encrypted using the Advanced Encryption Standard (AES) algorithm. This applies to block volumes and boot volumes.

Note that to use your own Vault service encryption key to encrypt data, an IAM policy must grant access to the service encryption key. See[Create Policy to Access User-Managed Encryption Keys for Encrypting Boot Volumes, Block Volumes, and/or File Systems](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpolicyconfig.htm#contengpolicyconfig_topic_Create_Policies_for_User_Managed_Encryption).
- Pod communication: If you selected VCN-native pod networking as the Network Type and Managed as the Node Type , specify how pods in the managed node pool communicate with each other using a pod subnet:
- Subnet compartment: The compartment in which the pod subnet resides.
- Subnet: A regional subnet configured to host pods. The pod subnet you specify must be private. In some situations, the worker node subnet and the pod subnet can be the same subnet (in which case, Oracle recommends defining security rules in network security groups rather than in security lists). See[Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#subnetconfig).
- Use security rules in Network Security Group (NSG): Control access to the pod subnet using security rules defined for one or more network security groups (NSGs) that you specify (up to a maximum of five). You can use security rules defined for NSGs instead of, or as well as, those defined for security lists (NSGs are recommended). For more information about the security rules to specify for the NSG, see[Security Rules for Worker Nodes and Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_pods_security_rules).

Optionally select Advanced options to specify the maximum number of pods that you want to run on a single worker node in a managed node pool, up to a limit of 256. The limit of 256 is the maximum number of IP addresses that can be assigned to a worker node. Select a shape that supports sufficient VNIC attachments and ensure the pod IP capacity is sized appropriately using the`ipCount`values configured for the secondary VNIC profiles. If you define Application Resources on secondary VNIC profiles, a pod can request a single Application Resource to pin to one selected profile and must include the required toleration for the node taint. If you deploy multi-interface pods, attach additional interfaces using Multus and NADs, and do not combine Multus network annotations with pod-level Application Resource requests in the same pod spec. For more information, see[Maximum Number of VNICs and Pods Supported by Different Shapes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_vnics_pods_shapes)and[Attaching Multiple Secondary VNICs for Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengAttaching_Multiple_VNICs.htm).

Note that node pools that expose Application Resources are tainted to prevent pods without explicit Application Resource requests from scheduling on those nodes. Pods that request an Application Resource must include a matching toleration.

For more information about pod communication, see[Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking.htm).
- 

Either accept the defaults for advanced managed node pool options, or select Advanced options and specify alternatives as follows:
- 

Cordon and drain: Specify when and how to cordon and drain managed nodes before shutting down or terminating them.
- Eviction grace period (mins): The length of time to allow to cordon and drain worker nodes before shutting down or terminating them. Either accept the default (60 minutes, which is the maximum) or specify an alternative. For example, when scaling down a node pool or changing its placement configuration, you might want to allow 30 minutes to cordon worker nodes and drain them of their workloads. To shut down or terminate worker nodes immediately, without cordoning and draining them, specify 0 minutes.
- Force terminate after grace period: When replacing nodes or deleting nodes in the node pool, whether to terminate worker nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. By default, this option isn't selected.
- Force action after grace period: When performing maintenance tasks on worker nodes (such as rebooting a node, and replacing a node's boot volume), whether to perform the action at the end of the eviction grace period, even if the worker node hasn't been successfully cordoned and drained. By default, this option isn't selected.

Node pools containing worker nodes that can't be shut down or terminated within the eviction grace period have the Needs attention status. The status of the work request that initiated the shut down or termination operation is set to Failed , and the operation is cancelled. For more information, see[Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm).

For more information, see[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm).
- Initialization script: (Optional) A script for cloud-init to run on each instance hosting managed nodes when the instance boots up for the first time. The script you specify must be written in one of the formats supported by cloud-init (for example, cloud-config), and must be a supported filetype (for example, .yaml). Specify the script as follows:
- Choose cloud-init script: Select a file containing the cloud-init script, or drag and drop the file into the box.
- Paste cloud-init script: Copy the contents of a cloud-init script, and paste it into the box.

If you have not previously written cloud-init scripts for initializing worker nodes in clusters created by Kubernetes Engine, you might find it helpful to select Download to download a cloud-init script template. The downloaded file contains the default logic provided by Kubernetes Engine. You can add your own custom logic either before or after the default logic, but do not modify the default logic. For examples, see[Example Usecases for Custom Cloud-init Scripts](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm#contengusingcustomcloudinitscripts_topic_Examplecloudinitscriptusecases).
- Kubernetes labels: (Optional) One or more labels (in addition to a default label) to add to worker nodes in the node pool to enable the targeting of workloads at specific node pools. For example, to exclude all the nodes in a node pool from the list of backend servers in a load balancer backend set, specify`node.kubernetes.io/exclude-from-external-load-balancers=true`(see[node.kubernetes.io/exclude-from-external-load-balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengsupportedlabelsusecases.htm#exclude-from-external-load-balancers)).
- Node pool tags and Node tags: (Optional) One or more tags to add to the node pool, and to compute instances hosting worker nodes in the node pool. Tagging enables you to group disparate resources across compartments, and also enables you to annotate resources with your own metadata. See[Tagging Kubernetes Cluster-Related Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources.htm).
- Add an SSH key: (Optional) Either generate a key pair or upload the public key portion of the key pair you want to use for SSH access to each node in the node pool. The public key is installed on all worker nodes in the cluster. Note that if you don't specify a public SSH key, Kubernetes Engine will provide one. However, since you won't have the corresponding private key, you will not have SSH access to the worker nodes. Note that you cannot use SSH to access directly any worker nodes in private subnets (see[Connecting to Managed Nodes in Private Subnets Using SSH](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconnectingworkernodesusingssh.htm#connectprivatesubnets)).
- Compute cluster: (Optional) Specify a compute cluster for the managed node pool. Select the compartment that contains the compute cluster, and then select the compute cluster. The compute cluster must be active. You can only specify a compute cluster when creating the managed node pool. You cannot add, remove, or change the compute cluster later. See[Using Compute Clusters to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcomputeclusters.htm).
- 

If you selected Virtual as the Node Type :

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
- If you have not selected any of the enhanced cluster features and you want to create the new cluster as a basic cluster rather than as an enhanced cluster, choose the Create a Basic cluster option on the Review and create page. See[Working with Enhanced Clusters and Basic Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenhancedclusters.htm).
- 

Select Create cluster to create the new cluster now.

Kubernetes Engine starts creating the cluster with the name you specified.

If you specified details for one or more node pools, Kubernetes Engine creates:
- node pools with the names you specified
- worker nodes with auto-generated names (managed node names have the format`oke-c<part-of-cluster-OCID>-n<part-of-node-pool-OCID>-s<part-of-subnet-OCID>-<slot>`, virtual node names are the same as the node's private IP address)

Do not change the auto-generated names of worker nodes.

Note that rather than creating the new cluster immediately, you can create it later using Resource Manager and Terraform, by selecting Save as stack to save the resource definition as a Terraform configuration. For more information about saving stacks from resource definitions, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
- Select Close to return to the Console.

Initially, the new cluster appears in the Console with a status of Creating. When the cluster has been created, it has a status of Active.
