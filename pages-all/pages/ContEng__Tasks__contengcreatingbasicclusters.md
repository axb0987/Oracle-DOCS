# Creating a Basic Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingbasicclusters.htm
- Fetched: 2026-09-05 01:54 CDT

# Creating a Basic Cluster

Find out how to create a basic cluster using Kubernetes Engine (OKE).

You can create basic clusters using the Console, the CLI, and the API.

Note the following when creating clusters:
- When using the Console to create a cluster, if you don't select any enhanced features during cluster creation, you have the option to create the new cluster as a basic cluster. A new cluster is created as an enhanced cluster by default, unless you explicitly choose to create a basic cluster.
- When using the CLI or the API to create a cluster, you can specify whether to create a basic cluster or an enhanced cluster. If you don't explicitly specify the type of cluster to create, a new cluster is created as a basic cluster by default (until the date specified in the Service Change Announcement[here](https://docs.oracle.com/iaas/Content/servicechanges.htm#servicechanges_topic_oke)).

Also note that you can upgrade a basic cluster to an enhanced cluster, provided it is a[VCN-native](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengfaqs.htm#VCN_Native_Clusters)cluster and meets the applicable upgrade prerequisites. A VCN-native cluster is a cluster with a Kubernetes API endpoint that is completely integrated into your own VCN. However, having upgraded a basic cluster to an enhanced cluster, you can't downgrade the enhanced cluster back to a basic cluster. For more information about upgrading a basic cluster, see[Upgrading a Basic Cluster to an Enhanced Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingbasicclusterstoenhanced.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingbasicclusters.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingbasicclusters.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingbasicclusters.htm#)
- 

To create a basic cluster using the Console:
- Follow the instructions in either of the following topics to create the cluster:
- [Using the Console to create a Cluster with Default Settings in the 'Quick Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Quick_Cluster_with_Default_Settings.htm)
- [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm)
- 

Do not select any of the enhanced cluster features in the 'Quick Create' or 'Custom Create' workflows.

Enhanced cluster features include:
- Virtual node pools and virtual nodes (both 'Quick Create' and 'Custom Create' workflows). See[Working with Virtual Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithvirtualnodes.htm).
- Cluster add-on management ('Custom Create' workflow only). See[Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm).

When you do not select any of the enhanced cluster features, the Create a Basic cluster option is shown on the Review and create page of the workflow.
- Choose the Create a Basic cluster option on the Review and create page.
- Select Create cluster to create the new cluster as a basic cluster.
- Verify that you have created the new cluster as a basic cluster by confirming that the Cluster details tab shows Cluster type: Basic .
- 

Use the[oci ce cluster create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/create.html)command and required parameters to create a basic cluster

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster)
