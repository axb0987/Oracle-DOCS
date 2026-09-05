# Troubleshooting API Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting.htm
- Fetched: 2026-09-05 01:38 CDT

# Troubleshooting API Gateway

Find out how to troubleshoot problems with API Gateway, and possible solutions to common issues.

This topic covers common issues related to the API Gateway service and how you can address them.

The issues in this topic are organized in the following broad categories:
- [Issues creating API gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting.htm#Troubleshooting_API_Gateway__APIGW-Troubleshooting-Setting-up-and-running-gateways)
- [Issues creating API deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting.htm#Troubleshooting_API_Gateway__APIGW-Troubleshooting-Setting-up-and-running-deployments)
- [Issues calling APIs](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting.htm#Troubleshooting_API_Gateway__APIGW-Troubleshooting-Calling-APIs)
- [Issues affecting API gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting.htm#Troubleshooting_API_Gateway__APIGW-Troubleshooting-Affecting-API-gateways)

See also[Troubleshooting Guides for API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-troubleshooting-guides.htm).

## Issues creating API gateways

Error message or description More information
Creating a new API gateway stalls with a state of Creating, or fails.[Creating a new API gateway stalls with a state of Creating, or fails](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-setting-up-and-running-API-gateways.htm#Creating_a_new_API_gateway_stalls_with_a_state_of_Creating_or_fails)
`VNIC attachment failed due to the limit for number of private IP addresses for this subnet`[Creating a new API gateway returns a "VNIC attachment failed due to the limit for number of private IP addresses for this subnet" message](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-setting-up-and-running-API-gateways.htm#Creating_a_new_API_gateway_returns_a_VNIC_attachment_failed_due_to_the_limit_for_number_of_private_IP_addresses_for_this_subnet_message)
`The limit for number of private IP addresses for this subnet has been exceeded`[Creating a new API gateway returns a "The limit for number of private IP addresses for this subnet has been exceeded" message](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-setting-up-and-running-API-gateways.htm#Creating_a_new_API_gateway_returns_a_The_limit_for_number_of_private_IP_addresses_for_this_subnet_has_been_exceeded_message)
`The limit for number of public IP addresses for this compartment has been exceeded`[Creating a new public API gateway returns a "The limit for number of public IP addresses for this compartment has been exceeded" message](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-setting-up-and-running-API-gateways.htm#Creating_a_new_public_API_gateway_returns_a_The_limit_for_number_of_public_IP_addresses_for_this_compartment_has_been_exceeded_message)
`Work request was cancelled`[Creating a new API gateway returns a "Work request was cancelled" message](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-setting-up-and-running-API-gateways.htm#Creating_a_new_API_gateway_returns_a_Work_request_was_cancelled_message)
`An unexpected error occurred. Contact Oracle Support for assistance.`[Creating a new API gateway returns a "An unexpected error occurred. Contact Oracle Support for assistance" message](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-setting-up-and-running-API-gateways.htm#Creating_a_new_API_gateway_returns_a_An_unexpected_error_occurred_Contact_Oracle_Support_for_assistance_message)
`Unknown resource <subnet-ocid>, make sure subnet exists, the user can access the subnet and it is in the same region where the gateway will be created`[Creating a new API gateway returns an "Unknown resource &lt;subnet-ocid&gt;, make sure subnet exists,..." message and a 400 error](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-setting-up-and-running-API-gateways.htm#Creating_a_new_API_gateway_returns_an_Unknown_resource_subnetocid_make_sure_subnet_exists_message_and_a_400_error)

See also[Troubleshooting Guides for Creating API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-troubleshooting-guides_creating-gateways.htm).

## Issues creating API deployments

Errors related to stalling API deployments:

Error message or description More information
Creating a new API deployment stalls with a state of Creating, or fails.[Creating a new API deployment stalls with a state of Creating, or fails](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-setting-up-and-running-API-deployments.htm#Creating_a_new_API_deployment_stalls_with_a_state_of_Creating_or_fails)

"Bad request" HTTP-4xx errors related to mTLS configuration:

Error message or description More information
`Cannot enable mutual TLS because custom CA Bundles are not added to the Gateway. Please add a custom CA Bundle and try again.`[Creating a new API deployment fails with "Cannot enable mutual TLS because custom CA Bundles are not added to the Gateway. Please add a custom CA Bundle and try again." message](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Creating_a_new_API_deployment_Bad-request-HTTP-400-errors.htm#apigatewaytroubleshooting_topic_Creating_a_new_API_deployment_fails_Cannot_enable_mutual_TLS)
`Duplicate SAN or CN values passed in input.`[Creating a new API deployment fails with "Duplicate SAN or CN values passed in input" message](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Creating_a_new_API_deployment_Bad-request-HTTP-400-errors.htm#apigatewaytroubleshooting_topic_Creating_a_new_API_deployment_fails_Duplicate_SAN_or_CN_values)
`Too many value, must not have more than 10 values.`[Creating a new API deployment fails with "Too many value, must not have more than 10 values" message](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Creating_a_new_API_deployment_Bad-request-HTTP-400-errors.htm#apigatewaytroubleshooting_topic_Creating_a_new_API_deployment_fails_Too_many_values)
`Length of SAN or CN string should be less than 256 characters.`[Creating a new API deployment fails with "Length of SAN or CN string should be less than 256 characters" message](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Creating_a_new_API_deployment_Bad-request-HTTP-400-errors.htm#apigatewaytroubleshooting_topic_Creating_a_new_API_deployment_fails_Length_of_SAN_or_CN)
`Invalid format for SAN or CN.`[Creating a new API deployment fails with "Invalid format for SAN or CN"](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Creating_a_new_API_deployment_Bad-request-HTTP-400-errors.htm#apigatewaytroubleshooting_topic_Creating_a_new_API_deployment_fails_Invalid_format_for_SAN_or_CN)

See also[Troubleshooting Guides for Creating API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-troubleshooting-guides_creating-deployments.htm).

## Issues calling APIs

Use API Gateway logs to review invocation information. The Oracle Cloud Infrastructure Logging service is the default and recommended option for accessing, searching, and storing API Gateway logs. For more information, see[Adding Logging to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddinglogpolicies.htm).

Use the error messages from the logs and the information below to resolve invocation issues.

HTTP-5xx errors when API deployment is created successfully but requests fail:

Error message or description More information
`failed to parse pem cert chain`, shown in the log.[Invoking the API deployment fails with an HTTP-5xx error, and a "failed to parse pem cert chain" error is output to the log](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Deployment-requests-fail-with-5xx.htm#apigatewaytroubleshooting_topic_Issues_calling_APIs_Deployment_requests_fail_with_5xx_failed_to_parse_perm_error)
`Client CA Bundle not present`, shown in the log.[Invoking the API deployment fails with an HTTP-5xx error, and a "Client CA Bundle not present" error is output to the log](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Deployment-requests-fail-with-5xx.htm#apigatewaytroubleshooting_topic_Issues_calling_APIs_Deployment_requests_fail_with_5xx_Client_CA_bundle_error)
`Error in client certificate verification`, shown in the log.[Invoking the API deployment fails with an HTTP-5xx error, and an "Error in client certificate verification" error is output to the log](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Deployment-requests-fail-with-5xx.htm#apigatewaytroubleshooting_topic_Issues_calling_APIs_Deployment_requests_fail_with_5xx_Client_certificate_verification_error)
`503: Service Unavailable`[Invoking the API deployment fails with a "Service Unavailable" message and a 503 error](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Deployment-requests-fail-with-5xx.htm#apigatewaytroubleshooting_topic-Issues-calling-APIs_Fail-with-503_Service-Unavailable-error)

HTTP-4xx errors when API deployment created successfully but requests fail:

Error message or description More information
`Client certificate is invalid for this gateway.`, shown in the log.[Invoking the API deployment fails with an HTTP-4xx error, and a "Client certificate is invalid for this gateway" error is output to the log](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Gateway-requests-fail-with-4xx.htm#apigatewaytroubleshooting_topic_Issues_calling_APIs_Gateway_requests_fail_with_4xx_client_certificate_invalid_error)
`SAN validation failure`, shown in the log.[Invoking the API deployment fails with an HTTP-4xx error, and a "SAN validation failure" error is output to the log](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Gateway-requests-fail-with-4xx.htm#apigatewaytroubleshooting_topic_Issues_calling_APIs_Gateway_requests_fail_with_4xx_SAN_validation_error)

Miscellaneous errors when calling APIs

Error message or description More information
`Base 64 Certificate Size greater than 8KB`, shown in the log.[Invoking the API deployment is successful but a "Base 64 Certificate Size greater than 8KB" warning is output to the log](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-calling-APIs_Miscellaneous-issues.htm#apigatewaytroubleshooting_topic_Issues_calling_APIs_Client_CA_bundle_issues_Base64_certificate_size)

See also[Troubleshooting Guides for Calling APIs](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-troubleshooting-guides_calling-apis.htm).

## Issues affecting API gateways

Error message or description More information
Modifying a defined tag causes an API gateway to enter a failed state.[Modifying a defined tag causes an API gateway to enter a failed state](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-Issues-affecting-API-gateways.htm#apigatewaytroubleshooting_topic-Modifying-defined-tag-causes-gateway-to-enter-failed-state)

See also[Troubleshooting Guides for API Gateway Issues](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting_topic-troubleshooting-guides_gateway-issues.htm)
