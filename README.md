Area of the French wine cepages per year.

## Data

Data is extracted from the [Observatoire de la viticulture française](http://www.observatoire-viti-france.com) maintained by FranceAgriMer.

The data is provided as CSV.

The columns are :

* **type_cepage**: String, Cepage type
* **surface_ha**: Number, Surface (in hectares)
* **wine_surface_proportion**: Number, Cepage proportion for wine
* **year**: Integer, Year of the data

A quick inspection will show you that sometimes, there are some accuracy issue or missing data.

Sometimes, for some cepages, you will have non existing value a year and a year later, you will have 400 ha area like for `SAUVIGNON GRIS G`. We doubt that it can vary this much in one year.

## Preparation

This package include the scripts to automate data retrieving and filtering. it relies on various utilities like pdftohtml to extract PDF content, a Python script and varous Unix command line utilities. We do not warranty that it will work on Windows computer.

You just have to do the following

## License

This Data Package is licensed by its maintainers under the [Public Domain Dedication and License (PDDL)](http://opendatacommons.org/licenses/pddl/1.0/).

The web site credits in French (see below excerpt) do allow to reuse data for commercial uses.

> Les droits de reproduction ou de représentation sont réservés sur l’ensemble du site Internet. La reproduction d’une partie du site (cartes, tableaux, …) est autorisée sous réserve du respect des trois consignes suivantes :

>    * gratuité de la diffusion
>    * respect de l’intégrité des documents reproduits : pas de modifications ni altération d’aucune sorte
>    * citation claire et lisible des sources de données sur chaque document et de la provenance (Observatoire de la viticulture française - FranceAgriMer)

Moreover, the list from [Data.Gouv.fr](https://www.data.gouv.fr/fr/Redevances) concerning public datasets excluded from free access does not mentioned this dataset.

We plan to release the dataset under ODBL licence but you should be aware that the licence may change due to possible legacy requests.