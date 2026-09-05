# Using Duo Security with Identity Domains
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm
- Fetched: 2026-09-05 02:18 CDT

# Using Duo Security with Identity Domains

These use cases provide a step-by-step example of using Duo Web SDK v2 or Duo Web SDK v4 with an identity domain.
- 

[Updating the Authentication Factor Settings with Duo Security Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_qpm_p2h_4jb)
- 

[Enabling Duo Web SDK v4](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#enabling_duo_websdk_v4)
- 

[Authenticating User Name and Password with Duo Security as an Authentication Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_uwx_chp_mjb)
- 

[Enrolling in MFA with Duo Security Using Self Service](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#self-service-enroll-mfa-duo-security)

## Updating the Authentication Factor Settings with Duo Security Settings

The following example shows how to update Multifactor Authentication settings for a tenant by submitting a PUT request on the REST resource using cURL. For more information about cURL, see[Use cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm).

### cURL Command
Note  
  
The command in this example uses the URL structure`https://<domainURL>/resource-path`, where`<domainURL>`represents the Identity Service URL, and the resource path represents the Identity Service API. See[Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm)for the appropriate URL structure to use.
```

```

### Request Body
The following shows an example of the request body in JSON format:

[Example Request Body](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#)

```

```

### Response Body

The following example shows the contents of the response body in JSON format:

[Example Response Body](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#)

```

```

## Enabling Duo Web SDK v4

Duo Web SDK v2 (iFrame) is enabled in an identity domain by default. To use Duo Web SDK v4, you must enable it.

Use the following instructions to enable Duo Web SDK v4.
- 

Using cURL,`GET /admin/v1/AuthenticationFactorSettings/AuthenticationFactorSettings`

Response Example

You should see the following Duo Web SDK v2 settings.
```

```

- Backup your instance in case rollback is required.
- 

Update the payload from step 1 by adding`enableWebSDKv4`and`duoSecurityAuthzRedirectUrl`under the`urn:ietf:params:scim:schemas:oracle:idcs:extension:thirdParty:AuthenticationFactorSettings`section.
- `enableWebSDKv4`: The default value is`false`. If`enableWebSDKv4`is false, Duo Web SDK v2 is used.
- 

`duoSecurityAuthzRedirectUrl`: The default value is blank. Add your organization's URL here. The redirect URL is used to initiate Duo security authentication, which receives a response from the Duo security server with the`duoSecurityAuthzState`and`duoSecurityAuthzCode`. This URL can be overridden by using the custom UI. The custom UI must use this endpoint to receive the code and parameter from the Duo Security Server.

Note the following attribute changes from v2 to v4.
- `client_id`(`integrationKey`in v2)
- `clientSecret`(`secretKey`in v2)
- `apiHostName`(no change from v2)
- `userMappingAttribute`(no change from v2)

Request Example
```

```

- 

Using cURL,`PUT /admin/v1/AuthenticationFactorSettings/AuthenticationFactorSettings`using step 3 payload.

## Authenticating User Name and Password with Duo Security as an Authentication Factor

This use case provides a step-by-step example of using the identity domains REST API to authenticate users and perform multifactor enrollment and authentication with Duo Web SDK v2 or Duo Web SDK v4.
Note  
  

- Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
- This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.

The following example sets are included in this use case:
- 

[Enroll a New User with Duo Security Using Web SDK v2](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb)
- 

[Enroll a New User with Duo Security Using Web SDK v4](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb-8)
- 

[Authenticate a User Account with Duo Security Using Web SDK v2](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb)
- 

[Authenticate a User Account with Duo Security Using Web SDK v4](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb-2)
- 

[Authenticate a User with Duo Security When Used as a Backup Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb)
- 

[Set Duo Security as the Preferred Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#set-duo-sec-preferred-factor)
- 

[Support Trusted Device When Using Duo as an Authentication Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#support-trusted-device-duo-auth-factor)

### Enroll a New User with Duo Security Using Web SDK v2

This use case provides a step-by-step example of using the identity domains REST API to enroll a new user and an associated device with Duo Web SDK v2.
Note  
  

- Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
- This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.

Use the following steps for the use case. Each step contains request and response examples:
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb__sec_begin-authn-flow)
- [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_inc_rdj_mjb)
- [Step 3: Initiate Duo Security Enrollment Request](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_lzs_5z3_mjb)
- [Step 4: Initiate Duo Security Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_fnh_1wg_4jb)
- [Step 5: Submit Factor Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_bjw_51j_mjb)
- [Step 6: Create the Authentication Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_r34_kcj_mjb)
Note  
  
These steps assume that MFA is enabled and a sign-on policy is created for MFA. See[Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../mfa/configure-multi-factor-authentication-settings.htm).

#### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

#### Step 2: Submit the User's Credentials

Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

In this use case example, enrollment is sent in the next step to initiate enrollment for the user.

#### Step 3: Initiate Duo Security Enrollment Request

This step initiates Duo Security enrollment. The client must include the following attributes:
- `op`: tells the server what kind of operation the client wants
- `authFactor`: defines which authentication factor that the user wants to enroll in
- `requestState`: received in the Step 2 response

Request Example

The following example shows the contents of the POST request in JSON format:

```

```

Response Example

The following example shows the contents of the request in JSON format:

```

```

In the response, the`nextOp`values indicate what can be sent as the op value in the next request. In this use case example,`credSubmit`is sent in the next step.

#### Step 4: Initiate Duo Security Authentication

Use Duo's Web SDK v2 to integrate identity domains with Duo Security. Duo offers a JavaScript library that interacts with iFrame that's used for secondary authentication.

After primary authentication, you must pass the authentication details such as`duoSecurityHost`and`duoSecurityChallenge`that you received from identity domains to iFrame. You can use the following example to initiate the Duo security authentication and load iFrame to make a connection with the Duo Security Server.
```

```

After completing the Duo authentication process, Duo calls the`duoSecurityCallback`method to get a Duo response.
```

```

Then upon receiving the response for Duo Security, you must pass the response to identity domains to complete the authentication.

#### Step 5: Submit Factor Credentials

This step submits the factor credentials in the requestState that were received in the Step 3 response. Note that the request payload doesn't contain the authFactor attribute because the requestState contains it. The client must include the following attributes:
- `op`: tells the server what kind of operation the client wants
- `requestState`: received in the Step 3 response

Request Example

The following example shows the contents of the POST request in JSON format to submit the factor credentials:

```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

The`nextOp`values indicate what can be sent as the`op`value in the next request. In this use case example,`createToken`is sent in the next step.

#### Step 6: Create the Authentication Token
This step indicates that the client is done and needs a session created. The server validates that no other factor evaluation (depending on what is defined for the policy) is needed and responds with the token or denies access. The client must include the following attributes:
- `op`: tells the server what kind of operation the client wants
- `requestState`: received in the Step 5 response

Request Example

The following example shows the contents of the POST request in JSON format:

```

```

Response Example

The following example shows the contents of the response in JSON format:

```

```

### Enroll a New User with Duo Security Using Web SDK v4

This use case provides a step-by-step example of using the identity domains REST API to enroll a new user and an associated device with Duo Web SDK v4.

Note  
  
If you need to enable Duo Web SDK v4, see[Enabling Duo Web SDK v4](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#enabling_duo_websdk_v4).
Note  
  

- Use this Authenticate API only if you're building your own end-to-end login experience by developing a custom sign-in application to be used by identity domains.
- This Authenticate API can't be used to integrate your applications with identity domains for single sign-on purposes.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.

Use the following steps for the use case. Each step contains request and response examples:
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb__sec_begin-authn-flow)
- [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_inc_rdj_mjb)
- [Step 3: Initiate Duo Security Enrollment Request](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_lzs_5z3_mjb)
- [Step 4: Initiate Duo Security Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_fnh_1wg_4jb)
- [Step 5: Submit Factor Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_bjw_51j_mjb)
- [Step 6: Create the Authentication Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_ccb_fw3_mjb__section_r34_kcj_mjb)
Note  
  
These steps assume that MFA is enabled and a sign-on policy is created for MFA. See[Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../mfa/configure-multi-factor-authentication-settings.htm).

#### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

#### Step 2: Submit the User's Credentials

Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

In this use case example, enrollment is sent in the next step to initiate enrollment for the user.

#### Step 3: Initiate Duo Security Enrollment Request

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the request in JSON format.
```

```

#### Step 4: Initiate Duo Security Authentication

During Duo Security authentication, the browser redirects to the Duo Security Server, the Duo Security Server then loads the secondary authentication page where the user performs the secondary authentication. After successful authentication, the Duo Security Server responds with the state (duoSecurityAuthzState) and code (duoSecurityAuthzCode) parameters. These parameters must be submitted to the identity domain to complete authentication.

Use the following steps to get the state and code parameters:
- 

Get the URL to redirect to from`duoSecurityAuthzRequest`.
For example:
```

```

The is the redirect URL for`duoSecurityAuthzRedirectURL`.
- 

Do 303 Redirect to the Duo Security Server.
- 

Complete the Duo Security enrollment and authentication process.

The Duo Security Server redirects back to`duoSecurityAuthzRedirectURL`with`duoSecurityAuthzState`and`duoSecurityAuthzCode`.

#### Step 5: Submit Factor Credentials

Pass`duoSecurityAuthzState`and`duoSecurityAuthzCode`from the response to the identity domain to complete authentication.

Request Example

The following example shows the contents of the request in JSON format:
```

```

Response Example
```

```

#### Step 6: Create the Authentication Token
This step indicates that the client is done and needs a session created. The server validates that no other factor evaluation (depending on what is defined for the policy) is needed and responds with the token or denies access. The client must include the following attributes:
- `op`: tells the server what kind of operation the client wants
- `requestState`: received in the Step 5 response

Request Example

The following example shows the contents of the POST request in JSON format:

```

```

Response Example

The following example shows the contents of the response in JSON format:

```

```

### Authenticate a User Account with Duo Security Using Web SDK v2

This use case provides a step-by-step example of using the identity domains Authentication API to authenticate a user account with Duo Web SDK v2.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__sec_begin-authn-flow)
- [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__section_wz2_54k_mjb)
- [Step 3: Initiate Duo Security Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__section_jk4_gxg_4jb)
- [Step 4: Submit Factor Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__section_orw_spk_mjb)
Note  
  
These steps assume that MFA is enabled and a sign-on policy is created for MFA. See[Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../mfa/configure-multi-factor-authentication-settings.htm)

#### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

#### Step 2: Submit the User's Credentials

Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`values indicate what can be sent as the op value in the next request. In this use case example,`credSubmit`is sent in the next step.

#### Step 3: Initiate Duo Security Authentication

Use Duo's Web SDK v2 to integrate identity domains with Duo Security. Duo offers a JavaScript library that interacts with iFrame that's used for secondary authentication.

After primary authentication, you must pass the authentication details such as`duoSecurityHost`and`duoSecurityChallenge`that you received from identity domains to iFrame. You can use the following example to initiate the Duo security authentication and load iFrame to make a connection with the Duo Security Server.
```

```

After completing the Duo authentication process, Duo calls the duoSecurityCallback method to get a Duo response.
```

```

Then upon receiving the response for Duo Security, you must pass the response to identity domains to complete the authentication.

#### Step 4: Submit Factor Credentials

This step submits the factor credentials in the`requestState`that were received in the Step 2 response. Note that the request payload doesn't contain the`authFactor`attribute because the`requestState`contains it. The client must include the following attributes:
- `op`: tells the server what kind of operation the client wants
- `requestState`: received in the Step 2 response

Request Example

The following example shows the contents of the POST request in JSON format to submit the factor credentials:

```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

### Authenticate a User Account with Duo Security Using Web SDK v4

This use case provides a step-by-step example of using the identity domains Authentication API to authenticate a user account with Duo Web SDK v4.

Note  
  
If you need to enable Duo Web SDK v4, see[Enabling Duo Web SDK v4](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#enabling_duo_websdk_v4).
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__sec_begin-authn-flow)
- [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__section_wz2_54k_mjb)
- [Step 3: Initiate Duo Security Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__section_jk4_gxg_4jb)
- [Step 4: Submit Factor Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_pd1_tnk_mjb__section_orw_spk_mjb)
Note  
  
These steps assume that MFA is enabled and a sign-on policy is created for MFA. See[Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../mfa/configure-multi-factor-authentication-settings.htm).

#### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

#### Step 2: Submit the User's Credentials

Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`values indicate what can be sent as the op value in the next request. In this use case example,`credSubmit`is sent in the next step.

#### Step 3: Initiate Duo Security Authentication

During Duo Security authentication, the browser redirects to the Duo Security Server, the Duo Security Server then loads the secondary authentication page where the user performs the secondary authentication. After successful authentication, the Duo Security Server responds with the state (duoSecurityAuthzState) and code (duoSecurityAuthzCode) parameters. These parameters must be submitted to the identity domain to complete authentication.

Use the following steps to get the state and code parameters:
- 

Get the URL to redirect to from`duoSecurityAuthzRequest`.
For example:
```

```

The is the redirect URL for`duoSecurityAuthzRedirectURL`.
- 

Do 303 Redirect to the Duo Security Server.
- 

Complete the Duo Security enrollment and authentication process.

The Duo Security Server redirects back to`duoSecurityAuthzRedirectURL`with`duoSecurityAuthzState`and`duoSecurityAuthzCode`.

#### Step 4: Submit Factor Credentials

Pass`duoSecurityAuthzState`and`duoSecurityAuthzCode`from the response to the identity domain to complete authentication.

Request Example

The following example shows the contents of the request in JSON format:
```

```

Response Example
```

```

### Authenticate a User with Duo Security When Used as a Backup Factor

This use case provides a step-by-step example of using the identity domains REST API to authenticate a user account with Duo Security even when it's configured as a backup factor.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb__sec_begin-authn-flow)
- [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb__section_dby_jyp_mjb)
- [Step 3: Get the List of Backup Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb__section_rk2_dvk_mjb)
- [Step 4: Select Duo Security from the List of Backup Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#concept_dbc_1vk_mjb__section_s4j_1wk_mjb)

#### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

#### Step 2: Submit the User's Credentials

Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`values indicate what can be sent as the op value in the next request. In this use case example,`getBackupFactors`is sent in the next step.

#### Step 3: Get the List of Backup Factors

This step enables you to get the list of backup factors.

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

#### Step 4: Select Duo Security from the List of Backup Factors
Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

### Set Duo Security as the Preferred Factor

This use case provides a step-by-step example of using the identity domains REST API to set Duo Security as the preferred factor for authentication.

You can set the`preferred`flag to`true`to make Duo Security as a preferred factor, if a user already has other factor other than Duo Security as preferred.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#set-duo-sec-preferred-factor__sec_begin-authn-flow)
- [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#set-duo-sec-preferred-factor__submit-user-credentials)
- [Step 3: Initiate Duo Security Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#set-duo-sec-preferred-factor__initiate-duo-sec-auth)
- [Step 4: Enable Duo Security as the Preferred Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#set-duo-sec-preferred-factor__enable-duo-preferred-factor)

#### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

#### Step 2: Submit the User's Credentials

Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`values indicate what can be sent as the op value in the next request. In this use case example,`credSubmit`is sent in the next step.

#### Step 3: Initiate Duo Security Authentication

Use Duo's Web SDK v2 to integrate identity domains with Duo Security. Duo offers a JavaScript library that interacts with iFrame that's used for secondary authentication.

After primary authentication, you must pass the authentication details such as`duoSecurityHost`and`duoSecurityChallenge`that you received from identity domains to iFrame. You can use the following example to initiate the Duo security authentication and load iFrame to make a connection with the Duo Security Server.
```

```

After completing the Duo authentication process, Duo calls the duoSecurityCallback method to get a Duo response.
```

```

Then upon receiving the response for Duo Security, you must pass the response to identity domains to complete the authentication.

#### Step 4: Enable Duo Security as the Preferred Factor
This step enables Duo Security as the preferred factor. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

### Support Trusted Device When Using Duo as an Authentication Factor

This use case provides a step-by-step example of using the identity domains REST API to support trusted device when using Duo as an authentication factor.
Tip  
  
Download the identity domains authentication use case examples collection and the global variables file from the idcs-authn-api-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.
Use the following steps for the use case. Each step contains request and response examples:
- [Step 1: Begin the Authentication Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#support-trusted-device-duo-auth-factor__sec_begin-authn-flow)
- [Step 2: Submit the User's Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#support-trusted-device-duo-auth-factor__submit-user-cred)
- [Step 3: Initiate Duo Security Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#support-trusted-device-duo-auth-factor__initiate-duo-auth)
- [Step 4: Enable a Device as Trusted](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#support-trusted-device-duo-auth-factor__enable-device-trusted)

#### Step 1: Begin the Authentication Flow

Obtain the initial`requestState`to begin the authentication flow.

Request Example

The following example shows the request in cURL format:
```

```

Note  
  
The`appName`is optional. The`appName`is the name of the App that the client wants to access. If an`appName`is provided, sign-on policies specific to the App are processed, and the client is challenged for the required factors based on that policy.

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the`nextOp`value indicates what can be sent as the`op`value in the next request. In this use case example,`credSubmit`should be sent in the next step. The`requestState`contains contextual data needed to process the request.

#### Step 2: Submit the User's Credentials

Submit the user's credentials as the first factor, which are the username and password. For this step, the client must include the following attributes:
- 

`credentials:`username and password
- 

`requestState:`received in the Step 1 response
- 

`op:`tells the server what kind of operation the client wants

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

```

```

In the response, the`nextOp`values indicate what can be sent as the op value in the next request. In this use case example,`credSubmit`is sent in the next step.

#### Step 3: Initiate Duo Security Authentication

Use Duo's Web SDK v2 to integrate identity domains with Duo Security. Duo offers a JavaScript library that interacts with iFrame that's used for secondary authentication.

After primary authentication, you must pass the authentication details such as`duoSecurityHost`and`duoSecurityChallenge`that you received from identity domains to iFrame. You can use the following example to initiate the Duo security authentication and load iFrame to make a connection with the Duo Security Server.
```

```

After completing the Duo authentication process, Duo calls the duoSecurityCallback method to get a Duo response.
```

```

Then upon receiving the response for Duo Security, you must pass the response to identity domains to complete the authentication.

#### Step 4: Enable a Device as Trusted

This step enables a device as trusted. After the device is trusted, then MFA will not be challenged even though Duo Security is enrolled.

Request Example

The following example shows the contents of the POST request in JSON format:
```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

## Enrolling in MFA with Duo Security Using Self Service

This use case provides a step-by-step example of using the identity domains REST API for self-service enrollment in Multifactor Authentication (MFA) using Duo Security.

Download the identity domains authentication use case examples collection and the global variables file from the idcs-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.

As a prerequisite step, you must obtain a ME token before following these steps. See[Generating Access Token Using Authentication API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#GenerateAccessToken)for information on obtaining a ME token.
Complete the following steps in this use case.
- [Step1: Enroll a User with Duo Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#self-service-enroll-mfa-duo-security__section_rzh_lvq_mjb)
- [Step 2: Initiate Duo Authentication for the User](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#self-service-enroll-mfa-duo-security__section_jyr_zxq_mjb)
- [Step 3: Validate Duo Factor for Enrollment Scenario](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/use-duosec-identity-cloud-service.htm#self-service-enroll-mfa-duo-security__section_sml_ffr_mjb)
Note  
  
These steps assume that relevant factors of MFA are enabled using[Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../mfa/configure-multi-factor-authentication-settings.htm).

### Step1: Enroll a User with Duo Factor
This step initiates Duo Security enrollment in a POST request to the`/admin/v1/MyAuthenticationFactorEnroller`endpoint. The client must include the following attribute:
- `value`: defines the user id. You can make a GET call to`{{HOST}}/admin/v1/Me`to get the "id" value.

### Request Example

The following example shows the contents of the POST request body in JSON format:

```

```

### Response Example

The following example shows the contents of the response body in JSON format:

```

```

In the response, the`deviceId`and the`requestId`should be passed in the next step.

### Step 2: Initiate Duo Authentication for the User

This step initiates the authentication on the third-party side by submitting a POST request to the`/admin/v1/MyAuthenticationFactorInitiator`endpoint. The client must include the following attributes:
- `requestId:`received in the Step 1 response
- `deviceId:`received in the Step 1 response
- `userName:`username of the user

### Request Example

The following example shows the contents of the POST request body in JSON format:

```

```

### Response Example

The following example shows the contents of the response in JSON format:

```

```

In the response`deviceId`and`requestId`should be passed in the next step.

### Step 3: Validate Duo Factor for Enrollment Scenario

This step calls the third-party factor API with collected credentials to validate the enrollment of a user in a POST request to the`/admin/v1/MyAuthenticationFactorValidator`endpoint.

The client must include the following attributes:
- `requestId:`received in the Step 2 response
- `deviceId:`received in the Step 2 response

Request Example

The following example shows the contents of the POST request in JSON format:

```

```

Response Example

The following example shows the contents of the response in JSON format:
```

```

In the response, the attribute`mfaStatus:"ENROLLED"`indicates that user has enrolled for MFA. The`mfaPreferredAuthenticationFactor`attribute indicates the factor set as the preferred method. In this case, it's`THIRDPARTY`
