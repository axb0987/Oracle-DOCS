# APIs
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/apis.htm
- Fetched: 2026-09-05 03:29 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/apis.htm#dcoc-content-body)

# APIs

The commercial APIs support integration with Oracle Alloy back-end systems. The API set is intended for internal integration scenarios within an Oracle Alloy or OCI Dedicated Region environment where a customer or operator has an existing third-party solution for commercial services, such as customer onboarding, ordering, pricing, subscriptions, billing, and invoicing.

Oracle Alloy commercial integrations use REST and SOAP interfaces across Oracle Fusion applications and Oracle Alloy-specific services. Fusion Supply Chain and Manufacturing Order Management provides product and service configuration, pricing, and order management. Fusion Financial Management provides accounts receivable capabilities for customer invoices.

## API Version Discovery and Framework Configuration

Operation Method Endpoint or Pattern Notes
Identify default and available REST framework versions GET /fscmRestApi/resources/latest Discovers the default version and the available versions.
Set a specific REST framework version Header Rest-Framework-Version on requests to /fscmRestApi/resources/latest Pins requests to a specific framework version.
Retrieve payload documentation for a resource GET /fscmRestApi/resources/latest/receivablesInvoices/describe Uses the describe pattern for payload metadata.

## Customer and Account Setup

Customer setup in Oracle Alloy follows a staged workflow that establishes the legal entity context, organization record, location, customer account, and enterprise set association used by downstream commercial processes.

Step Operation Method Endpoint Notes
1 Look up legal entity GET /fscmRestApi/resources/latest/legalEntitiesLOV Establishes the legal entity context.
2 Create organization and addresses POST /crmRestApi/resources/latest/hubOrganizations Creates the organization record and addresses.
3 Create location POST /crmService/FoundationPartiesLocationService Creates the location record.
4 Merge location into organization POST /crmService/FoundationPartiesOrganizationService Associates the location with the organization.
5 Get enterprise set ID GET /fscmRestApi/resources/latest/setIdSets Gets the enterprise set association.
6 Create customer account POST /crmService/CustomerAccountService Associates the organization party ID, party site ID, and enterprise set ID.
Lookup List organizations GET /crmRestApi/resources/latest/hubOrganizations Returns organization records.
Lookup Get organization by party number GET /crmRestApi/resources/latest/hubOrganizations/{PartyNumber} Retrieves a specific organization.
Lookup Get organization addresses GET /crmRestApi/resources/latest/hubOrganizations/{PartyNumber}/child/Address Returns organization address records.
Lookup List customer accounts GET /crmRestApi/resources/latest/accounts Returns customer accounts.
Lookup Get customer accounts by owner party number GET /crmRestApi/resources/latest/accounts?q=OwnerPartyNumber={OwnerPartyNumber} Filters accounts by owner party number.
Lookup Get customer account by account number GET /crmRestApi/resources/latest/accounts/{AccountNumber} Retrieves a specific customer account.
Lookup Get customer accounts by organization name GET /crmRestApi/resources/latest/accounts/?q=OrganizationName="{OrganizationName}" Filters accounts by organization name.

## Order Management Endpoints

Operation Method Endpoint Notes
Look up legal entities GET /fscmRestApi/resources/latest/legalEntitiesLOV Required prerequisite lookup.
Look up business units GET /fscmRestApi/resources/latest/finBusinessUnitsLOV Required prerequisite lookup.
Look up customer organizations GET /crmRestApi/resources/latest/hubOrganizations Required prerequisite lookup.
Look up customer addresses GET /crmRestApi/resources/latest/hubOrganizations/{PartyNumber}/child/Address Required prerequisite lookup.
Look up customer account sites GET /fscmRestApi/resources/latest/customerAccountSitesLOV Required prerequisite lookup.
Create commercial order POST /fscmRestApi/resources/latest/salesOrdersForOrderHub Creates a commercial order.
Create order with alternate price list POST /fscmRestApi/resources/latest/salesOrdersForOrderHub Uses the same resource with alternate pricing content.
Create extension order POST /fscmRestApi/resources/latest/salesOrdersForOrderHub Uses the same resource for an extension order.
List orders GET /fscmRestApi/resources/11.13.18.05/salesOrdersForOrderHub Returns orders.
Query orders by creation date GET /fscmRestApi/resources/11.13.18.05/salesOrdersForOrderHub?q=TransactionOn &gt; '{{creationDateFrom}}' AND TransactionOn &lt; '{{creationDateTo}}' Filters orders by creation date range.
Get order by key GET /fscmRestApi/resources/11.13.18.05/salesOrdersForOrderHub/{orderKey} Retrieves a specific order.
Get order by order number GET /fscmRestApi/resources/11.13.18.05/salesOrdersForOrderHub?q=OrderNumber={orderNumber} Filters by order number.
Get order lines GET /fscmRestApi/resources/latest/salesOrdersForOrderHub/{orderKey}/child/lines Returns line details.
Get bill-to customer GET /fscmRestApi/resources/latest/salesOrdersForOrderHub/{orderKey}/child/billToCustomer Returns bill-to details.
Get ship-to customer GET /fscmRestApi/resources/latest/salesOrdersForOrderHub/{orderKey}/child/shipToCustomer Returns ship-to details.
Get line additional information GET /fscmRestApi/resources/latest/salesOrdersForOrderHub/{orderKey}/child/lines/{lineId}/child/additionalInformation Returns line-level metadata.
Get subscription line attributes GET /fscmRestApi/resources/latest/salesOrdersForOrderHub/{orderKey}/child/lines/{lineId}/child/additionalInformation/{FulfillLineId}/child/FulfillLineEffBSubscription__Line__AttributesprivateVO Returns subscription-specific line metadata.

## Price List Endpoints

Operation Method Endpoint Notes
List price lists GET /fscmRestApi/resources/latest/priceLists Returns available price lists.
Get price list by ID GET /fscmRestApi/resources/latest/priceLists/{PriceListId} Retrieves a specific price list.
Query price list by name GET /fscmRestApi/resources/latest/priceLists?q=PriceListName LIKE '{PriceListName}%' Filters price lists by name prefix.
Update price list PATCH /fscmRestApi/resources/latest/priceLists/{PriceListId} Updates a price list.
List price list items GET /fscmRestApi/resources/latest/priceLists/{PriceListId}/child/items Returns items in a price list.
Get price list item GET /fscmRestApi/resources/latest/priceLists/{PriceListId}/child/items/{PriceListItemId} Retrieves a specific price list item.
List item charges GET /fscmRestApi/resources/latest/priceLists/{PriceListId}/child/items/{PriceListItemId}/child/charges Returns charges for a price list item.
Update product pricing, step 1 GET /fscmRestApi/resources/latest/priceLists/{price_list_id}/child/items/{price_list_item_id}/child/charges Gets the current charge collection.
Update product pricing, step 2 PATCH /fscmRestApi/resources/latest/priceLists/{price_list_id}/child/items/{price_list_item_id}/child/charges/{last_charge_item_id} Updates an existing charge.
Update product pricing, step 3 POST /fscmRestApi/resources/latest/priceLists/{price_list_id}/child/items/{price_list_item_id}/child/charges Creates a new charge in the same collection.

## Receivables Endpoints

Operation Method Endpoint Notes
Query all receivables invoices GET /fscmRestApi/resources/latest/receivablesInvoices Returns receivables invoices.
Query invoice by customer transaction ID GET /fscmRestApi/resources/latest/receivablesInvoices/{customer_transaction_id} Retrieves a specific receivables invoice.
Query invoice by transaction number GET /fscmRestApi/resources/latest/receivablesInvoices?q=TransactionNumber='{transaction_number}' Filters by transaction number.
Query receivables invoice lines GET /fscmRestApi/resources/latest/receivablesInvoices/{transaction_id}/child/receivablesInvoiceLines Returns line-level invoice details.

## Internal Subscription and Billing Services

### General Information: Billing Services APIs

The following table lists general information for the Billing ServicesAPI.

Field Description
Title Billing Services API
Version`20230401`
Base Path`/20230401`
Produces`application/json`
Host Example:`127.0.0.1`. Replace with the actual service endpoint.
Endpoint Template`https://billing-services-replace-me.{region}.oci.{secondLevelDomain}`

Service Operation Method Endpoint Notes
Internal Order Management Service Create order request POST /orderRequests Creates an operator-internal tenancy or subscription request.
Internal Order Management Service Get order request GET /orderRequests/{orderRequestId} Retrieves a specific order request.
Internal Order Management Service Update order request PUT /orderRequests/{orderRequestId} Updates an existing order request.
Internal Order Management Service Approve order request POST /orderRequests/{orderRequestId}/actions/approve Approves an order request.
Internal Order Management Service Deny order request POST /orderRequests/{orderRequestId}/actions/deny Denies an order request.
Internal Order Management Service List order requests GET /orderRequests?compartmentId={compartmentId} Lists order requests in a compartment.
Oracle Cloud Subscription Service Create order POST /orders Creates an order after intake from Fusion Order Management or Internal Order Management Service.
Oracle Cloud Subscription Service List orders GET /orders?compartmentId={compartmentId} Lists orders for a compartment.
Oracle Cloud Subscription Service Get order GET /orders/{orderId} Retrieves a specific order.
Oracle Cloud Subscription Service List subscriptions GET /subscriptions?compartmentId={compartmentId} Lists subscriptions for a compartment.
Oracle Cloud Subscription Service Get subscription GET /subscriptions/{subscriptionId} Retrieves a specific subscription.
Oracle Cloud Subscription Service Suspend subscription POST /subscriptions/{subscriptionId}/actions/suspend Suspends a subscription.
Oracle Cloud Subscription Service Resume subscription POST /subscriptions/{subscriptionId}/actions/resume Resumes a subscription.
Oracle Cloud Subscription Billing List billing accounts GET /20230401/billingAccounts Retrieves billing account records.
Oracle Cloud Subscription Billing Get billing account GET /20230401/billingAccounts/{billingAccountOcid} Retrieves a specific billing account.
Oracle Cloud Subscription Billing List billing runs GET /20230401/billingRuns Retrieves billing run records.
Oracle Cloud Subscription Billing Get billing run GET /20230401/billingRuns/{billingRunOcid} Retrieves a specific billing run.
Oracle Cloud Subscription Billing Create billing run POST /20230401/billingRuns Creates a billing run.
Oracle Cloud Subscription Billing Pause billing run POST /20230401/billingRuns/{billingRunOcid} Pauses a billing run.
Oracle Cloud Subscription Billing Resume billing run POST /20230401/billingRuns/{billingRunOcid}/actions/resume Resumes a billing run.
Oracle Cloud Subscription Billing Resubmit billing run POST /20230401/billingRuns/{billingRunOcid}/actions/resubmit Resubmits a billing run.
Oracle Cloud Subscription Billing Delete billing run DELETE /20230401/billingRuns/{billingRunOcid} Deletes a billing run.
Oracle Cloud Subscription Billing List billing documents GET /20230401/billingDocument Retrieves billing documents.
Oracle Cloud Subscription Billing Get billing document GET /20230401/billingDocument/{billingDocumentOcid} Retrieves a specific billing document.
Oracle Cloud Subscription Billing List billing cycles GET /20230401/billingCycles Retrieves billing cycle records.
Oracle Cloud Subscription Billing Get billing cycle GET /20230401/billingCycles/{billingCycleOcid} Retrieves a specific billing cycle.
Oracle Cloud Subscription Billing Create billing cycle POST /20230401/billingCycles Creates a billing cycle.
Oracle Cloud Subscription Billing Update billing cycle PUT /20230401/billingCycles/{billingCycleOcid} Updates a billing cycle.
Oracle Cloud Subscription Billing Delete billing cycle DELETE /20230401/billingCycles/{billingCycleOcid} Deletes a billing cycle.
Subscription Pricing Service List pricing rules GET /pricingRules Retrieves subscription pricing rules.
Subscription Pricing Service Create pricing rule POST /pricingRules Creates a subscription pricing rule.
Subscription Pricing Service Update pricing rule PUT /pricingRules/{pricingRuleId} Updates a pricing rule.
Subscription Pricing Service Delete pricing rule DELETE /pricingRules/{pricingRuleId} Deletes a pricing rule.

- [APIs](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/apis.htm#apis)
- [API Version Discovery and Framework Configuration](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/apis.htm#api-version-discovery-and-framework-configuration)
- [Customer and Account Setup](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/apis.htm#customer-and-account-setup)
- [Order Management Endpoints](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/apis.htm#order-management-endpoints)
- [Price List Endpoints](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/apis.htm#price-list-endpoints)
- [Receivables Endpoints](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/apis.htm#receivables-endpoints)
- [Internal Subscription and Billing Services](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/apis.htm#internal-subscription-and-billing-services)
- [General Information: Billing Services APIs](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/apis.htm#billing-services-apis)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
