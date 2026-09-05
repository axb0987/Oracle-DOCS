# Issues affecting API gateways
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-affecting-API-gateways.htm
- Fetched: 2026-09-05 01:38 CDT

# Issues affecting API gateways

Find out how to troubleshoot problems affecting API gateways created with the API Gateway service.

You might encounter the issues described in this topic that affect API gateways created with the API Gateway service.

See also[Troubleshooting Guides for API Gateway Issues](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-troubleshooting-guides_gateway-issues.htm).

## Modifying a defined tag causes an API gateway to enter a failed state

If you apply a defined tag to an API gateway (either directly or as a tag default for a compartment) and subsequently modify the tag definition, the API gateway can enter a failed state.

Apply a defined tag to an API gateway only if the defined tag isn't going to change.
