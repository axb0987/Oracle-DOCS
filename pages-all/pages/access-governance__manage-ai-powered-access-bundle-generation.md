# Manage AI-Powered Access Bundle Generation
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-ai-powered-access-bundle-generation.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage AI-Powered Access Bundle Generation

Oracle Access Governance streamlines application onboarding with its new AI-powered Auto-generated access bundles recommendation capability.

Instead of manually creating access bundles and associating permissions, the system allows you to instantly generate a list of AI-powered access bundle recommendations by leveraging existing user assignments in a managed system. You can accept, edit, or reject these recommendations making access provisioning faster and more efficient.

## Create Auto-Generated Access Bundle Recommendations

You can create intelligent Auto-generated access bundle recommendations using the Oracle Access Governance Console.

- Log in to the Oracle Access Governance Console.
- Click the navigation menu icon, and select Service Administration and then Orchestrated Systems . The Orchestrated Systems page lists the orchestrated systems that you have configured in your Oracle Access Governance service instance.
- Click the icon for the orchestrated system you want to create Auto-generated access bundle recommendations, and then select Manage integration .

The configuration page for the selected orchestrated system appears.
- From the Data settings section of the page, click Manage on the Auto-generated access bundles tile.

This will display the Auto-generated access bundles page for your orchestrated system.
- On the Auto-generated access bundles page, click Build new recommendations .

The Build new recommendations page is displayed.
- From the Select how we should make recommendations list, select either of the following:
- AI assisted recommendations based on current assignments : Generate access bundle recommendations based on assignment of permissions to users in the managed system.

Select either of the following and assign a value in the box:
- Percentage of assigned identities : Filter to include only bundles where the percentage of identities assigned is greater than or equal to X% assigned in the box.
- Number of assigned identities : Filter to include a distinct count of users to whom the permission is assigned.
- Generate access bundles for each assigned permission : Generate one access bundle for each assigned permission to a user in the managed system.
- In the Select which defaults should be used when building the recommendations section, perform the following steps:
- From the Who can request this bundle? list, define which identities can request this access bundle.

Select from one of the following values:
- No one
- Anyone
- From the Which approval workflow should be used? list, select the name of the approval workflow for this recommendation run.
- From the Who is the primary owner? list, select an Oracle Access Governance active user as the primary owner.
- From the Who else owns it? list, select one or more additional owners, if needed.
- From the Which account profile? list, select the account profile.
- From the Select an access guardrail required to allow access list, select an access guardrail.
- From the Time limits list, select an option to configure access duration.

Note  
  
The Time limits option is only available when you select Anyone in Who can request this bundle? in Step a.
Select from one of the following values:
- Indefinitely
- Maximum number of days [1-365]
- Maximum number of hours [1-24]
- Click Run .

It takes a few seconds to build the access bundle recommendations. Click Refresh status for the access bundle recommendations table to appear.
Note  
  

- The Origin column displays how the data was generated.
- Mined from the source by user : User initiated the data extraction.
- AI-Proposed : Data is suggested by the AI.
- The names for the access bundle recommendations, displayed in the Name column, are derived from Generative AI-generated conventions.
- Select one of the following to view an auto-generated access bundle recommendation of a specific orchestrated system:
- Click the auto-generated access bundle recommendation link in the Name column.
- Click View from the navigation menu.

The auto-generated access bundle recommendation page is displayed.
Note  
  
If you re-run the recommendations, the new recommendations will replace the current ones.

You can accept, reject, or edit a recommended access bundle.

## Finalize Auto-Generated Access Bundle Recommendations

Once the AI-powered system generates intelligent recommendations, you can accept and convert them into actual access bundles.

Once you accept a recommendation and convert it into an access bundle, it will be excluded from subsequent recommendation runs. This newly created access bundle will then appear under Current tab on the Auto-generated access bundles page.

- Log in to the Oracle Access Governance Console.
- Click the navigation menu icon, and select Service Administration and then Orchestrated Systems . The Orchestrated Systems page appears that lists the orchestrated systems that you have configured in your Oracle Access Governance service instance.
- Click the icon for the orchestrated system you want to finalize the Auto-generated access bundle recommendations, and then select Manage integration .

The configuration page for the selected orchestrated system appears.
- From the Data settings section of the page, click Manage on the Auto-generated access bundles tile.

This will display the Auto-generated access bundles page for your orchestrated system. The Recommendations tab lists all the AI-recommended access bundles.
- Select one of the following to convert a recommendation into an access bundle:
- Click Accept from the navigation menu.
- From the navigation menu, click View . On the auto-generated access bundle recommendation page, click Accept .
- On the Auto-generated access bundles page, select the check box for each recommendation you wish to convert, then click Create access bundles . This generates multiple access bundles.

On the Create recommended access bundle dialog box, click Create .
- On the Auto-generated access bundles page for your orchestrated system, click the Current tab.

It will display the newly created access bundle.
Note  
  

Once you accept a recommendation, it moves to the Current tab and becomes available for provisioning. You'll also observe that the count on the Current tab increases, while the count on the Recommendations tab decreases. The number of recommendations from Recommendations tab will be reduced corresponding to number of access bundles accepted. The accepted recommendations will now be available under the Current tab.

## View Auto-Generated Access Bundle Recommendations

You can view and review the AI-powered access bundle recommendations, prior to acceptance or rejection.

- Log in to the Oracle Access Governance Console.
- Click the navigation menu icon, and select Service Administration and then Orchestrated Systems . The Orchestrated Systems page appears that lists the orchestrated systems that you have configured in your Oracle Access Governance service instance.
- Click the icon for the desired orchestrated system, and then select Manage integration .

The configuration page for the selected orchestrated system appears.
- From the Data settings section of the page, click Manage on the Auto-generated access bundles tile.

This will display the Auto-generated access bundles page for your orchestrated system. It lists all the AI-recommended access bundles.
- Select either of the following to view and review an auto-generated access bundle recommendation.
- Click the auto-generated access bundle recommendation link in the Name column.
- Click View from the navigation menu.

The auto-generated access bundle recommendation page appears that displays all the information associated with the recommended access bundle.

## Edit Auto-Generated Access Bundle Recommendations

You can edit auto-generated access bundle recommendations by updating permissions, fields, or any attribute to refine their details to meet your requirements.

- Log in to the Oracle Access Governance Console.
- Click the navigation menu icon, and select Service Administration and then Orchestrated Systems . The Orchestrated Systems page appears that lists the orchestrated systems that you have configured in your Oracle Access Governance service instance.
- Click the icon for the desired orchestrated system, and then select Manage integration .

The configuration page for the selected orchestrated system appears.
- From the Data settings section of the page, click Manage on the Auto-generated access bundles tile.

This will display the Auto-generated access bundles page for your orchestrated system. It lists all the AI-recommended access bundles.
- Select either of the following to edit an auto-generated access bundle recommendation.
- Click Edit from the navigation menu.
- Click View from the navigation menu. From the Actions menu on the auto-generated access bundle recommendation page, click Edit .

The Edit the recommended access bundle page appears, allowing you to update any information associated with the recommended access bundle.
- On the Edit the recommended access bundle last screen, you can do either of the following:
- Click Update recommendation to save the required changes made to the recommended access bundle.
- Click Create access bundle to convert this recommendation into an access bundle.

## Reject Auto-Generated Access Bundle Recommendations

You can reject an auto-generated access bundle recommendation if it does not meet your requirement.

Once you reject a recommendation, it won't be displayed in subsequent recommendation runs.

- Log in to the Oracle Access Governance Console.
- Click the navigation menu icon, and select Service Administration and then Orchestrated Systems . The Orchestrated Systems page appears that lists the orchestrated systems that you have configured in your Oracle Access Governance service instance.
- Click the icon for the orchestrated system you want to finalize the Auto-generated access bundle recommendations, and then select Manage integration .

The configuration page for the selected orchestrated system appears.
- From the Data settings section of the page, click Manage on the Auto-generated access bundles tile.

This will display the Auto-generated access bundles page for your orchestrated system. It lists all the AI-recommended access bundles.
- Select either of the following to Reject an auto-generated access bundle recommendation:
- Click Reject from the navigation menu.
- From the navigation menu, click View . On the auto-generated access bundle recommendation page, click Reject .
