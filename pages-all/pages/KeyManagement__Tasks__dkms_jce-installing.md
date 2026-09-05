# Installing the JCE Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_jce-installing.htm
- Fetched: 2026-09-05 02:34 CDT

# Installing the JCE Provider

Learn how to install the Java Cryptography Extension (JCE) on a Linux instance for OCI' Dedicated Key Management (DKMS).

## Supported Platforms

- Oracle Linux 7 (OL7)
- Oracle Linux 8 (OL8)
- Oracle Linux 9 (OL9)

## Supported JDKs

- OpenJDK 8
- OpenJDK 11
- OpenJDK 17

## To Install the Java Cryptography Extension (JCE) RPM File

Use yum to install the`oci-hsm-jce`package, using the following command:

```

```

To confirm the installation, run the following command:

```

```

The installer copies the following files to your system:
- 

A JCE jar file. For example:`/opt/oci/hsm/lib/oci-dkms-jce- <version> -with-dependencies.jar`

Important: This jar must be included in the application classpath.
- 

A shared library (.so) file. For example:`/opt/oci/hsm/lib/libocidkmsjca.so`

Important: This library must be included in the`LD_LIBRARY_PATH`environment variable.
- javadocs. For example:`/opt/oci/hsm/lib/oci-dkms-jce- <version> -javadoc.jar`
- A config file to configure log level and log location:`/opt/oci/hsm/data/jcenative.cfg`
Note  
  
If you need to remove the`oci-hsm-jce`package, see[Uninstalling the Java Cryptography Extension (JCE)](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_uninstall_jce_provider_linux.htm)
