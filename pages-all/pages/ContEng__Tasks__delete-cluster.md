# Deleting a Kubernetes Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-cluster.htm
- Fetched: 2026-09-05 01:57 CDT

# Deleting a Kubernetes Cluster

Find out how to delete an existing Kubernetes cluster that you've created using Kubernetes Engine (OKE).

For more information and notes, see[Deleting Kubernetes Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingcluster.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-cluster.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-cluster.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-cluster.htm#)
- 

- On the Clusters list page, select the name of the cluster that you want to delete. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select Delete from the Actions menu, and then confirm that you want to delete the cluster.
- 

Use the[oci ce cluster delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/delete.html)command and required parameters to delete a cluster:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/DeleteCluster)
