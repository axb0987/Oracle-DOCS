# Changing the Shape of an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm
- Fetched: 2026-09-05 01:52 CDT

# Changing the Shape of an Instance

You can change the[shape](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm)of a virtual machine (VM) instance without having to rebuild the instance or redeploy your applications. Changing shapes lets you scale up your Compute resources for increased performance or scale down to reduce costs.

Changing the shape of an instance affects the number of OCPUs , amount of memory, network bandwidth, and maximum number of VNICs for the instance. In addition, you can select a shape that uses a different processor. The instance's public and private IP addresses, volume attachments, and VNIC attachments remain the same.

Optionally, you can change a regular instance to a burstable instance, or change a burstable instance to a regular instance. Similarly, you can change a regular instance to an extended memory VM instance, or change an extended memory VM instance to a regular instance.

To determine whether capacity is available for a specific shape before you change the shape of an instance, use the[CreateComputeCapacityReport](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport)operation.

## Supported Shapes

The instance's current shape and image determine available new shape targets. You can resize instances that use these shapes:
- 

VM Standard and Optimized shapes: Includes the following shapes:
- VM.Standard1 series
- VM.Standard.B1 series
- VM.Standard2 series
- VM.Standard3.Flex
- VM.Standard4.Ax.Flex
- VM.Standard.E2 series
- VM.Standard.E3.Flex
- VM.Standard.E4.Flex
- VM.Standard.E5.Flex
- VM.Standard.E6.Flex
- VM.Standard.E6.Ax.Flex
- VM.Optimized3.Flex
- VM.Standard.A1.Flex
- VM.Standard.A2.Flex
- VM.Standard.A4.Flex
- VM.Standard.A4.Ax.Flex

For both Linux and Windows images, you can change the number of OCPUs and the amount of memory allocated to a[flexible shape](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm#flexible). You can also change a standard shape in one series to a standard shape in another series. For example, you can change a fixed shape to a flexible shape.
Important  
  
For Windows Server 2019 instances running on shapes in the VM.Standard2 series, you can change the shape to a new shape only within the same series.
- VM.GPU3 series: You can change to any shape in the VM.GPU3 or VM.GPU.A10 series.
- VM.GPU.A10 series: You can change to any shape in the VM.GPU.A10 or VM.GPU3 series.

These shapes cannot be edited:
- VM.Standard.E2.1.Micro
- VM.DenseIO.E4.Flex
- VM.DenseIO.E5.Flex
- VM.DenseIO.E6.Ax.Flex
- VM.GPU2 series

## Limitations and Considerations

Be aware of the following information:
- The image that was used to create the instance must be compatible with the new shape. To see which shapes are compatible, do either of the following things:
- In the Console, on the Instance Details page, click the name of the image. Then, refer to the list of compatible shapes.
- Using the API, call the[ListShapes](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Shape/ListShapes)operation and pass the image OCID as a parameter.
- Some Marketplace images cannot be resized because of licensing constraints. If you want to resize a Microsoft SQL Server image,[contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
- You must have sufficient[service limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for the new shape. If you don't have service limits, the instance retains the original shape.
- Different shapes are billed at different rates. When you change the shape of an instance, you are billed to the nearest second of usage for each shape that you use. For more information, see[Compute Pricing](https://www.oracle.com/cloud/compute/pricing.html)and[Resource Billing for Stopped Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resource-billing-stopped-instances.htm).
- If the instance has secondary VNICs configured, you might need to reconfigure them after the instance is rebooted. For more information, see[VNICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).
- If the instance is running when you change the shape, it is rebooted as part of the change shape operation. If the applications that run on the instance take a long time to shut down, they could be improperly stopped, resulting in data corruption. To avoid this,[shut down the instance using the commands available in the OS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-stop-instance.htm#operatingsystem)before you change the shape.
- When you resize your VM, some hardware details might change. If the network interface name changes, it can cause issues for some guest OSs. The guest OS is more vulnerable if the OS has been customized. To ensure that you have consistent interface names, configure your guest OS. If the OS fails to boot after you change the shape, change the instance back to the original shape.
- If you created a regular instance using SR-IOV networking (the default for some regular instances), and want to change the instance to a[burstable instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/burstable-instances.htm), you must also[change the networking type](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-launch-options.htm)to paravirtualized.

## Before You Begin

- If you want to change the instance to a smaller shape that supports fewer VNICs,[detach the extra VNICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm#)
- 

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).
- Select an instance.
- Select the option you see:
- Select Actions then More actions then Edit .
- Select More actions then Edit .
- Select the option you see:
- Scroll down to the Shape Summary section.
- Select Edit shape .
Note  
  
The instance's current shape and image decide which shapes you can select as a target for the shape.

In the Shape series section, select a processor group. The following options are available:

- AMD: (Flexible) Standard shapes that use current-generation AMD processors. AMD shapes are flexible shapes.
- Intel: (Flexible) Standard and optimized shapes that use current-generation Intel processors. Intel shapes are flexible shapes.
- Ampere: (Flexible) The OCI Ampere A1 Compute and OCI Ampere A2 Compute shapes use Arm-based processors. The Arm-based shapes are flexible shapes. The`VM.Standard.A1.Flex`shape is an[Always Free](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm)shape. These shapes are not supported for Windows.
- Specialty and previous generation: Standard shapes with previous generation Intel and AMD processors, the[Always Free](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm)`VM.Standard.E2.1.Micro`shape, Dense I/O shapes, GPU shapes, and HPC shapes.

Edit the shape options which vary depending upon the shape:
- Number of OCPUs: Select the number of OCPUs that you want to allocate.
- Amount of memory (GB): Select the amount of memory that you want to allocate to this instance. The amount of memory allowed is based on the number of OCPUs selected.
- 

Select Save changes .

If the instance is running, it's rebooted. Confirm when prompted.
- 

Use the[instance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html)command and required parameters to update an instance:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute Service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).

- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to change the shape of an instance:
- [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)
