# Re-encrypting an Object Storage Object
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_reencrypt_an_object.htm
- Fetched: 2026-09-05 02:51 CDT

# Re-encrypting an Object Storage Object

Re-encrypt an object's data encryption keys with a different master encryption key in an Object Storage bucket.

You can re-encrypt the data encryption keys that encrypt an object by re-encrypting the object's data encryption keys with the latest version of the master encryption key assigned to the bucket. This re-encryption is possible whether it's an Oracle managed key or a key in a vault that you manage. You can also re-encrypt the object's data encryption keys with a different key in a vault or a different SSE-C key. If you use SSE-C keys, you must provide the SSE-C key during the object decryption and subsequent re-encryption process, as appropriate.

To re-encrypt an object, you need OBJECT_READ and OBJECT_OVERWRITE permissions. To re-encrypt an object that you encrypted with an SSE-C key, you must use the CLI to provide the SSE-C key to Object Storage for use during decryption and re-encryption, as appropriate.

If you receive an error, verify that you have the correct permissions. If you have access to the object, confirm that the object exists and hasn't recently been deleted. If you have permissions and the object exists, also confirm whether the object is encrypted with an SSE-C key.

For more information, see[Object Storage Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/encryption.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_reencrypt_an_object.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_reencrypt_an_object.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_reencrypt_an_object.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Objects .
The Objects tab opens. All objects in the selected bucket are displayed in a table.
- From the Actions menu for the object you want, select Re-encrypt .
The Re-encrypt object panel opens.
- Perform one of the following tasks, depending on whether the key assigned to the bucket is an Oracle-managed key or a key in a vault that you manage:

- For buckets encrypted with an Oracle-managed key, you can re-encrypt the object with the latest version of that key by selecting Use the key assigned to the bucket . Or, you can re-encrypt the object with a key in a vault by selecting Use a customer-managed key and then choosing a key from a compartment and vault that you have access to.
- For buckets encrypted with a customer-managed key, you can re-encrypt the object with the latest version of that key by selecting Use the key assigned to the bucket . Or, you can re-encrypt the object with a different Vault key by selecting Use a different customer-managed key and then choosing another key from a compartment and vault that you have access to.
- Select Re-encrypt .
- 

Use the[oci os object reencrypt](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/reencrypt.html)command and required parameters to re-encrypt an object's data encryption keys with the latest key version of the key assigned to the bucket:

```

```

For example:
```

```

The object's data encryption keys are re-encrypted with no further information returned.

## Encryption Using an SSE-C Key

You can re-encrypt an object's data encryption keys with an SSE-C key .

```

```

For example:

```

```

If the object's data encryption keys are currently encrypted with an SSE-C key, include the`source-encryption-key-file`parameter to also provide the name of the file that contains the base64-encoded string of the AES-256 source encryption key to first decrypt the object.

```

```

For example:
```

```

If the object is currently encrypted with an SSE-C key, and you want to encrypt the object's data encryption keys with a different SSE-C key, provide the file name of each key.

```

```

For example:

```

```

## Encryption Using a Vault Key

To re-encrypt an object's data encryption keys with a specific Vault key, include the`kms-key-id`parameter.

```

```

For example:

```

```

## Encryption Using Both SSE-C and Vault Keys

If the key is encrypted with an SSE-C key and you are re-encrypting an object's data encryption keys with a specific Vault key, you must include the`source-encryption-key-file`parameter that provides the name of the file that contains the base64-encoded string of the AES-256 source encryption key to first decrypt the object.

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ReencryptObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ReencryptObject)operation to re-encrypt an object's data encryption keys with the latest key version of the key assigned to the bucket.

Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API:
```

```

The object name is everything after the`/o/`
