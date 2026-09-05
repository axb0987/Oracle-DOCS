# Securing Data Integration
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/dataintegration_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Data Integration

Oracle Cloud Infrastructure Data Integration provides a collaborative data integration solution in accordance with industry-leading security best practices.

## Security Recommendations

- Assign least privilege access for IAM users and groups to resource types in dis-family.
- To minimize loss of data due to inadvertent deletes by an authorized user or malicious deletes, Oracle recommends to giving DIS_WORKSPACE_DELETE permission to a minimum possible set of IAM users and groups. Give DIS_WORKSPACE_DELETE permissions only to tenancy and compartment admins.
- To protect your data sources from any security vulnerability, provide credentials to read-only accounts only. Data Integration only needs read access to ingest data from data assets.

## Security Policy Examples

### Prevent Delete of Workspaces

Create this policy to allow group DISUsers to perform all actions on workspaces, except deleting them.

```

```

For more information on creating policies, see[Data Integration Policies](https://docs.oracle.com/iaas/Content/data-integration/using/policies.htm)
