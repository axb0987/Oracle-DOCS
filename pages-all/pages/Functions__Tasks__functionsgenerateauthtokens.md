# Generating an Auth Token to Enable Login to Oracle Cloud Infrastructure Registry
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsgenerateauthtokens.htm
- Fetched: 2026-09-05 02:08 CDT

# Generating an Auth Token to Enable Login to Oracle Cloud Infrastructure Registry

Find out how to generate an auth token to enable login to Oracle Cloud Infrastructure Registry for use with OCI Functions.

Before using OCI Functions, the user account you'll be using to create and deploy functions must have an Oracle Cloud Infrastructure auth token. You use the auth token as the password when logging Docker in to Oracle Cloud Infrastructure Registry

The instructions in this topic assume you have already completed the steps in[Setting the Context for the Fn Project CLI Using the oracle.profile Parameter](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionssetoracleprofile.htm).

If the user account already has an auth token, go straight on to[Starting Docker](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsstartdocker.htm). Otherwise, if the user account does not have an auth token, generate an auth token now.

To generate an auth token for the user account you'll be using to create and deploy functions:
- 

Sign in to the Console as a functions developer.
- In the navigation menu , select the Profile menu and then select User settings .
- On the Tokens and keys tab, go to the Auth tokens section and select Generate token .
- In the Generate token panel:
- Enter a meaningful description for the auth token. For example,`John's auth token for use with OCI Functions`. Avoid entering confidential information.
- Select Generate token . The new auth token is displayed. For example,`6aN___________6MqX`.
- Copy the auth token immediately to a secure location from where you can retrieve it later, because you won't see the auth token again in the Console.
- Close the Generate Token dialog.

When you have completed the steps in this topic, go on to[Starting Docker](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsstartdocker.htm)
