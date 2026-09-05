# Applying RSA-OAEP with AES to Wrap the Key Material of an Asymmetric Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importing_asymmetric_keys_topic_to_apply_rsa_oaep_with_aes_to_wrap_the_key_material.htm
- Fetched: 2026-09-05 02:35 CDT

# Applying RSA-OAEP with AES to Wrap the Key Material of an Asymmetric Key

Learn how to apply RSA-OAEP with AES to wrap key material in the OCI Key Management service .

## Using the CLI

This section describes how to apply RSA-OAEP with AES to wrap the key material command interface.

Open a command prompt and run the following commands to wrap the RSA key material using RSA-OAEP with a temporary AES key. Replace example file names and values as appropriate.

- Generate a temporary AES key:
```

```

- Wrap the temporary AES key with the public wrapping key using RSA-OAEP with SHA-256:
```

```

- Generate hexadecimal of the temporary AES key material:
```

```

- If the RSA private key you want to import is in PEM format, convert it to DER:
```

```

- Wrap your RSA private key with the temporary AES key:
```

```

- Create the wrapped key material by concatenating both wrapped keys:
```

```

Note  
  

If you import the key using the command interface, then you must apply base64 encoding on the wrapped key material. After applying bas64 encoding, you must import the wrapping key, for more information, see[import](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/importing_asymmetric_keys_topic_to_import_the_key_material_as_a_new_external_key.htm)steps. If you import the key material using the Console, then you can directly import the wrapping key material without base64 encoding.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/)
