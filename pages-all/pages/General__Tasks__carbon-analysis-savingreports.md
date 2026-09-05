# Creating User Reports
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Tasks/carbon-analysis-savingreports.htm
- Fetched: 2026-09-05 02:11 CDT

# Creating User Reports

You can create your own Carbon Emissions Analysis user reports based on any of the included default reports.

You can create a user report by changing one of the predefined Carbon Emissions Analysis Default Reports , and then save the custom settings as a new user report. The new reports can have their own set of filters, grouping dimension, date range, calculation method, and carbon emissions factor settings. You can also create new user reports based on user reports you have already created.

You can later access the report after leaving the Console and returning to Carbon Emissions Analysis, without needing to redo your preferred date range, filters, or grouping dimension. After a report has been saved, it can be accessed on the User Reports page. A maximum of 50 reports can be saved.

New user reports can be created on the Carbon Emissions Analysis page, User Reports page, or any of the Default Reports detail pages. The following example uses the Carbon Emissions Analysis page as the starting context.

- Open the navigation menu and select Governance &amp; Administration . Under Emissions Management , select Carbon Emissions Analysis .

The Carbon emissions analysis page opens and displays the Location-based Carbon Footprint by Service default report with applied filters on the Report details tab.
- In Applied filters , make your preferred filter changes. See[Viewing Carbon Emissions Reports](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/carbon-analysis-viewreports.htm)for more information on viewing reports and an explanation of the report fields. The filter settings you change are carried over into the new user report.

Note  
  
You can create either change filters on existing report and then create a new report, or you can select Create new user report and change filter settings later.
- When you're done making changes, select Create new user report .
- In the Create carbon emissions report panel, enter the report name in the required Report name field. Avoid entering confidential information.

A preview of the chart is displayed underneath the new user report settings. As you adjust report settings, the chart is automatically redisplayed.
- In Report template , you can use the selected predefined default report template or another as a starting point:

- Location-based Carbon Footprint by Service
- Market-based Carbon Footprint by Service
- Carbon Footprint by Service and Description
- Carbon Footprint by Service and SKU
- Location-based Carbon Footprint by Region
- Market-based Carbon Footprint by Region
- Carbon Footprint by Region
- In Calculation method , specify whether the report is Power-based or Spend-based .

- Spend-based : The amount a customer spends on a particular service. These calculations are based on the customer cost before discounts and the[Oracle Clean Cloud OCI Data Sheet](https://www.oracle.com/a/ocom/docs/corporate/citizenship/clean-cloud-oci.pdf).
- Power-based : The amount of power consumed (in kWh) by service workloads, which further satisfies GHG protocol guidelines, and EU and UK regulations on carbon emissions reporting.
- (Power-based calculation only) In Carbon emissions factor , specify whether the report is Location-based or Market-based .

- Location-based emissions : Emissions that are based directly on the region's power grid. While typically some level of emissions are emitted, certain location's emissions can be 100% renewable, depending on the location's power grid.
- Market-based emissions : Emissions that include any renewable energy certificates or renewable grid purchases. For example, European regions have market-based zero carbon emission factors.
Note  
  
When selecting the Spend-based calculation method, only Market-based emissions emissions are applicable.
- In Grouping dimension , select how the data is visualized in terms of a particular grouping.
- In Chart type , select either Bars or Lines .
- In Chart granularity , select either Monthly or Daily .
- In Chart scope , select either Not cumulative or Cumulative to specify whether the values are to be cumulative for the specified time period.
- Select Create report .

A notification is displayed that your report has been successfully created, and the report details are shown on the User Reports page.

The new saved report is now available for future selection from the User Reports page.

After a user report has been created, you can rename it, update it, or delete it.

[To rename a report](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/carbon-analysis-savingreports.htm#)

- Select the report from the User Reports page.
- Select Edit report properties .
- In the Edit report properties panel, enter the new name in the Name field. Avoid entering confidential information.
- Select Preview .

A notification is displayed on the report details page stating that the changes need to be saved.
- Select Save .

The report reloads to display the changes.

[To reset in-progress report changes](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/carbon-analysis-savingreports.htm#)

After changing any report (the default Location-based Carbon Footprint by Service, user report, or default report), from the Actions menu, select Reset .

The chart reloads to display the previous settings.

[To update a user report](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/carbon-analysis-savingreports.htm#)

- Select the report from the User Reports page.
- On the user report details page, make the preferred filter changes in Applied filters , or select Edit report properties to make name, grouping dimension, calculation method, or carbon emissions factor changes in the Edit report properties panel.
- Select Preview .

A notification is displayed on the report details page stating that the changes need to be saved.
- Select Save .

The chart is updated with the new settings.

[To delete a report](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/carbon-analysis-savingreports.htm#)

- Select the report from the User Reports page.
- From the Actions menu, select Delete .
-
