# Using NVIDIA GPU Cloud with Oracle Cloud Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/References/ngcimage.htm
- Fetched: 2026-09-05 01:49 CDT

# Using NVIDIA GPU Cloud with Oracle Cloud Infrastructure

NVIDIA GPU Cloud (NGC) is a GPU-accelerated cloud platform optimized for deep learning and scientific computing. This topic provides an overview of how to use NGC with Oracle Cloud Infrastructure.

NVIDIA makes available on Oracle Cloud Infrastructure a customized Compute image that is optimized for the NVIDIA Tesla Volta and Pascal GPUs. Running NGC containers on this instance provides optimum performance for deep learning jobs.

## Before You Begin

Prepare the following things:
- 

An Oracle Cloud Infrastructure tenancy with a GPU quota. For more information about quotas, see[Compute Quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas_topic-Compute_Quotas.htm).
- 

A cloud network to launch the instance in. For information about setting up cloud networks, see[Managing VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)in[VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNs.htm).
- 

A key pair, to use for connecting to the instance via SSH. For information about generating a key pair, see[Managing Key Pairs on Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/managingkeypairs.htm).
- 

Security group and policy configured for the File Storage service. For more information, see[Managing Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm),[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm), and[Details for the File Storage Service](https://docs.oracle.com/iaas/Content/Identity/Reference/filestoragepolicyreference.htm#Details_for_the_File_Storage_Service).
- 

An NGC API key for authenticating with the NGC service.

[To generate your NGC API key](https://docs.oracle.com/en-us/iaas/Content/Compute/References/ngcimage.htm#)

- 

Sign in to the[NGC website](https://ngc.nvidia.com/).
- 

On the[NGC Registry page](https://ngc.nvidia.com/registry/), click Get API Key .
- 

Click Generate API Key and then click Confirm to generate the key. If you have an existing API key it will become invalid once you generate a new key.

## Launching an Instance Based on the NGC Image

### Using the Console
- Open the Console. For steps, see[Signing In for the First Time](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm).
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select a Compartment that you have permission to work in.
- Click Create instance .
- 

Enter a name for the instance. Avoid entering confidential information.
- In the Placement section, select the Availability Domain that you want to create the instance in.
- In the Image and shape section:
- On the Shape card, click Change shape . Then, do the following:
- 

For Instance type , select Virtual machine or Bare metal machine .
- 

Select a GPU shape for the instance. For more information about GPU shapes, see[virtual machine GPU shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#vm-gpu)and[bare metal GPU shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#bm-gpu).
Important  
  
In order to access the GPU shapes, your tenancy must have a GPU quota. If your tenancy does not have a GPU quota, the GPU shapes will not be in the shape list. See[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Compute/References/ngcimage.htm#prereq)for more information.
- Click Select shape .
- 
To select the NGC image, on the Image card, click Change image . Then do the following.
Important  
  
In order to access the NVIDIA GPU Cloud images, your tenancy must have a GPU quota and you must select a GPU shape.
- In the Image source list, select Oracle images .
- Select the check box next to NVIDIA GPU Cloud Machine Image .
- Review and accept the terms of use, and then click Select image .
- 

In the Networking section, leave Select existing virtual cloud network selected, and then select the virtual cloud network (VCN) compartment, VCN, subnet compartment, and subnet.
- 

In the Add SSH keys section, upload the public key portion of the key pair that you want to use for SSH access to the instance. Browse to the key file that you want to upload, or drag and drop the file into the box.
- 

Click Create .

You should now see the NGC instance with the state of Provisioning . After the state changes to Running , you can connect to the instance. For general information about launching compute instances, see[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/launchinginstance.htm).

See the following topics for steps to access and work with the instance:
- [Connecting to an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/accessinginstance.htm)
- [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/restartinginstance.htm)
- [Terminating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/../Tasks/terminatinginstance.htm)

When you connect to the instance using SSH, you are prompted for the NGC API key. If you supply the API key at the prompt, the instance automatically logs you in to the NGC container registry so that you can run containers from the registry. You can choose not to supply the API key at the prompt and still log in to the instance. You can then log in later to the NGC container registry. See[Logging in to the NGC Container Registry](https://docs.oracle.com/en-us/iaas/Content/Compute/References/ngcimage.htm#logon)for more information.

### Using the CLI

Oracle Cloud Infrastructure provides a[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm)you can use to complete tasks. For more information, see[Quickstart](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm)and[Configuring the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliconfigure.htm).

Use the[launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html)command to create an instance, specifying image for sourceType and the image OCID`ocid1.image.oc1..aaaaaaaaknl6phck7e3iuii4r4axpwhenw5qtnnsk3tqppajdjzb5nhoma3q`in InstanceSourceDetails for LaunchInstanceDetails .

## Using the File Storage Service for Persistent Data Storage

You can use the File Storage service for data storage when working with NGC. For more information, see[Overview of File Storage](https://docs.oracle.com/iaas/Content/File/Concepts/filestorageoverview.htm). See the following tasks for creating and working with the File Storage service:
- [Creating File Systems](https://docs.oracle.com/iaas/Content/File/Tasks/creatingfilesystems.htm)
- [Mounting File Systems](https://docs.oracle.com/iaas/Content/File/Tasks/mountingfilesystems.htm)
- [Managing File Systems](https://docs.oracle.com/iaas/Content/File/Tasks/managingfilesystems.htm)

## Using the Block Volume Service for Persistent Data Storage

You can use the Block Volume service for data storage when working with NGC. For more information, see[Overview of Block Volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm). See the following tasks for creating and working with the Block Volume service:
- [Creating a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/creatingavolume.htm)
- [Attaching a Block Volume to an Instance](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm)
- [Connecting to a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/connectingtoavolume.htm)

You can also use the CLI to manage block volumes, see the[volume](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume.html)commands.

## Using the Object Storage Service for Persistent Data Storage

You can use the Object Storage service for data storage when working with NGC. For more information, see[Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm). See the following tasks for creating and working with the Object Storage service:
- [Creating an Object Storage Bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm)
- [Ways to Access Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm#accessways)
- [Object Storage Objects](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects.htm)
- [Uploading an Object Storage Object to a Bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects_topic-To_upload_objects_to_a_bucket.htm)

You can also use the CLI to manage object storage, see the[os](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os.html)command.

## Examples of Running Containers

You first need to log into the NGC container registry. You can skip this section if you provided your API key when logging into the instance via SSH. If you did not provide your API key when connecting to your instance, then you must perform this step.

[To log into the NGC container registry](https://docs.oracle.com/en-us/iaas/Content/Compute/References/ngcimage.htm#)

- 

Run the following Docker command:

```

```

- 

When prompted for a username, enter`$oauthtoken`.
- 

When prompted for a password enter your NGC API key.

At this point you can run Docker commands and access the NGC container registry from the instance.

[Example: MNIST Training Run Using PyTorch Container](https://docs.oracle.com/en-us/iaas/Content/Compute/References/ngcimage.htm#)

This sample demonstrates running the MNIST example under PyTorch. This example downloads the MNIST dataset from the web.
- 

Pull and run the PyTorch container with the following Docker commands:

```

```

- 

Run the MNIST example with the following commands:

```

```

[Example: MNIST Training Run Using TensorFlow Container](https://docs.oracle.com/en-us/iaas/Content/Compute/References/ngcimage.htm#)

This sample demonstrates running the MNIST example under TensorFlow. This example downloads the MNIST dataset from the web.
- 

Pull and run the TensorFlow container with the following Docker commands:

```

```

- 

Run the MNIST_with_summaries example with the following commands:

```

```
