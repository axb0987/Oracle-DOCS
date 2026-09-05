# Explore Access Profile in an Enterprise
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/explore-access-insights.htm
- Fetched: 2026-09-05 03:14 CDT

# Explore Access Profile in an Enterprise

As an Enterprise-wide Access Administrator , you can use the Who has Access to What functionality of Oracle Access Governance to get 360-degree visibility of access maps across an enterprise. Here, you get a complete and comprehensive understanding of identity access profiles across an enterprise. Managers can check accesses for their direct reports.

## View Access Profile across Enterprise

As an Enterprise-wide Access Administrator , get visibility into accesses across an enterprise using the Enterprise-wide Browser functionality. There are multiple perspective views available to browse through the access profile information. You can browse to view identity details, their accesses including roles, resources, permissions, accounts, or policies. Alternatively, you can choose access control entities to browse access information.
Here's how you can view access profile for your enterprise:

- Log on to Oracle Access Governance as an Enterprise-wide Access Administrator.
- From the navigation menu, select Who has Access to What &gt; Enterprise-wide Browser .
- In the Enterprise-wide Browser page, select the perspective view in the Select what you want to browse list.
- Perform keyword search or select suggested filters for anything to you want to locate.
- To search something specific, use the Add an advanced filter button to apply advanced filters.
Based on the perspective view selected, you will see the access information in a grid view. You can customize this default view by[hiding/showing the columns](https://docs.oracle.com/en-us/iaas/Content/access-governance/explore-access-insights.htm#manage-access-profile-layout).
- To view details related to each record in a grid view, select the View details link.
In the details page, you will see the reference count summary along with associated information for that perspective. You can further explore access details or identity information by selecting the View details link throughout the view. For more information on what components you can view, refer to[Enterprise wide Access Profile Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/enterprise-wide-access-profile-reference.htm).

## Search and Apply Filters

You can retrieve data of your choice by performing keyword search or applying filters. Within Enterprise-wide Browser page, you can apply suggested filters to view focused information, or add an advanced filter to get some specific information.
Here's how you can apply search

- To perform keyword search, in the Enterprise-wide Browser page, in the Search field, enter a keyword of your choice and press the Enter key on your keyword. Repeat the process to add additional keywords.
Records containing the search phrase will be displayed. For more than one keywords, all the keywords need to be satisfied.
- To view focused results, select one or more suggested filters available directly under the Search field.
- To look out for something specific, add one or more advanced filters:
- Click the Add an advanced filter button.
- Select one of the identity attributes in the What do you want to filter on? list.
- Select the logical operator of your choice.
- Select the value and click Apply .
You can view the applied advanced filters under the View advanced filters collapsible section.
- In the View advanced filter section
- Select the edit icon to modify the value listed in the applied filter.
- Select the delete icon to remove an advanced filter
- Click the Clear all link to remove all the applied advanced filters at once.

## Manage Access Profile Layout

You can customize the default access profile layout by including (show) or excluding (hide) the data columns, sorting individual column, or reordering the data columns to change the view sequence. You can even download the CSV file for the first 500 records for offline analysis.

Hide or Show Columns in the Access Profile Layout
- In the Enterprise-wide Browser page, select the Edit list setting icon.
- To add columns in your layout, from the Hide section, select one or more fields. The selected columns will be part of the Show section.
- To remove columns from your layout, from the Show section clear one or more fields. These unselected columns will be part of the Hide section and will be hidden from the access profile view layout.
- Click Apply .
- To restore your default layout, select the Restore defaults link.

Reorder Columns in the Access Profile Layout
- In the Enterprise-wide Browser page, select the Edit list setting icon.
- To reorder and rearrange the columns, select and drag the drag-handle icon and drop it at the relevant position.
- Click Apply .

Download Reports
- In the Enterprise-wide Browser page, select the CSV icon to download the first 500 records available in the access profile view.
- To download the PDF screenshot of the access details visible to you in the application:
- In the Enterprise-wide Browser page, for a specific access record, select the View details link.
- From the Actions menu, select Download screenshot PDF .
Note  
  
If you're having trouble viewing PDFs downloaded using Mozilla Firefox, update the browser advanced font settings, and select the Allow pages to choose your own font, instead of your selections above check box.
- To download the CSV report of identities associated with a specific resource:
- In the Enterprise-wide Browser page, for a specific access record, select the View details link.
- Click the CSV icon to download the specific access record details.

## Generate Compartment Report

For an Orchestrated system, you can generate a compartment report using the Export compartment report button from the Enterprise-wide Browser page. Clicking this button creates a CSV file containing comprehensive information on the available resources within that compartment along with access information for the associated identities for those resources.

Note  
  

- The Export compartment report button is visible on the Enterprise-wide Browser page only if you have at least one OCI tenancy connected.
- Each report generated is specific to one compartment.
- The report contains first 2,000 records available in the compartment.

To generate a compartment report:

- Log on to Oracle Access Governance as an Enterprise-wide Access Administrator.
- From the navigation menu, select Who has Access to What &gt; Enterprise-wide Browser .

The Enterprise-wide Browser page will appear.
- On the Enterprise-wide Browser page, from the Select what you want to browse list, select Resources .
- Click the Export compartment report button.
- On the Export compartment report dialog box, from the Which compartment? list, select the compartment name for which you want to generate the report, and then click Export .

A CSV file will be generated, which you can then download to view detailed information about each resource within that compartment, along with the identities that have access to them.

## Generate User-Created Access Reviews

Enterprise-wide Access Administrator or Oracle Access Governance Administrator can generate identity and access control access reviews while exploring the access profile insights within Enterprise-wide Browser . You can generate access reviews for identities, policies, and identity collections. For an identity, apart from regular identity access reviews, you can request specific access review on permissions, accounts, roles, identity collections, and policies.

Identity Access Reviews
- Log on to Oracle Access Governance as an Enterprise-wide Access Administrator .
- From the navigation menu, select Who has Access to What &gt; Enterprise-wide Browser
- In the Enterprise-wide Browser page, select Identities as the perspective view in the Select what you want to browse list.
- Select the View details link corresponding to the identity for which you want to generate the review.
- To create:
- All the possible identity access reviews for that identity, from the Actions menu, select Create access review .
- Specific identity access review for the selected permission, from the More Actions icon, select Create access review .
- Select the reviewer in the Who do you want to do the review field.
- Enter justification for this access review in the Why are you wanting it reviewed? box.
- Click Create .

Access Control Access Reviews
- Log on to Oracle Access Governance as an Enterprise-wide Access Administrator .
- From the navigation menu, select Who has Access to What &gt; Enterprise-wide Browser
- In the Enterprise-wide Browser page, depending on the access control type, select either Identity Collections or Policies as the perspective view in the Select what you want to browse list.
- Select the View details link corresponding to the access control that you want to review.
- In the details page, from the Actions menu, select Create access review .
- Select the reviewer in the Who do you want to do the review field. By default, the review is assigned to the owner of the selected access control.
- Enter justification for this access review in the Why are you wanting it reviewed? box.
- Click Create .

Reviewers can view these review tasks on the My Access Reviews page.

## My Directs' Access - View Access Profile Information for Team

Managers can now view key identity details for their direct reports, including assigned resources, accounts, roles, permission levels, and group memberships. They can also change passwords on behalf of their team members.

Note  
  
This feature is not available if you have integrated only OCI IAM, as your target system, with Oracle Access Governance. Here, My Directs' Access will provide the access information only for the direct reports, and not skip-level reports.

To review team access:

- In the Oracle Access Governance Console, select Who Has Access to What &gt; My Directs' Access from the navigation menu.
You navigate to the My Directs' Access page. A list of your direct reports is displayed.

You can use Advanced filters to limit the search results of users specific to user attributes, such as an application, a job code, or a location.
- To view access privileges assigned to a user, select the Username .
You will see the identity details page displaying all the access components for the identity. Refer to[Enterprise-wide Access Insights Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/enterprise-wide-access-profile-reference.htm)
