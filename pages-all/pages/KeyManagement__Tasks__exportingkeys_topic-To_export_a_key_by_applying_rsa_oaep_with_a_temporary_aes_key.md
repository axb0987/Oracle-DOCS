# Exporting a Software-protected key by Applying RSA-OAEP with Temporary AES Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/exportingkeys_topic-To_export_a_key_by_applying_rsa_oaep_with_a_temporary_aes_key.htm
- Fetched: 2026-09-05 02:35 CDT

# Exporting a Software-protected key by Applying RSA-OAEP with Temporary AES Key

Export a software-protected master encryption key by applying RSA-OAEP with a temporary AES key using the using the bash command line environment.

Note  
  
If you're using MacOS or Linux, you'll need to install the[OpenSSL](http://www.openssl.org/)1.1.1 series to run commands. If you plan to use the RSA encryption algorithm that uses a temporary AES key, then you must also patch OpenSSL with a patch that supports it, see[Configuring OpenSSL to Wrap Key Material](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/to_configure_and_patch_openssl.htm). If you're using Windows, you'll need to install[Git Bash for Windows](https://git-scm.com/download/win)and run commands with that tool.

## Using the CLI

The following example script invokes the RSA AES key wrap mechanism to generate a temporary AES key that wraps and unwraps the exportable key material. The process by which you transform the temporary AES key is called Optimal Asymmetric Encryption Padding (OAEP). OAEP is commonly used with the RSA encryption algorithm (RSA-OAEP). The Vault service supports RSA-OAEP with a SHA-256 hash.

Applying OAEP with the RSA encryption algorithm (RSA-OAEP) with a SHA-256 hash to wrap the temporary AES key with the provided public RSA wrapping key generates a wrapped temporary AES key. The wrapped temporary AES key and the wrapped exportable key material are concatenated to produce blob output that jointly represents them and which only the possessor of the private RSA wrapping key can decrypt.

To export a software-protected master encryption key, open a command prompt, and then run the following script, replacing example file names and values as appropriate:

```

```
