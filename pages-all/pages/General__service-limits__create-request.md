# Creating a Limit Increase Request
- Source: https://docs.oracle.com/en-us/iaas/Content/General/service-limits/create-request.htm
- Fetched: 2026-09-05 02:13 CDT

# Creating a Limit Increase Request

Request an increase for a service limit in Oracle Cloud Infrastructure.

Note  
  
Government Cloud customers can't use the following procedure to request a service limit increase. Instead, see[Requesting a Service Limit Increase for US Government Cloud and US Defense Cloud Tenancies](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#Requesti).

You can submit a request to increase your service limits. If you try to create a resource for which a limit has been met, you're prompted to submit a limit increase request. Also, you can[get details for a submitted request](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/get-request.htm).

The following procedure applies to requests for service limit increases. For details about the subscribed region limit and how to request an increase to such limits, see[Subscribed Region Limits](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/../Concepts/regions.htm#limits). For step-by-step instructions specific to Multicloud subscriptions, see[Requesting a Limit Increase for Multicloud](https://docs.oracle.com/iaas/Content/multicloud/limits-increase.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/create-request.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/create-request.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/create-request.htm#)
- 

Open the Help menu . Under Targeted help , select Request a limit increase .

The Request limit increase window opens.

## 1. General information

Enter the following values:
- Subscription ([Multicloud](https://docs.oracle.com/iaas/Content/multicloud/Oraclemulticloud.htm)): The subscription associated with the request. For step-by-step instructions specific to Multicloud subscriptions, see[Requesting a Limit Increase for Multicloud](https://docs.oracle.com/iaas/Content/multicloud/limits-increase.htm).
Note  
  
Subscriptions aren't applicable to all resource types. If you select a subscription, the limit update applies only to resources provisioned in the associated subscription. When None is selected, the limit increase applies to the displayed region or availability domain.

[Policy information for subscriptions](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/create-request.htm#)

When updating your service limits for a subscription, an administrator in your tenancy must set up the following required policy which you can view by selecting View Policy Statement . The View Policy Statement panel opens with the following policy you can copy:

```

```

Where &lt;group_name&gt; is the group or groups (separated by a comma) that need access in the Console.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
- Request name : User-friendly name for the limit request.
- Reason for request : The reason for the request. If the request is urgent or unusual, then provide details here. Avoid entering confidential information.

### Tagging

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.

Select Next .

## 2. Requested items

- Select Add .
- In the Add requested item panel, select or enter the following values.

- Service (under Select service ): The service that contains the limit you want to increase.
- Limit name (under Select limit ): The limit that you want to increase, and the value that you want to increase it to.

The current limit and usage is displayed under the field when the cursor is in the field.
Note  
  

The questions in the Select limit section depend on the selected service and limit, as in the following examples.
- Database - Exadata service, new resource questions include availability domain, database server limit name and value, and storage server limit name and value.
- Database - Exadata service, existing resource questions are focused on limit values related to the selected database instance.
- Multicloud limits sometimes include questions for multicloud partner region and physical availability zone.
- adw-ecpu-count - Autonomous Data Warehouse ECPU Count limit (for service Database ) questions include database version and cloud provider under Additional details .
- Some Email Delivery limit questions include email domain.

Value questions depend on the scope of the selected limit. A limit that uses an availability domain scope shows limit value questions for each availability domain in the current region. A limit that uses a region scope shows just the one region-specific limit value question.

To list questions for a service, use[ListLimitsIncreaseQuestions](https://docs.oracle.com/iaas/api/#/en/limits-increase/latest/LimitsIncreaseQuestionCollection/ListLimitsIncreaseQuestions).
- Select Add .
The requested item appears in the list table within the Request limit increase window.

To filter items in the list:

From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).
- Optionally edit or delete items.

To perform an action on a limit increase item directly from the list table, select an available option from the Actions menu in the row for that limit increase item:
- Edit : Open the Edit requested item panel to update the limit increase item.
- Delete : Delete the limit increase item.
- Select Next .

## 3. Review and create

Review the limit request, tags, and items and optionally edit before submitting.

To perform an action on a limit increase item directly from the list table, select an available option from the Actions menu in the row for that limit increase item:
- Edit : Open the Edit requested item panel to update the limit increase item.
- Delete : Delete the limit increase item.

Select Submit .

The limit increase request's details page opens with an In Progress status indicator next to the request's name.

A response can take anywhere from a few minutes to a few days. If the request is granted, then a confirmation email is sent to the address provided in the primary contact details.

If Oracle requires extra information about the request, then a follow-up email is sent to the address provided in the primary contact details.
- 

Use the[oci limits-increase limits-increase-request create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/limits-increase/limits-increase-request/create.html)command and required parameters to create a request for a service limit increase:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateLimitsIncreaseRequest](https://docs.oracle.com/iaas/api/#/en/limits-increase/latest/LimitsIncreaseRequest/CreateLimitsIncreaseRequest)
