# Creating an Enterprise Application with Authorization Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm
- Fetched: 2026-09-05 02:17 CDT

# Creating an Enterprise Application with Authorization Policy

These use cases provide example requests to create an enterprise application with an authorization policy using the identity domains REST API.

The following use cases walk you through the steps to create an enterprise application with authorization policy using the REST APIs:
- [Create an Enterprise Application](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_n2y_xzw_mjb)
- [Create an App Resource](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_ahr_wjx_mjb)
- [Update the App Resource ID Reference in an Enterprise App](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_gbt_qmx_mjb)
- [Add Web Tier Policy to an Enterprise App](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_t5w_ppx_mjb)
- [Create Allow Authorization Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_mb4_rhz_mjb-2)
- [Create Deny Authorization Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_ol4_4th_njb)

## Create an Enterprise Application

The following example shows how to create an enterprise application by submitting a POST request on the REST resource using cURL. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

Note  
  
Template id should map to the Enterprise app template.

### Example of Request Body

The following shows an example of the request body in JSON format:
```

```

### Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

## Create an App Resource

The following example shows how to create an app resource by submitting a POST request on the REST resource using cURL. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

Note  
  
Replace the`{{appid}}`placeholder with the app id from the app creation response.

### Example of Request Body

The following shows an example of the request body in JSON format:
```

```

### Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

## Update the App Resource ID Reference in an Enterprise App

The following example shows how to update values for an application by submitting a PATCH request on the REST resource using cURL. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

### Example of Request Body

The following shows an example of the request body in JSON format:
```

```

### Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

## Add Web Tier Policy to an Enterprise App

The following example shows how to update values for an application by submitting a PATCH request on the REST resource using cURL. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

### Example of Request Body

The following shows an example of the request body in JSON format:
```

```

### Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

## Create Allow Authorization Policy

These use cases provide example requests to create the allow authorization policy for an enterprise application using the identity domains REST API.

The following use cases walk you through the steps to create the allow authorization policy for an enterprise application using the identity domains REST API:
- [Add Allow Authorization Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_zdy_w5y_mjb)
- [Create Allow Authorization Policy Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_pkk_xwy_mjb)
- [Create Allow Authorization Policy Condition Group](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_xx4_lcz_mjb)
- [Create Allow Authorization Policy Rule](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_ljj_ndz_mjb)
- [Update Allow Authorization Policy Rule Reference](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_gqx_l2z_mjb)
- [Update App Resource Reference for Allow Authorization Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_gqs_hfz_mjb)

### Add Allow Authorization Policy

The Allow Authorization Policy is automatically added while creating an enterprise application.

The created policy ID is available in the response as follows:
```

```

### Create Allow Authorization Policy Conditions

The following example shows how to create a condition to be evaluated by submitting a POST request on the REST resource using cURL. Conditions are referenced from Condition Groups. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

#### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

#### Example of Request Body - Group Condition

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body - Group Condition

The following example shows the contents of the response body in JSON format:
```

```

#### Example of Request Body - User Not in Condition

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body - User Not in Condition

The following example shows the contents of the response body in JSON format:
```

```

#### Example of Request Body - Administrator Role Condition

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body - Administrator Role Condition

The following example shows the contents of the response body in JSON format:
```

```

#### Example of Request Body - Network Perimeter Condition

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body - Network Perimeter Condition

The following example shows the contents of the response body in JSON format:
```

```

### Create Allow Authorization Policy Condition Group

The following example shows how to create a condition group to be evaluated by submitting a POST request on the REST resource using cURL. Condition groups are referenced from a Rule. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

#### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

#### Example of Request Body

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

### Create Allow Authorization Policy Rule

The following example shows how to create a rule by submitting a POST request on the REST resource using cURL. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

#### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

#### Example of Request Body

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

### Update Allow Authorization Policy Rule Reference

The following example shows how to update values for a policy by submitting a PATCH request on the REST resource using cURL. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

#### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

#### Example of Request Body

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

### Update App Resource Reference for Allow Authorization Policy

The following example shows how to update values for an application by submitting a PATCH request on the REST resource using cURL. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

#### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

#### Example of Request Body

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

## Create Deny Authorization Policy

These use cases provide example requests to create the deny authorization policy for an enterprise application using the identity domains REST API.

The following use cases walk you through the steps to create the deny authorization policy for an enterprise application using the identity domains REST API:
- [Add Deny Authorization Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_vtn_5th_njb)
- [Create Deny Authorization Policy Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_zr1_l5h_njb)
- [Create Deny Authorization Policy Condition Group](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_atb_y5h_njb)
- [Create Deny Authorization Policy Rule](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_ofs_2vh_njb)
- [Update Deny Authorization Policy Rule Reference](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_hzs_5vh_njb)
- [Update App Resource Reference for Deny Authorization Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/entapp-create-ent-app-authz-policy.htm#concept_h4x_nvh_njb)

### Add Deny Authorization Policy

The Deny Authorization Policy is automatically added while creating an enterprise application.

The created policy id is available in the response as follows:
```

```

### Create Deny Authorization Policy Conditions

The following example shows how to create a condition to be evaluated by submitting a POST request on the REST resource using cURL. Conditions are referenced from Condition Groups. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

#### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

#### Example of Request Body - Group Condition

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body - Group Condition

The following example shows the contents of the response body in JSON format:
```

```

#### Example of Request Body - User Not in Condition

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body - User Not in Condition

The following example shows the contents of the response body in JSON format:
```

```

#### Example of Request Body - Administrator Role Condition

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body - Administrator Role Condition

The following example shows the contents of the response body in JSON format:
```

```

#### Example of Request Body - Network Perimeter Condition

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body - Network Perimeter Condition

The following example shows the contents of the response body in JSON format:
```

```

### Create Deny Authorization Policy Condition Group

The following example shows how to create a condition group to be evaluated by submitting a POST request on the REST resource using cURL. Condition groups are referenced from a Rule. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

#### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

#### Example of Request Body

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

### Create Deny Authorization Policy Rule

The following example shows how to create a rule by submitting a POST request on the REST resource using cURL. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

#### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

#### Example of Request Body

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

### Update Deny Authorization Policy Rule Reference

The following example shows how to update values for a policy by submitting a PATCH request on the REST resource using cURL. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

#### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

#### Example of Request Body

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```

### Update App Resource Reference for Deny Authorization Policy

The following example shows how to update values for an application by submitting a PATCH request on the REST resource using cURL. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

#### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

#### Example of Request Body

The following shows an example of the request body in JSON format:
```

```

#### Example of Response Body

The following example shows the contents of the response body in JSON format:
```

```
