# Self Service Using ServiceNow for Administrators
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/servicenow-self-service-using-servicenow-for-administrators.htm
- Fetched: 2026-09-05 03:16 CDT

# Self Service Using ServiceNow for Administrators

Oracle Access Governance Service Catalog administrator tasks include the following:
- Install Oracle Access Governance Service Catalog application.
- Configure Oracle Access Governance connection details.
- Synchronize access bundles.
- Synchronize request status.

## Install Oracle Access Governance Service Catalog Application

To enable Oracle Access Governance Service Catalog functionality in the ServiceNow you firstly need to install the supporting ServiceNow application.

Note  
  
Assumes that you have completed the prerequisite task[Integrate with ServiceNow (UM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-servicenow-um.htm)and configured a ServiceNow (UM) orchestrated system in authoritative mode before setting up Oracle Access Governance Service Catalog.
To install the Oracle Access Governance Service Catalog application:
- Navigate to the[ServiceNow App Store](https://store.servicenow.com/store/apps).
- Search for the Oracle Access Governance Service Catalog application.
- Install the application referring to the ServiceNow[installation documentation](https://store.servicenow.com/sn_appstore_store.do#!/store/help?article=KB0010027).

## Configure OCI OAuth To Access Oracle Access Governance API

To authenticate to the OCI instance you want to integrate with you need to configure OCI OAuth access to the Oracle Access Governance API.

To configure OCI OAuth API access:

- Create Confidential OAuth Application
- Navigate to OCI Console → Identity &amp; Security → Domains
- Select the Identity Domain.
- Select the Integrated applications tab.
- Select Add Application .
- Select the Confidential Application tile and select Launch Workflow .
- On the Add Confidential Application page:
- Enter a Name and Description . For example access-governance-rest-api-oauth .
- Select Submit .
- Configure OAuth Settings
- Select the integrated application you created in the previous step and select the OAuth configuration tab.
- Click Edit OAuth Configuration .
- Click Configure this application as a client now .
- Enable the Add resources toggle.
- Set Client Type : Confidential .
- Set Client IP Address : Anywhere .
- Set Token Issuance Policy : All .
- Click Add scope .
- Select the Oracle Access Governance service instance you require API access for.
- Click Add .
- Click Submit .
- Activate the Application
- In the application list, select Activate from the Actions menu.
- Ensure the Status changes from Inactive to Active .
- Assign Application Role
- Navigate to OCI Console → Identity &amp; Security → Domains
- Select the Identity Domain.
- Go to the Oracle cloud services tab.
- Select the Oracle Access Governance service instance.
- Select the Application Roles tab.
- Select the role AG_Administrator .
- Select Manage applications from the Actions menu.
- Select Assign Applications .
- Select the Confidential App you created.
- Select Assign .

### Get OAuth Token URL

Fetch the Domain URL from the OCI cloud account.
- In the Oracle cloud account, navigate to Identity &amp; Security , and select Domains .
- Apply a compartment filter and then select the domain.
- On the Details tab, copy the authentication host in the Domain URL field without the port number. For example, the domain URL is,`https://idcs-xxx.identity.example.com`
The authentication URL would be constructed as:
```

```

## Configure Oracle Access Governance Service Catalog Application Connection

Once you have installed the Oracle Access Governance Service Catalog application in your ServiceNow instance, you need to configure connection details to integrate the application with your Oracle Access Governance service instance.

To configure the Oracle Access Governance Service Catalog application connection refer to the[Oracle Access Governance Service Catalog Installation Guide](https://store.servicenow.com/store/app/88a5f81c477b62902ec7c1c4f16d4302#linksAndDocuments).

## Oracle Access Governance Service Catalog Application Scheduler

Once you have installed and configured the Oracle Access Governance Service Catalog application in your ServiceNow instance, you can refresh the status of requests and load access bundles from your Oracle Access Governance service instance.
To schedule access bundles loading:
- In the ServiceNow UI set the application scope to Oracle Access Governance Service Catalog.
- Navigate to the ServiceNow UI and search for the Oracle Access Governance Service Catalog application.
- Select Load Access Bundle from the ServiceNow application navigator.
- The Load access bundle list job is displayed. This job will load the current access bundle from Oracle Access Governance into Oracle Access Governance Service Catalog making them available for request from the ServiceNow portal page. The job allows you to perform the following tasks:
- Load access bundles on request by selecting the Execute Now option.
- Activate/de-activate the job
- Set conditions for the job
- Setup a time when the job should be run e.g. daily, weekly.
To synchronize status of access requests:
- Navigate to the ServiceNow UI and search for the Oracle Access Governance Service Catalog application.
- Select Sync Request Status from the ServiceNow application navigator.This job will synchronize access request status Oracle Access Governance to Oracle Access Governance Service Catalog ensuring that the correct status of request is shown in the ServiceNow portal page. The job allows you to perform the following tasks:
- Synchronize on request by selecting the Execute Now option.
- Activate/de-activate the job
- Set conditions for the job
-
