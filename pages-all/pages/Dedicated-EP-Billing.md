# About Autonomous AI Database Dedicated Elastic Pool Billing
- Source: https://docs.oracle.com/iaas/autonomous-database-serverless/doc/Dedicated-EP-Billing.html
- Fetched: 2026-09-05 18:57 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/Dedicated-EP-Billing.html#dcoc-content-body)

# About Autonomous AI Database Dedicated Elastic Pool Billing

Dedicated elastic pools are billed hourly for both allocated storage and compute (ECPUs).

Billing dedicated elastic pools is for the entire storage allocation, regardless of usage. Storage billing uses the ATP storage SKU and compute billing uses the ATP compute SKU regardless of whether the pool leader uses the Transaction Processing, Lakehouse, JSON, or APEX workload type. Pool members continue to have their own storage allocation, but they are not billed for storage individually, unlike traditional elastic pools.

For example, in a dedicated elastic pool with 256 TB and 256 ECPUs, the pool leader will be billed for both storage and compute on an hourly basis. Storage is billed per hour, including partial hours. Consider an example in which a dedicated elastic pool is created at 1:30 pm with 256 TB and 256 ECPUs, and terminated at 4:30 pm. In addition to the compute billing discussed earlier, the pool leader will also be billed for the storage every hour (1 to 2 pm, 2 to 3 pm, and 3 to 4 pm). There is no change in compute billing, whether it’s a dedicated elastic pool or a traditional elastic pool.

Note  
  
Note: Dedicated elastic pool’s compute resources (ECPU usage) are billed exactly the same way as any other elastic pool is billed for its compute (ECPU) usage. See[Autonomous AI Database Elastic Pool Billing](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/elastic-pools-about-billing.html#GUID-74D9A89B-8DE5-4FA3-80D8-FD802315C70A)for details and examples.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
