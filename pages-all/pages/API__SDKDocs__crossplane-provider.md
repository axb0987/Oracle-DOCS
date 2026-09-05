# Crossplane Provider for OCI
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/crossplane-provider.htm
- Fetched: 2026-09-05 01:36 CDT

# Crossplane Provider for OCI

Learn what the Crossplane Provider for Oracle Cloud Infrastructure (OCI) is, where to find it, and what to review before you use it across OCI regions.

[Crossplane](https://www.crossplane.io/)is a control plane framework for platform engineering that runs on Kubernetes. It lets platform teams define APIs and abstractions to manage cloud native software through Kubernetes custom resources without writing custom controllers for each resource.

The Crossplane Provider for OCI connects the Crossplane engine to the OCI services that you want to manage. The project is available on[GitHub](https://github.com/oracle/crossplane-provider-oci).
Caution  
  
Use the Crossplane Provider for OCI in a test or non-production OCI and Kubernetes environment first. Validate authentication, IAM policy scope, create and delete behavior, finalizers, and service-specific limits in an isolated environment before you promote any package bundle to production.

To start managing OCI resources with this provider, see[Getting Started](https://github.com/oracle/crossplane-provider-oci/blob/main/docs/quickstart.md).

## Licensing

This provider and its sample content are licensed under the Apache License Version 2.0.

## Availability

The Crossplane Provider for OCI is region agnostic. You can use it with[supported services](https://github.com/orgs/oracle/packages?repo_name=crossplane-provider-oci)in any OCI regions where those services are available. For the list of regions, region identifiers, region keys, locations, and availability domains, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Contributions

The Crossplane Provider for OCI is open source and accepts pull requests on[GitHub](https://github.com/oracle/crossplane-provider-oci).

## Notifications

To be notified when a new version is released, subscribe to the[Atom feed](https://github.com/oracle/crossplane-provider-oci/releases.atom).

## Questions or Feedback

For product documentation, see[Getting Started](https://github.com/oracle/crossplane-provider-oci/blob/main/docs/quickstart.md). To report bugs or request features, use[GitHub issues](https://github.com/oracle/crossplane-provider-oci/issues)
