# Details for Database Tools
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_database_tools.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Database Tools

Logging details for Database Tools.

For more information, see[Logging for Database Tools](https://docs.oracle.com/iaas/database-tools/doc/logging.html).

## Resources
- Database Tools MCP Server

## Log Categories

API value (ID): Console (Display Name) Description
invoke MCP Invocation Logs Logs Database Tools MCP server invocation events, including MCP request metadata, runtime identity context, and customer-visible permission failures.

## Policies

`DATABASE_TOOLS_MCP_SERVER_UPDATE`permission is required, along with[Logging](https://docs.oracle.com/iaas/Content/Identity/policyreference/loggingpolicyreference.htm)policies, to enable or disable service logs for a Database Tools MCP server.

## Availability

Database Tools logging is available in regions where Database Tools MCP servers and OCI Logging service logs are supported.

## Comments

Database Tools emits service logs for MCP invocation flows when service logging is enabled on the MCP server. Automated processors must tolerate logs with unrecognized fields or values.

## Contents of a Database Tools Log Entry

Property Description Example
message Human-readable message for the log event. Present when Database Tools has a customer-visible message to report.`Authorize permissions failed for request. Missing permissions: DATABASE_TOOLS_CONNECTION_READ`
level Log level for the event.`INFO`
mcpServerId OCID of the Database Tools MCP server that emitted the log.`ocid1.databasetoolsmcpserver.oc1.phx.<unique_ID>`
connectionId OCID of the Database Tools connection associated with the MCP server or invocation, when available.`ocid1.databasetoolsconnection.oc1.phx.<unique_ID>`
connectionRuntimeIdentityType Runtime identity type configured on the Database Tools connection, when available.`RESOURCE_PRINCIPAL`
mcpRuntimeIdentityType Runtime identity type configured on the MCP server, when available.`AUTHENTICATED_PRINCIPAL`
opcRequestId Request ID for correlating the MCP invocation with other OCI service activity.`<opc-request-id>`
jsonRpcMethod JSON-RPC method invoked by the MCP client.`tools/call`
jsonRpcRequestId JSON-RPC request ID supplied by the MCP client, when present.`request-1`
jsonRpcErrorCode JSON-RPC error code, present for logged permission failures.`-32001`
toolName MCP tool name, present for`tools/call`requests when the request includes a tool name.`dbtools_execute_sql`
mcpProtocolVersion MCP protocol version used for the request, when available.`2025-06-18`
requestPrincipalId OCID of the principal that made the request, when available.`ocid1.user.oc1..<unique_ID>`
requestPrincipalTenantId OCID of the requesting principal's tenancy, when available.`ocid1.tenancy.oc1..<unique_ID>`
requestPrincipalDomainId OCID of the requesting principal's identity domain, when available.`ocid1.domain.oc1..<unique_ID>`
requestPrincipalType Type of the requesting principal, when available.`user`
requestPrincipalSubType Subtype of the requesting principal, when available.`native`
requestPrincipalResourceType Resource type for the requesting principal, when available.`instance`
runtimePrincipalId Principal used by Database Tools at runtime. For MCP servers configured with resource principal runtime identity, this is the MCP server OCID.`ocid1.databasetoolsmcpserver.oc1.phx.<unique_ID>`

## Example Database Tools MCP Invocation Log
```

```

## Query Database Tools Logs
- 

Find logs related to MCP server OCID:
```

```

- 

Find all MCP logs:
```

```

- 

Find logs related to`opc-request-id`:
```

```
