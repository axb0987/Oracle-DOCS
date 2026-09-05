# Oracle Alloy Subscriptions
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/subscriptions.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/subscriptions.htm#dcoc-content-body)

# Oracle Alloy Subscriptions

Subscription administration in the Operator Console helps operators manage pricing, usage visibility, exports, and lifecycle actions.

## Subscription Administration

Open the Subscriptions workspace from My Tools on the Operator Console home page or from Business Operations in the navigation menu. The subscriptions list provides the operating view for active customer subscriptions and supports CSV export for local review.

The exported file includes subscription name, subscription number, payment model, status, and start and end dates.

## Subscription Details and Resources

Each subscription opens to a details page that shows the compartment, subscription ID, subscription number, subscription type, price list name, price list change policy, billing account, and contract start and end dates.

The resource pane groups the core subscription views into Usage, Rate Card, and Usage Statements so that end customers can move from contract data to billing and consumption review without leaving the subscription context.

## Pricing, Base Prices, and Discount Rules

The Rate Card view provides the contractual base prices for services in the subscription and supports CSV export when offline review is required. During contracting, the values shown are list prices and do not reflect negotiated adjustments after discounts are applied. From the same view, End customer can create pricing rules or review existing pricing rules that are associated with the subscription.

Pricing rules support two rule types: contractual discounts for initial order processing and promotional programs for existing customers. Rules can target one subscription or all subscriptions, and they can apply to all products or selected products by SKU or discount group. When SKU targeting is used, enter SKUs directly or upload a CSV file.

Pricing rules do not stack. When overlapping rules apply, the rule with the higher discount percentage takes precedence. The effective start date must be the next day or later.

## Usage and Usage Statements

The Usage view shows the total active commitments, current usage, and overage for the subscription. This view also shows whether the subscription follows a contract price model, in which prices remain fixed for the subscription term, or a current price model, in which prices track the current price list in effect.

Usage statements provide downloadable CSV-based billing detail. Filter usage statements by published date when dnd customer need to locate a specific statement.

## Lifecycle Status Management

Subscription records expose lifecycle status so that Alloy partners can review or change whether a subscription is active, suspended, or terminated. Suspension is used for conditions such as fraud review or nonpayment.

During the initial suspension grace period, existing resources continue to run, but new resource creation and portal access are blocked. If the subscription remains suspended, resources are later shut down and the subscription can transition to termination. Lifecycle changes generate customer email notifications so that status changes remain visible to affected users.

- [Oracle Alloy Subscriptions](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/subscriptions.htm#oracle-alloy-subscriptions)
- [Subscription Administration](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/subscriptions.htm#subscription-administration)
- [Subscription Details and Resources](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/subscriptions.htm#subscription-details-and-resources)
- [Pricing, Base Prices, and Discount Rules](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/subscriptions.htm#pricing-base-prices-and-discount-rules)
- [Usage and Usage Statements](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/subscriptions.htm#usage-and-usage-statements)
- [Lifecycle Status Management](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/subscriptions.htm#lifecycle-status-management)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
