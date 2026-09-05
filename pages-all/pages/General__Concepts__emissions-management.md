# Emissions Management
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/emissions-management.htm
- Fetched: 2026-09-05 02:10 CDT

# Emissions Management

Use the Carbon Emissions Analysis page to track the estimated carbon emissions footprint while using Oracle Cloud Infrastructure services.

## Carbon Emissions Analysis Overview

Carbon Emissions Analysis is an easy-to-use visualization tool that allows paying commercial OCI customers to track their estimated carbon emissions footprint. Charts and corresponding data tables or CSVs of carbon emissions usage can be generated, based on the selected carbon emissions factor, calculation method, time range, filters, and grouping dimensions.

OCI uses Green House Gas (GHG) protocol guidance to automate calculating carbon emissions for customers' purchased goods using the following calculation methods :
- Power-based : The amount of power consumed (in kWh) by service workloads, which satisfies GHG protocol guidelines, and EU and UK regulations on carbon emissions reporting. Power-based emissions track the power consumed by hardware in OCI data centers and then allocates energy to your resource workloads. Allocated energy considers both dedicated and shared hardware across customers. Allocated energy is then multiplied by a regional carbon emissions factor, which is based on the power grid mix of renewable and non-renewable energy.
- Spend-based : The amount a customer spends on a particular service, multiplied by a regional carbon emissions factor. These calculations are based on the customer cost before discounts and the[Oracle Clean Cloud OCI Data Sheet](https://www.oracle.com/a/ocom/docs/corporate/citizenship/clean-cloud-oci.pdf).

For the power-based calculation method only, two types of carbon emissions factors can be tracked in Carbon Emissions Analysis:
- Location-based emissions : Emissions that are based directly on the region's power grid. While typically some level of emissions are emitted, certain location's emissions can be 100% renewable, depending on the location's power grid.
- Market-based emissions : Emissions that include any renewable energy certificates or renewable grid purchases by Oracle, to offset emissions in such markets. For example, European regions have market-based zero carbon emission factors.
Note  
  
For usage associated with the European region, users can expect no usage data to appear (namely, zero carbon emissions) because all European data centers are powered by renewable sources. For more information, see the[Oracle Clean Cloud OCI Data Sheet](https://www.oracle.com/a/ocom/docs/corporate/citizenship/clean-cloud-oci.pdf).

Power-based calculations are more exact but are only supported by some OCI services. For other services, use spend-based calculations. Spend-based calculations support only the market-based emissions factor.
Important  
  
Carbon Emissions Analysis isn't intended to be used as a developer tool to reduce emissions. All customer carbon emissions provided by the OCI Carbon Emissions Analysis tool and[Usage API](https://docs.oracle.com/iaas/api/#/en/usage/)are estimates.

Carbon emission units in Carbon Emissions Analysis are expressed in terms of MTCO2e (Metric Tons Carbon dioxide equivalent).

You can use Carbon Emissions Analysis for spot checks of carbon emissions trends, and for generating reports. You can visualize emissions in charts, as tabular data, or download the data as a CSV file. For example, you can view carbon emissions by service and product description or SKU, view the carbon footprint by region, or view the location- or market-based carbon footprint by service. For more information, see[Viewing Carbon Emissions Reports](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Tasks/carbon-analysis-viewreports.htm).

By default, the Location-based Carbon Footprint by Service report is shown when the Carbon emissions analysis page first opens. When viewing this report and others you can filter by specific dates, compartments, regions, services, tags, or tenancies.

On the User Reports page, you can create and view[new user reports](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Tasks/carbon-analysis-savingreports.htm)based on one of the predefined default templates, and select the calculation method (whether power- or spend-based) and carbon emissions factor (location- or market-based). You can then pick how you want the data grouped in terms of a particular grouping dimension, chart type, chart scope, and granularity (monthly or daily).

On the Default Reports page, you can view one of the predefined default reports, where the reports are listed by name and calculation method (power- or spend-based).

See[Viewing Carbon Emissions Reports](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Tasks/carbon-analysis-viewreports.htm)for more information on viewing reports and the related Carbon Emissions Analysis query settings. See[Creating User Reports](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Tasks/carbon-analysis-savingreports.htm)for more information on creating your own reports.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).

To use Carbon Emissions Analysis, the following policy statements are required:
```

```

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).
