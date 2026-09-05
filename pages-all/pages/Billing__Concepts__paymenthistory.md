# Payment History
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/paymenthistory.htm
- Fetched: 2026-09-05 01:43 CDT

# Payment History

Use the Payment History page to track and monitor your Oracle Cloud Infrastructure paid invoice history. Only paid invoices are shown, in contrast to the Invoices page, which shows all invoices.

You can see both online payments made in Cost Management , and the offline payments. The page includes filter and search settings, and a list of invoices. Use Payment History to:
- [Filter payment history](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/paymenthistory.htm#paymenthistory__filter_payment_hist).
- Monitor payment status of invoices.
- [Review invoice charges](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/paymenthistory.htm#paymenthistory__payment_history)based on type such as Service or Usage.
- [View detailed invoice data](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/paymenthistory.htm#paymenthistory__viewing_invoices_paymenthist).
- [View usage](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/paymenthistory.htm#paymenthistory__view_usage_invoice_paymenthist).
- Download the Payment History table as a CSV file, by clicking the corresponding Download as CSV link.
- [Open a support request](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/paymenthistory.htm#paymenthistory__open_support_req_paymenthist).

## Filtering Payment History

Under Filters , you can filter based on invoice status, invoice type, and starting or ending invoice dates. You can also search for an invoice number directly. The following table describes the Payment History filter fields:

Invoice Filter Description
Status

- Closed : The invoice is closed.
- Payment Submitted : Invoices paid online in Cost Management but not closed.

By default, all statuses are displayed.
Type
- Service : Periodic invoices for Monthly/Annual Commit plans. The invoices appear under Resources on a subscription's detail page's[Billing Schedule section (see the Status field).
- Usage : Pay As You Go invoices, or overage invoices (if you exceed the committed amount for a Monthly/Annual commit period).

By default, all types are displayed.
Subscription ID Filter based on the subscription IDs in the tenancy. Defaults to ALL (all the invoices under Invoice No for the subscription ID).
Start/End Due Dates Allows specifying a date range corresponding to invoice due dates.

The Payment History table automatically refreshes when a custom date range is selected. The default date range is one year in the past, with the end being the current date. If no invoices are available, a message is displayed accordingly.
Search Search based on the invoice number, reference number, payment reference, or total amount.

## Payment History Table

The following table describes the Payment History table fields:

Field Description
Invoice No

The customer invoice number. The Party Name is also indicated in the information icon.

Click the Invoice No to display the Invoice No. details page.
Reference No Subscription plan number.
Status
- Payment Submitted
- 

Closed
Type

Invoice Type
- Service
- 

Usage
Due Date Invoice due date.
Payment Date Invoice payment date.
Payment Ref The payment type when the Cloud order was placed:
- Purchase Order PO
- Credit Card and Number
- PayPal
Payment Method Actual invoice payment method.
Amount paid Total amount paid.
Context (three dots) menu

Open this menu to:
- Download Invoice
- View Usage
- Open Support Request

After clicking the Invoice No , the Invoice No. details page is displayed. This page contains an Invoice Information tab, Payment tab (for paid invoices), and Invoice Lines table for each invoice.

On the Invoice No. details page you can:
- Download an invoice as a PDF
- View usage
- Open a support request

The Invoice No. details page Invoice information tab contains the following information:
- Invoice Date
- Due Date
- Reference No (the plan number)
- Payment Terms
- Payment Reference (PO number at order booking)
- Bill to Address
- Bill to Email
- Total Amount
- Credited Amount
- Adjusted Amount
- Applied Amount
- Amount Due

The Payments tab contains the following:

- Paid On : The invoice payment date, online or offline.
- Paid By : The email of the person making the Account Management payment. If the payment is offline, it appears as an empty field.
- Payment Method : Online or offline payment method. The online payment method shows credit card or PayPal, and represents the payment method used on the Invoices page. The offline payment method represents payments made through other methods, such as wire transfers and checks.
- Amount Paid : This shows amount paid for the invoice

Under Invoice Lines , the following is displayed:
- Order NO
- Subscription Id
Note  
  
For IaaS customers, the ID is same, but for SaaS customers, you can view multiple differing subscription ID lines for the Order No .
- Product
- Start Date/End Date
- Quantity
- Net Unit Price
- (Total invoice line) Amount

## Viewing Invoices

Two options are available for accessing invoices:
- View invoice details and invoice lines on the Payment History page, and individual invoices on the corresponding Invoice No. page.
- Download and save the invoice as a PDF from the Download Invoice context menu.

To view an invoice:
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Payment History .
- Enter the invoice number in the Search field, or click the invoice in the Invoice No. field. The Invoice No. page is displayed.

To download an invoice:
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Payment History .
- Select the invoice from the list of invoices on the Invoices page, or to find the particular invoice, enter the invoice number in the Search field.
- From the context menu, select Download Invoice .
Note  
  
You can also download the invoice by clicking Download Invoice on an invoice's Invoice No. details page, Invoice Information tab.

## Viewing Usage Associated with an Invoice

You can view and monitor your plans usage by viewing the usage through two access points.

Option 1:
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Payment History .
- Enter the invoice number in the Search field.
- From the context menu, select View Usage .

Option 2:
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Payment History .
- Enter the invoice number in the Search Field
- When the invoice appears, click the linked invoice from the Invoice No column.
- Click View Usage at the top of the page. The Subscription Usage page opens but shows you usage related to just the selected invoice number ( Invoice Usage ). A Usage by time chart and Used Services table details the usage. For more information, see[Usage](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/infrastructure_subscriptions.htm#account_management_usage).

## Opening a Support Request

Option 1:

- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Payment History .
- Enter the invoice number in the Search field.
- From the context menu, select Open Support Request .

Option 2:
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Payment History .
- Enter the invoice number in the Search field.
- When the invoice appears, click the linked invoice from the Invoice No column.
- Click Open Support Request at the top of the Invoice No. details page.
Note
