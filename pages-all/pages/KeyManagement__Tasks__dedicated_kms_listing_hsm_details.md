# Getting HSM Cluster Details
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_listing_hsm_details.htm
- Fetched: 2026-09-05 02:33 CDT

# Getting HSM Cluster Details

Learn how to find the details information for an HSM cluster in Dedicated Key Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_listing_hsm_details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_listing_hsm_details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_listing_hsm_details.htm#)
- 

- On the HSM cluster list page, find the HSM cluster that you want to work with. If you need help finding the list page, see[Listing HSM Clusters](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_details_dita.htm).
- Select a cluster name to open its details page.
- The HSM cluster information section displays the following information.

- OCID: The unique, Oracle-assigned ID of the HSM cluster.
- Compartment: The name of the compartment that contains the HSM cluster.
- Created: The date and time when you initially created the HSM cluster.
- DNS Name: DNS name for accessing the HSM cluster.
- 

Use the[oci kms kms-hsm-cluster hsm-cluster get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-cluster/get.html)command and required parameters to get details information for an HSM cluster.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[GetHSMCluster](https://docs.oracle.com/iaas/api/#/en/key/latest/HsmCluster/GetHsmCluster)API with the KMSHSMCLUSTER endpoint to get the details of an HSM cluster.
Note  
  
Each region uses the KMSHSMCLUSTER API endpoint for HSM cluster operations. For regional endpoints, see the[API Endpoints](https://docs.oracle.com/iaas/api/#/en/key/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
