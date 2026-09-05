# Uploading Certificates Generated from a CSR
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_dedicated_kms_uploading_cert.htm
- Fetched: 2026-09-05 02:36 CDT

# Uploading Certificates Generated from a CSR

Learn how to upload the signed certificate required for initialization of a new HSM cluster in OCI Dedicated Key Management.

Prerequisites : Complete the steps in the following tasks before you start this task:
- [Downloading a Certificate Signing Request](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_download_cert.htm)
- [Uploading Certificates Generated from a CSR](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_dedicated_kms_uploading_cert.htm)

Have the partition certificate ( partitionCert.pem ) and the partition owner certificate ( partitionOwnerCert.pem ) available before starting this task.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_dedicated_kms_uploading_cert.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_dedicated_kms_uploading_cert.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_dedicated_kms_uploading_cert.htm#)
- 

Complete the following steps to activate the HSM cluster:

- If you're not on the Upload certificates section of the Initialize cluster workflow, follow the instructions in[Downloading a Certificate Signing Request](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_download_cert.htm). You can skip step 3 ( Download CSR ) because you already have your certificates, and select Next to advance to the Upload certificates section.
- In the Upload partition certificate section, drop or select the partition certificate from your local machine into the form.
- In the Upload partition owner certificate section, drop or select the partition owner certificate from your local machine into the form.
- Select Upload .
- 

Use the[oci kms kms-hsm-cluster hsm-cluster upload-certificate-signing-request](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/kms-hsm-cluster/hsm-cluster/upload-partition-certificates.html)command and required parameters to download the certificate:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[UploadPartitionCertificates](https://docs.oracle.com/iaas/api/#/en/key/latest/HsmCluster/UploadPartitionCertificates)API with the KMSHSMCLUSTER endpoint to upload the partition owner certificates to the HSM Cluster resource.
Note  
  

The HSM Cluster Endpoint is used for is used for cluster management operations including Create, Update, List, Get, and Delete. This endpoint is also called the KMSHSMCLUSTER endpoint.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
