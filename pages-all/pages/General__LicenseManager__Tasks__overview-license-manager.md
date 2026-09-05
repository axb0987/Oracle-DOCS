# Viewing Product License Activity in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/overview-license-manager.htm
- Fetched: 2026-09-05 02:11 CDT

# Viewing Product License Activity in License Manager

Get an overview of license activity within License Manager.

Open the navigation menu and select Governance &amp; Administration . Under License Manager , select Overview .

The License Manager Overview page opens.

The License Manager Overview page provides an overall summary of your license activity. The page allows you to get quick insights into your most utilized licenses, Bring Your Own License (BYOL) resources needing the most licenses by OCPUs and ECPUs, an overall count of BYOL and license included resources, and licenses at or near expiration.

The top of the page has tiles to indicate the totals for the following:
- Product Licenses : The total number of product licenses.
- BYOL Resources : The total number of BYOL resources. Corresponds to what is listed in the Top BYOL resources by OCPUs and Top BYOL resources by ECPUs tables.
- License Included Resources : The count of license-included Database PaaS resources you have created in the tenancy.
- Licenses at or near expiration : The total number of license records within 90 days of expiration.

Following the totals summary, the Top Utilized Product Licenses table displays the following:
- Product License : The product license name. Select the linked name to go to its[details](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/get-product-license.htm)page.
- Status : The license status, which can be the following:
- Ok : The license has active license records for Oracle products, and active license records and an image associated for third-party licenses.
- Incomplete : The Oracle product license was created without any active license records within it. For third-party products, the status is Incomplete if there aren't any active records or images associated with the license.
- Issues Found : Over-subscribed licenses. The license requirement exceeds the entitlement.
- Warning : Shown for license records when all licensing requirements (mandatory options or base product licenses) aren't found in License Manager. Warning is also shown if data hasn't been updated in more than 24 hours.
- Requirement : What all the resources attributed to a license need, to be considered fully licensed. The licensing requirement is calculated every hour.
- Entitlement : The sum of all license counts in your license records.
- Metric : The metric that matches your licensing terms.

The Top BYOL resources by OCPUs table lists the following:
- Resource OCID : Select the link to go directly to the BYOL resource.
- OCPUs : The total number of OCPUs used by the BYOL resource.
- Compartment : The associated compartment.

The Top BYOL resources by ECPUs table lists the following:
- Resource OCID : Select the link to go directly to the BYOL resource.
- ECPUs : The total number of ECPUs used by the BYOL resource.
-
