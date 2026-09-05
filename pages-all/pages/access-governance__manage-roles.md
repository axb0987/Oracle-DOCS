# Manage Roles
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage Roles

A role is a group of access bundles. The access bundles contained within a role can span several targets. For example, Database Administrator role, which groups together the DBAdmin_Oracle , DBAdmin_DB2 , and DBAdmin_MySQL access bundles. Create roles that collect together the relevant access bundles to perform that role. These roles can then be associated with identities through policies.
Note  
  
A role doesn't provide access to a resource by default. Access is given to an identity when a role is assigned to that identity through a policy or self-service request.

## Create a Role

You can create a role in the Oracle Access Governance Console by following the steps below:

Applies to : Access Control Administrator, Access Control Restricted Administrator, Administrator . See[Application Roles and Responsibilities Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm)

### Create Role

- On the Oracle Access Governance console, click the Navigation icon, then select Access Controls → Roles → Create a Role .
- In the Roles page, select Create a role . The Create a new role flow initiates.
- In the Role settings tab, enter values for the following:
- Who can request this role? : Define who can request this role.
- No one : You can't request access to this role through self service flows. It can only be assigned by administrator through policies.
- Anyone : Any identity can request the access to this role.
- Members of organization : Only members of a specific organization can request access to this role through self service flows. For additional details about managing Oracle Access Governance Organization, see[Create and Manage Organizations](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#create-and-manage-organizations).
- For Members of organization , select one or more organization names that can request access to this role. Identities part of the selected organizations can only request this role.
- Which approval workflow? : Select the name of the approval workflow you want to associate with this role from the list. If No one was selected in the previous step, then this selection would be disabled.
- Primary Business approver : Select a user to review and approve access requests based on business needs. This role grants approval responsibility only and doesn't provide ownership or management of access resources. See[Business Approvers](https://docs.oracle.com/en-us/iaas/Content/access-governance/workflow-approval-workflow-overview.htm#workflow-approval-workflows-types__business-approver).
- Who else can be business approver : Select one or more business approvers to approve the task.
- Would you like to add any tags to this resource? : Enter any tags for this role to search. Examples might include regulatory compliance standards such as SOX , HIPPA , GDPR and others.
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource.

You can view the Primary Owner in the view list. All the owners can view and manage the resources that they own.

When you are happy with your selections, click Next to continue to the next step.
- Next step is Select access bundles . You can search for, and select, access bundles that you want your role to contain. These access bundles can originate from multiple targets if required.
- Next step is Add details . Enter values for the following:
- What is the name of this role? : Enter a name for the role you are creating.
- How do you want to describe this role? : Enter a description of the role you are creating.

Select Next to proceed.
- Next step is Review and submit . If you decide not to create the role, select Cancel to reject the changes, else if you want to amend any details, select Back .If you are happy with the changes reviewed, then you have three options to proceed.
- Role assignment : A role doesn't give access to anybody until it is assigned. If you select the Start assignment after creation checkbox, you will automatically navigate to the assignment flow on selecting the Create role and assign button. This is the default option.
- Create role : If you deselect the Start assignment after creation check box, you create the role, but do not navigate automatically to the assignment flow. On selecting the Create button, the role is saved and you are returned to the Roles page.
- Save as draft : You can select to save the role as a draft. You can edit the role later by selecting from the Roles page.

### Assign Role

If you selected Start assignment after creation , or selected the Add assignment option, you will navigate to the role assignment page, which gives you the option to assign your role to an existing policy, or to create a new policy and assign the role to that. Initially, you are asked Do you want to assign the role through an existing policy or create a new one?

If you select Existing policy :

You can assign your role to an existing policy by following the steps below:

- Select the policy you would like to add your role to from the drop-down list Which policy do you want to assign it to? .
- You have the option Do you want to add the role to existing associations or create a new one? .
- If the policy selected has existing role associations, then they are displayed under Which associations do you want to add this role to? . The role associations display as a tile which identifies which identities are associated with which roles. To add an association between your newly created role and the identities, select the relevant role association, at which point your new role name is displayed on the tile. To save the association, click on Add assignment . Your role assignment is saved and you are returned to the Roles page.

If you select Create a new policy :

You create a new policy with the following steps:

- Add the name of your policy in the What do you want to call this policy? field.
- Add a description of your policy in the How would you describe this policy? field.
- Under Which identity collections do you want to associate this role with? select the identity collections you want to associate with this role by selecting from the tiles displayed or entering a search.
- Select on Add assignment to save your changes.

## Edit a Role

To edit an existing or draft role, perform the steps described below.

- On the Oracle Access Governance service home page, click on the icon, then select Access Controls → Roles . You can select the option to edit a role in any one of the following ways:
- Select the name of the role to navigate to the View details page. Click on the Actions menu and select Edit .
- From the list of roles, select the Action menu. Select Edit .
- From the list of roles, select the Action menu. Select View details . From the View details page, select Edit .
- You navigate to the Role workflow. Make any amendments and save your changes.

## Delete a Role

You can delete a role using the Oracle Access Governance Console.

- On the Oracle Access Governance service home page, click on the icon, then select Access Controls → Roles to navigate to the Role page.
- Select the name of the role you want to delete, click on the Actions menu and select Delete .
-
