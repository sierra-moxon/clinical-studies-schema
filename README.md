# clinical-studies-schema

sample schema that uextends CMDR using LinkML-map.

## Website

[https://sierra-moxon.github.io/clinical-studies-schema](https://sierra-moxon.github.io/clinical-studies-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [clinical_studies_schema](src/clinical_studies_schema)
    * [schema](src/clinical_studies_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/clinical_studies_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
