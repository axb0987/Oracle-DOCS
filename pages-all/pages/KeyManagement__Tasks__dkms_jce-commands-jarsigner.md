# Jarsigner Commands
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-jarsigner.htm
- Fetched: 2026-09-05 02:34 CDT

# Jarsigner Commands

Learn about Jarsigner commands for the JCE Provider for Dedicated KMS.

When using the Jarsigner commands in this topic, ensure that you use the command flags discussed in[Prerequisites for Keytool and Jarsigner](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-configure-env-variables.htm).

## Signing a Jar File with a Key

This operation signs a JAR file with a key. The command is run using jarsigner with JCE.

[To sign a JAR file with a key stored in the HSM](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-jarsigner.htm#)

Command syntax:
```

```

If you receive a warning message stating "`The signer's certificate chain is invalid. Reason: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested targeThe signer's certificate chain is invalid`", the local keystore lacks a signed certificate.

You can resolve a certificate chain error with the following operations:
- 

Use the keytool program to generate a CSR corresponding to the key on the HSM.
```

```

Note the following:
- `-certreq`is used to generate a CSR.
- `-alias`indicates the alias for the specified key. By specifying this alias, if the key doesn’t exist in the keystore, the DKKS keystore searches the HSM for a label matching this alias.
- `-keyalg rsa -keysize 4096`specifies algorithm and key size for the key pair
- `-sigalg sha512withrsa -dname`provides the details for the CSR
- 

Use openssl to create a new self-signed local ca X.509 certificate (.crt file) and a RSA private key (.pem file).
```

```

- 

Insert the CA owner certificate into the keystore.
```

```

Note the following
- `-importcert`is used to import a certificate
- `-noprompt`instructs the program not to use prompts
- `-alias`specifies the alias that the CA certificate will be assigned
- `-file`is the file for the cert
- `-keypass`sets a password for the key
- 

List the certificate to ensure the local ca certificate is in the keystore:
```

```

The command returns output similar to the following:
```

```

- 

Using openssl, create an X.509 certificate with the generated CSR and local ca Crt. Then set the serial number for the new cert:
```

```

- 

Using keytool, import the &lt;output-crt&gt; .crt file into the keystore:
```

```

- 

Confirm that the certificate was successfully imported:
```

```

The program returns output similar to the following:
```

```

Tip  
  
Signing a jar file with a new key ensures that the signing operation doesn't produce a certificate chain error, because the new key's certificate is added to the local keystore during creation. Use the instructions in[Generate Key Pair](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-keytool.htm#dkms_jce_commands_keytool_generate_key_pair)to create a new key with keytool.

## Verifying the JAR File Signing Details

Use the`-verify`flag to verify the signing details of a signed JAR file, including which key was used to sign the file. The command is run using jarsigner with JCE.

[To verify the signed JAR file with the key](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-commands-jarsigner.htm#)

Command syntax:
```

```
