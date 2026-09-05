# Fusion Pricing Administration
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-pricing-administration.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-pricing-administration.htm#dcoc-content-body)

# Fusion Pricing Administration

Fusion pricing defines the baseline catalog that underpins Oracle Alloy commercial operations. Price lists hold the SKUs and baseline charges used for Oracle Alloy services and resources. You can create price lists or duplicate an existing price list when you need a different currency, customer-specific catalog, or pricing model.

A new price list remains in progress until it is populated and approved. Treat price-list creation, population, and approval as one continuous workflow.

## Price List Maintenance and Catalog Updates

Use Manage Price Lists in Fusion to review and search price-list content by SKU, item description, pricing unit of measure, and related line attributes before you make a catalog change.

When Oracle introduces new SKUs, add them to each price list that must expose the service. Create the recurring sale price charge, and set the future effective date that controls when the new catalog entry becomes active.

Changes to baseline prices are not retroactive. End-date current charges and future-date replacement charges when you update an existing item.

## Excel-Based Bulk Price Maintenance

For broad catalog updates, use the ADF Desktop Integration add-in for Excel to download the price-list workbook, authenticate to Fusion, edit the required rows, and upload the changes. This workflow is suited to populating a new price list, updating many base prices in one pass, and editing existing tier attributes at scale.

For active pricing records, duplicate the existing row, end-date the current charge at least 48 hours in the future, and start the replacement charge immediately after that end date. This approach makes the catalog change effective without overwriting active history.

## Discounting, Tiered Pricing, and Currency Enablement

Use the Discounting Spreadsheet during order entry when a new order requires contractual discounts that differ from the baseline catalog. Because the discounting attachment must be added before the order is submitted, manage subscription-level discounts for existing subscriptions in the Operator Console through pricing rules.

Fusion remains the control point for baseline tiered pricing and alternate-currency setup. Configure tiered adjustments by SKU in the price list, use price override as the supported adjustment type, and enable allowed override currencies and functional currency conversions before you use a new currency in ordering or billing.

- [Fusion Pricing Administration](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-pricing-administration.htm#fusion-pricing-administration)
- [Price List Maintenance and Catalog Updates](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-pricing-administration.htm#price-list-maintenance-and-catalog-updates)
- [Excel-Based Bulk Price Maintenance](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-pricing-administration.htm#excel-based-bulk-price-maintenance)
- [Discounting, Tiered Pricing, and Currency Enablement](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/fusion-pricing-administration.htm#discounting-tiered-pricing-and-currency-enablement)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
