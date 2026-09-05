# Identity Orchestration Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-overview.htm
- Fetched: 2026-09-05 03:14 CDT

# Identity Orchestration Overview

Identity Orchestration is an Oracle Access Governance framework that brings together diverse Authoritative and Managed Systems by supporting low-code integrations. It facilitates data transformations and correlation rules which ensures data coherence, extracts the required identity data from various systems into Oracle Access Governance, and performs fulfillment through account provisioning.

The entire orchestration process involves:
- Integrating with various on-premises or cloud systems through low-code integration.
- Extracting or ingesting only the required information (identity attributes, permission assignments, and policies) into Oracle Access Governance.
- Transforming and correlating the ingested data, both identity and account attributes, to build a composite identity profile and account information.
- Processing the identity data and using it for access controls, access reviews, workflows, etc.
- Provisioning, and synchronizing data between the Orchestrated systems.

## Significance of Identity Orchestration: Why Modern Identity Orchestration is Essential for your Enterprise

Identity Orchestration is crucial for a complex and dynamic IT ecosystem that may include the distributed nature of IT infrastructure, deployments across on-premises, demilitarized zone (DMZ), multi cloud, and IoT environments. Without this, enterprises face critical issues such as limited visibility of identity-related activities, fragmented access control, operational inefficiency, and a higher likelihood of security threats and compliance issues.
Members in your enterprise may use a variety of systems in their workday routine, such as Oracle HCM for resource management, Microsoft Teams as a collaboration suite, Oracle CRM for customer management, internal database applications, and legacy mainframe applications. In such a heterogeneous setup, Identity Orchestration plays a vital role in providing a comprehensive and centralized identity management and governance system. It allows you to seamlessly integrate various systems, extract and ingest only the required attributes, build a composite identity profile using data transformation and correlation rules, and finally, enabling fulfillment through account provisioning.

Managing identities and their respective accesses require seamless identity and access orchestration for effective identity lifecycle management, governance and compliance. Modern Identity Governance systems, such as Oracle Access Governance, offer a holistic Identity Orchestration system that provides low-code integrations, data correlation and data transformation capabilities along with fulfillment. This enables thorough access discovery, comprehensive insights into identity profiles and clearly stated access controls, access reviews, and micro-certifications.

## Integrations in Oracle Access Governance

Oracle Access Governance simplifies identity orchestration by offering a wide range of specialized and generic out-of-the-box integrations, requiring minimal configurations.
- Specialized Integrations : Integrations for specific applications, providing application-specific use cases. For example, integration with Oracle Human Capital Management (HCM), Microsoft Entra ID, Microsoft Teams, etc.
- Generic Integrations : Integrations for constrained or sensitive applications, or for applications with unsupported data structures. You can achieve the integration by using a Flat File or Generic Rest API, offering flexibility and broader compatibility.

Oracle Access Governance carries out integrations either through API (direct integration) with cloud services and systems in public domains or using an agent, which is a downloadable docker image, for systems behind firewalls. These systems and applications can be integrated either as Authoritative Sources or Managed Systems .

## Identity Orchestration Functional Overview

  

  

Let's understand the steps involved:
- Identity Data Synchronization + Correlation Rules + Inbound Data Transformation : In the first step, there’s synchronization of identity data from Authoritative Sources along with execution of correlation rules and inbound transformation on the ingested identity data. This is where Oracle Access Governance identities are created.
- Identity Profile + Identity Attributes : In the second step, a composite identity profile is built by customizing and configuring identity attributes within Oracle Access Governance.
- Correlation Rules + Inbound Data Transformation + Account Reconciliation : In the third step, there's execution of correlation rules and inbound transformation on the ingested account and permissions data from Managed Systems. During this process, your accounts are reconciled against identities. This is where Oracle Access Governance accounts are created, and are used for performing provisioning operations.
- Identity lifecycle + Access control + Access reviews : In the forth step, you can perform usual Oracle Access Governance features, such as managing identity lifecycle, executing access reviews, setting up access controls and approval workflows within Oracle Access Governance.
- Outbound Data Transformation + Account Provisioning : At last, Oracle Access Governance supports outbound data transformations which uses identity attributes to define account attributes for provisioning in the Managed Systems. For example, applying default values to null values or changing format of an attribute to maintain coherence throughout provisioning process.

### Authoritative Source and Managed System

Based on the type of identity and access data extracted from systems or applications, Oracle Access Governance segregates the systems into:
- Authoritative Source : Trusted source of identity data and identity attributes that can be used by Oracle Access Governance to load and manage identity data. A few examples can be Oracle Identity Governance, Microsoft Entra ID (formerly known as Azure Active Directory), or any HR system to manage identity data and its attributes, such as email address, username, location, or department.
- Managed System : Applications and services containing accounts and respective access privileges but do not serve as a trusted source of identities in your enterprise information, for example, Oracle Database User management, Salesforce, and Microsoft Teams. By establishing an orchestrated system, Oracle Access Governance manages user accounts and access permissions for these applications leveraging the defined access controls (including access request, RBAC, ABAC, and PBAC).
- Authoritative Source and Managed System : Systems and applications can fulfill both roles, serving as the authoritative source for identity data while also acting as a Managed Systems for governing access.

### Data Transformation and Correlation Rules
The key tenets of seamless identity orchestration include:
- Correlation Rules : You can leverage correlation or matching rules to match the identity data ingested from different Authoritative Sources, and thus build a composite identity profile. Similarly, during data ingestion from Managed Systems, multiple accounts may exist for an identity. You can match the account data with the respective identities to associate the user accounts ingested from Managed Systems with the identity. For example, you can match User Login coming from the Orchestrated System with Employee user name ingested in Oracle Access Governance.
- Inbound Data Transformations : Applications, whether Authoritative Sources or Managed Systems, may present data in different formats. During the data ingestion process from Authoritative Sources to Oracle Access Governance, you can transform the identity data to enhance the identity profile information using Inbound Transformation rules. For example, you may want to concatenate employee number with the first name to set a display name in Oracle Access Governance. Similarly, during the data ingestion from Managed Systems, you can define or customize account data using the Inbound Transformation rules. For example, during rebranding of a product, you may want to change the application display name to some other fixed value.
- Outbound Data Transformations : Oracle Access Governance offers Outbound Transformation rules, where you use identity attributes to define account attributes for account provisioning in the Managed Systems. For example, you can set organization having null value to some default value.
