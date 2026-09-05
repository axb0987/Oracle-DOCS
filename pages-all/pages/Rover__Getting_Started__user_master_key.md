# Using Your Own Master Key with Roving Edge Infrastructure Devices
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/user_master_key.htm
- Fetched: 2026-09-05 03:00 CDT

# Using Your Own Master Key with Roving Edge Infrastructure Devices

Learn how to set up a user-provided KMS-based master key to manage secret information on Roving Edge devices. This only applies to older Roving Edge Devices (provisioned by Oracle).
Important  
  

This section isn't applicable to Roving Edge devices that are self-provisioned. For such devices, the key passphrases are generated during provisioning and they never leave the device. For more information regarding recovery keys on such devices, see '[Recovering Your Roving Edge Infrastructure Device After Shredding the Master Key](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../recover_key.htm#recover_key).

On older Roving Edge devices (devices provisioned by Oracle), Oracle manages secret information on your Roving Edge Infrastructure devices, such as the superuser passphrase and unlock password, using a KMS-based master key. Oracle also uses a hardware security module to further protect this data. However, as an alternative to relying on Oracle's master key to manage this secret data, you can provide your own KMS-based master key from your own OCI tenancy.
Note  
  

You can only provide your own master key when creating the node resource. You can't edit an existing node resource to use your own master key the resource was originally created using an Oracle-provided master key.

## Writing the Master Key Policy

To use your own master key, you must first write a policy that authorizes this capability using one of the following methods:
- 

Using the Oracle Cloud Infrastructure Console:

Create the following policy:
```

```

where`master-key-id`is the master key OCID in the customer tenancy that is used to encrypt customer secret information like the superuser password and unlock passphrase. For example:
```

```

- 

Using the CLI:

Enter the following command:
```

```

For example:
```

```

## Selecting the Vault and Master Key

After you write the policy, select your vault and master key and the compartments in which they reside using one of the following methods:
- 

Using the Oracle Cloud Infrastructure Console:

When you create a Roving Edge Infrastructure node resource using the Create dialog box within the Oracle Cloud Infrastructure Console, the Encryption Key section appears. Here you can select one of the following options:
- 

Encrypt using Oracle-managed keys : Choose to have key encryption managed by the Oracle Cloud Infrastructure service. No further action is required.
- 

Encrypt using customer managed keys : Choose to provide your own encryption key.

If you choose to provide your own key, the Encryption Key section displays the additional fields:
- 

Vault Compartment : Select the compartment containing the vault you want from the list.
- 

Vault : Select one of the vaults from the list contained within the vault compartment you previously chose.
- 

Master Encryption Key Compartment : Select the compartment containing the master encryption key you want from the list.
- 

Master Encryption Key : Select one of the master encryption keys from the list within the master encryption key value you previously chose.
- 

Using the CLI:

Include the`master-key-id`option when you create the Roving Edge Infrastructure node resource. For example:
```

```

For example:
```

```
