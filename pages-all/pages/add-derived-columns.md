# Add Derived Columns
- Source: https://docs.oracle.com/iaas/analytics-for-applications/doc/add-derived-columns.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/analytics-for-applications/doc/add-derived-columns.html#dcoc-content-body)

# Add Derived Columns

Add a derived column to an existing subject area.
- Sign in to your service.
- In Oracle Fusion Data Intelligence Console , click Semantic Model Extensions under Application Administration .
- On the Semantic Model Extensions page, click User Extensions .
You see the main and existing customization branches.
- In the User Extensions region, under Customization Branches, click a branch to open the Branch page.
- On the Branch page, click Add Step .
- In Add Step, select Add a Column .
You see the wizard sequence to add a column.
- In step 1 of the wizard, enter a name for your customization step, for example, Regional Revenue and add a brief description.
- Select a target subject area to which you want to add the column. For example, Profitability .
You see the details of the selected subject area.
- Select the presentation folder within the selected subject area and the logical table to which you want to add the column.
- Click Next .
You see the Create Column dialog in step 2 of the wizard.
- In step 2 of the wizard, define your new column using these instructions:

- In Create Column, enter a display name.
- Under Data Elements , search for a data element from the subject area that you had selected previously.
- From the search results, double-click the data element to place it in the text pane.
- Under Functions , search for a function to construct a column using expressions. From the search results, double-click the applicable result to add it to the central text pane. For example, search for functions like "Filter" or "Avg" to construct expression-based columns. A sample expressions to derive the average supplier payment days is`avg(ROUND(((CASE WHEN Invoice Received Date is not null THEN (Financials - AP Payments.Payment Date.Payment Date - Invoice Received Date) ELSE (Financials - AP Payments.Payment Date.Payment Date - Financials - AP Invoices.Invoice Date.Invoiced Date) END)/Financials - AP Payments.Facts - Analytics Currency.Total Payment Count),0))`.
- Click Validate , and then click Save .
- Optional: If you want the underlying measure of the column to be calculated to a specific level of a predefined dimensional hierarchy, then complete these steps:

- Click the Hierarchy Level-Based Aggregation icon.
- In the Hierarchy Level-Based Aggregation dialog, select the dimension, level, and then click OK .
- Click Add Dimension to add more dimensions.
- Click Next .
- Optional: Select additional subject areas to add the fact.
- Click Finish .
You see a message that your step is being applied to the customization branch. After it's applied, you see the new customization step in the customization branch. You can now apply the customization branch to the main branch or edit it to add more steps.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
