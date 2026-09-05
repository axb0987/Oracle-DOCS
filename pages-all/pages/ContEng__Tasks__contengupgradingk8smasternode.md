# Upgrading the Kubernetes Version on Control Plane Nodes in a Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8smasternode.htm
- Fetched: 2026-09-05 01:56 CDT

# Upgrading the Kubernetes Version on Control Plane Nodes in a Cluster

Find out how to upgrade the version of Kubernetes running on the control plane nodes of clusters that you create using Kubernetes Engine (OKE).

When Kubernetes Engine supports a newer version of Kubernetes than the version currently running on the control plane nodes in a cluster, you can upgrade the Kubernetes version running on the control plane nodes.

To upgrade the Kubernetes version running on the control plane nodes in a cluster, all the worker nodes must be in a READY state. The Kubernetes version configured for each managed node pool, and the Kubernetes versions currently running on all worker nodes, must also be compatible with the target control plane version. If the upgrade fails, review the failed`CLUSTER_UPDATE`work request for more information. See[Viewing Work Requests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm). The Kubernetes version configured for a managed node pool can differ from the Kubernetes versions currently running on its nodes (for example, after you configure a node pool with an earlier Kubernetes version but before you replace the existing nodes). Kubernetes Engine checks both when upgrading the control plane.

Note that when you upgrade the Kubernetes version running on control plane nodes, the virtual nodes in every virtual node pool in the cluster are also automatically upgraded to that Kubernetes version. For more information about virtual node upgrade, see[Upgrading Virtual Nodes to a Newer Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingvirtualnodes.htm).
Note  
  

If the cluster uses a master encryption key that you manage, upgrading the control plane from an earlier Kubernetes version to Kubernetes version 1.36.1 or later enables KMS provider version 2. Kubernetes Engine uses KMS provider version 2 for new Kubernetes secret objects and for existing secret objects that are subsequently updated.

Existing unchanged secret objects can remain encrypted using KMS provider version 1. They are not migrated automatically when you upgrade the control plane. To re-encrypt all existing unchanged secret objects using KMS provider version 2, see[Migrating Kubernetes Secrets to KMS v2](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingsecretstokmsv2.htm).
Important  
  
After you upgrade control plane nodes to a newer Kubernetes version, you can't downgrade the control plane nodes to an earlier Kubernetes version. So, before you upgrade the Kubernetes version running on the control plane nodes, test that applications deployed on the cluster are compatible with the new Kubernetes version.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8smasternode.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8smasternode.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8smasternode.htm#)
- 

- 

On the Clusters list page, locate the cluster for which you want to upgrade the Kubernetes version running on the control plane nodes. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).

Where Kubernetes Engine supports a newer Kubernetes version than the version currently running on the control plane nodes of a cluster:
- An Upgrade recommended label appears beside the cluster if the Kubernetes version currently running on the control plane is not the most recent version that Kubernetes Engine supports, but the version is still supported by Kubernetes Engine. In this case, an Upgrade available option is shown on the Actions menu (three dots) on the Clusters list page.
- An Upgrade strongly recommended label appears beside the cluster if the Kubernetes version currently running on the control plane is no longer supported by Kubernetes Engine. In this case, an Upgrade recommended option is shown on the Actions menu (three dots) menu on the Clusters list page.

In both cases, an equivalent option ( New Kubernetes version available ) is also shown on the Actions menu on the cluster details page.
- On the Clusters list page, select Upgrade available or Upgrade recommended (as appropriate) from the Actions menu (three dots) .
- In the Upgrade cluster control plane dialog box, select the Kubernetes version to which to upgrade the control plane nodes, and select Upgrade . We recommend that you select a version number that has the format`x.y`(see[Kubernetes Versions and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengupgradeoverview.htm)).

Note the list of Kubernetes versions includes preview versions provided for early access testing and validation purposes only. These preview versions have ".0" as the patch version number (for example, 1.34.0). Preview versions are not intended for production workloads, and might contain issues without known workarounds. We do not recommend using preview versions for production workloads.

The Kubernetes version running on the control plane nodes is upgraded. The new Kubernetes version appears as an option when you're defining new node pools for the cluster.
- 

Use the`ce cluster update`command and required parameters to upgrade control plane nodes:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster)
