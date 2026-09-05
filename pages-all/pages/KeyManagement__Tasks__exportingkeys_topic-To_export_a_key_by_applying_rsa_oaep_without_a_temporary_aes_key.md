# Exporting a Software-protected key by Applying RSA-OAEP without Temporary AES Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/exportingkeys_topic-To_export_a_key_by_applying_rsa_oaep_without_a_temporary_aes_key.htm
- Fetched: 2026-09-05 02:35 CDT

# Exporting a Software-protected key by Applying RSA-OAEP without Temporary AES Key

Export a software-protected master encryption key by applying RSA-OAEP without a temporary AES key using the bash command line environment.

Note  
  
If you're using MacOS or Linux, you'll need to install the[OpenSSL](http://www.openssl.org/)1.1.1 series to run commands. If you plan to use the RSA encryption algorithm that uses a temporary AES key, then you must also patch OpenSSL with a patch that supports it, see[Configuring OpenSSL to Wrap Key Material](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/to_configure_and_patch_openssl.htm). If you're using Windows, you'll need to install[Git Bash for Windows](https://git-scm.com/download/win)and run commands with that tool.

## Using the CLI

The following example script transforms the software-protected master encryption key through a mechanism called Optimal Asymmetric Encryption Padding (OAEP). OAEP is commonly used with the RSA encryption algorithm (RSA-OAEP). The Vault service supports RSA-OAEP with a SHA-256 hash.

The script wraps the software-protected master encryption key with the provided public RSA wrapping key, and then unwraps and exports it with the private RSA wrapping key. Only the possessor of the private RSA wrapping key can decrypt the wrapped master encryption key.

To export a software-protected master encryption key, open a command prompt, and then run the following script, replacing example file names and values as appropriate:

```

```
