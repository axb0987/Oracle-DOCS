# Installing the HSM Client RPM Package
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_installation_install_rpm.htm
- Fetched: 2026-09-05 02:32 CDT

# Installing the HSM Client RPM Package

Install client RPM package.

You must install oci-hsm-client RPM package to connect to the HSM cluster.
To install the`oci-hsm-client`RPM package:
- Type the following command:
```

```

Output
```

```

- The RPM installs the client utilities such as`client_daemon,``key_mgmt_util,`and`user_mgmt_util.`After the installation is complete, the binaries are created under the`/opt/oci/hsm/bin`directory.
What's next?
The`oci-hsm-client`package includes the following client utility components. You must first install the package and then configure the utility components one by one:
- `client_daemon`: Lets you to connect to HSMs by establishing an end-to-end encrypted connection. See[Configuring Client Daemon](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_installation_configure_daemon.htm)for configuration instructions.
- `key_mgmt_util`: Lets you perform key management operations (such as create, list and delete keys) on the HSM. See[Configuring Key Management Utility in Linux](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_installation_configure_user_key_mgmt_util1_dita.htm)for configuration instructions.
- `user_mgmt_util`: Lets you to manage and perform user management operations on the HSM. See[Configuring the User Management Utility in Linux](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_launch_vm.htm)for configuration instructions.

For release history information for the Red Hat RPM package, see[Dedicated KMS Client Changelog](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_downloads.htm)
