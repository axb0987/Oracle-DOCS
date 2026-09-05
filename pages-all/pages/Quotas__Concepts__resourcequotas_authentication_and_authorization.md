# Authentication and Authorization
- Source: https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_authentication_and_authorization.htm
- Fetched: 2026-09-05 02:52 CDT

# Authentication and Authorization

Authenticate and authorize users for the Compartment Quotas service.

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

For common policies used to authorize users, see[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). To manage quotas in a compartment, you must belong to a group that has the correct permissions. For example:

```

```

For in-depth information on granting users permissions for the Compartment Quotas service, see[Details for the Quotas Service](https://docs.oracle.com/iaas/Content/Identity/Reference/quotaspolicyreference.htm)
