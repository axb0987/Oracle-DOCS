# Activating an HSM Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_activating_hsm_cluster.htm
- Fetched: 2026-09-05 02:32 CDT

# Activating an HSM Cluster

Learn what operations are needed to activate an HSM cluster in Dedicated Key Management after initialization.

After the HSM cluster is initialized, the state changes to "Activation Required." To activate the cluster, you need to complete the following tasks:
- 

Gather the following information about the HSM cluster from the cluster details page:
- DNS name for the HSM partition
- User Management utility and Key Management utility port details for the HSM partition
- PRECO credentials for the HSM cluster in the "Activation Required" state

See the following topics for instructions:[Get DNS name](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_getting_dns_name.htm),[Get HSM partition port details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedocated_kms_fetching_hsm_partition_port_details.htm), and[View PRECO Credentials](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_view_preco_credentails.htm).
- Create a Compute instance in the OCI Compute service to use with the Dedicated KMS command line tools. See[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)for instructions.
- Configure a service gateway, as needed. A service gateway lets cloud resources without public IP addresses to privately access Oracle services. If you access Oracle services through a service gateway, you must use client utilities to access your HSM partitions. For more information on how to set up and manage a service gateway, see[Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm).
- 

Install and configure Dedicated KMS command line tools:
- Linux: Complete the tasks in[Dedicated KMS command line tools for Linux](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_linux_support.htm).
- Windows: Complete the tasks in[Dedicated KMS command line tools for Windows](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_install_windows_client.htm)
- Change the default PRECO user password using a command line tool. After you change the default password, the HSM cluster state changes from "Activation Required" to "Activating," and then to "Active." After the cluster is in the "Active" state, it is ready for use. See[To change the default PRECO user password](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_activating_hsm_cluster.htm#dedicated_kms_activating_hsm_cluster_preco_pw__change-default-preco-user-password)in this topic for instructions.

## Changing the Default PRECO User Password

After completing these steps in this topic, you must sign in to a Linux or Windows User Management Utility using PRECO user credentials and change the default PRECO user password. Upon changing the password, the PRECO user account is converted to a Crypto Officer account.

[To change the default PRECO user password](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_activating_hsm_cluster.htm#)

- 

From the command line, open the`User_Mgmt_util`utility.

Linux:

```

```

Windows:

```

```

- Sign in as PRECO User.
```

```

- List the number of users.
```

```

- Change the default PRECO password using the`changePswd`command.
```

```

- List users to verify if the user account has changed from PRECO to Crypto Officer (CO).
-
