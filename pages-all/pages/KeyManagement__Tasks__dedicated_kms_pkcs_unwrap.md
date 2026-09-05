# Unwrapping a Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_pkcs_unwrap.htm
- Fetched: 2026-09-05 02:33 CDT

# Unwrapping a Key

Configure command to unwrap a key.

The`unwrapKey`command enables you to unwrap a sensitive key on an HSM. You can identify the key by its handle.

Open a command prompt and run`unwrapKey`command to unwrap sensitive keys on HSM. You can identify the key by its handle.

Syntax
```

```

Parameter Description
`-h`Displays this information
`-f`Specifies the path and name of the file that contains the wrapped key.
`-w`Specifies the wrapping key. enter the key handle of an AES key or RSA key value on the HSM.
-m Specifies the value representing the wrapping mechanism.
-out Specifies the path and output file name.
-t Specifies the hashing algorithm.
-nex Makes the key nonextractable. cDefault value is the key is extractable.
-noheader The initialization vector (IV) (hex value).
-l Specifies the label to be added to the unwrapped key.
-i Specifies the unwrapping initialization vector (IV) to be used.
-kc Specifies the class of the key to be unwrapped. Acceptable values are 3 = private key from a public-private key pair and 4 = secret (symmetric) key.
-kt Specifies the type of key to be unwrapped.
-sess Creates a key that is available only in the current session. The key cannot be recovered after the session ends
-iv_file The file in which you want to write the IV value obtained in response.
-attest Runs an check that verifies the firmware on which the cluster runs has not been tampered.
-min_sev Specifies the minimum number of HSMs on which the key is synchronized before the value of the -timeout parameter expires. Default value is 2.
-time_out Specifies how long (in seconds) the command waits for a key to be synchronized to the number of HSMs specified by the min_srv parameter. Default value is no timeout.
-u List of users to share the key (comma-delimited list) (optional). Example
```

```
