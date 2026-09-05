# Monitoring a Work Request for a Deleted Tag
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_monitor_a_work_request_for_a_deleted_tag.htm
- Fetched: 2026-09-05 03:07 CDT

# Monitoring a Work Request for a Deleted Tag

Monitor the work request for a deleted tag key definition.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_monitor_a_work_request_for_a_deleted_tag.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_monitor_a_work_request_for_a_deleted_tag.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces_topic-To_monitor_a_work_request_for_a_deleted_tag.htm#)
- 

- On the Tag namespaces list page, select the namespace that you want to work with. If you need help finding the list page, see[Listing Tag Namespaces](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/../Common/../Concepts/list-tagnamespace.htm).
- To track the progress of the tag key definitions you deleted, from the Actions menu at the top of the Tag namespace details page, select View work requests .
- 

This task can't be performed using the CLI.
- 

Use these API operations to manage work requests spawned by the DeleteTag operation:
- [ListTaggingWorkRequests](https://docs.oracle.com/iaas/api/#/en/identity/latest/TaggingWorkRequestSummary/ListTaggingWorkRequests)
- [ListTaggingWorkRequestErrors](https://docs.oracle.com/iaas/api/#/en/identity/latest/TaggingWorkRequestErrorSummary/ListTaggingWorkRequestErrors)
- [ListTaggingWorkRequestLogs](https://docs.oracle.com/iaas/api/#/en/identity/latest/TaggingWorkRequestLogSummary/ListTaggingWorkRequestLogs)
- [GetTaggingWorkRequest](https://docs.oracle.com/iaas/api/#/en/identity/latest/TaggingWorkRequest/GetTaggingWorkRequest)
