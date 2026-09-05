# Security Zone Integration
- Source: https://docs.oracle.com/en-us/iaas/Content/Database/Concepts/security_zones_topic-database_service_integration_overview.htm
- Fetched: 2026-09-05 01:58 CDT

# Security Zone Integration

The Database service supports OCI security zones.

A security zone is associated with one or more[compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/concepts-account.htm#conceptcompartment)in your tenancy, and created with a set of security policies called a security recipe. While you can create custom security recipes for particular use cases, OCI offers an Oracle-managed Maximum Security Recipe which provides the highest level of protection for your Database resources. The policies of a particular security recipe are enforced on any resource that is provisioned or moved into a security zone that uses the recipe. Thus, the only way to apply security zone policies is to control the compartment assignments of your Oracle Cloud Infrastructure resources.

For a complete overview of security zones, including instructions for creating security zones and security recipes, see the[Security Zones](https://docs.oracle.com/iaas/Content/security-zone/home.htm)section of the Oracle Cloud Infrastructure user guide.

## Restrictions on Database Service Resources Located in Maximum Security Recipe Compartments

The Maximum Security Recipe includes all available[security zone policies](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm). For example, restrictions placed on databases in a security zone that uses the Maximum Security Recipe include:
- The database cannot allow public network access
- The database must have automatic backups enabled
- The database cannot have Data Guard associations that aren't in compartments within the same security zone

For a complete list of the Database restrictions implemented by the Maximum Security Recipe, see[Security Zone Policies](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm).

Your can also create custom recipes that do not include all possible security restrictions for Database service resources, and assign a custom recipe to a security zone. See[Managing Recipes](https://docs.oracle.com/iaas/Content/security-zone/using/managing-recipes.htm).

## Supported Database Service Resources

The following Database service resources can be provisioned and managed in security zones that use the Maximum Security Recipe:
- Autonomous AI Database
- Bare metal and virtual machine DB systems
- Exadata Cloud DB systems
