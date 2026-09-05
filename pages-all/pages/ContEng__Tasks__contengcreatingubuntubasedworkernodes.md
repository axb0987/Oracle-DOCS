# Running Ubuntu on Worker Nodes Using Custom Images
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm
- Fetched: 2026-09-05 01:54 CDT

# Running Ubuntu on Worker Nodes Using Custom Images

Find out how to include worker nodes that run the Ubuntu Linux distribution in clusters created with Kubernetes Engine (OKE), using custom images and cloud-init scripts.

Ubuntu is a popular open-source Linux distribution that is commonly used to run GPU-intensive and AI/ML workloads. When you create clusters with Kubernetes Engine (OKE), you can use custom images and cloud-init scripts to create the following types of worker node to run Ubuntu:
- managed nodes
- self-managed nodes

Note that you cannot create virtual nodes to run Ubuntu using custom images and cloud-init scripts.

At a high level, the process for creating a worker node to run Ubuntu is:
- [Step 1: Create a custom image based on an existing compute instance running the required Ubuntu release](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcustomimage). Oracle provides node packages for different Ubuntu releases, and each node package is compatible with certain Kubernetes versions. For more information, see[Availability and Compatibility](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_availabilitycompatibility).
- [Step 2: Construct the URL from which to download an Ubuntu node package](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_constructubuntuurl). The URL from which to download the Ubuntu node package provided by Oracle depends on both the Ubuntu release and the Kubernetes version that you want to run on the worker node. There is a different download URL for each supported combination of Ubuntu release and Kubernetes version.
- [Step 3: Create a cloud-init script to install the Ubuntu node package and bootstrap the worker node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcloudinitscript). The cloud-init script to create depends on whether the worker node on which you want to run Ubuntu is a managed node, or a self-managed node.
- [Step 4: Add worker nodes running Ubuntu to a cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_addworkernodes). The way in which you add Ubuntu nodes to a cluster depends on whether you want to add the nodes as managed nodes or as self-managed nodes. For managed nodes, you define a managed node pool. For self-managed nodes, you add compute instances as worker nodes.

## Availability and Compatibility

This table lists the Ubuntu releases for which Oracle provides node packages, along with the Kubernetes versions that each node package is compatible with. The node packages that Oracle provides are designed to work on both x86 and ARM architectures.

Ubuntu release Package to use with Kubernetes 1.27 Package to use with Kubernetes 1.28 Package to use with Kubernetes 1.29 Package to use with Kubernetes 1.30 Package to use with Kubernetes 1.31 Package to use with Kubernetes 1.32 Package to use with Kubernetes 1.33 Package to use with Kubernetes 1.34 Package to use with Kubernetes 1.35 Package to use with Kubernetes 1.36
Jammy (Ubuntu 22.04)`oci-oke-node-all-1.27.10``oci-oke-node-all-1.28.10``oci-oke-node-all-1.29.1``oci-oke-node-all-1.30.10``oci-oke-node-all-1.31.10``oci-oke-node-all-1.32.10``oci-oke-node-all-1.33.10``oci-oke-node-all-1.34.10``oci-oke-node-all-1.35.2``oci-oke-node-all-1.36.1`
Noble (Ubuntu 24.04)`oci-oke-node-all-1.27.10``oci-oke-node-all-1.28.10``oci-oke-node-all-1.29.1``oci-oke-node-all-1.30.10``oci-oke-node-all-1.31.10``oci-oke-node-all-1.32.10``oci-oke-node-all-1.33.10``oci-oke-node-all-1.34.10``oci-oke-node-all-1.35.2``oci-oke-node-all-1.36.1`

## Step 1: Create a custom image based on an existing compute instance running the required Ubuntu release

In this step, you use the Compute service to create a custom image from a compute instance that is already running the Ubuntu release you want on worker nodes in the Kubernetes cluster.

Note that you create the image as a 'custom' image, even though you do not modify the image.
- Decide which Ubuntu release and which Kubernetes version you want on worker nodes.

Oracle provides node packages for different Ubuntu releases, and each node package is compatible with certain Kubernetes versions. For more information, see[Availability and Compatibility](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_availabilitycompatibility).
- 

Identify an existing compute instance that is running the Ubuntu release you require.

This is the compute instance that you will use as the basis of the custom image.

If a suitable compute instance does not already exist, follow the instructions in[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)in the Compute service documentation to create a suitable compute instance now.
- Follow the instructions in[Managing Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm#Using2)in the Compute service documentation, to create a custom image based on the existing compute instance that is running the Ubuntu release you require.
- Make a note of the OCID of the custom image you have created.

## Step 2: Construct the URL from which to download an Ubuntu node package

In this step, you construct the URL from which to download the Ubuntu node package provided by Oracle.

The download URL depends on the Ubuntu release and Kubernetes version you want on worker nodes. The download URL includes the Object Storage location, as well as details of the particular Ubuntu release and Kubernetes version.

Bear in mind that the versions of Kubernetes running on control plane nodes and on worker nodes (including self-managed nodes) must be compatible, as described in the[Kubernetes version skew support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/)in the Kubernetes documentation. It is your responsibility to construct the download URL for a node package that contains a compatible Kubernetes version. Kubernetes Engine does not check that the Kubernetes version in the node package you specify is compatible with the Kubernetes version running on the cluster's control plane nodes.

Construct the download URL as follows:
- Open a new text file in your preferred text editor.
- Create the download URL in one of the following ways:
- by using the following static URL:
```

```

- by including a PAR (Pre-Authenticated Request) token in the following URL:

```

```
where`<par-token>`is the current Object Storage PAR (Pre-Authenticated Request) token. PAR tokens are valid for 12 months. The current PAR token is:
```

```

Note  
  

The current PAR token expires on November 1st, 2026 and will not be replaced. Update any code that uses the PAR-based URL to use the static URL before November 1, 2026.

In both cases:
- 

`<ubuntu-release>`is one of the following, according to the release of Ubuntu that you want to run on the worker node:
- `ubuntu-jammy`(Ubuntu 22.04)
- `ubuntu-noble`(Ubuntu 24.04)
- `<kubernetes-version>`is one of the following, according to the minor version of Kubernetes that you want to run on the worker node:
- `kubernetes-1.27`
- `kubernetes-1.28`
- `kubernetes-1.29`
- `kubernetes-1.30`
- `kubernetes-1.31`
- `kubernetes-1.32`
- `kubernetes-1.33`
- `kubernetes-1.34`
- `kubernetes-1.35`
- `kubernetes-1.36`

For example, if you want to run Ubuntu 22.04 and Kubernetes version 1.29 on worker nodes, construct one of the following download URLs (using either a static URL or a PAR token) for the appropriate node package:
```

```

```

```

- (optional) Save the text file in a convenient location, as you need the download URL in the next step.

## Step 3: Create a cloud-init script to install the Ubuntu node package and bootstrap the worker node

In this step, you create a cloud-init script to download and install the Ubuntu node package provided by Oracle, and to bootstrap the worker node.

Note that there is different logic to add to the cloud-init script, depending on whether you want to run Ubuntu on managed nodes, or on self-managed nodes.

### Creating a cloud-init script for managed nodes

To create a cloud-init script to run Ubuntu on managed nodes:
- Create a new cloud-init script file from scratch with a filetype supported by cloud-init (such as .yaml), and add the following logic to the script file:
```

```

where:
- `<download-url>`is the URL from which to download the Ubuntu node package that you constructed in the previous step (see[Step 2: Construct the URL from which to download an Ubuntu node package](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_constructubuntuurl)). For example,`https://objectstorage.us-sanjose-1.oraclecloud.com/n/odx-oke/b/okn-repositories/o/prod/ubuntu-jammy/kubernetes-1.29 stable main`
- `<oci-package-name>`is one of the following, according to the minor version of Kubernetes that you want to run on the managed node:
- `oci-oke-node-all-1.27.10`
- `oci-oke-node-all-1.28.10`
- `oci-oke-node-all-1.29.1`
- `oci-oke-node-all-1.30.10`
- `oci-oke-node-all-1.31.10`
- `oci-oke-node-all-1.32.10`
- `oci-oke-node-all-1.33.10`
- `oci-oke-node-all-1.34.10`
- `oci-oke-node-all-1.35.2`
- `oci-oke-node-all-1.36.1`

The Kubernetes minor version must match the Kubernetes minor version you specified when constructing the download URL (see[Step 2: Construct the URL from which to download an Ubuntu node package](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_constructubuntuurl)).

For example, if you want to run Ubuntu 22.04 (jammy) and Kubernetes version 1.29.1 on managed nodes, add the following logic to the script file:
```

```

- Save the cloud-init script file.

### Creating a cloud-init script for self-managed nodes

To create a cloud-init script to run Ubuntu on self-managed nodes:
- Follow the instructions in[Creating Cloud-init Scripts for Self-managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm)to obtain the Kubernetes API private endpoint of the enhanced cluster to which you want to add the self-managed node, using the Console or the CLI.
- Follow the instructions in[Creating Cloud-init Scripts for Self-managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm)to obtain the cluster's base64-encoded CA certificate from the cluster's kubeconfig file, using the Console or the CLI.
- Create a new cloud-init script file from scratch with a filetype supported by cloud-init (such as .yaml), and add the following logic to the script file:
```

```

where:
- `<download-url>`is the URL from which to download the Ubuntu node package that you constructed in the previous step (see[Step 2: Construct the URL from which to download an Ubuntu node package](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_constructubuntuurl)). For example,`https://objectstorage.us-sanjose-1.oraclecloud.com/n/odx-oke/b/okn-repositories/o/prod/ubuntu-jammy/kubernetes-1.29 stable main`
- 

`<oci-package-name>`is one of the following, according to the minor version of Kubernetes that you want to run on the self-managed node:
- `oci-oke-node-all-1.27.10`
- `oci-oke-node-all-1.28.10`
- `oci-oke-node-all-1.29.1`
- `oci-oke-node-all-1.30.10`
- `oci-oke-node-all-1.31.10`
- `oci-oke-node-all-1.32.10`
- `oci-oke-node-all-1.33.10`
- `oci-oke-node-all-1.34.10`
- `oci-oke-node-all-1.35.2`
- `oci-oke-node-all-1.36.1`

The Kubernetes minor version must match the Kubernetes minor version you specified when constructing the download URL (see[Step 2: Construct the URL from which to download an Ubuntu node package](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_constructubuntuurl)).
- `<cluster-endpoint>`is the IP address of the cluster's Kubernetes API endpoint that you obtained earlier.
- `<base64-encoded-certificate>`is the cluster's base64-encoded CA certificate that you obtained earlier (starting with the characters`LS0t`).

For example, if you want to run Ubuntu 22.04 (Jammy) and Kubernetes version 1.29.1 on a self-managed node, add the following logic to the script file:
```

```

- Save the cloud-init script file.

## Step 4: Add worker nodes running Ubuntu to a cluster

In this step, you use the cloud-init script you created earlier to add worker nodes running Ubuntu to a Kubernetes cluster.

Note that there are different instructions to follow, depending on whether you want to run Ubuntu on managed nodes, or on self-managed nodes. For managed nodes, you define a managed node pool. For self-managed nodes, you add compute instances as worker nodes.

Note that you have to use the CLI to create managed nodes based on custom images.

### Adding Ubuntu worker nodes as managed nodes

To add managed nodes running Ubuntu in an existing cluster
- Open a command prompt and use the[oci ce node-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/create.html)command to create a new node pool.
- As well as the mandatory parameters required by the command:
- Include the`--node-image-id`parameter, and specify the OCID of the custom image that you created in[Step 1: Create a custom image based on an existing compute instance running the required Ubuntu release](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcustomimage).
- Include the`--node-metadata`parameter and specify the cloud-init script that you created for managed nodes in[Step 3: Create a cloud-init script to install the Ubuntu node package and bootstrap the worker node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcloudinitscript), in the appropriate format for your environment:
- Linux:`--node-metadata '{"user_data": "'$(cat <cloud-init-file> | base64 -w 0)'"}'`
- Mac:`--node-metadata '{"user_data": "'$(cat <cloud-init-file> | base64- b 0)'"}'`
where:
- `<cloud-init-file>`is the name of the cloud-init file that you created
- `base64`specifies the file is to be base64-encoded

For example, you might enter the following command on a Mac work station:
```

```

Note that the Kubernetes version you specify using the`--kubernetes-version`parameter must correspond to the Kubernetes version you specified in the cloud-init script (see[Step 3: Create a cloud-init script to install the Ubuntu node package and bootstrap the worker node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcloudinitscript)).

### Adding Ubuntu worker nodes as self-managed nodes

Before you create a self-managed node, confirm that:
- The cluster to which you want to add the self-managed node is configured appropriately for self-managed nodes. See[Cluster Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-clusterreqs).
- A dynamic group and an IAM policy already exist to allow the compute instance hosting the self-managed node to join an enhanced cluster created with Kubernetes Engine. See[Creating a Dynamic Group and a Policy for Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm).

Using the Console
- Create a new compute instance to host the self-managed node:
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Follow the instructions in the[Compute service documentation](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)to create a new compute instance. Note that appropriate policies must exist to allow the new compute instance to join the enhanced cluster. See[Creating a Dynamic Group and a Policy for Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm).
- In the Image and Shape section, select Change image .
- Select My images , select the Image OCID option, and then enter the OCID of the custom image that you created in[Step 1: Create a custom image based on an existing compute instance running the required Ubuntu release](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcustomimage).
- Select Advanced options , and in the Management section, select the Paste cloud-init script option.
- Copy and paste the cloud-init script you created for self-managed nodes in[Step 3: Create a cloud-init script to install the Ubuntu node package and bootstrap the worker node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcloudinitscript), into the Cloud-init script field.
- Select Create to create the compute instance to host the self-managed node.

When the compute instance is created, it is added as a self-managed node to the cluster with the Kubernetes API endpoint that you specified in the cloud-init script.
- (Optional) Verify that the self-managed node has been added to the Kubernetes cluster, and that labels have been added to the node and set as expected, by following the instructions in[Creating Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingselfmanagednodes.htm).

Using the CLI
- Open a command prompt and enter the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html)oci Compute instance launch`command and required parameters to create a self-managed node.
- As well as the mandatory parameters required by the command:
- Include the`--image-id`parameter, and specify the OCID of the custom image that you created in[Step 1: Create a custom image based on an existing compute instance running the required Ubuntu release](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcustomimage).
- Include the`--user-data-file`parameter and specify the cloud-init script that you created for self-managed nodes in[Step 3: Create a cloud-init script to install the Ubuntu node package and bootstrap the worker node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcloudinitscript).

For example, you might enter the following command:
```

```
