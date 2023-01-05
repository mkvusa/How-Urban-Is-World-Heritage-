## Heritage Zoning and Urbanization: An Assessment of Urbanization Trends and Patterns in World Heritage Properties

  This is the reporsitory of the project amd Journal paper 'Heritage Zoning and Urbanisation: An Assessment of Urbanization Trends and Patterns in World Heritage Properties' published in the ISPRS International Journal of Geo-Information. It contains Steps, data and Results of the process resulting from the assessemtent of urbanisation trends and patterns in sampled 426 [UNESCOs World Heritage properties](https://whc.unesco.org/en/list/). 
To use it, follow the setup and instructions below.

## Summary
0.  Workflow
01. Requirements
02. Setup
03. Folders
04. Files
05. Leveraging on Github Capabilities
06. Writing
07. Journal Submissions
08. Principles
09. Further Reading

## Workflow and datasets
The work flow illustrate the step by step approach for this project. The original shapefiles were generated and collected from [The International Center on Space Technologies for Natural and Cultural Heritage (HIST)](http://www.unesco-hist.org/index.php?r=en/index) as such are not provided in this repository but can be accessed by request from the institution. The World Human Footprin layer evolution were processed and accessed through the [German Aerospace Center(DLR)](https://www.dlr.de/EN/Home/home_node.html) and can be dowloaded and processed by request through [German Aerospace Center(DLR)](https://geoservice.dlr.de/web/maps/eoc:wsfevolution).
The datasets provided in this repository are the results of the spatial temporal analysis of the World Human footprint layer in the world heritage properties showing the [built-up picxel count](https://github.com/mkvusa/heritagezoning/blob/main/_PixelCount_WSFEvo_ShapesNoBuffer_transposed_renamed.xlsx) of each year per property from the year 1985-2015. Additionally, these excel datasets show the [names of the World Heritage properties that were assessed in the by region and by category of reporting on urban development and not reporting on urban development](https://github.com/mkvusa/heritagezoning/delete/main/_PixelCount_WSFEvo_ShapesNoBuffer_transposed_renamed.xlsx).
![Workflow of the project](https://github.com/mkvusa/heritagezoning/blob/main/Regional%20maps/WorkFLow_HIST_new_edited.jpg)

## 1. Requirements

This workflow requires:
- [QGIS](https://www.qgis.org/fr/site/)[Free]
- [FME](https://www.safe.com/)[Licensed]
- [Python](https://www.python.org) [Free] 
- [LaTeX](https://www.latex-project.org) [Free]
- [Excel](https://www.microsoft.com/en-us/microsoft-365/excel)[Licensed]

Other great languages and softwares may also be used.
- [R](https://www.r-project.org) [Free]
- [Stata](https://www.stata.com) [Licensed]
- [ArcGIS](https://www.arcgis.com/index.html)[Licensed]

## Setup
Depending on how the raw data is collected;
1. Group the properties in to folders of uUNESCO regions i.e EUR, LAC, APA, AFR and ARB.
2. For each region group the shapefiles of the properties into categories of REPORT and NOT REPORTING for properties that are either reportinf or not reporting on urban developoment.
3. Use python or whatever works to match names of folders to names in the attribute excel sheet of the world heritage list downloadable from [UNESCO website](https://whc.unesco.org/en/syndication).
4. Use qGIS to merge the shapefiles by their regions and then edit the attribute table by adding the value Status, Showing"Reporting" or "Not Reporting"
5. Join the attrbutes of the attribute table from of the world heritage list to the merged shapefils in set up 3.

## Folders


## Files


## Leveraging on Github Capabilities


## Writing



## Journal Submissions



## Principles



## Further Reading



Here is the link to [project report](https://docs.google.com/document/d/1z2x7LImbpOdwTfusMivY_bJPvH6AD3ctfQOXbscvRqc/edit)

Here is the link to the [Graphical Summary](https://docs.google.com/presentation/d/1FWlQp0J-vXN2YH4g35VbUQuPiCwq16CPVWzjlesev10/edit#slide=id.g120edecb748_2_261)

We are using Draw.IO for creating the diagrams of the project.

Here is a link to [project_data_assessment_process](https://drive.google.com/file/d/1P1xcFAEAEWp0NpKyCJqnSuvNw9EEZyqd/view?usp=sharing)
