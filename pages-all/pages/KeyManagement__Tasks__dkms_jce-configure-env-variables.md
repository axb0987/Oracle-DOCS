# Prerequisites for Keytool and Jarsigner
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-configure-env-variables.htm
- Fetched: 2026-09-05 02:34 CDT

# Prerequisites for Keytool and Jarsigner

Learn about the environment variables and command line flags used with Keytool and Jarsigner.

## Environment Variables

The following shell environment variables are used with the JCE provider:
- `LD_LIBRARY_PATH`: This variable must include the path to the directory that contains the`ocidkmsjca.so`file. Using this variable lets JCE find the native java libraries required to communicate with the HSM. For standard installations, the directory is`/opt/oci/hsm/lib`.
- `HSM_USER`: The crypto user name.
- `HSM_PASSWORD`: The password for the crypto user.

Prefix these values before commands, as the following example shows for the`importcert`command:
```

```

Optionally, you can create environment variables for your credentials if you don't want to append them each time. Don't export credentials as environment variables if other users would have access to your credentials. For example:
```

```

## Command Flags

Use the following flags with all Keytool and Jarsigner commands when using the Dedicated KMS JCE provider:
- `-J-cp -J <dedicated_kms_jce_jar_path>`: Adds the Dedicated KMS JCE JAR file to the class path when executing commands. See[To Install the Java Cryptography Extension (JCE) RPM File](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-installing.htm#dkms_install_jce_provider_linux)for more information about this file.
- 

`-storetype`: "DKKS" (`-storetype DKKS)`indicates that a DKKS keystore (Dedicated KMS KeyStore) is used.
- `-keypass:`Required by the keytool and jarsigner utilities, but not validated by the HSM. You can pass any value for this flag, but you must include the flag in the command.
- `-storepass:`
