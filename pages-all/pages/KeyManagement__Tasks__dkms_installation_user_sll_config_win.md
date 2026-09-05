# Setting up the HSM Cluster Client in Windows
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_installation_user_sll_config_win.htm
- Fetched: 2026-09-05 02:34 CDT

# Setting up the HSM Cluster Client in Windows

Learn how to configure the HSM cluster client for Windows.

You must complete the following configuration steps for a new user configuration.
- 

Generate a private key (`pkey-c`) and a CSR (`pkeycsr.csr`).
```

```

- 

Get the CSR (`pkeycsr.csr)`signed by the partition owner using the`customerPO.key`and`partitionOwnerCert.pem`files to generate`cert-c`. For information on`customerPO.key`and`partitionOwnerCert.pem`, see[Signing the CSR](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_signing_cert.htm).
```

```

- Copy`pkey-c`,`cert-c`, and`partitionOwnerCert.pem`to the`/data`directory of the Windows client installation. By default, the directory is at`C:\Program Files\Oracle\DedicatedKms\data`
