# Scheduling the Deletion of an HSM Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_deleting_hsm_cluster.htm
- Fetched: 2026-09-05 02:32 CDT

# Scheduling the Deletion of an HSM Cluster

Learn how to schedule the deletion of an HSM cluster.
When you schedule the deletion of an HSM cluster, the cluster lifecycle state changes to "pending deletion". The cluster is deleted by OCI Dedicated Key Management after a 7-day waiting period. You can cancel the deletion at any time during the 7-day waiting period. See[Canceling Scheduled Deletion of an HSM Cluster](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_canceling_deleting_hsm_cluster_dita.htm)for more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_deleting_hsm_cluster.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_deleting_hsm_cluster.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_deleting_hsm_cluster.htm#)
- 

- On the HSM cluster list page, find the HSM cluster that you want to work with. If you need help finding the list page, see[Listing HSM Clusters](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_details_dita.htm).
- From the Actions menu (three dots) at the end of the row entry for the cluster, select Delete HSM cluster .
- Enter the name of the cluster to confirm the deletion.
- Select Delete HSM cluster .

Note  
  
OCI When you schedule a cluster for deletion, the cluster goes to a transition state and all actions on the HSM Cluster Details page are disabled. After 7 days, the cluster is deleted, unless you cancel the deletion.
- 

Use the[oci kms kms-hsm-cluster hsm-cluster schedule-hsm-cluster-deletion](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-cluster/schedule-hsm-cluster-deletion.html)command and required parameters to schedule HSM cluster deletion.

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[ScheduleHsmClusterDeletion](https://docs.oracle.com/iaas/api/#/en/key/latest/HsmCluster/ScheduleHsmClusterDeletion)API with the KMSHSMCLUSTER API endpoint to schedule the deletion of an HSM cluster.
Note  
  
Each region uses the KMSHSMCLUSTER API endpoint for HSM cluster operations. For regional endpoints, see the[API Endpoints](https://docs.oracle.com/iaas/api/#/en/key/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
