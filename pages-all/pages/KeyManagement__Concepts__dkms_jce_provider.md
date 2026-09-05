# JCE Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/dkms_jce_provider.htm
- Fetched: 2026-09-05 02:31 CDT

# JCE Provider

Learn about the Java Cryptography Extension (JCE) provider for use with a Dedicated Key Management HSM cluster.

The Java Cryptography Extension (JCE) provider for Dedicated Key Management is an implementation of the[Java Cryptography Extension (JCE) provider framework](https://docs.oracle.com/en/java/javase/17/security/java-cryptography-architecture-jca-reference-guide.html). The JCE provider lets you perform cryptographic operations with the Java Development Kit (JDK) on your HSM. The provider offers seamless integration between Java-based applications and the HSM.

JCE provides a set of cryptographic APIs that enable developers to perform secure encryption, decryption, digital signing, and key management operations. Offloading these cryptographic tasks to the HSM cluster gives you superior performance and the highest level of security for sensitive data. Performing these operations on the HSM also improves efficiency by distributing the computational load. The JCE provider is thus ideal for performance-critical and security-sensitive applications.

## Topics

- [Installing the JCE Provider](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/../Tasks/dkms_jce-installing.htm)
- [Configuring JCE](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/../Tasks/dkms_jce-configure.htm)
- [Key Types and Algorithms](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/dkms_jce_provider-key_types_algorithms.htm)
- [Crypto Operations and Mechanisms](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/dkms_jce_provider-crypto_operations.htm)
- [Key Attributes for the JCE Provider](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/dkms_jce_provider-key_attributes.htm)
- [Dedicated KMS Keystores for JCE](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/dkms_jce_provider-keystore.htm)
- [Javadocs](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/dkms_jce_provider-javadocs.htm)
- [Using the JCE Provider with Keytool and Jarsigner](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/../Tasks/dkms_jce-using_keytool_and_jarsigner.htm)
