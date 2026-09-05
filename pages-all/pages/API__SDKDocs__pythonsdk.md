# SDK for Python
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/pythonsdk.htm
- Fetched: 2026-09-05 01:36 CDT

# SDK for Python

The Oracle Cloud Infrastructure SDK for Python enables you to write code to manage Oracle Cloud Infrastructure resources.

This SDK and sample is dual-licensed under the Universal Permissive License 1.0 and the Apache License 2.0; third-party content is separately licensed as described in the code.

Download: The SDK for Python is available on[GitHub](https://github.com/oracle/oci-python-sdk/releases)or the[Python Package Index (PyPi)](https://pypi.python.org/pypi/oci).

Reference documentation: Available on[docs.cloud.oracle.com](https://docs.oracle.com/iaas/tools/python/latest/).
Tip  
  

Cloud Shell: The SDK for Python is pre-configured with your credentials and ready to use immediately from within[Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cloudshellintro.htm). For more information on using the SDK for Python from within Cloud Shell, see[SDK for Python Cloud Shell Quick Start](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cloudshellquickstart_python.htm).

Oracle Linux Cloud Developer image: The SDK for Python is pre-installed on the Oracle Linux Cloud Developer platform image. For more information, see[Oracle Linux Cloud Developer](https://docs.oracle.com/iaas/oracle-linux/oci/developer-image.htm).

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
- Compute Cloud@Customer
- Compute Instance Agent (Oracle Cloud Agent)
- Kubernetes Engine
- Container Instances
- Content Management
- Core Services (Networking, Compute, Block Volume)
- Cloud Guard
- Cloud Migrations
- Cluster Health
- Cluster Placement Groups
- Connector Hub
- Console Dashboard
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
- OS Management Hub
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

## Python Support

### Supported Python Versions and Operating Systems

This table lists the versions of Python supported by the OCI SDK for Python for each operating system:

Operating System Supported Python Versions for CLI
CentOS 7 3.6 to 3.9
CentOS 8 3.6 to 3.9
Oracle Autonomous Linux 7.9 3.6 to 3.9
Oracle Linux 7.8 3.6 to 3.9
Oracle Linux 7.9 3.6 to 3.9
Oracle Linux 8 3.6 to 3.11
Oracle Linux 9 3.7 to 3.11
Ubuntu 18.0.4 3.6 to 3.11
Ubuntu 20.0.4 3.6 to 3.11
Windows Desktop 10 &amp; 11 3.6 to 3.11
Windows Server (2012/2016/2019) 3.6 to 3.11

Newer versions of Python may not be immediately supported. The OCI SDK for Python might work on unlisted operating systems, but we do not test them for compatibility.

## Installing with Resource Manager

You can use[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)to[install the Oracle Cloud Development Kit on a Compute instance in your compartment](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/devtools.htm). The Oracle Cloud Development Kit includes the SDK for Python, along with other Oracle development tools.

## Installing with yum

If you're using Oracle Linux 7 or 8, you can use yum to install the OCI SDK for Python.

The following example shows how to use yum to install the OCI SDK for Python 3.6:

```

```

This example shows how to use yum to install the OCI SDK for Python 2.7:

```

```

## Client-Side Encryption

Client Side Encryption allows you to encrypt data on the client side before storing it locally or using it with other Oracle Cloud Infrastructure services.

To use client-side encryption, you must create a master encryption key (MEK) using the Key Management Service. This can be done using the[CreateKey](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/CreateKey)or[ImportKey](https://docs.oracle.com/iaas/api/#/en/key/latest/Key/ImportKey)operations.

The MEK is used to generate a Data Encryption Key (DEK) to encrypt each payload. A encrypted copy of this DEK (encrypted under the MEK) and other pieces of metadata are included in the encrypted payload returned by the SDKs so that they can be used for decryption.

### Examples

The following code example shows how to encrypt a string:

```

```

The following example shows how to encrypt a file stream:

```

```

## Contact Us

### Contributions

Got a fix for a bug or a new feature you'd like to contribute? The SDK is open source and[accepting pull requests](https://github.com/oracle/oci-python-sdk/blob/master/CONTRIBUTING.rst)on[GitHub](https://github.com/oracle/oci-python-sdk).

### Notifications

To be notified when a new version of the SDK for Python is released, subscribe to the[Atom feed](https://github.com/oracle/oci-python-sdk/releases.atom).

### Questions or Feedback
- [GitHub Issues](https://github.com/oracle/oci-python-sdk/issues): To file bugs and feature requests only
- [Stack Overflow](https://stackoverflow.com/): Please use the[oracle-cloud-infrastructure](https://stackoverflow.com/questions/tagged/oracle-cloud-infrastructure)and[oci-python-sdk](https://stackoverflow.com/questions/tagged/oci-python-sdk)tags in your post
- [Developer Tools section](https://cloudcustomerconnect.oracle.com/resources/9c8fa8f96f/search/posts?find=&daysBack=0&userName=&tagName=Developer+Tools&type=)of the Oracle Cloud forums
- [My Oracle Support](https://support.oracle.com)
