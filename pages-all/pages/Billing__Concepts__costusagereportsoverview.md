# Cost Reports
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm
- Fetched: 2026-09-05 01:43 CDT

# Cost Reports

Cost reports are comma-separated value (CSV) files and reflect the cost of resource consumption. They're generated daily and are stored in an Object Storage bucket. Use the Cost and Usage Reports page to download and access the reports.
Important  
  
Usage reports were deprecated on January 31, 2025. Instead, you can use[cost reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm#costreports)in the[OCI proprietary format](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm#costreports)and[FOCUS format](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm#costreports)to analyze your consumption. For more information, see[Cost Report Types](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm#costreports). You can continue to access your existing usage report CSV files until July 31, 2025.

A cost report is a comma-separated value (CSV) file that's similar to a usage report, but also includes cost columns. The report can be used to obtain a breakdown of your invoice line items at resource-level granularity. As a result, you can optimize your Oracle Cloud Infrastructure spending, and make more informed cloud spending decisions.

Industry-standard FOCUS CSV cost reports, which conform to the[FinOps Open Cost &amp; Usage Specification (FOCUS)](https://focus.finops.org/#specification), are also generated and available on the Cost and Usage Reports page. For more information, see[Cost Report Types](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm#costreports). FOCUS CSV reports are available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
Note  
  
Cost reports don't apply to non-metered tenancies.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).

To use cost reports, the following policy statement is required:
```

```

Note  
  
This example has a specific tenancy OCID, because the reports are stored in an Oracle-owned Object Storage bucket hosted by Oracle Cloud Infrastructure, and not a customer's tenancy.

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

## Cost Report Types

Both OCI proprietary cost reports and FOCUS cost reports are available on the Cost and Usage Reports page to download. Cost reports are automatically generated every six hours, and are stored in an Oracle-owned Object Storage bucket. The reports contain one row per each Oracle Cloud Infrastructure resource (such as instance, Object Storage bucket, VNIC) per hour along with consumption information (usage, price, cost), metadata, and tags. Cost reports generally contain six hours of usage data, and occasionally late-arriving data, but the data can be delayed up to 24 hours. Cost reports are retained for one year.

[FOCUS (FinOps Open Cost &amp; Usage Specification)](https://focus.finops.org/#specification)is an open source specification and schema for cloud billing data. FOCUS reports in the OCI Console are partitioned by usage date, and they're displayed in a collapsible and expandable folder structure by year, month, and day to aid viewing. For example, reports for usage occurring on May 24, 2024 are found under FOCUS Reports &gt; 2024 &gt; 05 &gt; 24 . For more information, see[Listing Cost Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/list-cost-usage-report.htm).

Cost reports can contain corrections. Corrections are added as new rows to the report, with the`lineItem/iscorrection`column set and the`referenceNo`value of the corrected line populated in the`lineItem/backReference`column.

The file name for each cost report is appended with an automatically incrementing numerical value, and the first file is appended with`-00001.csv.gz`. Cost report files are split into multiple files when more than 1 million records are present in the cost report file. When a file split occurs, new successive files are generated and are appended with`-00002.csv.gz`,`-00003.csv.gz`, and so on, for each file split. If the cost report file size stays under the file size threshold, then file splitting doesn't occur and only a single file is generated.

The file naming for FOCUS reports corresponds to the year, month, and day that the usage occurred.

### OCI Proprietary Cost Report Schema

The following table shows the OCI proprietary cost report schema.

Field Name Description
`lineItem/referenceNo`Line identifier. Used for debugging and corrections.
`lineItem/TenantId`The identifier (OCID) for the Oracle Cloud Infrastructure tenant.
`lineItem/intervalUsageStart`The start time of the usage interval for the resource in UTC.
`lineItem/intervalUsageEnd`The end time of the usage interval for the resource in UTC.
`product/service`The service that the resource is in.
`product/compartmentId`The ID of the compartment that contains the resource.
`product/compartmentName`The name of the compartment that contains the resource.
`product/region`The region that contains the resource.
`product/availabilityDomain`The Availability domain that contains the resource.
`product/resourceId`The identifier for the resource.
`usage/billedQuantity`

The quantity of the resource that has been billed over the usage interval.

Note:`billedQuantity`,`myCost`, and`unitPrice`are inclusive of Overage numbers and broken nodes in dedicated GPU pools. Broken nodes aren't charged to you, even though they're included in the`billedQuantity`.
`usage/billedQuantityOverage`The usage quantity that's billed as an overage over your Oracle Universal Credits commit, or usage quantity that's billed against your Funded Allocation commitment.

Note: This quantity doesn't include broken nodes in dedicated GPU pools, which aren't billed to you.
`cost/subscriptionId`A unique identifier associated with your commitment or subscription.
`cost/productSku`The Part Number for the resource in the line.
`product/description`The product description for the resource in the line.
`cost/unitPrice`

The cost billed to you for each unit of the resource used.

Note:`billedQuantity`,`myCost`, and`unitPrice`are inclusive of Overage numbers.
`cost/unitPriceOverage`The cost per unit of usage for overage usage of a resource.
`cost/myCost`

The cost charged for this line of usage.`myCost`is equal to`usage/billedQuanty`*`cost/unitPrice`.

Note:`billedQuantity`,`myCost`, and`unitPrice`are inclusive of Overage numbers.
`cost/myCostOverage`The cost billed for overage usage of a resource.
`cost/currencyCode`The currency code for your tenancy.
`cost/billingUnitReadable`The unit measure associated with the`usage/billedQuantity`in the line. This field is structured as:`<count> <GiB/MiB/TiB/PiB> <HOURS/MILLIS/MONTH/SECOND> <measure>`. For example:`ONE GiB MONTH DATA_TRANSFERRED`.
`cost/skuUnitDescription`The usage for a particular SKU.
`cost/overageFlag`The cost when you have exceeded your[Oracle Universal Credits](https://www.oracle.com/cloud/universal-credits/)
`lineItem/isCorrection`Used if the current line is a correction. See the`lineitem/backReference`column for a reference to the corrected line item.
`lineItem/backReferenceNo`Reference to the line item being corrected. Populated when the row is a correction (`lineItem/isCorrection = true`) generated to roll back or amend a prior line item. Contains the`lineItem/referenceNo`of the original line, or the most recent correction, that this row amends. For non-correction rows, this field is blank. Use together with`lineItem/isCorrection`to chain and reconcile corrections.
`cost/attributedCost``cost/attributedCost`and`usage/attributedUsage`are the same as`cost/myCost`and`usage/billedQuantity`for any non-virtual machine cluster type resource. Otherwise, this field shows the cost for pluggable databases in a virtual machine cluster. For more information, see[Viewing Cost and Usage from Virtual Machine Cluster Pluggable Databases](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#view_vmclusterpdb_costusage).
`usage/attributedUsage``cost/attributedCost`and`usage/attributedUsage`are the same as`cost/myCost`and`usage/billedQuantity`for any non-virtual machine cluster type resource. Otherwise, this field shows the usage for pluggable databases in a virtual machine cluster. For more information, see[Viewing Cost and Usage from Virtual Machine Cluster Pluggable Databases](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#view_vmclusterpdb_costusage).
`tags/`The report contains one column per tag definition.

### FOCUS Cost Report Schema

The following table shows the FOCUS cost report schema, including the mapping to the OCI proprietary cost report schema.

Column ID Display Name Proprietary Mapping Type Description
AvailabilityZone Availability Zone`product/availabilityDomain`String Logical Availability domain.
BilledCost Billed Cost`cost/myCost`BigDecimal The calculated cost after all discounts have been applied.

Note : The Billed Cost doesn't include taxes and might vary from the invoice amount.
BillingAccountId Billing Account ID`cost/subscriptionId`String Subscription identifier.
BillingAccountName Billing Account Name NONE String Null
BillingCurrency Billing Currency`cost/currencyCode`CurrencyCode Currency code for the cost.
BillingPeriodEnd Billing Period End NONE DateTime The end date and time of the billing period.

Note : The billing period start and end is based on the current monthly boundary of usage, and might be different from the date when commitment invoices are issued.
BillingPeriodStart Billing Period Start NONE DateTime The start date and time of the billing period.
ChargeCategory Charge Category`lineItem/isCorrection`String

Indicates an upfront or recurring fee, cost of usage that already occurred, an after-the-fact adjustment (credits), or taxes. Cost of usage that already occurred (`Usage`), or an after-the-fact adjustment (`Adjustment`).
ChargeDescription Charge Description`product/description`String The SKU description of the charge's purchase and price.
ChargeFrequency Charge Frequency NONE String Indicates how often a charge occurs, and is commonly used to understand the recurrence period. Defaults to`Usage-based`.
ChargePeriodEnd Charge Period End`lineItem/intervalUsageEnd`String Start time of the usage in milliseconds since epoch.
ChargePeriodStart Charge Period Start`lineItem/intervalUsageStart`String End time of the usage in milliseconds since epoch.
ChargeSubcategory Charge Subcategory NONE String Null
CommitmentDiscountCategory Commitment Discount Category NONE String Null
CommitmentDiscountId Commitment Discount ID NONE String Null
CommitmentDiscountName Commitment Discount Name NONE String Null
CommitmentDiscountType Commitment Discount Type NONE String This field is null because OCI doesn't have the concept of reserved instances.
EffectiveCost Effective Cost`cost/myCost`BigDecimal The calculated cost, inclusive of all applicable discounts.
InvoiceIssuerName Invoice Issuer NONE String Defaults to`Oracle`as the only indicated value.
ListCost List Cost NONE BigDecimal Calculated cost based on the current list price.
ListUnitPrice List Unit Price NONE BigDecimal Based on the current global list price, the unit price for a single pricing unit of the associated SKU, exclusive of any discounts.
PricingCategory Pricing Category NONE String Null
PricingQuantity Pricing Quantity`usage/billedQuantity`BigDecimal Hourly rounded billable value, if applicable.
PricingUnit Pricing Unit`cost/skuUnitDescription`String SKU units description.
ProviderName Provider NONE String Defaults to`Oracle`.
PublisherName Publisher NONE String`Oracle`except for third-party marketplace listings.
Region Region`product/region`String The region associated with the cost entry, indexed together with tenantId, compartmentId, resourceId, and resourceMeter for uniqueness.
ResourceId Resource ID`product/resourceId`String Unique resource identifier, indexed together with tenantId, compartmentId, region, and resourceMeter for uniqueness.
ResourceName Resource Name NONE String This field is null because Oracle doesn't publish this value in its cost reports.
ResourceType Resource Type NONE String The kind of resource the charge applies to. For example,`Storage`.
ServiceCategory Service Category NONE String Enum values for a service classification accepted in FOCUS.
ServiceName Service Name`product/service`String The service associated with the resource, indexed together with tenantId, compartmentId, resourceId, and resourceMeter for uniqueness.
SkuId SKU ID`cost/productSku`String The unique SKU ID.
SkuPriceId SKU Price ID NONE String This field is null because this construct doesn't exist in OCI.
SubAccountId Sub Account ID`lineItem/TenantId`String The identifier (OCID) for the Oracle Cloud Infrastructure tenant.
SubAccountName Sub Account Name NONE String The tenancy name.
Tags Tags`tags/`JSON Tags associated with the entry, stored as a byte array.
UsageQuantity Usage Quantity`usage/billedQuantity`BigDecimal Hourly rounded billable value, if applicable.
UsageUnit Usage Unit`cost/skuUnitDescription`
