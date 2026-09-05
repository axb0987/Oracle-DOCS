# Issues creating API deployments
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-setting-up-and-running-API-deployments.htm
- Fetched: 2026-09-05 01:38 CDT

# Issues creating API deployments

Find out how to troubleshoot problems when creating API deployments with the API Gateway service.
You might encounter the issues described in this topic when creating API deployments:
- [Creating a new API deployment stalls with a state of Creating, or fails](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-setting-up-and-running-API-deployments.htm#Creating_a_new_API_deployment_stalls_with_a_state_of_Creating_or_fails)
- ["Bad request" HTTP-4xx errors when creating a new API deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Creating_a_new_API_deployment_Bad-request-HTTP-400-errors.htm)
- ["Bad request" HTTP-4xx errors related to mTLS configuration](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Creating_a_new_API_deployment_Bad-request-HTTP-400-errors.htm#apigatewaytroubleshooting_topic_Creating_a_new_API_deployment_Bad_request_HTTP_400_errors_mTLS)

See also[Troubleshooting Guides for Creating API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-troubleshooting-guides_creating-deployments.htm).

## Creating a new API deployment stalls with a state of Creating, or fails

It can take a few minutes to create a new API deployment. While it is being created, the API deployment is shown with a state of Creating on the Deployments tab of the API gateway details page. When it has been created successfully, the new API deployment is shown with a state of Active.

If you have waited more than a few minutes for the API deployment to be shown with an Active state (or if the API deployment creation operation has failed):
- Select the name of the API deployment, and select the Work requests tab to see an overview of the API deployment creation operation.
-
