# Upgrading a Basic Cluster to an Enhanced Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingbasicclusterstoenhanced.htm
- Fetched: 2026-09-05 01:56 CDT

# Upgrading a Basic Cluster to an Enhanced Cluster

Find out how to upgrade a basic cluster to an enhanced cluster using Kubernetes Engine (OKE).

You can upgrade a basic cluster to an enhanced cluster, provided it is[VCN-native](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengfaqs.htm#VCN_Native_Clusters)and meets the applicable upgrade prerequisites. A VCN-native cluster is a cluster with a Kubernetes API endpoint that is completely integrated into your own VCN. You cannot upgrade a basic cluster to an enhanced cluster if it is not VCN-native. For information about migrating a cluster to be VCN-native, see[Migrating to VCN-Native Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm).

Note that after you upgrade a basic cluster to an enhanced cluster, you can't downgrade the enhanced cluster back to a basic cluster.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingbasicclusterstoenhanced.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingbasicclusterstoenhanced.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingbasicclusterstoenhanced.htm#)
- 

- On the Clusters list page, select the name of the basic cluster that you want to upgrade to an enhanced cluster. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).

The Cluster details tab shows Cluster type: Basic .
- Select Upgrade to Enhanced Cluster .
- Select the Upgrade to Enhanced Cluster option to confirm that want to upgrade the basic cluster to an enhanced cluster.

Note that after you upgrade a basic cluster to an enhanced cluster, you can't downgrade the enhanced cluster back to a basic cluster.
- Select Upgrade .

The basic cluster is upgraded to an enhanced cluster.

The Cluster details tab now shows Cluster type: Enhanced .
- 

Use the[oci ce cluster update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update.html)command and required parameters to upgrade a basic cluster to an enhanced cluster:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster)
