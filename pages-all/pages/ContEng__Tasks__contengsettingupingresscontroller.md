# Example: Setting Up an Nginx Ingress Controller on a Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupingresscontroller.htm
- Fetched: 2026-09-05 01:56 CDT

# Example: Setting Up an Nginx Ingress Controller on a Cluster

Find out how to set up and use an example Nginx ingress controller on a cluster you've created using Kubernetes Engine (OKE).
Note  
  

In November 2025, the Kubernetes community announced that the NGINX Ingress Controller will stop receiving maintenance in March 2026. After that time, no further releases, bug fixes, or security updates will be provided. Existing deployments are expected to continue functioning, and current installation artifacts will remain available. However, we recommend that you plan a migration to an alternative ingress solution to maintain security posture and ongoing supportability.

The following options describe common approaches:
- Adopt a different Ingress controller. This option enables you to continue using the Kubernetes Ingress API and typically requires fewer changes to application manifests and operational processes.
- Set up a Gateway API controller. This option replaces the NGINX Ingress Controller and the use of the Ingress API with an implementation of the Kubernetes Gateway API. The Gateway API is a vendor-neutral, extensible standard for managing ingress traffic. Adopting the Gateway API involves specifying a Gateway (the entry point where traffic is received), the GatewayClass (the type(s) of supported load balancer implementations), and route resources (such as HTTPRoute). For example, you could implement the Gateway API using[Envoy Gateway](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenvoygatewayforgatewayapi.htm), or using[Istio as cluster add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithistioaddonforgatewayapi.htm).

For more information, see the following:
- [Third party ingress controllers](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/#third-party-ingress-controllers)in the Kubernetes documentation
- [Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/)in the Kubernetes documentation
- [Gateway API documentation](https://gateway-api.sigs.k8s.io), including:
- [Getting Started with Gateway API](https://gateway-api.sigs.k8s.io/guides/getting-started/)
- [Migrating from Ingress](https://gateway-api.sigs.k8s.io/guides/getting-started/migrating-from-ingress/)
- [Implementations](https://gateway-api.sigs.k8s.io/implementations/)

You can set up different open source ingress controllers on clusters you have created with Kubernetes Engine to manage Kubernetes application traffic.

This topic explains how to set up an example Nginx ingress controller along with corresponding access control on an existing cluster. Having set up the ingress controller, this topic describes how to use the ingress controller with an example hello-world backend, and how to verify the ingress controller is working as expected. If you want to continue using the example ingress controller, follow the upgrade instructions. And when you have no further use for the example ingress controller, this topic shows you how to delete it.

## Example Components

The example includes an ingress controller and a hello-world backend.

### Ingress Controller Components

The ingress controller comprises:
- An ingress controller deployment called`ingress-nginx-controller`. The deployment deploys an image that contains the binary for the ingress controller and Nginx. The binary manipulates and reloads the`/etc/nginx/nginx.conf`configuration file when an ingress is created in Kubernetes. Nginx upstreams point to services that match specified selectors.
- An ingress controller service called`ingress-nginx-controller`. The service exposes the ingress controller deployment as a service of type LoadBalancer. Because Kubernetes Engine uses an Oracle Cloud Infrastructure integration/cloud-provider, a load balancer will be dynamically created with the correct nodes configured as a backend set.

### Backend Components

The hello-world backend comprises:
- A backend deployment called`docker-hello-world`. The deployment handles default routes for health checks and 404 responses. This is done by using a stock hello-world image that serves the minimum required routes for a default backend.
- A backend service called`docker-hello-world-svc`.The service exposes the backend deployment for consumption by the ingress controller deployment.

## Setting Up the Example Ingress Controller

In this section, you create the access rules for ingress. You then create the example ingress controller components, and confirm they are running.

### Creating the Access Rules for the Ingress Controller
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- If your Oracle Cloud Infrastructure user is a tenancy administrator, skip the next step and go straight to[Deploying the Ingress Controller and associated resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupingresscontroller.htm#settingupcontroller__creatingserviceaccount).
- 

If your Oracle Cloud Infrastructure user is not a tenancy administrator, in a terminal window, grant the user the Kubernetes RBAC cluster-admin clusterrole on the cluster by entering:

```

```

where:
- `<my-cluster-admin-binding>`is a string of your choice to be used as the name for the binding between the user and the Kubernetes RBAC cluster-admin clusterrole. For example,`jdoe_clst_adm`
- `<user-OCID>`is the user's OCID (obtained from the Console ). For example,`ocid1.user.oc1..aaaaa...zutq`(abbreviated for readability).

For example:

```

```

### Deploying the Ingress Controller and associated resources

How to deploy the ingress controller and associated resources (including the Kubernetes RBAC roles and bindings, and the`ingress-nginx-controller`ingress controller service of type LoadBalancer) depends on whether you are deploying into a cluster with managed/self-managed nodes, or into a cluster with virtual nodes:
- 

Managed nodes and self-managed nodes

To deploy the Nginx ingress controller, run the following command:

```

```

where`<vnum>`is the version number of the latest version of the`ingress-nginx-controller`ingress controller deployment script. For example, at the time of writing, the latest version of the script has the version number 1.1.3, so the command to run is:

```

```

To find out the version number of the latest version of the script, see the[kubernetes/ingress-nginx documentation on GitHub](https://github.com/kubernetes/ingress-nginx).
- 

Virtual nodes

On virtual nodes, you have to modify the ingresss controller's deployment manifest and comment out the`fsgroup`,`allowprivilegeEscalation`, and`capabilities`security contexts. For an example of such a modified deployment manifest, see[https://github.com/oracle-devrel/oci-oke-virtual-nodes/tree/main/ingress-nginx](https://github.com/oracle-devrel/oci-oke-virtual-nodes/tree/main/ingress-nginx).

To deploy the Nginx ingress controller based on this modified manifest, run the following command:

```

```

### Verifying the`ingress-nginx-controller`Ingress Controller Service is Running as a Load Balancer Service
- 

View the list of running services by entering:

```

```

The output from the above command shows the services that are running:

```

```

The EXTERNAL-IP for the`ingress-nginx-controller`ingress controller service is shown as`<pending>`until the load balancer has been fully created in Oracle Cloud Infrastructure.
- 

Repeat the`kubectl get svc`command until an EXTERNAL-IP is shown for the`ingress-nginx-controller`ingress controller service:

```

```

The output from the above command shows the EXTERNAL-IP for the`ingress-nginx-controller`ingress controller service:

```

```

### Creating the TLS Secret

A TLS secret is used for SSL termination on the ingress controller.
- 

Output a new key to a file. For example, by entering:

```

```

To generate the secret for this example, a self-signed certificate is used. While this is okay for testing, for production, use a certificate signed by a Certificate Authority.
Note  
  
Under Windows, you may need to replace`"/CN=nginxsvc/O=nginxsvc"`with`"//CN=nginxsvc\O=nginxsvc"`. For example, this is necessary if you run the`openssl`command from a Git Bash shell.
- 

Create the TLS secret by entering:

```

```

## Setting Up the Example Backend

In this section, you define a hello-world backend service and deployment.

### Creating the docker-hello-world Service Definition
- 

Create the file`hello-world-ingress.yaml`containing the following code. This code uses a publicly available hello-world image from Docker Hub. You can substitute another image of your choice that can be run in a similar manner.

```

```

Note the docker-hello-world service's type is ClusterIP, rather than LoadBalancer, because this service will be proxied by the`ingress-nginx-controller`ingress controller service. The docker-hello-world service does not need public access directly to it. Instead, the public access will be routed from the load balancer to the ingress controller, and from the ingress controller to the upstream service.
- 

Create the new hello-world deployment and service on nodes in the cluster by running the following command:

```

```

## Using the Example Ingress Controller to Access the Example Backend

In this section you create an ingress to access the backend using the ingress controller.

### Creating the Ingress Resource
- 

Create the file`ingress.yaml`and populate it with this code:

```

```

Note that the above example YAML works with clusters running Kubernetes version 1.19.x and later.
- 

Create the resource by entering:

```

```

## Verifying that the Example Components are Working as Expected

In this section, you confirm that all of the example components have been successfully created and are operating as expected. The`docker-hello-world-svc`service should be running as a ClusterIP service, and the`ingress-nginx-controller`service should be running as a LoadBalancer service. Requests sent to the ingress controller should be routed to nodes in the cluster.

### Obtaining the External IP Address of the Load Balancer

To confirm the`ingress-nginx-controller`service is running as a LoadBalancer service, obtain its external IP address by entering:

```

```

The output from the above command shows the services that are running:

```

```

### Sending cURL Requests to the Load Balancer
- 

Use the external IP address of the`ingress-nginx-controller`service (for example, 129.146.214.219) to curl an http request by entering:

```

```

Example output from the above command:

```

```

The output shows a 301 redirect and a Location header that suggest that http traffic is being redirected to https.
- 
Either cURL against the https url or add the`-L`option to automatically follow the location header. The`-k`option instructs cURL to not verify the SSL certificates. For example, by entering:

```

```

Example output from the above command:

```

```

The last line of the output shows the HTML that is returned from the pod whose hostname is`docker-hello-world-1732906117-0ztkm`.
- 

Issue the cURL request several times to see the hostname in the HTML output change, demonstrating that load balancing is occurring:

```

```

### Inspecting nginx.conf

The`ingress-nginx-controller`ingress controller deployment manipulates the`nginx.conf`file in the pod within which it is running.
- 

Find the name of the pod running the`ingress-nginx-controller`ingress controller deployment by entering:

```

```

The output from the above command shows the name of the pod running the`ingress-nginx-controller`ingress controller deployment:

```

```

- 

Use the name of the pod running the`ingress-nginx-controller`ingress controller deployment to show the contents of`nginx.conf`by entering the following`kubectl exec`command:

```

```

- 

Look for`proxy_pass`in the output. There will be one for the default backend and another that looks similar to:

```

```

This shows that Nginx is proxying requests to an upstream called`upstream_balancer`.
- 

Locate the upstream definition in the output. It will look similar to:

```

```

The upstream is proxying via Lua.

## (Optional) Upgrading the Example Ingress Controller

In this optional section, you find out how to carry on using the example ingress controller for Kubernetes application traffic management, rather than removing it immediately.

If you want to, you can continue using the example ingress controller you created earlier. However, note that new versions of Nginx are released periodically. Therefore, if you do continue using the example ingress controller, you will periodically have to upgrade the version of Nginx that the ingress controller uses. Typically, you'll want to preserve the ingress controller's existing EXTERNAL-IP address when upgrading Nginx.

To upgrade the existing ingress controller without deleting the existing Oracle Cloud Infrastructure load balancer (and thereby preserve its existing EXTERNAL-IP address), follow the[Upgrading Nginx Without Helm](https://kubernetes.github.io/ingress-nginx/deploy/upgrade/#without-helm)instructions in the Nginx documentation.

To determine which Nginx image to reference when upgrading Nginx, see the[Nginx Changelog](https://github.com/kubernetes/ingress-nginx/blob/main/Changelog.md)in the Nginx documentation.

## (Optional) Removing the Example Ingress Controller

In this optional section, you remove the example ingress controller you created earlier, including:
- the`ingress-nginx-controller`ingress controller deployment
- the Kubernetes RBAC roles and bindings
- the`ingress-nginx-controller`ingress controller service of type LoadBalancer

Note that if you later decide to apply the ingress controller deployment script for a second time to re-create the example ingress controller, a new`ingress-nginx-controller`service of type LoadBalancer is created that has a different EXTERNAL-IP address to the previous service.

You do not have to remove the example ingress controller if you want to continue using it. However, if you do continue using the example ingress controller, you will periodically have to upgrade the version of Nginx that the ingress controller uses. See[(Optional) Upgrading the Example Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupingresscontroller.htm#contengsettingupingresscontroller_topic-Housekeeping-Upgrade-ingress-controller).

### Removing the Example Ingress Controller
- 

Run the following command to remove the example ingress controller you created earlier:

```

```

where`<deployment-script-location>`is the location of the deployment script that you previously used to create the example ingress controller.

For example:

```

```
