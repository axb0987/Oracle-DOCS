# Updating a Managed Node Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-node-pool.htm
- Fetched: 2026-09-05 01:58 CDT

# Updating a Managed Node Pool

Find out how to update a managed node pool using Kubernetes Engine (OKE).

For general information about updating node pools, see[Modifying Node Pool and Worker Node Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingnodepool.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-node-pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-node-pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-node-pool.htm#)
- 

To modify the properties of node pools and worker nodes of existing Kubernetes clusters:
- On the Clusters list page, select the name of the cluster you want to modify. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab, and then select the name of the node pool that you want to modify.
- 

Use the Details tab of the node pool page to view information about the node pool, including:
- The status of the node pool.
- The node pool's OCID.
- The type of the worker nodes in the node pool (managed).
- The configuration currently used when starting new worker nodes in the node pool, including:
- the version of Kubernetes to run on worker nodes
- the shape to use for worker nodes
- the image to use on worker nodes
- The availability domains, fault domains, and different regional subnets (recommended) or AD-specific subnets hosting worker nodes.
- 

Change managed node pool and managed node properties as follows:
- From the Actions menu, select Edit and specify:
- Name: A different name for the node pool. Avoid entering confidential information.
- 

Version: A different version of Kubernetes to run on new worker nodes in the node pool. You can select a newer Kubernetes version to upgrade managed nodes, or an earlier available Kubernetes version to roll back managed nodes. The Kubernetes version on worker nodes must be either the same version as that on the control plane nodes, or an earlier version that is still compatible (see[Kubernetes Versions and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengupgradeoverview.htm)).

Available Kubernetes version numbers are shown in`x.y`format, where`x`is a major version, and`y`is a minor version. Having selected a Kubernetes version in`x.y`format, you can optionally select Show patch versions and specify a supported patch version for the major.minor version you selected. However, we recommend you simply select a Kubernetes version in`x.y`format, to enable Kubernetes Engine to automatically select the most recent supported patch version for the minor version. For more information, see[Kubernetes Versions and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengupgradeoverview.htm).

If you specify an OKE image for worker nodes, the Kubernetes version you select here must be the same as the version of Kubernetes in the OKE image.

Updating the Kubernetes version configured for the node pool does not change the Kubernetes version running on existing managed nodes. To apply the selected Kubernetes version to the existing managed nodes, replace the nodes. For an enhanced cluster, you can cycle the node pool. For a basic cluster, manually delete and replace the managed nodes.

To upgrade managed nodes, see[Upgrading Managed Nodes to a Newer Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode.htm). To roll back managed nodes, see[Rolling Back Managed Nodes to an Earlier Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_Rolling-Back.htm).

You can also specify a newer version of Kubernetes for managed nodes by performing an out-of-place upgrade. For more information, see[Performing an Out-of-Place Managed Node Kubernetes Upgrade by Replacing an Existing Node Pool with a New Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode_topic-Performing_an_OutofPlace_Worker_Node_Upgrade_by_Replacing_an_Existing_Node_Pool_with_a_New_Node_Pool.htm).

Note the list of Kubernetes versions includes preview versions provided for early access testing and validation purposes only. These preview versions have ".0" as the patch version number (for example, 1.34.0). Preview versions are not intended for production workloads, and might contain issues without known workarounds. We do not recommend using preview versions for production workloads.
- Node count: A different number of nodes in the node pool. See[Scaling Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingnodepools.htm).
- 

Advanced options: Either accept the existing values for advanced node pool options, or select Advanced options and specify alternatives as follows:
- 

Cordon and drain: Change when and how to cordon and drain worker nodes before terminating them.
- Eviction grace period (mins): The length of time to allow to cordon and drain worker nodes before terminating them. Either accept the default (60 minutes, which is the maximum) or specify an alternative. For example, when scaling down a node pool or changing its placement configuration, you might want to allow 30 minutes to cordon worker nodes and drain them of their workloads. To terminate worker nodes immediately, without cordoning and draining them, specify 0 minutes.
- Force terminate after grace period: When replacing nodes or deleting nodes in the node pool, whether to terminate worker nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. By default, this option isn't selected.
- Force action after grace period: When performing maintenance tasks on worker nodes (such as rebooting a node, and replacing a node's boot volume), whether to perform the action at the end of the eviction grace period, even if the worker node hasn't been successfully cordoned and drained. By default, this option isn't selected.

Node pools containing worker nodes that can't be shut down or terminated within the eviction grace period have the Needs attention status. The status of the work request that initiated the termination operation is set to Failed , and the termination operation is cancelled. For more information, see[Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm).

For more information, see[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm).
- Initialization script: (Optional) A different script for cloud-init to run on instances hosting worker nodes when the instance boots up for the first time. The script you specify must be written in one of the formats supported by cloud-init (for example, cloud-config), and must be a supported filetype (for example, .yaml). Specify the script as follows:
- Choose cloud-init script: Select a file containing the cloud-init script, or drag and drop the file into the box.
- Paste cloud-init script: Copy the contents of a cloud-init script, and paste it into the box.

If you have not previously written cloud-init scripts for initializing worker nodes in clusters created by Kubernetes Engine, you might find it helpful to select Download to download a cloud-init script template. The downloaded file contains the default logic provided by Kubernetes Engine. You can add your own custom logic either before or after the default logic, but do not modify the default logic. For examples, see[Example Usecases for Custom Cloud-init Scripts](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm#contengusingcustomcloudinitscripts_topic_Examplecloudinitscriptusecases).
- Kubernetes labels: (Optional) One or more labels (in addition to a default label) to add to worker nodes in the node pool to enable the targeting of workloads at specific node pools. For example, to exclude all the nodes in a node pool from the list of backend servers in a load balancer backend set, specify`node.kubernetes.io/exclude-from-external-load-balancers=true`(see[node.kubernetes.io/exclude-from-external-load-balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengsupportedlabelsusecases.htm#exclude-from-external-load-balancers)).
- Add an SSH key: (Optional) A different public key portion of the key pair you want to use for SSH access to the nodes in the node pool. The public key is installed on all worker nodes in the cluster. Note that if you don't specify a public SSH key, Kubernetes Engine will provide one. However, since you won't have the corresponding private key, you will not have SSH access to the worker nodes. Note that you cannot use SSH to access directly any worker nodes in private subnets (see[Connecting to Managed Nodes in Private Subnets Using SSH](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconnectingworkernodesusingssh.htm#connectprivatesubnets)).
- Node placement configuration:
- Availability domain: An availability domain in which to place worker nodes.
- Worker node subnet compartment: The compartment in which the worker node subnet resides.
- Worker node subnet: A regional subnet (recommended) or AD-specific subnet configured to host worker nodes. If you specified load balancer subnets, the worker node subnets must be different. The subnets you specify can be private (recommended) or public. See[Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#subnetconfig).
- Fault domains: (Optional) One or more fault domains in the availability domain in which to place worker nodes.

Optionally select Advanced options to specify a capacity type to use (see[Managing Worker Node Capacity Types](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmanagingcapacitytypes.htm)). If you specify a capacity reservation, note that the node shape, availability domain, and fault domain in the managed node pool's placement configuration must match the capacity reservation's instance type, availability domain, and fault domain respectively. See[Using Capacity Reservations to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmakingcapacityreservations.htm). If you specify a compute host group, the compute host group must be active, must use the same shape as the node pool, and must be in the same availability domain as the placement configuration. See[Using Compute Host Groups to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusinghostgroups.htm).

When the worker nodes are created, they are distributed as evenly as possible across the availability domains and fault domains you select. If you don't select any fault domains for a particular availability domain, the worker nodes are distributed as evenly as possible across all the fault domains in that availability domain.

If the node pool uses a compute cluster, do not specify fault domains. All worker nodes in the managed node pool are created in the availability domain that contains the compute cluster. See[Using Compute Clusters to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcomputeclusters.htm).
- Network Launch Type: Optionally select a different networking launch type for worker node networking. If you do not select a value, PARAVIRTUALIZED is used as the default.

In most cases, select PARAVIRTUALIZED . Select VFIO only when the selected shape and image support hardware-assisted SR-IOV networking and your workload requires it. Select E1000 only when required for compatibility with an image or workload that does not support paravirtualized networking. Support for each launch type depends on the selected compute shape and image.
- Primary VNIC: (VCN-native pod networking only) Optionally specify one or more (up to a maximum of five) ZPR security attributes to add to the primary VNIC of worker nodes in the node pool.

If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.

See also[Adding Security Attributes to Cluster-Related Resources and Applying ZPR Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm)
- Configure Secondary VNICs for nodes: When the cluster's Network type is VCN-native pod networking , optionally change one or more secondary VNICs. For more information, see[Attaching Multiple Secondary VNICs for Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengAttaching_Multiple_VNICs.htm).
- 

Node shape: A different shape to use for worker nodes in the node pool. The shape determines the number of CPUs and the amount of memory allocated to each node. To change the shape, select Change shape .

Only those shapes available in your tenancy that are supported by Kubernetes Engine are shown. If you select a flexible shape, you can explicitly specify the number of CPUs and the amount of memory. See[Supported Images (Including Custom Images) and Shapes for Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengimagesshapes.htm).

If the node pool uses a compute cluster, only select a node shape that supports RDMA and compute clusters. See[Using Compute Clusters to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcomputeclusters.htm)
- 

Image: A different image to use on worker nodes in the node pool. An image is a template of a virtual hard drive that determines the operating system and other software for the node.

To change the image, select Change image . In the Browse all images window, choose an Image source and select an image as follows:
- 

OKE Worker Node Images: Recommended. Provided by Oracle and built on top of platform images. OKE images are optimized to serve as base images for worker nodes, with all the necessary configurations and required software. Select an OKE image if you want to minimize the time it takes to provision worker nodes at runtime when compared to platform images and custom images.

OKE image names include the version number of the Kubernetes version they contain. Note that if you specify a Kubernetes version for the node pool, the OKE image you select here must have the same version number as the node pool's Kubernetes version.
- Platform images: Provided by Oracle and only contain an Oracle Linux operating system. For Kubernetes versions earlier than 1.35, select a platform image if you want Kubernetes Engine to download, install, and configure required software when the compute instance hosting a worker node boots up for the first time.

In clusters running Kubernetes version 1.35 (and later), the use of platform images (both OL7 platform images and OL8 platform images) is not recommended. We strongly recommend the use of OKE images for all new deployments and upgrades.

See[Supported Images (Including Custom Images) and Shapes for Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengimagesshapes.htm).
- Use security rules in Network Security Group (NSG): Control access to the node pool using security rules defined for one or more network security groups (NSGs) that you specify (up to a maximum of five). You can use security rules defined for NSGs instead of, or as well as, those defined for security lists (NSGs are recommended). For more information about the security rules to specify for the NSG, see[Security Rules for Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#securitylistconfig__section_rules_for_worker_nodes).
- 

Boot volume : Change the size and encryption options for the worker node's boot volume:
- To specify a custom size for the boot volume, select Specify a custom boot volume size and enter a custom size from 50 GB to 32 TB. The specified size must be larger than the default boot volume size for the selected image. See[Custom Boot Volume Sizes](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm#Custom)for more information.

Note that if you increase the boot volume size, you also need to extend the partition for the boot volume (the root partition) to take advantage of the larger size. See[Extending the Partition for a Boot Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/extendingbootpartition.htm). Oracle Linux platform images include the`oci-utils`package. You can use the`[](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-growfs)oci-growfs`command from that package in a custom cloud-init script to extend the root partition and then grow the file system. For more information, see[Extending the Root Partition of Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengextendingrootpartitionmanually.htm).
- For VM instances, you can optionally select Use in-transit encryption . For[bare metal instances](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption__bm)that support in-transit encryption, it is enabled by default and is not configurable. See[Block Volume Encryption](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption)for more information about in-transit encryption. If you are using your own Vault service encryption key for the boot volume, then this key is also used for in-transit encryption. Otherwise, the Oracle-provided encryption key is used.
- Boot volumes are encrypted by default, but you can optionally use your own Vault service encryption key to encrypt the data in this volume. To use the[Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)for your encryption needs, select Encrypt this volume with a key that you manage . Select the vault compartment and vault that contains the master encryption key that you want to use, and then select the master encryption key compartment and master encryption key. If you enable this option, this key is used for both data at rest encryption and in-transit encryption.
Important  
  
The Block Volume service does not support encrypting volumes with keys encrypted using the Rivest-Shamir-Adleman (RSA) algorithm. When using your own keys, you must use keys encrypted using the Advanced Encryption Standard (AES) algorithm. This applies to block volumes and boot volumes.

Note that to use your own Vault service encryption key to encrypt data, an IAM policy must grant access to the service encryption key. See[Create Policy to Access User-Managed Encryption Keys for Encrypting Boot Volumes, Block Volumes, and/or File Systems](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpolicyconfig.htm#contengpolicyconfig_topic_Create_Policies_for_User_Managed_Encryption).
- Pod communication: When the cluster's Network type is VCN-native pod networking , change how pods in the node pool communicate with each other using a pod subnet:
- Subnet compartment: The compartment in which the pod subnet resides.
- Subnet: A regional subnet configured to host pods. The pod subnet you specify must be private. In some situations, the worker node subnet and the pod subnet can be the same subnet (in which case, Oracle recommends defining security rules in network security groups rather than in security lists). See[Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#subnetconfig).
- Use security rules in Network Security Group (NSG): Control access to the pod subnet using security rules defined for one or more network security groups (NSGs) that you specify (up to a maximum of five). You can use security rules defined for NSGs instead of, or as well as, those defined for security lists (NSGs are recommended). For more information about the security rules to specify for the NSG, see[Security Rules for Worker Nodes and Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_pods_security_rules).

Optionally select Advanced options to specify the maximum number of pods that you want to run on a single worker node in a node pool, up to a limit of 256. The limit of 256 is the maximum number of IP addresses that can be assigned to a worker node. Select a shape that supports sufficient VNIC attachments and ensure the pod IP capacity is sized appropriately using the`ipCount`values configured for the secondary VNIC profiles. If you define Application Resources on secondary VNIC profiles, a pod can request a single Application Resource to pin to one selected profile and must include the required toleration for the node taint. If you deploy multi-interface pods, attach additional interfaces using Multus and NADs, and do not combine Multus network annotations with pod-level Application Resource requests in the same pod spec. For more information, see[Maximum Number of VNICs and Pods Supported by Different Shapes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_vnics_pods_shapes)and[Attaching Multiple Secondary VNICs for Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengAttaching_Multiple_VNICs.htm).

Note that node pools that expose Application Resources are tainted to prevent pods without explicit Application Resource requests from scheduling on those nodes. Pods that request an Application Resource must include a matching toleration. For more information about pod communication, see[Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking.htm).
- Select Update to save the updated properties.
- Use the Kubernetes labels tab to see the labels applied to managed nodes.
- Use the Nodes tab to see information about specific worker nodes in the managed node pool. Optionally edit the configuration details of a specific worker node by selecting the worker node's name.
- Use the Security tab to see information about the ZPR security attributes that have been added to the primary VNIC and secondary VNICs of managed nodes in the node pool. Optionally add or remove the security attributes. For more information, see[Adding Security Attributes to Cluster-Related Resources and Applying ZPR Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm)
- Use the Monitoring tab to monitor the health, capacity, and performance of the managed node pool. For more information, see[Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengmetrics.htm).
- Use the Work requests tab:
- Get the details of a particular work request for the node pool resource.
- List the work requests for the node pool resource.

For more information, see[Viewing Work Requests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm).
- Use the Tags tab to add or modify tags applied to the node pool (and the tags applied to compute instances hosting managed nodes in the node pool). Tagging enables you to group disparate resources across compartments, and also enables you to annotate resources with your own metadata. See[Tagging Kubernetes Cluster-Related Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources.htm).
- 

Use the[oci ce node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/update.html)command and required parameters to update a managed node pool:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool)
