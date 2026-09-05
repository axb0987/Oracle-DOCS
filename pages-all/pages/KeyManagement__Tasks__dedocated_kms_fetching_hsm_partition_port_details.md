# Getting HSM Partition Port Details
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_fetching_hsm_partition_port_details.htm
- Fetched: 2026-09-05 02:34 CDT

# Getting HSM Partition Port Details

Get port details for the HSM partition in the "Activation Required."

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_fetching_hsm_partition_port_details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_fetching_hsm_partition_port_details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_fetching_hsm_partition_port_details.htm#)
- 

- Open the[Oracle Cloud Console](https://cloud.oracle.com/)navigation menu and click Identity &amp; Security . Under Key Management &amp; Secret Management , click Dedicated Key Management .
- In the HSM Cluster summary table, find a cluster in "Active" state, and click and then to view details.
- The Details page displays the User Management utility and Key Management utility port details.
- Click Close .
- 

View HSM partition port details.

Use the[oci kms kms-hsm-cluster hsm-partition get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-partition/get.html)command and required parameters to view port details.
```

```

Example
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetHsmPartition](https://docs.oracle.com/iaas/api/#/en/key/release/HsmPartition/GetHsmPartition)operation that uses the KMSHSMCLUSTER API endpoint.
Note  
  
Each region uses the KMSHSMCLUSTER API endpoint for HSM cluster operations. For regional endpoints, see the[API Endpoints](https://docs.oracle.com/iaas/api/#/en/key/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
