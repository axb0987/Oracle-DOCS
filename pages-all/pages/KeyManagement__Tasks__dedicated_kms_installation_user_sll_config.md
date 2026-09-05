# Setting up the HSM Cluster Client in Linux
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_installation_user_sll_config.htm
- Fetched: 2026-09-05 02:32 CDT

# Setting up the HSM Cluster Client in Linux

Learn how to configure the HSM cluster client for Linux.

You must complete the following configuration steps for a new user configuration.
- 

Generate a private key (`pkey-c`) and a CSR (`pkeycsr.csr`).
```

```

- 

Get the CSR (`pkeycsr.csr)`signed by Partition Owner using`customerPO.key`and`partitionOwnerCert.pem`to generate`cert-c`.
```

```

- Copy`pkey-c`,`cert-c`, and`partitionOwnerCert.pem`to the path`/opt/oci/hsm/data/`
