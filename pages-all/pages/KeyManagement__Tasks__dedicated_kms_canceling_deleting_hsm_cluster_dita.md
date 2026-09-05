# Canceling Scheduled Deletion of an HSM Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_canceling_deleting_hsm_cluster_dita.htm
- Fetched: 2026-09-05 02:32 CDT

# Canceling Scheduled Deletion of an HSM Cluster

Learn how to cancel the scheduled deletion of an HSM cluster.
Note that you can only cancel the scheduled deletion of HSM clusters that are in the 7-day waiting period that follows the scheduling of the deletion.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_canceling_deleting_hsm_cluster_dita.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_canceling_deleting_hsm_cluster_dita.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_canceling_deleting_hsm_cluster_dita.htm#)
- 

- On the HSM cluster list page, find the HSM cluster that you want to work with. If you need help finding the list page, see[Listing HSM Clusters](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_details_dita.htm).
- From the Actions menu (three dots) at the end of the row entry for the cluster, select Cancel Deletion .
- Select Cancel Deletion in the confirmation dialog to confirm that you want to cancel the deletion of the cluster.
- 

Use the[oci kms kms-hsm-cluster hsm-cluster cancel-hsm-cluster-deletion](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-cluster/cancel-hsm-cluster-deletion.html)command and required parameters to cancel the pending deletion of a HSM cluster:
```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[CancelHsmClusterDeletion](https://docs.oracle.com/iaas/api/#/en/key/latest/HsmCluster/CancelHsmClusterDeletion)API with the KMSHSMCLUSTER endpoint to cancel a scheduled HSM cluster deletion operation.
Note  
  
Each region uses the KMSHSMCLUSTER API endpoint for HSM cluster operations. For regional endpoints, see the[API Endpoints](https://docs.oracle.com/iaas/api/#/en/key/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
