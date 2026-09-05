# SDK for Go
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/gosdk.htm
- Fetched: 2026-09-05 01:36 CDT

# SDK for Go

The Oracle Cloud Infrastructure SDK for Go enables you to write code to manage Oracle Cloud Infrastructure resources.

This SDK and sample is dual-licensed under the Universal Permissive License 1.0 and the Apache License 2.0; third-party content is separately licensed as described in the code.

Download: Download the SDK from[GitHub](https://github.com/oracle/oci-go-sdk/releases).

Documentation: The reference documentation is available from Oracle[here](https://docs.oracle.com/iaas/tools/go/latest/)and at[godoc.org](https://godoc.org/github.com/oracle/oci-go-sdk).
Tip  
  

Cloud Shell: The SDK for Go is pre-configured with your credentials and ready to use immediately from within[Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cloudshellintro.htm). For more information on using the SDK for Go from within Cloud Shell, see[SDK for Go Cloud Shell Quick Start](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cloudshellquickstart_go.htm).

Oracle Linux Cloud Developer image: The SDK for Go is pre-installed on the Oracle Linux Cloud Developer platform image. For more information, see[Oracle Linux Cloud Developer](https://docs.oracle.com/iaas/oracle-linux/oci/developer-image.htm).

## Requirements

To use the SDK for Go, you must have the following:
- An Oracle Cloud Infrastructure account.
- A user created in that account, in a group with a policy that grants the required permissions. This can be a user for yourself, or another person/system that needs to call the API. For an example of how to set up a new user, group, compartment, and policy, see[Adding Users](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm#Adding_Users). For a list of policies to use, see[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#top).
- A key pair used for signing API requests, with the public key uploaded to Oracle. Only the user calling the API must have the private key. For more information, see[Configure the SDK](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File).
- A supported Go version. The SDK supports two most recent major releases of Go. To find the most recent Go version, see[Go Release History](https://go.dev/doc/devel/release).

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
- Cloud Migrations
- Cluster Health
- Cluster Placement Groups
- Compute Cloud@Customer
- Compute Instance Agent (Oracle Cloud Agent)
- Console Dashboard
- Kubernetes Engine
- Container Instances
- Content Management
- Core Services (Networking, Compute, Block Volume)
- Cloud Guard
- Connector Hub
- Cost Anomaly Detection
- Data Catalog
- Data Flow
- Data Integration
- Data Labeling
- Data Safe
- Data Science
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
- Integration Cloud
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
- PostgreSQL
- Process Automation
- Publisher
- Queue Service
- Quotas
- Resource Analytics
- Resource Manager
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

## Installing with Resource Manager

You can use[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)to[install the Oracle Cloud Development Kit on a Compute instance in your compartment](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/devtools.htm). The Oracle Cloud Development Kit includes the SDK for Go, along with other Oracle development tools.

## Installing with yum

If you're using Oracle Linux 7 or 8, you can use yum to install the OCI SDK for Go. GoLang 1.16.3 will also be installed.

For Oracle Linux 7:

```

```

For Oracle Linux 8:
```

```

The OCI Go SDK will be located in`/usr/share/gocode/src/github.com/oracle/oci-go-sdk`.
Golang 1.16.3 enables the go module by default, even when no`go.mod`is present. You need to turn the go module off to ensure that the OCI Go SDK can be referenced from the filesystem where yum installed the Go SDK. To do so, set the following environment variables:
```

```

## Contact Us

### Contributions

Got a fix for a bug or a new feature you'd like to contribute? The SDK is open source and[accepting pull requests](https://github.com/oracle/oci-go-sdk/blob/master/CONTRIBUTING.md)on[GitHub](https://github.com/oracle/oci-go-sdk).

### Notifications

To be notified when a new version of the SDK for Go is released, subscribe to the[Atom feed](https://github.com/oracle/oci-go-sdk/releases.atom).

### Questions or Feedback
- [GitHub Issues](https://github.com/oracle/oci-go-sdk): To file bugs and feature requests only
- [Stack Overflow](https://stackoverflow.com/): Please use the[oracle-cloud-infrastructure](https://stackoverflow.com/questions/tagged/oracle-cloud-infrastructure)and[oci-go-sdk](https://stackoverflow.com/questions/tagged/oci-go-sdk)tags in your post
- [Developer Tools section](https://community.oracle.com/community/oracle-cloud/cloud-infrastructure/content?filterID=contentstatus%5Bpublished%5D~category%5Bdeveloper-tools%5D)of the Oracle Cloud forums
- [My Oracle Support](https://support.oracle.com)
