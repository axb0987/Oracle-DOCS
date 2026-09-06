# Management Dashboard Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#dcoc-content-body)

## Management Dashboard Common Types

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_CHANGE_MANAGEMENT_DASHBOARDS_COMPARTMENT_DETAILS_T Type

Compartment to which the dashboard is being moved.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID of the compartment to which the dashboard is being moved.

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_CHANGE_MANAGEMENT_SAVED_SEARCHES_COMPARTMENT_DETAILS_T Type

Compartment to which the saved search is being moved.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) OCID of the compartment to which the saved search is being moved.

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_JSON_ELEMENT_T_TBL Type

Nested table type of json_element_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_TILE_DETAILS_T Type

Properties of the dashboard tile representing a saved search. Tiles are laid out in a twelve column grid system with (0,0) at upper left corner.

Syntax
```

```

Fields

Field Description

`display_name`

(required) Display name of the saved search.

`saved_search_id`

(required) ID of the saved search.

`l_row`

(required) Tile's row number.

`l_column`

(required) Tile's column number.

`height`

(required) The number of rows the tile occupies.

`width`

(required) The number of columns the tile occupies.

`nls`

(required) JSON that contains internationalization options.

`ui_config`

(required) It defines the visualization type of the widget saved search, the UI options of that visualization type, the binding of data to the visualization.

`data_config`

(required) It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for various data sources.

`state`

(required) Current state of the saved search.

Allowed values are: 'DELETED', 'UNAUTHORIZED', 'DEFAULT'

`drilldown_config`

(required) Drill-down configuration to define the destination of a drill-down action.

`parameters_map`

(optional) Specifies the saved search parameters values

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_TILE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_management_dashboard_management_dashboard_tile_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_CREATE_MANAGEMENT_DASHBOARD_DETAILS_T Type

Properties of a dashboard. ID of the dashboard must only be provided for Out-of-the-Box (OOB) dashboards.

Syntax
```

```

Fields

Field Description

`dashboard_id`

(optional) ID of the dashboard, which must only be provided for Out-of-the-Box (OOB) dashboards.

`provider_id`

(required) ID of the service (for example, log-analytics) that owns the dashboard. Each service has a unique ID.

`provider_name`

(required) The user friendly name of the service (for example, Logging Analytics) that owns the dashboard.

`provider_version`

(required) The version of the metadata of the provider. This is useful for provider to version its features and metadata. Any newly created saved search (or dashboard) should use providerVersion 3.0.0.

`tiles`

(required) Array of dashboard tiles.

`display_name`

(required) Display name of the dashboard.

`description`

(required) Description of the dashboard.

`compartment_id`

(required) OCID of the compartment in which the dashboard resides.

`is_oob_dashboard`

(required) Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be modified.

`is_show_in_home`

(required) Determines whether the dashboard will be displayed in Dashboard Home.

`metadata_version`

(required) The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.

`is_show_description`

(required) Determines whether the description of the dashboard is displayed.

`screen_image`

(required) Screen image of the dashboard.

`nls`

(required) JSON that contains internationalization options.

`ui_config`

(required) JSON that contains user interface options.

`data_config`

(required) Array of JSON that contain data source options.

`l_type`

(required) Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.

`is_favorite`

(required) Determines whether the dashboard is set as favorite.

`parameters_config`

(optional) Defines parameters for the dashboard.

`features_config`

(optional) Contains configuration for enabling features.

`drilldown_config`

(optional) Drill-down configuration to define the destination of a drill-down action.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_CREATE_MANAGEMENT_SAVED_SEARCH_DETAILS_T Type

Properties of a saved search.

Syntax
```

```

Fields

Field Description

`id`

(optional) ID of the saved search, which must only be provided for Out-of-the-Box (OOB) saved search.

`display_name`

(required) Display name of the saved search.

`provider_id`

(required) ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.

`provider_version`

(required) The version of the metadata of the provider. This is useful for provider to version its features and metadata. Any newly created saved search (or dashboard) should use providerVersion 3.0.0.

`provider_name`

(required) The user friendly name of the service (for example, Logging Analytics) that owns the saved search.

`compartment_id`

(required) OCID of the compartment in which the saved search resides.

`is_oob_saved_search`

(required) Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle and cannot be modified.

`description`

(required) Description of the saved search.

`nls`

(required) JSON that contains internationalization options.

`l_type`

(required) Determines how the saved search is displayed in a dashboard.

Allowed values are: 'SEARCH_SHOW_IN_DASHBOARD', 'SEARCH_DONT_SHOW_IN_DASHBOARD', 'WIDGET_SHOW_IN_DASHBOARD', 'WIDGET_DONT_SHOW_IN_DASHBOARD', 'FILTER_SHOW_IN_DASHBOARD', 'FILTER_DONT_SHOW_IN_DASHBOARD'

`ui_config`

(required) It defines the visualization type of the widget saved search, the UI options of that visualization type, the binding of data to the visualization.

`data_config`

(required) It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for various data sources.

`screen_image`

(required) Screen image of the saved search.

`metadata_version`

(required) The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.

`widget_template`

(required) The UI template that the saved search uses to render itself.

`widget_vm`

(required) The View Model that the saved search uses to render itself.

`parameters_config`

(optional) Defines parameters for the saved search.

`features_config`

(optional) Contains configuration for enabling features.

`drilldown_config`

(optional) Drill-down configuration to define the destination of a drill-down action.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_T Type

Properties of a saved search.

Syntax
```

```

Fields

Field Description

`id`

(required) ID of the saved search.

`display_name`

(required) Display name of the saved search.

`provider_id`

(required) ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.

`provider_version`

(required) Version of the service that owns this saved search.

`provider_name`

(required) Name of the service (for example, Logging Analytics) that owns the saved search.

`compartment_id`

(required) OCID of the compartment in which the saved search resides.

`is_oob_saved_search`

(required) Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle and cannot be modified.

`description`

(required) Description of the saved search.

`nls`

(required) JSON that contains internationalization options.

`l_type`

(required) Determines how the saved search is displayed in a dashboard.

Allowed values are: 'SEARCH_SHOW_IN_DASHBOARD', 'SEARCH_DONT_SHOW_IN_DASHBOARD', 'WIDGET_SHOW_IN_DASHBOARD', 'WIDGET_DONT_SHOW_IN_DASHBOARD', 'FILTER_SHOW_IN_DASHBOARD', 'FILTER_DONT_SHOW_IN_DASHBOARD'

`ui_config`

(required) It defines the visualization type of the widget saved search, the UI options of that visualization type, the binding of data to the visualization.

`data_config`

(required) It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for various data sources.

`created_by`

(required) The principle id of the user that created this saved search. This is automatically managed by the system. In OCI the value is ignored. In EM it can skipped or otherwise it is ignored in both create and update API and system automatically sets its value.

`updated_by`

(required) The principle id of the user that updated this saved search.

`time_created`

(required) Date and time the saved search was created.

`time_updated`

(required) Date and time the saved search was updated.

`screen_image`

(required) Screen image of the saved search.

`metadata_version`

(required) The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.

`widget_template`

(required) The UI template that the saved search uses to render itself.

`widget_vm`

(required) The View Model that the saved search uses to render itself.

`lifecycle_state`

(required) OCI lifecycle status. This is automatically managed by the system.

Allowed values are: 'ACTIVE'

`parameters_config`

(optional) Defines parameters for the saved search.

`features_config`

(optional) Contains configuration for enabling features.

`drilldown_config`

(optional) Drill-down configuration to define the destination of a drill-down action.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_TBL Type

Nested table type of dbms_cloud_oci_management_dashboard_management_saved_search_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_T Type

Properties of a dashboard, including dashboard ID.

Syntax
```

```

Fields

Field Description

`dashboard_id`

(required) ID of the dashboard. Same as id.

`id`

(required) ID of the dashboard. Same as dashboardId.

`provider_id`

(required) ID of the service (for example, log-analytics) that owns the dashboard. Each service has a unique ID.

`provider_name`

(required) Name of the service (for example, Logging Analytics) that owns the dashboard.

`provider_version`

(required) Version of the service that owns the dashboard.

`tiles`

(required) Array of dashboard tiles.

`display_name`

(required) Display name of the dashboard.

`description`

(required) Description of the dashboard.

`compartment_id`

(required) OCID of the compartment in which the dashboard resides.

`is_oob_dashboard`

(required) Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be modified.

`is_show_in_home`

(required) Determines whether the dashboard will be displayed in Dashboard Home.

`created_by`

(required) User who created the dashboard.

`time_created`

(required) Date and time the dashboard was created.

`updated_by`

(required) User who updated the dashboard.

`time_updated`

(required) Date and time the dashboard was updated.

`metadata_version`

(required) The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.

`is_show_description`

(required) Determines whether the description of the dashboard is displayed.

`screen_image`

(required) Screen image of the dashboard.

`nls`

(required) JSON that contains internationalization options.

`ui_config`

(required) JSON that contains user interface options.

`data_config`

(required) Array of JSON that contain data source options.

`l_type`

(required) Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.

`is_favorite`

(required) Determines whether the dashboard is set as favorite.

`saved_searches`

(required) Array of saved searches in the dashboard.

`lifecycle_state`

(required) State of dashboard.

Allowed values are: 'ACTIVE'

`parameters_config`

(optional) Defines parameters for the dashboard.

`drilldown_config`

(optional) Drill-down configuration to define the destination of a drill-down action.

`features_config`

(optional) Contains configuration for enabling features.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_SUMMARY_T Type

Summary of the properties of a dashboard.

Syntax
```

```

Fields

Field Description

`dashboard_id`

(required) ID of the dashboard. Same as id.

`id`

(required) ID of the dashboard. Same as dashboardId.

`display_name`

(required) Display name of the dashboard.

`description`

(required) Description of the dashboard.

`compartment_id`

(required) OCID of the compartment in which the dashboard resides.

`provider_id`

(required) ID of the service (for example, log-analytics) that owns the dashboard. Each service has a unique ID.

`provider_name`

(required) The user friendly name of the service (for example, Logging Analytics) that owns the dashboard.

`provider_version`

(required) The version of the metadata of the provider. This is useful for provider to version its features and metadata. Any newly created saved search (or dashboard) should use providerVersion 3.0.0.

`is_oob_dashboard`

(required) Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be modified.

`created_by`

(required) User who created the dashboard.

`time_created`

(required) Date and time the dashboard was created.

`updated_by`

(required) User who updated the dashboard.

`time_updated`

(required) Date and time the dashboard was updated.

`metadata_version`

(required) The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.

`screen_image`

(required) Screen image of the dashboard.

`nls`

(required) JSON that contains internationalization options.

`l_type`

(required) Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.

`features_config`

(optional) Contains configuration for enabling features.

`lifecycle_state`

(required) Current lifecycle state of the dashboard.

Allowed values are: 'ACTIVE'

`freeform_tags`

(required) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_management_dashboard_management_dashboard_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_COLLECTION_T Type

List of dashboards.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of dashboard summaries.

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_FOR_IMPORT_DETAILS_T Type

Properties of a saved search.

Syntax
```

```

Fields

Field Description

`id`

(required) ID of the saved search.

`display_name`

(required) Display name of the saved search.

`provider_id`

(required) ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.

`provider_version`

(required) The version of the metadata of the provider. This is useful for provider to version its features and metadata. Any newly created saved search (or dashboard) should use providerVersion 3.0.0.

`provider_name`

(required) The user friendly name of the service (for example, Logging Analytics) that owns the saved search.

`compartment_id`

(required) OCID of the compartment in which the saved search resides.

`is_oob_saved_search`

(required) Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle and cannot be modified.

`description`

(required) Description of the saved search.

`nls`

(required) JSON that contains internationalization options.

`l_type`

(required) Determines how the saved search is displayed in a dashboard.

Allowed values are: 'SEARCH_SHOW_IN_DASHBOARD', 'SEARCH_DONT_SHOW_IN_DASHBOARD', 'WIDGET_SHOW_IN_DASHBOARD', 'WIDGET_DONT_SHOW_IN_DASHBOARD', 'FILTER_SHOW_IN_DASHBOARD', 'FILTER_DONT_SHOW_IN_DASHBOARD'

`ui_config`

(required) It defines the visualization type of the widget saved search, the UI options of that visualization type, the binding of data to the visualization.

`data_config`

(required) It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for various data sources.

`screen_image`

(required) Screen image of the saved search.

`metadata_version`

(required) The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.

`widget_template`

(required) The UI template that the saved search uses to render itself.

`widget_vm`

(required) The View Model that the saved search uses to render itself.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`parameters_config`

(optional) Defines parameters for the saved search.

`features_config`

(optional) Contains configuration for enabling features.

`drilldown_config`

(optional) Drill-down configuration to define the destination of a drill-down action.

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_FOR_IMPORT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_management_dashboard_management_saved_search_for_import_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_FOR_IMPORT_EXPORT_DETAILS_T Type

Properties of a dashboard, including dashboard ID and saved searches, for import purposes.

Syntax
```

```

Fields

Field Description

`dashboard_id`

(required) ID of the dashboard.

`provider_id`

(required) ID of the service (for example log-analytics) that owns the dashboard. Each service has a unique ID.

`provider_name`

(required) The user friendly name of the service (for example, Logging Analytics) that owns the dashboard.

`provider_version`

(required) The version of the metadata of the provider. This is useful for provider to version its features and metadata. Any newly created saved search (or dashboard) should use providerVersion 3.0.0.

`tiles`

(required) Array of dashboard tiles.

`display_name`

(required) Display name of the dashboard.

`description`

(required) Description of the dashboard.

`compartment_id`

(required) OCID of the compartment in which the dashboard resides.

`is_oob_dashboard`

(required) Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be modified.

`is_show_in_home`

(required) Determines whether the dashboard will be displayed in Dashboard Home.

`metadata_version`

(required) The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.

`is_show_description`

(required) Determines whether the description of the dashboard is displayed.

`screen_image`

(required) Screen image of the dashboard.

`nls`

(required) JSON that contains internationalization options.

`ui_config`

(required) It defines the visualization type of the widget saved search, the UI options of that visualization type, the binding of data to the visualization.

`data_config`

(required) It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for various data sources.

`l_type`

(required) Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.

`is_favorite`

(required) Determines whether the dashboard is set as favorite.

`saved_searches`

(required) Array of saved searches in the dashboard.

`parameters_config`

(optional) Defines parameters for the dashboard.

`features_config`

(optional) Contains configuration for enabling features.

`drilldown_config`

(optional) Drill-down configuration to define the destination of a drill-down action.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_FOR_IMPORT_EXPORT_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_management_dashboard_management_dashboard_for_import_export_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_EXPORT_DETAILS_T Type

Array of dashboards to export. Response from export must be directly acceptable to import (compartmentIds may have to be changed).

Syntax
```

```

Fields

Field Description

`dashboards`

(required) Array of dashboards.

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_IMPORT_DETAILS_T Type

Array of dashboards to import.

Syntax
```

```

Fields

Field Description

`dashboards`

(required) Array of dashboards.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_SUMMARY_T Type

Summary of the properties of a saved search.

Syntax
```

```

Fields

Field Description

`id`

(required) ID of the saved search.

`display_name`

(required) Display name of the saved search.

`is_oob_saved_search`

(required) Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle and cannot be modified.

`compartment_id`

(required) OCID of the compartment in which the saved search resides.

`provider_id`

(required) ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.

`provider_version`

(required) The version of the metadata of the provider. This is useful for provider to version its features and metadata. Any newly created saved search (or dashboard) should use providerVersion 3.0.0.

`provider_name`

(required) The user friendly name of the service (for example, Logging Analytics) that owns the saved search.

`description`

(required) Description of the saved search.

`nls`

(required) JSON that contains internationalization options.

`l_type`

(required) Determines how the saved search is displayed in a dashboard.

Allowed values are: 'SEARCH_SHOW_IN_DASHBOARD', 'SEARCH_DONT_SHOW_IN_DASHBOARD', 'WIDGET_SHOW_IN_DASHBOARD', 'WIDGET_DONT_SHOW_IN_DASHBOARD', 'FILTER_SHOW_IN_DASHBOARD', 'FILTER_DONT_SHOW_IN_DASHBOARD'

`ui_config`

(required) It defines the visualization type of the widget saved search, the UI options of that visualization type, the binding of data to the visualization.

`data_config`

(required) It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for various data sources.

`created_by`

(required) The principle id of the user that created this saved search. This is automatically managed by the system. In OCI the value is ignored. In EM it can skipped or otherwise it is ignored in both create and update API and system automatically sets its value.

`updated_by`

(required) The principle id of the user that updated this saved search

`time_created`

(required) Date and time the saved search was created.

`time_updated`

(required) Date and time the saved search was updated.

`screen_image`

(required) Screen image of the saved search.

`metadata_version`

(required) The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.

`widget_template`

(required) The UI template that the saved search uses to render itself.

`widget_vm`

(required) The View Model that the saved search uses to render itself.

`lifecycle_state`

(required) OCI lifecycle status. This is automatically managed by the system.

Allowed values are: 'ACTIVE'

`parameters_config`

(optional) Defines parameters for the saved search.

`features_config`

(optional) Contains configuration for enabling features.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_management_dashboard_management_saved_search_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_COLLECTION_T Type

List of saved searches.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of saved search summaries.

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_UPDATE_MANAGEMENT_DASHBOARD_DETAILS_T Type

Properties of a dashboard. Dashboard ID must not be provided.

Syntax
```

```

Fields

Field Description

`provider_id`

(optional) ID of the service (for example, log-analytics) that owns the dashboard. Each service has a unique ID.

`provider_name`

(optional) The user friendly name of the service (for example, Logging Analytics) that owns the dashboard.

`provider_version`

(optional) The version of the metadata of the provider. This is useful for provider to version its features and metadata. Any newly created saved search (or dashboard) should use providerVersion 3.0.0.

`tiles`

(optional) Array of dashboard tiles.

`display_name`

(optional) Display name of the dashboard.

`description`

(optional) Description of the dashboard.

`compartment_id`

(optional) OCID of the compartment in which the dashboard resides.

`is_oob_dashboard`

(optional) Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be modified.

`is_show_in_home`

(optional) Determines whether the dashboard will be displayed in Dashboard Home.

`metadata_version`

(optional) The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.

`is_show_description`

(optional) Determines whether the description of the dashboard is displayed.

`screen_image`

(optional) Screen image of the dashboard.

`nls`

(optional) JSON that contains internationalization options.

`ui_config`

(optional) JSON that contains user interface options.

`data_config`

(optional) Array of JSON that contain data source options.

`l_type`

(optional) Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.

`is_favorite`

(optional) Determines whether the dashboard is set as favorite.

`parameters_config`

(optional) Defines parameters for the dashboard.

`features_config`

(optional) Contains configuration for enabling features.

`drilldown_config`

(optional) Drill-down configuration to define the destination of a drill-down action.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_UPDATE_MANAGEMENT_SAVED_SEARCH_DETAILS_T Type

Properties of a saved search. Saved search ID must not be provided.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Display name of the saved search.

`provider_id`

(optional) ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.

`provider_version`

(optional) The version of the metadata of the provider. This is useful for provider to version its features and metadata. Any newly created saved search (or dashboard) should use providerVersion 3.0.0.

`provider_name`

(optional) The user friendly name of the service (for example, Logging Analytics) that owns the saved search.

`compartment_id`

(optional) OCID of the compartment in which the saved search resides.

`is_oob_saved_search`

(optional) Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle and cannot be modified.

`description`

(optional) Description of the saved search.

`nls`

(optional) JSON that contains internationalization options.

`l_type`

(optional) Determines how the saved search is displayed in a dashboard.

Allowed values are: 'SEARCH_SHOW_IN_DASHBOARD', 'SEARCH_DONT_SHOW_IN_DASHBOARD', 'WIDGET_SHOW_IN_DASHBOARD', 'WIDGET_DONT_SHOW_IN_DASHBOARD', 'FILTER_SHOW_IN_DASHBOARD', 'FILTER_DONT_SHOW_IN_DASHBOARD'

`ui_config`

(optional) It defines the visualization type of the widget saved search, the UI options of that visualization type, the binding of data to the visualization.

`data_config`

(optional) It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for various data sources.

`screen_image`

(optional) Screen image of the saved search.

`metadata_version`

(optional) The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.

`widget_template`

(optional) The UI template that the saved search uses to render itself.

`widget_vm`

(optional) The View Model that the saved search uses to render itself.

`parameters_config`

(optional) Defines parameters for the saved search.

`features_config`

(optional) Contains configuration for enabling features.

`drilldown_config`

(optional) Drill-down configuration to define the destination of a drill-down action.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

- [Management Dashboard Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-BECC7F32-25B4-4918-A022-A448D93896DA)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-1E85D689-1A45-417F-9409-EBF5FD9D917F)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_CHANGE_MANAGEMENT_DASHBOARDS_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-CD478610-66FF-415C-BF2F-A4D1CE2846B9)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_CHANGE_MANAGEMENT_SAVED_SEARCHES_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-432CA012-AF71-4A5D-AAB9-B7B7AA18C6AB)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_JSON_ELEMENT_T_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-566EB3C4-1292-4497-97E4-9B628E0D5643)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_TILE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-6C7614DE-950C-4148-9F15-705D68FC7734)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_TILE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-F1563390-57A7-4B89-AC0C-1F7A752DC683)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_CREATE_MANAGEMENT_DASHBOARD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-72163CC3-390E-4FF0-9283-043A4FE46CF0)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_CREATE_MANAGEMENT_SAVED_SEARCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-62A9049E-FDDB-4E4F-A8F5-ADD7DDED3917)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-A84A4262-67E4-47FD-9198-905EAF33BE03)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-2F194103-407D-4151-BC1D-8682F04D9AD3)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-315EBAC8-C076-452F-BCE9-67654B99B183)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-64D0C403-CAC7-4C3E-B669-A61D04355FFC)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-BF55B878-138B-498F-87F1-6EBEAB9FE2F3)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-9B255622-A055-4E1F-9B9E-C89EFC2AC934)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-A2062E96-F50B-4AF1-B237-2018905A326A)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_FOR_IMPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-A19298F1-958C-46F2-AF48-5061AB3B5AC9)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_FOR_IMPORT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-1FE4E9EE-2755-49A3-9587-8A4D471EC690)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_FOR_IMPORT_EXPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-F17C5FD5-E3A1-4436-A303-38FB32657DF2)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_FOR_IMPORT_EXPORT_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-30CB7B52-6481-4BF1-BB12-2995DA8ABCDA)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_EXPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-614E7BA1-9C35-4FEB-A212-BB34F65C4D7B)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_DASHBOARD_IMPORT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-374410A4-170F-43C8-BC39-298FDB8F3FF8)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-537EE0C5-FB94-49C8-BC4E-51916514BC8D)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-BCC425FC-F27F-42D6-BB69-F106AC9488C6)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_MANAGEMENT_SAVED_SEARCH_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-EE6A9F52-0218-4477-917C-FF20FD437796)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_UPDATE_MANAGEMENT_DASHBOARD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-C21D52A6-207F-45F2-926B-3D9B8D7C9448)
- [DBMS_CLOUD_OCI_MANAGEMENT_DASHBOARD_UPDATE_MANAGEMENT_SAVED_SEARCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/management_dashboard_t.html#ADSDK-GUID-09691F74-0F1C-4823-BB6D-14E57ECABE26)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
