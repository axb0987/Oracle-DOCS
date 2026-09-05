# Invoices
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm
- Fetched: 2026-09-05 01:43 CDT

# Invoices

Use the Invoices page to track and monitor your Oracle Universal Credits invoice activity.

You can:
- [Filter invoices](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm#account_management_invoices__filter_invoices).
- [Pay an invoice](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm#account_management_invoices__paying_invoices).
- Monitor payment status of invoices.
- [Review invoice charges](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm#account_management_invoices__invoice_table)based on the Service or Usage type (or both).
- [View detailed invoice data](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm#account_management_invoices__viewing_invoices).
- Download the Invoices table as a CSV file, by clicking the corresponding Download as CSV link.
- [View usage](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm#account_management_invoices__view_usage_invoice)for a particular invoice.
- [Open a support request](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm#account_management_invoices__open_support_req).

The page includes filter and search settings, and a list of invoices.
Note  
  
If one or more invoices aren't visible on the Invoices page, you can also check for invoices at the[Oracle Customer Center](https://customercenter.oracle.com/).

## To Filter Invoices

Under Filters , you can filter based on invoice status, invoice type, and starting or ending invoice dates. You can also search for an invoice number directly. The following table describes the Invoices filter fields:

Invoice Filter Description
Status

- Open : The invoice is open.
- Closed : The invoice is closed.
- Past Due : The invoice is past due.
- Payment Submitted : Invoices paid online in Cost Management but not closed.

By default, all statuses are displayed.
Type
- Service : Periodic invoices for Monthly/Annual Commit plans. The invoices appear under Resources on a subscription's detail page's[Billing Schedule section (see the Status field).
- Usage : Pay As You Go invoices, or overage invoices (if you exceed the committed amount for a Monthly/Annual commit period).

By default, all types are displayed.
Subscription ID Filter based on the subscription IDs in the tenancy. Defaults to ALL (all the invoices under Invoice No for the subscription ID).
Start/End Invoice Dates Allows specifying the invoice date range. The Invoices table automatically refreshes when a custom date range is selected. The default date range is one year in the past, with the end being the current date. If no invoices are available, a message is displayed.
Search Search based on the invoice number, reference number, payment reference, or total amount.

## Invoices Table

Under Filters , a tabular list of the invoices is displayed, where you can also[pay an invoice](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm#account_management_invoices__paying_invoices). The following table describes the Invoices table fields:

Field Description
Invoice No

The customer invoice number. The Party Name is also indicated in the information icon.

Click the Invoice No to display the Invoice No. details page.
Reference No Subscription plan number.
Status
- Open
- Closed
- Past Due
- Payment Submitted
Type

Invoice Type:
- Service
- 

Usage
Invoice Date Invoice generation date.
Due Date Invoice due date.
Payment Ref

The payment type when the Oracle Cloud order was placed:
- Purchase Order PO
- Credit Card and Number
- PayPal
Total Amount Total invoiced amount.
Balance Due Balance remaining on the invoice. The information icon also displays the following:
- Total
- Credited
- Adjusted
- Applied
- Amount Due
[Pay](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm#account_management_invoices__paying_invoices)Allows you to[pay for an unpaid or past due invoice](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm#account_management_invoices__paying_invoices)using a credit card or PayPal, through the secure PCI-compliant payment service.

Note: This link doesn't appear if you have already paid the invoice.
Actions (three dots) menu

Open this menu to:
- Download Invoice
- View Usage
- Open Support Request

Click the Invoice No to display the Invoice No. details page. This page contains an Invoice Information tab, Payment tab (for paid invoices), and Invoice Lines table for each invoice.

On the Invoice No. details page you can:
- Pay an invoice (open and past due invoices)
- Download an invoice as a PDF
Note  
  
You can also download the entire Invoices page table as a CSV file, by clicking the corresponding Download as CSV link.
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
- Payment Method : Online or offline payment method. The online payment method shows credit card or PayPal, and represents the payment method entered at order booking. The offline payment method represents payments made through other methods, such as wire transfers and checks.
- Amount Paid : The amount paid for the invoice

Under Invoice Lines , the following is displayed:
- Order No
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
- View invoice details and invoice lines on the Invoices page, and individual invoices on the corresponding Invoice No. details page.
- Download and save the invoice as a PDF from the Download Invoice context menu.

To view an invoice:
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Invoices .
- Enter the invoice number in the Search field, or click the invoice in the Invoice No. field. The Invoice No. details page is displayed.

To download an invoice:
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Invoices .
- Select the invoice from the list of invoices on the Invoices page, or to find the particular invoice, enter the invoice number in the Search field . The Invoice No. details page is displayed.
- Click Download Invoice on the invoice's Invoice No. page. A notification is displayed that the invoice download has started, and another notification is displayed after the download is successful.

## Paying Invoices

Credit Card and PayPal are available options for making a payment. Payments amounts are restricted to amounts less than USD 100,000 (you can't pay for any charge over USD 100,000 through the Console). Only open and past due invoices have the pay function available on the Invoice No. page.
Note  
  
Both payment options might not be available for every country.

To pay using a credit card :
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Invoices .
- Enter the invoice number in the search field.
- Click Pay for the associated invoice. The Oracle payment window is displayed with the available payment methods. You can pay with either an existing payment method, or enter a new one.
- To add a new credit card, click Credit Card . An Add Payment Method pop-up is displayed.
- After entering your billing and credit card details, click Finish . The newly added credit card is now available as a payment method in the Oracle payment window.
- Select the credit card that you want to pay with and click Pay Now . A confirmation is displayed that the payment is successful. On the Invoices page , the payment's Status field changes to Payment Submitted , to indicate that you submitted the payment. You can then monitor the payment on the Payment History page (see[Payment History](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/paymenthistory.htm)for more information).

To pay using PayPal :

- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Invoices .
- Enter the invoice number in the search field.
- Click Pay for the associated invoice. The Oracle payment window is displayed with the available payment methods. You can pay with either an existing payment method, or enter a new one.
- To add PayPal as a payment method, click PayPal . A PayPal pop-up is displayed, where you can enter your PayPal credentials, and choose the PayPal payment source.
- After selecting your PayPal payment options, click Continue and Agree &amp; Pay . PayPal is now available as a payment method.
- Select the PayPal account that you want to pay with and click Pay Now . A confirmation is displayed that the payment is successful. On the Invoices page , the payment's Status field changes to "Payment Submitted" to indicate that you submitted the payment. You can then monitor the payment on the Payment History page (see[Payment History](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/paymenthistory.htm)for more information).

## Viewing Usage Associated with an Invoice

You can view and monitor your plans usage by viewing the usage through two access points.

Option 1:
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Invoices .
- Enter the invoice number in the Search field.
- From the context menu, select View Usage .

Option 2:
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Invoices .
- Enter the invoice number in the Search Field
- When the invoice appears, click the linked invoice from the Invoice No column.
- Click View Usage at the top of the page. This opens the Subscription Usage page but shows you usage related to only the selected invoice number ( Invoice Usage ). A Usage by time chart and Used Services table details the usage. For more information, see[Usage](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/infrastructure_subscriptions.htm#account_management_usage).

## Viewing Payments Made on an Invoice

You can check the payment status of a paid invoice (only paid invoices are shown) and reconcile your account. Paid invoices associated with the Oracle Cloud account on file are available. The invoice status is provided for current or past due invoices. Payment details are also provided.
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Invoices .
- Enter the invoice number in the Search field, or filter within a specific date range.
- Once the invoice appears, click the linked invoice from the Invoice No column. See[Invoices Table](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm#account_management_invoices__invoice_table)for more information on the fields and descriptions of the Invoices and Invoice No. details pages.
- To show payment information, click Payment at the top of the page.

## Opening a Support Request

Option 1:

- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Invoices .
- Enter the invoice number in the Search field.
- From the context menu, select Open Support Request .

Option 2:
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Invoices .
- Enter the invoice number in the Search field.
- When the invoice appears, click the linked invoice from the Invoice No column.
- Click Open Support Request at the top of the Invoice No. details page.
Note  
  
For the best service, open a support request from the associated page, page table, or billing entry where an issue has been encountered, rather than opening a support request from the main support menu. As a result, a resolution for your billing-related issue can be more easily tracked and targeted.

## What Happens If a Credit Card is Declined and the Payment Isn't Processed?
- You will receive an email for one of two reasons:
- New orders when the initial credit card authorization/charge fails.
- Existing orders when the credit card authorization for the current billing cycle has failed (previous authorization might have been successful).
- The email directs you to the Oracle Store to update your credit card information for payment.
- The invoice payment status for the failed payment remains as Payment Submitted until a payment has been applied.
- You continue to receive emails from Oracle Collections until the payment has been applied.

To create an Oracle Store Profile:
- Go to the Oracle Store at[https://shop.oracle.com/](https://shop.oracle.com/apex/f?p=dstore:home:0).
- Select "New User? " from the top left of the screen.
- Complete your profile.
- To verify your e-mail address, open your email and click the link.
- Click Continue .
- Sign in to the Oracle Store at[https://shop.oracle.com/](https://shop.oracle.com/apex/f?p=dstore:home:0).
- Select Dashboard under the user icon.
- Go to the Payment Center section.
- Select Payments Due .
- The next page will list your order and allow you to submit your payment.

Already have an existing Oracle Store Profile?
- Go to the Oracle Store at[https://shop.oracle.com/](https://shop.oracle.com/apex/f?p=dstore:home:0).
- Sign in to the Oracle Store using your Oracle Account.
- Select Dashboard under the user icon.
- Go to the Payment Center section.
- Select Payments Due .
-
