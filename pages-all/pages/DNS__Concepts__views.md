# Private Views
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/views.htm
- Fetched: 2026-09-05 01:58 CDT

# Private Views

Use private views to logically group a set of private domain name service (DNS) zones. A zone can only belong to a single view.

When you create a VCN, the VCN-dedicated resolver has a protected default view. You can add zones to the default view within restrictions on zone names to avoid collisions with protected zones. You can create and attach a view to a resolver in addition to the default view, so that their zones are resolvable in the VCN. If a resolver is deleted, and its default view contains unprotected zones, then the default view is converted to an unprotected view instead of being deleted.

The same zone name can be used in many views, but zone names within a view must be unique. Views aren't used with public zones.
Note  
  
Protected private zones are managed by other OCI services, so you can't delete them directly. For example, if a protected zone was created because a subnet was created, then deleting the subnet would delete the zone.

See[Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/privatedns.htm)for a feature overview and more information.

## Private View Tasks

You can perform the following tasks with views:
- [Creating a Private View](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/view-create.htm)
- [Creating a Private DNS Zone in a Private View](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/view-add-zone.htm)
- [Listing Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/view-list.htm)
- [Getting a Private View's Details](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/view-get.htm)
- [Editing a Private View](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/view-edit.htm)
- [Moving a Private View Between Compartments](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/view-move-compartment.htm)
- [Deleting a Private View](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/../Tasks/view-delete.htm)
