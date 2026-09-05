# Securing Data Catalog
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/datacatalog_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Data Catalog

Oracle Cloud Infrastructure Data Catalog provides a collaborative data discovery and governance solution in accordance with industry-leading security best practices.

## Security Recommendations

- Assign least privilege access for IAM users and groups to resource types in`data-catalog-family`.
- To minimize loss of data due to inadvertent deletes by an authorized user or malicious deletes, Oracle recommends to giving`CATALOG_DELETE`permission to a minimum possible set of IAM users and groups. Give`CATALOG_DELETE`permissions only to tenancy and compartment admins.
- To protect your data sources from any security vulnerability, provide credentials to read-only accounts only. Data Catalog only needs read access to harvest data assets.

## Security Policy Examples

### Prevent Delete of Data Catalogs

Create this policy to allow group`DataCatalogUsers`to perform all actions on data catalogs, except deleting them.

```

```

### Let Users Read all Data Catalog Instances

Create this policy to allow group`DataCatalogUsers`to read all data catalog instances in the tenancy or a specific compartment.
```

```

```

```

### Let Users Access Data Assets in Data Catalogs
Create this policy to allow group`DataCatalogUsers`to read or use data assets in the tenancy or a compartment. For example, the policies allow the group to read data assets is as follows:
```

```

```

```

### Let Users Access Specific Data Assets in Data Catalogs

Create this policy to allow group`DataCatalogUsers`to read or use specific data assets in the tenancy or a compartment. For example, the policy allow the group to read specific data assets is as follows:
```

```

### Let Users Access Glossaries in Data Catalogs

Create this policy to allow group`DataCatalogUsers`to read or use glossaries in the tenancy or a compartment. For example, the policies allow the group to read glossaries is as follows:
```

```

```

```

For more information on creating policies, see[Data Catalog Policies](https://docs.oracle.com/iaas/Content/data-catalog/using/policies.htm)
