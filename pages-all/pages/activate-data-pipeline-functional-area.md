# Activate a Data Pipeline for a Functional Area
- Source: https://docs.oracle.com/iaas/analytics-for-applications/doc/activate-data-pipeline-functional-area.html
- Fetched: 2026-09-05 18:59 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/analytics-for-applications/doc/activate-data-pipeline-functional-area.html#dcoc-content-body)

# Activate a Data Pipeline for a Functional Area

You must activate the data pipeline for a functional area to run it and load the data into the data warehouse.
Ensure that you don't activate a data pipeline for a functional area in the following situations:
- Load in progress: If an incremental load is in progress.
- An impending load: If an incremental load is scheduled to run in the next hour.
- Exceeded the number of daily refresh requests: The maximum number of ad hoc data refresh requests for the day is four. If you've exceeded this number, then you can submit a request the following day.
- Sign in to your service.
- In Oracle Fusion Data Intelligence Console , click Data Configuration under Application Administration .
- On the Data Configuration page, click your service. For example, under Applications, click Enterprise Resource Planning .
- On the service page, for example, the Data Configuration: Oracle Financial Analytics page, click the Action menu for the saved data pipeline for the functional area that you want to activate, and click Edit .
- Review the details of the data pipeline for the functional area and then click Activate .
  

  
[Description of the illustration fawag-activate-pipeline.png](https://docs.oracle.com/iaas/analytics-for-applications/doc/img_text/fawag-activate-pipeline.html)  

- In step 4 of the Data Configuration wizard, select Scheduled Execution Data to specify the date and time on which to run the data pipeline for the functional area. Select Run Immediately to create and run the data pipeline for the functional area immediately. Click Finish .
  

  
[Description of the illustration fawag-schedule-activation-pipeline.png](https://docs.oracle.com/iaas/analytics-for-applications/doc/img_text/fawag-schedule-activation-pipeline.html)  

Oracle Fusion Data Intelligence runs the data pipeline for the functional area, loads data into your data warehouse, and displays your data pipeline for the functional area on the Data Configuration page. Once data is successfully loaded, the system updates the status of the data pipeline for the functional area to Activation Completed .

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
