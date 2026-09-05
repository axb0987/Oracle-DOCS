# Working with Envoy Gateway to implement Kubernetes Gateway API
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenvoygatewayforgatewayapi.htm
- Fetched: 2026-09-05 01:57 CDT

# Working with Envoy Gateway to implement Kubernetes Gateway API

Find out how to set up Envoy Gateway to support the Kubernetes Gateway API in clusters you create using Kubernetes Engine (OKE).

The Kubernetes Gateway API (Gateway API) is the next generation standard for managing ingress and network traffic in Kubernetes clusters, succeeding the Ingress API. For more information about the Gateway API, see[Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/)in the Kubernetes documentation, and the[Gateway API documentation](https://gateway-api.sigs.k8s.io).

Envoy Gateway is an open-source implementation of the Gateway API that manages Envoy Proxy as the data plane. It provides a standard, compliant way to manage ingress traffic without relying on vendor-specific CRDs.

By deploying Envoy Gateway, you can use it as the underlying controller to manage`Gateway`,`HTTPRoute`, and other Gateway API resources.

The Envoy Gateway deployment includes several components that work together:
- Gateway API CRDs extend the Kubernetes API with new resource types such as`Gateway`and`HTTPRoute`, allowing declarative management of ingress traffic.
- Envoy Gateway controller acts as the control plane, watching for Gateway API resources and translating them into detailed configuration for the data plane.
- Envoy Proxy pods form the data plane, handling network traffic in accordance with the policies and routes defined by Gateway resources.
- OCI Network Load Balancer integration ensures that external traffic is properly routed to applications via Envoy Proxy nodes.

## Prerequisites

Before setting up Envoy Gateway to support the Kubernetes Gateway API:
- You must have`kubectl`access to the cluster created by Kubernetes Engine.
- The machine from which you access the cluster must have Helm CLI (v3.0 or later) installed.
- You must have cluster-admin privileges to install custom resource definitions (CRDs) and controllers.

## Setting Up Envoy Gateway as a Gateway API Controller

### High level steps to set up Envoy Gateway

At a high-level, the steps to set up Envoy Gateway to serve as the Gateway API controller are as follows:
- [Step 1: Install Gateway API CRDs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenvoygatewayforgatewayapi.htm#envoygateway-settingup__envoygatewaystepinstallgatewaycrds)
- [Step 2: Install Envoy Gateway](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenvoygatewayforgatewayapi.htm#envoygateway-settingup__envoygatewaystepinstall)
- [Step 3: Configure OCI Network Load Balancer integration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenvoygatewayforgatewayapi.htm#envoygateway-settingup__envoygatewaystepconfigureocinlb)
- [Step 4: Create a GatewayClass](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenvoygatewayforgatewayapi.htm#envoygateway-settingup__envoygatewaystepcreategatewayclass)
- [Step 5: Create a Gateway](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenvoygatewayforgatewayapi.htm#envoygateway-settingup__envoygatewaystepcreategateway)
- [Step 6: Deploy a sample application](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenvoygatewayforgatewayapi.htm#envoygateway-settingup__envoygatewaystepdeploysampleapplication)
- [Step 7: Create an HTTPRoute](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenvoygatewayforgatewayapi.htm#envoygateway-settingup__envoygatewaystepcreatehttproute)
- [Step 8: Verify connectivity](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenvoygatewayforgatewayapi.htm#envoygateway-settingup__envoygatewaystepverifyconnectivity)

### Step 1: Install Gateway API CRDs

The Gateway API Custom Resource Definitions (CRDs) are not installed by default in clusters you create using Kubernetes Engine. Before using Envoy Gateway as a Gateway API controller, you must install the CRDs.
- 

Install the standard channel CRDs (v1.2.0) by entering:
```

```

- 

Verify that the CRD is installed by entering:
```

```

- Confirm that the CRD is listed in the output.

### Step 2: Install Envoy Gateway

Use Helm to install the Envoy Gateway controller.
- 

Install the chart into the`envoy-gateway-system`namespace by entering:
```

```

- 

Wait for the Envoy Gateway controller to be ready by entering:
```

```

### Step 3: Configure OCI Network Load Balancer integration

Create an`EnvoyProxy`custom resource to inject the necessary OCI annotations into the`Service`that Envoy Gateway creates.
- 

Create a file named`oci-envoy-proxy.yaml`with the following content:
```

```

- 

Create the`EnvoyProxy`custom resource by entering:
```

```

### Step 4: Create a GatewayClass

Create a`GatewayClass`that tells the controller to use the`EnvoyProxy`you created.
- 

Create a file named`oci-gateway-class.yaml`with the following content:
```

```

- 

Create the`GatewayClass`by entering:
```

```

### Step 5: Create a Gateway

Create the`Gateway`resource, which triggers the creation of the OCI network load balancer.
- 

Create a file named`my-gateway.yaml`with the following content:
```

```

- 

Create the`Gateway`by entering:
```

```

- 

Get the external IP address by entering:
```

```

It might take a few minutes for OCI to provision the load balancer.

Wait until the`PROGRAMMED`column contains`True`and an IP address appears in the`ADDRESS`column.

### Step 6: Deploy a sample application

Test the gateway by deploying a simple echo service.
- 

Create a file named`echo-app.yaml`with the following content:
```

```

- 

Create the sample application by entering:
```

```

### Step 7: Create an HTTPRoute

Create an`HTTPRoute`to direct traffic from the`Gateway`to the application.
- 

Create a file named`echo-route.yaml`with the following content:
```

```

- 

Create the`HTTPRoute`by entering:
```

```

### Step 8: Verify connectivity

Verify connectivity by sending a request to the external IP address of the`Gateway`.
- 

Retrieve the public IP address of the gateway and save it as an environment variable by entering:
```

```

- 

Use`curl`to send a request to the Gateway external IP address by entering:
```

```

- Confirm that you receive a`200 OK`response, along with a JSON body that shows details about the request (headers, host, and so on).

### (Optional) Clean up

You can optionally remove the resources that you have created in this topic by entering:
```

```

```

```

```

```

```

```

```

```

```

```

If you no longer need the Gateway API on this cluster, you can remove the CRDs by entering:
```

```
