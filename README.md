## How Urban Is World Heritage? An Investigation of Built-up Area Increase in Cultural Heritage Properties

  This is the reporsitory of the project amd Journal paper 'How Urban Is World Heritage? An Investigation of Built-up Area Increase in Cultural Heritage Properties' published in the Land journal. It contains Steps, data and Results of the process resulting from the assessemtent of Built-up Area Increase in Cultural Heritage Properties in sampled 668 [UNESCOs World Heritage properties](https://whc.unesco.org/en/list/). 
To use it, follow the setup and instructions below.

## Summary
0.  [Workflow and Dataset](https://github.com/mkvusa/heritagezoning/blob/main/README.md#workflow-and-datasets)
01. [Requirements](https://github.com/mkvusa/heritagezoning/blob/main/README.md#1-requirements)
02. [Setup](https://github.com/mkvusa/heritagezoning/blob/main/README.md#2-setup)
03. [Files](https://github.com/mkvusa/heritagezoning/blob/main/README.md#3-files)
04. [Results figures](https://github.com/mkvusa/heritagezoning/tree/main/Figures_updated_202_june)
05. [Writting](https://github.com/mkvusa/heritagezoning/blob/main/README.md#4-writing)
06. [Acknownledge](https://github.com/mkvusa/heritagezoning/blob/main/README.md#5-acknowledgement)
07. [Further Reading](https://github.com/mkvusa/heritagezoning/blob/main/README.md#further-reading)

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

## 2. Setup
Depending on how the raw data is collected;
1. Group the properties in to folders of UNESCO regions i.e EUR, LAC, APA, AFR and ARB.
2. For each region group the shapefiles of the properties into categories of REPORT and NOT REPORTING for properties that are either reportinf or not reporting on urban developoment.
3. Use python or whatever works to match names of folders to names in the attribute excel sheet of the world heritage list downloadable from [UNESCO website](https://whc.unesco.org/en/syndication).
4. Use qGIS to merge the shapefiles by their regions and then edit the attribute table by adding the value Status, Showing"Reporting" or "Not Reporting"
5. Join the attrbutes of the attribute table from of the world heritage list to the merged shapefils in set up 3.
6. Provide core zones in shapefile format to DLR or use World Footprint layer evolution versio for assesment of Built-up change per year.

## 3. Files
##### `PUP.py`
This was the python script used to retrieved the World heritage shapefiles on the Protected Urban Planets Geodataset for decsion making on which database was suitable for analysis in the project. see results of the [assessment](https://github.com/mkvusa/heritagezoning/blob/main/Data%20Assessment.pptx) 


## 4. Writing
- Keep a set of continuously-updated slides reflecting the current state and vision of the project.
- Online LaTeX editing tools such as [Overleaf](https://www.overleaf.com/) are suffiecient for simultaneous editing and comments.
- Keep all `.bib` references organized in overleaf.

## 5. Acknowledgement
The workflows and datasets of this paper can be used under the [Creative Common License (Attribution CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Please give appropriate credit, such as providing a link to our paper or to this github repository. The copyright of all the downloaded and processed images belongs to the image owners.

## 6. Further Reading

Here is the link to [project report](https://docs.google.com/document/d/1z2x7LImbpOdwTfusMivY_bJPvH6AD3ctfQOXbscvRqc/edit)

Here is the link to the [Graphical Summary](https://docs.google.com/presentation/d/1FWlQp0J-vXN2YH4g35VbUQuPiCwq16CPVWzjlesev10/edit#slide=id.g120edecb748_2_261)

We are using Draw.IO for creating the diagrams of the project.

Here is a link to [project_data_assessment_process](https://drive.google.com/file/d/1P1xcFAEAEWp0NpKyCJqnSuvNw9EEZyqd/view?usp=sharing)
