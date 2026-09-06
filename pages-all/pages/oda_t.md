# ODA Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#dcoc-content-body)

## ODA Common Types

### DBMS_CLOUD_OCI_ODA_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_CHANNEL_T Type

Properties of a Channel.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the Channel was created.

`name`

(required) The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`description`

(optional) A short description of the Channel.

`category`

(required) The category of the Channel.

Allowed values are: 'AGENT', 'APPLICATION', 'BOT', 'BOT_AS_AGENT', 'SYSTEM', 'EVENT'

`l_type`

(required) The Channel type.

Allowed values are: 'ANDROID', 'APPEVENT', 'APPLICATION', 'CORTANA', 'FACEBOOK', 'IOS', 'MSTEAMS', 'OSS', 'OSVC', 'SERVICECLOUD', 'SLACK', 'TEST', 'TWILIO', 'WEB', 'WEBHOOK'

`session_expiry_duration_in_milliseconds`

(optional) The number of milliseconds before a session expires.

`lifecycle_state`

(required) The Channel's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_ANDROID_CHANNEL_T Type

The configuration for an Android channel.

Syntax
```

```

`dbms_cloud_oci_oda_android_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`max_token_expiration_time_in_minutes`

(optional) The maximum time until the token expires (in minutes).

`is_client_authentication_enabled`

(required) Whether client authentication is enabled or not.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_APP_EVENT_CHANNEL_T Type

The configuration for an Application Event channel.

Syntax
```

```

`dbms_cloud_oci_oda_app_event_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`outbound_url`

(optional) The URL for sending errors and responses to.

`event_sink_bot_ids`

(optional) The IDs of the Skills and Digital Assistants that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_APPLICATION_CHANNEL_T Type

The configuration for an Application channel.

Syntax
```

```

`dbms_cloud_oci_oda_application_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`outbound_url`

(optional) The URL to send response and error messages to.

`is_authenticated_user_id`

(required) True if the user id in the AIC message should be treated as an authenticated user id.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_AUTHENTICATION_PROVIDER_T Type

Settings for the Authentication Provider.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the Authentication Provider was created.

`grant_type`

(required) The grant type for the Authentication Provider.

Allowed values are: 'CLIENT_CREDENTIALS', 'AUTHORIZATION_CODE'

`identity_provider`

(required) Which type of Identity Provider (IDP) you are using.

Allowed values are: 'GENERIC', 'OAM', 'GOOGLE', 'MICROSOFT'

`name`

(required) A name to identify the Authentication Provider.

`token_endpoint_url`

(required) The IDPs URL for requesting access tokens.

`authorization_endpoint_url`

(optional) The IDPs URL for the page that users authenticate with by entering the user name and password.

`short_authorization_code_request_url`

(optional) A shortened version of the authorization URL, which you can get from a URL shortener service (one that allows you to send query parameters). You might need this because the generated authorization-code-request URL could be too long for SMS and older smart phones.

`revoke_token_endpoint_url`

(optional) If you want to revoke all the refresh tokens and access tokens of the logged-in user from a dialog flow, then you need the IDP's revoke refresh token URL. If you provide this URL, then you can use the System.OAuth2ResetTokens component to revoke the user's tokens for this service.

`client_id`

(required) The client ID for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration. With Microsoft identity platform, use the application ID.

`scopes`

(required) A space-separated list of the scopes that must be included when Digital Assistant requests an access token from the provider. Include all the scopes that are required to access the resources. If refresh tokens are enabled, include the scope that’s necessary to get the refresh token (typically offline_access).

`subject_claim`

(optional) The access-token profile claim to use to identify the user.

`refresh_token_retention_period_in_days`

(optional) The number of days to keep the refresh token in the Digital Assistant cache.

`redirect_url`

(optional) The OAuth Redirect URL.

`is_visible`

(required) Whether this Authentication Provider is visible in the ODA UI.

`lifecycle_state`

(required) The Authentication Provider's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_AUTHENTICATION_PROVIDER_SUMMARY_T Type

Summary of the Authentication Provider.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the Authentication Provider was created.

`grant_type`

(required) The grant type for the Authentication Provider.

Allowed values are: 'CLIENT_CREDENTIALS', 'AUTHORIZATION_CODE'

`identity_provider`

(required) Which type of Identity Provider (IDP) you are using.

Allowed values are: 'GENERIC', 'OAM', 'GOOGLE', 'MICROSOFT'

`name`

(required) A name to identify the Authentication Provider.

`lifecycle_state`

(required) The Authentication Provider's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_AUTHENTICATION_PROVIDER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_oda_authentication_provider_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_AUTHENTICATION_PROVIDER_COLLECTION_T Type

A collection of Authentication Provider summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The Authentication Provider summaries.

### DBMS_CLOUD_OCI_ODA_BOT_T Type

Metadata for a Bot resource.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the resource was created.

`name`

(required) The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`version`

(required) The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces. The version must begin with a letter or a number.

`display_name`

(required) The resource's display name.

`category`

(optional) The resource's category. This is used to group resource's together.

`description`

(optional) A short description of the resource.

`namespace`

(optional) The resource's namespace.

`lifecycle_state`

(required) The resource's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(required) The resource's publish state.

Allowed values are: 'PUBLISHED', 'DRAFT'

`platform_version`

(required) The ODA Platform Version for this resource.

`base_id`

(optional) The unique identifier for the base reource (when this resource extends another).

`multilingual_mode`

(optional) The multilingual mode for the resource.

Allowed values are: 'NATIVE', 'TRANSLATION'

`primary_language_tag`

(optional) The primary language for the resource.

`native_language_tags`

(optional) A list of native languages supported by this resource.

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_CHANGE_ODA_INSTANCE_COMPARTMENT_DETAILS_T Type

Properties required to move a Digital Assistant instance from one compartment to another.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) Identifier of the compartment into which the Digital Assistant instance should be moved.

### DBMS_CLOUD_OCI_ODA_CHANGE_ODA_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type

Properties required to move an ODA Private Endpoint from one compartment to another.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that the ODA private endpoint belongs to.

### DBMS_CLOUD_OCI_ODA_CHANNEL_SUMMARY_T Type

Summary of the Channel.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the Channel was created.

`name`

(required) The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`description`

(optional) A short description of the Channel.

`category`

(required) The category of the Channel.

Allowed values are: 'AGENT', 'APPLICATION', 'BOT', 'BOT_AS_AGENT', 'SYSTEM', 'EVENT'

`l_type`

(required) The Channel type.

Allowed values are: 'ANDROID', 'APPEVENT', 'APPLICATION', 'CORTANA', 'FACEBOOK', 'IOS', 'MSTEAMS', 'OSS', 'OSVC', 'SERVICECLOUD', 'SLACK', 'TEST', 'TWILIO', 'WEB', 'WEBHOOK'

`lifecycle_state`

(required) The Channel's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_CHANNEL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_oda_channel_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_CHANNEL_COLLECTION_T Type

A collection of Channel summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The Channel summaries.

### DBMS_CLOUD_OCI_ODA_CREATE_DIGITAL_ASSISTANT_DETAILS_T Type

Properties that are required to create a Digital Assistant.

Syntax
```

```

Fields

Field Description

`kind`

(required) How to create the Digital Assistant.

Allowed values are: 'NEW', 'CLONE', 'VERSION', 'EXTEND'

`category`

(optional) The resource's category. This is used to group resource's together.

`description`

(optional) A short description of the resource.

`platform_version`

(optional) The ODA Platform Version for this resource.

`multilingual_mode`

(optional) The multilingual mode for the resource.

Allowed values are: 'NATIVE', 'TRANSLATION'

`primary_language_tag`

(optional) The primary language for the resource.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_CLONE_DIGITAL_ASSISTANT_DETAILS_T Type

Properties that are required to create a new Digital Assistant by cloning an existing Digital Assistant.

Syntax
```

```

`dbms_cloud_oci_oda_clone_digital_assistant_details_t`is a subtype of the`dbms_cloud_oci_oda_create_digital_assistant_details_t`type.

Fields

Field Description

`id`

(required) The unique identifier of the Digital Assistant to clone.

`name`

(required) The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`display_name`

(required) The resource's display name.

`version`

(optional) The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces. The version must begin with a letter or a number.

### DBMS_CLOUD_OCI_ODA_CREATE_SKILL_DETAILS_T Type

Properties that are required to create a Skill.

Syntax
```

```

Fields

Field Description

`kind`

(required) How to create the Skill.

Allowed values are: 'NEW', 'CLONE', 'VERSION', 'EXTEND'

`category`

(optional) The resource's category. This is used to group resource's together.

`description`

(optional) A short description of the resource.

`platform_version`

(optional) The ODA Platform Version for this resource.

`multilingual_mode`

(optional) The multilingual mode for the resource.

Allowed values are: 'NATIVE', 'TRANSLATION'

`primary_language_tag`

(optional) The primary language for the resource.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_CLONE_SKILL_DETAILS_T Type

Properties that are required to create a new Skill by cloning an existing Skill.

Syntax
```

```

`dbms_cloud_oci_oda_clone_skill_details_t`is a subtype of the`dbms_cloud_oci_oda_create_skill_details_t`type.

Fields

Field Description

`id`

(required) The unique identifier of the Skill to clone.

`name`

(required) The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`display_name`

(required) The resource's display name.

`version`

(optional) The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces. The version must begin with a letter or a number.

### DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_PARAMETER_VALUE_T Type

Properties for configuring a Parameter in a Digital Assistant instance.

Syntax
```

```

Fields

Field Description

`name`

(required) The Parameter name. This must be unique within the parent resource.

`l_type`

(required) The value type.

Allowed values are: 'STRING', 'INTEGER', 'FLOAT', 'BOOLEAN', 'SECURE'

`value`

(required) The current value. The value will be interpreted based on the `type`.

### DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_PARAMETER_VALUE_TBL Type

Nested table type of dbms_cloud_oci_oda_digital_assistant_parameter_value_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_CONFIGURE_DIGITAL_ASSISTANT_PARAMETERS_DETAILS_T Type

Properties for configuring the Digital Assistant Parameters in a Digital Assistant instance.

Syntax
```

```

Fields

Field Description

`parameters`

(required) The values to use to configure the Digital Assistant Parameters.

### DBMS_CLOUD_OCI_ODA_CORTANA_CHANNEL_T Type

The configuration for a Cortana channel.

Syntax
```

```

`dbms_cloud_oci_oda_cortana_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`msa_app_id`

(required) The Microsoft App ID that you obtained when you created your bot registration in Azure.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_CREATE_CHANNEL_DETAILS_T Type

Properties that are required to create a Channel.

Syntax
```

```

Fields

Field Description

`name`

(required) The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`description`

(optional) A short description of the Channel.

`l_type`

(required) The Channel type.

Allowed values are: 'ANDROID', 'APPEVENT', 'APPLICATION', 'CORTANA', 'FACEBOOK', 'IOS', 'MSTEAMS', 'OSS', 'OSVC', 'SERVICECLOUD', 'SLACK', 'TEST', 'TWILIO', 'WEB', 'WEBHOOK'

`session_expiry_duration_in_milliseconds`

(optional) The number of milliseconds before a session expires.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_CREATE_ANDROID_CHANNEL_DETAILS_T Type

Properties required to create an Android channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_android_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`max_token_expiration_time_in_minutes`

(optional) The maximum time until the token expires (in minutes).

`is_client_authentication_enabled`

(required) Whether client authentication is enabled or not.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_CHANNEL_RESULT_T Type

Properties of a Channel.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the Channel was created.

`name`

(required) The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`description`

(optional) A short description of the Channel.

`category`

(required) The category of the Channel.

Allowed values are: 'AGENT', 'APPLICATION', 'BOT', 'BOT_AS_AGENT', 'SYSTEM', 'EVENT'

`l_type`

(required) The Channel type.

Allowed values are: 'ANDROID', 'APPEVENT', 'APPLICATION', 'CORTANA', 'FACEBOOK', 'IOS', 'MSTEAMS', 'OSS', 'OSVC', 'SERVICECLOUD', 'SLACK', 'TEST', 'TWILIO', 'WEB', 'WEBHOOK'

`session_expiry_duration_in_milliseconds`

(optional) The number of milliseconds before a session expires.

`lifecycle_state`

(required) The Channel's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_CREATE_ANDROID_CHANNEL_RESULT_T Type

The configuration for an Android channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_android_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`secret_key`

(required) The secret key used to verify the authenticity of received messages. This is only returned this once. If it is lost the keys will need to be rotated to generate a new key.

`max_token_expiration_time_in_minutes`

(optional) The maximum time until the token expires (in minutes).

`is_client_authentication_enabled`

(required) Whether client authentication is enabled or not.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_APP_EVENT_CHANNEL_DETAILS_T Type

Properties required to create an Application Event channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_app_event_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`outbound_url`

(optional) The URL for sending errors and responses to.

`event_sink_bot_ids`

(optional) The IDs of the Skills and Digital Assistants that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_APP_EVENT_CHANNEL_RESULT_T Type

The configuration for an Application Event channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_app_event_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`secret_key`

(required) The secret key used to verify the authenticity of received messages. This is only returned this once. If it is lost the keys will need to be rotated to generate a new key.

`outbound_url`

(required) The URL for sending errors and responses to.

`event_sink_bot_ids`

(optional) The IDs of the Skills and Digital Assistants that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_CREATE_APPLICATION_CHANNEL_DETAILS_T Type

Properties required to create an Application channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_application_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`outbound_url`

(optional) The URL to send response and error messages to.

`is_authenticated_user_id`

(required) True if the user id in the AIC message should be treated as an authenticated user id.

### DBMS_CLOUD_OCI_ODA_CREATE_APPLICATION_CHANNEL_RESULT_T Type

The configuration for an Application channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_application_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`secret_key`

(required) The secret key used to verify the authenticity of received messages. This is only returned this once. If it is lost the keys will need to be rotated to generate a new key.

`outbound_url`

(optional) The URL to send response and error messages to.

`is_authenticated_user_id`

(required) True if the user id in the AIC message should be treated as an authenticated user id.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_CREATE_AUTHENTICATION_PROVIDER_DETAILS_T Type

Properties required to create a new Authentication Provider.

Syntax
```

```

Fields

Field Description

`grant_type`

(required) The grant type for the Authentication Provider.

Allowed values are: 'CLIENT_CREDENTIALS', 'AUTHORIZATION_CODE'

`identity_provider`

(required) Which type of Identity Provider (IDP) you are using.

Allowed values are: 'GENERIC', 'OAM', 'GOOGLE', 'MICROSOFT'

`name`

(required) A name to identify the Authentication Provider.

`token_endpoint_url`

(required) The IDPs URL for requesting access tokens.

`authorization_endpoint_url`

(optional) The IDPs URL for the page that users authenticate with by entering the user name and password.

`short_authorization_code_request_url`

(optional) A shortened version of the authorization URL, which you can get from a URL shortener service (one that allows you to send query parameters). You might need this because the generated authorization-code-request URL could be too long for SMS and older smart phones.

`revoke_token_endpoint_url`

(optional) If you want to revoke all the refresh tokens and access tokens of the logged-in user from a dialog flow, then you need the IDP's revoke refresh token URL. If you provide this URL, then you can use the System.OAuth2ResetTokens component to revoke the user's tokens for this service.

`client_id`

(required) The client ID for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration. With Microsoft identity platform, use the application ID.

`client_secret`

(required) The client secret for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration. With Microsoft identity platform, use the application secret.

`scopes`

(required) A space-separated list of the scopes that must be included when Digital Assistant requests an access token from the provider. Include all the scopes that are required to access the resources. If refresh tokens are enabled, include the scope that’s necessary to get the refresh token (typically offline_access).

`subject_claim`

(optional) The access-token profile claim to use to identify the user.

`refresh_token_retention_period_in_days`

(optional) The number of days to keep the refresh token in the Digital Assistant cache.

`redirect_url`

(optional) The OAuth Redirect URL.

`is_visible`

(optional) Whether this Authentication Provider is visible in the ODA UI.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_CREATE_CORTANA_CHANNEL_DETAILS_T Type

Properties required to create a Cortana channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_cortana_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`msa_app_id`

(required) The Microsoft App ID that you obtained when you created your bot registration in Azure.

`msa_app_password`

(required) The client secret that you obtained from your bot registration.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_CORTANA_CHANNEL_RESULT_T Type

The configuration for a Cortana channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_cortana_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`msa_app_id`

(required) The Microsoft App ID that you obtained when you created your bot registration in Azure.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_CREATE_DIGITAL_ASSISTANT_VERSION_DETAILS_T Type

Properties that are required to create a new version of an existing Digital Assistant.

Syntax
```

```

`dbms_cloud_oci_oda_create_digital_assistant_version_details_t`is a subtype of the`dbms_cloud_oci_oda_create_digital_assistant_details_t`type.

Fields

Field Description

`id`

(required) The unique identifier of the Digital Assistant to create a new version of.

`version`

(required) The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces. The version must begin with a letter or a number.

### DBMS_CLOUD_OCI_ODA_CREATE_FACEBOOK_CHANNEL_DETAILS_T Type

Properties required to create a Facebook channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_facebook_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`app_secret`

(required) The app secret for your Facebook app.

`page_access_token`

(required) The page access token that you generated for your Facebook page.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_FACEBOOK_CHANNEL_RESULT_T Type

The configuration for a Facebook channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_facebook_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`verify_token`

(required) The Facebook verify token. This is used by Facebook when verifying the webhook channel. This is only returned this once. If it is lost the keys will need to be rotated to generate a new verify token.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_CREATE_IMPORTED_PACKAGE_DETAILS_T Type

Payload for creating an imported package

Syntax
```

```

Fields

Field Description

`current_package_id`

(required) ID of the package to import.

`parameter_values`

(optional) A list of parameter values to use when importing the given package. Must match those defined in the import contract.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_CREATE_IOS_CHANNEL_DETAILS_T Type

Properties required to create an iOS channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_ios_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`max_token_expiration_time_in_minutes`

(optional) The maximum time until the token expires (in minutes).

`is_client_authentication_enabled`

(required) Whether client authentication is enabled or not.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_IOS_CHANNEL_RESULT_T Type

The configuration for an iOS channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_ios_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`secret_key`

(required) The secret key used to verify the authenticity of received messages. This is only returned this once. If it is lost the keys will need to be rotated to generate a new key.

`max_token_expiration_time_in_minutes`

(optional) The maximum time until the token expires (in minutes).

`is_client_authentication_enabled`

(required) Whether client authentication is enabled or not.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_MS_TEAMS_CHANNEL_DETAILS_T Type

Properties required to create an MS Teams channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_ms_teams_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`msa_app_id`

(required) The Microsoft App ID that you obtained when you created your bot registration in Azure.

`msa_app_password`

(required) The client secret that you obtained from your bot registration.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_MS_TEAMS_CHANNEL_RESULT_T Type

The configuration for an MS Teams channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_ms_teams_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`msa_app_id`

(required) The Microsoft App ID that you obtained when you created your bot registration in Azure.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_CREATE_NEW_DIGITAL_ASSISTANT_DETAILS_T Type

Properties that are required to create a Digital Assistant from scratch.

Syntax
```

```

`dbms_cloud_oci_oda_create_new_digital_assistant_details_t`is a subtype of the`dbms_cloud_oci_oda_create_digital_assistant_details_t`type.

Fields

Field Description

`name`

(required) The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`display_name`

(required) The resource's display name.

`version`

(optional) The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces. The version must begin with a letter or a number.

`native_language_tags`

(optional) A list of native languages supported by this resource.

### DBMS_CLOUD_OCI_ODA_CREATE_NEW_SKILL_DETAILS_T Type

Properties that are required to create a Skill from scratch.

Syntax
```

```

`dbms_cloud_oci_oda_create_new_skill_details_t`is a subtype of the`dbms_cloud_oci_oda_create_skill_details_t`type.

Fields

Field Description

`name`

(required) The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`display_name`

(required) The resource's display name.

`version`

(required) The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces. The version must begin with a letter or a number.

`native_language_tags`

(optional) A list of native languages supported by this resource.

### DBMS_CLOUD_OCI_ODA_CREATE_OSS_CHANNEL_DETAILS_T Type

Properties required to create an Oracle Streaming Service (OSS) channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_oss_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`event_sink_bot_ids`

(optional) The IDs of the Skills and Digital Assistants that the Channel is routed to.

`inbound_message_topic`

(required) The topic inbound messages are received on.

`outbound_message_topic`

(required) The topic outbound messages are sent on.

`bootstrap_servers`

(required) The Oracle Streaming Service bootstrap servers.

`security_protocol`

(required) The security protocol to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.

`sasl_mechanism`

(required) The SASL mechanmism to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.

`tenancy_name`

(required) The tenancy to use when connecting to the Oracle Streaming Service.

`user_name`

(required) The user name to use when connecting to the Oracle Streaming Service.

`stream_pool_id`

(required) The stream pool OCI to use when connecting to the Oracle Streaming Service.

`auth_token`

(required) The authentication token to use when connecting to the Oracle Streaming Service.

### DBMS_CLOUD_OCI_ODA_CREATE_OSS_CHANNEL_RESULT_T Type

The configuration for an Oracle Streaming Service (OSS) channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_oss_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`event_sink_bot_ids`

(optional) The IDs of the Skills and Digital Assistants that the Channel is routed to.

`inbound_message_topic`

(required) The topic inbound messages are received on.

`outbound_message_topic`

(required) The topic outbound messages are sent on.

`bootstrap_servers`

(required) The Oracle Streaming Service bootstrap servers.

`security_protocol`

(required) The security protocol to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.

`sasl_mechanism`

(required) The SASL mechanmism to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.

`tenancy_name`

(required) The tenancy to use when connecting to the Oracle Streaming Service.

`user_name`

(required) The user name to use when connecting to the Oracle Streaming Service.

`stream_pool_id`

(required) The stream pool OCI to use when connecting to the Oracle Streaming Service.

### DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_ATTACHMENT_OWNER_T Type

Details about an attachment owner

Syntax
```

```

Fields

Field Description

`owner_service_name`

(required) Name of the owner service principal

`owner_service_tenancy`

(required) Tenancy OCID of the owner service principal

### DBMS_CLOUD_OCI_ODA_CREATE_ODA_INSTANCE_ATTACHMENT_DETAILS_T Type

Properties required to create an ODA instance attachment.

Syntax
```

```

Fields

Field Description

`attach_to_id`

(required) The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which this ODA instance is being attached.

`attachment_type`

(required) The type of target instance which this ODA instance is being attached.

Allowed values are: 'FUSION'

`attachment_metadata`

(optional) Attachment specific metadata. Defined by the target service.

`restricted_operations`

(optional) List of operations that are restricted while this instance is attached.

`owner`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_CREATE_ODA_INSTANCE_DETAILS_T Type

Properties that are required to create a Digital Assistant instance.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) User-friendly name for the instance. Avoid entering confidential information. You can change this value anytime.

`description`

(optional) Description of the Digital Assistant instance.

`compartment_id`

(required) Identifier of the compartment.

`shape_name`

(required) Shape or size of the instance.

Allowed values are: 'DEVELOPMENT', 'PRODUCTION'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_role_based_access`

(optional) Should this Digital Assistant instance use role-based authorization via an identity domain (true) or use the default policy-based authorization via IAM policies (false)

`identity_domain`

(optional) If isRoleBasedAccess is set to true, this property specifies the identity domain that is to be used to implement this type of authorzation. Digital Assistant will create an Identity Application instance and Application Roles within this identity domain. The caller may then perform and user roll mappings they like to grant access to users within the identity domain.

### DBMS_CLOUD_OCI_ODA_CREATE_ODA_PRIVATE_ENDPOINT_ATTACHMENT_DETAILS_T Type

Properties that are required to create an ODA private endpoint attachment.

Syntax
```

```

Fields

Field Description

`oda_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the attached ODA Instance.

`oda_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ODA Private Endpoint.

### DBMS_CLOUD_OCI_ODA_CREATE_ODA_PRIVATE_ENDPOINT_DETAILS_T Type

Properties that can be specified to create an ODA private endpoint.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) User-defined name for the ODA private endpoint. Avoid entering confidential information. You can change this value.

`description`

(optional) Description of the ODA private endpoint.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that the ODA private endpoint belongs to.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet that the private endpoint belongs to.

`nsg_ids`

(optional) List of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of[network security groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_SCAN_LISTENER_INFO_T Type

Customer's Real Application Cluster (RAC)'s SCAN listener FQDN, port or list IPs and their ports.

Syntax
```

```

Fields

Field Description

`scan_listener_fqdn`

(optional) FQDN of the customer's Real Application Cluster (RAC)'s SCAN listeners.

`scan_listener_ip`

(optional) A SCAN listener's IP of the customer's Real Application Cluster (RAC).

`scan_listener_port`

(optional) The port that customer's Real Application Cluster (RAC)'s SCAN listeners are listening on.

### DBMS_CLOUD_OCI_ODA_SCAN_LISTENER_INFO_TBL Type

Nested table type of dbms_cloud_oci_oda_scan_listener_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_CREATE_ODA_PRIVATE_ENDPOINT_SCAN_PROXY_DETAILS_T Type

Properties that are required to create an ODA Private Endpoint Scan Proxy.

Syntax
```

```

Fields

Field Description

`scan_listener_type`

(required) Type indicating whether Scan listener is specified by its FQDN or list of IPs

`protocol`

(required) The protocol used for communication between client, scanProxy and RAC's scan listeners

`scan_listener_infos`

(required) The FQDN/IPs and port information of customer's Real Application Cluster (RAC)'s SCAN listeners.

### DBMS_CLOUD_OCI_ODA_CREATE_OSVC_CHANNEL_DETAILS_T Type

Properties required to create an OSVC channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_osvc_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`host`

(required) The host. For OSVC, you can derive these values from the URL that you use to launch the Agent Browser User Interface or the chat launch page. For example, if the URL is https://sitename.exampledomain.com/app/chat/chat_launch, then the host is sitename.exampledomain.com. For FUSION, this is the host portion of your Oracle Applications Cloud (Fusion) instance's URL. For example: sitename.exampledomain.com.

`port`

(required) The port.

`user_name`

(required) The user name for the digital-assistant agent.

`password`

(required) The password for the digital-assistant agent.

`total_session_count`

(required) The total session count.

`channel_service`

(optional) The type of OSVC service.

Allowed values are: 'OSVC', 'FUSION'

`authentication_provider_name`

(required) The name of the Authentication Provider to use to authenticate the user.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_OSVC_CHANNEL_RESULT_T Type

The configuration for an OSVC channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_osvc_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`host`

(required) The host. For OSVC, you can derive these values from the URL that you use to launch the Agent Browser User Interface or the chat launch page. For example, if the URL is https://sitename.exampledomain.com/app/chat/chat_launch, then the host is sitename.exampledomain.com. For FUSION, this is the host portion of your Oracle Applications Cloud (Fusion) instance's URL. For example: sitename.exampledomain.com.

`port`

(required) The port.

`user_name`

(required) The user name for the digital-assistant agent.

`total_session_count`

(required) The total session count.

`channel_service`

(required) The type of OSVC service.

Allowed values are: 'OSVC', 'FUSION'

`authentication_provider_name`

(required) The name of the Authentication Provider to use to authenticate the user.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_SERVICE_CLOUD_CHANNEL_DETAILS_T Type

Properties required to create an Service Cloud channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_service_cloud_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`domain_name`

(required) The domain name. If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com. If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.

`host_name_prefix`

(required) The host prefix. If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com. If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.

`user_name`

(required) The user name for an Oracle B2C Service staff member who has the necessary profile permissions.

`password`

(required) The password for the Oracle B2C Service staff member who has the necessary profile permissions.

`client_type`

(required) The type of Service Cloud client.

Allowed values are: 'WSDL', 'REST'

### DBMS_CLOUD_OCI_ODA_CREATE_SERVICE_CLOUD_CHANNEL_RESULT_T Type

The configuration for a Service Cloud agent channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_service_cloud_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`domain_name`

(required) The domain name. If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com. If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.

`host_name_prefix`

(required) The host prefix. If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com. If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.

`user_name`

(required) The user name for an Oracle B2C Service staff member who has the necessary profile permissions.

`client_type`

(required) The type of Service Cloud client.

Allowed values are: 'WSDL', 'REST'

### DBMS_CLOUD_OCI_ODA_CREATE_SKILL_PARAMETER_DETAILS_T Type

Properties that are required to create a Skill Parameter.

Syntax
```

```

Fields

Field Description

`name`

(required) The Parameter name. This must be unique within the parent resource.

`display_name`

(required) The display name for the Parameter.

`description`

(optional) A description of the Parameter.

`l_type`

(required) The value type.

Allowed values are: 'STRING', 'INTEGER', 'FLOAT', 'BOOLEAN', 'SECURE'

`value`

(required) The current value. The value will be interpreted based on the `type`.

### DBMS_CLOUD_OCI_ODA_CREATE_SKILL_VERSION_DETAILS_T Type

Properties that are required to create a new version of an existing Skill.

Syntax
```

```

`dbms_cloud_oci_oda_create_skill_version_details_t`is a subtype of the`dbms_cloud_oci_oda_create_skill_details_t`type.

Fields

Field Description

`id`

(required) The unique identifier of the Skill to create a new version of.

`version`

(required) The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces. The version must begin with a letter or a number.

### DBMS_CLOUD_OCI_ODA_CREATE_SLACK_CHANNEL_DETAILS_T Type

Properties required to create a Slack channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_slack_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`client_id`

(required) The Slack Client Id for the Slack app.

`auth_success_url`

(optional) The URL to redirect to when authentication is successful.

`auth_error_url`

(optional) The URL to redirect to when authentication is unsuccessful.

`signing_secret`

(required) The Signing Secret for the Slack App.

`client_secret`

(required) The Client Secret for the Slack App.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_SLACK_CHANNEL_RESULT_T Type

The configuration for a Slack channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_slack_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`client_id`

(required) The Slack Client Id for the Slack app.

`auth_success_url`

(optional) The URL to redirect to when authentication is successful.

`auth_error_url`

(optional) The URL to redirect to when authentication is unsuccessful.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_CREATE_TEST_CHANNEL_RESULT_T Type

The configuration for the Test channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_test_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`secret_key`

(optional) The secret key used to verify the authenticity of received messages. This is only returned this once. If it is lost the keys will need to be rotated to generate a new key.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_CREATE_TRANSLATOR_DETAILS_T Type

Properties that are required to create a Translator.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The Translation Service to use for this Translator.

Allowed values are: 'GOOGLE', 'MICROSOFT'

`base_url`

(required) The base URL for invoking the Translation Service.

`auth_token`

(required) The authentication token to use when invoking the Translation Service

`properties`

(optional) Properties used when invoking the translation service. Each property is a simple key-value pair.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_CREATE_TWILIO_CHANNEL_DETAILS_T Type

Properties required to create a Twilio channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_twilio_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`account_sid`

(required) The Account SID for the Twilio number.

`phone_number`

(required) The Twilio phone number.

`auth_token`

(required) The Auth Token for the Twilio number.

`is_mms_enabled`

(required) Whether MMS is enabled for this channel or not.

`original_connectors_url`

(optional) The original connectors URL (used for backward compatibility).

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_TWILIO_CHANNEL_RESULT_T Type

The configuration for a Twilio channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_twilio_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`account_sid`

(required) The Account SID for the Twilio number.

`phone_number`

(required) The Twilio phone number.

`is_mms_enabled`

(required) Whether MMS is enabled for this channel or not.

`original_connectors_url`

(optional) The original connectors URL (used for backward compatibility).

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_CREATE_WEB_CHANNEL_DETAILS_T Type

Properties required to create a Web channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_web_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`max_token_expiration_time_in_minutes`

(optional) The maximum time until the token expires (in minutes).

`is_client_authentication_enabled`

(required) Whether client authentication is enabled or not.

`allowed_domains`

(optional) A comma-delimited whitelist of allowed domains. The channel will only communicate with the sites from the domains that you add to this list. For example, *.corp.example.com, *.hdr.example.com. Entering a single asterisk (*) allows unrestricted access to the channel from any domain. Typically, you'd only enter a single asterisk during development. For production, you would add an allowlist of domains.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_WEB_CHANNEL_RESULT_T Type

The configuration for a Web channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_web_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`secret_key`

(required) The secret key used to verify the authenticity of received messages. This is only returned this once. If it is lost the keys will need to be rotated to generate a new key.

`max_token_expiration_time_in_minutes`

(optional) The maximum time until the token expires (in minutes).

`is_client_authentication_enabled`

(required) Whether client authentication is enabled or not.

`allowed_domains`

(optional) A comma-delimited whitelist of allowed domains. The channel will only communicate with the sites from the domains that you add to this list. For example, *.corp.example.com, *.hdr.example.com. Entering a single asterisk (*) allows unrestricted access to the channel from any domain. Typically, you'd only enter a single asterisk during development. For production, you would add an allowlist of domains.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_WEBHOOK_CHANNEL_DETAILS_T Type

Properties required to create a Webhook channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_webhook_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_details_t`type.

Fields

Field Description

`outbound_url`

(required) The URL to send responses to.

`payload_version`

(required) The version for payloads.

Allowed values are: '1.0', '1.1'

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_CREATE_WEBHOOK_CHANNEL_RESULT_T Type

The configuration for a Webhook channel.

Syntax
```

```

`dbms_cloud_oci_oda_create_webhook_channel_result_t`is a subtype of the`dbms_cloud_oci_oda_create_channel_result_t`type.

Fields

Field Description

`secret_key`

(required) The secret key used to verify the authenticity of received messages. This is only returned this once. If it is lost the keys will need to be rotated to generate a new key.

`outbound_url`

(required) The URL to send responses to.

`payload_version`

(required) The version for payloads.

Allowed values are: '1.0', '1.1'

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_RESOURCE_TYPE_DEFAULT_PARAMETER_VALUES_T Type

Default values needed to import a resource type for a package.

Syntax
```

```

Fields

Field Description

`resource_type`

(required) The type of resource to which these resourceType-specific parameter values apply

`parameter_values`

(required) A list of parameter values used to import the package.

### DBMS_CLOUD_OCI_ODA_RESOURCE_TYPE_DEFAULT_PARAMETER_VALUES_TBL Type

Nested table type of dbms_cloud_oci_oda_resource_type_default_parameter_values_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_DEFAULT_PARAMETER_VALUES_T Type

Default values for parameters required to import a package

Syntax
```

```

Fields

Field Description

`resource_types_default_parameter_values`

(optional) A list of resource type specific default parameter values, one set for each resource type listed in the package definition.

### DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_T Type

Digital Assistant metadata.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the resource was created.

`name`

(required) The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`version`

(required) The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces. The version must begin with a letter or a number.

`display_name`

(required) The resource's display name.

`category`

(optional) The resource's category. This is used to group resource's together.

`description`

(optional) A short description of the resource.

`namespace`

(optional) The resource's namespace.

`lifecycle_state`

(required) The resource's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(required) The resource's publish state.

Allowed values are: 'PUBLISHED', 'DRAFT'

`platform_version`

(required) The ODA Platform Version for this resource.

`base_id`

(optional) The unique identifier for the base reource (when this resource extends another).

`multilingual_mode`

(optional) The multilingual mode for the resource.

Allowed values are: 'NATIVE', 'TRANSLATION'

`primary_language_tag`

(optional) The primary language for the resource.

`native_language_tags`

(optional) A list of native languages supported by this resource.

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_SUMMARY_T Type

Summary of a Digital Assistant.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the resource was created.

`name`

(required) The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`version`

(required) The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces. The version must begin with a letter or a number.

`display_name`

(required) The resource's display name.

`namespace`

(required) The resource's namespace.

`category`

(required) The resource's category. This is used to group resource's together.

`lifecycle_state`

(required) The resource's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(required) The resource's publish state.

Allowed values are: 'PUBLISHED', 'DRAFT'

`platform_version`

(required) The ODA Platform Version for this resource.

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_oda_digital_assistant_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_COLLECTION_T Type

A collection of Digital Assistant summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The Digital Assistant summaries.

### DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_PARAMETER_T Type

Metadata for a Digital Assistant Parameter.

Syntax
```

```

Fields

Field Description

`name`

(required) The Parameter name. This must be unique within the parent resource.

`display_name`

(required) The display name for the Parameter.

`description`

(optional) A description of the Parameter.

`l_type`

(required) The value type.

Allowed values are: 'STRING', 'INTEGER', 'FLOAT', 'BOOLEAN', 'SECURE'

`value`

(required) The current value. The value will be interpreted based on the `type`.

`lifecycle_state`

(required) The Parameter's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_PARAMETER_SUMMARY_T Type

Metadata for a Digital Assistant Parameter property.

Syntax
```

```

Fields

Field Description

`name`

(required) The Parameter name. This must be unique within the parent resource.

`display_name`

(required) The display name for the Parameter.

`description`

(optional) A description of the Parameter.

`l_type`

(required) The value type.

Allowed values are: 'STRING', 'INTEGER', 'FLOAT', 'BOOLEAN', 'SECURE'

`value`

(optional) The current value. The value will be interpreted based on the `type`.

`lifecycle_state`

(required) The Parameter's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_PARAMETER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_oda_digital_assistant_parameter_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_PARAMETER_COLLECTION_T Type

A collection of Digital Assistant Parameter summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The Digital Assistant Parameter summaries.

### DBMS_CLOUD_OCI_ODA_ERROR_BODY_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, which is useful for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_ODA_STORAGE_LOCATION_T Type

Properties that point to a specific object in Object Storage.

Syntax
```

```

Fields

Field Description

`region_id`

(required) The region id.

`compartment_id`

(required) The unique identifier for the compartment.

`namespace_name`

(required) The Object Storage namespace.

`bucket_name`

(required) The name of the bucket.

`object_name`

(required) The name of the object.

### DBMS_CLOUD_OCI_ODA_EXPORT_BOT_DETAILS_T Type

Properties to export a Bot to Object Storage.

Syntax
```

```

Fields

Field Description

`target`

(required)

### DBMS_CLOUD_OCI_ODA_EXPORT_DIGITAL_ASSISTANT_DETAILS_T Type

Properties that specify where in Object Storage to export the Digital Assistant to.

Syntax
```

```

Fields

Field Description

`target`

(required)

### DBMS_CLOUD_OCI_ODA_EXPORT_SKILL_DETAILS_T Type

Properties that specify where in Object Storage to export the Skill to.

Syntax
```

```

Fields

Field Description

`target`

(required)

### DBMS_CLOUD_OCI_ODA_EXTEND_DIGITAL_ASSISTANT_DETAILS_T Type

Properties that are required to create a new Digital Assistant by extending an existing Digital Assistant.

Syntax
```

```

`dbms_cloud_oci_oda_extend_digital_assistant_details_t`is a subtype of the`dbms_cloud_oci_oda_create_digital_assistant_details_t`type.

Fields

Field Description

`id`

(required) The unique identifier of the Digital Assistant to extend.

`name`

(required) The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`display_name`

(required) The resource's display name.

`version`

(optional) The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces. The version must begin with a letter or a number.

### DBMS_CLOUD_OCI_ODA_EXTEND_SKILL_DETAILS_T Type

Properties that are required to create a new Skill by extending an existing Skill.

Syntax
```

```

`dbms_cloud_oci_oda_extend_skill_details_t`is a subtype of the`dbms_cloud_oci_oda_create_skill_details_t`type.

Fields

Field Description

`id`

(required) The unique identifier of the Skill to extend.

`name`

(required) The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`display_name`

(required) The resource's display name.

`version`

(optional) The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces. The version must begin with a letter or a number.

### DBMS_CLOUD_OCI_ODA_FACEBOOK_CHANNEL_T Type

The configuration for a Facebook channel.

Syntax
```

```

`dbms_cloud_oci_oda_facebook_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_IMPORT_BOT_DETAILS_T Type

Properties to import a Bot resource from Object Storage.

Syntax
```

```

Fields

Field Description

`source`

(required)

### DBMS_CLOUD_OCI_ODA_PARAMETER_DEFINITION_T Type

A parameter to a resource.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the parameter

`l_type`

(required) Enumerated parameter type.

Allowed values are: 'STRING', 'URI', 'URL', 'NUMBER', 'BOOLEAN'

`description`

(optional) Description of the parameter.

`is_required`

(optional) Is this parameter required. Ignored for parameters with direction = OUTPUT.

`is_sensitive`

(optional) Is the data for this parameter sensitive (e.g. should the data be hidden in UI, encrypted if stored, etc.)

`default_value`

(optional) Default value for the parameter.

`min_length`

(optional) Used for character string types such as STRING to constrain the length of the value

`max_length`

(optional) Used for character string types such as STRING to constrain the length of the value

`pattern`

(optional) Regular expression used to validate the value of a string type such as STRING

`direction`

(optional) Is this parameter an input parameter, output parameter, or both?

Allowed values are: 'INPUT', 'OUTPUT'

`ui_placement_hint`

(optional) A forward-slash-delimited 'path' in an imaginary hierarchy, at which this parameter's UI widgets should be placed

`resource_type_metadata`

(optional) Any configuration needed to help the resource type process this parameter (e.g. link to manifest, etc.).

### DBMS_CLOUD_OCI_ODA_PARAMETER_DEFINITION_TBL Type

Nested table type of dbms_cloud_oci_oda_parameter_definition_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_RESOURCE_TYPE_IMPORT_CONTRACT_T Type

The contract guiding the import experience for the consumer and behavior of the resource provider for a single resourceType.

Syntax
```

```

Fields

Field Description

`resource_type`

(required) The type of resource to which this resourceType-specific contract applies

`parameters`

(required) A list of definitions for parameters that are required to import this package into a target instance.

### DBMS_CLOUD_OCI_ODA_RESOURCE_TYPE_IMPORT_CONTRACT_TBL Type

Nested table type of dbms_cloud_oci_oda_resource_type_import_contract_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_IMPORT_CONTRACT_T Type

The contract guiding the import experience for the consumer and behavior of the resource providers for all resource types in a package.

Syntax
```

```

Fields

Field Description

`import_contract`

(optional) A list of resource type specific import contracts, one for each resource type listed in the package definition.

### DBMS_CLOUD_OCI_ODA_IMPORTED_PACKAGE_T Type

An imported/instantiated package within an instance.

Syntax
```

```

Fields

Field Description

`oda_instance_id`

(required) ID of the host instance.

`current_package_id`

(required) ID of the package.

`name`

(required) Stable name of the package (the same across versions).

`display_name`

(required) Display name of the package (can change across versions).

`version`

(required) version of the package.

`status`

(required) Status of the imported package.

Allowed values are: 'READY', 'OPERATION_PENDING', 'FAILED'

`time_created`

(required) When the imported package was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the imported package was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`status_message`

(required) Short message explaining the status of this imported package.

`parameter_values`

(required) A list of parameter values used to import the package.

### DBMS_CLOUD_OCI_ODA_IMPORTED_PACKAGE_SUMMARY_T Type

A summary of an imported/instantiated package within an instance.

Syntax
```

```

Fields

Field Description

`oda_instance_id`

(required) ID of the host instance.

`current_package_id`

(required) ID of the package.

`name`

(required) Stable name of the package (the same across versions).

`display_name`

(required) Display name of the package (can change across versions).

`version`

(required) version of the package.

`status`

(required) Status of the imported package.

`time_created`

(required) When the imported package was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the imported package was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_IOS_CHANNEL_T Type

The configuration for an iOS channel.

Syntax
```

```

`dbms_cloud_oci_oda_ios_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`max_token_expiration_time_in_minutes`

(optional) The maximum time until the token expires (in minutes).

`is_client_authentication_enabled`

(required) Whether client authentication is enabled or not.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_MS_TEAMS_CHANNEL_T Type

The configuration for an MS Teams channel.

Syntax
```

```

`dbms_cloud_oci_oda_ms_teams_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`msa_app_id`

(required) The Microsoft App ID that you obtained when you created your bot registration in Azure.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_METADATA_PROPERTY_T Type

Property to describe and object.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of property.

`value`

(required) Value for the property.

### DBMS_CLOUD_OCI_ODA_OSS_CHANNEL_T Type

The configuration for an Oracle Streaming Service (OSS) channel.

Syntax
```

```

`dbms_cloud_oci_oda_oss_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`event_sink_bot_ids`

(optional) The IDs of the Skills and Digital Assistants that the Channel is routed to.

`inbound_message_topic`

(required) The topic inbound messages are received on.

`outbound_message_topic`

(required) The topic outbound messages are sent on.

`bootstrap_servers`

(required) The Oracle Streaming Service bootstrap servers.

`security_protocol`

(required) The security protocol to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.

`sasl_mechanism`

(required) The SASL mechanmism to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.

`tenancy_name`

(required) The tenancy to use when connecting to the Oracle Streaming Service.

`user_name`

(required) The user name to use when connecting to the Oracle Streaming Service.

`stream_pool_id`

(required) The stream pool OCI to use when connecting to the Oracle Streaming Service.

### DBMS_CLOUD_OCI_ODA_RESTRICTED_OPERATION_T Type

Summary of a restricted operation for a Digital Assistant instance.

Syntax
```

```

Fields

Field Description

`operation_name`

(required) Name of the restricted operation.

`restricting_service`

(required) Name of the service restricting the operation.

### DBMS_CLOUD_OCI_ODA_RESTRICTED_OPERATION_TBL Type

Nested table type of dbms_cloud_oci_oda_restricted_operation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_T Type

Description of `OdaServiceInstance` object.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the instance was created.

`display_name`

(optional) User-defined name for the Digital Assistant instance. Avoid entering confidential information. You can change this value.

`description`

(optional) Description of the Digital Assistant instance.

`compartment_id`

(required) Identifier of the compartment that the instance belongs to.

`shape_name`

(required) Shape or size of the instance.

Allowed values are: 'DEVELOPMENT', 'PRODUCTION'

`web_app_url`

(optional) URL for the Digital Assistant web application that's associated with the instance.

`connector_url`

(optional) URL for the connector's endpoint.

`time_created`

(optional) When the Digital Assistant instance was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(optional) When the Digital Assistance instance was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`lifecycle_state`

(optional) The current state of the Digital Assistant instance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_sub_state`

(optional) The current sub-state of the Digital Assistant instance.

Allowed values are: 'CREATING', 'STARTING', 'STOPPING', 'CHANGING_COMPARTMENT', 'ACTIVATING_CUSTOMER_ENCRYPTION_KEY', 'UPDATING_CUSTOMER_ENCRYPTION_KEY', 'DEACTIVATING_CUSTOMER_ENCRYPTION_KEY', 'DELETING', 'DELETE_PENDING', 'RECOVERING', 'UPDATING', 'PURGING', 'QUEUED'

`state_message`

(optional) A message that describes the current state in more detail. For example, actionable information about an instance that's in the `FAILED` state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_role_based_access`

(optional) Should this Digital Assistant instance use role-based authorization via an identity domain (true) or use the default policy-based authorization via IAM policies (false)

`identity_domain`

(optional) If isRoleBasedAccess is set to true, this property specifies the identity domain that is to be used to implement this type of authorzation. Digital Assistant will create an Identity Application instance and Application Roles within this identity domain. The caller may then perform and user roll mappings they like to grant access to users within the identity domain.

`identity_app_guid`

(optional) If isRoleBasedAccess is set to true, this property specifies the GUID of the Identity Application instance Digital Assistant has created inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this Digital Assistant instance for users within the identity domain.

`identity_app_console_url`

(optional) If isRoleBasedAccess is set to true, this property specifies the URL for the administration console used to manage the Identity Application instance Digital Assistant has created inside the user-specified identity domain.

`imported_package_names`

(optional) A list of package names imported into this instance (if any). Use importedPackageIds field to get the details of the imported packages.

`imported_package_ids`

(optional) A list of package ids imported into this instance (if any). Use GetImportedPackage to get the details of the imported packages.

`attachment_types`

(optional) A list of attachment types for this instance (if any). Use attachmentIds to get the details of the attachments.

`attachment_ids`

(optional) A list of attachment identifiers for this instance (if any). Use GetOdaInstanceAttachment to get the details of the attachments.

`restricted_operations`

(optional) A list of restricted operations (across all attachments) for this instance (if any). Use GetOdaInstanceAttachment to get the details of the attachments.

### DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_OWNER_T Type

Details about an ODA instance owner

Syntax
```

```

Fields

Field Description

`owner_service_name`

(required) Name of the owner service principal

`owner_service_tenancy`

(required) Tenancy OCID of the owner service principal

### DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_ATTACHMENT_T Type

Description of an ODA instance attachment.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the ODA instance attachment was created.

`instance_id`

(required) The OCID of the ODA instance to which the attachment applies.

`attach_to_id`

(required) The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which the ODA instance is or is being attached.

`attachment_type`

(required) The type of attachment defined as an enum.

Allowed values are: 'FUSION'

`attachment_metadata`

(optional) Attachment-specific metadata, defined by the target service.

`restricted_operations`

(optional) List of operation names that are restricted while this ODA instance is attached.

`owner`

(optional)

`time_created`

(optional) The time the attachment was created. An RFC3339 formatted datetime string

`time_last_update`

(optional) The time the attachment was last modified. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the attachment.

Allowed values are: 'ATTACHING', 'ACTIVE', 'DETACHING', 'INACTIVE', 'FAILED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_ATTACHMENT_SUMMARY_T Type

Description of an ODA instance attachment.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the ODA instance attachment was created.

`instance_id`

(required) The OCID of the ODA instance to which the attachment applies.

`attach_to_id`

(required) The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which the ODA instance is or is being attached.

`attachment_type`

(required) The type of attachment defined as an enum.

Allowed values are: 'FUSION'

`attachment_metadata`

(optional) Attachment-specific metadata, defined by the target service.

`restricted_operations`

(optional) List of operation names that are restricted while this ODA instance is attached.

`owner`

(optional)

`time_created`

(optional) The time the attachment was created. An RFC3339 formatted datetime string

`time_last_update`

(optional) The time the attachment was last modified. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the attachment.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_ATTACHMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_oda_oda_instance_attachment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_ATTACHMENT_COLLECTION_T Type

Results of a Oda instance attachment search. Contains OdaInstanceAttachment items.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Oda instance attachments.

### DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_SUMMARY_T Type

Summary of the Digital Assistant instance.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier of the Digital Assistant instance.

`display_name`

(optional) User-defined name for the Digital Assistant instance. You can change this value.

`description`

(optional) Description of the Digital Assistant instance.

`compartment_id`

(required) Identifier of the compartment that the instance belongs to.

`shape_name`

(optional) Shape or size of the instance.

Allowed values are: 'DEVELOPMENT', 'PRODUCTION'

`time_created`

(optional) When the Digital Assistant instance was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(optional) When the Digital Assistant instance was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`lifecycle_state`

(required) The current state of the instance.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_sub_state`

(optional) The current sub-state of the Digital Assistant instance.

Allowed values are: 'CREATING', 'STARTING', 'STOPPING', 'CHANGING_COMPARTMENT', 'ACTIVATING_CUSTOMER_ENCRYPTION_KEY', 'UPDATING_CUSTOMER_ENCRYPTION_KEY', 'DEACTIVATING_CUSTOMER_ENCRYPTION_KEY', 'DELETING', 'DELETE_PENDING', 'RECOVERING', 'UPDATING', 'PURGING', 'QUEUED'

`state_message`

(optional) A message describing the current state in more detail. For example, actionable information about an instance that's in the `FAILED` state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_role_based_access`

(optional) Should this Digital Assistant instance use role-based authorization via an identity domain (true) or use the default policy-based authorization via IAM policies (false)

`identity_domain`

(optional) If isRoleBasedAccess is set to true, this property specifies the identity domain that is to be used to implement this type of authorzation. Digital Assistant will create an Identity Application instance and Application Roles within this identity domain. The caller may then perform and user roll mappings they like to grant access to users within the identity domain.

`imported_package_names`

(optional) A list of package names imported into this instance (if any).

`attachment_types`

(optional) A list of attachment types for this instance (if any).

### DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_T Type

A private endpoint allows Digital Assistant Instance to access resources in a customer's virtual cloud network (VCN).

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)that was assigned when the ODA private endpoint was created.

`display_name`

(required) User-defined name for the ODA private endpoint. Avoid entering confidential information. You can change this value.

`description`

(optional) Description of the ODA private endpoint.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that the ODA private endpoint belongs to.

`time_created`

(optional) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(optional) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`lifecycle_state`

(optional) The current state of the ODA private endpoint.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet that the private endpoint belongs to.

`nsg_ids`

(optional) List of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of[network security groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_ATTACHMENT_T Type

ODA Private Endpoint Attachment is used to attach ODA Private Endpoint to ODA (Digital Assistant) Instance.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ODA Private Endpoint Attachment.

`oda_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the attached ODA Instance.

`oda_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ODA Private Endpoint.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that the ODA private endpoint attachment belongs to.

`lifecycle_state`

(required) The current state of the ODA Private Endpoint attachment.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(optional) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_ATTACHMENT_SUMMARY_T Type

Summary of the ODA private endpoint attachment.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ODA Private Endpoint Attachment.

`oda_instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the attached ODA Instance.

`oda_private_endpoint_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ODA Private Endpoint.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that the ODA private endpoint attachment belongs to.

`lifecycle_state`

(required) The current state of the ODA Private Endpoint attachment.

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(optional) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_ATTACHMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_oda_oda_private_endpoint_attachment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_ATTACHMENT_COLLECTION_T Type

A collection of ODA Private Endpoint Attachment summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The ODA Private Endpoint Attachment summaries.

### DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_SUMMARY_T Type

Summary of the ODA private endpoint.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)that was assigned when the ODA private endpoint was created.

`display_name`

(optional) User-defined name for the ODA private endpoint. Avoid entering confidential information. You can change this value.

`description`

(optional) Description of the ODA private endpoint.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that the ODA private endpoint belongs to.

`time_created`

(optional) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(optional) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`lifecycle_state`

(required) The current state of the ODA private endpoint.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_oda_oda_private_endpoint_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_COLLECTION_T Type

A collection of ODA Private Endpoint summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The ODA Private Endpoint summaries.

### DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_SCAN_PROXY_T Type

Details pertaining to a scan proxy instance created for a scan listener FQDN/IPs

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ODA Private Endpoint Scan Proxy.

`scan_listener_type`

(required) Type indicating whether Scan listener is specified by its FQDN or list of IPs

Allowed values are: 'FQDN', 'IP'

`protocol`

(required) The protocol used for communication between client, scanProxy and RAC's scan listeners

Allowed values are: 'TCP'

`scan_listener_infos`

(required) The FQDN/IPs and port information of customer's Real Application Cluster (RAC)'s SCAN listeners.

`lifecycle_state`

(optional) The current state of the ODA Private Endpoint Scan Proxy.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(optional) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_SCAN_PROXY_SUMMARY_T Type

Details pertaining to a scan proxy instance created for a scan listener FQDN/IPs

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ODA Private Endpoint Scan Proxy.

`scan_listener_type`

(required) Type indicating whether Scan listener is specified by its FQDN or list of IPs

`protocol`

(required) The protocol used for communication between client, scanProxy and RAC's scan listeners

`scan_listener_infos`

(required) The FQDN/IPs and port information of customer's Real Application Cluster (RAC)'s SCAN listeners.

`lifecycle_state`

(optional) The current state of the ODA Private Endpoint Scan Proxy.

`time_created`

(optional) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_SCAN_PROXY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_oda_oda_private_endpoint_scan_proxy_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_SCAN_PROXY_COLLECTION_T Type

A collection of ODA Private Endpoint Scan Proxy summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The ODA Private Endpoint Scan Proxy summaries.

### DBMS_CLOUD_OCI_ODA_OSVC_CHANNEL_T Type

The configuration for an OSVC channel.

Syntax
```

```

`dbms_cloud_oci_oda_osvc_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`host`

(required) The host. For OSVC, you can derive these values from the URL that you use to launch the Agent Browser User Interface or the chat launch page. For example, if the URL is https://sitename.exampledomain.com/app/chat/chat_launch, then the host is sitename.exampledomain.com. For FUSION, this is the host portion of your Oracle Applications Cloud (Fusion) instance's URL. For example: sitename.exampledomain.com.

`port`

(required) The port.

`user_name`

(required) The user name for the digital-assistant agent.

`total_session_count`

(required) The total session count.

`channel_service`

(required) The type of OSVC service.

Allowed values are: 'OSVC', 'FUSION'

`authentication_provider_name`

(required) The name of the Authentication Provider to use to authenticate the user.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_METADATA_PROPERTY_TBL Type

Nested table type of dbms_cloud_oci_oda_metadata_property_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_RESOURCE_TYPE_METADATA_T Type

Describes resources of a given type within a package.

Syntax
```

```

Fields

Field Description

`resource_type`

(optional) The type of the resource described by this metadata object.

`properties`

(optional) Any properties needed to describe the content and its usage for this resource type, and within the containing package.

### DBMS_CLOUD_OCI_ODA_RESOURCE_TYPE_METADATA_TBL Type

Nested table type of dbms_cloud_oci_oda_resource_type_metadata_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_PACKAGE_T Type

Details of `Package` object.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the Package was registered.

`publisher_id`

(required) ID of the publisher providing the package.

`name`

(required) Name of package.

`display_name`

(required) Display name for the package (displayed in UI and user-facing applications).

`version`

(required) Version of the package.

`time_uploaded`

(required) When the package was uploaded. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_published`

(required) When the package was last published. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`description`

(required) Description of the package.

`resource_types`

(required) A list of resource types describing the content of the package.

`resource_types_metadata`

(required) A map of resource type to metadata key/value map that further describes the content for the resource types in this package.. Keys are resource type names, values are a map of name/value pairs per resource type.

`publisher_metadata`

(required) A map of metadata key/value pairs that further describes the publisher and the platform in which the package might be used.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`import_contract`

(required)

`default_parameter_values`

(required)

### DBMS_CLOUD_OCI_ODA_PACKAGE_SUMMARY_T Type

Summary of `Package` object.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the Package was registered.

`publisher_id`

(required) ID of the publisher providing the package.

`name`

(required) Name of package.

`display_name`

(required) Display name for the package (displayed in UI and user-facing applications).

`version`

(required) Version of the package.

`time_published`

(required) When the package was last published. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`description`

(required) Description of the package.

`resource_types`

(required) A list of resource types describing the content of the package.

`resource_types_metadata`

(required) A map of resource type to metadata key/value map that further describes the content for the resource types in this package.. Keys are resource type names, values are a map of name/value pairs per resource type.

`publisher_metadata`

(required) A map of metadata key/value pairs that further describes the publisher and the platform in which the package might be used.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_PARAMETER_T Type

Metadata for a Parameter.

Syntax
```

```

Fields

Field Description

`name`

(required) The Parameter name. This must be unique within the parent resource.

`display_name`

(required) The display name for the Parameter.

`description`

(optional) A description of the Parameter.

`l_type`

(required) The value type.

Allowed values are: 'STRING', 'INTEGER', 'FLOAT', 'BOOLEAN', 'SECURE'

`value`

(required) The current value. The value will be interpreted based on the `type`.

`lifecycle_state`

(required) The Parameter's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_ODA_SERVICE_CLOUD_CHANNEL_T Type

The configuration for a Service Cloud agent channel.

Syntax
```

```

`dbms_cloud_oci_oda_service_cloud_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`domain_name`

(required) The domain name. If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com. If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.

`host_name_prefix`

(required) The host prefix. If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com. If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.

`user_name`

(required) The user name for an Oracle B2C Service staff member who has the necessary profile permissions.

`client_type`

(required) The type of Service Cloud client.

Allowed values are: 'WSDL', 'REST'

### DBMS_CLOUD_OCI_ODA_SKILL_T Type

Skill metadata.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the resource was created.

`name`

(required) The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`version`

(required) The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces. The version must begin with a letter or a number.

`display_name`

(required) The resource's display name.

`category`

(optional) The resource's category. This is used to group resource's together.

`description`

(optional) A short description of the resource.

`namespace`

(optional) The resource's namespace.

`lifecycle_state`

(required) The resource's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(required) The resource's publish state.

Allowed values are: 'PUBLISHED', 'DRAFT'

`platform_version`

(required) The ODA Platform Version for this resource.

`base_id`

(optional) The unique identifier for the base reource (when this resource extends another).

`multilingual_mode`

(optional) The multilingual mode for the resource.

Allowed values are: 'NATIVE', 'TRANSLATION'

`primary_language_tag`

(optional) The primary language for the resource.

`native_language_tags`

(optional) A list of native languages supported by this resource.

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_SKILL_SUMMARY_T Type

Summary of a Skill.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the resource was created.

`name`

(required) The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`version`

(required) The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces. The version must begin with a letter or a number.

`display_name`

(required) The resource's display name.

`namespace`

(required) The resource's namespace.

`category`

(required) The resource's category. This is used to group resource's together.

`lifecycle_state`

(required) The resource's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(required) The resource's publish state.

Allowed values are: 'PUBLISHED', 'DRAFT'

`platform_version`

(required) The ODA Platform Version for this resource.

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_SKILL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_oda_skill_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_SKILL_COLLECTION_T Type

A collection of Skill summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The Skill summaries.

### DBMS_CLOUD_OCI_ODA_SKILL_PARAMETER_T Type

Metadata for a Skill Parameter.

Syntax
```

```

Fields

Field Description

`name`

(required) The Parameter name. This must be unique within the parent resource.

`display_name`

(required) The display name for the Parameter.

`description`

(optional) A description of the Parameter.

`l_type`

(required) The value type.

Allowed values are: 'STRING', 'INTEGER', 'FLOAT', 'BOOLEAN', 'SECURE'

`value`

(required) The current value. The value will be interpreted based on the `type`.

`lifecycle_state`

(required) The Parameter's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_ODA_SKILL_PARAMETER_SUMMARY_T Type

Metadata for a Skill Parameter property.

Syntax
```

```

Fields

Field Description

`name`

(required) The Parameter name. This must be unique within the parent resource.

`display_name`

(required) The display name for the Parameter.

`description`

(optional) A description of the Parameter.

`l_type`

(required) The value type.

Allowed values are: 'STRING', 'INTEGER', 'FLOAT', 'BOOLEAN', 'SECURE'

`value`

(optional) The current value. The value will be interpreted based on the `type`.

`lifecycle_state`

(required) The Parameter's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_ODA_SKILL_PARAMETER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_oda_skill_parameter_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_SKILL_PARAMETER_COLLECTION_T Type

A collection of Skill Parameter summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The Skill Parameter summaries.

### DBMS_CLOUD_OCI_ODA_SLACK_CHANNEL_T Type

The configuration for a Slack channel.

Syntax
```

```

`dbms_cloud_oci_oda_slack_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`client_id`

(required) The Slack Client Id for the Slack app.

`auth_success_url`

(optional) The URL to redirect to when authentication is successful.

`auth_error_url`

(optional) The URL to redirect to when authentication is unsuccessful.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_TEST_CHANNEL_T Type

The configuration for the Test channel.

Syntax
```

```

`dbms_cloud_oci_oda_test_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_TRANSLATOR_T Type

The properties for a Translator.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the Translator was created.

`l_type`

(required) The Translation Service to use for this Translator.

Allowed values are: 'GOOGLE', 'MICROSOFT'

`name`

(required) The descriptive name for this Translator.

`base_url`

(required) The base URL for invoking the Translation Service.

`lifecycle_state`

(required) The Translator's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`properties`

(optional) Properties used when invoking the translation service. Each property is a simple key-value pair.

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_TRANSLATOR_SUMMARY_T Type

Summary of the Translator.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique immutable identifier that was assigned when the Translator was created.

`l_type`

(required) The Translation Service to use for this Translator.

Allowed values are: 'GOOGLE', 'MICROSOFT'

`name`

(required) The descriptive name for this Translator.

`lifecycle_state`

(required) The Translator's current state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) When the resource was created. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_updated`

(required) When the resource was last updated. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_TRANSLATOR_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_oda_translator_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_TRANSLATOR_COLLECTION_T Type

A collection of Translator summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The Translator summaries.

### DBMS_CLOUD_OCI_ODA_TWILIO_CHANNEL_T Type

The configuration for a Twilio channel.

Syntax
```

```

`dbms_cloud_oci_oda_twilio_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`account_sid`

(required) The Account SID for the Twilio number.

`phone_number`

(required) The Twilio phone number.

`is_mms_enabled`

(required) Whether MMS is enabled for this channel or not.

`original_connectors_url`

(optional) The original connectors URL (used for backward compatibility).

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_UPDATE_CHANNEL_DETAILS_T Type

Properties to update a Channel.

Syntax
```

```

Fields

Field Description

`name`

(optional) The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.

`description`

(optional) A short description of the Channel.

`l_type`

(required) The Channel type.

Allowed values are: 'ANDROID', 'APPEVENT', 'APPLICATION', 'CORTANA', 'FACEBOOK', 'IOS', 'MSTEAMS', 'OSS', 'OSVC', 'SERVICECLOUD', 'SLACK', 'TEST', 'TWILIO', 'WEB', 'WEBHOOK'

`session_expiry_duration_in_milliseconds`

(optional) The number of milliseconds before a session expires.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_UPDATE_ANDROID_CHANNEL_DETAILS_T Type

Properties to update an Android channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_android_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`max_token_expiration_time_in_minutes`

(optional) The maximum time until the token expires (in minutes).

`is_client_authentication_enabled`

(optional) Whether client authentication is enabled or not.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_UPDATE_APP_EVENT_CHANNEL_DETAILS_T Type

Properties to update an Application Event channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_app_event_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`outbound_url`

(optional) The URL for sending errors and responses to.

`event_sink_bot_ids`

(optional) The IDs of the Skills and Digital Assistants that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_UPDATE_APPLICATION_CHANNEL_DETAILS_T Type

Properties to update an Application channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_application_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`outbound_url`

(optional) The URL to send response and error messages to.

`is_authenticated_user_id`

(optional) True if the user id in the AIC message should be treated as an authenticated user id.

### DBMS_CLOUD_OCI_ODA_UPDATE_AUTHENTICATION_PROVIDER_DETAILS_T Type

Properties to update an Authentication Provider.

Syntax
```

```

Fields

Field Description

`token_endpoint_url`

(optional) The IDPs URL for requesting access tokens.

`authorization_endpoint_url`

(optional) The IDPs URL for the page that users authenticate with by entering the user name and password.

`short_authorization_code_request_url`

(optional) A shortened version of the authorization URL, which you can get from a URL shortener service (one that allows you to send query parameters). You might need this because the generated authorization-code-request URL could be too long for SMS and older smart phones.

`revoke_token_endpoint_url`

(optional) If you want to revoke all the refresh tokens and access tokens of the logged-in user from a dialog flow, then you need the IDP's revoke refresh token URL. If you provide this URL, then you can use the System.OAuth2ResetTokens component to revoke the user's tokens for this service.

`client_id`

(optional) The client ID for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration. With Microsoft identity platform, use the application ID.

`client_secret`

(optional) The client secret for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration. With Microsoft identity platform, use the application secret.

`scopes`

(optional) A space-separated list of the scopes that must be included when Digital Assistant requests an access token from the provider. Include all the scopes that are required to access the resources. If refresh tokens are enabled, include the scope that’s necessary to get the refresh token (typically offline_access).

`subject_claim`

(optional) The access-token profile claim to use to identify the user.

`refresh_token_retention_period_in_days`

(optional) The number of days to keep the refresh token in the Digital Assistant cache.

`redirect_url`

(optional) The OAuth Redirect URL.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_UPDATE_CORTANA_CHANNEL_DETAILS_T Type

Properties to update a Cortana channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_cortana_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`msa_app_id`

(optional) The Microsoft App ID that you obtained when you created your bot registration in Azure.

`msa_app_password`

(optional) The client secret that you obtained from your bot registration.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_UPDATE_DIGITAL_ASSISTANT_DETAILS_T Type

Properties to update a Digital Assistant.

Syntax
```

```

Fields

Field Description

`category`

(optional) The resource's category. This is used to group resource's together.

`description`

(optional) A short description of the resource.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_UPDATE_DIGITAL_ASSISTANT_PARAMETER_DETAILS_T Type

Properties to update a Digital Assistant Parameter.

Syntax
```

```

Fields

Field Description

`value`

(required) The current value. The value will be interpreted based on the `type`.

### DBMS_CLOUD_OCI_ODA_UPDATE_FACEBOOK_CHANNEL_DETAILS_T Type

Properties to update a Facebook channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_facebook_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`app_secret`

(optional) The app secret for your Facebook app.

`page_access_token`

(optional) The page access token that you generated for your Facebook page.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_UPDATE_IMPORTED_PACKAGE_DETAILS_T Type

Payload for updating an imported package

Syntax
```

```

Fields

Field Description

`current_package_id`

(required) ID of the new package (i.e. version) to import, replacing the old imported package. Leave null if no new package resources are required. The name of the new package must must match the name of the already-imported package.

`parameter_values`

(required) A list of the updated parameter values to apply to this imported package.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_UPDATE_IOS_CHANNEL_DETAILS_T Type

Properties to update an iOS channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_ios_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`max_token_expiration_time_in_minutes`

(optional) The maximum time until the token expires (in minutes).

`is_client_authentication_enabled`

(optional) Whether client authentication is enabled or not.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_UPDATE_MS_TEAMS_CHANNEL_DETAILS_T Type

Properties to update an MS Teams channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_ms_teams_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`msa_app_id`

(optional) The Microsoft App ID that you obtained when you created your bot registration in Azure.

`msa_app_password`

(optional) The client secret that you obtained from your bot registration.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_UPDATE_OSS_CHANNEL_DETAILS_T Type

Properties to update an Oracle Streaming Service (OSS) channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_oss_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`event_sink_bot_ids`

(optional) The IDs of the Skills and Digital Assistants that the Channel is routed to.

`inbound_message_topic`

(optional) The topic inbound messages are received on.

`outbound_message_topic`

(optional) The topic outbound messages are sent on.

`bootstrap_servers`

(optional) The Oracle Streaming Service bootstrap servers.

`security_protocol`

(optional) The security protocol to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.

`sasl_mechanism`

(optional) The SASL mechanmism to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.

`tenancy_name`

(optional) The tenancy to use when connecting to the Oracle Streaming Service.

`user_name`

(optional) The user name to use when connecting to the Oracle Streaming Service.

`stream_pool_id`

(optional) The stream pool OCI to use when connecting to the Oracle Streaming Service.

`auth_token`

(optional) The authentication token to use when connecting to the Oracle Streaming Service.

### DBMS_CLOUD_OCI_ODA_UPDATE_ODA_INSTANCE_ATTACHMENT_DETAILS_T Type

ODA attachment details to be updated.

Syntax
```

```

Fields

Field Description

`attachment_metadata`

(required) Attachment specific metadata. Defined by the target service.

`restricted_operations`

(required) List of operations that are restricted while this instance is attached.

`owner`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_UPDATE_ODA_INSTANCE_DETAILS_T Type

The Digital Assistant instance information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) User-friendly name for the Digital Assistant instance.

`description`

(optional) Description of the Digital Assistant instance.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_UPDATE_ODA_PRIVATE_ENDPOINT_DETAILS_T Type

The ODA Private Endpoint information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) User-defined name for the ODA private endpoint. Avoid entering confidential information. You can change this value.

`description`

(optional) Description of the ODA private endpoint.

`nsg_ids`

(optional) List of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of[network security groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_UPDATE_OSVC_CHANNEL_DETAILS_T Type

Properties required to update an OSVC channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_osvc_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`host`

(optional) The host. For OSVC, you can derive these values from the URL that you use to launch the Agent Browser User Interface or the chat launch page. For example, if the URL is https://sitename.exampledomain.com/app/chat/chat_launch, then the host is sitename.exampledomain.com. For FUSION, this is the host portion of your Oracle Applications Cloud (Fusion) instance's URL. For example: sitename.exampledomain.com.

`port`

(optional) The port.

`user_name`

(optional) The user name for the digital-assistant agent.

`password`

(optional) The password for the digital-assistant agent.

`total_session_count`

(optional) The total session count.

`channel_service`

(optional) The type of OSVC service.

Allowed values are: 'OSVC', 'FUSION'

`authentication_provider_name`

(optional) The name of the Authentication Provider to use to authenticate the user.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_UPDATE_SERVICE_CLOUD_CHANNEL_DETAILS_T Type

Properties to update a Service Cloud agent channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_service_cloud_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`domain_name`

(optional) The domain name. If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com. If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.

`host_name_prefix`

(optional) The host prefix. If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com. If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.

`user_name`

(optional) The user name for an Oracle B2C Service staff member who has the necessary profile permissions.

`password`

(optional) The password for the Oracle B2C Service staff member who has the necessary profile permissions.

`client_type`

(optional) The type of Service Cloud client.

Allowed values are: 'WSDL', 'REST'

### DBMS_CLOUD_OCI_ODA_UPDATE_SKILL_DETAILS_T Type

Properties to update a Skill.

Syntax
```

```

Fields

Field Description

`category`

(optional) The resource's category. This is used to group resource's together.

`description`

(optional) A short description of the resource.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_UPDATE_SKILL_PARAMETER_DETAILS_T Type

Properties to update a Skill Parameter.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The display name for the Parameter.

`description`

(optional) A description of the Parameter.

`value`

(optional) The current value. The value will be interpreted based on the `type`.

### DBMS_CLOUD_OCI_ODA_UPDATE_SLACK_CHANNEL_DETAILS_T Type

Properties to update a Slack channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_slack_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`client_id`

(optional) The Slack Client Id for the Slack app.

`auth_success_url`

(optional) The URL to redirect to when authentication is successful.

`auth_error_url`

(optional) The URL to redirect to when authentication is unsuccessful.

`signing_secret`

(optional) The Signing Secret for the Slack App.

`client_secret`

(optional) The Client Secret for the Slack App.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_UPDATE_TRANSLATOR_DETAILS_T Type

Properties to update a Translator.

Syntax
```

```

Fields

Field Description

`base_url`

(optional) The base URL for invoking the Translation Service.

`auth_token`

(optional) The authentication token to use when invoking the Translation Service

`properties`

(optional) Properties used when invoking the translation service. Each property is a simple key-value pair.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_ODA_UPDATE_TWILIO_CHANNEL_DETAILS_T Type

Properties to update a Twilio channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_twilio_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`account_sid`

(optional) The Account SID for the Twilio number.

`phone_number`

(optional) The Twilio phone number.

`auth_token`

(optional) The Auth Token for the Twilio number.

`is_mms_enabled`

(optional) Whether MMS is enabled for this channel or not.

`original_connectors_url`

(optional) The original connectors URL (used for backward compatibility).

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_UPDATE_WEB_CHANNEL_DETAILS_T Type

Properties to update a Web channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_web_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`max_token_expiration_time_in_minutes`

(optional) The maximum time until the token expires (in minutes).

`is_client_authentication_enabled`

(optional) Whether client authentication is enabled or not.

`allowed_domains`

(optional) A comma-delimited whitelist of allowed domains. The channel will only communicate with the sites from the domains that you add to this list. For example, *.corp.example.com, *.hdr.example.com. Entering a single asterisk (*) allows unrestricted access to the channel from any domain. Typically, you'd only enter a single asterisk during development. For production, you would add an allowlist of domains.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_UPDATE_WEBHOOK_CHANNEL_DETAILS_T Type

Properties to update a Webhook channel.

Syntax
```

```

`dbms_cloud_oci_oda_update_webhook_channel_details_t`is a subtype of the`dbms_cloud_oci_oda_update_channel_details_t`type.

Fields

Field Description

`outbound_url`

(optional) The URL to send responses to.

`payload_version`

(optional) The version for payloads.

Allowed values are: '1.0', '1.1'

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_WEB_CHANNEL_T Type

The configuration for a Web channel.

Syntax
```

```

`dbms_cloud_oci_oda_web_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`max_token_expiration_time_in_minutes`

(optional) The maximum time until the token expires (in minutes).

`is_client_authentication_enabled`

(required) Whether client authentication is enabled or not.

`allowed_domains`

(optional) A comma-delimited whitelist of allowed domains. The channel will only communicate with the sites from the domains that you add to this list. For example, *.corp.example.com, *.hdr.example.com. Entering a single asterisk (*) allows unrestricted access to the channel from any domain. Typically, you'd only enter a single asterisk during development. For production, you would add an allowlist of domains.

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

### DBMS_CLOUD_OCI_ODA_WEBHOOK_CHANNEL_T Type

The configuration for a Webhook channel.

Syntax
```

```

`dbms_cloud_oci_oda_webhook_channel_t`is a subtype of the`dbms_cloud_oci_oda_channel_t`type.

Fields

Field Description

`outbound_url`

(required) The URL to send responses to.

`payload_version`

(required) The version for payloads.

Allowed values are: '1.0', '1.1'

`bot_id`

(optional) The ID of the Skill or Digital Assistant that the Channel is routed to.

`webhook_url`

(required) The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.

### DBMS_CLOUD_OCI_ODA_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`resource_action`

(required) The action to take against the resource.

Allowed values are: 'CREATE', 'UPDATE', 'DELETE', 'PURGE', 'RECOVER', 'STOP', 'START', 'CHANGE_COMPARTMENT', 'CHANGE_CUST_ENC_KEY', 'DEACT_CUST_ENC_KEY', 'CREATE_ASSOCIATION', 'DELETE_ASSOCIATION', 'UPDATE_ENTITLEMENTS_FOR_CACCT', 'CREATE_ODA_INSTANCE_ATTACHMENT', 'UPDATE_ODA_INSTANCE_ATTACHMENT', 'DELETE_ODA_INSTANCE_ATTACHMENT', 'CREATE_IMPORTED_PACKAGE', 'UPDATE_IMPORTED_PACKAGE', 'DELETE_IMPORTED_PACKAGE', 'EXPORT'

`resource_type`

(required) The resource type that the work request affects.

`resource_id`

(required) The identifier of the resource that is the subject of the request.

`status`

(required) The current state of the work request. The `SUCCEEDED`, `FAILED`, AND `CANCELED` states correspond to the action being performed.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'CANCELING', 'CANCELED'

`status_message`

(optional) Short message providing more detail for the current status. For example, if an operation fails this may include information about the reason for the failure and a possible resolution.

`resource_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_ODA_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_oda_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ODA_WORK_REQUEST_T Type

The description of work request, including its status.

Syntax
```

```

Fields

Field Description

`id`

(required) The identifier of the work request.

`compartment_id`

(required) The identifier of the compartment that contains the work request.

`oda_instance_id`

(required) The identifier of the Digital Assistant instance to which this work request pertains.

`resource_id`

(required) The identifier of the resource to which this work request pertains.

`request_action`

(required) The type of the operation that's associated with the work request.

Allowed values are: 'CREATE_ODA_INSTANCE', 'UPGRADE_ODA_INSTANCE', 'DELETE_ODA_INSTANCE', 'PURGE_ODA_INSTANCE', 'RECOVER_ODA_INSTANCE', 'STOP_ODA_INSTANCE', 'START_ODA_INSTANCE', 'CHANGE_ODA_INSTANCE_COMPARTMENT', 'CHANGE_CUST_ENC_KEY', 'DEACT_CUST_ENC_KEY', 'CREATE_ASSOCIATION', 'DELETE_ASSOCIATION', 'CREATE_PCS_INSTANCE', 'UPDATE_ENTITLEMENTS_FOR_CACCT', 'LOOKUP_ODA_INSTANCES_FOR_CACCT', 'CREATE_ODA_INSTANCE_ATTACHMENT', 'UPDATE_ODA_INSTANCE_ATTACHMENT', 'DELETE_ODA_INSTANCE_ATTACHMENT', 'CREATE_IMPORTED_PACKAGE', 'UPDATE_IMPORTED_PACKAGE', 'DELETE_IMPORTED_PACKAGE', 'IMPORT_BOT', 'CREATE_SKILL', 'CLONE_SKILL', 'EXTEND_SKILL', 'VERSION_SKILL', 'EXPORT_SKILL', 'CREATE_DIGITAL_ASSISTANT', 'CLONE_DIGITAL_ASSISTANT', 'EXTEND_DIGITAL_ASSISTANT', 'VERSION_DIGITAL_ASSISTANT', 'EXPORT_DIGITAL_ASSISTANT', 'CREATE_ODA_PRIVATE_ENDPOINT', 'DELETE_ODA_PRIVATE_ENDPOINT', 'UPDATE_ODA_PRIVATE_ENDPOINT', 'CHANGE_ODA_PRIVATE_ENDPOINT_COMPARTMENT', 'CREATE_ODA_PRIVATE_ENDPOINT_SCAN_PROXY', 'DELETE_ODA_PRIVATE_ENDPOINT_SCAN_PROXY', 'CREATE_ODA_PRIVATE_ENDPOINT_ATTACHMENT', 'DELETE_ODA_PRIVATE_ENDPOINT_ATTACHMENT'

`status`

(required) The status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'CANCELING', 'CANCELED'

`status_message`

(optional) A short message that provides more detail about the current status. For example, if a work request fails, then this may include information about why it failed.

`resources`

(required) The resources that this work request affects.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time that the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time that the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), CKQ section 14.29.

`time_finished`

(optional) The date and time that the object finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339). CKQ

### DBMS_CLOUD_OCI_ODA_WORK_REQUEST_ERROR_T Type

Description of the unexpected error that prevented completion of the request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occurred. Error codes are listed at (https://docs.us-phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm)

`message`

(required) A human-readable description of the issue.

`time_stamp`

(required) When the error occurred. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_ODA_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`time_stamp`

(required) When the log message was written. A date-time string as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

### DBMS_CLOUD_OCI_ODA_WORK_REQUEST_SUMMARY_T Type

A description of the work request's status.

Syntax
```

```

Fields

Field Description

`id`

(required) The identifier of the work request.

`compartment_id`

(required) The identifier of the compartment that contains the work request.

`oda_instance_id`

(required) The identifier of the Digital Assistant instance to which this work request pertains.

`resource_id`

(required) The identifier of the resource to which this work request pertains.

`request_action`

(required) The type of the operation that's associated with the work request.

Allowed values are: 'CREATE_ODA_INSTANCE', 'UPGRADE_ODA_INSTANCE', 'DELETE_ODA_INSTANCE', 'PURGE_ODA_INSTANCE', 'RECOVER_ODA_INSTANCE', 'STOP_ODA_INSTANCE', 'START_ODA_INSTANCE', 'CHANGE_ODA_INSTANCE_COMPARTMENT', 'CHANGE_CUST_ENC_KEY', 'DEACT_CUST_ENC_KEY', 'CREATE_ASSOCIATION', 'DELETE_ASSOCIATION', 'UPDATE_ENTITLEMENTS_FOR_CACCT', 'LOOKUP_ODA_INSTANCES_FOR_CACCT', 'CREATE_ODA_INSTANCE_ATTACHMENT', 'UPDATE_ODA_INSTANCE_ATTACHMENT', 'DELETE_ODA_INSTANCE_ATTACHMENT', 'CREATE_IMPORTED_PACKAGE', 'UPDATE_IMPORTED_PACKAGE', 'DELETE_IMPORTED_PACKAGE', 'IMPORT_BOT', 'CREATE_SKILL', 'CLONE_SKILL', 'EXTEND_SKILL', 'VERSION_SKILL', 'EXPORT_SKILL', 'CREATE_DIGITAL_ASSISTANT', 'CLONE_DIGITAL_ASSISTANT', 'EXTEND_DIGITAL_ASSISTANT', 'VERSION_DIGITAL_ASSISTANT', 'EXPORT_DIGITAL_ASSISTANT', 'CREATE_ODA_PRIVATE_ENDPOINT', 'DELETE_ODA_PRIVATE_ENDPOINT', 'UPDATE_ODA_PRIVATE_ENDPOINT', 'CHANGE_ODA_PRIVATE_ENDPOINT_COMPARTMENT', 'CREATE_ODA_PRIVATE_ENDPOINT_SCAN_PROXY', 'DELETE_ODA_PRIVATE_ENDPOINT_SCAN_PROXY', 'CREATE_ODA_PRIVATE_ENDPOINT_ATTACHMENT', 'DELETE_ODA_PRIVATE_ENDPOINT_ATTACHMENT'

`status`

(required) The status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'CANCELING', 'CANCELED'

`resources`

(required) The resources that this work request affects.

- [ODA Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-8F4B2BAE-969E-49D5-89D7-D4C70CFDF704)
- [DBMS_CLOUD_OCI_ODA_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-5D558056-5232-48E8-8FAE-F61748414EC9)
- [DBMS_CLOUD_OCI_ODA_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-EAC973FA-2889-4691-B106-9EC9DF4E1CC1)
- [DBMS_CLOUD_OCI_ODA_ANDROID_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-9C7230DF-84DA-45BD-9D9E-A6062532B489)
- [DBMS_CLOUD_OCI_ODA_APP_EVENT_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-A8685843-290D-44BD-8EA4-C0257F804915)
- [DBMS_CLOUD_OCI_ODA_APPLICATION_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-0D7AD8F8-768A-412C-9FB8-3F7BE95FE279)
- [DBMS_CLOUD_OCI_ODA_AUTHENTICATION_PROVIDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-ABE18170-0E85-4A8B-B31D-1AF62CFA69C1)
- [DBMS_CLOUD_OCI_ODA_AUTHENTICATION_PROVIDER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-0CA0720B-AA59-493C-AAE9-68A909AD61C4)
- [DBMS_CLOUD_OCI_ODA_AUTHENTICATION_PROVIDER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-0884FA87-F17D-4128-8853-4B2002225439)
- [DBMS_CLOUD_OCI_ODA_AUTHENTICATION_PROVIDER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-1B5CF749-954F-457E-98D0-8B85341CB96C)
- [DBMS_CLOUD_OCI_ODA_BOT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-24A58C96-C760-4D86-A3D0-097FA6605DBB)
- [DBMS_CLOUD_OCI_ODA_CHANGE_ODA_INSTANCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-D7BBD19C-CB6D-49B0-B61B-85B9D9837908)
- [DBMS_CLOUD_OCI_ODA_CHANGE_ODA_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-4D40D760-576D-4057-99D2-E129DE313818)
- [DBMS_CLOUD_OCI_ODA_CHANNEL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-EF9A50C3-6836-4422-BE3F-459221185C33)
- [DBMS_CLOUD_OCI_ODA_CHANNEL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-8EB779FD-1570-4366-B0E6-27CFF529B37D)
- [DBMS_CLOUD_OCI_ODA_CHANNEL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-E969A378-B9D1-453D-B564-CB6595682047)
- [DBMS_CLOUD_OCI_ODA_CREATE_DIGITAL_ASSISTANT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-F9695EA5-38D1-4E1F-90C3-1CF0B5649EFC)
- [DBMS_CLOUD_OCI_ODA_CLONE_DIGITAL_ASSISTANT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-5C057C0A-675A-4F5E-AF6B-B73CA3911EBE)
- [DBMS_CLOUD_OCI_ODA_CREATE_SKILL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-1E71836D-EFE0-4B49-9901-6451FD3602D7)
- [DBMS_CLOUD_OCI_ODA_CLONE_SKILL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-48794063-3196-4625-B2C1-9D1FF107E4DC)
- [DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_PARAMETER_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-E95B569A-57F4-411A-98FC-B3399200527B)
- [DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_PARAMETER_VALUE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-5716F410-BA71-4C01-BAB8-443E909539CA)
- [DBMS_CLOUD_OCI_ODA_CONFIGURE_DIGITAL_ASSISTANT_PARAMETERS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-18378382-8E19-4B2D-AC9B-4AC5936CB32F)
- [DBMS_CLOUD_OCI_ODA_CORTANA_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-D1594CDA-8421-43EF-9181-3017B6832533)
- [DBMS_CLOUD_OCI_ODA_CREATE_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-B0435BFB-9402-4119-88E1-302383FC9EEF)
- [DBMS_CLOUD_OCI_ODA_CREATE_ANDROID_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-E28CD3F5-DDCB-40B5-80D6-984B95268926)
- [DBMS_CLOUD_OCI_ODA_CREATE_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-C6B10223-E128-422C-A397-CA1E2AD77E37)
- [DBMS_CLOUD_OCI_ODA_CREATE_ANDROID_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-45FCA097-59D5-4EF0-A1BA-00A056497627)
- [DBMS_CLOUD_OCI_ODA_CREATE_APP_EVENT_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-77F444D7-9011-4D34-B100-8F2E0788866F)
- [DBMS_CLOUD_OCI_ODA_CREATE_APP_EVENT_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-5F102B55-CAC5-4C73-B869-3B3A27591E26)
- [DBMS_CLOUD_OCI_ODA_CREATE_APPLICATION_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-E4B25DC1-4207-4746-BFBD-600FB4FBBC5C)
- [DBMS_CLOUD_OCI_ODA_CREATE_APPLICATION_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-826E5273-8FC7-45F3-ABD0-A7E78F1042B7)
- [DBMS_CLOUD_OCI_ODA_CREATE_AUTHENTICATION_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-48E20032-41E8-45F0-999C-CB85F64CBBCC)
- [DBMS_CLOUD_OCI_ODA_CREATE_CORTANA_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-6E65306F-CEBA-45C9-B4BB-A4953691E13B)
- [DBMS_CLOUD_OCI_ODA_CREATE_CORTANA_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-D87D295E-9BAF-470C-87A1-DB79B7ECC960)
- [DBMS_CLOUD_OCI_ODA_CREATE_DIGITAL_ASSISTANT_VERSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-0A0AEDC0-7C19-4983-AB3A-1ED388339138)
- [DBMS_CLOUD_OCI_ODA_CREATE_FACEBOOK_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-42F24B75-13D6-4F2C-9ACC-F034EC45D612)
- [DBMS_CLOUD_OCI_ODA_CREATE_FACEBOOK_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-4FE1C224-6694-4E74-B1CF-0F2DB0B7B63C)
- [DBMS_CLOUD_OCI_ODA_CREATE_IMPORTED_PACKAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-4DB31457-29B6-402D-A25F-CCC9C2B1EA46)
- [DBMS_CLOUD_OCI_ODA_CREATE_IOS_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-2F41742F-0C4D-4038-8C8A-9B449B6E88B3)
- [DBMS_CLOUD_OCI_ODA_CREATE_IOS_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-1616591A-D3F7-4E38-B4E9-58D26AE33870)
- [DBMS_CLOUD_OCI_ODA_CREATE_MS_TEAMS_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-C2C710D9-4CB6-4206-A39F-24A8B9602BBA)
- [DBMS_CLOUD_OCI_ODA_CREATE_MS_TEAMS_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-8913DA15-3404-4652-83CC-B2BF953F7820)
- [DBMS_CLOUD_OCI_ODA_CREATE_NEW_DIGITAL_ASSISTANT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-E5199412-F1FF-4F7A-AA6D-5F9723BD4A9B)
- [DBMS_CLOUD_OCI_ODA_CREATE_NEW_SKILL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-03800CA0-9C16-431F-A9CA-93492195869D)
- [DBMS_CLOUD_OCI_ODA_CREATE_OSS_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-F62A869C-C1A4-45B3-BF51-0D5F00E770B2)
- [DBMS_CLOUD_OCI_ODA_CREATE_OSS_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-EE121DD4-6AE8-4380-A4E1-E968EFCEDB6C)
- [DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_ATTACHMENT_OWNER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-B7DEA495-0C82-49C0-94D3-DD0B768FC46C)
- [DBMS_CLOUD_OCI_ODA_CREATE_ODA_INSTANCE_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-B6192017-678B-4A9E-ABC1-1991E9D32ED8)
- [DBMS_CLOUD_OCI_ODA_CREATE_ODA_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-35805C31-88B2-4173-B88E-E20F0E6700D2)
- [DBMS_CLOUD_OCI_ODA_CREATE_ODA_PRIVATE_ENDPOINT_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-5F9AD00A-1E66-421D-B0C5-174D143ACFA6)
- [DBMS_CLOUD_OCI_ODA_CREATE_ODA_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-AEBE1413-B721-4FE0-8721-CEE563B17013)
- [DBMS_CLOUD_OCI_ODA_SCAN_LISTENER_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-A71BDF52-2DFB-4FBF-AAD2-3D31D72B28D9)
- [DBMS_CLOUD_OCI_ODA_SCAN_LISTENER_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-4AC93BF6-6E5D-4E72-A6D7-92037971DE9E)
- [DBMS_CLOUD_OCI_ODA_CREATE_ODA_PRIVATE_ENDPOINT_SCAN_PROXY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-25948D1A-BEC0-4257-8C5D-F65C9C083238)
- [DBMS_CLOUD_OCI_ODA_CREATE_OSVC_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-4A9AF397-6886-4F1A-AA68-308D535A7DA0)
- [DBMS_CLOUD_OCI_ODA_CREATE_OSVC_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-79C7FF8B-7A93-42F7-AC98-AC36E1F91A3C)
- [DBMS_CLOUD_OCI_ODA_CREATE_SERVICE_CLOUD_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-080DD444-5915-427A-875A-596AC5A52661)
- [DBMS_CLOUD_OCI_ODA_CREATE_SERVICE_CLOUD_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-67372B3A-13B5-40A3-847C-839C20E09066)
- [DBMS_CLOUD_OCI_ODA_CREATE_SKILL_PARAMETER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-02CB1896-D4E3-4379-9177-F2D801BB3FD7)
- [DBMS_CLOUD_OCI_ODA_CREATE_SKILL_VERSION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-F0BACB8E-670E-44AC-B3F1-B02A4DBD51D1)
- [DBMS_CLOUD_OCI_ODA_CREATE_SLACK_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-D6CC7EEE-3492-43E4-89F5-B9BC0DE60F72)
- [DBMS_CLOUD_OCI_ODA_CREATE_SLACK_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-62DBF6C0-9988-453D-B1DE-64A9604DFE59)
- [DBMS_CLOUD_OCI_ODA_CREATE_TEST_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-130AFF0E-0F64-477C-A172-D0F501B0F5AB)
- [DBMS_CLOUD_OCI_ODA_CREATE_TRANSLATOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-60CB922F-BED7-4645-B255-9A98740B01A0)
- [DBMS_CLOUD_OCI_ODA_CREATE_TWILIO_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-F0D945EA-758B-4A1D-96BB-043768C96C92)
- [DBMS_CLOUD_OCI_ODA_CREATE_TWILIO_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-2AAB2609-D80F-4CEC-98BF-24E5967E3529)
- [DBMS_CLOUD_OCI_ODA_CREATE_WEB_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-FA2DF3C1-46CB-419E-93E9-C14B3BCCB615)
- [DBMS_CLOUD_OCI_ODA_CREATE_WEB_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-12A76E85-5861-4636-911D-ED71220546E9)
- [DBMS_CLOUD_OCI_ODA_CREATE_WEBHOOK_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-A9D144CF-07C1-4C7C-919E-8A09FD938D5B)
- [DBMS_CLOUD_OCI_ODA_CREATE_WEBHOOK_CHANNEL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-3AA818CF-AE8B-4E48-B17A-8E8B1369B936)
- [DBMS_CLOUD_OCI_ODA_RESOURCE_TYPE_DEFAULT_PARAMETER_VALUES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-503F18DB-B894-446B-ABA1-62DA99ACBA89)
- [DBMS_CLOUD_OCI_ODA_RESOURCE_TYPE_DEFAULT_PARAMETER_VALUES_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-DF86301C-0437-4D19-8AB9-C91C88A59079)
- [DBMS_CLOUD_OCI_ODA_DEFAULT_PARAMETER_VALUES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-BACB0F41-870E-4999-ADFC-927A706C1D0C)
- [DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-C3EAE7E1-F10C-49DB-94E1-6FA2C20004CD)
- [DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-A75D63DA-6F6E-4435-BA2A-DE41FE6E3EB2)
- [DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-3FD46915-98C9-412B-B79C-C3712C022160)
- [DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-0C028343-5CBF-4541-A347-25EE61477AD8)
- [DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_PARAMETER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-AE9016E6-B16C-4750-9B3B-21BF514E84B5)
- [DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_PARAMETER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-FB990BFD-6565-4F24-B906-0292DFE94936)
- [DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_PARAMETER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-6DCF294C-6603-47B8-8871-4C095E2835CC)
- [DBMS_CLOUD_OCI_ODA_DIGITAL_ASSISTANT_PARAMETER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-B555B5C7-3987-4762-A812-5DDADFD5556F)
- [DBMS_CLOUD_OCI_ODA_ERROR_BODY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-97C81FC0-C9EC-4B9B-A9B3-D047237DF9CB)
- [DBMS_CLOUD_OCI_ODA_STORAGE_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-3DD10B24-01DB-457D-AFEC-5C663E1FE8FB)
- [DBMS_CLOUD_OCI_ODA_EXPORT_BOT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-2B1C1818-B0D3-4B43-8CA6-DD9625D5D8EE)
- [DBMS_CLOUD_OCI_ODA_EXPORT_DIGITAL_ASSISTANT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-ECBEEDEC-F097-4796-B242-2811207BEF1D)
- [DBMS_CLOUD_OCI_ODA_EXPORT_SKILL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-B8AD92F5-25BD-4DAF-A956-1CD3853F9E69)
- [DBMS_CLOUD_OCI_ODA_EXTEND_DIGITAL_ASSISTANT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-F95B0D9B-EA52-4BA2-9AE8-8262A8BA76C9)
- [DBMS_CLOUD_OCI_ODA_EXTEND_SKILL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-3BFA7285-013F-4EB5-8FD9-DDB6B04C8758)
- [DBMS_CLOUD_OCI_ODA_FACEBOOK_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-A8EEDF1F-FF2C-4FFC-9CD0-01943A3F562C)
- [DBMS_CLOUD_OCI_ODA_IMPORT_BOT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-A16579BC-CA3F-4212-BDC3-C77605ACBF03)
- [DBMS_CLOUD_OCI_ODA_PARAMETER_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-6CAC0A05-DB5D-48CD-86FC-F62ACC2CCA96)
- [DBMS_CLOUD_OCI_ODA_PARAMETER_DEFINITION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-B9457387-A55C-42A8-B4C7-7EE27EB7BD38)
- [DBMS_CLOUD_OCI_ODA_RESOURCE_TYPE_IMPORT_CONTRACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-88013EBC-5B34-4C18-BFD5-77C046C0F309)
- [DBMS_CLOUD_OCI_ODA_RESOURCE_TYPE_IMPORT_CONTRACT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-DA0C7C8D-E636-4CBE-9DA8-735679D2E7D4)
- [DBMS_CLOUD_OCI_ODA_IMPORT_CONTRACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-909C0A0C-F044-49B9-8699-B6068653C6BF)
- [DBMS_CLOUD_OCI_ODA_IMPORTED_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-334DE2CA-1A1C-4F91-839E-7EEC67EF9C6A)
- [DBMS_CLOUD_OCI_ODA_IMPORTED_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-8B10964E-A257-4B10-83AD-1707BB0B221A)
- [DBMS_CLOUD_OCI_ODA_IOS_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-02B3F2D3-729E-4170-B530-B0E5437F17C5)
- [DBMS_CLOUD_OCI_ODA_MS_TEAMS_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-41EBAD37-A780-4CA9-81AA-E57DFA0D9491)
- [DBMS_CLOUD_OCI_ODA_METADATA_PROPERTY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-85FA224B-54AC-4450-AC19-3587B0B784D4)
- [DBMS_CLOUD_OCI_ODA_OSS_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-B3C58679-8E4B-47F0-BCF0-C7FC28BDD76E)
- [DBMS_CLOUD_OCI_ODA_RESTRICTED_OPERATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-A4D74EB1-2064-4F17-B4E5-E253796CA863)
- [DBMS_CLOUD_OCI_ODA_RESTRICTED_OPERATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-1AEC30C4-8522-4113-8CA4-F612042B6A0F)
- [DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-4DC8A5A5-3FB9-485D-BD35-D94434E11D63)
- [DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_OWNER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-276C996E-53F6-4AAC-BEA0-A323D5712569)
- [DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-0F081C82-7B7C-4754-A50E-53D254CF55B0)
- [DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_ATTACHMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-7E9EEC1D-73FA-4FCF-AC98-D9F53775C4D0)
- [DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_ATTACHMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-2981C53C-D4EC-4C15-BBE0-6E59B0D5008E)
- [DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_ATTACHMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-6A703D23-50ED-442A-BC6B-4A745C207596)
- [DBMS_CLOUD_OCI_ODA_ODA_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-4DB1C167-DCD6-4E2F-AD58-C025BB21F30E)
- [DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-315966DD-D6E1-43DF-8FCD-8D8CC8AA4C77)
- [DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_ATTACHMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-76BF2860-6E8E-47B3-8B55-7F19A4B70120)
- [DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_ATTACHMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-CC85F90D-56F7-41B5-995C-2366CF75B76B)
- [DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_ATTACHMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-DC053A38-8899-4154-9477-8DA6B25CFB39)
- [DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_ATTACHMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-BBB223E6-7579-40DB-96C3-7104454BC004)
- [DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-253691AB-8CFD-46FF-B2D2-7314E7A6C012)
- [DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-B5EFCDB7-4014-4EAE-9280-BFE74C4F8955)
- [DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-F4B5D13D-0C51-4B29-86FD-E10C20330F8E)
- [DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_SCAN_PROXY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-2972EC79-9CCF-48C6-BF75-911B61A60044)
- [DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_SCAN_PROXY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-EB3E1911-BEF8-4838-A923-E95D64BD3AE9)
- [DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_SCAN_PROXY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-A460E9F6-B573-4C04-9039-6741A337D967)
- [DBMS_CLOUD_OCI_ODA_ODA_PRIVATE_ENDPOINT_SCAN_PROXY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-6A139AE4-FCF8-4615-9361-4F2D8899F205)
- [DBMS_CLOUD_OCI_ODA_OSVC_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-A886B2CC-9A6A-40A6-BA61-D993FE79ADB2)
- [DBMS_CLOUD_OCI_ODA_METADATA_PROPERTY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-1691488A-3ACC-4A2A-B3F2-FC314285E40F)
- [DBMS_CLOUD_OCI_ODA_RESOURCE_TYPE_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-249350C3-4867-47C7-A3EA-000A1E89168E)
- [DBMS_CLOUD_OCI_ODA_RESOURCE_TYPE_METADATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-510AB8A0-928A-4FD1-B543-8F0828867E68)
- [DBMS_CLOUD_OCI_ODA_PACKAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-D6CE788D-B9B7-4DFE-92BA-08668234F48E)
- [DBMS_CLOUD_OCI_ODA_PACKAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-883FFA49-15B7-4D28-87D1-ACE6B83FBD71)
- [DBMS_CLOUD_OCI_ODA_PARAMETER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-2678553C-B857-42C8-9F16-D362435E0885)
- [DBMS_CLOUD_OCI_ODA_SERVICE_CLOUD_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-26756994-33C3-4AEE-AA2F-61C51BD4D70E)
- [DBMS_CLOUD_OCI_ODA_SKILL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-E28AE6D0-7F26-45DD-82B4-EC1F7A08246C)
- [DBMS_CLOUD_OCI_ODA_SKILL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-1F882318-91E2-455F-B195-07AE1B98C3C8)
- [DBMS_CLOUD_OCI_ODA_SKILL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-3D77BC10-5BD6-4CE5-81E0-AB2584F4F93B)
- [DBMS_CLOUD_OCI_ODA_SKILL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-AD58B179-F6B0-4CFB-BF7D-069F8E1904E2)
- [DBMS_CLOUD_OCI_ODA_SKILL_PARAMETER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-7FFDDD58-A3FF-4EB8-A867-8E8D46E2C71E)
- [DBMS_CLOUD_OCI_ODA_SKILL_PARAMETER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-14FEEE1C-7710-432A-9167-ED96D4BE7F90)
- [DBMS_CLOUD_OCI_ODA_SKILL_PARAMETER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-FE2721D0-DECC-458F-B503-D0686947D278)
- [DBMS_CLOUD_OCI_ODA_SKILL_PARAMETER_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-3DF33F2C-D1B1-4873-A052-0C423610DE78)
- [DBMS_CLOUD_OCI_ODA_SLACK_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-384D9206-A826-4D8E-9136-5A669DE30FE9)
- [DBMS_CLOUD_OCI_ODA_TEST_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-D52CF60B-5C0C-423F-A633-2B70A5440416)
- [DBMS_CLOUD_OCI_ODA_TRANSLATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-54C923F5-855D-4070-9B83-FD6B1E7B24B2)
- [DBMS_CLOUD_OCI_ODA_TRANSLATOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-9CD36D56-906D-4CD3-90E0-BB7640349565)
- [DBMS_CLOUD_OCI_ODA_TRANSLATOR_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-CCBD1FAD-8609-48A5-AAA7-D8BFECD6DB61)
- [DBMS_CLOUD_OCI_ODA_TRANSLATOR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-397F65AE-24CE-4D79-8122-9D695EC1C686)
- [DBMS_CLOUD_OCI_ODA_TWILIO_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-955E9C77-FD85-4CE4-98DD-BCB077A1F451)
- [DBMS_CLOUD_OCI_ODA_UPDATE_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-0C47AC09-7698-437B-B487-9B585A015ABA)
- [DBMS_CLOUD_OCI_ODA_UPDATE_ANDROID_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-3D2DB262-CC17-45DC-AFD3-349C18C62586)
- [DBMS_CLOUD_OCI_ODA_UPDATE_APP_EVENT_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-8595693D-E674-411D-8ADA-440245E35ABB)
- [DBMS_CLOUD_OCI_ODA_UPDATE_APPLICATION_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-BAA37012-0B21-410A-A84E-5625A94ADABF)
- [DBMS_CLOUD_OCI_ODA_UPDATE_AUTHENTICATION_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-D7B8C322-BB20-443F-8409-AB6CB4DA4C3D)
- [DBMS_CLOUD_OCI_ODA_UPDATE_CORTANA_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-F67DD4A4-2F26-4945-9955-9841A84ABBFE)
- [DBMS_CLOUD_OCI_ODA_UPDATE_DIGITAL_ASSISTANT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-C63A2A9F-ED52-4820-B6D7-C9BCCE5CE5A7)
- [DBMS_CLOUD_OCI_ODA_UPDATE_DIGITAL_ASSISTANT_PARAMETER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-D61CFBD2-932F-4D06-A9AE-9C54F7733062)
- [DBMS_CLOUD_OCI_ODA_UPDATE_FACEBOOK_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-72FD67DE-875D-41DC-9073-78467646D5C9)
- [DBMS_CLOUD_OCI_ODA_UPDATE_IMPORTED_PACKAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-E33FC5B7-DC2D-451B-8D03-4B48DAD4D95B)
- [DBMS_CLOUD_OCI_ODA_UPDATE_IOS_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-3C2EEF61-33D0-42F3-A798-E0B0D7F12A2F)
- [DBMS_CLOUD_OCI_ODA_UPDATE_MS_TEAMS_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-5205A24B-F694-4F01-AD4F-6EB406857EC3)
- [DBMS_CLOUD_OCI_ODA_UPDATE_OSS_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-B3369938-BED0-4C9D-A254-E815FB5A3FFF)
- [DBMS_CLOUD_OCI_ODA_UPDATE_ODA_INSTANCE_ATTACHMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-B70F6FD4-917E-4B65-B73D-CED4718DD388)
- [DBMS_CLOUD_OCI_ODA_UPDATE_ODA_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-567CC42E-3E3E-43FE-B93C-3F3DD046C6FE)
- [DBMS_CLOUD_OCI_ODA_UPDATE_ODA_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-5D0DA1B8-0D5A-4F9A-B267-EACC43088338)
- [DBMS_CLOUD_OCI_ODA_UPDATE_OSVC_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-A1D3901A-2D1C-4EB3-97E6-33E347D82948)
- [DBMS_CLOUD_OCI_ODA_UPDATE_SERVICE_CLOUD_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-621EB105-8DB4-4946-9A00-72CA4184BB68)
- [DBMS_CLOUD_OCI_ODA_UPDATE_SKILL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-99B09831-12BE-4F6B-AF38-0B0729AEA364)
- [DBMS_CLOUD_OCI_ODA_UPDATE_SKILL_PARAMETER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-9A517EAC-31AA-41C9-A45F-E15503157088)
- [DBMS_CLOUD_OCI_ODA_UPDATE_SLACK_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-82849666-B2B5-4910-A697-5DC0D3E1B405)
- [DBMS_CLOUD_OCI_ODA_UPDATE_TRANSLATOR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-5F8607CC-CED4-49C6-87FB-EC7E373BFCEB)
- [DBMS_CLOUD_OCI_ODA_UPDATE_TWILIO_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-CC955F96-58AA-4F68-B17C-B0161216A7B0)
- [DBMS_CLOUD_OCI_ODA_UPDATE_WEB_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-330BB47B-6CB0-4A87-8301-1B33380D3901)
- [DBMS_CLOUD_OCI_ODA_UPDATE_WEBHOOK_CHANNEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-E878B502-A8C6-4C34-B159-586BE4E5941C)
- [DBMS_CLOUD_OCI_ODA_WEB_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-EF382C8C-A176-4AED-A27F-74810BB551B4)
- [DBMS_CLOUD_OCI_ODA_WEBHOOK_CHANNEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-8E8F3432-DB06-4E93-B466-57AA6B6CAC80)
- [DBMS_CLOUD_OCI_ODA_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-3DB1D833-6A47-4566-9240-D7A75C1651AE)
- [DBMS_CLOUD_OCI_ODA_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-D2EB6EA5-449F-434F-927C-3C591514493D)
- [DBMS_CLOUD_OCI_ODA_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-B001459B-DAE8-4F13-A4CE-D128C2D32C4B)
- [DBMS_CLOUD_OCI_ODA_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-FCF4A372-6924-4D62-BE35-52D6F69E21CC)
- [DBMS_CLOUD_OCI_ODA_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-0EBC15F9-9AB3-44AD-8CFF-00D69620498C)
- [DBMS_CLOUD_OCI_ODA_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oda_t.html#ADSDK-GUID-F1AB564A-65D1-4F9D-9628-5F6757844F64)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
