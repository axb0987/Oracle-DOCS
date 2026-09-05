# Order Management
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/order-management.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/order-management.htm#dcoc-content-body)

# Order Management

Use this section to learn how operators create internal orders, review and process pending requests, manage order records, track activation status, and resend activation emails for internal customers.

Use order management workflows when internal teams, departments, or employees need OCI resources in the Dedicated Region environment. Operators perform these tasks from the Operator Console. Orders area and the Subscription Request application. Keep order administration aligned with the assigned operator role, internal approval process, and activation status of the resulting tenancy.

Order Management Area Use Primary Operator Actions
Internal order creation Create an order request for an internal customer that needs a Dedicated Region tenancy and OCI resources. Open Orders, select Internal Orders, create the internal order, provide the requester and tenancy administrator details, and submit the order for review.
Pending request processing Approve or deny internal order requests from the Subscription Request application. Open Pending Requests, review one or more requests, and use Approve Selected or Deny Selected when the operator is authorized to process the request.
Order list management Search and inspect existing internal orders and subscription information. Use filters on the Orders page, select the required order, and review order details such as service name, subscription count, subscription description, and subscription ID.
Activation tracking Help internal customers troubleshoot order activation issues. Use Order Activation Tracker, enter the order number, and review order status, ID numbers, activation status, and activation history.
Activation email resend Send or reissue the activation email when the internal customer did not receive it or needs it sent to a different address. Open the tracked order, select Resend Activation Email from Activation History, enter the target email address, and send the message.

### Create an Internal Order

Create an internal order when an internal customer needs access to OCI resources in the Dedicated Region environment.
- 

On the Operator Console home page, under My tools, select Orders.
- 

In the navigation menu, select Internal Orders.
- 

Select Create internal order.
- 

Enter the requester first name, requester last name, tenancy administrator email address, cost center, and department.
- 

To preserve internal approval or onboarding context, add notes.

### Process Internal Order Requests

Process internal order requests only when the assigned role allows access to pending and processed requests in the Subscription Request application.
- 

If the Subscription Request application is not already open, go to the Order page in the Operator Console and select Create Internal Order to open the application.
- 

Select Pending Requests to review order requests that are waiting for action.
- 

Review the request details before acting on the order. When multiple requests are ready for the same decision, select the applicable orders together.
- 

Select Approve Selected or Deny Selected to process the selected requests.

After an order is approved, the activation email is sent automatically to the requestor with onboarding tasks. The tenancy is allocated after activation is complete.

### Manage Orders

Use the Orders page under Order Management to find and review internal customer orders and related subscription details.
- 

Go to the Orders page under Order Management.
- 

Use filters to narrow the order list when searching for specific order criteria.
- 

Select the order from the order list.
- 

Review the order details, including service name, number of subscriptions, subscription description, and subscription ID number.

### Track Activation Status

Use Order Activation Tracker to help internal customers resolve order activation issues and to confirm where an order is in the activation flow.
- 

Go to the Orders page.
- 

Select Order Activation Tracker.
- 

Enter the order number and select Track.
- 

Review the status shown, ID numbers, activation status, and activation history. Use this information to troubleshoot activation issues or determine the next follow-up action.

### Resend Activation Email

Resend the activation email when the internal customer did not receive the original email or when the activation link must be sent to a different email address.
- 

Go to the Orders page.
- 

Select Order Activation Tracker.
- 

Enter the order number and select Track.
- 

In Activation History, select Resend Activation Email.
- 

Enter the email address. Use the email address from the original Fusion Console order or provide a new email address when the activation email must be redirected.
- 

Select Send.

### Order Management Guardrails

Keep order management aligned with least-privilege operator access and auditable onboarding records.

Guardrail Implementation Guidance
Role-based access Limit pending-request processing, order creation, activation tracking, and activation-email resend actions to the operator roles that require those capabilities.
Approval recordkeeping Retain the order number, requester information, tenancy administrator email, cost center, department, subscription ID, activation status, and any notes used during review.
Activation follow-up Use activation history before resending an email so the operator can confirm the current state and avoid unnecessary duplicate messages.
Customer communication When an activation issue requires follow-up, use the order status, ID numbers, activation status, and activation history to provide a clear next step to the internal customer.

- [Order Management](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/order-management.htm#order-management)
- [Create an Internal Order](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/order-management.htm#create-an-internal-order)
- [Process Internal Order Requests](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/order-management.htm#process-internal-order-requests)
- [Manage Orders](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/order-management.htm#manage-orders)
- [Track Activation Status](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/order-management.htm#track-activation-status)
- [Resend Activation Email](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/order-management.htm#resend-activation-email)
- [Order Management Guardrails](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/order-management.htm#order-management-guardrails)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
