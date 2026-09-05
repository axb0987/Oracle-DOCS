# Using Istio on Clusters Created with Kubernetes Engine (OKE)
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-using-istio.htm
- Fetched: 2026-09-05 01:53 CDT

# Using Istio on Clusters Created with Kubernetes Engine (OKE)

Find out about using Istio on clusters you've created with Kubernetes Engine (OKE).

Istio is an open-source, platform-independent service mesh that provides traffic management, policy enforcement, and telemetry collection. Istio is designed to manage communications between microservices and applications. Istio uses Envoy proxies, deployed as sidecars to the underlying services, to mediate all inbound and outbound traffic for all services in the service mesh. Without requiring changes to the underlying services, Istio provides automated baseline traffic resilience, service metrics collection, distributed tracing, traffic encryption, protocol upgrades, and advanced routing functionality for all service-to-service communication.

Istio uses ingress and egress gateways to configure load balancers executing at the edge of a service mesh. Istio ingress gateways are implemented using Kubernetes Gateway and VirtualService resources, and provide a consistent, high-performance traffic management layer across all the services in the service mesh. An ingress gateway is a single entry point into the service mesh through which all incoming HTTP and HTTPS request traffic flows. The ingress gateway routes traffic to the appropriate service based on the request. Similarly, an egress gateway defines exit points from the service mesh.

For more information about Istio, see the[Istio documentation](https://istio.io/latest/docs/).

You can deploy Istio on a Kubernetes cluster in two ways:
- as a standalone program (see[Working with Istio as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm))
- as a cluster add-on (see[Working with Istio as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm))

Note that service mesh products (such as Istio) are supported regardless of the CNI plugin you are using for pod networking (either the OCI VCN-Native Pod Networking CNI plugin or the flannel CNI plugin). Worker nodes must be running Kubernetes 1.26 (or later).
Note  
  

You can use Istio with managed node pools, but not with virtual node pools.

## Using the Kubernetes Gateway API

The[Gateway API](https://gateway-api.sigs.k8s.io)is an official Kubernetes project focused on providing API resources for layer 4 (L4) and layer 7 (L7) routing in Kubernetes. The Gateway API represents the next generation of Kubernetes ingress, load balancing, and service mesh APIs.

Kubernetes Engine supports installation of the Gateway API custom resource definitions (CRDs), providing you follow the instructions in the[Getting Started with Gateway API](https://gateway-api.sigs.k8s.io/guides/getting-started/)documentation. For example, to install the standard channel, use the following command:

```

```

After installing the Gateway API CRDs, you can use Istio either as a standalone program or as a cluster add-on to take advantage of Gateway API support. Along with support for[Kubernetes Ingress resources](https://istio.io/latest/docs/tasks/traffic-management/ingress/kubernetes-ingress/), Istio enables you to configure ingress traffic using Gateway API[Gateway resources](https://gateway-api.sigs.k8s.io/api-types/gateway). Gateways provide more extensive customization and flexibility than Ingress resources, allowing Istio features such as monitoring and route rules to be applied to traffic entering the cluster.

The Istio documentation describes how to use the Gateway API with Istio. When defining a Gateway with Istio as the implementation, it is important to set the`gatewayClassName`property to`istio`. For example:

```

```

For more information about configuring Gateways and using advanced Istio features with the Gateway API, see[Kubernetes Gateway API](https://istio.io/latest/docs/tasks/traffic-management/ingress/gateway-api/)in the Istio documentation, and the[Gateway API](https://gateway-api.sigs.k8s.io)
