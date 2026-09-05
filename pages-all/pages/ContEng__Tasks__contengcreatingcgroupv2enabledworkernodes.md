# Enabling Cgroups v2 on OL8 Worker Nodes Using Custom Images
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingcgroupv2enabledworkernodes.htm
- Fetched: 2026-09-05 01:54 CDT

# Enabling Cgroups v2 on OL8 Worker Nodes Using Custom Images

Find out how to enable cgroups v2 on worker nodes that run Oracle Linux 8 (OL8) in clusters created with Kubernetes Engine (OKE), using custom images.
Note  
  

In OKE OL8 images that have a build number of 1367 or greater, cgroups v2 is enabled by default. However, in OKE OL8 images that have a build number lower than 1367 (and in OL8 platform images), cgroups v1 is enabled by default. This topic describes how to enable cgroups v2 in the Linux kernel of instances hosting worker nodes that use OKE OL8 images that have a build number lower than 1367, or that use OL8 platform images.

In clusters running Kubernetes version 1.35 (and later), the use of platform images (both OL7 platform images and OL8 platform images) is not recommended. We strongly recommend the use of OKE images for all new deployments and upgrades. If you want to continue to use a platform image, create a custom image based on the platform image and specify the custom image's OCID when creating or updating a node pool (note that we do not recommend this approach).

Control Groups (cgroups) is a Linux kernel feature that provides a mechanism for managing and controlling resource allocation for processes or groups of processes. The cgroups feature enables system administrators and developers to allocate and limit various system resources (such as CPU, memory, I/O, network bandwidth) to specific processes or sets of processes. Cgroups offers a powerful and flexible way to manage resource usage, ensuring that processes receive the necessary resources while preventing them from consuming excessive amounts and impacting the performance of other processes or the system as a whole. By creating and organizing processes into control groups, administrators can enforce resource constraints, prioritize tasks, and maintain system stability.

Oracle Linux provides two types of control groups:
- Control groups version 1 (cgroups v1): These groups provide a per-resource controller hierarchy. Each resource, such as CPU, memory, I/O, and so on, has its own control group hierarchy. A disadvantage of cgroups v1 is the difficulty of coordinating resource use among groups that might belong to different process hierarchies.
- Control groups version 2 (cgroups v2): These groups provide a single control group hierarchy against which all resource controllers are mounted. In this hierarchy, you can coordinate resource use across different resource controllers

For more information about control groups and Oracle Linux, see[Managing Resources Using Control Groups](https://docs.oracle.com/en/operating-systems/oracle-linux/8/boot/boot-Managing_Resources_Cgroups.html)in the Oracle Linux documentation.

Both cgroups v1 and cgroups v2 are present in Oracle Linux 8 (and later versions).

In OKE OL8 images that have a build number of 1367 or greater, cgroups v2 is enabled by default. In OKE OL8 images that have a build number lower than 1367 (and in OL8 platform images), cgroups v1 is enabled by default. Therefore, when you specify an OKE OL8 image with a build number lower than 1367 (or an OL8 platform image) for a node pool, cgroups v1 is enabled by default in the Linux kernels of compute instances hosting the nodes in the node pool.

However, you can enable cgroups v2 when using OKE OL8 images with a build number lower than 1367 (and OL8 platform images).

At a high level, the process to enable cgroups v2 is as follows:
- [Step 1: Create a compute instance running the required OL8 image, and enable cgroups v2](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingcgroupv2enabledworkernodes.htm#contengcreatingcgroupv2enabledworkernodes_createcomputeinstance).
- [Step 2: Enable cgroups v2 on the compute instance](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingcgroupv2enabledworkernodes.htm#contengcreatingcgroupv2enabledworkernodes_enablecgroupsv2).
- [Step 3: Create a custom image based on the compute instance where cgroups v2 is enabled](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingcgroupv2enabledworkernodes.htm#contengcreatingcgroupv2enabledworkernodes_createcustomimage).
- [Step 4: Add worker nodes running OL8 with cgroups v2 enabled to a cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingcgroupv2enabledworkernodes.htm#contengcreatingcgroupv2enabledworkernodes_addworkernodes). The way in which you add cgroups v2-enabled nodes to a cluster depends on whether you want to add the nodes as managed nodes or as self-managed nodes. For managed nodes, you define a managed node pool. For self-managed nodes, you add compute instances as worker nodes.

## Step 1: Create a compute instance running the required OL8 image, and enable cgroups v2

In this step, you use the Compute service to create a compute instance that is running the OL8 release you want on worker nodes in the Kubernetes cluster.
- Decide which OL8 release (and if you're going to select an OKE image, which Kubernetes version) you want on worker nodes.

Oracle provides a number of different OL8 OKE images and platform images.
- 

Follow the instructions in[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)in the Compute service documentation to create a new compute instance, and select a suitable platform image (either by selecting a platform image or by specifying the OCID of an OKE image).

This is the compute instance that you will use as the basis of a new custom image.

## Step 2: Enable cgroups v2 on the compute instance

In this step, you enable cgroups v2 on the compute instance you created in the previous step. The instructions here are intended as a convenient summary of[Enabling cgroups v2](https://docs.oracle.com/en/operating-systems/oracle-linux/8/boot/cgroups-EnableCGrp2.html)in the OL8 documentation.
- In a terminal window, connect to the compute instance and configure all kernel boot entries to mount cgroups v2 by default, by entering:

```

```

- Reboot the instance, by entering:

```

```

- Confirm that cgroups v2 is now mounted, by entering:

```

```

- Optionally, check the contents of the`/sys/fs/cgroup`directory (the root control group), by entering:

```

```

For cgroups v2, the files in the directory should have prefixes at the start of their file names (such as`cgroup`.*,`cpu`.*,`memory`.*).

## Step 3: Create a custom image based on the compute instance where cgroups v2 is enabled

In this step, you use the Compute service to create a custom image from the compute instance that you have enabled for cgroups v2 in the previous step.
- Shut down the instance that you have enabled for cgroups v2, by entering:
```

```

- Follow the instructions in[Managing Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm#Using2)in the Compute service documentation, to create a custom image based on the compute instance.
- Make a note of the OCID of the custom image you have created.

## Step 4: Add worker nodes running OL8 with cgroups v2 enabled to a cluster

In this step, you use the custom image you created in the previous step to add worker nodes running OL8 with cgroups v2 enabled to a Kubernetes cluster.

Note that there are different instructions to follow, depending on whether you want to enable cgroups v2 on managed nodes, or on self-managed nodes. For managed nodes, you define a managed node pool. For self-managed nodes, you add compute instances as worker nodes.

Note that you have to use the CLI to create managed nodes based on custom images.

### Adding managed nodes running OL8 with cgroups v2 enabled

To add managed nodes running OL8 with cgroups v2 enabled to an existing cluster:
- Open a command prompt and use the[oci ce node-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/create.html)command to create a new node pool.
- As well as the mandatory parameters required by the command, include the`--node-image-id`parameter, and specify the OCID of the custom image that you created in[Step 3: Create a custom image based on the compute instance where cgroups v2 is enabled](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingcgroupv2enabledworkernodes.htm#contengcreatingcgroupv2enabledworkernodes_createcustomimage).

For example, you might enter the following command:
```

```

### Adding self-managed nodes running OL8 with cgroups v2 enabled

Before you create a self-managed node:
- Confirm that the cluster to which you want to add the self-managed node is configured appropriately for self-managed nodes. See[Cluster Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-clusterreqs).
- Confirm that a dynamic group and an IAM policy already exist to allow the compute instance hosting the self-managed node to join an enhanced cluster created with Kubernetes Engine. See[Creating a Dynamic Group and a Policy for Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm).
- Create a cloud-init script containing the Kubernetes API private endpoint and base64-encoded CA certificate of the enhanced cluster to which you want to add the self- managed node. See[Creating Cloud-init Scripts for Self-managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm).

Using the Console
- Create a new compute instance to host the self-managed node:
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Follow the instructions in the[Compute service documentation](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)to create a new compute instance. Note that appropriate policies must exist to allow the new compute instance to join the enhanced cluster. See[Creating a Dynamic Group and a Policy for Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm).
- In the Image and Shape section, select Change image .
- Select My images , select the Image OCID option, and then enter the OCID of the custom image that you created in[Step 3: Create a custom image based on the compute instance where cgroups v2 is enabled](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingcgroupv2enabledworkernodes.htm#contengcreatingcgroupv2enabledworkernodes_createcustomimage).
- Select Advanced options , and in the Management section, select the Paste cloud-init script option.
- Copy and paste the cloud-init script for self-managed nodes that you created earlier, into the Cloud-init script field.
- Select Create to create the compute instance to host the self-managed node.

When the compute instance is created, it is added as a self-managed node to the cluster with the Kubernetes API endpoint that you specified in the cloud-init script.
- (Optional) Verify that the self-managed node has been added to the Kubernetes cluster, and that labels have been added to the node and set as expected, by following the instructions in[Creating Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingselfmanagednodes.htm).

Using the CLI
- Open a command prompt and enter the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html)oci Compute instance launch`command and required parameters to create a self-managed node.
- As well as the mandatory parameters required by the command:
- Include the`--image-id`parameter, and specify the OCID of the custom image that you created in[Step 3: Create a custom image based on the compute instance where cgroups v2 is enabled](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingcgroupv2enabledworkernodes.htm#contengcreatingcgroupv2enabledworkernodes_createcustomimage).
- Include the`--user-data-file`parameter and specify the cloud-init script for self-managed nodes that you created earlier.

For example, you might enter the following command:
```

```
