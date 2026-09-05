# Creating Confidential Resource App
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_creating_confidential_resource_app.htm
- Fetched: 2026-09-05 02:34 CDT

# Creating Confidential Resource App

Create Confidential Resource Application for user authentication.

To use the OAuth2 protocol, you must create a confidential resource app in the identity provider. The confidential resource application has a 1:1 relationship with the external key manager and is used to replicate metadata about keys from the external key manager.
See[Adding a Confidential Application](https://docs.oracle.com/iaas/Content/Identity/applications/add-confidential-application.htm)for complete instructions. The mandatory fields (specific to External KMS) that you must provide for the confidential app are:
- Name: Name of the confidential resource application.
- Description: A short description about the app.
- Resource server configuration:
- Primary audience: Based on your TLS connectivity configuration, provide either the IP address of the external key manager or the API Gateway Private IP address. For example, https://10.101.111.10/.
- Scope:
- `oci_ekms`. Use to perform all operations in the external key manager platform.
- Client configuration
- `Client Credentials`. Enable the client credentials check box for the external key manager to authenticate with OCI KMS and in turn authorizing OCI KMS requests. Activate the application by selecting the activate button. You can see the client app id and the client secret on the home page.

Caution
