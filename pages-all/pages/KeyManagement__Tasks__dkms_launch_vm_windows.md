# Configure the Dedicated KMS User Management Utility in Windows
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_launch_vm_windows.htm
- Fetched: 2026-09-05 02:34 CDT

# Configure the Dedicated KMS User Management Utility in Windows

Learn how to configure the Dedicated KMS user management utility in Windows.

Complete the following steps to configure the`user_mgmt_util.cfg`utility.
- 

Ensure you have moved the`pkey-c`,`cert-c`, and`partitionOwnerCert.pem`files into the data directory, for example,`c:\Program Files\Oracle\DedicatedKMS\data`. For more information, see[Signing the CSR](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_signing_cert.htm).
- Open the`user_mgmt_util.cfg`in a text editor to validate the installation location and DNS name of the HSM.
- If required, update hostname field with DNS value available on the OCI Console. For more information, see[Getting HSM Cluster DNS Name.](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_getting_dns_name.htm)
- If required, update port field with user management utility port value available on the OCI Console. For more information, see[Getting HSM Cluster Port Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_fetching_hsm_partition_port_details.htm).
Output
```

```
