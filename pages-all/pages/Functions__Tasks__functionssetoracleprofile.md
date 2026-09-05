# Setting the Context for the Fn Project CLI Using the oracle.profile Parameter
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionssetoracleprofile.htm
- Fetched: 2026-09-05 02:09 CDT

# Setting the Context for the Fn Project CLI Using the oracle.profile Parameter

Find out how to set the context for the Fn Project CLI using the oracle.profile parameter for use with OCI Functions.

Before using OCI Functions, you have to configure the Fn Project CLI to use the new profile you added to the Oracle Cloud Infrastructure CLI configuration file`~/.oci/config`(see[Creating a Profile in the Oracle Cloud Infrastructure CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfigureocicli.htm)). The profile you added contains the credentials of the user account you'll be using to create and deploy functions.

Note that unless you specify otherwise, the Fn Project CLI will attempt to use a profile in the`~/.oci/config`file named`default`.

If you are using Cloud Shell as your development environment, the Fn Project CLI has already been configured for you to use the profile in the Oracle Cloud Infrastructure CLI configuration file.

The instructions in this topic assume:
- you are not using Cloud Shell as your development environment
- you are using Linux
- you have already completed the steps in[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatefncontext.htm)

To configure the Fn Project CLI to use the profile you've created for use with OCI Functions:
- 

Log in to your development environment as a functions developer.
- 

In a terminal window, configure the Fn Project CLI context with the name of the profile you've created for use with OCI Functions by entering:

```

```

For example:

```

```

When you have completed the steps in this topic, go on to[Generating an Auth Token to Enable Login to Oracle Cloud Infrastructure Registry](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsgenerateauthtokens.htm)
