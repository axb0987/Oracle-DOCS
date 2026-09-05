# Getting Certificate
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_get_cert.htm
- Fetched: 2026-09-05 02:33 CDT

# Getting Certificate

Command to get certificate details.

The`getCert`command get the certificate stored on the HSM.

In the User Management utility, open a command prompt and run`getCert`command to get the certificate stored on the HSM cluster.

Syntax
```

```

Parameter Description
`FileName`Absolute path to store the cert file.
`CertType`CertType:
- 1 - Manufacturer Root Certificate
- 2 - HSM Certificate (issued by Manufacturer Root Certificate)
- 4 - Partition Owner Certificate
- 8 - Partition Certificate (issued by Partition Owner Certificate)
- 16 - Partition Certificate (issued by HSM Certificate)

Example
```

```
