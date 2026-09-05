# Inviting a Tenancy to Join an Organization
- Source: https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-create.htm
- Fetched: 2026-09-05 02:12 CDT

# Inviting a Tenancy to Join an Organization

Create an invitation to join an organization and asynchronously send the invitation to the recipient tenancy.

If you have the correct limits, you can invite another tenancy to join your organization. If the tenancy joins your organization, its subscription is managed by the parent tenancy.
Caution  
  
Tenancies that only have SaaS or Multicloud subscriptions can't become standalone after joining an organization. They can only transfer to a new organization. To become standalone again, a valid Universal Credit Model subscription must be activated into the child tenancy first.

For more information about the limits related to inviting another tenancy, see[Organization Limits](https://docs.oracle.com/en-us/iaas/Content/General/organization/../service-limits/default.htm#organizations-limits).

To accept the invitation, the invited (recipient) tenancy must have the correct permissions to manage subscription sharing in the child tenancy. For more information, see[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_required_iam_policy.htm). The recipient tenancy also must be in a home region within the same realm.
Note  
  

Parent tenancies and tenancies that aren't already in a sharing relationship can send invitations. Child tenancies can't send invitations.

If the invitation is accepted by an authorized user in the recipient tenancy, and the recipient tenancy is subscribed to a Pay As You Go subscription, all usage in the recipient tenancy will be metered against your subscription. To stop sharing your subscription with the recipient tenancy after the invitation has been accepted, you can[map the subscription](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-create.htm).

Commercial matters related to the subscription, such as credits, credit rebalancing, and so on need to be negotiated with an Oracle sales representative and are subject to recontracting.

Invited tenancies continue to retain their own distinct service limits, and they can request a limits increase through support requests. For more information, see[Creating a Limit Increase Request](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm).
Caution  
  
An invited tenancy is automatically mapped to the default subscription in the organization, so all usage is computed and charged against the default subscription's rate card . If you don't want the invited tenancy to consume from the default subscription, you can[map the subscription](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-create.htm)back to the original subscription after the invited tenancy has joined the organization.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-create.htm#)
- 

You can attach[governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm)to the invited tenancy when you create the invitation, or you can[attach rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-attachruletenancy.htm)later. To attach governance rules before sending the invitation, you can[create governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm)first on the Governance Rules page, so they're available for selection during the invite tenancy process.

To invite a tenancy, follow these steps:

- Sign in to the sender tenancy (the one that will send the invitation), as a user that has permissions to manage Organization Management functions.
- Open the navigation menu and select Governance &amp; Administration . Under Organization Management , select Tenancies .
- On the Tenancies list page, select Invite tenancy.
- In the Tenancy details step of the workflow, enter the following information:

- Invitation name : The name of the invitation that will be visible to the recipient. Avoid entering confidential information.
Note  
  
For the invitation name, it can be helpful to use notation that signifies the direction and number of sending invitation attempts. For example, entering a1 to b1 v1 can signify that tenancy a1 is sending an invitation to tenancy b1, and v1 as the first try. Such a convention allows the invitations to be more readable to the Console user, without needing to access the invitation details page to view sender and recipient details. For more information, see[Listing Sender Invitations](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-list.htm)and[Listing Recipient Invitations](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-list.htm).
- Recipient tenancy OCID : The recipient's OCID. You can[find the OCID](https://docs.oracle.com/en-us/iaas/Content/General/organization/../tenancy/managingtenancy.htm#info)on the[tenancy details](https://docs.oracle.com/en-us/iaas/Content/General/organization/../tenancy/managingtenancy.htm#info)page.
- Recipient email : The recipient's email address.
Note  
  
To accept the invitation, the recipient must have the correct permissions to manage subscription sharing in the recipient tenancy. For more information, see[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_required_iam_policy.htm).
- Tags : (Optional) Add one or more tags to the invitation.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Select Next .
In the Governance rules step, you can select[governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm)to attach to the tenancy, or skip this step and[attach them later](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-attachruletenancy.htm). By default, the Require tenancy to join organization governance option is selected for the tenancy. If you clear this option, a message indicates that you haven't selected organization governance for this tenancy. To attach governance rules to this tenancy in the future, you must request the invited tenancy to use governance rules, and have the tenancy accept ([opt in to](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-optinuserules.htm)) the request.
- If you want to select governance rules now, select them from the table. You can filter the table by the rule name, type, or OCID, or the targeted tenancy. You can expand any rule entry and view its details.

Note  
  
Some rules are set by the entire organization. Such rules are already selected, and you can't clear them.
- Select Next .
- Review the summary step to verify the invited tenancy settings.

- Tenancy details shows the invitation name and recipient tenancy OCID.
- Governance rules shows the rule names, rule type, and targeted tenancies if governance rules were attached. Whether rules were attached or not, the Require tenancy to join organization governance field indicates whether the invited tenancy is required to join organization governance with Yes or No .[Governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm)can be created, attached, and detached later.
- Select Invite tenancy .
The invitation is sent to the recipient tenancy. A notification is displayed that you have successfully requested to invite a tenancy (with the associated OCID) to join the organization. If the request completes successfully, then the recipient tenancy receives an invitation to accept. The invitation expires in 30 days.
- After the invitation is accepted and processed, its Status field changes to Accepted . The recipient tenancy then becomes a child tenancy under the parent tenancy in the organization.

After the invitation is accepted, it takes one to two hours for metering to start flowing to the subscription in the parent tenancy. After that, all usage in the child tenancy is metered against the parent tenancy's subscription. In addition, after the tenancy joins the organization, we recommend that you wait a few hours before creating resources (that is, if you want to be sure that all spending accrues against the subscription of the parent tenancy).

If a remaining subscription balance exists, contact your sales representative to move it to a primary subscription in the sending tenancy.
Note  
  
After the tenancy becomes a child tenancy in the organization, it can't invite another tenancy to become a child tenancy. Also, when a tenancy joins your organization, its subscription is managed by the parent tenancy. To map a child tenancy back to the original subscription, use[Subscription Mapping](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-management.htm).

On the Tenancies list page for the child tenancy and the parent tenancy both tenancies are listed. On the parent tenancy's Tenancies list page, you can view the child tenancy and parent tenancy, and other child tenancies that are being metered against the organization's subscription. The following information is shown:
- Tenancy name : Displays the name of the tenancy and whether it's a parent or child tenancy.
- Tenancy OCID : Displays the OCID of the tenancy.
- Status : (Parent tenancy only) Displays the invitation status.
- Organization governance : Specifies whether the tenancy is using[governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm)( Joined ) or not ( Not joined ).
- Join Date : (Parent tenancy only) The UTC date and time that the tenancy joined the organization and subscription sharing began.

See[Accepting an Invitation to Join an Organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-accept.htm)for more information on accepting an invitation to join an organization.
- 

Use the[oci organizations sender-invitation create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/sender-invitation/create.html)command and required parameters to create a sender invitation and asynchronously send the invitation to a recipient:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateSenderInvitation](https://docs.oracle.com/iaas/api/#/en/organizations/latest/SenderInvitation/CreateSenderInvitation)
