# Known Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/known_issues_WAF.htm
- Fetched: 2026-09-05 03:12 CDT

# Known Issues

These known issues have been identified in Web Application Firewall.

## Unable to add default origin to WAF policy created with the API

Details: When creating a WAF policy using the API, if you do not specify a default origin, you cannot add the default origin later using the Console or API. This issue does not apply to policies created using the Console.
Workaround : Delete the policy that was created without a default origin and create a new policy with the default origin specified.

## TLS versions TLS_V1 and TLS_V1_1 have been deprecated

Details: TLS versions TLS_V1 and TLS_V1_1 have been deprecated and cannot be used in policy configurations. If you use these versions, a validation might occur.
Workaround: To work around this issue, update your policy configuration to use versions TLS_V1_2 or TLS_V1_3, or both.

## Global DNS change will cause service disruption if new subnets are not whitelisted

Details: Global DNS changes will be made for all Oracle Web Application Firewall (WAF) customers beginning in December 2019. All customers that have an origin lock-down (using an explicit IP whitelisting) and will not whitelist the new subnets will have downtime and service degradation.
Workaround:

( Action Required ) Customers must whitelist the new subnets to avoid service disruption. For the API documentation, see[ListEdgeSubnets](https://docs.oracle.com/iaas/api/#/en/waas/latest/EdgeSubnet/ListEdgeSubnets).

OCI WAF Expansion Whitelist

130.35.0.0/20

130.35.128.0/20

130.35.240.0/20

138.1.32.0/21

138.1.128.0/19

147.154.96.0/19

192.29.96.0/20

130.35.16.0/20

130.35.48.0/20

130.35.64.0/19

130.35.96.0/20

130.35.120.0/21

130.35.144.0/20

130.35.176.0/20

130.35.192.0/19

130.35.224.0/22

130.35.232.0/21

138.1.48.0/21

147.154.0.0/18

147.154.64.0/20

147.154.80.0/21

130.35.112.0/22

138.1.16.0/20

138.1.80.0/20

138.1.208.0/20

138.1.224.0/19

147.154.224.0/19

138.1.0.0/20

138.1.40.0/21

138.1.64.0/20

138.1.96.0/21

138.1.104.0/22

138.1.160.0/19

138.1.192.0/20

147.154.128.0/18

147.154.192.0/20

147.154.208.0/21

192.29.0.0/20

192.29.64.0/20

192.29.128.0/21

192.29.144.0/21

192.29.16.0/21

192.29.32.0/21

192.29.48.0/21
