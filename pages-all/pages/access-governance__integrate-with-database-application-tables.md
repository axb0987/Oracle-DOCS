# Integrate with Database Application Tables
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-database-application-tables.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Database Application Tables

Oracle Access Governance can be integrated with Database Application Tables, enabling identity orchestration, including on-boarding of identity (user) data, and provisioning of accounts.

## Overview: Integrate Oracle Access Governance with Database Application Tables

Database Application Tables can be defined as database-driven custom applications.
In terms of identity administration these applications are characterized by the following:
- Applications have no APIs for identity administration
- Each application can have a different set of schemas for identity, account, and permission data
- The application schema is not known to Oracle Access Governance prior to configuring and running the integration
- There is no direct mapping between the application database tables and any Oracle Access Governance entities
- There is no common pattern to how identity data is organized within the application schema. Identity data may be in a single table, or spread across many tables

The Database Application Tables integration enables the exchange of user data between a customer database and Oracle Access Governance.
The Database Application Tables integration supports the following elements:
- Database Application Tables as an authoritative (trusted) source of identity information allowing for reconciliation of identities created or modified in database tables.
- Database Application Tables as a Managed System enabling provisioning of application accounts in database tables.

## Database Application Tables Integration Architecture Overview

Integration with Database Application Tables allows you to retrieve identity data from a system, transport it to Oracle Access Governance, and ingest. Once a system is connected, you can perform provisioning and remediation tasks and operations, such as create, reconcile, update, delete, disable/enable, add/delete permission, and add/delete group, which are then reflected in the managed system.

  

  
Figure 1. DBAT Architecture
Database Application Tables integration is implemented using an Agent-based connection type. This means that a direct connection is not available, so an indirect connection is made between Oracle Access Governance and the required database instance using the[Access Governance Agent](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#access-governance-agent). The Database Application Tables integration supports the following modes:
- If you select the[Authoritative Source](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-overview.htm#identity-orchestration-functional-overview)configuration mode when you setup a Database Application Tables Orchestrated System, then Oracle Access Governance will retrieve identity data from the database instance and treat it as an authoritative (trusted) source of identity information.
- If you select the[Managed Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-overview.htm#identity-orchestration-functional-overview)configuration mode, then Oracle Access Governance will allow you to manage user accounts in the target database. This enables the provisioning of new accounts in customer database instances from Oracle Access Governance.

To identify the relevant schema for the integration, the Database Application Tables integration offers automatic schema discovery. This is the process of identifying the underlying database schema that contains your user data. Support is provided for Day-0 limited schema, and later modifications in the user schema are accommodated by Day-N support, which allows you to update the schema with any changes that have been made to the database tables, and apply them to your discovered schema

Details of the relevant user database tables are provided during agent creation. Details of the schema are stored in a schema file, which is located with the agent. Details of the schema can be updated by directly editing this file as required.
Connection to the database holding your user tables is made through an JDBC database connection. This allows the agent to:
- Discover the schema for your database-driven application
- Perform full or incremental data loads. For Database Application Tables (Oracle) you can configure partial data load, see[Configure Partial Data Load Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-partial-data-load-settings).
- Provision accounts

A full load of relevant identity and account data is made into Oracle Access Governance each time the load is run. If this is the first time that the load is made, then relevant identity and account structures are created in Oracle Access Governance as appropriate. On subsequent data load runs, all data is loaded to Oracle Access Governance and the ingestion process updates any changes since the last data load in the appropriate identity and account artefacts.

Once your orchestrated system is configured, you can provision accounts using Oracle Access Governance's provisioning engine which will take any request for accounts or permissions and pass it through the agent and onwards to the target database. Provisioning supports create, update, and revoke operations.

In the event that your schema file is lost or corrupted in any way, the Database Application Tables integration provides schema file recovery. This is useful in scenarios such as an agent crash or loss of the schema file.

## Database Application Tables Integration Functional Overview

Database Application Tables integration supports usecases including configuration of the Orchestrated System, dataload, account creation and revocation, change password, and assign and remove roles.

### Supported Integration Functions
Integration of Database Application Tables with Oracle Access Governance supports the following functions:
- Configure Orchestrated System
- Load Data
- Create Account
- Assign Permissions
- Remove Permissions
- Change Password
- Revoke Account

For full details of functions supported, refer to[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)

### An Example Account Lifecycle
Let's look at an example. You have created a new orchestrated system which is connected to the MyDBAT database instance which contains user data for your organization. The orchestrated system is configured for Authoritative Source and Managed System modes. On the first dataload, identity and account data is loaded into Oracle Access Governance. At this time the following details are created in Oracle Access Governance:
- An Oracle Access Governance identity is created, say MyAGIdentity , comprising authoritative data such as name, email, and location.
- An account is created in Oracle Access Governance for existing Database Application Tables roles, say DBATRole_Composer . We now have the following:
- MyAGIdentity
- MyDBATAccount
- DBATRole_Composer

After some time MyAGIdentity moves into a new position within their organization requiring the developer role. An access bundle DBATBundle_Developer is created in Oracle Access Governance which contains the development permissions required. This access bundle can be assigned as a result of a policy, role or request. Let's say the user requests the access bundle using the Request a new access option. On approval, the request triggers a provisioning operation which applies the changes to MyDBAT , assigning the Database Application Tables roles corresponding to the permissions contained in DBATBundle_Developer access bundle.
We now have the following:
- MyAGIdentity
- MyDBATAccount
- DBATRole_Composer
- DBATBundle_Developer
Additional accounts may be mapped to the MyAGIdentity identity over time from other managed systems giving us a profile like this:
- MyAGIdentity
- MyDBATAccount
- MyOracleDBAccount
- MyMSTeamsAccount

MyAGIdentity is then required to change their password. Using the My Access functionality in Oracle Access Governance Console, they change their password, which propagates the change to MyDBAT using Oracle Access Governance provisioning.
MyAGIdentity then moves into a role which means they no longer require an account on MyDBAT . In this case a revoke account provisioning task can be generated by revoking the identity's account as part of an access review. Alternatively, their association with customer database roles can be removed by removing the identity from the relevant Oracle Access Governance role or policy. In either case, this will result in a provisioning task which will revoke the account from the customer database, together with any related roles. The profile would now resemble:
- MyAGIdentity
- MyOracleDBAccount
- MyMSTeamsAccount

If the Database Application Tables Orchestrated System is configured in Authoritative Source mode, and you make an identity inactive, then the the MyAGIdentity identity is effectively disabled. In this case a provisioning task will be generated and applied to the Managed System.
We now have the following:
-
