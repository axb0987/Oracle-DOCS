# About Autonomous AI Database Workload Types
- Source: https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-autonomous-database-workloads.html
- Fetched: 2026-09-05 18:57 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-autonomous-database-workloads.html#dcoc-content-body)

# About Autonomous AI Database Workload Types

Autonomous AI Database supports different workload types, including: Lakehouse, Transaction Processing, JSON Database, and APEX Service. Each of these workload types provides performance improvements and additional features that support operations for the specified workload.

## About Oracle Autonomous AI Lakehouse

Autonomous AI Lakehouse is an evolution of Oracle’s Autonomous Data Warehouse that adds support for open-source technologies like Apache Iceberg. It provides a unified system for managing, accessing, and analyzing enterprise data across various clouds and platforms, while retaining longstanding Oracle database capabilities.

By integrating with Autonomous AI Database, Autonomous AI Lakehouse allows organizations to efficiently access and analyze data distributed across multiple environments, promoting interoperability and reducing data duplication. It provides a fact-based approach to integrating, managing, and processing enterprise data across cloud providers and platforms, leveraging open standards and existing Oracle database functions. Its features address both interoperability and performance needs for modern data management and AI workloads.

Key new features of Autonomous AI Lakehouse include:
- 

Unified Metadata Catalog: The Autonomous AI Database Catalog connects and unifies metadata from different sources (such as Databricks Unity, AWS Glue, and Snowflake Polaris), making it easier to find and work with data across clouds and systems.
- 

Native Iceberg and SQL Access: Users can query data in Apache Iceberg and other catalogs using SQL, without transferring or duplicating the data.
- 

Performance Optimization: The Data Lake Accelerator automatically scales resources during query execution, and frequently accessed Iceberg tables can be cached for faster retrieval.
- 

AI Workflow Tools: Built-in features (Select AI Agent, Data Science Agent) support development and deployment of AI-driven processes, as well as data exploration and preparation through natural language.
- 

Real-Time Data Integration: Oracle GoldenGate streams data from multiple sources into Iceberg tables for up-to-date analytics.
- 

Controlled Data Sharing: The Table Hyperlink feature allows sharing of current data sets with others via temporary, secure links.
- 

Cloud and Platform Compatibility: Supports use across AWS, Azure, GCP, OCI, as well as with platforms like Databricks and Snowflake, without restricting users to a specific environment.

To get started you create an Autonomous AI Database with workload type Lakehouse and specify the number of ECPUs and the storage capacity in TB’s for the Autonomous AI Database.

You can use Autonomous AI Database with Oracle Analytics Cloud or Oracle Analytics Desktop to easily create visualizations and projects that reveal trends in your company’s data and help you answer questions and discover important insights about your business.

## About Oracle Autonomous AI Transaction Processing

Autonomous AI Database is designed to support all standard business applications and deliver scalable query performance.

Autonomous AI Database provides all of the performance of the market-leading Oracle AI Database in an environment that is tuned and optimized to meet the demands of a variety of applications, including: mission-critical transaction processing, mixed transactions and analytics, IoT, and JSON document store.

To get started you create an Autonomous AI Database with the workload type Transaction Processing and specify the number of ECPUs and the storage capacity for the database.

You can use Autonomous AI Database with Oracle Analytics Cloud or Oracle Analytics Desktop to easily create visualizations and projects that reveal trends in your company’s operational data and help you answer questions and discover important insights about your business.

The following figure shows the Autonomous AI Database architecture with related components for transaction processing and mixed workloads.

[Description of the illustration autonomous-transaction-processing-architecture.png](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/img_text/autonomous-transaction-processing-architecture.html)

## About Autonomous AI JSON Database

Oracle Autonomous AI JSON Database is Oracle Autonomous AI Transaction Processing, but designed for developing NoSQL-style applications that use JavaScript Object Notation (JSON) documents. You can promote an Autonomous AI JSON Database service to an Autonomous AI Transaction Processing service.

Autonomous AI JSON Database uses the ECPU compute model for newly provisioned databases.

Oracle Autonomous AI JSON Database provides all of the same features as Autonomous AI Transaction Processing, with this important limitation : you can store only up to 20 GB of data other than JSON document collections. There is no storage limit for JSON collections. See[List the Non-JSON Objects on an Autonomous AI Database Instance](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/upgrade-json-transaction-processing.html#GUID-FA14865F-1469-440E-8092-1F96AC64F05A__SECTION_BDK_HFW_BGC)for more information on non-JSON objects subject to the 20 GB limit.

Development of NoSQL-style, document-centric applications is particularly flexible because the applications use schemaless data. This lets you quickly react to changing application requirements. There’s no need to normalize the data into relational tables, and no impediment to changing data structure or organization at any time, in any way. A JSON document has internal structure, but no relation is imposed on separate JSON documents.

With Oracle Autonomous AI JSON Database your JSON document-centric applications typically use[Simple Oracle Document Access (SODA)](https://docs.oracle.com/en/database/oracle/simple-oracle-document-access/adsdi/overview-soda.html#GUID-BE42F8D3-B86B-43B4-B2A3-5760A4DF79FB), which is a set of NoSQL-style APIs for various application-development languages and for the representational state transfer (REST) architectural style. You can use any SODA API to access any SODA collection.

SODA document collections are backed by ordinary database tables and views. To use other kinds of data, subject to the 20 GB limit, you typically need some knowledge of Structured Query Language (SQL) and how that data is stored in the database.

No matter what kind of data your applications use, whether JSON or something else, you can take advantage of all Oracle AI Database features. This is true regardless of the kind of Oracle Autonomous AI Database you use.

JSON data is stored natively in the database. In a SODA collection on an Autonomous AI Database JSON data is stored in Oracle’s native binary format, OSON.

## About Oracle APEX Application Development

Oracle APEX Application Development (APEX Service) is a low cost, Oracle Cloud service offering convenient access to the Oracle APEX platform for rapidly building and deploying low-code applications.

APEX Service uses the ECPU compute model for newly provisioned databases.

APEX Service is designed to support all standard business applications and deliver scalable query performance. You can promote APEX Service to Autonomous AI Transaction Processing service.

See[Oracle APEX Application Development](https://docs.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database/serverless/adbsb&id=apex-service)and[Update APEX Service to Autonomous AI Transaction Processing](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/upgrade-apex-transaction-processing.html#GUID-9FF563D1-60B6-44E6-B871-2A5A857771DC)for more information.

- [About Autonomous AI Database Workload Types](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-autonomous-database-workloads.html#GUID-E1C8C5F2-22FB-4225-A3B9-9E78277A5834)
- [About Oracle Autonomous AI Lakehouse](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-autonomous-database-workloads.html#GUID-4B91499D-7C2B-46D9-8E4D-A6ABF2093414)
- [About Oracle Autonomous AI Transaction Processing](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-autonomous-database-workloads.html#GUID-B90147B2-EA04-4147-9606-0413D9CC1589)
- [About Autonomous AI JSON Database](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-autonomous-database-workloads.html#GUID-00FCBE2F-D258-4681-9A84-8985999EC574)
- [About Oracle APEX Application Development](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-autonomous-database-workloads.html#GUID-125BC742-4228-465B-9B31-50E3BB9801E6)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
