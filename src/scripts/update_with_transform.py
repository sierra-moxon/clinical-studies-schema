"""Transformation script to convert CMDR schema to new, extendable schema"""
import yaml
from linkml_map.datamodel.transformer_model import TransformationSpecification, ClassDerivation, SlotDerivation
from linkml_map.inference.schema_mapper import SchemaMapper
from linkml_runtime.utils.formatutils import camelcase, underscore
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.utils.schemaview import SchemaView
from pathlib import Path


REPO_ROOT = Path.cwd().parent.parent

def load_transformation_spec_from_yaml(yaml_path: Path) -> TransformationSpecification:
    """
    Loads a TransformationSpecification instance from a YAML file.

    :param yaml_path: Path to the YAML file containing the transformation specification.
    :return: An instance of TransformationSpecification.
    """
    # Load the YAML file content
    with yaml_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # Deserialize the YAML data into a TransformationSpecification instance
    ts = TransformationSpecification(**data)
    return ts


def main():
    """Main function to convert CMDR schema to new schema."""
    schema_path = REPO_ROOT / "src" / "cmdr" / "schema" / "cmdr.yaml"  # Use quotes to denote string literals
    cmdr_sv = SchemaView(schema_path)
    class_derivations_file = REPO_ROOT / "src" / "scripts" / "cmdr_to_clinical_studies_schema_transformation_spec.yaml"
    ts = load_transformation_spec_from_yaml(class_derivations_file)
    ts.title = "CMDR to clincal studies schema transformation"
    ts.id = "cmdr_to_clinical_studies_schema"

    yaml_dumper.dump(ts, "cmdr_to_clinical_studies_schema_transformation_spec.yaml")

    mapper = SchemaMapper()
    mapper.source_schemaview = cmdr_sv

    target_schema_obj = mapper.derive_schema(
        specification=ts,
        target_schema_id="cmdr-clinical-studies-schema-schema",
        target_schema_name="cmdr_clinical_studies_schema"
    )

    # ugly bit of hacking to demonstrate end-to-end functionality
    target_schema_obj.types = cmdr_sv.all_types()

    yaml_dumper.dump(target_schema_obj, "cmdr_clinical_studies_schema_schema.yaml")

if __name__ == "__main__":
    """Entry point for the script."""
    main()