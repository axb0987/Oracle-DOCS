# System Status
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm
- Fetched: 2026-09-05 02:10 CDT

# System Status

The Oracle Cloud Infrastructure Status service allows you to see the status of OCI services in a region on a dashboard, and query service status programmatically.
Note  
  
The Oracle Cloud Infrastructure Status dashboard shows service outages at the service or region level. Outages specific to a customer are communicated to the customer with[Console Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements.htm).

## Service Highlights

- View a dashboard that shows the health of services in a region.
- See event information, and a history of events.
- Programmatically query the status of services.
- You can access the status dashboard from a provided URL.

## Status Dashboard

The Status Dashboard shows the health of each individual service in a realm. The Status Dashboard page is auto-refreshed every 5 minutes. To view the status for a region group, select the corresponding tab at the top of the dashboard panel.
  
  

### Status Icons
Services displayed in the dashboard can show the following types of status indicator icons:
- Normal Performance : The service is available and operating within normal parameters. This status won't have an associated event report.
- Informational : Useful information regarding service performance is available.
- Service Disruption : The service is reporting a high number of request failures, resulting in the service being unavailable some of the time. This status has an associated event report.
- Service Down : The service is not available. This status has an associated event report.
- Dash (-): Service not available in the region.
Tip  
  
Click on a , , or icon to view the associated event report. Learn more about[event reports](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#status_service_topic_Incidents).

### To view the Status dashboard:
- 

For commercial regions, open a browser and navigate to[https://ocistatus.oraclecloud.com/](https://ocistatus.oraclecloud.com/).

For government regions, open a browser and navigate to[https://gov.ocistatus.com/](https://gov.ocistatus.com/).
Tip  
  
Bookmark the URL for future reference.

## Service Events

The History provides detailed event reports for each service that experiences degraded, partial, or complete outage conditions. Filter events by Services and Regions . You can obtain information for both current events and those that occurred in the past up to today's date. Use the Date Range selector to view past events.

You can access the History from the Status Dashboard, and you can also subscribe to RSS notifications about events and updates.

### Event Details

The following information is available for each event. Some types of information won't be immediately available but are added as the event is investigated, addressed, and closed:
- Title: A short description of the location, affected services, and reference number for the event.
- Event Status: The current mitigation status of the event. Options are Investigating , Identified , Monitoring , and Resolved .
- Message: Informative messages from the Oracle Cloud Infrastructure team about the event and action being taken to resolve the event.
- Customer Impact: Details about the effects that customers might see in their services as a result of the event.
- Reference Number: A unique reference number identifying the event.
- Start Time: (Included if known) The date and time that the event first occurred, shown in UTC format. For example: January 17, 2021, 17:35 UTC
- End Time: (Included if known) The date and time that the event was resolved, shown in UTC format. For example: January 18, 2021, 05:29 UTC
- Next Update: The estimated time that you can expect an event update, shown in UTC format. For example: January 18, 2021, 10:30 UTC
- Preliminary Root Cause: (When determined) A summary of the preliminary root cause of the event.

[To view service events](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#)

- Open a browser and navigate to[https://ocistatus.oraclecloud.com/](https://ocistatus.oraclecloud.com/)for commercial regions, or[https://gov.ocistatus.com/](https://gov.ocistatus.com/)for government regions.
- Select History in the upper-right corner of the menu bar.
- Use the Services and Regions filters to find an event for a specifc service, or within a specified region.
- Select the directional arrows to Select a Date Range you want to view.
- Select View More to see Event Details related to the event.

[To subscribe to RSS notifications about status updates](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#)

Note  
  

- When you subscribe, you receive all notifications for all services and regions.
- 

For commercial regions, open a browser and navigate to[https://ocistatus.oraclecloud.com/](https://ocistatus.oraclecloud.com/).

For government regions, open a browser and navigate to[https://gov.ocistatus.com/](https://gov.ocistatus.com/).
- Select RSS in the upper-right corner of the menu bar.
- Copy the RSS feed URL link. Open your RSS reader and follow the instructions to load the Status feed URL.

## Programmatically Accessible Status Reports

The status service provides JSON file reports that you can download:
- Summary Report: Shows the current status of every service and region.

Download this report:[https://ocistatus.oraclecloud.com/api/v2/components.json](https://ocistatus.oraclecloud.com/api/v2/components.json)
- Status Report: Shows a high-level status for all systems.

Download this report:[https://ocistatus.oraclecloud.com/api/v2/status.json](https://ocistatus.oraclecloud.com/api/v2/status.json)

### JSON File Contents and Syntax

Expand to view an example of each report JSON file, and a table of syntax definitions:

[Example of the Summary Report JSON File](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#)

Note  
  
This example shows a shortened sample of the report contents. To see the full report, download it from the provided URL.
```

```

TBD
Field Name Definition Type Examples
`realm`The Oracle Cloud Infrastructure realm string

`"OC1", "OC2"`

A realm is a logical collection of regions. Realms are isolated from each other and do not share any data.
`regionHealthReports`Heath reports grouped by region. array See preceding[Summary Report JSON file](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#status_service_topic_programmatic_access__summary_json).
`regionId`Unique identifier for a region string Numeric, dash-separated value
`regionName`The region name string US East (Ashburn) See[About Regions and Availability Domains](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm#About)for more information.
`regionCanonicalName`The canonical name of the region, used for search consistency string`account-management-and-billing`
`geographicAreaName`The geographic group the region is in string`"Americas", "Europe"`
`serviceHealthReports`Heath reports grouped by service array See preceding[Summary Report JSON file](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#status_service_topic_programmatic_access__summary_json).
`serviceId`Unique identifier for a service string Numeric, dash-separated value
`serviceName`The name of a specific service string`"Autonomous AI Lakehouse", "File Storage", "Virtual Cloud Networks"`
`serviceCanonicalName`The canonical name of the service, used for search consistency string`account-management-and-billing`
`serviceCategoryId`Unique identifier for a service category string Numeric, dash-separated value
`serviceCategoryName`The category the service belongs to. Each service is grouped in the same service category as in Console home page. string`"Compute", "Storage", "Analytics", "Database", "Networking"`
`serviceStatus`The current status of the service string`Normal Performance, Informational, Service Disruption, Service Down`
`incidents`Events reported by the service array See preceding[Summary Report JSON file](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#status_service_topic_programmatic_access__summary_json).
`incidentId`Unique identifier for an event string OCID (Oracle Cloud Identifier)
`severity`The event severity string`Normal Performance, Informational, Service Disruption, Service Down`

[Example of the Status Report JSON File](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#)

```

```

TBD
Field Name Definition Type Examples
`page`The status report page. array See preceeding[Example of the Status Report JSON File](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#status_service_topic_programmatic_access__status_json).
name The status report name. string "OCI"
`updated_at`

Report creation time in ISO 8601 format.

Expressed as`<date> T <time>`string

`"updated_at": "2021-09-18`

`T19:55:47.204985"`
`status`The high-level status of all systems. array See preceeding[Example of the Status Report JSON File](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/status-service.htm#status_service_topic_programmatic_access__status_json).
`indicator`The current status of all systems. string

`critical`

`major`

`minor`

`none`
`description`A description of the current status of all systems. string

Critical Service Outage

Major Service Outage

Minor Service Outage
