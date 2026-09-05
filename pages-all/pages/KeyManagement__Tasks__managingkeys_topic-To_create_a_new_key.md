# Creating a Master Encryption Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm
- Fetched: 2026-09-05 02:35 CDT

# Creating a Master Encryption Key

Learn how to create a master encryption key in OCI's Key Management service.

Note the following when creating master encryption keys:
- 

Auto-rotation: When you create a master encryption key in a virtual private vault, you have the option of enabling automatic key rotation. See the[Automatic Key Rotation](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Concepts/keyoverview.htm#concepts__automatic-key-rotation-overview-section)section of the[Vault and Key Management Concepts](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Concepts/keyoverview.htm#concepts)topic for complete details. See[Enabling and Updating Auto Key Rotation](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/tasks_tasks_managingkeys_topic_edit_auto_key_rotation.htm)for instructions on updating auto-rotation settings.
- 

Available algorithms: You can select from the following algorithms when creating a key:
- AES : Advanced Encryption Standard (AES) keys are symmetric keys that you can use to encrypt data at rest.
- RSA : Rivest-Shamir-Adleman (RSA) keys are asymmetric keys, also known as key pairs that consists of a public key and a private key. You can use them to encrypt data in transit, to sign data, and to verify the integrity of signed data.
- ECDSA : Elliptic curve cryptography digital signature algorithm (ECDSA) keys are asymmetric keys that you can use to sign data and to verify the integrity of signed data.

For more information on keys in OCI's Key Management service, see[Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Concepts/keyoverview.htm#concepts__keys)in the[Vault and Key Management Concepts](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Concepts/keyoverview.htm#concepts)topic.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm#)
- 

- On the Master Encryption Keys list page for the vault you're using, select Create Key . If you need help finding the list page, see[Listing Keys](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_a_list_of_keys.htm).
- Select a compartment to create the key.
- For Protection Mode , select one of the following options:

- HSM : Select this option to create a master encryption key that's stored and processed on a hardware security module (HSM).
- Software: Select this option to create a master encryption key that's stored and processed on a server.

You can't change a key's protection mode after you create it. For more information about keys, including information about key protection modes, see[Vault and Key Management Concepts](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Concepts/keyoverview.htm#concepts).
- Enter a name to identify the key. Avoid entering confidential information.
- For Key Shape: Algorithm , select one of the following algorithms:

- AES : Advanced Encryption Standard (AES) keys are symmetric keys that you can use to encrypt data at rest.
- RSA : Rivest-Shamir-Adleman (RSA) keys are asymmetric keys, also known as key pairs that consists of a public key and a private key. You can use them to encrypt data in transit, to sign data, and to verify the integrity of signed data.
- ECDSA : Elliptic curve cryptography digital signature algorithm (ECDSA) keys are asymmetric keys that you can use to sign data and to verify the integrity of signed data.
- RSA only. If you selected AES or RSA, select the corresponding key shape length, in bits.
- ECDSA only. If you selected ECDSA, select a value for Key Shape: Elliptic Curve ID .
- Imported keys only. To create a key by importing a publicly wrapped key, select Import External Key and provide the following details:

- Wrapping Algorithm: Select RSA_OAEP_AES_SHA256 (RSA-OAEP with an SHA-256 hash for a temporary AES key).
- External Key Data Source: Upload the file that contains the wrapped RSA key material.
- Optional. Select Auto rotation to enable auto key rotation. Note that you can edit auto-rotation settings after the key is created.
- For auto-rotation only. In the Auto-rotation Schedule section, provide the following details:

- Start date: Use the calendar icon to select a date to start the key rotation schedule. The rotation happens on or before the scheduled date. For example, if you create a key today or update an existing key, and schedule the auto rotation start date as April 10 with a predefined interval of 90 days, then auto rotation starts on or before July 10 (April 10 + 90 days).
Note  
  
KMS ensures automatic rotation happens on or before the conclusion of the rotation interval. Rotation might start up to a few days before the scheduled interval.
- Rotation interval: Select a predefined interval within which the keys must be rotated. By default, the interval is set as 90 days.
- Custom: Optional. Select this option to set a custom rotation interval between 60 to 365 days.
- To apply tags, select Tags .
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create Key .
- 

Use the[oci kms management key create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/key/create.html)command and required parameters to create a master encryption key:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[CreateKey](https://docs.oracle.com/iaas/api/#/en/key/latest/KeyVersion/CreateKeyVersion)API with the Management Endpoint to create a new master encryption key.
Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
