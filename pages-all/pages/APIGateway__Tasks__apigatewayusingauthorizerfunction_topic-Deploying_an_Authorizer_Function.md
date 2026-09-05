# Deploying an Authorizer Function
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingauthorizerfunction_topic-Deploying_an_Authorizer_Function.htm
- Fetched: 2026-09-05 01:39 CDT

# Deploying an Authorizer Function

Find out how to deploy an authorizer function for use with API Gateway.

To deploy an authorizer function that you've written:
- 

Build a Docker image from the code, push the Docker image to a Docker registry, and create a new function in OCI Functions based on the image. You can do this in different ways:
- You can use the Fn Project CLI command`fn deploy`to build a new Docker image, push the image to the Docker registry, and create a new function in OCI Functions based on the image. See[Creating and Deploying Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsuploading.htm).
- You can use Docker commands to build the image and push it to the Docker registry, and then use the Fn Project CLI command`fn create function`(or the`CreateFunction`API operation) to create a new function in OCI Functions based on the image. See[Creating Functions from Existing Docker Images](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionscreatingfunctions.htm).
- Make a note of the OCID of the function you create in OCI Functions. For example,`ocid1.fnfunc.oc1.phx.aaaaaaaaac2______kg6fq`
- 

If one doesn't exist already, create an Oracle Cloud Infrastructure policy and specify a policy statement to give API gateways access to function-related resources. The policy enables API deployments on those API gateways to invoke the authorizer function. For more information, see[Create a Policy to Give API Gateways Access to Functions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#dynamicgrouppolicy)
