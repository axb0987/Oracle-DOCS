# Getting PRECO Credentials
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_view_preco_credentails.htm
- Fetched: 2026-09-05 02:34 CDT

# Getting PRECO Credentials

Get PRECO credentials for the HSM cluster in "Activation Required" state.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_view_preco_credentails.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_view_preco_credentails.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_view_preco_credentails.htm#)
- 

- Open the[Oracle Cloud Console](https://cloud.oracle.com/)navigation menu and click Identity &amp; Security . Under Key Management &amp; Secret Management , click Dedicated Key Management .
- In the HSM Cluster summary table, find a cluster in "Activation Required" state, click the Actions menu (three dots) and then select View Preco Credentials .
- In the Preco Credentials dialog box, click Show to view the PRECO password.
- Click Close .
- 

Use the[oci kms kms-hsm-cluster hsm-cluster get-pre-co-user-credentials](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-cluster/get-pre-co-user-credentials.html)command and required parameters to get PRECO credentials:
```

```

Example
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetPreCoUserCredentials](https://docs.oracle.com/iaas/api/#/en/key/release/HsmCluster/GetPreCoUserCredentials)operation that uses the KMSHSMCLUSTER API endpoint.
Note  
  
Each region uses the KMSHSMCLUSTER API endpoint for HSM cluster operations. For regional endpoints, see the[API Endpoints](https://docs.oracle.com/iaas/api/#/en/key/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
