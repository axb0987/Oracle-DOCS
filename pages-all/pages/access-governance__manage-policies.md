# Manage Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage Policies

Policies are the mechanism by which you can provide resource access to identities within your organization. Policies associate resources and permissions with identities by means of roles and access bundles. Here we will see how you can maintain policies within your Oracle Access Governance service.

## Create a Policy

You can create a policy in the Oracle Access Governance Console by following the steps below:

- In your browser, navigate to the Oracle Access Governance service home page, and log in as a user with the Administrator or Access Control Administrator application role.
- On the Oracle Access Governance service home page, click on the icon, then select Access Controls → Policies . This will take you to the Policies page, where you can view, edit, and create policies.
- Click on the Create a policy button. This will take you to the Create a new policy flow, which guides you through the steps to setup a policy.
- The Let's get started building your policy step of the flow allows to you provide a name and description for your policy, and select what types of associations to add to the policy.
Enter values for the following:
- What do you want to call this policy? : Add a name for your policy.
- How would you describe this policy? : Add a description for your policy.
- Would you like to add any tags? : Enter any tags for this role that you would like to be able to search on. Examples may include regulatory compliance standards such as SOX , HIPPA , GDPR and others.
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource.

You can view the Primary Owner in the view list. All the owners can view and manage the resources that they own.
Click the Add a new association tile, and select one of the following association types to add.
- Access bundle association
- Role association
- When you have selected the association type to add, you will navigate either the Add an access bundle policy assignment or Add a role policy assignment flow, which guide you through the steps to assign your access bundle or role to a policy. The steps in the flow are mostly the same, where differences occur these will be highlighted in the instructions which follow.
- Select who is the first step of the flow, where you add the identity collections to which the policy will apply. Select, or search for, the identity collections you want to include in your policy, and select Next to continue.
- Depending on whether you selected access bundle or role association, the next step will be either Select access bundles or Select roles . Select the access bundle or role that you want to assign to the policy, and select Next to continue.
- Review and submit is the next step. If you are happy with the information you have added, select Add association to save the association. You can also select Back to revisit the details you entered, or Cancel to abandon your changes.
- If you add the association you will be taken back to the beginning of the Create a new policy flow. At this point you can elect to add another association to your policy by selecting Add a new association and adding the association as previously described. Once you are finished entering associations for the policy, select Create to save the policy, or Save as draft to save your policy for editing at a later date.

## Edit a Policy

To edit an existing or draft policy, perform the steps described below.

- On the Oracle Access Governance service home page, click on the icon, then select Access Controls → Policies . You can select the option to edit a policy in any one of the following ways:
- Select the name of the policy to navigate to the View details page. Click on the Actions menu and select Edit .
- From the list of policies, select the Action menu. Select Edit .
- From the list of policies, select the Action menu. Select View details . From the View details page, select Edit .
- You navigate to the Policies workflow. Make any amendments and save your changes.

## Delete a Policy

You can delete a policy using the Oracle Access Governance Console.

- On the Oracle Access Governance service home page, click on the icon, then select Access Controls → Policies to navigate to the Policies page.
- Select the name of the policy you want to delete, click on the Actions menu and select Delete .
-
