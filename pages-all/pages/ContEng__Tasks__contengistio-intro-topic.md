# Working with Istio as a Standalone Program
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm
- Fetched: 2026-09-05 01:55 CDT

# Working with Istio as a Standalone Program

Find out how to install Istio as a standalone program on clusters you've created with Kubernetes Engine (OKE).

This topic provides an example of how to install Istio as a standalone program on clusters you've created with Kubernetes Engine (OKE). In addition, key features of OKE and Istio are demonstrated.

Topics covered include:
- [Installing Istio as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm#install_istio_on_oke)
- [Exploring Istio Observability](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm#exploring_istio_observability)
- [Managing Traffic](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm#managing_traffic)
- [Securing Istio](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm#securing_istio)

Note that service mesh products (such as Istio) are supported regardless of the CNI plugin you are using for pod networking (either the OCI VCN-Native Pod Networking CNI plugin or the flannel CNI plugin). Worker nodes must be running Kubernetes 1.26 (or later).
Note  
  

You can use Istio with managed node pools, but not with virtual node pools.

## Installing Istio as a Standalone Program

To get started using Istio, create an OKE cluster or use an existing OKE cluster, then install Istio. The sections provided below discuss the steps to install and test your Istio setup. For a complete list of installation options,[see here](https://istio.io/latest/docs/setup/install/).

### Creating an OKE cluster

Create an OKE cluster.
- If you have not already done so, create an OKE cluster within your OCI tenancy.[Multiple options](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm)are available to create an OKE cluster . The simplest option is the[Quick Create](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Quick_Cluster_with_Default_Settings.htm)wizard in the web console.
- To access the OKE cluster on your local machine, install[kubectl](https://kubernetes.io/docs/tasks/tools/)and[oci-cli](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliupgrading.htm).
- [Access the OKE cluster](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#localdownload)from the command line using`kubectl`by setting up the`kubeconfig`file and ensure that`kubectl`can access the cluster.

### Downloading Istio from the Command Line

Follow these steps to download Istio from the command line.
- Download Istio by running the following command:

```

```

- Move to the Istio package directory. For example, if the package is istio-1.11.2:

```

```

- Add the`istioctl`client tool to the`PATH`for your workstation.

```

```

- Validate if the cluster meets Istio install requirements by running the precheck:

```

```

### Installing Istio with istioctl
Install Istio with`istioctl`using the following command:

```

```

### Running the Bookinfo Application

The Istio project provides the Bookinfo application as a way to demonstrate Istio features. The application displays information about a book, similar to a single catalog entry of an online book store. Each book page contains a description of the book, details about the book (ISBN, number of pages), and a few book reviews. For more information on the Bookinfo application, see[the Bookinfo docs here](https://istio.io/latest/docs/examples/bookinfo/).

As you can see from the diagram, the Bookinfo application is composed of four microservices.
- Product Page Service: Calls the Details and Reviews services to create a product page.
- Details Service: Returns book information.
- Reviews Service: Returns book reviews and calls the Ratings service.
- Ratings Service: Returns ranking information for a book review.

To install and run the Bookinfo application, follow these steps.
- Label the namespace that hosts the application with`istio-injection=enabled`.

```

```

- Deploy the sample Bookinfo application.

```

```

- Verify that all services and pods are running.

```

```

- Confirm that the application is running by sending a curl command from a pod.

```

```

- Make the application accessible from outside the cluster.

```

```

- Verify that the application is using the gateway. Determine the`INGRESS_HOST`and`INGRESS_PORT`using[these instructions](https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/#determining-the-ingress-ip-and-ports).

```

```

Also, open the URL`http://${INGRESS_HOST}:${INGRESS_PORT}/productpage`in a browser to view the Bookinfo web page. Refresh the page several times to see different versions of reviews shown on the product page.

### Adding Istio Integration Applications

Istio integrates well with several popular Kubernetes related applications.

Prometheus

Istio provides a basic sample installation to quickly get Prometheus up and running.

```

```

Alternatively, install prometheus and[configure](https://istio.io/latest/docs/ops/integrations/prometheus/#configuration)it to scrape Istio metrics.

For production-scale monitoring using Prometheus, see[Using Prometheus for production-scale monitoring](https://istio.io/latest/docs/ops/best-practices/observability/#using-prometheus-for-production-scale-monitoring).

Grafana

Istio provides a basic sample installation to get Grafana up and running quickly. All the Istio dashboards are included in the installation.

```

```

Alternatively,[install Grafana separately](https://grafana.com/docs/grafana/latest/installation/kubernetes/). In addition,[Istio's preconfigured dashboards](https://istio.io/latest/docs/ops/integrations/grafana/)can be imported.

Jaeger

Istio provides a basic sample installation to quickly get Jaeger up and running.

```

```

Alternatively, install Jaeger separately and[configure](https://istio.io/latest/docs/ops/integrations/jaeger/)Istio to send traces to the Jaeger deployment.

Zipkin

Istio provides a basic sample installation to quickly get zipkin up and running.

```

```

Alternatively, install zipkin separately and[configure](https://istio.io/latest/docs/ops/integrations/zipkin/#installation)Istio to send traces to the zipkin deployment.

Kiali

Istio provides a basic sample installation to quickly get Kiali up and running:

```

```

Alternatively,[install and configure Kiali separately](https://kiali.io/documentation/latest/installation-guide/).

## Exploring Istio Observability

In this section, explore the performance metrics and tracing features provided by the Istio integration applications.

### Querying Metrics from Prometheus for Bookinfo application

With Prometheus and Istio, the Bookinfo performance data is analyzed in several ways.

First, verify that Prometheus is installed.

```

```

Start the Prometheus UI with the following command:

```

```

Select Graph to the right of Prometheus in the header. To see some data, generate traffic for product page using a browser or`curl`. The traffic is reflected in the Prometheus dashboard.
- For viewing results, follow the[instructions here](https://istio.io/latest/docs/tasks/observability/metrics/querying-metrics/#querying-istio-metrics).
- For more on querying Prometheus, read the Istio[querying docs](https://prometheus.io/docs/querying/basics/).

### Visualizing Metrics for Bookinfo Application with Grafana

Combining Prometheus with Grafana provides some nice performance dashboards for applications. To use the dashboards, first verify that both Prometheus and Grafana are installed.

```

```

Start the Istio Grafana dashboard.

```

```

Managing Grafana Dashboards

The Istio service mesh delivers six Grafana dashboards. The Istio service mesh Grafana dashboard snapshots are captured here.
Note  
  
Generate traffic to the product page using a browser or`curl`and see it reflected in the Grafana dashboard.

Istio Mesh Dashboard
[

Istio Service Dashboard
[

Istio Workload Dashboard
[

Istio Performance Dashboard
[

Istio Control Pane Dashboard
[

For more on how to create, configure, and edit dashboards, see the[Grafana documentation](https://docs.grafana.org/).

### Performing Distributed Tracing using Jaeger

Use the Jaeger open source framework to perform application tracing with Istio.
- Enable and configure tracing using`istioctl`:

```

```

- With the Bookinfo application deployed, open the Jaeger UI using`istioctl`.

```

```

- To generate traces, send in requests to the product page.

```

```

You see that the traces reflected in the Jaeger dashboard.

Jaeger Dashboard
[

Jaeger Application Trace
[

### Performing Distributed Tracing using zipkin

Use the zipkin open source framework to perform application tracing with Istio.
- Enable and configure tracing using`istioctl`.

```

```

- With the Bookinfo application deployed, open the zipkin UI using`istioctl`.

```

```

- To generate traces, send in requests to the product page.

```

```

You see that the traces reflect in the zipkin dashboard.

Sample zipkin Dashboard
[

### Performing Distributed Tracing with OCI Application Performance Monitoring

OCI[Application Performance Monitoring (APM)](https://docs.oracle.com/iaas/application-performance-monitoring/doc/application-performance-monitoring.html)integrates with open source tracing system tools such as Jaeger and zipkin. APM enables you to upload trace data in OCI. To integrate with OCI APM, create an APM domain by following the instructions mentioned[here](https://docs.oracle.com/iaas/application-performance-monitoring/doc/create-apm-domain.html). An APM domain is an OCI resource which contains the systems monitored by APM.

After the domain is created, view the domain details and[obtain the data upload endpoint](https://docs.oracle.com/iaas/application-performance-monitoring/doc/obtain-data-upload-endpoint-and-data-keys.html), private key, and public key to construct the APM Collector URL. The APM collector URL is required when configuring open source tracers to communicate with the APM service. The Collector URL format requires a URL constructed using the data upload endpoint as the base URL and generates the path based on choices including values from our private or public key. The format is documented[here](https://docs.oracle.com/iaas/application-performance-monitoring/doc/configure-open-source-tracing-systems.html#GUID-B5EDE254-C854-436D-B844-B986A4E077AA). With the URL path constructed, plug the URL into the Istio config.
Note  
  
For more detailed information on configuring APM service policies, see:
- [APM Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/apmpolicyreference.htm)
- [APM Policy Example](https://docs.oracle.com/iaas/application-performance-monitoring/doc/perform-oracle-cloud-infrastructure-prerequisite-tasks.html)

Configuring Istio to Send Traces to APM
- Enable tracing with`istioctl`.

```

```

Note  
  
The endpoint address of`aaaabbbb.apm-agt.us-ashburn-1.oci.oraclecloud.com`is an example and not an actual endpoint.
- Configure Envoy to[send the zipkin traces](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/trace/v3/zipkin.proto)to APM. Replace the code in`samples/custom-bootstrap/custom-bootstrap.yaml`with the following code block.

```

```

- Apply the custom config.

```

```

- For all our services in Bookinfo to use this custom bootstrap configuration, add an annotation`sidecar.istio.io/bootstrapOverride`with the name of custom ConfigMap as the value. In the following example, an annotation is added for product page under`samples/bookinfo/platform/kube/bookinfo.yaml`. Add a similar annotation to other services.

```

```

- Apply the yaml, all the restarted pods start sending traces to APM.

```

```

- To enable an ingress-gateway to send traces, create a`configmap`named`custom-bootstrap.yaml`in the istio-system namespace:

```

```

- Create a patch named`gateway-patch.yaml`for the ingress-gateway to start using custom-bootstrap config:

```

```

- Apply the previous patch for the ingress gateway:

```

```

- To generate traces, send in requests to the product page.

```

```

You see that the traces reflect in the APM dashboard by following the steps[here](https://docs.oracle.com/iaas/application-performance-monitoring/doc/monitor-traces-trace-explorer.html).

Zipkin Trace Explorer
[

Zipkin Trace
[

Zipkin Spans

To see the spans, select Home in the APM list.
[

Zipkin App Dashboard

APM provides functionality to create dashboards and explore the spans generated over time. Dashboards can be created by following the steps[here](https://docs.oracle.com/iaas/application-performance-monitoring/doc/create-custom-dashboard.html).
[

Zipkin Metrics Explorer

APM allows you to monitor the health, capacity, and performance of your applications by using[metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics),[alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms), and[notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#Notifications_Overview). Follow to steps[here](https://docs.oracle.com/iaas/application-performance-monitoring/doc/application-performance-monitoring-metrics.html)to configure metrics.
[

### Observing Logs with OCI Logging

[OCI Logging](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm)is a central component for analyzing and searching log file entries for tenancies in OCI. Kubernetes container logs from OKE worker nodes can be published as[custom logs](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengviewingworkernodelogs.htm)to OCI Logging. Follow the[steps described here to configure OCI Logging](https://www.ateam-oracle.com/observabitiliy-on-oracle-oci-using-custom-logs-in-oci-logging-to-monitor-and-analyze-cloud-native-applications)to ingest container logs.
- Enable envoy access logging in Istio with`istioctl`.

```

```

- Access the Bookinfo product page using a browser or curl. The generated access logs can be viewed using the`kubectl`command.

```

```

If OCI Logging is configured for the cluster, these logs can be queried and analyzed using OCI console's log search page.

OCI Logging Search
[

OCI Logging Search Expanded
[

### Visualizing Mesh Using Kiali

Verify that Kiali is installed.

```

```

Open the Kiali UI in the browser.

```

```

Send some traffic to the product page.

```

```

Visualize your mesh in Kiali by following step 5[from here](https://istio.io/latest/docs/tasks/observability/kiali/#generating-a-graph).

## Managing Traffic

Istio's traffic routing rules lets you control the flow of traffic between services and simplifies configuration of service-level properties like circuit breakers, timeouts, and retries. Istio makes it easy to set up important tasks like A/B testing, canary rollouts, and staged rollouts with percentage-based traffic splits.

Istio's traffic management API resources:
- [Virtual Services](https://istio.io/latest/docs/concepts/traffic-management/#virtual-services)
- [Destination Rules](https://istio.io/latest/docs/concepts/traffic-management/#destination-rules)
- [Gateways](https://istio.io/latest/docs/concepts/traffic-management/#gateways)
For Istio to control the Bookinfo application version routing, define all the available versions of your service, called subsets, in destination rules. Create default destination rules for the Bookinfo services:

```

```

### Shifting Traffic

Istio allows us to migrate traffic gradually from one version of a microservice to another version using Istio's weighted routing feature. The following example shows how to configure to send 50% of traffic to`reviews:v1`and 50% to`reviews:v3`. After that, complete the migration by sending 100% of traffic to`reviews:v3`.
- Route all traffic to the v1 version of each microservice.

```

```

To view the Bookinfo web page, open the URL`http://${INGRESS_HOST}:${INGRESS_PORT}/productpage`in a browser. Notice that the reviews part of the page displays with no rating stars, no matter how many times you refresh. Istio is configured to route all traffic for the reviews service to`reviews:v1`and this version of the service does not access the star ratings service.
- Transfer 50% of the traffic from`reviews:v1`to`reviews:v3`with the following command, and wait for the new rules to propagate.

```

```

Refresh the`/productpage`URL in your browser and see red colored star ratings approximately 50% of the time. The`reviews:v3`accesses the star ratings service, but the`reviews:v1`version does not.
- Now route 100% of the traffic to`reviews:v3`.

```

```

- Refresh the`/productpage`URL in your browser and see red colored star ratings all the time for each review.

### Managing Request Routing
Istio can route traffic in several ways. To start, configure Istio to route all traffic through v1 of each microservice.

```

```

To view the Bookinfo web page, open the URL`http://${INGRESS_HOST}:${INGRESS_PORT}/productpage`in a browser . Notice that the reviews part of the page displays with no rating stars, no matter how many times you refresh. Because Istio is configured to route all traffic for the reviews service to the version`reviews:v1`. This version of the service does not access the star ratings service.
[

Routing based on User Identity

To route based on user identity:
- Change the route configuration so that all traffic from a specific user named`jason`is routed to`reviews:v2`. Istio doesn't have any special, built-in understanding of user identity. In this example, the`productpage`service adds a custom end-user header to all outbound HTTP requests to the reviews service.

```

```

- 

To view the Bookinfo web page and login as user`jason`, open the URL`http://${INGRESS_HOST}:${INGRESS_PORT}/productpage`in a browser. Refresh the browser to see that star ratings appear next to each review.
[
- 

Open the URL`http://${INGRESS_HOST}:${INGRESS_PORT}/productpage`in a browser to view the Bookinfo web page and login as user other than`jason`. Refresh the browser to see no stars for each review.
[

Routing based on URL Rewriting

In this example, HTTP requests with a path that starts with`/products`or`/bookinfoproductpage`are rewritten to`/productpage`. HTTP requests are sent to pods with`productpage`running on port 9080. For more information on Istio URL rewriting,[see here](https://istio.io/latest/docs/reference/config/networking/virtual-service/#HTTPRewrite).
- Apply the following yaml:

```

```

- 

To view the Bookinfo web page, open the URL`http://${INGRESS_HOST}:${INGRESS_PORT}/products`and`http://${INGRESS_HOST}:${INGRESS_PORT}/bookinfoproductpage`in a browser. In both the cases, a rewrite is performed before forwarding the request.

Rewrite /bookproductpage
[

Rewrite /products
[
- Clean up the yaml file to the original version provided by Istio and apply it.

```

```

- 

Open the URL`http://${INGRESS_HOST}:${INGRESS_PORT}/bookinfoproductpage`or`http://${INGRESS_HOST}:${INGRESS_PORT}/products`to not see the product page because the yaml doesn't rewrite the request.

404 Error /products
[

404 Error /booksproductpage
[

### Testing Network Resilience

Istio allows you to configure your installation for request timeouts, fault injection, and circuit breakers. These settings allow manage and test the fault tolerance of deployed applications.

Setting Request Timeouts

A timeout is the amount of time an Envoy proxy waits for replies from a given service. The timeout ensures that services don't wait for replies indefinitely and ensures that calls succeed or fail within a predictable timeframe. For more information on timeouts,[see here](https://istio.io/latest/docs/concepts/traffic-management/#timeouts).

A timeout for HTTP requests can be specified using the timeout field of the[route rule](https://istio.io/latest/docs/reference/config/networking/virtual-service/#HTTPRoute). By default, the request timeout is disabled.
- Initialize the application version routing by running the following command:

```

```

- Route requests to`reviews:v2`service, in effect, a version that calls the ratings service:

```

```

- Add a 2-second delay to calls to the ratings service:

```

```

- To view the Bookinfo web page with ratings stars displayed, open the URL`http://${INGRESS_HOST}:${INGRESS_PORT}/productpage`in a browser . A 2-second delay occurs whenever you refresh the page.
[
- Add a half second request timeout for calls to the reviews service:

```

```

- To view the Bookinfo web page, open the URL`http://${INGRESS_HOST}:${INGRESS_PORT}/productpage`in a browser. Notice the page returns in about 1 second, instead of 2, and the reviews are unavailable.
[

The reason that the response takes 1 second, even though the timeout is configured at half a second, is because a hard-coded retry in the`productpage`service. The service calls the timed out reviews service twice before returning.

In addition to overriding them in route rules, the timeout can also be overridden on a per-request basis if the application adds an`x-envoy-upstream-rq-timeout-ms`header on outbound requests.

Managing Fault Injection

Fault injection is a testing method that introduces errors into a system to ensure that the system withstands and recovers from error conditions. Istio allows fault injection at the application layer such as HTTP error codes. Istio injects two types of faults, both configured using a virtual service. For more information on fault injection,[see here](https://istio.io/latest/docs/concepts/traffic-management/#fault-injection).
- Delays: Delays are timing failures that mimic increased network latency or an overloaded upstream service.
- Aborts: Aborts are crash failures that mimic failures in upstream services. Aborts manifest in the form of HTTP error codes or TCP connection failures.

To test fault injection, run the following command to initialize the application version routing:

```

```

Injecting an HTTP Delay Fault

To inject a delay fault, follow these steps:
- Create a fault injection rule to delay traffic coming from the user`jason`. The following command injects a 7-second delay between the`reviews:v2`and ratings microservices for user`jason`.

```

```

Note  
  
The`reviews:v2`service has a 10-s hard-coded connection timeout for calls to the ratings service. With 7-second delay, expect the end-to-end flow to continue without any errors.
- To view the Bookinfo web page, open the URL`http://${INGRESS_HOST}:${INGRESS_PORT}/productpage`in a browser.
[

The Bookinfo home page loads without any errors in approximately seven seconds. However, the reviews section displays an error message: Sorry, product reviews are currently unavailable for this book . A bug exists in the application code. The hard-coded timeout between the`productpage`and the`reviews`service results in a 6-second delay, 3 seconds plus 1 retry. As a result, the`productpage`call to`reviews`times out prematurely and throws an error after 6 seconds.

To fix the bug, increase the`productpage`to`reviews`service timeout, or decrease the`reviews`to`ratings`timeout to less than 3 seconds.
- Let's fix the bug by adding a 2-second delay to the`ratings`service for user`jason`.

```

```

- Now that the bug is fixed, open the URL`http://${INGRESS_HOST}:${INGRESS_PORT}/productpage`in a browser to view the Bookinfo web page. Sign in as`jason`with ratings stars displayed.
[

Injecting an HTTP Abort Fault

Follow these steps to inject an abort fault:
- Create a fault injection rule to send an HTTP abort response for user`jason`:

```

```

- To view the Bookinfo web page, open the URL`http://${INGRESS_HOST}:${INGRESS_PORT}/productpage`in a browser. Login as user`jason`. A message indicates the`ratings`service is unavailable.
[

Logout from user`jason`or login with any other user to not see any error message.
[

Creating Circuit Breakers

Circuit breaking allows us to write applications that limit the impact of failures, latency spikes, and other undesirable effects of network peculiarities. For more information on circuit breakers,[see here](https://istio.io/latest/docs/concepts/traffic-management/#circuit-breakers).
- Create a[destination rule](https://istio.io/latest/docs/reference/config/networking/destination-rule/)to apply circuit breaking settings when calling the product service. The following rule sets the maximum number of connections to be not more than one and have a maximum of one HTTP pending requests. In addition, the rules configure hosts to be scanned every 1 second. Any host that fails one time with a 5XX error code is ejected for 3 minutes. Also, 100% of hosts in the load balancing pool for the upstream service are ejected.

```

```

- Route all traffic to the v1 version of each microservice.

```

```

- Create a client to send traffic to the product service. Fortio lets you control the number of connections, concurrency, and delays for outgoing HTTP calls. If you have enabled[automatic sidecar injection](https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/#automatic-sidecar-injection), deploy the`fortio`service:

```

```

Alternatively, manually inject the sidecar before deploying the`fortio`application.

```

```

- Log in to the client pod and use the`fortio`tool to call`productpage`and verify the response status code to be 200 with the following commands.

```

```

The following output is produced:

```

```

- Call the service with 2 concurrent connections (-c 2) and send 20 requests (-n 20). Interestingly, 16 requests passthrough and 4 fail.

```

```

The command produces output similar to the following.

```

```

- Increase the number of concurrent connections to 3.

```

```

Only 26.7% of the requests succeeded and circuit breaking traps the rest.

```

```

- Query the`istio-proxy`stats to gain more information.

```

```

Circuit breaking flags 32 calls by looking at the metric`upstream_rq_pending_overflow`.

```

```

- Clean up the client.

```

```

### Mirroring

Traffic mirroring, also called shadowing, allows teams to bring changes to production with as little risk as possible. Mirroring sends a copy of live traffic to a mirrored service. The mirrored traffic occurs outside of the critical request path for the primary service.
- Route all traffic to the v1 version of each microservice.

```

```

- Change the route rule to mirror traffic to`reviews:v2`.

```

```

The previous route rule sends 100% of the traffic to`reviews:v1`and mirrors 100% of the same traffic to the`reviews:v2`service.

When traffic gets mirrored, the requests are sent to the mirrored service with their Host/Authority headers appended with`-shadow`. For example, reviews become`reviews-shadow.Mirrored`requests considered as "fire and forget." The mirrored responses are discarded.

Instead of mirroring all requests, change the value field under the`mirrorPercentage`field to mirror a fraction of the traffic. If this field is absent, all traffic is mirrored.
- Send in some traffic by refreshing the url`http://${INGRESS_HOST}:${INGRESS_PORT}/productpage`in a browser.
- Logs of`reviews:v1`service. Note v1 service does not call the ratings service.
[
- Logs of`reviews:v2`mirrored service. Note for the v2 service, the header is appended with`-shadow`.
[

### Managing Gateways

Gateway describes a load balancer operating at the edge of the mesh receiving incoming or outgoing HTTP/TCP connections. Gateway configurations are applied to standalone Envoy proxies that are running at the edge of the mesh, rather than sidecar Envoy proxies running alongside your service workloads. Istio provides some preconfigured gateway proxy deployments`istio-ingressgateway`and`istio-egressgateway`.
If you haven't setup the Istio gateways as part of the installation, run the following command to install them.

```

```

The command deploys Istio using the default settings which includes a gateway. For more information,[see here](https://istio.io/latest/docs/setup/additional-setup/gateway/).
Note  
  
Determine the`INGRESS_HOST`and`INGRESS_PORT`using[these instructions](https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/#determining-the-ingress-ip-and-ports).

Configuring Ingress using Istio Gateway

The ingress gateway configures exposed ports and protocols, but unlike Kubernetes Ingress Resources, does not include any traffic routing configuration. Traffic routing for ingress traffic is instead configured using Istio routing rules. For more information on Istio ingress,[see here](https://kubernetes.io/docs/concepts/services-networking/ingress/).
Note  
  
If you have already deployed the Bookinfo application, the following steps are not required.
- Create an Istio gateway that configures on port 80 for HTTP traffic.

```

```

- Configure routes for traffic entering through the Gateway:

```

```

- To deploy the Bookinfo application, see the "Running the Bookinfo Application" section of the[Installing Istio and OKE page](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm#install_istio_on_oke).
- Access the`productpage`service using curl:

```

```

The command produces the following output:

```

```

- Access any other URL that has not been explicitly exposed. You see an HTTP 404 error.

```

```

The command produces the following output:
```

```

- For explicit hosts in gateways, use the -H flag to set the Host HTTP header. The flag is needed because your ingress gateway and virtual service are configured to handle the host. For example, your host is example.com and the name is specified in both gateways and virtual service.

```

```

- Also, open the URL`http://${INGRESS_HOST}:${INGRESS_PORT}/productpage`in a browser to view the Bookinfo web page.

Configuring Ingress using Kubernetes Ingress Resource

The reader assumes that Bookinfo application is deployed into the cluster. To deploy the Bookinfo application, see the "Running the Bookinfo Application" section of the[Installing Istio and OKE page](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm#install_istio_on_oke).
- Remove the Istio gateway if the configuration is already applied.

```

```

- Create an Ingress resource on port 80 for HTTP traffic.

```

```

The`[](https://kubernetes.io/docs/concepts/services-networking/ingress/)kubernetes.io/ingress.class`annotation is required to tell the Istio gateway controller to handle this`Ingress`.
- Verify accessing the Bookinfo application by following the instructions from previous section.
- Delete the resource and enable Istio gateway for further tasks.

```

```

Accessing External Services with Egress

By default, all outbound traffic from an Istio enabled pod is redirected to its sidecar proxy and Istio configures the Envoy proxy to pass through requests for unknown services. Istio configures the sidecar handling of external services through a configuration field`meshConfig.outboundTrafficPolicy.mode`. If this option is set to:
- `ALLOW_ANY`(default): Istio proxy lets calls to unknown services pass through.
- `REGISTRY_ONLY`: Istio proxy blocks any host without an HTTP service or service entry defined within the mesh.

The reader assumes that the Bookinfo application is deployed into the cluster. If not, follow the steps to deploy the Bookinfo application.

Managing Envoy Passthrough to External Services

To enable passthrough to external services, follow these steps.
- Change the`meshConfig.outboundTrafficPolicy.mode`option to`ALLOW_ANY`with`istioctl`.

```

```

Note  
  
This step is required only if you have explicitly set the option to`REGISTRY_ONLY`during the installation.
- To confirm successful 200 responses, make a request to external services from the`SOURCE_POD`:

```

```

The command produces the following output:
```

```

However, the drawback with this approach is that Istio monitoring and control for traffic to external services is lost.

Controlling Access to External Services [Recommended]

To set up controlled access to external services, follow these steps:
- Change the`meshConfig.outboundTrafficPolicy.mode`option to`REGISTRY_ONLY`. This step is required only if you haven't explicitly set the option to`REGISTRY_ONLY`during the installation.
- Follow only step 1 from the "Envoy Passthrough to External Services" section. The only change to make here is that replace`ALLOW_ANY`with`REGISTRY_ONLY`.
- To verify that the external services are blocked, make a couple of requests to external HTTPS services from the`SOURCE_POD`. Configuration changes take several seconds to propagate, so successful connections are possible. Wait for several seconds and then retry the last command.

```

```

The command produces the following output:
```

```

- Create a`ServiceEntry`to allow access to an external HTTP service.

```

```

- Make a request to the external HTTP service from`SOURCE_POD`. Notice that the headers added by the Istio sidecar proxy:`X-Envoy-Decorator-Operation`.

```

```

The command produces the following output:
```

```

Remove the`grep`command to see all the headers.

```

```

The command produces the following output:
```

```

- For accessing HTTPS calls, replace the port and protocol when creating service entries.
- The approach adds external service traffic management features like timeouts and fault injection. The following request returns 200 (OK) in approximately five seconds.

```

```

Use`kubectl`to set a 3-second timeout on calls to the[httpbin.org](http://httpbin.org/)external service:

```

```

This time a timeout appears after 3 seconds. Although[httpbin.org](http://httpbin.org/)was waiting five seconds, Istio cut off the request at 3 seconds:

```

```

- Clean up the resources for further future tasks.

```

```

Directing Access to External Services

This approach bypasses the Istio sidecar proxy, giving services direct access to any external server. However, configuring the proxy this way does require cluster-provider specific knowledge and configuration. Similar to the first approach, we lose monitoring of access to external services and can't apply Istio features on traffic to external services. Follow[these steps](https://istio.io/latest/docs/tasks/traffic-management/egress/egress-control/#direct-access-to-external-services)to provide direct access to external services.

## Securing Istio

The Istio security features provide strong identity, powerful policy, transparent TLS encryption, and authentication, authorization, and audit (AAA) tools to protect your services and data.

### Configuring Authentication

Istio offers mutual TLS as a full-stack solution for transport authentication, which is enabled without requiring service code changes.
Deploy`sleep`and`httpbin`services in the default namespace.

```

```

By default, Istio performs several tasks. Istio tracks the server workloads migrated to Istio proxies. Istio configures client proxies to send mutual TLS traffic to those workloads automatically. Istio sends plain text traffic to workloads without sidecars.
To verify that certs are sent, send a request from a`sleep`pod to`httpbin`pod and look for the X-Forwarded-Client-Cert header.

```

```

Deploy another instance of the`sleep`and`httpbin`services without the sidecar enabled.

```

```

The request from the`sleep`pod in the default namespace to`httpbin`pod in the legacy namespace is plaintext because the destination is not sidecar enabled. Verify that plain text is sent by running the following command.

```

```

The request from the`sleep`pod in the legacy namespace to`httpbin`in the default namespace also succeeds with a plaintext connection. The can be verified with the following command.

```

```

To prevent non-mutual TLS traffic for the whole mesh, set a mesh-wide peer authentication policy with the mutual TLS mode set to`STRICT`.

```

```

The connection from a`sleep`pod in the legacy namespace to`httpbin`in default namespace no longer works when mutual TLS mode is set to`STRICT`.

```

```

Revert the`STRICT`peer authentication setting by deleting the CR.

```

```

In addition to the global mutual TLS setting, it can also be set at a namespace or workload level. Follow[the Istio documentation for detailed authentication configurations](https://istio.io/latest/docs/tasks/security/authentication/authn-policy/).

### Configurating Authorization

Istio allows you to configure authorization policies for your applications.
First, configure a simple`allow-nothing`policy that rejects all requests to the workload, and then grants more access to the workload gradually and incrementally.

```

```

Open the Bookinfo product page in your browser. It shows "`RBAC: access denied`" error confirming that the`deny-all`policy is working as intended.
Create a policy to grant to all users and workloads access to the product page using the following command.

```

```

You see the "Bookinfo Sample" page but the`productpage`service cannot access the details and reviews page.

Add the following policies to grant`productpage`workload access to the details and reviews workloads and reviews workload access to the`ratings`workload.

Set Details Viewer

```

```

Set Reviews Viewer

```

```

Set Ratings Viewer

```

```

View the product page from a browser without any errors.

To revert the applied policies, enter the following commands.

```

```

### Securing Gateways with TLS

We can expose the Bookinfo application as a secure HTTPS service using either simple or mutual TLS. To sign the certificates for your services, create a root certificate and private key:

```

```

Create a certificate and a private key for`productpage.bookinfo.com`.

```

```

Ensure you have deployed the Bookinfo application. Create a secret for the ingress gateway certificates.

```

```

Update the Bookinfo gateway to include a secure port.

```

```

Create Bookinfo destination rules if not already created.

```

```

Create a virtual service bound to the gateway.

```

```

You can verify TLS connection to the gateway with the following`curl`command.

```

```
