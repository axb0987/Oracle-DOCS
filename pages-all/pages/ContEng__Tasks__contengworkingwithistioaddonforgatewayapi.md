# Working with Istio as a Cluster Add-on to implement Kubernetes Gateway API
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithistioaddonforgatewayapi.htm
- Fetched: 2026-09-05 01:57 CDT

# Working with Istio as a Cluster Add-on to implement Kubernetes Gateway API

Find out how to install, configure, and use the Istio cluster add-on to implement the Kubernetes Gateway API in clusters you've created using Kubernetes Engine (OKE).

The Kubernetes Gateway API (Gateway API) is the next generation standard for managing ingress and network traffic in Kubernetes clusters, succeeding the Ingress API. For more information about the Gateway API, see[Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/)in the Kubernetes documentation, and the[Gateway API documentation](https://gateway-api.sigs.k8s.io).

The Istio cluster add-on is an Oracle-managed extension for Kubernetes Engine that deploys and manages the Istio control plane in a cluster. It enables advanced service mesh and Gateway API support for ingress and traffic management.

By enabling the Istio cluster add-on, you can use Istio as the underlying controller to manage`Gateway`,`HTTPRoute`, and other Gateway API resources.

Using Istio as a cluster add-on (the Istio cluster add-on) simplifies the lifecycle management of the control plane (`istiod`). You can more simply:
- Enable or disable the Istio control plane.
- Opt into, and out of, automatic version updates by Oracle.
- Manage add-on specific customizations using approved key/value pair configuration arguments.

These sections describe how to work with the Istio cluster add-on to configure Gateway API networking:
- [Setting Up the Istio Cluster Add-on as a Gateway API Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithistioaddonforgatewayapi.htm#istioaddon-settingup)
- [Disabling (and removing) the Istio cluster add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithistioaddonforgatewayapi.htm#istioaddon-disabling)

## Prerequisites

Before setting up the Istio cluster add-on to support the Kubernetes Gateway API:
- You must have`kubectl`access to the cluster created by Kubernetes Engine.
- You must have cluster-admin privileges to install custom resource definitions (CRDs) and controllers.

## Setting Up the Istio Cluster Add-on as a Gateway API Controller

### High level steps to set up the Istio cluster add-on as a Gateway API controller

At a high-level, the steps to set up the Istio cluster add-on to serve as the Gateway API controller are as follows:
- [Step 1: Install Gateway API CRDs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithistioaddonforgatewayapi.htm#istioaddon-settingup__istioaddonstepinstallgatewaycrds)
- [Step 2: Create the Istio cluster add-on configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithistioaddonforgatewayapi.htm#istioaddon-settingup__istioaddonstepconfigfile)
- [Step 3: Deploy the Istio cluster add-on on the cluster and confirm successful deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithistioaddonforgatewayapi.htm#istioaddon-settingup__istioaddonstepdeploy)
- [Step 4: Create a Gateway](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithistioaddonforgatewayapi.htm#istioaddon-settingup__istioaddonstepcreategateway)
- [Step 5: Deploy a sample application](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithistioaddonforgatewayapi.htm#istioaddon-settingup__istioaddonstepdeploysampleapplication)
- [Step 6: Create an HTTPRoute](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithistioaddonforgatewayapi.htm#istioaddon-settingup__istioaddonstepcreatehttproute)
- [Step 7: Verify connectivity](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithistioaddonforgatewayapi.htm#istioaddon-settingup__istioaddonstepverifyconnectivity)

### Step 1: Install Gateway API CRDs

The Gateway API Custom Resource Definitions (CRDs) are not installed by default in clusters you create using Kubernetes Engine. Before using Istio as a Gateway API controller, you must install the CRDs.
- 

Install the standard Gateway API CRDs (v1.2.0) by entering:
```

```

- 

Verify that the CRD is installed by entering:
```

```

- Confirm that the CRD is listed in the output.
- Confirm that the Kubernetes Gateway API release is compatible with the Istio add-on version supported by Kubernetes Engine for the version of Kubernetes running on the cluster (see[Comparisons - v1.2](https://gateway-api.sigs.k8s.io/implementations/v1.2/)in the Gateway API documentation, and[Cluster Add-on Supported Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-supportedversions.htm)).

### Step 2: Create the Istio cluster add-on configuration file

Create an Istio cluster add-on configuration file for use with the OCI CLI.
- 

Create a JSON file (for example,`enableistio.json`).
- 

Add the following content to enable the add-on.

Note: Unlike the standard Service Mesh use case, you do not strictly need to set the legacy`enableIngressGateway`because the Gateway API can dynamically provision gateway infrastructure. However, setting it provides a default fallback.
```

```

Note the following points:
- If you set`value`to`"true"`, the Istio cluster add-on provisions the classic`istio-ingressgateway`deployment and service alongside the control plane.
- If you set`value`to`"false"`, only the control plane (`istiod`) is installed. You can then create`Gateway`resources that Istio will automatically provision as needed.
- 

Save and close the file.

### Step 3: Deploy the Istio cluster add-on on the cluster and confirm successful deployment

Deploy the Istio cluster add-on.
- 

Deploy the add-on using the OCI CLI by entering:
```

```

- 

Verify successful deployment:
- 

Enter:
```

```

- 

Confirm that the lifecycle state of the Istio cluster add-on is`ACTIVE`.
- 

Verify that the Istio control plane is running:
- 

Enter:
```

```

- 

Confirm that the`istiod`pod is in the`Running`state.

### Step 4: Create a Gateway

Create the`Gateway`resource.
- Create a new namespace (for example, test-gateway) by entering:
```

```

- 

Create a file named`gateway.yaml`with the following content.
```

```

Note the`gatewayClassName: istio`line, which tells the Istio cluster add-on to manage this gateway.
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

### Step 5: Deploy a sample application

Deploy a sample application into the new namespace.
- 

Deploy a sample application (for example, httpbin) by entering:
```

```

### Step 6: Create an HTTPRoute

Create an`HTTPRoute`to direct traffic from the`Gateway`to the httpbin service.
- 

Create a file named`route.yaml`with the following content:
```

```

- 

Create the`HTTPRoute`by entering:
```

```

### Step 7: Verify connectivity

Verify connectivity by sending a request to the external IP address of the`Gateway`.
- 

Retrieve the public IP address of the gateway and save it as an environment variable by entering:
```

```

- 

Use`curl`to send a request to the Gateway external IP address by entering:
```

```

```

```

- 

Confirm that you receive a`200 OK`response from the httpbin application.

## Disabling (and removing) the Istio cluster add-on

These instructions describe how to disable and remove the Istio cluster add-on.
- 

Disable and remove the add-on using the OCI CLI by entering:
```

```

- 

(Optional) Remove Gateway API resources.

The add-on removal process does not automatically delete the`Gateway`or`HTTPRoute`resources you created. Manually remove them to clean up the associated load balancers by entering:
```

```

```

```

- 

(Optional) Remove Gateway API CRDs.

If you no longer need the Gateway API on this cluster, you can remove the CRDs by entering:
```

```
