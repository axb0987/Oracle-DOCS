# Dedicated Region - Identity and Access Management (IAM)
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#dcoc-content-body)

# Dedicated Region - Identity and Access Management (IAM)

Use this section to learn how to establish Dedicated Region IAM control, configure federation, assign operator access, and govern access to Operator Console, Customer Console, Fusion Console, and Business Reporting functions.

Use this section when planning administrator onboarding, operator access, group assignments, report access, and console sign-in flows after the Dedicated Region environment is transferred to the customer operator team.

## IAM Operating Model and Tenancy Boundaries

Dedicated Region IAM operations begin with the initial Dedicated Region order and the activation email sent to the designated Operator Administrator. After activation, use the Operator Administrator account to access the Dedicated Region operator experience and approve membership in Operator Access Tenancy groups.

IAM Area Operational Use Design Guidance
Commercial Subscription Tenancy Tracks resources consumed by customers for Cost and Usage reporting. Subscription identifiers for these resources begin with ocid1.organizationsubscription. Use the custom tenancy name selected during subscription activation. Treat this tenancy as the commercial subscription boundary for customer consumption reporting.
Oralce Approved Tenancy Tenancy Provides access to the Operator Console and the Customer Console entry point. It contains the predefined administrative groups in the operators domain. Create operator user accounts in the operators domain and assign only the groups required for each role. The Default domain might appear during authentication, but it is used by customers and is not an operator administration target.
Operator Resources Tenancy Tracks resources consumed by the operator organization for billing and reporting. Subscription identifiers for these resources begin with ocid1.oraclecloudsubscription. Invite the operator_resources tenancy as a child tenancy of the Commercial Subscription Tenancy when instructed during onboarding. Use this tenancy for operator-owned resource usage tracking.
Environment control transfer After control transfer, Oracle no longer has console access. The operator can become the tenancy administrator of the operator_resources tenancy and remove remaining Oracle employee user accounts from that tenancy. Complete the control transfer before broad operator onboarding. Confirm access, group assignments, and support contacts before removing transitional accounts.

## Operator Access and Federation

Configure federation before inviting users to the operators domain when operators must authenticate through the organization identity provider. The operators domain is created in the Oracle Approved root tenancy and configured as the service provider. Identity data is federated or synchronized depending on the identity provider type.

Setup Area Operator Action Implementation Guidance
SAML identity provider setup Open the Customer Console from the Operator Console, go to Identity and Security, open Domains, select the operators domain, and add the identity provider from the Federation tab. Provide the IdP name, optional description, and supported icon. Export SAML metadata to the identity provider, then import metadata, enter metadata manually, or import the IdP metadata URL.
Advanced federation controls Review optional SAML controls before creating the IdP. Use the required signature hashing algorithm, encrypted assertion setting, force authentication setting, requested authentication context, Holder-of-Key subject confirmation, and signing certificate options required by the enterprise IdP configuration.
Attribute mapping Select the requested Name ID format and map identity attributes from the IdP to the OCI identity domain. Validate required mappings such as NameID to UserName when applicable. Mapping options vary by identity provider.
Validation and activation Review the SAML IdP settings, create the IdP, test the SSO connection, activate the IdP, and assign it to the appropriate IdP policy rule. Do not invite broad operator access until the IdP test succeeds and the policy rule exposes the correct sign-in option.
IdP policy assignment Open the IdP policy, edit the identity provider rule, select Assign identity providers, select the IdP, and save changes. Assign additional IdPs to the same rule only when the sign-in experience and access policy intentionally allow those providers.

## Operator Users, Groups, and Report Access

Use predefined groups to grant only the Operator Console capabilities and reports required for each role. Create users in the operators domain after federation is ready, and assign one or more predefined groups during user creation or from the group membership workflow.

Group Name Primary Responsibility Report Access
Operator Administrator Complete initial setup, configure the realm, manage operator users, and approve membership in Operator Access Tenancy groups. All reports.
Billing Managers Create and run billing runs, adjust billing run schedules, place customers on billing hold, release billing holds, and view billing account lists. Revenue and Consumption reports.
Order Managers View order lists and details, create orders, check activation status, resend activation emails, and look up individual orders. Consumption reports.
Subscription Managers Receive quotes, complete subscription request forms, place orders, reissue activation emails, and view, suspend, or reinstate subscriptions. Revenue, Consumption, and Capacity Management reports.
Customer Limits Managers Support technical realm operations and view or edit customer resource limits and spending limits. Order and Provisioning and Capacity Management reports.
Realms Managers Review realm capacity information when the role is used for reporting access. Capacity Management reports.

To create an operator user, open the Customer Console from the Operator Console, go to Identity and Security, open Domains, select the operators domain, and create the user from Users or User Management. Provide the user details, keep Use the email address as the username selected when appropriate, assign the required predefined groups, and create the user. The invite email is sent to the email address provided for the user.

To grant Business Reporting access to an existing user, open the Operator Access Domain in the Customer Console, select the required group, select Assign user to groups, select the user, and add the user to the group. Search by the beginning of the username, first name, or last name when the user list is large.

## Console Access Patterns

Console access depends on the tenancy, identity domain, assigned groups, and the specific console needed for the task. Bookmark direct console URLs only after the initial access path is validated.

Console or Access Path How to Access Access Notes
Operator Console as a federated user Use the administrator-provided link, sign in to the Oracle approved root tenancy, select the operators identity domain, and complete the IdP sign-in flow. Available plugins depend on assigned groups. A user assigned to one operator group cannot access features that belong only to another group.
Customer Console as an Operator Administrator Open the provided Customer Console URL, or select View customer console from the Operator Console. Select the oracle approved root tenancy, continue, select the operators identity domain, and sign in. Use this path for IAM domain, group, federation, and operator-user administration tasks.
Fusion Console Open Fusion orders, Fusion invoicing, or Fusion Support from the Operator Console, or use a direct Fusion Console URL when credentials and access have already been provided. Grant Fusion access only through the required groups. Bookmark the Fusion Console URL only when direct future access is required.
Business Reporting dashboards Access dashboards from the Operator Console. Assign users to the appropriate operator groups in the Customer Console when dashboard or report access is required. Report visibility is group-based. Refresh dashboard data before operational review or export.

## IAM Operational Guardrails

Keep IAM administration aligned with least-privilege access, audited group membership, and clear separation between operator, customer, and Oracle-facing responsibilities.

Guardrail Implementation Guidance
Federation readiness before invitations Set up and validate federation for the target domain before inviting users who must use enterprise SSO.
Group-based least privilege Assign only the predefined groups required for the operator task. Review users with multiple groups for segregation-of-duties concerns.
Console boundary awareness Use the Operator Console for operator workflows, the Customer Console for identity-domain and customer-console workflows, and Fusion Console only for assigned Fusion functions.
Report access control Grant report access through group membership instead of custom access. Verify that report visibility matches the user role before sharing exported data.
Post-transfer cleanup After taking control of the environment, validate the Operator Administrator path, confirm operator_resources tenancy administration, and remove remaining transitional Oracle employee accounts where appropriate.

## Customer Limits

Use this section to learn how operators use the Operator Console to view customer limits, change limits and spending limits, review limit requests, contact internal customers, and review customer request history and communication.

Open Customer limits from the Operator Console home page under My tools, or use the navigation menu and select Business operations, then Customer limits. Use the Customer Limits page for capacity limits, and use Customer spending limits when the request changes spending controls for an internal tenancy.

Customer Limits Area Use Primary Operator Actions
Customer limits View and update service capacity limits for a tenancy and region. Enter the tenancy OCID, select the region, optionally apply one or more service filters, and apply the search. Use Change Limit from the actions menu when an approved limit must be updated.
Customer spending limits View and update spending limits for an internal tenancy. Open Customer spending limits, enter the tenancy OCID, review the displayed limits, and use Change Limit from the actions menu when an approved spending limit must be updated.
Limit requests Locate, review, decline, escalate, or follow up on customer limit requests. Search by SR number, service, tenancy OCID, or status. Open the request from the Request title column, then use the available request actions.
Customer communication and history Review previous customer comments, communication, and related requests before taking action. Open the limit request, then use Customer communication or Customer request history to review prior context.

### Access the Customer Console

Use the Customer Console when an operator workflow requires customer-console access. In the Operator Console, select View customer console from the Welcome to Operator Console area, complete the authentication prompt in the new window, and bookmark the Customer Console URL only when direct future access is required.

### View Customer Limits

View customer limits when you need to inspect capacity limits for a specific tenancy and region before taking action on a request.
- 

Open Customer limits from My tools or from Business operations.
- 

Enter the customer tenancy OCID and press Tab.
- 

Select the region.
- 

Optionally filter by service. Use a single service filter, such as API Gateway, or multiple service filters, such as API Gateway, Compute, Database, and IP Management.
- 

Select Apply to show the limits for the search combination.

### Change Customer Limits

Change a customer limit only after the related request is reviewed and approved. From the Customer Limits page, enter the tenancy OCID, select the region, apply any service filters, and open the actions menu for the limit that must change. Select Change Limit, enter the resource quantity, and select Calculate limit to convert the resource quantity into the dollar equivalent limit. If the calculated value is correct, select Change limit. The internal customer is notified by email after the change is made.

## Change Customer Spending Limits

Use Customer spending limits to review or update spending controls for an internal tenancy. Open Customer spending limits, enter the customer tenancy OCID, and press Tab to show spending limits for that tenancy. To update an approved spending limit, open the actions menu for the limit, select Change Limit, enter the new spending limit, and select Change limit. The internal customer is notified by email after the change is made.

## Review Limit Requests

Use Limit requests to review customer-submitted limit requests and updates to existing requests. Under Limits, select Limit requests, then search by SR number or filter by service, tenancy OCID, or status. Status values include Approved, Declined, and Requested. Open the request by selecting its value in the Request title column.

From the Limit Request page, use the available actions to escalate the request to Oracle for approval, decline a request that is still in Requested status, contact the customer for more details, view the ticket in the Fusion Console, review customer request history, or view customer communication.

### Contact the Customer

Contact the customer when more information is required before approving, declining, or escalating a limit request. Open the limit request, select Contact customer, enter the reason for the follow-up in the Comment field, and select Add Comment. The customer is notified about the comment and can respond with additional information.

## Review Customer Communication and Request History

Review customer communication before making a decision when prior comments might affect the request. Open the limit request and select Customer communication to show previous comments.

Review customer request history when you need context from earlier customer requests. Open the limit request and scroll to Customer request history. The history shows request title, SR number, service, status, and date updated. Select a request title to open and review the prior request.

### Decline a Limit Request

Decline a limit request only when the request is in Requested status. Open the limit request, select Decline limit, enter the reason in Reason for decline, and select Decline. The customer is notified about the decision by email.

### Escalate a Limit Request

Escalate a limit request to Oracle when Oracle approval or knowledge-base research is required before the request can be approved. Use My Oracle Support (MOS) only for Dedicated Region knowledge-base research and approval support. Do not use other MOS features for Dedicated Region operations.

Before using MOS, create and set up the Oracle.com account, retrieve the Customer Support Identifier (CSI), register the CSI, and access the support portal. Keep the MOS workflow separate from in-realm customer request handling and retain the SR number, tenancy OCID, service, request title, and request status when escalating.

- [Dedicated Region - Identity and Access Management (IAM)](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#dedicated-region-identity-and-access-management-iam)
- [IAM Operating Model and Tenancy Boundaries](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#iam-operating-model-and-tenancy-boundaries)
- [Operator Access and Federation](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#operator-access-and-federation)
- [Operator Users, Groups, and Report Access](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#operator-users-groups-and-report-access)
- [Console Access Patterns](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#console-access-patterns)
- [IAM Operational Guardrails](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#iam-operational-guardrails)
- [Customer Limits](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#customer-limits)
- [Access the Customer Console](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#access-the-customer-console)
- [View Customer Limits](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#view-customer-limits)
- [Change Customer Limits](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#change-customer-limits)
- [Change Customer Spending Limits](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#change-customer-spending-limits)
- [Review Limit Requests](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#review-limit-requests)
- [Contact the Customer](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#contact-the-customer)
- [Review Customer Communication and Request History](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#review-customer-communication-and-request-history)
- [Decline a Limit Request](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#decline-a-limit-request)
- [Escalate a Limit Request](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-identity-access-management-iam.htm#escalate-a-limit-request)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
