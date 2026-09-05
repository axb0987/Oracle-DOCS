# OCI Service Operator for Kubernetes
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/operator-kubernetes.htm
- Fetched: 2026-09-05 01:36 CDT

# OCI Service Operator for Kubernetes

The OCI Service Operator for Kubernetes lets Kubernetes users create, manage, and connect to Oracle Cloud Infrastructure (OCI) resources through the Kubernetes API.

Kubernetes users can install the operator and manage OCI resources through the Kubernetes API instead of relying on the OCI CLI or other OCI developer tools to interact with a service API.

This is based on the[Operator Framework](https://operatorframework.io/), an open source toolkit for managing Operators. It uses the[controller-runtime](https://github.com/kubernetes-sigs/controller-runtime)library, which provides high-level APIs and abstractions for writing operational logic, along with tools for scaffolding and code generation for Operators.
Caution  
  
Use the OCI Service Operator for Kubernetes in a test or non-production OCI and Kubernetes environment first. Don't make a production cluster the first deployment target. Validate authentication, IAM policy scope, create and delete behavior, finalizers, and service-specific limits in an isolated test environment before promoting any package bundle to production.

The OCI Service Operator for Kubernetes is available on[GitHub](https://github.com/oracle/oci-service-operator).

To get started with this provider for managing OCI resources, see[Getting Started](https://github.com/oracle/oci-service-operator%23start-here).

## Licensing

This provider and samples are licensed under the Apache License Version 2.0.

## Availability

The OCI Service Operator for Kubernetes is region agnostic. You can use it with[supported services](https://github.com/oracle/oci-service-operator/blob/main/docs/reference/index.md)in any OCI regions where those services are available.

See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for the list of available regions, associated locations, region identifiers, region keys, and availability domains.

## Contributions

Got a fix for a bug or a new feature to contribute? The OCI Service Operator for Kubernetes is open source and accepts pull requests on[GitHub](https://github.com/oracle/oci-service-operator).

## Notifications

To be notified when a new version of the OCI Service Operator for Kubernetes is released, subscribe to the[Atom feed](https://github.com/oracle/oci-service-operator/releases.atom).

## Questions or Feedback

See the[API reference](https://github.com/oracle/oci-service-operator/blob/main/docs/reference/api/index.md)documentation for more information. You can also use[GitHub](https://github.com/oracle/oci-service-operator/issues)
