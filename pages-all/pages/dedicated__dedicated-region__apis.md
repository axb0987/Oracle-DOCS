# APIs
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#dcoc-content-body)

# APIs

Use this section to learn how architects and engineers interact with Dedicated Region through the OCI Console, APIs, SDKs, CLIs, Terraform, and automation tools.

Dedicated Region uses the same OCI service interaction model as OCI public regions. Teams must automate through[OCI APIs](https://docs.oracle.com/iaas/api/), SDKs, CLI, Terraform providers, and service-specific endpoints while validating which services are enabled in the target Dedicated Region.

Interface Dedicated Region Design Note
OCI Console The console URL follows the Dedicated Region realm and region naming pattern that is provided during deployment. Access must be federated and governed by IAM policies.
Service APIs API endpoints follow the service, region identifier, and realm domain assigned to the Dedicated Region. Example pattern: https:// . . .
SDKs and CLI Use standard OCI SDK and CLI profiles with the Dedicated Region endpoint, tenancy Oracle Cloud ID (OCID), user or workload identity, key material, and region metadata.
Terraform and infrastructure as code (IaC) Use standard OCI provider patterns and pin provider versions for production. Validate region endpoint metadata and service availability before pipeline rollout.
OCI Control Center Use consumption and capacity data from the Dedicated Region console extension and APIs to support forecasting, expansion planning, and automation.

Validate the following endpoint examples during onboarding: identity, iaas, objectstorage, database, ons, marketplace, and service-specific endpoints that each workload needs.

Protect API access with least-privilege IAM policies,[compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/Working_with_Compartments.htm), dynamic groups, MFA, network sources, and logging.

Document the region identifier, realm domain, console URL, tenancy onboarding process, service endpoint list, automation runners, and break-glass administrative process.

## Operator API Readiness

Before you use operator APIs, create an IAM user or workload identity for the caller, place the caller in the appropriate predefined operator group, generate an API signing key, record the key fingerprint, and collect the tenancy OCID and user OCID. Use policy statements in the following form, and grant only the permissions that the automation task requires:

allow group to { } in tenancy

API callers must use the Dedicated Region service endpoint for the target realm and region, pass compartment or tenancy OCIDs consistently, and retain response headers, such as opc-request-id, for troubleshooting. List operations must handle opc-next-page pagination. Update operations must account for etag or precondition behavior when optimistic concurrency applies.

Caution: These APIs are intended for internal use within the Dedicated Cloud environment. Treat API credentials, signing keys, database wallets, request payloads, billing documents, and support diagnostics as restricted operational data.

## Operator API Reference Areas

Use the following API areas for Dedicated Region operations.

API Area Use in Dedicated Region Operations
Internal orders Create, list, view, update, approve, and deny internal order requests for internal teams or employees that need a tenancy. Approved requests are forwarded to Oracle Cloud Subscription to start subscription and tenancy creation.
Subscriptions List and retrieve subscriptions, review subscription details, and manage subscription lifecycle actions, such as suspend and resume.
Billing Manage billing accounts, billing cycles, billing runs, billing documents and lines, unit credits, commitments, and usage summaries for chargeback, showback, and billing automation.
Limits and spending controls List available services and service limits, retrieve usage, manage limit overrides, view spending limits, and estimate the cost of dynamic limit increases.
Capacity and business reporting Use exported dashboard data and available APIs for compute, block storage, file storage, object storage, and Exadata capacity planning. Connect approved BI tools to the reporting data warehouse when direct reporting access is required.

## Internal Order APIs

### General Information: Internal Order APIs

The following table lists general information for the Internal Order API.

Field Description
Title Internal Order API
Version`20241220`
Base Path`/20241220`
Produces`application/json`
Host Example:`127.0.0.1`. Replace with the actual service endpoint.
Endpoint Template`https://internal-order-replace-me.{region}.oci.{secondLevelDomain}`

Use the OracleCloudSubscriptions Internal Order Management Service (IOMS) API for internal order requests that create internal subscriptions and tenancies for teams or employees. do not use IOMS to create end-customer tenancies. The core workflow is to create an OrderRequest, list requests in the compartment, retrieve the request by OCID, update request details when needed, and approve or deny the request with an optional review note.

Operation Endpoint Pattern Design Note
Create order request POST /20241220/orderRequests Requires compartmentId, firstName, lastName, adminEmail, and tenantOrganization. Include displayName, costCenter, notes, and tags when needed.
List order requests GET /20241220/orderRequests?compartmentId={compartmentId} Use filtering, sorting, and pagination to review pending, approved, succeeded, or failed requests.
Get order request GET /20241220/orderRequests/{orderRequestId} Use the OrderRequest OCID to inspect requester details, lifecycle state, lifecycle details, review notes, and tags.
Update order request PUT /20241220/orderRequests/{orderRequestId} Update administrator, organization, cost center, notes, or tag details before final approval when the request state allows updates.
Approve or deny request POST /20241220/orderRequests/{orderRequestId}/actions/approve or POST /20241220/orderRequests/{orderRequestId}/actions/deny Use a reviewNote to preserve the review decision. Approval can create an asynchronous work request that must be tracked through the returned work request identifier when present.

Common IOMS states include ACCEPTED with PENDING_REVIEW during intake, WAITING or SUCCEEDED after approval processing, and FAILED when order creation does not complete. Operators must capture the OrderRequest OCID, lifecycleDetails, opc-request-id, and opc-work-request-id when troubleshooting.

## Subscription Lifecycle APIs

### General Information: Subscription Lifecycle APIs

The following table lists general information for the Subscription Lifecycle API.

Field Description
Title Subscription Lifecycle API
Version`20230428`
Base Path`/20230428`
Produces`application/json`
Host Example:`127.0.0.1`. Replace with the actual service endpoint.
Endpoint Template`https://subscription-lifecycle-replace-me.{region}.oci.{secondLevelDomain}`

Use the OracleCloudSubscriptions API to review subscriptions and automate lifecycle actions. The base path is /20230428. List subscriptions by compartment, retrieve a subscription by subscription OCID, suspend a subscription with a grace period and reason code, and resume a suspended subscription when service must be restored.

Operation Endpoint Pattern Design Note
List subscriptions GET /20230428/subscriptions?compartmentId={compartmentId} Use compartmentId as the required scope. Apply limit, page, lifecycleState, displayName, or adminEmail filters when reviewing large subscription sets.
Get subscription GET /20230428/subscriptions/{subscriptionId} Review billing model, active billing mode, customer details, data center region, line items, lifecycle state, subscription number, and start or end times.
Suspend subscription POST /20230428/subscriptions/{subscriptionId}/actions/suspend Provide gracePeriodInDays and reasonCode where required. Verify that lifecycle state and lifecycle details move through the expected suspension states.
Resume subscription POST /20230428/subscriptions/{subscriptionId}/actions/resume Verify that the subscription moves from suspended or inactive processing states through activating and active states.

## Billing APIs

Use the OcsBillingService API to automate billing administration for internal chargeback or showback. The service endpoint follows https://ocs-billingservice.{region}.oci.{secondLevelDomain}, with the base path /20230401. The API supports authorization checks, auditing, tagging, pagination, sorting, and request tracing.

Billing Resource Primary Operations Use in Operations
Billing accounts List, get, update Track charges and credits for usage and commitments in a single currency, group subscriptions under an account, or split charges across accounts.
Billing cycles Create, list, get, update, delete Define the billing period, period type, and billing day that determine cutoff dates and schedule behavior.
Billing runs Create, list, get, delete, pause, resume, resubmit Run regular or on-demand billing jobs, use dry runs for simulation where appropriate, and review processed, total, and failed account counts.
Billing documents and lines List and get Review generated billing documents, billing periods, totals, charge types, discounts, drawdown amounts, and itemized document lines.
Unit credits and commitments List and get Track universal credit model (UCM) entitlements, service credits, prepaid balances, commitment charges, and remaining credit balances.
Usage summaries Summarize Aggregate credits, consumption, and overage for operator and end-customer reporting views.

For billing automation, design for pagination, sort order, compartment scope, resource OCIDs, and standard error handling. Common billing run states include ACCEPTED, IN_PROGRESS, WAITING, FAILED, SUCCEEDED, and CANCELED. Retain opc-request-id for all failures. Include billingAccountId, billingRunId, billingDocumentId, subscriptionId, and cutoff timestamps in troubleshooting records.

### Billing Operations in the Operator Console

Use the Operator Console for day-to-day billing administration that complements billing API automation. Billing account, billing cycle, billing hold, billing run, and billing history tasks are performed from the root compartment so operators can manage chargeback or showback records consistently across internal subscriptions.

Open billing account tasks from the Operator Console home page under My tools, or from the navigation menu under Business operations. Use Billing accounts for account values, billing dates, billing holds, and billing history. Use Billing runs for scheduled, simulation, and on-demand billing run actions.

### Billing Account Review and Billing Dates

A billing account contains the values that billing operations act on, including account identity, billing cycle, hold state, and billing status. In the root compartment, use the account status, on billing hold, bill cycle, and billing status filters to locate the account and open the billing account value for review.

Use the Account details area to review Last Billed, Billing cut-off date, Billing Cycle, and Next billing run date. The billing cycle cadence is selected as part of the original customer contract, entered during order placement, and cannot be changed after the order is processed.

### Billing Holds

Use a billing hold to pause a billing account cycle and prevent billing runs from occurring while the account is under review. Create the hold from the account by selecting On billing hold, choosing Customer Request, Failure to Pay, or Fraud, adding comments when useful, and confirming the hold.

Remove the hold when billing can resume by selecting On billing hold and confirming removal. When the console presents the option, decide whether to run a billing run immediately or wait until the next scheduled billing run in the billing cycle.

### Billing Runs

Billing runs generate billing documents on the billing cycle schedule. Manually run a run when initial billing document generation was incorrect or when billing must be regenerated after a subscription is removed from hold. Use Simulation mode to preview the run without running it.

Create a regular run by bill cycle by selecting Monthly, Quarterly, or Annually, then setting the billing day of the month and billing cut-off date. Create an on-demand run by account by selecting the account name and billing cut-off date.

To temporarily prevent run, open the billing run and select Pause Billing Run. To remove a run that should not proceed, select Cancel billing run. Use the type, status, and billing cut-off date filters to locate the run. A scheduled run might not be eligible for pause or cancellation.

### Billing History and Pre-Tax Documents

Use Billing history to inspect prior billing documents for a customer. Open the billing account, select Billing history under Resources, filter by created date or billing period, and select the billing document OCID to download the CSV.

Downloaded billing documents are pre-tax CSV files that contain charged line items from the last billing run. Subscribers have one base-rate line item, and overages appear as separate SKU line items.

For operational consistency, retain the billing account identifier, billing run identifier, billing document OCID, billing period, billing cut-off date, selected filters, comments used for holds, and any console error text when escalating billing issues or reconciling chargeback records.

## Limits, Capacity, and Reporting APIs

Use the Limits Control Plane Operator API to inspect and manage tenancy-level service limits and spending controls. Typical operations include listing available services, listing limits for a service, viewing usage for a specific limit, retrieving or updating limit overrides, retrieving spending limits, updating spending limit overrides, and computing estimated cost for a dynamic limit increase.

Endpoint Pattern Use
GET /services?compartmentId={tenancy_ocid} List available services for the specified tenancy.
GET /services/{serviceName}/limits?compartmentId={tenancy_ocid} List service limits in the current region for the tenancy.
GET /services/{serviceName}/limits/{limitName}/overrides or PUT /services/{serviceName}/limits/{limitName}/overrides Retrieve or update an override for a specific service limit when the operator is authorized.
GET /services/{serviceName}/limits/{limitName}/usage Retrieve current usage for a specific service limit.
GET /spendingLimit or PUT /spendingLimit/overrides View effective spending limits or update spending limit overrides.
POST /spendingLimit/actions/computeEstimatedCost Estimate the incremental cost of a dynamic limit increase before approval.

Capacity management must stay aligned with the operator API model. Dashboards and data are available for Compute, Block Storage, File Storage, Object Storage, and Exadata. Charts can be exported from the Console as Excel, PPT, or CSV files and then consumed through APIs for automation. Use this data during the forecast, review, expand, and repeat cycle with Oracle Capacity Management.

For business reporting, operators can use Operator Console dashboards or securely connect an approved business intelligence (BI) tool directly to the reporting data warehouse. Before direct data warehouse access is enabled, allowlist the BI server IP addresses, download the database wallet, and obtain the current credentials through the approved operational process.

## API Testing and Operational Standards

Use the provided Bruno collections to test and validate API behavior before promoting automation into production. Available collections include oci-billing, oci-limits, and oci-ocs-ioms. After you install Bruno, open the extracted collection, select the request, configure the target environment, and run the request from the collection interface.

Standardize API automation around least-privilege[IAM policies](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm), compartment scoping, request identifiers, pagination, retry and backoff for 429 responses, and consistent handling for 400, 401, 403, 404, 409, 412, 429, and 500 responses. Include resource OCIDs, timestamps, request IDs, lifecycle state, lifecycle details, and recent payload changes in SRs or internal escalation records.

- [APIs](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#apis)
- [Operator API Readiness](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#operator-api-readiness)
- [Operator API Reference Areas](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#operator-api-reference-areas)
- [Internal Order APIs](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#internal-order-apis)
- [General Information: Internal Order APIs](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#internal-order-apis)
- [Subscription Lifecycle APIs](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#subscription-lifecycle-apis)
- [General Information: Subscription Lifecycle APIs](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#subscription-lifecycle-apis)
- [Billing APIs](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#billing-apis)
- [Billing Operations in the Operator Console](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#billing-operations-in-the-operator-console)
- [Billing Account Review and Billing Dates](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#billing-account-review-and-billing-dates)
- [Billing Holds](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#billing-holds)
- [Billing Runs](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#billing-runs)
- [Billing History and Pre-Tax Documents](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#billing-history-and-pre-tax-documents)
- [Limits, Capacity, and Reporting APIs](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#limits-capacity-and-reporting-apis)
- [API Testing and Operational Standards](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/apis.htm#api-testing-and-operational-standards)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
