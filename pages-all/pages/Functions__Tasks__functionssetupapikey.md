# Setting up an Oracle Cloud Infrastructure API Signing Key for Use with OCI Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionssetupapikey.htm
- Fetched: 2026-09-05 02:09 CDT

# Setting up an Oracle Cloud Infrastructure API Signing Key for Use with OCI Functions

Find out how to set up an Oracle Cloud Infrastructure API signing key for use with OCI Functions.

Before using OCI Functions, you have to set up an Oracle Cloud Infrastructure API signing key.

If you are using Cloud Shell as your development environment, an Oracle Cloud Infrastructure API signing key has already been set up for you.

If you are using a local host as your development environment and your user account doesn't already have an Oracle Cloud Infrastructure API signing key, follow the instructions in[Functions QuickStart on Local Host](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhosts_topic_set_up_signing_key)to set up an API signing key. Note that if the ~/.oci directory already exists and already contains a private key file and public key file, there's no need to create new private and public key files. Instead, follow the instructions to upload or paste an API key in[To add an API signing key](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm#upload_key), and obtain a configuration file snippet containing a fingerprint.

If you are using a local host as your development environment and your user account already has an API signing key, go straight to[Creating a Profile in the Oracle Cloud Infrastructure CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfigureocicli.htm).
