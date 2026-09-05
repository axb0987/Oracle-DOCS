# Managing Kubernetes Gateway API Controllers
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmanaggatewaycontrollers.htm
- Fetched: 2026-09-05 01:55 CDT

# Managing Kubernetes Gateway API Controllers

Find out about Kubernetes Gateway API controllers you can set up in clusters you create using Kubernetes Engine (OKE).

The Kubernetes Gateway API (Gateway API) is the next generation standard for managing ingress and network traffic in Kubernetes clusters, succeeding the Ingress API.

A Gateway API controller implements the rules and configuration options defined in Gateway API resources (such as`Gateway`and`HTTPRoute`).

For more information about the Gateway API, see[Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/)in the Kubernetes documentation, and the[Gateway API documentation](https://gateway-api.sigs.k8s.io).

When you create clusters using Kubernetes Engine, you can set up Gateway API controllers to provide scalable, flexible, and cloud-native traffic management for workloads. For example, you can set up the following Gateway API controllers:
- 

Envoy Gateway (open source)

Envoy Gateway is an open-source implementation of the Gateway API that manages Envoy Proxy as the data plane. It provides a standard, compliant way to manage ingress traffic without relying on vendor-specific CRDs. See[Working with Envoy Gateway to implement Kubernetes Gateway API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenvoygatewayforgatewayapi.htm).
- 

Istio as a cluster add-on

By enabling the Istio add-on, you can use Istio as the underlying controller to manage`Gateway`,`HTTPRoute`, and other Gateway API resources. The add-on simplifies lifecycle management and enables Oracle-managed upgrades. See[Working with Istio as a Cluster Add-on to implement Kubernetes Gateway API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithistioaddonforgatewayapi.htm)
