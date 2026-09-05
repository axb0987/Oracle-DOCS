# Creating a Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-cluster.htm
- Fetched: 2026-09-05 01:57 CDT

# Creating a Cluster

Find out how to create a cluster using Kubernetes Engine (OKE).

You can use Kubernetes Engine to create new Kubernetes clusters. To create a cluster, you must either belong to the tenancy's Administrators group, or belong to a group to which a policy grants the CLUSTER_MANAGE permission. See[Policy Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpolicyconfig.htm).

To ensure high availability, Kubernetes Engine performs the following tasks:
- Creates the Kubernetes control plane on multiple Oracle-managed control plane nodes, distributing the control plane nodes across different availability domains in a region (where supported).
- Creates worker nodes in each of the fault domains in an availability domain, distributing the worker nodes as evenly as possible across the fault domains (subject to any other infrastructure restrictions).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-cluster.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-cluster.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-cluster.htm#)
- 

- On the Clusters list page, select Create cluster . If you need help finding the list page, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select one of the following workflows to create the cluster:
- Quick create: Select this workflow when you only want to specify those properties that are absolutely essential for cluster creation. When you select this option, Kubernetes Engine uses default values for many cluster properties, and creates new network resources as required.
- Custom create: Select this workflow when you want to be able to specify all of the cluster's properties, use existing network resources, and select advanced options.

For more information about the different workflows, see[Creating Kubernetes Clusters Using Console Workflows](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm).
- Select Proceed .
- Complete the pages of the workflow you selected. For more information, see:
- [Using the Console to create a Cluster with Default Settings in the 'Quick Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Quick_Cluster_with_Default_Settings.htm)
- [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm)
- 

Use the[oci ce cluster create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/create.html)command and required parameters to create a cluster:

```

```

For example:

```

```

To create a cluster with a virtual node pool and virtual nodes:

- Create a new cluster, specifying the OCI VCN-Native Pod Networking CNI plugin for pod networking:

```

```

For example:

```

```

- Obtain the OCID of the new cluster for use in the next step.
- Create a new virtual node pool in the cluster:

```

```

where:
- `<ad-name>`is the name of the availability domain in which to place virtual nodes. To find out the availability domain name to use, run:

```

```

- `<shape-name>`is one of`Pod.Standard.E3.Flex`,`Pod.Standard.E4.Flex`.

For example:

```

```

- 

Run the[CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster)
