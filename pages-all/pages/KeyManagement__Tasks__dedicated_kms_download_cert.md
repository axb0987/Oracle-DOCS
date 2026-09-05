# Downloading a Certificate Signing Request
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_download_cert.htm
- Fetched: 2026-09-05 02:32 CDT

# Downloading a Certificate Signing Request

Learn how to download a certificate signing request (CSR) for an HSM cluster in OCI Dedicated Key Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_download_cert.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_download_cert.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_download_cert.htm#)
- 

Complete the following steps to initialize the HSM cluster:

- On the HSM cluster list page, find the HSM cluster that you want to work with. If you need help finding the list page, see[Listing HSM Clusters](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/dedicated_kms_list_hsm_details_dita.htm).
- From the Actions menu (three dots) in the row of the HSM cluster, select Initialize cluster .

Note : The Intitialize cluster option is visible only for HSM clusters that are in "Initialization required" state.
- Select Download CSR .
- Download the CSR to your local machine.
- Select Next to continue to the Upload certificates workflow.
Leave the Console window open and continue the initialization operation by following the instructions in[Signing the CSR](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_signing_cert.htm).
- 

Use the[oci kms kms-hsm-cluster hsm-cluster download-certificate-signing-request](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-cluster/download-certificate-signing-request.html)command and required parameters to download the certificate:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[DownloadCertificateSigningRequest](https://docs.oracle.com/iaas/api/#/en/key/latest/HsmCluster/DownloadCertificateSigningRequest)API with the KMSHSMCLUSTER endpoint to download the certificate signing request (CSR) for the specified HSM Cluster resource.
Note  
  

The HSM Cluster Endpoint is used for is used for cluster management operations including Create, Update, List, Get, and Delete. This endpoint is also called the KMSHSMCLUSTER endpoint.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
