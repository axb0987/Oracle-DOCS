# Listing Product Information for a Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-products-product-summary.htm
- Fetched: 2026-09-05 01:43 CDT

# Listing Product Information for a Subscription

List the product information and usage details that are specific to a subscription ID's reward usage period.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-products-product-summary.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-products-product-summary.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-products-product-summary.htm#)
- 

- Open the navigation menu and select Billing &amp; Cost Management . Under Programs and Rewards , select Oracle Support Rewards .

The Oracle Support Rewards page opens.
- To view the usage associated with the rewards, for a particular accrual date, select the Actions menu (three dots) to the right side in that row and select View Usage .

The View Usage panel lists the products that are eligible for rewards, along with the associated usage amount, and the earned rewards amount for each product.
Note  
  
The View Usage details aren't available for dates where rewards data was updated manually.

You can filter the list based on eligibility, by selecting an Eligible or Non-eligible value from the corresponding Eligibility list. You can also search for product names, product numbers, or partial keywords from product names, by entering them in the search field. The list updates dynamically based on the search parameters.
- To download a copy of the table in CSV format, select Download CSV .
- 

Use the[oci usage rewards product-summary list-products](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/usage/rewards/product-summary/list-products.html)command and required parameters to list the product information and usage details that's specific to a subscription ID's reward usage period:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ListProducts](https://docs.oracle.com/iaas/api/#/en/usage-proxy/latest/ProductSummary/ListProducts)
