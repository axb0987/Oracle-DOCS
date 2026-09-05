# Invoking OCI Functions from Other Oracle Cloud Infrastructure Services
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsintegratingwithother.htm
- Fetched: 2026-09-05 02:08 CDT

# Invoking OCI Functions from Other Oracle Cloud Infrastructure Services

Find out how to invoke functions in OCI Functions from other Oracle Cloud Infrastructure services.

You can invoke functions in OCI Functions from other Oracle Cloud Infrastructure services. Typically, you'll want an event in another service to trigger a request to invoke a function defined in OCI Functions.

This functionality is currently available in:
- The Events service. For more information, see[Functions](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#func-events)in[Services that Produce Events](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm).
- The Notifications service. For more information, see[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). For a scenario, see[Scenario A: Automatically Resizing VMs](https://docs.oracle.com/iaas/Content/Notification/Tasks/scenarioa.htm).
- The API Gateway service. For more information, see[Adding a Function in OCI Functions as an API Gateway Back End](https://docs.oracle.com/iaas/Content/APIGateway/Tasks/apigatewayusingfunctionsbackend.htm).
- The Oracle Integration service, using the OCI Signature Version 1 security policy. For more information, see[Configure Oracle Integration to Call Oracle Cloud Infrastructure Functions with the REST Adapter](https://www.oracle.com/pls/topic/lookup?ctx=oic&id=ICSRE-GUID-B53B83D6-3647-4591-A1B3-4D075D595F2F)in[Using the REST Adapter with Oracle Integration](https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-adapter/index.html).
- The Connector Hub service. You can invoke a function to process data (as the task in a connector), or to act on the processed data (as the target in a connector). For more information, see[Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm). For a scenario, see[Scenario: Sending Log Data to an Autonomous AI Database](https://docs.oracle.com/iaas/Content/connector-hub/dblogs.htm).
- The Streaming service (via Connector Hub). You can synchronously invoke a function to consume and process data from partitions in a stream (as the task in a connector). For more information, see[Streaming](https://docs.oracle.com/iaas/Content/Streaming/home.htm)and[Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm)
