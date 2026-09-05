# Associating a Key with a Certificate Using the import_key Utility
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_cng_associated_key_with_certificate.htm
- Fetched: 2026-09-05 02:34 CDT

# Associating a Key with a Certificate Using the import_key Utility

Learn how to use the import_key utility to associate a key with a certificate.

To use Dedicated KMS tools with third-party tools such as Microsoft SignTool, you must import the key's metadata to the Dedicated KMS key store and associate it with the certificate. This topic explains how to migrate a key using the`import_key.exe`utility.

The following instructions explain how to move a key into the Dedicated KMS Cavium KSP from another KSP (in the example scenario, the key is being moved from Microsoft's KSP to DKMS).

Before beginning this task, ensure the`OCI Dedicated KMS service`is running on your local machine.

- Get the details of your certificate using the following command:`certutil -store <CertificateStoreName>`

Make a note of the following string values:
- Serial Number
- Unique container name
- Provider

For example:
```

```

- Use the`import_key.exe -from MSKSP -RSA <Unique_container_name>`command to associate the key with the certificate. Use the Unique container name value from the output of the command in the previous step.
For example:
```

```

- Update the certificate store. The command uses the Serial Number value from the first step.
For example:
```

```

- Verify the provider name by running the`certutil -store`command. The command uses the Serial Number value. The Provider value is now "Cavium Key Storage Provider".
For example:
```

```
