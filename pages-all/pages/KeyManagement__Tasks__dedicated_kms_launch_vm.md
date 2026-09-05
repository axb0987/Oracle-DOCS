# Configuring the User Management Utility in Linux
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_launch_vm.htm
- Fetched: 2026-09-05 02:33 CDT

# Configuring the User Management Utility in Linux

Configure user management utility.

Complete the following steps to configure the`user_mgmt_util`utility.
- 

Ensure you have copied pkey-c, cert-c, and partitionOwnerCert.pem to:
```

```

- Use vim or any other editor to update user_mgmt_util configuration.
```

```

- Update hostname field with DNS value available on the OCI Console. For more information, see[Getting HSM Partition DNS Name.](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_getting_dns_name.htm)
- Update port field with user management utility port value available on the OCI Console. For more information, see[Getting HSM Partition Port Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_fetching_hsm_partition_port_details.htm).
Output
```

```
