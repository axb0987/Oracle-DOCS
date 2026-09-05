# Using Remote Exec
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/usingremoteexec.htm
- Fetched: 2026-09-05 02:57 CDT

# Using Remote Exec

With Resource Manager, you can use Terraform's remote exec functionality to execute scripts or commands on a remote computer. You can also use this technique for other provisioners that require access to the remote resource.

For more information, see[remote-exec Provisioner (terraform.io)](https://developer.hashicorp.com/terraform/language/resources/provisioners/remote-exec).

## Before You Begin

- The location where the script is remotely executed must be an Oracle Cloud Infrastructure resource with one of the following configurations.
- A[private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm). For more information, see[Private Remote Exec](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#remote-exec).
- A[public IP address](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm)with support of remote logins.
- On Windows, WinRM must be enabled. On Linux or Unix, SSH must be enabled.
- A key pair used for signing API requests, with the public key uploaded to Oracle. For more information on generating and uploading keys, see[Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm).

## Authenticating

We recommend using one of the following approaches, depending on whether you have access to the Vault service. For more information, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).

### With Vault

First, use Vault to encrypt your private key. For more information, see[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm)and[Using Master Encryption Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm).

Next, provide the encrypted private key to Resource Manager. You can use the decrypt data source to decrypt it.

The following code sample demonstrates this process.

```

```

### Without Vault

If you do not have access to the Vault service, you can dynamically generate a key pair and store them in the state file.
- Generate a key pair using a TLS resource.
- When you launch the compute instance, use the public key from the TLS resource.
- When you establish the SSH connection, provide the private key.
Caution  
  
You should not save your private key in your Terraform configuration file because that is not a secure location.

The following sample demonstrates how to use the TLS private key resource to provision a compute instance, then perform a remote execution on that instance.

```

```

### Connection Construct

This example demonstrates how to use a`connection`construct for remote exec. Terraform uses a number of defaults when connecting to a resource, but these can be overridden using a`connection`block in either a`resource`or`provisioner`. For more information, see[Provisioner Connection Settings](https://developer.hashicorp.com/terraform/language/resources/provisioners/connection)
