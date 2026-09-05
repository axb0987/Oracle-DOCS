# Getting a Managed Node Pool's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-node-pool.htm
- Fetched: 2026-09-05 01:57 CDT

# Getting a Managed Node Pool's Details

Find out how to get the details of a specific managed node pool created using Kubernetes Engine (OKE).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-node-pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-node-pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-node-pool.htm#)
- 

- On the Clusters list page, select the name of the cluster that contains the node pool for which you want to see detailed information. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab.

Node pools in the cluster are shown in tabular form.
- Select the name of the node pool for which you want to see detailed information, and use the tabs on the node pool details page.
- 

Use the[oci ce node-pool get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/get.html)command and required parameters to get details of a managed node pool:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/GetNodePool)
