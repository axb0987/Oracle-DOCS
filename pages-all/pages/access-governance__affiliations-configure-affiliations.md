# Configure and Manage Affiliations
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/affiliations-configure-affiliations.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure and Manage Affiliations

As an Administrator, configure and manage affiliations from the Identity Attributes page. With affiliations, for a single identity you can manage different accesses based on varied job data ingested from Authoritative source.

## Navigate to Affiliations

Affiliations are set up from the Manage Integrations page for a specific orchestrated system.

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems.
- Select the Manage integration option from the action menu for the orchestrated system you want to configure. The Manage Integration page for the selected orchestrated system is displayed.
- From the Data settings section, select Manage on the Identity attributes tile.
This tile is available only for orchestrated system supporting Authoritative sources.
- Select the Affiliations tab.

## Create an Affiliation

Select + Create an affiliation to start the workflow. The Create a new affiliation page is displayed.

### Add Details

In the Add Details task, you can enter general settings about your affiliation. You are also able to add user friendly tags that can be used while searching this affiliation.

- Name : Enter a name of your affiliation.
- Display name : Enter meaningful display name.
- Description : Enter description
- Click Next .

### Define Attributes

Add one or more core or complex identity attributes to associate with affiliations and manage the flag for using the attributes in the Oracle Access Governance features.

- Select Add an attribute .
The identity attribute fields are displayed in the editable mode letting you add new attributes.
- Enter the Attribute name .
- Enter the Display name that would be shown on the Oracle Access Governance Console.
- Select the appropriate Data type for the attribute.
- Select the Oracle Access Governance features flags where you want to the attribute.

Option Description
Identity details If selected, attributes are displayed in:
- [Who Has Access to What](https://docs.oracle.com/en-us/iaas/Content/access-governance/who-has-access-overview.htm)functionality where you can view resource details for an identity.
- [My Access Reviews](https://docs.oracle.com/en-us/iaas/Content/access-governance/perform-access-reviews-section.htm)functionality where you can perform access reviews and see review insights.
Campaign selection If selected, the attribute is available for use in[user access review campaigns](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-access-review-campaigns.htm).
Event-based Setup If selected, the attribute is available for use in[configure event-based triggers](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-and-manage-event-based-access-reviews.htm)for identity access reviews.
Manage Identities If selected, the attribute is available for use in[configure activation rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)to manage identities from Oracle Access Governance, and to[enable custom attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm)in creating an identity collection.
- Continue adding additional attributes for the affiliation.
- Click Next .

### Add Rules for Deriving Values

In the Value source task, use the data transformation rules on the identity attributes to derive affiliation value.
For more information on fetching values using data rules, see[Data Transformation Rules Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/transformation-for-inbound-and-outbound-rules.htm).

- Rule : Enter the rule you want to apply to this affiliation/
- Click the Validate button to check your rule. If the rule is valid then you will see a confirmation message and the rule will be marked as validated. If there is an issue with the rule, then you will see an error message and the rule will be marked as invalid. You cannot save your rule if it is marked as invalid.
- (Optional) Expand the Show me the available rule link attributes to list all the available attributes that you may use to construct your rule.
- Click Next .
Example : You can extract JobCode, Description and JobName from the job array in the Authoritative Source, using a rule similar to:
```

```

### Review and Submit

In the Review and Submit task, you can review the information you added in the previous steps.

If everything looks correct, then click Create to create the affiliation. You may select addition actions:
- Cancel : To cancel the process.
- Back : To go back to the previous step.

## Edit Affiliations

The Edit Affiliations page provides the same guided tasks as you see while creating a new affiliation.

Click the Actions menu icon corresponding to the affiliation that you want to modify, and then select Edit .
After updating your affiliation, on the Review and submit step, select Update . Alternatively you can select Back to edit values, or select Cancel to discard your changes.
To edit an affiliation name, clone the affiliation to make changes, and then delete the previous affiliation.

## Delete Affiliation

Administrators can delete affiliations and delete associated attributes.

- Click the Actions menu icon corresponding to the affiliation that you want to delete, and then select Delete .
On the confirmation pop-up, click Delete to remove the affiliation or click Cancel to retain it.
Delete Attributes
- Click the Actions menu icon corresponding to the affiliation that you want to modify, and then select Edit .
- On the Define Attributes task, select the Delete icon corresponding to the attribute that you want to delete.
- On the Delete attribute confirmation message box, select Continue .

## View Affiliation Details

You can view affiliation details, attributes associated with the affiliation, and the rules for extracting the value from the Authoritative source.

Select the Actions menu icon corresponding to the affiliation that you want to view, and then select View Details .  

- [DBAT Affiliation Support for Custom Multivalued Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/database-application-tables-integration-reference.htm#db-tables-dbataffiliations)
Related information  

- [Affiliations Support with Identity Schema Extension - Adding Custom Complex Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-flat-file.htm#file-identity-schemaextension)
