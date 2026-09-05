# Cluster API Provider for OCI
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cluster-api-provider.htm
- Fetched: 2026-09-05 01:36 CDT

# Cluster API Provider for OCI

The Cluster API Provider for Oracle Cloud Infrastructure (OCI) implements the Cluster API specification for OCI so you can use declarative, Kubernetes-style APIs to create, configure, and manage Oracle Kubernetes Engine and self-managed Kubernetes clusters.

[Cluster API](https://cluster-api.sigs.k8s.io/)is a Kubernetes subproject focused on providing declarative APIs and tooling to simplify provisioning, upgrading, and operating several Kubernetes clusters. It uses Kubernetes-style APIs and patterns to automate cluster lifecycle management for platform operators.

The supporting infrastructure, such as virtual machines, networks, load balancers, and VPCs, and the Kubernetes cluster configuration, is defined in the same way that application developers deploy and manage workloads. This approach supports consistent, repeatable cluster deployments across a wide range of infrastructure environments.

The Kubernetes Cluster API Provider for OCI brings declarative, Kubernetes-style APIs to Kubernetes cluster creation, configuration, and management on OCI. It covers Oracle Kubernetes Engine and self-managed Kubernetes clusters. The source is available on[GitHub](https://github.com/oracle/cluster-api-provider-oci).
Caution  
  
Use the Kubernetes Cluster API Provider for OCI in a test or non-production OCI and Kubernetes environment first. Don't make a production cluster the first deployment target. Validate authentication, IAM policy scope, create and delete behavior, finalizers, and service-specific limits in an isolated test environment before promoting any package bundle to production.

See[Getting Started](https://github.com/oracle/cluster-api-provider-oci%23getting-started)for more information.

## Licensing

This provider and samples are licensed under the Apache License Version 2.0.

## Availability

The Kubernetes Cluster API Provider for OCI is region agnostic. You can use it in all OCI regions where the required services it manages are available.

See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for the list of available regions, associated locations, region identifiers, region keys, and availability domains.

## Contributions

The Kubernetes Cluster API Provider for OCI is open source and accepts pull requests on[GitHub](https://github.com/oracle/cluster-api-provider-oci).

## Notifications

To be notified when a new version of the Kubernetes Cluster API Provider for OCI is released, subscribe to the[Atom feed](https://github.com/oracle/cluster-api-provider-oci/releases.atom).

## Questions or Feedback

See the detailed documentation in the[Cluster API Provider for OCI Book](https://oracle.github.io/cluster-api-provider-oci/). You can also use[GitHub](https://github.com/oracle/cluster-api-provider-oci/issues)
