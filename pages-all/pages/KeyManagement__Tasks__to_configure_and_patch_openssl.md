# Configuring OpenSSL to Wrap Key Material
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/to_configure_and_patch_openssl.htm
- Fetched: 2026-09-05 02:36 CDT

# Configuring OpenSSL to Wrap Key Material

Learn how to patch OpenSSL so that you can wrap key material using`RSA_OAEP_AES_SHA256`.

The OpenSSL -id-aes256-wrap-pad cipher compatible with`RSA_AES_KEY_WRAP`isn't enabled by default in the OCI CLI. Patch OpenSSL to enable the envelope wrapping that's needed for the`CKM_RSA_AES_KEY_WRAP`mechanism.
Note  
  

For the "Bring your own key (BYOK)" scenario, you must patch the OpenSSL for RSA_OAEP_AES_SHA256 wrapping.

Perform the following steps to download, compile, and run a new local copy of OpenSSL v1.1.1d using the CLI, without altering the default installation of OpenSSL in the system:

- Create directories to store the latest OpenSSL binaries in`/root/build`.

```

```

- Run the following command and note the OpenSSL version:

```

```

- Note the latest OpenSSL version at[https://www.openssl.org/source/](https://www.openssl.org/source/).
- Download and unpack the libraries.
Replace openssl-1.1.1d.tar.gz with the latest version from step[3](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/to_configure_and_patch_openssl.htm#to_configure_and_patch_openssl__openssl_version).

```

```

- Install the patch, make gcc tools to patch, and then compile the binaries.

```

```

- Run the following commands:

Note  
  
You might need to update these commands for newer versions of OpenSSL.

```

```

Confirm successful patching if response is similar to the following:

```

```

- Compile the`enc.c`file.

Note  
  
Compiling might take several minutes for each command.

```

```

You have successfully installed the latest version of OpenSSL. This version is dynamically linked to libraries in the`$HOME/local/ssl/lib/`directory, and cannot be run directly. Set the environment variable`LD_LIBRARY_PATH`to ensure that the associated libraries are available to OpenSSL.
- Create a script named`openssl.sh`that loads the`$HOME/local/ssl/lib/`path before running the binary. This makes it easier to run OpenSSL multiple times.

```

```

- Set the execute bit on the script.

```

```

- Start OpenSSL with the following command:

```

```
