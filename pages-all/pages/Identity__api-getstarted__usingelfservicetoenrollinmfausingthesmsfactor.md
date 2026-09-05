# Enrolling in MFA using the SMS Factor Using Self Service
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingelfservicetoenrollinmfausingthesmsfactor.htm
- Fetched: 2026-09-05 02:18 CDT

# Enrolling in MFA using the SMS Factor Using Self Service

This use case provides a step-by-step example of using the identity domains REST API for Self-Service enrollment in Multifactor Authentication (MFA) using SMS Factor.

Download the identity domains authentication use case examples collection and the global variables file from the idcs-rest-clients folder within the[idm-samples](https://github.com/oracle-samples/idm-samples)GitHub repository and then import them into Postman.

As a prerequisite step, you must obtain a ME token before following these steps. See[Generating Access Token Using Authentication API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingauthenticateapis.htm#GenerateAccessToken)for information on obtaining a ME token.
There are three steps in this use case. Each step contains request and response examples:
- [Step 1: Create the Self Service Enrollment Using the SMS Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingelfservicetoenrollinmfausingthesmsfactor.htm#concept_rt5_rxf_ngb__title_ycs_cy3_xhb)
- [Step 2: Initiate the Self Service Enrollment Using the OTP by SMS](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingelfservicetoenrollinmfausingthesmsfactor.htm#concept_rt5_rxf_ngb__title_o3z_3y3_xhb)
- [Step 2a: Initiate the Self Service Enrollment Request to Resend OTP by SMS](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingelfservicetoenrollinmfausingthesmsfactor.htm#concept_rt5_rxf_ngb__title_cnv_brw_23b)
- [Step 3: Validate the Self Service Enrollment Using the OTP](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingelfservicetoenrollinmfausingthesmsfactor.htm#concept_rt5_rxf_ngb__title_hkk_hz3_xhb)
Note  
  
These steps assume that relevant factors of MFA are enabled using[Configure Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../mfa/configure-multi-factor-authentication-settings.htm).

## Step1: Create the Self Service Enrollment Using the SMS Factor

This step initiates SMS enrollment in a POST request to the`/admin/v1/MyAuthenticationFactorEnroller`endpoint. The client must include the following attributes:

- `value`: defines the user id. You can make a GET call to`{{HOST}}/admin/v1/Me`to get the "id" value.
- `displayName`: defines the display name for the device
- `countryCode`: defines the country code of the phone number where the SMS text will be sent
- `phoneNumber`: defines the phone number where the SMS text will be sent

## Request Example

The following example shows the contents of the POST request body in JSON format:

```

```

## Response Example

The following example shows the contents of the response body in JSON format:

```

```

In the response, the`deviceId`and the`requestId`should be passed in the next step.

## Error Response Examples
The following example shows the error message in JSON format when the`userId`is invalid. You get a 400 HTTP response code.
```

```

The following example shows the error message in JSON format if a`phoneNumber`is incorrect. You get a 400 HTTP response code.
```

```

## Step 2: Initiate the Self Service Enrollment Using the OTP by SMS

This step requests that the OTP be sent through SMS in a POST request to the`/admin/v1/MyAuthenticationFactorInitiator`endpoint. The client must include the following attributes:

`requestId:`received in the Step 1 response

`deviceId:`received in the Step 1 response

`userName:`username of the user

## Request Example

The following example shows the contents of the POST request body in JSON format:

```

```

## Response Example

The following example shows the contents of the response in JSON format:

```

```

An OTP code is sent by using SMS to the user's mobile device. In the response`deviceId`and`requestId`should be passed in the next step.

## 2a. Initiate the Self Service Enrollment Request to Resend OTP by SMS

In case the user wants the server to "resend" the OTP, then same payload as mentioned in the[Step 2](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/usingelfservicetoenrollinmfausingthesmsfactor.htm#concept_rt5_rxf_ngb__section_xnc_3y5_ngb)should be sent to the server again.

## Request Example

The following example shows the contents of the POST request body in JSON format:

```

```

## Response Example

The following example shows the contents of the response in JSON format:

```

```

An OTP code is sent using SMS to the user's mobile device. In the response`deviceId`and`requestId`should be passed in the next step.

## Step 3: Validate the Self Service Enrollment Using the OTP

This step validates the SMS enrollment of a user in a POST request to the`/admin/v1/MyAuthenticationFactorValidator`endpoint.

The client must include the following attributes:

- `otpCode:`the code received by the user on their device
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

In the response, the attribute`mfaStaus:"ENROLLED"`indicates that user has enrolled for MFA. The`mfapreferredAuthenticationFactor`attribute indicates the factor set as the preferred method. In this case, it's SMS.
Note  
  
This value may be different, if the first enrolled factor is different from SMS.

## Error Response Examples

The following example shows the error message in JSON format if OTP is incorrect. You get a 401 HTTP response code and the enrollment fails.
```

```
