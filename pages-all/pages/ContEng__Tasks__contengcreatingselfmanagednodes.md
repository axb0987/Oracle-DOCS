# Creating Self-Managed Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingselfmanagednodes.htm
- Fetched: 2026-09-05 01:54 CDT

# Creating Self-Managed Nodes

Find out how to create a new self-managed node and add it to an existing cluster.

You use the Compute service to create the compute instance on which to run a self-managed node. Having created the self-managed node, you then add it to an existing enhanced cluster.

If you want a self-managed node to use the flannel CNI plugin for pod networking, you can create the self-managed node using the Console, the CLI, and the API. If you want a self-managed node to use the OCI VCN-Native Pod Networking CNI plugin for pod networking, you can create the self-managed node using the CLI, and the API.
Note  
  
For information about creating self-managed nodes that run Ubuntu, see[Running Ubuntu on Worker Nodes Using Custom Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingselfmanagednodes.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingselfmanagednodes.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingselfmanagednodes.htm#)
- 

To create a self-managed node using the Console:
- Create the cloud-init script containing the Kubernetes API private endpoint and base64-encoded CA certificate of the enhanced cluster to which you want to add the self- managed node. See[Creating Cloud-init Scripts for Self-managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm).
- Create a new compute instance to host the self-managed node:
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Follow the instructions in the[Compute service documentation](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)to create a new compute instance. Note that appropriate policies must exist to allow the new compute instance to join the enhanced cluster. See[Creating a Dynamic Group and a Policy for Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm).
- In the Image and Shape section, select Change image .
- Select My images , select the Image OCID option, and then enter the OCID of the OKE Oracle Linux 7 (OL7) or Oracle Linux 8 (OL8) image you want to use. See[Image Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-imagereqs).
- Select Advanced options , and in the Management section, select the Paste cloud-init script option.
- Copy and paste the cloud-init script containing the Kubernetes API private endpoint and base64-encoded CA certificate into the Cloud-init script field. See[Creating Cloud-init Scripts for Self-managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm).
- Click Next , and follow the remaining instructions in the[Compute service documentation](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)to create the compute instance to host the self-managed node.

When the compute instance is created, it is added as a self-managed node to the cluster with the Kubernetes API endpoint that you specified .
- Verify that the self-managed node has been added to the Kubernetes cluster and confirm the node's readiness status by entering:

```

```

For example:
```

```

- Confirm that labels have been added to the node and set as expected by entering:

```

```

For example
```

```

- 

Use the[oci Compute instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html)command and required parameters to create a self-managed node:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).

Tips:
- Specify the name of the file containing the cloud-init script (required to add the compute instance to the cluster as a self-managed node) using the[oci Compute instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html)command's`--user-data-file`parameter. See[Creating Cloud-init Scripts for Self-managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm).
- Specify the image to use to create the self-managed node by setting the[oci Compute instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html)command's`--image-id`parameter. See[Image Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-imagereqs).
- If you want the self-managed node to use the OCI VCN-Native Pod Networking CNI plugin for pod networking, add the`--metadata`parameter to the`oci compute instance launch`command, as follows:

```

```

where:
- `"oke-native-pod-networking": "true"`specifies that you want the self-managed node to use the OCI VCN-Native Pod Networking CNI plugin for pod networking.
- `"oke-max-pods": "<max-pods-per-node>"`specifies the maximum number of pods that you want to run on the self-managed node.
- `"pod-subnets": "<pod-subnet-ocid>"`specifies the OCID of the pod subnet that supports communication between pods and direct access to individual pods using private pod IP addresses. The pod subnet must be a private subnet.
- `"pod-nsgids": "<nsg-ocid>"`optionally specifies the OCID of one or more network security groups (NSGs) containing security rules to route network traffic to pods. When specifying multiple NSGs, use a comma-delimited list in the format`"pod-nsgids": "<nsg-ocid-1>,<nsg-ocid-2>"`

For more information about the OCI VCN-Native Pod Networking CNI plugin, see[Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm).
- If you want the self-managed node to be a dual stack IPv4/IPv6 node (with both IPv4 and IPv6 addresses), add the`--metadata`parameter to the`oci compute instance launch`command, as follows:

```

```

Examples:

Example 1: Command to create a self-managed node that uses the flannel CNI plugin for pod networking.

```

```

Example 2: Command to create a self-managed node that uses the OCI VCN-Native Pod Networking CNI plugin for pod networking.

```

```

Example 3: Alternative command to create a self-managed node that uses the OCI VCN-Native Pod Networking CNI plugin for pod networking.

```

```

- 

Run the[LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance)operation to create a self-managed node.

If you want the self-managed node to use the OCI VCN-Native Pod Networking CNI plugin for pod networking, use the metadata attribute to specify values for the following keys:
- oke-native-pod-networking: Set to true to specify that you want the self-managed node to use the OCI VCN-Native Pod Networking CNI plugin for pod networking.
- oke-max-pods : The maximum number of pods that you want to run on the self-managed node.
- pod-subnets : The OCID of the pod subnet that supports communication between pods and direct access to individual pods using private pod IP addresses. The pod subnet must be a private subnet.
- pod-nsgids: (optional) The OCID of one or more network security groups (NSGs) containing security rules to route network traffic to pods. When specifying multiple NSGs, use a comma-delimited list in the format`"pod-nsgids": "<nsg-ocid-1>,<nsg-ocid-2>"`

For more information about the OCI VCN-Native Pod Networking CNI plugin, see[Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm)
