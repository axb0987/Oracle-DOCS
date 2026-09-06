# AI Speech Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#dcoc-content-body)

## AI Speech Common Types

### DBMS_CLOUD_OCI_AI_SPEECH_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_AI_SPEECH_AUDIO_FORMAT_DETAILS_T Type

Audio format details.

Syntax
```

```

Fields

Field Description

`format`

(optional) Input file format. Example - WAV.

`number_of_channels`

(optional) Input file number of channels.

`encoding`

(optional) Input file encoding. Example - PCM.

`sample_rate_in_hz`

(optional) Input file sampleRate. Example - 16000

### DBMS_CLOUD_OCI_AI_SPEECH_CHANGE_TRANSCRIPTION_JOB_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of a transcription job.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where the resource should be moved.

### DBMS_CLOUD_OCI_AI_SPEECH_DIARIZATION_T Type

Speaker diarization is a combination of speaker segmentation and speaker clustering. Provide diarization details to enable this feature.

Syntax
```

```

Fields

Field Description

`is_diarization_enabled`

(optional) Set true to enable Speaker diarization and tag transcription with speaker tags. By default this is disabled.

`number_of_speakers`

(optional) Number of speakers in the audio provided. By default service will auto detect all speakers in audio file

### DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_SETTINGS_T Type

Processes to perform on the generated transcription.

Syntax
```

```

Fields

Field Description

`diarization`

(optional)

### DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_MODEL_DETAILS_T Type

Model details.

Syntax
```

```

Fields

Field Description

`domain`

(optional) Domain for input files.

Allowed values are: 'GENERIC'

`language_code`

(optional) Locale value as per given in [https://datatracker.ietf.org/doc/html/rfc5646]. - en-US: English - United States - es-ES: Spanish - Spain - pt-BR: Portuguese - Brazil - en-GB: English - Great Britain - en-AU: English - Australia - en-IN: English - India - hi-IN: Hindi - India - fr-FR: French - France - de-DE: German - Germany - it-IT: Italian - Italy

Allowed values are: 'en-US', 'es-ES', 'pt-BR', 'en-GB', 'en-AU', 'en-IN', 'hi-IN', 'fr-FR', 'de-DE', 'it-IT'

`transcription_settings`

(optional)

### DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_FILTER_T Type

Transcription Filter.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of filters.

Allowed values are: 'PROFANITY'

### DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_FILTER_TBL Type

Nested table type of dbms_cloud_oci_ai_speech_transcription_filter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_NORMALIZATION_T Type

Information to Normalize generated transcript.

Syntax
```

```

Fields

Field Description

`is_punctuation_enabled`

(optional) Whether to add punctuation in the generated transcription. Enabled by default.

`filters`

(optional) List of filters.

### DBMS_CLOUD_OCI_AI_SPEECH_INPUT_LOCATION_T Type

The location of the input(s).

Syntax
```

```

Fields

Field Description

`location_type`

(required) The type of input location.

Allowed values are: 'OBJECT_LIST_INLINE_INPUT_LOCATION', 'OBJECT_LIST_FILE_INPUT_LOCATION'

### DBMS_CLOUD_OCI_AI_SPEECH_OUTPUT_LOCATION_T Type

OCI Object Storage Location.

Syntax
```

```

Fields

Field Description

`namespace_name`

(required) Object Storage namespace.

`bucket_name`

(required) Object Storage bucket name.

`prefix`

(required) Object Storage folder name.

### DBMS_CLOUD_OCI_AI_SPEECH_CREATE_TRANSCRIPTION_JOB_DETAILS_T Type

The information about new Transcription Job.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the job.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the job.

`description`

(optional) A short description of the job.

`additional_transcription_formats`

(optional) Transcription Format. By default, the JSON format is used.

Allowed values are: 'SRT'

`model_details`

(optional)

`normalization`

(optional)

`input_location`

(required)

`output_location`

(required)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace-1\": {\"bar-key-1\": \"value-1\", \"bar-key-2\": \"value-2\"}, \"foo-namespace-2\": {\"bar-key-1\": \"value-1\", \"bar-key-2\": \"value-2\"}}`.

### DBMS_CLOUD_OCI_AI_SPEECH_ERROR_T Type

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

### DBMS_CLOUD_OCI_AI_SPEECH_OBJECT_LOCATION_T Type

A location in Object Storage that is uniquely identified by namespace name, bucket name and object name.

Syntax
```

```

Fields

Field Description

`namespace_name`

(required) Object Storage namespace name.

`bucket_name`

(required) Object Storage bucket name.

`object_names`

(required) Object Storage object names.

### DBMS_CLOUD_OCI_AI_SPEECH_OBJECT_LIST_FILE_INPUT_LOCATION_T Type

Use this locationType when passing the location of the object storage in the request (where the WAV file is stored).

Syntax
```

```

`dbms_cloud_oci_ai_speech_object_list_file_input_location_t`is a subtype of the`dbms_cloud_oci_ai_speech_input_location_t`type.

Fields

Field Description

`object_location`

(required)

### DBMS_CLOUD_OCI_AI_SPEECH_OBJECT_LOCATION_TBL Type

Nested table type of dbms_cloud_oci_ai_speech_object_location_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_SPEECH_OBJECT_LIST_INLINE_INPUT_LOCATION_T Type

Use this locationType when passing the WAV file name in the request.

Syntax
```

```

`dbms_cloud_oci_ai_speech_object_list_inline_input_location_t`is a subtype of the`dbms_cloud_oci_ai_speech_input_location_t`type.

Fields

Field Description

`object_locations`

(required) A list of ObjectLocations.

### DBMS_CLOUD_OCI_AI_SPEECH_PROFANITY_TRANSCRIPTION_FILTER_T Type

Profanity transcription filter to recognize profane words.

Syntax
```

```

`dbms_cloud_oci_ai_speech_profanity_transcription_filter_t`is a subtype of the`dbms_cloud_oci_ai_speech_transcription_filter_t`type.

Fields

Field Description

`l_mode`

(required) - `MASK`: Will mask detected profanity in transcription. - `REMOVE`: Will replace profane word with * in transcription. - `TAG`: Will tag profane word as profanity but will show actual word.

Allowed values are: 'MASK', 'REMOVE', 'TAG'

### DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_JOB_T Type

Description of Transcription Job.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`display_name`

(optional) A user-friendly display name for the job.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the job.

`description`

(optional) A short description of the job.

`model_details`

(required)

`normalization`

(optional)

`time_accepted`

(optional) Job accepted time.

`time_started`

(optional) Job started time.

`time_finished`

(optional) Job finished time.

`total_tasks`

(optional) Total tasks in a job.

`outstanding_tasks`

(optional) Total outstanding tasks in a job.

`successful_tasks`

(optional) Total successful tasks in a job.

`ttl_in_days`

(optional) Time to live duration in days for Job. Job will be available till max 90 days.

`percent_complete`

(optional) How much progress the operation has made, vs the total amount of work that must be performed.

`input_location`

(required)

`output_location`

(required)

`created_by`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the job.

`additional_transcription_formats`

(optional) Transcription format. JSON format will always be provided in addition to any formats in this list.

Allowed values are: 'SRT'

`lifecycle_state`

(optional) The current state of the Job.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'CANCELING', 'CANCELED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace-1\": {\"bar-key-1\": \"value-1\", \"bar-key-2\": \"value-2\"}, \"foo-namespace-2\": {\"bar-key-1\": \"value-1\", \"bar-key-2\": \"value-2\"}}`.

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`.

### DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_JOB_SUMMARY_T Type

Summary of the Transcription Job.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the job.

`display_name`

(required) A user-friendly display name for the job.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment where you want to create the job.

`created_by`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the user who created the job.

`percent_complete`

(optional) How much progress the operation has made, vs the total amount of work that must be performed.

`time_accepted`

(optional) Job accepted time.

`time_started`

(optional) Job started time.

`time_finished`

(optional) Job finished time.

`total_tasks`

(optional) Total number of tasks in a job.

`outstanding_tasks`

(optional) Total outstanding tasks in a job.

`successful_tasks`

(optional) Total successful tasks in a job.

`lifecycle_state`

(optional) The current state of the Speech Job.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace-1\": {\"bar-key-1\": \"value-1\", \"bar-key-2\": \"value-2\"}, \"foo-namespace-2\": {\"bar-key-1\": \"value-1\", \"bar-key-2\": \"value-2\"}}`.

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`.

### DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_JOB_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ai_speech_transcription_job_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_JOB_COLLECTION_T Type

Results of a Transcription Job search. Contains both TranscriptionJobSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of transcription jobs.

### DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_TASK_T Type

Description of Transcription Task.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the task.

`display_name`

(optional) A user-friendly display name for the task.

`time_started`

(optional) Task started time.

`time_finished`

(optional) Task finished time.

`percent_complete`

(optional) How much progress the operation has made, vs the total amount of work that must be performed.

`ttl_in_days`

(optional) Time to live duration in days for tasks. Task will be available till max 90 days.

`model_details`

(optional)

`audio_format_details`

(optional)

`file_size_in_bytes`

(optional) Size of input file in Bytes.

`file_duration_in_seconds`

(optional) Duration of input file in Seconds.

`processing_duration_in_seconds`

(optional) Task proccessing duration, which excludes waiting time in the system.

`input_location`

(optional)

`output_location`

(optional)

`lifecycle_state`

(optional) The current state of the Task.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'CANCELED'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_TASK_SUMMARY_T Type

Summary of the Transcription Task.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the task.

`display_name`

(required) A user-friendly display name for the task.

`percent_complete`

(optional) How much progress the operation has made, vs the total amount of work that must be performed.

`file_size_in_bytes`

(optional) Size of input file in Bytes.

`file_duration_in_seconds`

(optional) Duration of input file in Seconds.

`processing_duration_in_seconds`

(optional) Task proccessing duration, which excludes waiting time in the system.

`time_started`

(optional) Task started time

`time_finished`

(optional) Job finished time

`lifecycle_state`

(optional) The current state of the Speech Job.

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

### DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_TASK_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_ai_speech_transcription_task_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_TASK_COLLECTION_T Type

Results of a Transcription Task search. Contains both TranscriptionTaskSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of Transcription Task.

### DBMS_CLOUD_OCI_AI_SPEECH_UPDATE_TRANSCRIPTION_JOB_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly display name for the job.

`description`

(optional) A short description of the job.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace-1\": {\"bar-key-1\": \"value-1\", \"bar-key-2\": \"value-2\"}, \"foo-namespace-2\": {\"bar-key-1\": \"value-1\", \"bar-key-2\": \"value-2\"}}`.

- [AI Speech Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-A2E2711E-2111-48AA-B18C-B6A4DB442018)
- [DBMS_CLOUD_OCI_AI_SPEECH_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-FC73EFA9-D99C-4E1A-BCB2-F035D2490D6D)
- [DBMS_CLOUD_OCI_AI_SPEECH_AUDIO_FORMAT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-A92AAC26-8184-4776-A590-1E9C8801157F)
- [DBMS_CLOUD_OCI_AI_SPEECH_CHANGE_TRANSCRIPTION_JOB_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-1E05EDDE-9F3D-4A93-82E0-D1971B534CD8)
- [DBMS_CLOUD_OCI_AI_SPEECH_DIARIZATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-0EE1DE6C-5B60-4DC1-982C-55D7F54634BE)
- [DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_SETTINGS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-F41FA550-655D-4A64-8E56-5484A35B5331)
- [DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_MODEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-DB06A2E9-4EE3-4C1B-B6AD-8439924D2468)
- [DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-DF53023D-B3B3-4055-BB39-3B524DF33030)
- [DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_FILTER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-F2077005-394A-4304-9195-B1F4C1E6610C)
- [DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_NORMALIZATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-B111AEDB-7002-462A-A9A8-2DDFF6F9C56B)
- [DBMS_CLOUD_OCI_AI_SPEECH_INPUT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-03863F78-5590-4E78-8AAD-075449E599A3)
- [DBMS_CLOUD_OCI_AI_SPEECH_OUTPUT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-9C84732A-B228-408A-B0F2-80ED10E03FC5)
- [DBMS_CLOUD_OCI_AI_SPEECH_CREATE_TRANSCRIPTION_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-F3FAEE7E-C4EC-4044-A846-50B4C8F0486D)
- [DBMS_CLOUD_OCI_AI_SPEECH_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-E69141F7-BD95-4DAB-9BEE-F07BC1126451)
- [DBMS_CLOUD_OCI_AI_SPEECH_OBJECT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-38A5F5C5-CB1D-4CC5-A8BD-302BED3E819F)
- [DBMS_CLOUD_OCI_AI_SPEECH_OBJECT_LIST_FILE_INPUT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-6AAF2549-10B2-497A-B132-058340E3C0BF)
- [DBMS_CLOUD_OCI_AI_SPEECH_OBJECT_LOCATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-562BD779-5E29-43AD-A1B0-E4D52B812EFF)
- [DBMS_CLOUD_OCI_AI_SPEECH_OBJECT_LIST_INLINE_INPUT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-50A27BC6-8611-407F-97BB-D03A87BE670B)
- [DBMS_CLOUD_OCI_AI_SPEECH_PROFANITY_TRANSCRIPTION_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-FAFA1D07-79B4-42A0-803E-BCB9333F52BA)
- [DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_JOB_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-22756018-DBEC-42B8-BF31-2A36FD5D1EEC)
- [DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_JOB_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-17626347-4B1D-4C47-827C-84CACC0D9832)
- [DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_JOB_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-03831C53-0669-41D0-98BD-2DC3E24005C8)
- [DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_JOB_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-5B388C9F-CDEA-4C46-8802-9F0A842115A7)
- [DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-1615DB77-E463-4448-B218-6F1A14650604)
- [DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_TASK_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-CFBAB3E2-8566-4729-BF66-4F93600735D2)
- [DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_TASK_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-2B9481E2-1B28-4787-9F14-868B9499EA0B)
- [DBMS_CLOUD_OCI_AI_SPEECH_TRANSCRIPTION_TASK_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-7C1E214A-ACD6-4C21-B884-CCF6D0DD5874)
- [DBMS_CLOUD_OCI_AI_SPEECH_UPDATE_TRANSCRIPTION_JOB_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/ai_speech_t.html#ADSDK-GUID-F8CD8CF8-6579-4D18-B944-6BECB4D3E522)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
