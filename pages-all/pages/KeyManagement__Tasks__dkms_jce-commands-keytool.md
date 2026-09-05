# Keytool Commands
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm
- Fetched: 2026-09-05 02:34 CDT

# Keytool Commands

Learn about KeyTool commands for the JCE Provider for Dedicated KMS.

When using the keytool commands in this topic, ensure that you use the command flags discussed in[Prerequisites for Keytool and Jarsigner](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-configure-env-variables.htm).

## Generate Key Pair

Use the`-genkeypair`flag to generate 1 private key and 1 public key in the DKMS HSM using keytool with JCE. The key is also stored in the local keystore by this operation.

[To generate a key pair](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#)

Important: When you use the`keytool`command to generate a key pair or import an existing keystore, your Java Security configuration ensures that a public and private key are generated in the HSM card. If you're using the`java.security`file for this configuration, the OCI Dedicated KMS provider must be specified as priority 2 in the file for key pairs to be generated in the HSM.

Alternately, in the current directory, create a Java Security Override File file and add the OCI Dedicated KMS provider in the second position as`security.provider.2`. When executing a Keytool command, use the following option to specifiy the Java Security Override file:
```

```

See[Add the JCE Provider to Java Security](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-configure.htm#dkms_jce_configure_java_sec_file)for more information on configuring Java Security.
Tip  
  
The generated key pair can't be found using an alias in the Key Management Utility. Optionally, you can list keys before and after key generation to identify the new key in the HSM. This lets you easily delete the key in the HSM if you need to do so. Before creating a key pair, sign in to the HSM and create a list of existing handles. Then create a list after creating the key pair to find the handle of the new key pair. See[Identifying the Handle of a New Key Pair or Secret Key in the HSM](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#dkms_jce_commands_keytool_identify_handle)for instructions.

Command syntax:
```

```

## Generate Secret Key

Use the`-genseckey`flag in the Key Management Utility with JCE .to perform this operation. This operation generates 1 secret key in the HSM.

[To generate a secret key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#)

Important  
  
The secret key can't be found using an alias in the Key Management Utility. Before creating a secret key, sign in to the HSM and create a list of existing handles. You can use this list after creating the key pair to find the handle of the new secret key. See[Identifying the Handle of a New Key Pair or Secret Key in the HSM](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#dkms_jce_commands_keytool_identify_handle)for instructions.

Command syntax:
```

```

## Identifying the Handle of a New Key Pair or Secret Key in the HSM

New key pairs or secret keys created in the HSM cannot be found using an alias in the Key Management Utility. You can find the handle of a new key pair or secret key by comparing a list of all handles before a key pair or secret key is generated with a second list of all handles created after a key pair or secret key is generated. The difference between the two lists shows the newly created handle for the key pair or secret key.

[To identify the handle of the new key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#)

- [Sign in to the HSM](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_key_mgmt_login.htm)with the Key Management Utility.
- 

Run the following command to find and save a list of the existing handles:

```

```

For the &lt;key-type&gt; , valid values are: 2 = public 3 = private 4 = secret. See[Finding a Single Key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_key_mgmt_find_a_single_key.htm)for more information.
- Generate a key pair or secret key. See[Generate Key Pair](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#dkms_jce_commands_keytool_generate_key_pair)and[Generate Secret Key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#dkms_jce_commands_keytool_generate_secret_key)for instructions.
- Repeat steps 1 and 2 and use the`findKey -c 4`command to find and save a list of the handles in the HSM. The new list includes the handle for the newly generated key pair or secret key.
- Perform a diff operation on the two lists to find new handle.

## Deleting a Key

Use the instructions in the following expandable section to delete keys from the local keystore and the HSM.

[To delete a key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#)

- 

Run the following keytool command to delete the key in the local keystore:
```

```

- 

To delete a key in the HSM, run the following command in the Dedicated Key Management utility:

```

```

See[Deleting a Key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_key_mgmt_delete_key.htm)for more information:

## Generating a Certificate Signing Request (CSR) with Keytool

Use the`-certreq`flag to generate a certificate signing request (CSR) using a key in the HSM. The command is run using the keytool utility with JCE.

[To generate a CSR](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#)

Run the following command to generate a CSR using a key in the HSM:

```

```

## Importing a Cert Into a Keystore

Use the`-importcert`flag to import a cert into the local keystore. The command is run using the keytool with JCE.

[To import a cert into a keystore](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#)

Command syntax:
```

```

## Importing a Java Keystore Into the HSM

Use the`-importkeystore`flag to import all keys in a keystore into the HSM. The command is run using keytool with JCE.

[To import keystore into the HSM](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#)

Important:
- 

When you use the`keytool`command to generate a key pair or import an existing keystore, your Java Security configuration ensures that a public and private key are generated in the HSM card. If you're using the`java.security`file for this configuration, the OCI Dedicated KMS provider must be specified as priority 2 in the file for key pairs to be generated in the HSM.

Alternately, in the current directory, create a Java Security Override File file and add the OCI Dedicated KMS provider in the second position as`security.provider.2`. When executing a Keytool command, use the following option to specify the Java Security Override file:
```

```

See[Add the JCE Provider to Java Security](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-configure.htm#dkms_jce_configure_java_sec_file)for more information on configuring Java Security.
- If you import a keystore with 2 or more keys into the HSM, you can't identify the handle of the keys using the method described in[Identifying the Handle of a New Key Pair or Secret Key in the HSM](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#dkms_jce_commands_keytool_identify_handle), and you can't reference the keys in the Key Management Utility using an alias.

Command syntax:
```

```

## Initializing a Keystore

If you don't have an empty initialized keystore, you can create one by performing the following operations:
- 

The keytool program can't create an empty DKKS keystore, but you can use keytool to create a keystore as part of a key generation operation. After you generate a key with keytool, you can delete the key, and the initialized keystore remains available to you.

Use the instructions in[Generate Key Pair](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#dkms_jce_commands_keytool_generate_key_pair)and[Identifying the Handle of a New Key Pair or Secret Key in the HSM](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#dkms_jce_commands_keytool_identify_handle)to generate a key pair that can be identified by a handle. When you generate this key pair, the keytool utility creates an initialized keystore that you can use for future operations.
- Delete the unnecessary key pair from the HSM using the instructions in[Deleting a Key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#dkms_jce_commands_keytool_delete_key)
