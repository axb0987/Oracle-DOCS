# Solutions for Self-Managed Kubernetes on OCI
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/solutions-kubernetes.htm
- Fetched: 2026-09-05 01:36 CDT

# Solutions for Self-Managed Kubernetes on OCI

This section describes the solutions that you can use to create and operate self-managed Kubernetes platforms on Oracle Cloud Infrastructure (OCI).

OCI provides Oracle Kubernetes Engine (OKE), a fully managed Kubernetes service for deploying and managing containerized applications. If you need greater control over or customization of your Kubernetes platform, such as custom Kubernetes tooling or governance, OCI also provides solutions that use open source technologies and native OCI features to help you provision and manage self-managed Kubernetes platforms.

## Cluster API Provider for OCI

Use declarative, Kubernetes-style APIs to create, configure, and manage upstream Kubernetes clusters.
- Documentation:[Cluster API Provider](https://docs.oracle.com/iaas/Content/API/SDKDocs/cluster-api-provider.htm)
- Download:[GitHub](https://github.com/oracle/cluster-api-provider-oci)

## OCI Cloud Controller Manager

Manage Kubernetes nodes and Oracle Cloud Infrastructure resources by using the Oracle Cloud Infrastructure implementation of Kubernetes Cloud Controller Manager. The controller manages nodes and supports LoadBalancer, Container Storage Interface (CSI), FlexVolume, and node IP address management (IPAM).
- Documentation:[Cloud Controller Manager](https://github.com/oracle/oci-cloud-controller-manager/blob/master/README.md)
- Download:[GitHub](https://github.com/oracle/oci-cloud-controller-manager)

## OCI Native Ingress Controller

Use an ingress controller that integrates Kubernetes services with Oracle Cloud Infrastructure Load Balancer.
- Documentation:[Native Ingress Controller](https://github.com/oracle/oci-native-ingress-controller/blob/main/GettingStarted.md)
- Download:[GitHub](https://github.com/oracle/oci-native-ingress-controller)

## Workload Identity

Use the JSON Web Token (JWT)-to-Resource Principal Session Token (RPST) exchange feature in Oracle Cloud Infrastructure Identity and Access Management (IAM) to provide workload-specific access to OCI services from self-managed Kubernetes clusters.
- Documentation:[Workload Identity](https://www.ateam-oracle.com/oci-workload-identity-federation-using-ephemeral-rpst)

## Crossplane Provider for OCI

Use the open source Crossplane provider to create and manage Oracle Cloud Infrastructure resources and application control planes by using declarative, Kubernetes-style APIs.
- Documentation:[Crossplane Provider](https://docs.oracle.com/iaas/Content/API/SDKDocs/crossplane-provider.htm)
- Download:[GitHub](https://github.com/oracle/crossplane-provider-oci)

## Oracle Service Operator for Kubernetes

Use the Oracle implementation of the open source Operator Framework to create, configure, and manage Oracle Cloud Infrastructure resources by using declarative, Kubernetes-style APIs.
- Documentation:[Oracle Service Operator for Kubernetes](https://docs.oracle.com/iaas/Content/API/SDKDocs/operator-kubernetes.htm)
- Download:[GitHub](https://github.com/oracle/oci-service-operator)
