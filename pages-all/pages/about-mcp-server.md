# About MCP Server
- Source: https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-mcp-server.html
- Fetched: 2026-09-05 18:57 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-mcp-server.html#dcoc-content-body)

# About MCP Server

The Oracle Autonomous AI Database MCP Server is a managed, multi-tenant server designed to provide secure, standardized access to database tools and features through the Model Context Protocol (MCP). It provides an MCP server for each Autonomous AI Database, enabling AI agents and client applications to interact seamlessly with custom and built-in Select AI Agent tools using MCP APIs.

MCP Server integrates with database identity, authorization, and governance frameworks, supporting enterprise-grade security, auditing, and compliance. Autonomous AI Database MCP Server is available for Autonomous AI Database Serverless and Dedicated Region as well supported multicloud environments - Google, AWS, Microsoft. MCP Server is supported with Oracle Autonomous AI Database versions 26ai and 19c. It eliminates the need for you to manage your own MCP server infrastructure.

## Benefits of MCP Server

MCP Server offers several advantages that enhance the integration, security, and management of AI-driven applications within Oracle Autonomous AI Database.

MCP Server provides a secure and efficient way to connect AI Agents supporting MCP to the Oracle Autonomous AI Database.The key benefits are:
- 

Enables seamless integration of Autonomous AI Database with MCP-compatible clients such as Claude Desktop, Visual Studio Code with Cline, and OCI AI Agent, while providing secure, governed, and scoped access.
- 

No customer-side MCP server infrastructure involved, reducing deployment effort.
- 

Integrated with database roles, supports network access control lists (ACLs) and Private Endpoint (PE) configurations.

## Feature Highlights of MCP Server

Explore key feature highlights of the MCP Server in the following table:

These features enable you to access MCP tools through agentic AI applications that support MCP clients. You must create tools using`DBMS_CLOUD_AGENT_AI`, which are then available as MCP tools when your database instance is MCP-enabled.

Features Descriptions
Enable MCP server A database administrator (DBA) or the`ADMIN`user can enable or disable the MCP server using OCI free-form tags. See[Enable MCP Server](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/use-mcp-server.html#GUID-397E59A6-0151-4A8B-9EDB-474A785FE4DA)for more details.
Create custom tools with Select AI Agent

Database users create custom tools using the`DBMS_CLOUD_AI_AGENT`PL/SQL package. See[Create Select AI Agent Tools](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/use-mcp-server.html#GUID-76B55076-6101-4161-B0AE-31C3D35D5241)for more details.

**Note**: You can use Java with MCP tools when the tool implementation is written in PL/SQL that calls Java stored procedures. Oracle AI Database supports Java when the Java Virtual Machine (JAVAVM) option is enabled in the database. To enable Java support in Autonomous AI Database, see[Use Oracle Java on Autonomous AI Database](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/autonomous-oracle-java.html#GUID-2516EE33-B38D-4270-BE52-30A4F9014E8B).

JavaScript functions created using Oracle AI Database Multilingual Engine (MLE) are not supported as MCP tools. For more information about JavaScript support in Oracle AI Database, see[Oracle Multilingual Engine (MLE) for JavaScript Overview](https://docs.oracle.com/en/database/oracle/oracle-database/26/mlejs/overview-multilingual-engine-javascript.html).

Authentication The MCP server supports authentication using database credentials. See[Configure MCP Server in AI Agent Application](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/use-mcp-server.html#GUID-B540AEF5-FB92-4091-9519-289C1B52B690)for more details.
Security Controls Implements rate limiting, Access Control List (ACL) and Private Endpoint (PE) enforcement, and fine-grained secured data access controls using Virtual Private Database (VPD) policies. See[Create and Register a VPD Policy](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/security.html#GUID-D5D50E8C-F366-4B4D-9AFB-D2CF8AC373EF)for more details.

## Architecture of MCP Server

This provides an overview of the MCP server architecture and its key components.

The MCP server architecture is organized into three key layers: Unified Security Layer, Multi-tenant MCP Server, and Select AI Agent Framework. Together, these layers provide a secure, governed, per-database MCP server that is natively integrated with Autonomous AI Database.

Unified Security Layer : With Unified Security Layer, you can:
- 

Enforce network ACLs and support for private endpoints
- 

Support for database identities
- 

Enforce database roles and Virtual Private Database (VPD) policies

Multi-tenant MCP Server : With the Multi-tenant MCP server, you can:
- 

Securely use Select AI Agent custom tools without managing MCP server deployment or infrastructure
- 

Log all interactions to database audit logs

Select AI Agent Framework : With the Select AI Agent framework, you can:
- 

Utilize tools defined through the Select AI Agent
- 

Create and update tools
- 

Manage the lifecycle of the tools that get exposed as MCP tools

See[Select AI Agent](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/select-ai-agent1.html#GUID-1681F862-4CF9-4A25-ADCC-1535429BD38F)for more details.

- [About MCP Server](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-mcp-server.html#GUID-568465D7-DA8D-4F6B-9328-AA551B1B1940)
- [Benefits of MCP Server](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-mcp-server.html#GUID-DA31A3DD-9EC2-438C-BD11-D73FD67C8B7E)
- [Feature Highlights of MCP Server](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-mcp-server.html#GUID-92862D7C-BB16-449B-AF6D-2959217197EC)
- [Architecture of MCP Server](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-mcp-server.html#GUID-56C75508-1A63-4B97-BC0F-C2E87BC9C26C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
