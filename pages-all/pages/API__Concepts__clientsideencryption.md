# Client-Side Encryption
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/clientsideencryption.htm
- Fetched: 2026-09-05 01:35 CDT

# Client-Side Encryption

The Oracle Cloud Infrastructure SDK for Python and SDK for Java support Client Side Encryption, which encrypts your data on the client side before storing it locally or using it with other Oracle Cloud Infrastructure services.

By default, the SDK generates a unique data key for each data object that it encrypts. Data is encrypted using a secure, authenticated, symmetric AES/GCM key algorithm with a 256-bit key length.

To use client-side encryption, you must create a master encryption key (MEK) using the Key Management Service. This can be done using the[CreateKey](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/CreateKey)or[ImportKey](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/ImportKey)operations.

The MEK is used to generate a Data Encryption Key (DEK) to encrypt each payload. A encrypted copy of this DEK (encrypted under the MEK) and other pieces of metadata are included in the encrypted payload returned by the SDKs so that they can be used for decryption.

## Java Prerequisites

The[unlimited policy files for earlier releases](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)are required only for JDK 8, 7, and 6 updates earlier than 8u161, 7u171, and 6u16. For those versions and later the policy files are included but not enabled by default.

Current versions of the JDK do not require these policy files. They are provided here for use with older versions of the JDK. JDK 9 and later ship with the unlimited policy files and use them by default.

## Examples

The following code example show how to encrypt a string:

### Java

```

```

### Python

```

```

The following examples show how to encrypt a file stream:

### Java

```

```

### Python

```

```
