# Installing PKCS #11
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_installation_pkcs_11.htm
- Fetched: 2026-09-05 02:32 CDT

# Installing PKCS #11

Install PKCS #11 Library.

Run the following command to install the PKCS #11 libraries.
Note  
  
Before you install PKCS #11 RPM package, ensure that you have installed the`oci-hsm-client-<version>.x86_64.rpm`on your machine and ensure`client_daemon`is running.
```

```

The PKCS #11 libraries are installed under the path`/opt/oci/hsm/lib`and the header files are available in the directory`/opt/oci/hsm/include`
