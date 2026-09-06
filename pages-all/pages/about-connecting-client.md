# About Connecting to Autonomous AI Database Using a Client Application
- Source: https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-connecting-client.html
- Fetched: 2026-09-05 18:57 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/about-connecting-client.html#dcoc-content-body)

# About Connecting to Autonomous AI Database Using a Client Application

Applications can connect to Autonomous AI Database using any of the connection types supported by Oracle Net Services.

Consult your application documentation for details about how your application connects to Oracle.

The following steps describe the process of connecting to Autonomous AI Database using a client application:
- 

Determine what connection type your application uses, (for example OCI, ODBC, JDBC Thin, and so on).
- 

The steps required to prepare the client computer depend on the type of connection the client application uses. Determine what authentication type your application uses, either mTLS or TLS and prepare your client computer:
- 

Mutual TLS authentication connections : In all cases, with mTLS connections, client credentials in the form of a wallet file must be downloaded to the client.
- 

TLS authentication connections : For connections with JDBC Thin Driver using JDK8u162 or higher, including connections with Oracle SQL Developer and Oracle SQLcl, a wallet is not required.

Oracle Call Interface (OCI) clients support TLS authentication without a wallet if you are using the following client versions:
- 

Oracle Instant Client/Oracle Database Client 19.13 - only on Linux x64
- 

Oracle Instant Client/Oracle Database Client 19.14 (or later), 21.5 (or later), or 23.1 (or later)

See the details for each driver type for information on the steps required to prepare your application to connect to Autonomous AI Database.
- 

Within your application, set up the connection.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
