# Dedicated KMS Keystores for JCE
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/dkms_jce_provider-keystore.htm
- Fetched: 2026-09-05 02:31 CDT

# Dedicated KMS Keystores for JCE

Learn about the keystores for the Dedicated KMS JCE provider.

The`KeyStore`Java class detailed in this topic is used to store your key data, and it correlates these with the key data stored in the HSM cluster. It also provides the functionality to store certificates in memory.

## Dedicated KMS KeyStore

`DedicatedKMSKeyStore`extends the[KeyStoreSpi](https://docs.oracle.com/javase/8/docs/api/java/security/KeyStoreSpi.html)Java class. Create a`DedicatedKmsKeyStore`object as follows:
```

```

This KeyStore provides the following functions:

Function Description
aliases Returns all the aliases found in the local memory-based store.
containsAlias Similar to`getKey`, this function first searches the local memory-based store, and then searches the HSM for a match on a specified alias.
deleteEntry Removes the specified alias from the local memory-based store. The key continues to live on the HSM. To delete a key in the HSM, use the function`destroy`under the`DedicatedKmsKey`class, or the[deleteKey](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/../Tasks/dedicated_kms_key_mgmt_delete_key.htm)command in the Key Management Utility.
getCertificate Retrieves the certificate for a specified alias.
getCertificateAlias Checks to see if a provided certificate matches any stored certificates in the local memory-based store.
getCertificateChain Retrieves a chain of certificates for a specified alias.
getCreationDate Returns the date a specified key was added to the local memory-based store.
getKey Retrieves the key associated with the specified alias from the keystore. The function first tries to retrieve the key from the local memory-based store. If the key isn't found, Dedicated KMS searches the Hardware Security Module (HSM) for a supported key type. Note that the HSM doesn't enforce unique key labels, so if multiple keys are found, a random non-public key is returned.
isCertificateEntry Indicates if a specified alias is associated with a certificate entry.
isKeyEntry Indicates if a specified alias is associated with a key entry. Similar to`getKey`, this function first searches the local memory-based store, and then searches the HSM for a match on a specified key entry.
load Loads the keystore from the specified input stream.
setCertificateEntry Assigns a specified certificate to an alias and stores the certificate in the local memory-based store.
setKeyEntry with Key object Assigns a specified key to the an alias and stores the key in the local memory-based store and in the HSM.
setKeyEntry with byte[] Key This API isn't supported.
size Gets the number of entries in the local memory-based store.
store Stores the keystore to the specified output stream.

## Dedicated KMS Extended KeyStore

`DedicatedKmsExtendedKeystore`extends the DedicatedKmsExtendedKeyStoreSpi Java class. Create a`DedicatedKmsExtendedKeyStore`object as follows:
```

```

This KeyStore provides the following functions:

Function Description
findKey Finds a random key in the hardware security module (HSM) that matching the specified alias, key type (for example, RSA, EC, AES, or DES3) and key object type (for example,`PUBLIC_KEY`,`PRIVATE_KEY`, or`SECRET_KEY`)
findKeys Finds all keys in the hardware security module (HSM) that match the specified alias, key type (for exmaple, RSA, EC, AES, or DES3) and key object type (for example,`PUBLIC_KEY`,`PRIVATE_KEY`, or`SECRET_KEY`
