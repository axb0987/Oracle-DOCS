# Create a Kubernetes Cluster
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm
- Fetched: 2026-09-05 19:21 CDT

# Create a Kubernetes Cluster

Use Terraform to set up a Kubernetes cluster in your Oracle Cloud Infrastructure account.

Key tasks include how to:
- Copy your existing scripts from Terraform tutorials.
- Edit existing scripts for reuse.
- Write new scripts for a Kubernetes cluster.

For more information, see:
- [Overview of Kubernetes Engine (OKE)](https://docs.oracle.com/iaas/Content/ContEng/Concepts/contengoverview.htm)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [What is Terraform?](https://developer.hashicorp.com/terraform/intro)
- [Terraform Registry](https://registry.terraform.io/browse/providers)

## Before You Begin

To successfully perform this tutorial, you must have the following:

[Requirements](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

- A paid Oracle Cloud Infrastructure account. See[Request and Manage Free Oracle Cloud Promotions](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm).
- A MacOS, Linux, or Windows computer.
- Terraform tutorial resources:
- Go through all the steps in:
- [Set Up a Simple Infrastructure with OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm)
- Keep the scripts you created in the following directory:
- `$HOME/tf-simple-infrastructure/`

## 1. Gather Required Information

Gather information for the compute instances in the node pool.

[Get Node Shape](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

This tutorial uses`VM.Standard2.1`for the compute instances in the node pool..

Save the`<node-shape>``VM.Standard2.1`in your notepad.
To learn more about the shape, go to[Standard Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#vm-standard).

[Get Image ID](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

- In the Console navigation bar, find your region.
See[Working in Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm).
- Go to[Image Release Notes](https://docs.oracle.com/iaas/images/).
- Select Oracle Linux 7.x .
- Select the latest Oracle Linux 7.x-&lt;date&gt; . Don't select any images labeled Gen2-GPU .
- Copy the Image OCID for your region.
- Save the`<image-ocid>`in your notepad.

Note  
  
Ensure that you select a commercial OCID without`gov`in its OCID.

## 2. Copy Existing Scripts

Copy scripts created at[Set Up a Simple Infrastructure with OCI Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-simple-infrastructure.htm). Then, remove the scripts and outputs related to the compute instance. In the next section, you declare a node pool with compute instances.

[Copy the Scripts](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

- In your`$HOME`directory, create a directory called`tf-cluster`and change to that directory.

```

```

```

```

- Copy all the files ending in`.tf`from the`tf-simple-infrastructure`directory.

```

```

- Confirm that you have the following files in your directory.

```

```

```

```

Note  
  
Don't copy the state files (`terraform.tfstate`or`terraform.tfstate.backup`). These files contain the state of resources for their current directory. After you run the scripts in this new directory, you get a new state file.

[Remove Irrelevant Scripts](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

- Remove the`compute.tf`file from the`tf-cluster`directory.

```

```

- In the`outputs.tf`file, remove all the outputs for the compute instance.

```

```

## 3. Create Scripts

Create scripts for a cluster, a node pool, and to print outputs.

[Declare a Cluster](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

- Create a file called`cluster.tf`.
- Add the following code to`cluster.tf`.

- Replace`<your-cluster-name>`with a name of your choice. Example:`tf-cluster`.

```

```

- Save the`cluster.tf`file.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

At[Argument Reference (oci_containerengine_cluster)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/containerengine_cluster#argument-reference), find all required arguments:
- compartment_id
- kubernetes_version
- name
- vcn_id

[To navigate to this URL](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

To navigate to[Argument Reference (oci_containerengine_cluster)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/containerengine_cluster#argument-reference):
- Go to[Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs).
- In the Filter box on the upper left, enter`container engine`.

Results are returned for both data sources and resources.
- Under Container Engine , go to Resources and select oci_containerengine_cluster .
- Select Argument Reference .

[Argument Reference](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/containerengine_cluster#argument-reference)opens.

Construct a resource block:
- Declare a resource block with the keyword:`resource`
- Add a label for resource type :`"oci_containerengine_cluster"`
- Add a label for a local name (your choice):
- The label can contain letters, digits, underscores (`_`), and hyphens (`-`). The first character must not be a digit.
- Example:`"oke-cluster"`
- Inside the code block, provide a value for the required arguments:
- compartment_id: Point to the compartment declared in`compartment.tf`:`oci_identity_compartment.tf-compartment.id`
- kubernetes_version: This tutorial uses version`v1.21.5`. You can check the Quick Create option in the Console for the latest version.
- name: Assign a name of your choice.
- vcn_id: Point to the compartment declared in`vcn-module.tf`:`module.vcn.vcn_id`

A required argument doesn't have a default value.
- Provide values for the following optional arguments to override their default values.
- kubernetes_network_config: Assign a CIDR block as a string for the following arguments:
- `pods_cidr`
- `services_cidr`
Note  
  

The CIDR block for the pods must not overlap with the worker node and load balancer subnet CIDR blocks.

The CIDR block for the Kubernetes service must not overlap with the VCN CIDR block.

The example code in this tutorial uses the same CIDR blocks as the Quick Create option in the Console.

For more explanation, see[CIDR Blocks and Kubernetes Engine (OKE)](https://docs.oracle.com/iaas/Content/ContEng/Concepts/contengcidrblocks.htm).
- service_lb_subnet_ids: Assign the public subnet you declared in`public-subnet.tf`
Note  
  
The argument, service_lb_subnet_ids accepts a list of subnet ids:
- Even if you have one subnet, use square brackets to denote a list.
- Example:`[oci_core_subnet.vcn-public-subnet.id]`

[Declare a Node Pool](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

- Create a file called`node-pool.tf`.
- Add the following code to`node-pool.tf`.

- Replace the following fields with the information you gathered in section one:
- `<node-shape>`with`VM.Standard2.1`
- `<image-ocid>`
- Replace the following field with the name you chose when you declared a cluster:
- `<your-cluster-name>`

```

```

- Save the`node-pool.tf`file.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

At[Alarm Reference (oci_containerengine_node_pool)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/containerengine_node_pool#argument-reference), find all required arguments:
- cluster_id
- compartment_id
- kubernetes_version
- name
- node_config_details
- placement_configs
- availability_domain
- subnet_id
- node_shape
- node_source_details
- image_id
- source_type

[To navigate to this URL](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

To navigate to[Alarm Reference (oci_containerengine_node_pool)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/containerengine_node_pool#argument-reference):
- Go to[Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs).
- In the Filter box on the upper left, enter`container engine`.

Results are returned for both data sources and resources.
- Under Container Engine , go to Resources and select oci_containerengine_node_pool .
- Select Argument Reference .

[Argument Reference](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/containerengine_node_pool#argument-reference)opens.

Construct a resource block:
- Declare a resource block with the keyword:`resource`
- Add a label for resource type :
```

```

- Add a label for a local name (your choice):
- The label can contain letters, digits, underscores (`_`), and hyphens (`-`). The first character must not be a digit.
- Example:`"oke-node-pool"`
- Inside the code block, provide a value for the required arguments:
- cluster_id: Point to the cluster declared in`cluster.tf`:
```

```

- compartment_id Point to the compartment declared in`compartment.tf`:
```

```

- kubernetes_version: This tutorial uses the same version as the Console Create Cluster wizard .
- name: Assign a name of your choice. The Console Create Cluster wizard uses the name`pool1`.
- node_shape: Enter information you gathered in section one.
- node_source_details:
- image_id: Enter information you gathered in section one.
- source_type: Set to`"image"`.
- Provide values for the following optional arguments to override their default values.
- initial_node_labels: Assign key/value pairs for the nodes.
- key: Assign a key of your choice. The Console Quick Create option creates the key`"name"`.
- value: Assign a value for the key. The Console Quick Create option assigns`"<your-cluster-name>"`to the`"name"`key.

[Add Outputs](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

In this section, you declare outputs for the cluster and the node pool.

- Add the following code to`outputs.tf`.

```

```

- Save the`outputs.tf`file.

[Explanation](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

- For cluster outputs, see Attribute Reference at[oci_containerengine_cluster](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/containerengine_cluster).
- For node pool outputs, see Attribute Reference at[oci_containerengine_node_pool](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/containerengine_node_pool)page.

##### Outputs for List Items

- Usually list attributes are plural (end in s).
- List attribute example for node pool:
- `node_config_details`
- To output all the attributes in a list, use the list attribute by itself, without any brackets.
- Example:
```

```

Sample output:
```

```

- To output or call an item from a list:
- Use the following format:

`<list-attribute-name>[index].<attribute-from-list>`
- Replace`[index]`with:
- [0] for the first item.
- [1] for the second item.
- ...
- [n] for the (n+1) th item.
- Example:

Value for the`size`attribute:
```

```

## 4. Run Scripts

Run your Terraform scripts to create a compartment, a virtual cloud network, a Kubernetes cluster, and a node pool.

[Initialize](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

- Initialize a working directory in the`tf-cluster`directory.

```

```

Example output:
```

```

- Check the contents of the`tf-cluster`directory.

```

```

Note  
  
Troubleshooting:
- After running`terraform init`
- error message: Failed to query available provider packages :
- If you are on a VPN, check your proxy settings.
You now have a folder called`.terraform`that includes the plugins for the`oci`provider.

[Plan](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

- Create an execution plan :

```

```

- Review the changes that Terraform plans to make to your account.

Example output:
```

```

[Apply](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

Run your Terraform scripts:

```

```

When prompted for confirmation, enter`yes`, for your resources to be created.

It might take 15 minutes or more for the cluster to be created. After Terraform creates the resources, review the output in the terminal.
```

```

[Troubleshooting](https://docs.oracle.com/iaas/Content/dev/terraform/tutorials/tf-cluster.htm#)

- 401 errors - (Service error:NotAuthenticated):
- You have an incorrect value for one of the following:
- tenancy OCID
- user OCID
- fingerprint
- RSA private key (the path or the key)
- no such host:
- You have an incorrect value for the following:
- region identifier

References:

- [Basic CLI Features](https://developer.hashicorp.com/terraform/cli/commands)
- [Oracle Cloud Infrastructure Provider](https://registry.terraform.io/providers/oracle/oci/latest/docs)
- [oci_containerengine_cluster](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/containerengine_cluster)
- [oci_containerengine_node_pool](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/containerengine_node_pool)

## What's Next

Congratulations! You have created a Kubernetes cluster using Terraform, in your Oracle Cloud Infrastructure account.

Now that you have a Kubernetes cluster, try Kubernetes tutorials at[Developer Tutorials](https://docs.oracle.com/iaas/Content/developer/home.htm#home__functions).

To explore more information about development with Oracle products, check out these sites:
- [Oracle Developer Center](https://www.oracle.com/developer/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
