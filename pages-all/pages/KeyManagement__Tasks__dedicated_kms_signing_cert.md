# Signing the CSR
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_signing_cert.htm
- Fetched: 2026-09-05 02:33 CDT

# Signing the CSR

Learn how to sign a certificate signing request (CSR) as part of an HSM cluster initialization in OCI Dedicated Key Management.

Prerequisite: This task is completed after you download the CSR as described in[Downloading a Certificate Signing Request](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_download_cert.htm).
To sign, you must first create a self-signed signing certificate and use it for signing the certificate signing request (CSR). To sign, you must complete the following tasks:
- Generate an RSA key pair for your HSM cluster resource. This key is called the Partition Owner (PO) key. Ensure you store the key and pass phrase in secure and safe location such as a KMS Vault. You can use the key to sign the partition CSR you downloaded in the previous step.
```

```

- Use the Partition Owner key (`customerPO.key`) key to generate a partition owner certificate (`partitionOwnerCert.pem`). The following command generates the certificate valid only for ten years. You can change the expiry date if required but expiry must be at least 5 years. The partition owner certificate must be shared with Dedicated KMS users.
```

```

- Sign the CSR (`partitionCsr`.csr) using the Partition Owner key (`customerPO.key`) and`partitionOwnerCert.pem`(created in previous steps) to generate`partitionCert.pem`.
```

```

- Encode the partitionCert.pem and partitionOwnerCert.pem to base 64 using below commands. (This step is only required for CLI).
- Upload the partitionCert.pem and partitionOwnerCert.pem certificates to the HSM cluster.
```

```
