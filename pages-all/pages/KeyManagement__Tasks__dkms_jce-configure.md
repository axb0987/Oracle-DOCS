# Configuring JCE
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-configure.htm
- Fetched: 2026-09-05 02:34 CDT

# Configuring JCE

Use the information in the following topics to configure the Dedicated Key Management JCE provider.

## Setting the Environment Variable for the JCE Provider

Set the following environment variable to use the JCE Provider:

`LD_LIBRARY_PATH`: This variable must include the path to the directory that contains the`ocidkmsjca.so`file. Using this variable lets JCE find the native java libraries required to communicate with the HSM. For standard installations, the directory is`/opt/oci/hsm/lib`.

## Add the JCE Provider to Java Security

You must add the JCE provider to the Java security configuration for your system using either of the methods described in this section.

[To edit the Java Security file](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-configure.htm#)

In the JAVA_HOME, add the OCI Dedicated KMS security provider to the end of the list of security providers. The provider entry is the following:

```

```

- 

Open the java.security file in a editor. For example, run this command to open the file in the VIM editor:

```

```

- 

Add the entry to the end of the list of security providers in the file. In the following example, the entry is added as`security.provider.13`:
```

```

[To dynamically load the JCE provider in Java applications](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-configure.htm#)

Use the`addProvider`method in the Security Java class to add the JCE Provider, as follows:
```

```

See[addProvider](https://docs.oracle.com/javase/8/docs/api/java/security/Security.html#addProvider-java.security.Provider-)in the Java documentation for more information.

## Authentication

Users are authenticated for login to the HSM by credentials that are retrieved from several sources in a specific order of priority. If valid credentials are found in any source, the login is completed. If no valid credentials are found, the login fails.

### Credential Sources and Priority Order

Login credentials are provided by following mechanisms:
- 

CallbackHandler: If this is provided, it retrieves credentials dynamically. For example:
```

```

- 

HsmCredentials.properties file: The application checks for a properties file named`HsmCredentials.properties`in the classpath. If the file exists and contains valid credentials, they're used for authentication. This file must contain the following:
- HSM_USER = crypto_user
- HSM_PASSWORD = cupassword
- 

Java system properties: If the credentials aren't found in the properties file, the Java System properties are checked. The`HSM_USER`, and`HSM_PASSWORD`values are expected to be set as system properties. You can set these using`-D`flags when running java applications. For example
```

```

- 

Operating System environment variables (lowest priority): If the credentials aren't found in Java system properties,they can be retrieved from environment variables, if the environment variables are set. Set`HSM_USER`, and`HSM_PASSWORD`values as environment variables, then export them as shown in the following example:
```

```
