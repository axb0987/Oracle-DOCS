# Identity Orchestration Components
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm
- Fetched: 2026-09-05 03:14 CDT

# Identity Orchestration Components

Identity Orchestration components serve as the building blocks that unify diverse systems and effectively manage the identity lifecycle for your enterprise. These include Oracle Access Governance agent for indirect integrations, inbound and outbound data transformation rules for ensuring data coherence, correlation rules to build composite profiles, and Orchestrated System Resources to effectively manage resources and control sources used to load the data.

## Access Governance Agent

The Oracle Access Governance agent is a downloadable docker image, which allows Oracle Access Governance to synchronize continuously or periodically with Authoritative Sources or Managed Systems where a direct connection is not available.

The agent runs scheduled distributed extract-transform-load (ETL) jobs to perform full or incremental synchronization of remote identity data, such as users, roles, application instances, entitlements, and entitlement assignments, to Oracle Access Governance. Once registered and installed, the agent can be monitored via the Oracle Access Governance Console. The agent runs in a docker environment located in your local (customer) environment. This environment should meet the following prerequisites:
- Installation of Docker or Podman
- Allow connection to the customer's target identity database
- Allow connection to the customer's Oracle Access Governance instance hosted in Oracle Cloud. If required, this connection can be made through a web proxy.

The agent extracts data, picked up by the Oracle Access Governance ingestion service, and is loaded into Oracle Access Governance for consumption.

Fulfillment requests (provisioning of accounts or closed-loop access remediation) are passed on to Managed systems. For example, on completion of access review campaigns, any permissions that have been revoked in Oracle Access Governance will be remediated by raising a revoke operation in the Orchestrated system. This revoke request will be passed to the Managed system via the agent.
Note  
  
Agents are applicable only in cases where a direct connection cannot be established with Oracle Access Governance. Typically, you will need an agent when integrating with the on-premises systems. The Oracle Access Governance agent acts as an arbitrator supporting the synchronization of Authoritative Sources or Managed Systems and Oracle Access Governance.

## Data Transformations

Different systems represent data differently. Oracle Access Governance allows you to manipulate and transform incoming identity and account data from Authoritative Source or Managed Systems, or outgoing data being provisioned to Managed Systems. You can modify data values to meet your requirements, such as including derived values or ensuring consistent formatting. This ensures data coherence and system unification.
You can apply data transformations to:
- Enhance incoming identity attributes being ingested from an Authoritative Source into Oracle Access Governance using inbound transformation rules. For example, you can set the username to uppercase, or concatenate the family name with the name to create a display name.
- Enhance incoming account attributes being ingested from Managed Systems into Oracle Access Governance using inbound transformation rules. For example, you can concatenate username with default domain to set the primary email within Oracle Access Governance.
- Customize composite identity attributes built up in Oracle Access Governance so that you can match incoming attributes. For example, Database User Management applications store username in a specific format and, as it contains only account data, you would need to customize the composite identity attributes in Oracle Access Governance so that incoming DBUM username matches with identity attributes available in Oracle Access Governance.
- Define account attributes by enhancing identity attributes for account provisioning by Oracle Access Governance into Managed Systems. For example, setting jobDescription to some fixed value, in case you have a null value.

### Transformation Types and its Workflow
  

  

Let's see the types of transformations available in Oracle Access Governance and its workflow:

- You first integrate an Authoritative Source with Oracle Access Governance by adding an Orchestrated system. Here, you can execute inbound transformations on the source identity attributes data during the data ingestion process. For example, you may integrate Oracle HCM as an Authoritative Source and apply inbound transformations to create a display name from the full name. These transformations are unique and specific to each Orchestrated system.
- Once you integrate Authoritative source systems, internally, a composite identity profile is constructed that contains Core and Custom attributes within Oracle Access Governance. This composite identity profile can contain identity attributes from various Authoritative sources that you have integrated. For example, identity in Oracle Access Governance can contain attributes jobCode ingested from Oracle HCM and department ingested from Flat File. In the scenario where the same attribute is available in more than one Authoritative source, you have the option to select and change the Orchestrated system from which you want to bring this attribute value. Refer to[Manage Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm)for more details. This composite identity profile acts as a source of truth for Oracle Access Governance to perform various governance and provisioning operations.
- Next, you integrate Managed Systems to load account attributes. These account attributes are matched against composite identity attributes available within Oracle Access Governance.
- For outbound provisioning, you manipulate the composite identity attributes available in Oracle Access Governance for accurate account provisioning into Managed Systems.

### Inbound Data Transformation

Inbound data transformations allow you to control how attribute values are transformed when they are received from an orchestrated system into Oracle Access Governance. When you load data from an Orchestrated system, identity and account attributes will be imported into Oracle Access Governance. During the data load or data ingestion process, it is possible to apply data transformations to the attributes.

An example use case might include some of the following:
- Populate the primaryEmail identity attribute in Oracle Access Governance by concatenating FirstName, ., LastName, @mydomain.com. This is how you achieve this in Oracle Access Governance.
```
[](http://mydomain.com/)
```

- Set the value of an attribute to another value if the value coming from the orchestrated system is null. An example might be if the organization is null then set the value in Oracle Access Governance to a fixed value.
```

```

### Outbound Data Transformation

Identity Orchestration includes the ability to provision accounts using the[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm)(self service),[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm)(for others), or[policy](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm#create-a-policy)based access functionality. As part of this process, it is possible to apply data transformations to the data provisioned into the Managed system account. When provisioning operations such as Reset password or Create Account are triggered in Oracle Access Governance, data transformation rules can be invoked which derive values from the identity data and transform the data using strings and other manipulations, so that provisioning of accounts is done against correct identities into Managed system.
An example use case might include some of the following:
- Populate the workEmail attribute in the provisioned Managed system with the identity primaryEmail attribute value.
- Create a value for the displayName attribute in the provisioned Managed system by concatenating the identity title , userName , and employeeNumber .
- Set the value of an attribute to another value if the identity input value is null. An example might be if organization is null then set the value to a fixed value in the provisioned Managed system account.

### Identity Attributes: Customizing Composite Oracle Access Governance Identity Profile by Applying Transformation Rules

When you load identity attributes from various Authoritative Sources, a composite identity profile is built in Oracle Access Governance, containing identity attributes from various sources. When you load account attributes from Managed Systems, the values available in this composite identity profile are matched with account attributes (Identity Account Matching). In special circumstances, you may have to apply additional transformation rules on this composite identity profile so that it can match the incoming data from various systems. Typically, you require this type of transformation to customize an identity attribute within Oracle Access Governance so that it matches the account attributes incoming from Managed Systems.
Note  
  
Inbound Transformations are specific to Orchestrated System and Identity Attribute Customization is applied on the composite identity profile built in Oracle Access Governance. For example, if you have applied inbound transformation on JobCode ingested from Oracle HCM but you have selected Flat File as the source for this attribute in the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm)page, then this transformation won't have any impact on the value available in Oracle Access Governance.

Scenario

For example, your Database User Management (DBUM) may store an attribute, such as a username in a very specific format, different from the username available in the composite identity profile within Oracle Access Governance. To match a DBUM account with the identity that exists in Oracle Access Governance, you need to customize the Identity Attribute by applying transformation rules. As DBUM is a Managed System account, you cannot manipulate identity data by applying inbound transformation rules. That's where you need to customize composite Identity Attributes. For example, when you connect MySQL DBUM, Oracle Access Governance adds an internal identity attribute userNameMysql , with the applicable transformation rules. Then you can match username incoming from My SQL DBUM with userNameMysql identity attribute. The same rule is applied on the outbound transformation side so that the provisioning of accounts is done accurately.

Authoritative Source Composite Identity Attribute Managed System

- Identity Attribute : username
- Value : John.Doe@o.com
- Identity Attribute : username
- Value : John.Doe@o.com
- Account Attribute : userLogin
- Value : John_Doe@o.com

- Internal Identity Attribute : userNameMysql
- Value : John_Doe@o.com

The Identity attribute username has a different value than Account Attribute userLogin and we cannot match these attributes. The composite identity attributes transformation will transform John.Doe@o.com to John_Doe@o.com and store in the userNameMysql created within Oracle Access Governance. Once that is done, the incoming value, John_Doe@o.com , will match.
Note  
  
As a best practice, we recommend using inbound transformations to transform an identity attribute and limit the use of applying transformation rules on the composite identity profile. It may interfere with the provisioning of accounts.

## Account Attributes

Account Attributes in Oracle Access Governance allow administrators to configure additional account attributes beyond the default ones supported for an orchestrated system. You can source values for account attributes from a managed system, from Global key values reference file, or define it when creating an access bundle.

When you configure an orchestrated system it will include a default set of attributes that provide details of an account as defined for the particular target system you are using as your source. In some cases you may have a requirement to include additional attributes in your integration that are present in the target system, but are not exposed by default. This is where account attributes come in.
Account attributes allow you to configure additional attributes for your orchestrated system which can be reconciled from a managed system, or can be provided as a value passed when a user requests an access bundle. Oracle Access Governance provides support for the following account attribute features:
- User can view account attributes for a specified orchestrated system. The user can view default attributes created as part of orchestrated system initialization, as well as account attributes created by user.
- User can create account attributes in the orchestrated system definition.
- User can edit account attributes in the orchestrated system definition.
- User can delete account attributes in the orchestrated system definition.
- Account attributes support both simple and complex data types.
- Account attributes can be used in both inbound and outbound transformations.
- Account attributes are supported for orchestrated systems configured in managed system mode.
- Account attributes are not supported for:
- Oracle Cloud Infrastructure (OCI) orchestrated systems.
- Oracle Identity Governance orchestrated system.
- Orchestrated systems configured in authoritative source mode.
- User-created account attributes are not available for:
- Database Application Table orchestrated systems.
- Generic REST orchestrated systems.

Let's look at some simple usecases:

### Usecase: Add account attribute using access bundle definition
Figure 1. Add account attribute

In this usecase the administrator has created an account attribute which is mapped the Description attribute in the managed system, and has value source set to access bundle. They have also defined an access bundle which includes the account attribute. When a user requests the access bundle, they are prompted to enter a value for Description . Once the access bundle request is approved, the account is provisioned to the managed system. The value of the Description attribute entered by the user may or may not be subject to an outbound transformation. Finally, the value of Description is provisioned as part of the account created for the user.

### Usecase: Reflect identity attribute update in account attribute
Figure 2. Identity attribute update

In this use case an administrator has created an account attribute postalCode which as well as being mapped to the managed system is also associated with an identity attribute, Location . Assume that we have an identity in Oracle Access Governance for a user, Alice. Alice's identity is derived from an authoritative source such as Oracle HCM. Alice moves house, resulting in a change to the Location value in Oracle HCM. On the next data load, this update will be reflected in Oracle Access Governance where Alice's identity:Location attribute will be updated. With account attributes, this change will also trigger an Update account activity which will update the value of account:postalCode with the contents of identity:Location. In this way, you can synchronize your account attributes with values derived from an authoritative source.

## Account Profiles - Reusable Templates for Access Bundle Generation

Account profiles in Oracle Access Governance serve as reusable templates that standardize and simplify the creation of new user accounts in managed systems by pre-defining and storing default values for their account attributes. This streamlines user provisioning, ensuring data consistency and reducing manual effort.

### Account Profiles in Oracle Access Governance Overview

When you provision new user accounts to a managed system from Oracle Access Governance, you need to pass some mandatory information or common attributes. Account profiles act as a blueprint allowing you to define default values once for the common attributes needed by the managed system.

This ensures consistency in provisioning and eliminates the need to manually enter account details frequently in each access bundle, thereby simplifying permission management.

While defining account profiles, you may choose to provide default values or choose to ask the requester to provide values during the self-service request.

When you link an account profile to an access bundle, Oracle Access Governance seamlessly populates the necessary default information during user provisioning, ensuring that the new account is created successfully with accurate and consistent data.

An account profile can be linked to multiple access bundles, as it is not specific to any single one.
Note  
  
You can only assign a single account profile to an access bundle.

### Key Features of Account Profiles

Let us explore the capabilities of account profiles by examining the key features.

- Referential Integrity: Prevents the deletion of an account profile if it is linked to an access bundle, maintaining data consistency and referential integrity.
- Centralized Updates: Updating an account profile attribute value propagates that change across all associated access bundles. This triggers provisioning requests for affected users with the updated account attribute value. This eliminates the manual effort of updating individual access bundles.
- Reusable Templates: Serve as bundled snapshots of attributes that can be easily re-purposed across different access bundles, eliminating redundant configuration.

## Matching Rules

Oracle Access Governance leverages correlation, or matching, rules to match the identity data ingested from different Authoritative sources, and thus build a composite identity profile. Similarly, during data ingestion from Managed Systems, several accounts might exist for an identity. In this case, account data needs to be ingested and matched to the respective identities. Account matching rules can be leveraged to associate user accounts ingested from downstream applications with identities in Oracle Access Governance. If you have a system that acts both as Authoritative Source and Managed System within Oracle Access Governance , then you can implement identity matching and account matching for the same system.

You can easily build these correlation rules in Oracle Access Governance using identity and account attributes. If an account cannot be automatically matched to an identity, Oracle Access Governance creates a micro-certification for this unmatched account, so that it can be manually matched with the identity or remediated from the Managed System.

### Types of Matching Rules

When data is received from an Orchestrated system, Oracle Access Governance checks to see if the data matches data already onboarded as an identity or account. Oracle Access Governance supports the following matching types:
- Identity matching : This match checks if an incoming identity matches an existing identity or is new to Oracle Access Governance. If it is a match, then the incoming data is correlated with the existing identity. If there is no match, then the data is used to create a new identity in Oracle Access Governance.
- Account matching : This match checks if an incoming account matches with an existing identity. If there is a match the account information is correlated with the matching identity. If no match is found, then the account is flagged as unmatched.

### Insights for Match Results

Use the insights to view a list of incoming accounts or identities, including matched, unmatched or multi-matched identities or accounts.
- No Match : The incoming identity or account isn't linked to an existing identity. Match it manually to the correct identity, or take the appropriate remediation action for the system.
- Matching Rule : Identities or accounts are matched automatically based on the configured matching rules.
- Multi-match : Several matches found to an identity, Review accounts or identities and manually match to the correct identity.
- User deleted : Displays orphan accounts that were previously linked to an identity, but the associated identity was deleted from the authoritative source. The account remains in the managed system with no associated identity.
- Provisioned by AG : The account is matched because it was created or provisioned through Oracle Access Governance. If the account shouldn't be linked, unlink the account.
Note  
  
Some account attribute values might be masked (displayed as asterisks, "********") based on your organization's policies. See:[Configure Account Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-account-attributes).

Based on the application role, you can perform the actions from various modules within Oracle Access Governance. For details, see[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)and[Performing Account Lifecycle Operations in Data Browser](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-operations.htm#data-browser-ops).

## Orchestrated System Resources

You can decide which resources you want to ingest from systems allowing full control of the source used to load data into Oracle Access Governance. You can manage which resources are populated from orchestrated systems. This functionality is very specific to Oracle Identity Governance.

A typical use case might be where you have identity data managed by Oracle Identity Governance (OIG), and you want governance in a hybrid fashion till the time you migrate completely to the cloud environment. By default, all resources ingested from the Authoritative Source and Managed System will be available to Oracle Access Governance. As you add direct connections between Oracle Access Governance and systems, you can remove these from your primary governance system to avoid duplication of data.
For example, you have onboarded identities from the Oracle Unified Directory (OUD) by using the OIG orchestrated system in Oracle Access Governance. To migrate your OUD identities directly, rather than coming from OIG, you would establish a direct integration with the OUD system in Oracle Access Governance. Once you have tested and implemented this direct configuration, you can disable the Oracle Unified Directory resource in the Oracle Identity Governance orchestrated system. The remaining resources enabled in the Oracle Identity Governance Orchestrated system would continue as usual.

## Understanding Virtual Systems for an Orchestrated System

Virtual Systems allow a single orchestrated integration to represent and manage multiple related applications or domains as logical subsystems. This is helpful where an enterprise might have multiple domains or subsystems that need to be managed, each with different data but sharing the same structural schema.

Instead of creating and managing a separate orchestrated system for every domain, virtual systems enable you to:
- Group multiple applications under a single orchestrated system.
- Store and process data files per application according to the mapping.
- Manage these applications individually for provisioning for access control features.

Applies to : Flat File

Example

Suppose your enterprise integrates three AD domains: Alpha , Beta , and Gamma . Without virtual systems, each would require a separate orchestrated system
With virtual systems
- Configure a single orchestrated system (for example,`Flatfile-MultiApp-01`) and enable the virtual systems.
- Upload a CSV like with id and name:

ID Name
virtual_ad_123 Alpha
virtual_ad_456 Beta
virtual_ad_789 Gamma
- After successful integrations, see the bucket structure:
```

```

Note  
  
Sub folders, such as virtual_ad_123, virtual_ad_456, and so on are created only when virtual systems are enabled.
- Perform the post configuration steps to add the data files in the respective folders. Any schema extension for an orchestrated system would be applied across all virtual systems. For more information, see[Integrate with Flat File - Post Configuration](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-flat-file.htm#file-postconfig)
