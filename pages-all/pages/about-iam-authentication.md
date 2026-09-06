# About Identity and Access Management (IAM) Authentication with Autonomous AI Database
- Source: https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-iam-authentication.html
- Fetched: 2026-09-05 18:57 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-iam-authentication.html#dcoc-content-body)

# About Identity and Access Management (IAM) Authentication with Autonomous AI Database

You can enable an Autonomous AI Database instance to use Oracle Cloud Infrastructure (IAM) authentication and authorization for users.

Note  
  
Note: Autonomous AI Database integration with Oracle Cloud Infrastructure IAM is supported in commercial regions with identity domains as well as in the legacy IAM, which does not include identity domains. IAM with identity domains was introduced with new Oracle Cloud Infrastructure tenancies that were created after November 8, 2021. Autonomous AI Database supports users and groups in default and non-default identity domains.

Oracle Cloud Infrastructure IAM integration with Autonomous AI Database supports the following:
- 

IAM Database Password Authentication
- 

Identity and Access Management (IAM) SSO Token Based Authentication

See[Authenticating and Authorizing IAM Users for Oracle Autonomous AI Databases](https://docs.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database/serverless/adbsb&id=DBSEG-GUID-466A8800-5AF1-4202-BAFF-5AE727D242E8)for complete details about the architecture for using IAM users on Autonomous AI Database.

## IAM Database Password Authentication

You can enable an Autonomous AI Database instance to allow user access with an Oracle Cloud Infrastructure IAM database password (using a password verifier).

Note  
  
Note: Any supported 12c and later database client can be used for IAM database password access to Autonomous AI Database.

An Oracle Cloud Infrastructure IAM database password allows an IAM user to log in to an Autonomous AI Database instance as Oracle AI Database users typically log in with a user name and password. The user enters their IAM user name and IAM database password. An IAM database password is a different password than the Oracle Cloud Infrastructure Console password. Using an IAM user with the password verifier you can login to Autonomous AI Database with any supported database client.

For password verifier database access, you create the mappings for IAM users and OCI applications to the Autonomous AI Database instance. The IAM user accounts themselves are managed in IAM. The user accounts and user groups can be in either the default domain or in a custom, non-default domain.

## Identity and Access Management (IAM) SSO Token Based Authentication

You can enable an Autonomous AI Database instance to use Oracle Cloud Infrastructure (OCI) Identity and Access Management (IAM) SSO tokens.

For token verifier database access, you create the mappings for IAM users and OCI applications to the Autonomous AI Database instance. The IAM user accounts themselves are managed in IAM. The user accounts and user groups can be in either the default domain or in a custom, non-default domain.

There are several ways a database client can obtain an IAM database token:
- 

A client application or tool can request the database token from IAM for the user and can pass the database token through the client API. Using the API to send the token overrides other settings in the database client. Using IAM tokens requires the latest Oracle Database client 19c (at least 19.16). Some earlier clients provide a limited set of capabilities for token access.
- 

If the application or tool does not support requesting an IAM database token through the client API, the IAM user can first use Oracle Cloud Infrastructure command line interface (CLI) to retrieve the IAM database token and save it in a file location. For example, to use SQL*Plus and other applications and tools using this connection method, you first obtain the database token using the Oracle Cloud Infrastructure (OCI) Command Line Interface (CLI). If the database client is configured for IAM database tokens, when a user logs in with the slash login form, the database driver uses the IAM database token that has been saved in a default or specified file location.
- 

A client application or tool can use an Oracle Cloud Infrastructure IAM instance principal or resource principal to get an IAM database token, and use the IAM database token to authenticate itself to an Autonomous AI Database instance.
- 

IAM users and OCI applications can request a database token from IAM with several methods, including using an API-key. See[Configuring a Client Connection for SQL*Plus That Uses an IAM Token](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/iam-access-database.html#GUID-6527F0AC-9402-49B8-9929-DCF576084FA4)for an example. See[About Authenticating and Authorizing IAM Users for an Oracle Autonomous AI Database](https://docs.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database/serverless/adbsb&id=DBSEG-GUID-CD09A907-0ABA-41D1-84C4-96DADF6BB99B)for a description of other methods such as using a delegation token within an OCI cloud shell.

- [About Identity and Access Management (IAM) Authentication with Autonomous AI Database](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-iam-authentication.html#GUID-CD33BEA1-4679-451C-AC54-D130C3C3FDEA)
- [IAM Database Password Authentication](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-iam-authentication.html#GUID-17A096C3-5F0F-4D07-98C4-2CD9D9915677)
- [Identity and Access Management (IAM) SSO Token Based Authentication](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-iam-authentication.html#GUID-83BC21EB-0D0B-44EA-9EB8-221F250D136E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
