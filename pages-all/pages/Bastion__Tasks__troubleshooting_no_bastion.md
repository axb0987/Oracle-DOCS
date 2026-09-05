# No Bastions or Sessions are Visible
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/troubleshooting_no_bastion.htm
- Fetched: 2026-09-05 01:42 CDT

# No Bastions or Sessions are Visible

Fix general problems that prevent you from viewing and managing resources in Bastion.

## Missing IAM Policy

To use Oracle Cloud Infrastructure, you must be granted security access in a policy by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which compartment to work in.
Example policy:

```

```
See[Bastion IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/../Reference/bastionpolicyreference.htm)for detailed policy information and more examples.

## Wrong Compartment is Specified

Within the Console, be sure to select the Compartment that contains the bastion or session that you want to view. Also be sure that an administrator has granted you access to bastions and sessions in this compartment.
