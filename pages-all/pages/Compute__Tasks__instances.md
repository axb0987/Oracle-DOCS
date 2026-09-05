# Working with Instances
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm
- Fetched: 2026-09-05 01:51 CDT

# Working with Instances

Oracle Cloud Infrastructure Compute lets you provision and manage compute hosts, known as instances. You can create instances as needed to meet your compute and application requirements. After you create an instance, you can access it securely from your computer, restart it, attach and detach volumes, and terminate it when you're done with it.
- [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm): Follow the steps in this topic to create a bare metal or virtual machine (VM) compute instance.
- Instances launched using Oracle Linux, CentOS, or Ubuntu images use an SSH key pair instead of a password to authenticate a remote user. Therefore, to connect to an instance, you might need to[create an SSH key pair](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm).
- You can create[burstable instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/burstable-instances.htm),[shielded instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/shielded-instances.htm), and[confidential instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/confidential_compute.htm).
- You can configure your instances to use different[capacity types](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/computeoverview.htm#capacity_types).
- You can add extended memory and cores to instances with[extended memory VM instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/extended-memory-vm-instances.htm).
- [Connecting to an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm): You can connect to a running instance by using a Secure Shell (SSH) or Remote Desktop connection.
- [Editing an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-instance.htm): You can edit the properties of a compute instance without having to rebuild the instance or redeploy your applications.
- [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm): You can stop and start an instance as needed to update software or resolve error conditions.
- [Replacing a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/replacingbootvolume.htm): You can automatically replace the boot volume of an instance without terminating and recreating the instance.
- [Setting Up Contextual Notifications for an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/contextual-notifications-compute.htm): You can get messages when something happens with a compute instance.
- [Adding Users to an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/addingusers.htm): You can add users to a compute instance.
- [Running Commands on an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/runningcommands.htm): You can remotely configure, manage, and troubleshoot compute instances by running scripts within the instance using the run command feature.
- [Disabling Simultaneous Multithreading](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/disablesmt.htm): You can disable simultaneous multithreading (SMT) on your instances through the console or by using CLI commands.
- [Getting Instance Metadata](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm): The instance metadata service (IMDS) provides information about a running instance, including details about the instance, its attached virtual network interface cards (VNICs), its attached multipath-enabled volume attachments, and any custom metadata that you define. IMDS also provides information to cloud-init that you can use for various system initialization tasks.
- [Updating Instance Metadata](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancemetada.htm): You can add and update custom metadata for a compute instance using the CLI or REST APIs.
- [Moving a Compute Instance to a New Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm): You can relocate instances using[reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#reboot)or a[manual process](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#manual).
- [Terminating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm): You can permanently delete (terminate) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates.

## Security Zones

[Security Zones](https://docs.oracle.com/iaas/Content/security-zone/home.htm)ensure that cloud resources comply with Oracle security principles. If any operation on a resource in a security zone compartment violates a[policy for that security zone](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm), then the operation is denied.

The following security zone policies affect the ability to create instances:
- The boot volume for a compute instance in a security zone must also be in the same security zone.
- A Compute instance that isn't in a security zone can't use a boot volume that is in a security zone.
- A Compute instance in a security zone must use subnets that are also in the same security zone.
- All Compute instances in a security zone must be created using[platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/images.htm). You can't create a compute instance from a custom image in a security zone.
Important  
  
Failing to implement one of the listed security zone policies might prevent the creation of an instance.

## Required IAM Policy for Working with Instances

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.
Tip  
  
When you create an instance, several other resources are involved, such as an image, a cloud network, and a subnet. Those other resources can be in the same compartment with the instance or in other compartments. You must have the required level of access to each of the compartments involved in order to launch the instance. This is also true when you attach a volume to an instance; they don't have to be in the same compartment, but if they're not, you need the required level of access to each of the compartments.

For administrators: The simplest policy to let users[create](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm),[edit](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-instance.htm), and[terminate (delete)](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm)instances is listed in[Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances). It gives the specified group general access to manage instances and images, along with the required level of access to attach existing block volumes to the instances. If the specified group doesn't need to launch instances or attach volumes, you could simplify that policy to include only`manage instance-family`, and remove the statements involving`volume-family`and`virtual-network-family`.

If the group needs to create block volumes, they'll need the ability to manage block volumes. See[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups).

If the group needs access to community images specifically, they'll need the ability to read community images. See[Publishing Community Applications](https://docs.oracle.com/iaas/Content/Marketplace/Tasks/publishingcommunityapplications.htm).

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for Core Services](https://docs.oracle.com/iaas/Content/Identity/Reference/corepolicyreference.htm).

Some Compute tasks require additional policies, as described in the following sections.

### Partner Image Catalog

If the group needs to create instances based on partner images, they'll need the manage permission for app-catalog-listing to create subscriptions to images from the Partner Image catalog. See[Let users list and subscribe to images from the Partner Image catalog](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#subscribe-catalog).

### SSH and Remote Desktop Access

For users: To[connect to a running instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm)with a Secure Shell (SSH) or Remote Desktop connection, you don't need an IAM policy to grant you access. However, you do need the public IP address of the instance.

For administrators: If there's a policy that lets users launch an instance, that policy probably also lets users get the instance's IP address. The simplest policy that does both is listed in[Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances).

Here's a more restrictive policy that lets the specified group get the IP address of existing instances and use power actions on the instances (for example, stop or start the instance), but not launch or terminate instances. The policy assumes the instances and the cloud network are together in a single compartment (XYZ).

```

```

### Instance Metadata Service (IMDS)

For users: No IAM policy is required if you're logged in to the instance and using cURL to[get the instance metadata](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm).

For administrators: Users can also get instance metadata through the Compute API (for example, with[GetInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/GetInstance)). The policy in[Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances)covers that ability.

To require that[legacy IMDSv1 endpoints are disabled](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm#upgrading-v2)on any new instances that are created, use the following policy:

```

```

### Capacity Reservations

For administrators: The following examples show typical policies that give access to[capacity reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm). Create the policy in the tenancy so that the access is easily granted to all compartments by way of[policy inheritance](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the capacity reservations in a particular compartment, specify that compartment instead of the tenancy.

Type of access: Ability to launch an instance in a reservation.

```

```

Type of access: Ability to manage capacity reservations.

```

```

### Run Command

For administrators: To write policy for the[run command feature](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/runningcommands.htm), do the following:
- 

[Create a group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm)that includes the users who you want to allow to issue commands, cancel commands, and view the command output for the instances in a compartment. Then, write the following policy to grant access for the group:

```

```

- 

[Create a dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)that includes the instances that you want to allow commands to run on. For example, a rule inside the dynamic group can state:

```

```

- 
Write the following policy to grant access for the dynamic group:
Note  
  
If you create an instance and then add it to a dynamic group, it takes up to 30 minutes for the instance to start to poll for commands. If you create the dynamic group first and then create the instance, the instance starts to poll for commands as soon as the instance is created.

```

```

- 

To allow the dynamic group to access the script file from an Object Storage bucket and save the response to an Object Storage bucket, write the following policies:

```

```

## Recommended Networking Launch Types for Compute Instances

When you create a VM instance, by default, Oracle Cloud Infrastructure chooses a recommended networking type for the VNIC based on the instance shape and OS image. The networking interface handles functions such as disk input/output and network communication.

The following networking types are available:
- Paravirtualized networking : For general-purpose workloads such as enterprise applications, microservices, and small databases. Paravirtualized networking also provides increased flexibility to use the same image across different hardware platforms. Linux images with paravirtualized networking support live migration during infrastructure maintenance.
- Hardware-assisted (SR-IOV) networking : Single root input/output virtualization. For low-latency workloads such as video streaming, real-time applications, and large or clustered databases. Hardware-assisted (SR-IOV) networking uses the VFIO driver framework.
- AcceleratedPV : For instances launched on supported Acceleron SmartNIC shapes. AcceleratedPV uses the SmartNIC-native data plane to offload network processing from the host CPU, reducing network hops and CPU overhead while improving throughput, latency, and bandwidth consistency. AcceleratedPV is supported with compatible images and is available only on supported shapes.
Important  
  
To use a particular networking type, both the shape and the image must support that networking type.

Shapes: The following table lists the default and supported networking types for[VM shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm#vmshapes).

Shape Default Networking Type Supported Networking Types
VM.Standard3.Flex Paravirtualized Paravirtualized, SR-IOV
VM.Standard4.Ax.Flex AcceleratedPV AcceleratedPV
VM.Standard.E4.Flex

Paravirtualized Paravirtualized, SR-IOV
VM.Standard.E5.Flex

Paravirtualized Paravirtualized, SR-IOV
VM.Standard.E6.Flex

Paravirtualized Paravirtualized, SR-IOV
VM.Standard.E6.Ax.Flex AcceleratedPV AcceleratedPV
VM.Standard.A1.Flex[1 Paravirtualized Paravirtualized, SR-IOV
VM.Standard.A2.Flex Paravirtualized Paravirtualized, SR-IOV
VM.Standard.A4.Flex Paravirtualized Paravirtualized, SR-IOV
VM.Standard.A4.Ax.Flex AcceleratedPV AcceleratedPV
VM.DenseIO1 series SR-IOV Paravirtualized, SR-IOV
VM.DenseIO2 series Paravirtualized Paravirtualized, SR-IOV
VM.DenseIO.E4.Flex Paravirtualized Paravirtualized, SR-IOV
VM.DenseIO.E5.Flex Paravirtualized Paravirtualized, SR-IOV
VM.DenseIO.E6.Ax.Flex AcceleratedPV AcceleratedPV
VM.GPU2 series SR-IOV Paravirtualized, SR-IOV
VM.GPU3 series SR-IOV Paravirtualized, SR-IOV
VM.GPU.A10 series SR-IOV Paravirtualized, SR-IOV
VM.Optimized3.Flex

Paravirtualized Paravirtualized, SR-IOV

Paravirtualized Supported Images:

Paravirtualized networking is supported on these[platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/images.htm):
- Oracle Linux 10, Oracle Linux 9, Oracle Linux 8, Oracle Autonomous Linux 8.x, Oracle Autonomous Linux 7.x, Oracle Linux Cloud Developer 8: All images.
- Oracle Linux 7: Images published in March 2019 or later.
- CentOS Stream 8, CentOS 7: Images published in July 2019 or later.
- Ubuntu 24.04, Ubuntu 22.04, Ubuntu 20.04: All images.
- Ubuntu 18.04: Images published in March 2019 or later.
- Windows Server 2025, Windows Server 2022, Windows Server 2019: All images.
- Windows Server 2016, Windows Server 2012 R2: Images published in August 2019 or later.

SR-IOV Supported Images:

SR-IOV networking is supported on all[platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/images.htm), with the following exceptions:
- Images for Arm-based shapes do not support SR-IOV networking.
- On Windows Server 2019, Windows Server 2022, and Windows Server 2025 when launched using a shape in the VM.Standard2 series, SR-IOV networking is not supported.
- On Windows Server 2012 R2, SR-IOV networking is supported on platform images released in April 2021 or later.
- The Server Core installation option for Windows Server does not support SR-IOV networking.

AcceleratedPV Supported Images:

AcceleratedPV networking is supported on these[platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/images.htm):
- Oracle Linux 10, Oracle Linux 9, Oracle Linux 8: All images.

## Troubleshooting Creation Errors by Using Work Requests

Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.

If an operation such as the create instance operation fails, or if the instance state moves directly from provisioning to terminating, use[work requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr)to determine where in the workflow the error occurred. Errors can occur because of problems with the configuration or problems with the user data. Synchronous errors occur during the initial call to the Compute API to create the instance. Asynchronous errors occur during the create instance workflow that occurs after the initial API call. Work requests capture asynchronous validation failures. A successful create instance API call that returns an HTTP 200 response might be followed by an asynchronous error during the subsequent create instance workflow.

The response to the REST API call contains the OCID of the work request in the`opc-work-request-id`header. You can monitor the status of the work request at any time by calling`GetWorkRequest`in the[Work Requests API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/)and passing in the work request ID found in the`opc-work-request-id`header. If an error occurs during the workflow, you can call`ListWorkRequestErrors`in the Work Requests API and pass in the work request ID to retrieve a list of errors.

For information about using work requests to troubleshoot errors, see[Work Requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm). For detailed information about asynchronous work requests, including how to filter the request response and a sample request and response, see[Asynchronous Work Requests](https://docs.oracle.com/iaas/Content/API/Concepts/workrequests.htm).

## Managing Tags for an Instance

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

To manage tags for an instance:
- Open the navigation menu and select Compute . Under Compute , select Instances .
- 

Select the instance that you're interested in.
- 

Select the Tags tab to view or edit the existing tags. Or click More Actions , and then click Add tags to add new ones.
[1 See[Limit on size of VM.Standard.A1.Flex shape using the SR-IOV network type](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../known-issues.htm#a1-VFIO-networking)
