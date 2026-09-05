# Using ServiceNow with Oracle Access Governance
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/using-service-now.htm
- Fetched: 2026-09-05 03:16 CDT

# Using ServiceNow with Oracle Access Governance

Oracle Access Governance Service Catalog is a ServiceNow application which streamlines access requests, status tracking, and approval processes within your enterprise, while seamlessly integrating with Oracle Access Governance for fulfillment. This allows users to submit access requests in ServiceNow, which are processed, and provisioned within the Oracle Access Governance system.
- [Self Service Using ServiceNow for Administrators](https://docs.oracle.com/en-us/iaas/Content/access-governance/servicenow-self-service-using-servicenow-for-administrators.htm)
- [Self Service Using ServiceNow For End Users](https://docs.oracle.com/en-us/iaas/Content/access-governance/servicenow-self-service-using-servicenow-for-end-users.htm)

## Self Service Using ServiceNow Overview

Figure 1. Self Service Using ServiceNow

The diagram shows the overall flow between the user, Oracle Access Governance Service Catalog, and Oracle Access Governance.

ServiceNow Request Portal

Administrators and end users can make access requests from the ServiceNow Request Portal for subsequent fulfillment by Oracle Access Governance. The high-level flow includes the following steps:
- Initiate Request : Users can initiate an access request within the Service Portal for themselves or for another person (depending on permissions).
Note  
  
The`userName`attribute is used to retrieve the user name from ServiceNow, which is then verified in Oracle Access Governance. If the user exists in Oracle Access Governance, you can proceed to initiate an access request.
- Select Access : Users select the access that they want to request from the Service Catalog. These can be selected from a list of[access bundles](https://docs.oracle.com/en-us/iaas/Content/access-governance/glossary.htm#glossary-a)that have been synchronized to ServiceNow from Oracle Access Governance.
- Workflow Approval Routing : If required, the access request can be subject to the approval process governed by ServiceNow. The access request is either rejected, and the request closed, or is approved and passed to Oracle Access Governance for fulfillment.

Oracle Access Governance
Once the access request is submitted to Oracle Access Governance for fulfillment it completes a number of steps including the following:
- Request Create : An access request is made on the Oracle Access Governance system to carry out the fulfillment activities.
- Risk Assessment/Compliance : Oracle Access Governance provides robust support for assessing risk and enforcing compliance of identity across your enterprise. This includes support for preventative segregation of duties (SoD) using Oracle Fusion Cloud Risk Management and Compliance (RMC), access control constraints via access guardrails, and auditing support.
- Fulfillment : if an access request meets all requirement for fulfillment, Oracle Access Governance will create/update relevant account and permissions for an identity, and will update the status of the service request in ServiceNow.

## Key Benefits

Oracle Access Governance Service Catalog provides a number of benefits that can help your enterprise provide identity governance, ensuring that users only have the necessary access to the right resources for performing their jobs when needed.

- Streamlined access requests : Access requests can be created, monitored, and maintained in the familiar ServiceNow environment. The requests is managed within the ServiceNow Portal, while fulfillment and additional governance activities are performed seamlessly in Oracle Access Governance, with results being synchronized back to ServiceNow.
- Integrated User Experience : By acting as a single pane of glass for all access requests, Oracle Access Governance Service Catalog reduces IT workload and provides a better user experience when undertaking governance tasks.
- Increased Visibility : Users can track access requests, approvals, and fulfillments, providing visibility and audit trails.
- Enhanced Governance : Oracle Access Governance Service Catalog allows ServiceNow users to leverage Oracle Access Governance for advanced identity governance and administration capabilities.

## Administrator Workflow

ServiceNow administrators are primarily responsible for the one-time setup of Oracle Access Governance Service Catalog. This comprises the following tasks:
- Configure Integration of Oracle Access Governance With ServiceNow User Management (UM) : Configuration of this integration is a prerequisite for setting up the Oracle Access Governance Service Catalog. Detail of how to implement this can be found by referring to[Integrate with ServiceNow (UM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-servicenow-um.htm). You should configure your ServiceNow (UM) orchestrated system in authoritative mode to support Oracle Access Governance Service Catalog.
- Configure OCI OAuth : In order to authenticate the Oracle Access Governance Service Catalog with Oracle Access Governance you must configure OAuth and a confidential application in OCI. For details on how to do this refer to[Configure OCI OAuth To Access Oracle Access Governance API](https://docs.oracle.com/en-us/iaas/Content/access-governance/servicenow-self-service-using-servicenow-for-administrators.htm#servicenow-configureoauth).
- Install Oracle Access Governance Service Catalog : Installation of the Oracle Access Governance Service Catalog requires administrator privileges. The steps to do this can be found in the[Install Oracle Access Governance Service Catalog Application](https://docs.oracle.com/en-us/iaas/Content/access-governance/servicenow-self-service-using-servicenow-for-administrators.htm#servicenow-installsnowapp)documentation.
- Configure Oracle Access Governance Service Catalog Application Connection : In order to integrate with Oracle Access Governance the administrator needs to configure the connection details as described[here](https://docs.oracle.com/en-us/iaas/Content/access-governance/servicenow-self-service-using-servicenow-for-administrators.htm#servicenow-connection).
- Synchronize Access Bundles : To allow users to select access bundles in Oracle Access Governance Service Catalog you must synchronize the available access bundles from Oracle Access Governance to ServiceNow. Details of setting up synchronization can be found in the[Oracle Access Governance Service Catalog Application Scheduler](https://docs.oracle.com/en-us/iaas/Content/access-governance/servicenow-self-service-using-servicenow-for-administrators.htm#servicenow-scheduler)documentation.
Once initial installation and setup is configured, an administrator may be called upon to perform routine periodic configuration, or to create access requests for other users.
- Maintenance : Administrators may be asked to update configuration regarding the synchronization of access bundles or status information. Details can be found in the[Oracle Access Governance Service Catalog Application Scheduler](https://docs.oracle.com/en-us/iaas/Content/access-governance/servicenow-self-service-using-servicenow-for-administrators.htm#servicenow-scheduler)documentation.
- Create Access Requests : Administrators have the ability to create access requests for other users. For details on how to carry this out, see the[Create Access Request (Other)](https://docs.oracle.com/en-us/iaas/Content/access-governance/servicenow-self-service-using-servicenow-for-end-users.htm#servicenow-createrequestother)documentation.

## End User Workflow

ServiceNow end users are responsible for creating access requests, managing approvals, and monitoring the progress of requests created. Access requests can be create for your own user (Self) or, in the case of managers or administrators for self and other users (Other).

  

  
Figure 2. End User Workflow
The end user workflow tasks can be summarised as:
- Create Service Request : An end user can create a request for themselves, or for another (depending on permissions). The access request is made for an access bundle which is a collection of permissions associated with an application or service. Access bundles are maintained in Oracle Access Governance for all the downstream applications that the particular service instance is integrated with. Access bundles are synchronized between Oracle Access Governance and the Oracle Access Governance Service Catalog. ServiceNow users can request access bundles from the Oracle Access Governance Service Catalog for provisioning.
- ServiceNow Approval Flow : Once an access request is made it will be subject to the ServiceNow approval process. If rejected, then the access request is ended. If approved, the access request continues through the end user flow, and is sent to Oracle Access Governance for fulfillment.
- Oracle Access Governance Compliance Checking : When the access request arrives in Oracle Access Governance it is checked for compliance against any guard rails that have been configured. If any violations are found then the access request is routed to a compliance approver in Oracle Access Governance. If denied the request will be ended. If approved then it is passed on for provisioning. If no compliance issues are found, then the access request is sent directly for provisioning.
-
