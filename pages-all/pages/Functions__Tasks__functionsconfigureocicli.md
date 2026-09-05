# Creating a Profile in the Oracle Cloud Infrastructure CLI Configuration File
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfigureocicli.htm
- Fetched: 2026-09-05 02:07 CDT

# Creating a Profile in the Oracle Cloud Infrastructure CLI Configuration File

Find out how to create a profile in the Oracle Cloud Infrastructure CLI configuration file for use with OCI Functions.

Before using OCI Functions, you must have an Oracle Cloud Infrastructure CLI configuration file that contains the credentials of the user account that you will be using to create and deploy functions. These user account credentials are referred to as a 'profile'. By default, the Oracle Cloud Infrastructure CLI configuration file is located at`~/.oci/config`.

If you are using Cloud Shell as your development environment, an`~/.oci/config`file with a suitable profile has already been created for you.

If you are using a local host as your development environment, follow the instructions in the[Functions QuickStart on Local Host](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhosts_topic_set_up_signing_key)to create a profile in the`~/.oci/config`file by copying and pasting a configuration file snippet. Note the following:
- You might already have a configuration file as a result of installing the Oracle Cloud Infrastructure CLI. However, you don't need to have installed the Oracle Cloud Infrastructure CLI in order to use OCI Functions.
- The`~/.oci/config`file can contain several profiles. If you already have an`~/.oci/config`file containing one or more profiles, you have to add a new profile to the existing file for the Oracle Cloud Infrastructure user who will be using OCI Functions to create and deploy functions.
- Change the name of the new profile you paste into the`~/.oci/config`file in the configuration file snippet, from`DEFAULT`to a name of your choosing. Note that the`~/.oci/config`file cannot contain two profiles with the same name.

This topic assumes you have already obtained an API signing key, as described in[Setting up an Oracle Cloud Infrastructure API Signing Key for Use with OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionssetupapikey.htm). When you have created a profile in the`~/.oci/config`file, go on to[Installing Docker for Use with OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinstalldocker.htm)
