# Getting Started with the Identity Domains REST API
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-get-started.htm
- Fetched: 2026-09-05 02:17 CDT

# Getting Started with the Identity Domains REST API

The identity domains REST API securely manage resources, including identities and configuration data. Support for OpenID Connect allows integration with compliant applications and identity domains. The OAuth2 service provides an API infrastructure for authorization that supports a range of token grant types that enable you to securely connect clients to services.

The identity domains REST API supports SCIM 2.0 compliant endpoints with standard SCIM 2.0 core schemas and Oracle schema extensions to:
- 

Manage users, groups, and apps.
- 

Perform identity functions, including password generation and reset.
- 

Perform administrative tasks including bulk operations and job scheduling.
- 

Configure settings for an identity domain including multifactor authentication, branding, and notification templates.

This guide contains the following sections:
- [Endpoints Deprecation Notices](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-get-started.htm#DeprecatedEndpoints): Learn about endpoints deprecation notices for identity domains.
- [Quick Start](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-get-started.htm#QuickStart): Quickly get started with the identity domains REST API by completing prerequisites, installing curl, and setting up authorization to manage your identity domain resources such as users, groups, and applications.
- [API Rate Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../sku/overview.htm#api-rate-limits): Understand the rate limiting for APIs for different identity domain types.
- [Structuring Resource Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequestResponse.htm): Learn the guidelines for building send requests in an identity domain.
- [Using cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm): Learn how to use cURL to access the REST APIs.
- [Managing Authorization Using the API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-managing-authorization.htm): Learn how to use an OAuth client to access identity domains REST API. The identity domains REST API isn't accessible using only an identity domain username and password. To access the identity domains REST API, you need an OAuth2 access token or an API key to use for authorization.
- [API Use Cases](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-use-cases.htm): Step through typical use cases using the identity domain REST APIs.

The following resources aren't in this guide but are also available to you.

When using the identity domains user interface:
- To administer IAM in tenancies with identity domains, see[Oracle Cloud Infrastructure Identity and Access Management](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../home.htm).
- For user self-service instructions, such as setting up MFA, see the[IAM User Guide](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../using/aboutidentitydomains.htm).

When using the API or CLI:
- To manage identity domains (for example, creating or deleting a domain), see[IAM API](https://docs.oracle.com/iaas/api/#/en/identity/).
- To manage resources within an identity domain, for example, users, dynamic resource groups, groups, and identity providers, see[Identity Domains CLI](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/identity-domains.html#).

## Endpoints Deprecation Notices

Read the endpoint deprecation notices for identity domains in IAM.

To review details about Oracle Cloud Infrastructure breaking changes, such as deprecated features, deprecated APIs, and service behavior changes, see[IAM (Service Change Announcements)](https://docs.oracle.com/iaas/Content/servicechanges.htm#servicechanges_topic_IAM).

## Quick Start

Quickly get started with the identity domains REST API by completing prerequisites, installing curl, and setting up authorization to manage your identity domain resources such as users, groups, and applications.

### Prerequisites
- Buy an Oracle Cloud Subscription: See[Buy an Oracle Cloud Subscription](https://docs.oracle.com/iaas/Content/GSG/Tasks/buysubscription.htm).
- Activate your order: Set up your account or activate your order. See Activate Your Order from Your Welcome Email in[Buy an Oracle Cloud Subscription](https://docs.oracle.com/iaas/Content/GSG/Tasks/buysubscription.htm).
- Obtain the appropriate account credentials and authorization to access identity domain APIs from your identity domain administrator:
- 

To sign in to your identity domain. See your identity domain administrator to obtain your username, password, and identity domain name.
- 

To use the API without a user account. Administrators can use the identity domains API without a user account in the identity domain. To use the identity domains API without a user account, request a client ID and a client secret from the identity domain administrator.

### Step 1: Sign In to Your Identity Domain

After you activate your account, you're sent sign-in credentials and a link to the home page of your identity domain. Select the link in the email, and then enter the provided sign-in credentials. Your identity domain home page appears. See[Sign In to the Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm).

### Step 2: Install cURL

The examples within this document use the`cURL`command line tool to demonstrate how to access the identity domains REST API.

To connect securely to the server, you must install a version of cURL that supports SSL and provide an SSL certificate authority (CA) certificate file or bundle to authenticate against the Verisign CA certificate. For more information about:
- 

Using cURL, see[Using cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).
- 

Authorization, see[Managing Authorization Using the API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-managing-authorization.htm).
The following procedure demonstrates how to install cURL on a Windows 64-bit system.
- 

In a browser, navigate to the cURL home page at[http://curl.haxx.se/download.html](http://curl.haxx.se/download.html).
- 

On the cURL Releases and Downloads page, find the SSL-enabled version that corresponds to your OS, and then select the link to download the ZIP file.
- 

Install the software.
- 

Navigate to the cURL CA Certs page at[http://curl.haxx.se/docs/caextract.html](http://curl.haxx.se/docs/caextract.html), and then download the ca-bundle.crt SSL certificate authority (CA) certificate bundle into the folder where you installed cURL.
- 
Set the cURL environment variable:
- 

Open a command window.
- 

Navigate to the directory where you installed cURL.
- 

Set the cURL environment variable (CURL_CA_BUNDLE) to the SSLCA certificate bundle location. For example:`C:\curl> set CURL_CA_BUNDLE=ca-bundle.crt`.

### Step 3: Understand the Resource URL Format

You access the identity domains REST API using a URL, which includes the REST endpoint, the resource that you want to access, and any query parameters that you want to include in a request.

The basic endpoint for the identity domains REST API is:
```

```

See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for specific details on building these URLs.

### Step 4: Set Up Authorization

You need to generate the access token that you can then use to authorize requests that you send to the identity domains REST API. See[Managing Authorization Using the API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-managing-authorization.htm).

You're now ready to send requests to an identity domain using`cURL`.

### Step 5: Manage Your Identity Domain Resources

Begin using the REST API to manage overall identity domain configurations and identities and resources.

## API Rate Limits

Understand the rate limiting for APIs for different identity domain types.

Oracle APIs are subject to rate limiting to protect the API service usage for all Oracle's customers. If you reach the API limit for the identity domain type, then IAM returns a 429 error code.

### Rate Limits for all Identity Domain Types

API Group Per Free Oracle Apps Oracle Apps Premium Premium External User External Active User
AuthN second 10 50 80 95 90 90
AuthN minute 150 1000 2100 4500 3100 3100
BasicAuthN second 10 100 160 95 90 90
BasicAuthN minute 150 3000 4000 4500 3100 3100
Token Mgmt second 10 40 50 65 60 60
Token Mgmt minute 150 1000 1700 3400 2300 2300
Others second 20 50 55 90 80 80
Others minute 150 1500 1750 5000 4000 4000
Bulk second 5 5 5 5 5 5
Bulk minute 200 200 200 200 200 200
Import and export day 4 8 10 10 10 10
Import and export hour 2 3 3 3 3 3
Note  
  
The maximum number of Identity Propagation Trust objects that can be created is restricted to 30. Contact support if the limit needs to be increased. For more information on object limits, see[IAM Identity Domain Object Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../sku/overview.htm#iam-object-limits).

### APIs in API Groups

API limits apply to the total of all APIs within a group.

[Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-get-started.htm#)

- `/sso/v1/user/login`
- `/sso/v1/user/secure/login`
- `/sso/v1/user/logout`
- `/sso/v1/sdk/authenticate`
- `/sso/v1/sdk/session`
- `/sso/v1/sdk/idp`
- `/sso/v1/sdk/secure/session`
- `/mfa/v1/requests`
- `/mfa/v1/users/{userguid}/factors`
- `/oauth2/v1/authorize`
- `/oauth2/v1/userlogout`
- `/oauth2/v1/consent`
- `/fed/v1/user/request/login`
- `/fed/v1/sp/sso`
- `/fed/v1/idp/sso`
- `/fed/v1/idp/usernametoken`
- `/fed/v1/metadata`
- `/fed/v1/mex`
- `/fed/v1/sp/slo`
- `/fed/v1/sp/initiatesso`
- `/fed/v1/sp/ssomtls`
- `/fed/v1/idp/slo`
- `/fed/v1/idp/initiatesso`
- `/fed/v1/idp/wsfed`
- `/fed/v1/idp/wsfedsignoutreturn`
- `/fed/v1/user/response/login`
- `/fed/v1/user/request/logout`
- `/fed/v1/user/response/logout`
- `/fed/v1/user/testspstart`
- `/fed/v1/user/testspresult`
- `/admin/v1/SigningCert/jwk`
- `/admin/v1/Asserter`
- `/admin/v1/MyAuthenticationFactorInitiator`
- `/admin/v1/MyAuthenticationFactorEnroller`
- `/admin/v1/MyAuthenticationFactorValidator`
- `/admin/v1/MyAuthenticationFactorsRemover`
- `/admin/v1/TermsOfUseConsent`
- `/admin/v1/MyTermsOfUseConsent`
- `/admin/v1/TrustedUserAgents`
- `/admin/v1/AuthenticationFactorInitiator`
- `/admin/v1/AuthenticationFactorEnroller`
- `/admin/v1/AuthenticationFactorValidator`
- `/admin/v1/MePasswordResetter`
- `/admin/v1/UserPasswordChanger`
- `/admin/v1/UserLockedStateChanger`
- `/admin/v1/AuthenticationFactorsRemover`
- `/admin/v1/BypassCodes`
- `/admin/v1/MyBypassCodes`
- `/admin/v1/MyTrustedUserAgents`
- `/admin/v1/Devices`
- `/admin/v1/MyDevices`
- `/admin/v1/TermsOfUses`
- `/admin/v1/TermsOfUseStatements`
- `/admin/v1/AuthenticationFactorSettings`
- `/admin/v1/SsoSettings`
- `/admin/v1/AdaptiveAccessSettings`
- `/admin/v1/RiskProviderProfiles`
- `/admin/v1/Threats`
- `/admin/v1/UserDevices`
- `/session/v1/SessionsLogoutValidator`
- `/ui/v1/signin`

[Basic Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-get-started.htm#)

- `/admin/v1/HTTPAuthenticator`
- `/admin/v1/PasswordAuthenticator`

[Tokens](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-get-started.htm#)

- `/oauth2/v1/token`
- `/oauth2/v1/introspect`
- `/oauth2/v1/revoke`
- `/oauth2/v1/device`

[Import/Export](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-get-started.htm#)

- `/job/v1/JobSchedules?jobType=UserImport`
- `/job/v1/JobSchedules?jobType=UserExport`
- `/job/v1/JobSchedules?jobType=GroupImport`
- `/job/v1/JobSchedules?jobType=GroupExport`
- `/job/v1/JobSchedules?jobType=AppRoleImport`
- `/job/v1/JobSchedules?jobType=AppRoleExport`

[Bulk](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-get-started.htm#)

- `/admin/v1/Bulk`
- `/admin/v1/BulkUserPasswordChanger`
- `/admin/v1/BulkUserPasswordResetter`
- `/admin/v1/BulkSourceEvents`

[Other](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-get-started.htm#)

Any API not in one of the other API Groups is included in the Other API Group

### Other Restrictions

These restrictions are for Bulk, Import, and Export for all tiers:
- Payload size: 1 MB
- Bulk API: 50 operations limit per call
- Only one of these can be run at a time:
- Import: For Users, Groups &amp; App Role Memberships
- Full sync from apps
- Bulk APIs
- Export: For Users, Groups &amp; App Role Memberships
- CSV Import: 100 K rows limit per CSV &amp; Max file size: 10 MB
-
