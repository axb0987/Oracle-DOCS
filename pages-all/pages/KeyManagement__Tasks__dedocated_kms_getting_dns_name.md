# Getting HSM Cluster DNS Name
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_getting_dns_name.htm
- Fetched: 2026-09-05 02:34 CDT

# Getting HSM Cluster DNS Name

Get DNS name for the HSM cluster in the "Activation Required" state.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_getting_dns_name.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_getting_dns_name.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_getting_dns_name.htm#)
- 

- Open the[Oracle Cloud Console](https://cloud.oracle.com/)navigation menu and click Identity &amp; Security . Under Key Management &amp; Secret Management , click Dedicated Key Management .
- In the Dedicated KMS page, from the list of clusters, click a cluster name to open its details page.
- The HSM Cluster Information section display the DNS Name of the HSM cluster.
- 

Use the[oci kms kms-hsm-cluster hsm-cluster get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-cluster/get.html)command and required parameters to get the HSM partition's DNS name.

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetHsmCluster](https://docs.oracle.com/iaas/api/#/en/key/release/HsmCluster/GetHsmCluster)operation that uses the KMSHSMCLUSTER API endpoint.
Note  
  
Each region uses the KMSHSMCLUSTER API endpoint for HSM cluster operations. For regional endpoints, see the[API Endpoints](https://docs.oracle.com/iaas/api/#/en/key/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
