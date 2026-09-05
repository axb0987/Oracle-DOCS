# Renaming an HSM Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_renaming_hsm_cluster.htm
- Fetched: 2026-09-05 02:33 CDT

# Renaming an HSM Cluster

Learn how to update an HSM cluster name.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_renaming_hsm_cluster.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_renaming_hsm_cluster.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_renaming_hsm_cluster.htm#)
- 

- Open the navigation menu , select Identity &amp; Security , and then select Dedicated Key Management .
- In the Dedicated Key Management home page, select a cluster from the list.
- In the HSM Cluster Details page, select Rename .
- Enter a new name for the cluster and then select Update .
- 

Use the[oci kms kms-hsm-cluster hsm-cluster update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-cluster/update.html)command and required parameters to update an HSM cluster.

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[UpdateHsmCluster](https://docs.oracle.com/iaas/api/#/en/key/latest/HsmCluster/UpdateHsmCluster)API with the KMSHSMCLUSTER endpoint to update an HSM cluster resource.
Note  
  
Each region uses the KMSHSMCLUSTER API endpoint for HSM cluster operations. For regional endpoints, see the[API Endpoints](https://docs.oracle.com/iaas/api/#/en/key/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
