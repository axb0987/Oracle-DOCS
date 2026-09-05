# Importing an RSA Key as an External Key Version Using a Script
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/importing_asymmetric_keys_topic_script_to_import_rsa_key_material_as_a_new_external_key_version.htm
- Fetched: 2026-09-05 02:35 CDT

# Importing an RSA Key as an External Key Version Using a Script

You can automate the import of AES key material as a new key version for an existing key.

Note  
  
If you're using MacOS or Linux, you'll need to install the[OpenSSL](http://www.openssl.org/)1.1.1 series to run commands. If you plan to use the RSA encryption algorithm that uses a temporary AES key, then you must also patch OpenSSL with a patch that supports it, see[Configuring OpenSSL to Wrap Key Material](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/to_configure_and_patch_openssl.htm). If you're using Windows, you'll need to install[Git Bash for Windows](https://git-scm.com/download/win)and run commands with that tool.
Open a command prompt, and then run the following script, replacing example file names and values as appropriate:

```

```
