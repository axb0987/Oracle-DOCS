# API Use Cases
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-use-cases.htm
- Fetched: 2026-09-05 02:17 CDT

# API Use Cases

Step through typical use cases using the IAM identity domain REST APIs.

The response output that you get might differ from the response examples shown in the use cases. The output depends on the release and environment, and the configuration of the identity domain.

Task More Information

Adaptive Risk Analysis for Custom Client Applications

This use case provides an example request of using the adaptive risk analysis endpoints for custom applications and on-premises access management systems.

See[Adaptive Risk Analysis for Custom Client Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/adaptive-custom-clients.htm).

Oracle Services Onboarding Using the API

Identity domain administrators can manage the onboarding process of OPC applications to an identity domain.

See[Allowing Oracle Services Onboarding Using the API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-allow_oracle_services_onboarding.htm).

Changing Your Own Profile Attributes

Use the API to change your own profile attributes (for example, an email address or a password) by setting the`allowSelfChange`attribute to`true`in the request payload or URL query string parameter.

See[Using allowSelfChange To Update Profile Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/change-your-own-profile-attributes.htm).

Creating an Enterprise Application with Authorization Policy

This use case provides an example request of creating an enterprise application using REST API.

See[Creating an Enterprise Application with Authorization Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm).

Importing and Exporting Users, Groups, and AppRoles

These use cases provide example requests for bulk loading users, groups, and application roles from other repositories into an identity domain.

See[Importing and Exporting Users, Groups, and AppRoles](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/BulkImportExport.htm).

Managing Custom Claims

This use case provides an example request of how to add custom claims to an access token, an identity token, or both the tokens.

See[Managing Custom Claims](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/custom-claims-token.htm).

Managing the Refresh Token Expiration Value

This use case provides an example of how to verify the validity of a refresh token and update the token expiry time.

See[Updating Refresh Token Expirations](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/refreshtokenexiry.htm).

Managing User Schema Customizations

This use case provides examples of how to add, update, remove, and enable the import of custom user schema attributes in an identity domain.

See[Customizing User Schemas](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/schemacustomization.htm).

Obtaining and Using an OAuth Token for Platform Services

This use case provides an example request of how to use a OAuth 2.0 token issued by an identity domain to access REST endpoints from an Oracle Cloud Platform Services (PaaS).

See[Using an OAuth Token for Platform Services](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/obtainoauthtokenidcs.htm).

Triggering an Email Verification Flow if Email Address is Already Verified

This use case provides an example of how custom clients can re the change email flow for users who already have verified their email addresses.

[Resending Email Verifications When The Email Address Is Already Verified](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/trigger-email-verify-flow-if-email-already-verified.htm)

Using Duo Security with an IAM identity domain

This use case provides an example of how to use an Authenticate API with Duo Security.

See[Using Duo Security with Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm).

Using OpenID Connect to Extend OAuth 2.0

This use case provides an example of how client applications can authenticate to an identity domain using OpenID connect protocol and identity domain REST APIs.

See[Using OpenID Connect to Extend OAuth 2.0](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingopenidconnect.htm).

Using Self Service to Enroll in MFA using the SMS Factor

This use case provides a step-by-step example of using the identity domain REST API for Self-Service enrollment in Multifactor Authentication (MFA) using SMS Factor.

See[Enrolling in MFA using the SMS Factor Using Self Service](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingelfservicetoenrollinmfausingthesmsfactor.htm).

Using the Authenticate API to develop a custom sign-in page

This use case provides an example of how to use the Authenticate API to develop a custom sign-in page.

[Using the Authenticate API to Develop a Custom Sign-in Page](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm)

Using the Audit Event APIs

This use case provides example of how to get Audit logs covering significant events, changes, and actions.

[Using the Audit Event APIs](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauditeventapis.htm)

Important : IAM identity domains AuditEvents and certain reports templates in the Reports APIs will stop returning new data after May 15, 2024. Instead, you can use the[OCI Audit service](https://docs.oracle.com/iaas/Content/Audit/home.htm)to get this data. To view service change announcements for IAM, see[IAM (Service Change Announcements)](https://docs.oracle.com/iaas/Content/servicechanges.htm#servicechanges_topic_IAM).

Using the`onBehalfOf`Allowed Operation

This use case provides an example of how to create an application and specify the`onBehalfOf`User allowed operation.

See[Using the onBehalfOf Allowed Operation](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OnBehalfOf.htm).

Using the On Demand MFA API to Develop Custom Sign-In Page

This use case provides a step-by-step example of using the Authenticate API to authenticate users and perform multifactor enrollment and authentication. This is used when you develop a custom sign-in page.

See[Using the On-Demand MFA API to Develop Custom Sign-In Page](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingondemandapis.htm).

Working with Apps

These use cases provide example requests to create and activate an OAuth Resource Server, an OAuth Client Apps, and a SAML App using the REST APIs. Each use case also provides the required App attributes.

See[Working with Apps](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/WorkingWithApps.htm).

Working with OAuth 2 to Access the REST API

This use case walks you through using an OAuth client with identity domains to access the REST APIs.

See[Using OAuth 2 to Access the REST API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OATOAuthClientWebApp.htm)
