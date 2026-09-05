# Self Service Using ServiceNow For End Users
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/servicenow-self-service-using-servicenow-for-end-users.htm
- Fetched: 2026-09-05 03:16 CDT

# Self Service Using ServiceNow For End Users

End users can create requests in Oracle Access Governance Service Catalog which are then passed to Oracle Access Governance for fulfillment. This allows end users to use ServiceNow as a single pane of glass for all access requests while leaving fulfillment, risk assessment, and compliance to Oracle Access Governance.

## Create Access Request (Self)

End users can request access to entitlements listed in the Oracle Access Governance Service Catalog in the ServiceNow Service Portal.
To create an access request for another user:
- In the ServiceNow UI set the application scope to Oracle Access Governance Service Catalog.
- Navigate to the ServiceNow UI and search for the Oracle Access Governance Service Catalog application.
- Select Oracle Access Request Portal from the ServiceNow application navigator.
- From the Oracle Access Governance Service Catalog Portal select the Access Request icon.
- Select the Yes checkbox when prompted Is this request for you? .
- At the Select the access bundles you want to request prompt, select the access bundles you want to request access for.
- Enter the Justification for the access request.
- Click Submit .

## Create Access Request (Other)

End users with Administrator or Manager role can request access to entitlements listed in the Oracle Access Governance Service Catalog for another user. The request is made in the ServiceNow Service Portal.
To create an access request for another user:
- In the ServiceNow UI set the application scope to Oracle Access Governance Service Catalog.
- Navigate to the ServiceNow UI and search for the Oracle Access Governance Service Catalog application.
- Select Oracle Access Request Portal from the ServiceNow application navigator.
- From the Oracle Access Governance Service Catalog Portal select the Access Request icon.
- Select the No checkbox when prompted Is this request for you? .
- At the Who is this request for? prompt select the ServiceNow user you want to request the access for.
- At the Select the access bundles you want to request prompt, select the access bundles you want to request access for.
- Enter the Justification for the access request.
- Click Submit .

## Request Status

When an access request is submitted from Oracle Access Governance Service Catalog users can monitor the status of the fulfillment of the request in the ServiceNow Service Portal.

### Check Request Status

Administrators and end users can check the status of an access request in the ServiceNow Service Portal.
To check the status of an access request:
- In the ServiceNow UI set the application scope to Oracle Access Governance Service Catalog.
- Navigate to the ServiceNow UI and search for the Oracle Access Governance Service Catalog application.
- Select Oracle Access Request Portal from the ServiceNow application navigator.
- From the Oracle Access Request Portal select the Service Portal icon.
- From the ServiceNow Service Portal select Oracle AG Request from the menu bar.
- Select the access request or request item that you want to check the status for, and view the following:
- Access Governance Request Status : This is the status of the fulfillment of the access request submitted to Oracle Access Governance.
- State : This is the status of the request or request item in ServiceNow.
- Optionally you can select the Refresh AG Status button in an access request to ensure that the latest statuses from Oracle Access Governance have been synchronized with ServiceNow.
Note  
  
Mapping of Access Governance Request Status to State can be referred to in[Status Mapping](https://docs.oracle.com/en-us/iaas/Content/access-governance/servicenow-self-service-using-servicenow-for-end-users.htm#servicenow-statusmapping).

### Status Mapping

Mapping of Oracle Access Governance to ServiceNow are shown in the table below:

#### Parent/Access Request Level (AG)

Parent/Access Request Level
Oracle Access Governance ServiceNow
SUCCESS Closed Complete
FAILED Closed Incomplete
REJECTED Closed Incomplete
IN_PROGRESS Work in Progress

#### Child/Access Bundle Level (AG)

Child/Access Bundle Level
Oracle Access Governance ServiceNow
PENDING_APPROVALS Pending
INFO_REQUESTED Pending
APPROVED Work in Progress
REJECTED Closed Incomplete
DELETED Closed Incomplete
FAILED Closed Incomplete
CANCELLED Closed Incomplete
PENDING_SOD Pending
PROVISIONED Closed Complete
PROVISIONING_IN_PROGRESS Work in Progress
PROVISIONING_FAILED Closed Incomplete

## Manage Approvals

Administrators and approvers can manage access requests (approve or reject) in the ServiceNow Service Portal. Approval workflows are managed by ServiceNow.
To manage approvals for an access request:
- In the ServiceNow UI set the application scope to Oracle Access Governance Service Catalog.
- Navigate to the ServiceNow UI and search for the Oracle Access Governance Service Catalog application.
- Select Oracle Access Request Portal from the ServiceNow application navigator.
- From the Oracle Access Request Portal select the Service Portal icon.
- From the ServiceNow Service Portal select Approvals from the menu bar.
- Select the access request or request item that you want to manage, and select one of the following:
- Approve : Selecting Approve will update the status of the request and initiate fulfillment of the request by Oracle Access Governance.
-
