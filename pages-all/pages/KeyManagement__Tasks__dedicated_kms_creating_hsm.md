# Creating an HSM Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_creating_hsm.htm
- Fetched: 2026-09-05 02:32 CDT

# Creating an HSM Cluster

Learn how to create an HSM cluster resource in OCI Dedicated Key Management.

Note that the cluster created for this operation remains in the "Creating" state while Dedicated Key Management provisions three HSM partitions with DNS entries. When the partitions are configured, the state changes to "Initialization Required." See[Initializing an HSM Cluster](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_initializing_hsm.htm)for details on initializing the new cluster.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_creating_hsm.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_creating_hsm.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_creating_hsm.htm#)
- 

- On the HSM cluster list page, select Create HSM Cluster . If you need help finding the list page, see[Listing HSM Clusters](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_details_dita.htm).
- In the Create HSM Cluster page, select a compartment in which you want to create the HSM cluster.
- Enter a name for the cluster.
- Select Tags to add tags to the cluster.

Note  
  
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags.](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
- Select Create .

After the HSM cluster is created, the cluster state changes from "Creating" to "Initialization Required."
- 

Use the[oci kms kms-hsm-cluster hsm-cluster create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-cluster/create.html)command and required parameters to create an HSM cluster.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[CreateHSMCluster](https://docs.oracle.com/iaas/api/#/en/key/latest/HsmCluster/CreateHsmCluster)API with the KMSHSMCLUSTER API endpoint to create an HSM cluster.
Note  
  

The HSM Cluster Endpoint is used for is used for cluster management operations including Create, Update, List, Get, and Delete. This endpoint is also called the KMSHSMCLUSTER endpoint.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
