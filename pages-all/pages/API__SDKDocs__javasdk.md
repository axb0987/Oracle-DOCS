# SDK for Java
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdk.htm
- Fetched: 2026-09-05 01:36 CDT

# SDK for Java

The Oracle Cloud Infrastructure SDK for Java enables you to write code to manage Oracle Cloud Infrastructure resources.

This SDK and sample is dual-licensed under the Universal Permissive License 1.0 and the Apache License 2.0; third-party content is separately licensed as described in the code.

Download:[GitHub](https://github.com/oracle/oci-java-sdk/releases)or[Maven](https://central.sonatype.com/search?q=oci-java-sdk&namespace=com.oracle.oci.sdk).
Tip  
  

Cloud Shell: The SDK for Java is pre-configured with your credentials and ready to use immediately from within[Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cloudshellintro.htm). For more information on using the SDK for Java from within Cloud Shell, see[SDK for Java Cloud Shell Quick Start](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cloudshellquickstart_java.htm).

Oracle Linux Cloud Developer image: The SDK for Java is pre-installed on the Oracle Linux Cloud Developer platform image. For more information, see[Oracle Linux Cloud Developer](https://docs.oracle.com/iaas/oracle-linux/oci/developer-image.htm).

## Requirements

To use the SDK for Java, you must have the following:
- An Oracle Cloud Infrastructure account.
- A user created in that account, in a group with a policy that grants the desired permissions. This can be a user for yourself, or another person/system that needs to call the API. For an example of how to set up a new user, group, compartment, and policy, see[Adding Users](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm). For a list of typical policies you may want to use, see[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
- A key pair used for signing API requests, with the public key uploaded to Oracle. Only the user calling the API should be in possession of the private key. For more information, see[Configuring the SDK](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkgettingstarted.htm#Configur).
- Java 8, Java 11, Java 17, or Java 21 (see[Java Support Notes](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdk.htm#javasdk_topic_Requirements_Java_Support)).
- A TTL value of 60. For more information, see[Configuring the SDK](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdkgettingstarted.htm#Configur).

### Java Support Notes

Java 17 Support
- Versions 2.23.0 and later of the OCI SDK have been tested to run and compile with Java 17.

Java 11 Support
- The OCI SDK for Java has been tested with Java version 11.
- Java 8 is required to build the OCI SDK for Java from source, but once it's built you can use the OCI SDK for Java with Java version 11.
- For OCI Java SDK versions before 1.27.0, you need to include the`javax.bind`and`sun.bind`dependencies, since Java 11 no longer includes Java EE and CORBA modules. For more information, see the[JDK 11 Release Notes](https://docs.oracle.com/en/java/javase/11/migrate/index.html#JSMIG-GUID-4B3D2D73-359C-4ADA-937E-BAEA79CFDF0F).

Java 21 Support
- Versions 3.25.2 and later of the OCI SDK have been tested to run and compile with Java 21.

## Services Supported

- Access Governance
- Account Management
- AI Data Platform
- AI Language
- AI Speech
- AI Vision
- Analytics Cloud
- Announcements
- API Gateway
- Application Dependency Management
- Application Management
- Application Performance Monitoring
- Audit
- Autonomous Recovery
- Autoscaling (Compute)
- Bastion
- Batch
- Big Data Service
- Blockchain Platform
- Budgets
- Build
- OCI Cache
- Certificates
- Cloud Bridge
- Cloud Guard
- Cloud Migrations
- Cluster Health
- Cluster Placement Groups
- Compute Cloud@Customer
- Compute Instance Agent (Oracle Cloud Agent)
- Console Dashboard
- Kubernetes Engine
- Container Instances
- Container Registry
- Content Management
- Core Services (Networking, Compute, Block Volume)
- Connector Hub
- Cost Anomaly Detection
- Data Catalog
- Data Flow
- Data Integration
- Data Labeling
- Data Science
- Data Safe
- Database
- Database Lifecycle Management
- Database Management
- Database Migration
- Database Tools
- Database Tools Runtime
- Data Infrastructure Cloud@Customer
- Delegate Access Control
- Demand Signal
- DevOps
- Digital Assistant
- Digital Media
- Disaster Recovery
- DNS
- Document Understanding
- Email Delivery
- Enterprise Manager Warehouse
- Events
- Exadata Fleet Update
- File Storage
- File Storage with Lustre
- Fleet Application Management
- Functions
- Fusion Apps as a Service
- Generative AI
- Generative AI Agent
- Generative AI Inference
- Generic Artifacts
- Globally Distributed AI Database
- GoldenGate
- Governance Rules
- Health Checks
- IAM
- Identity Domains
- Integration
- Internet of Things
- Java Management
- Java Management Service Downloads
- Key Management (for the Vault service)
- License Manager
- Limits
- Load Balancer
- Logging
- Log Analytics
- Logging Search
- Logging Ingestion
- Managed Access
- Managed Services for Mac
- Management Agent Cloud
- Management Dashboard
- Marketplace
- Marketplace Private Offer
- Monitoring
- Multicloud
- MySQL HeatWave
- Network Firewall
- Network Load Balancing
- Network Monitoring
- Networking Topology
- NoSQL Database Cloud
- Notifications
- Object Storage
- OCI Control Center
- OCI Registry
- OCI Secure Desktops
- OneSubscription
- Operations Insights
- Operator Access Control
- Optimizer
- Organizations
- OS Management
- OS Management Hub
- PostgreSQL
- Process Automation
- Publisher
- Queue Service
- Quotas
- Resource Manager
- Resource Analytics
- Resource Scheduler
- Roving Edge Infrastructure
- Search
- Secret Management (for the Vault service)
- Secure Desktops
- Security Attribute
- Service Catalog
- Service Mesh
- Source Code Management
- Stack Monitoring
- Streaming
- Streaming with Apache Kafka
- Support Management
- Threat Intelligence
- Usage
- Visual Builder
- VMWare Solution
- Vulnerability Scanning
- Web Application Acceleration and Security
- WebLogic Management
- Work Requests (Compute, Database)
- Zero Trust Packet Routing

## Contact Us

### Contributions

Got a fix for a bug or a new feature you'd like to contribute? The SDK is open source and[accepting pull requests](https://github.com/oracle/oci-java-sdk/blob/master/CONTRIBUTING.md)on[GitHub](https://github.com/oracle/oci-java-sdk).

### Notifications

To be notified when a new version of the SDK for Java is released, subscribe to the[Atom feed](https://github.com/oracle/oci-java-sdk/releases.atom).

### Questions or Feedback
- [GitHub Issues](https://github.com/oracle/oci-java-sdk/issues): To file bugs and feature requests only
- [Stack Overflow](https://stackoverflow.com/): Please use the[oracle-cloud-infrastructure](https://stackoverflow.com/questions/tagged/oracle-cloud-infrastructure)and[oci-java-sdk](https://stackoverflow.com/questions/tagged/oci-java-sdk)tags in your post
- [Developer Tools section](https://cloudcustomerconnect.oracle.com/resources/9c8fa8f96f/search/posts?find=&daysBack=0&userName=&tagName=Developer+Tools&type=)of the Oracle Cloud forums
- [My Oracle Support](https://support.oracle.com)
