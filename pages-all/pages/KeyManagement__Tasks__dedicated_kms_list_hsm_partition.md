# Getting HSM Partition Details
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_partition.htm
- Fetched: 2026-09-05 02:33 CDT

# Getting HSM Partition Details

Lean how to get HSM partition details for a specified HSM cluster in OCI Dedicated Key Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_partition.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_partition.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_partition.htm#)
- 

- On the HSM cluster list page, find the HSM cluster that you want to work with. If you need help finding the list page, see[Listing HSM Clusters](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_details_dita.htm).
- Select a cluster name to open its details page, then select the HSM partitions tab to see a list of the cluster's partitions.
The HSM partitions tab displays the following partition details:
- OCID: The unique, Oracle-assigned ID of the partition.
- Created: The date and time when you created the HSM partition.
- Status: The lifecyle state for the HSM partition.
- 

Use the[oci kms kms-hsm-cluster hsm-partition get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-partition/get.html)command and required parameters to get HSM partition details.

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[GetHsmPartition](https://docs.oracle.com/iaas/api/#/en/key/latest/HsmPartition/GetHsmPartition)API with the KMSHSMCLUSTER endpoint to view the details of an HSM partition.
Note  
  
Each region uses the KMSHSMCLUSTER API endpoint for HSM cluster operations. For regional endpoints, see the[API Endpoints](https://docs.oracle.com/iaas/api/#/en/key/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
