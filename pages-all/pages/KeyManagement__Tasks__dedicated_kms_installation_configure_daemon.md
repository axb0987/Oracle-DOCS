# Configuring Client Daemon
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_installation_configure_daemon.htm
- Fetched: 2026-09-05 02:32 CDT

# Configuring Client Daemon

Configure client daemon.

Complete the following steps to configure the client daemon. Ensure you have copied`pkey-c, cert-c,`and`partitionOwnerCert.pem`to`/opt/oci/hsm/data`directory.
- Use vim or any editor to update the`client_daemon`configuration to`/opt/oci/hsm/data`directory.
```

```

- Update hostname field with DNS value available on the OCI Console. For more information, see[Getting HSM Partition DNS Name.](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_getting_dns_name.htm)
- Update port field with client daemon Port value available on the OCI Console. For more information, see[Getting HSM Partition Port Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_fetching_hsm_partition_port_details.htm).
Output
```

```
