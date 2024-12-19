"""Transformation script to convert CMDR schema to new, extendable schema"""
from linkml_map.datamodel.transformer_model import TransformationSpecification, ClassDerivation, SlotDerivation
from linkml_runtime.utils.formatutils import camelcase, underscore
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.utils.schemaview import SchemaView
from pathlib import Path


REPO_ROOT = Path.cwd().parent.parent


def get_source_class_derivations(target_schemaview) -> dict:
    """
    Function to get BDC class definitions

    :param target_schemaview: SchemaView object
    :param subset_classes: List of classes to subset
    :return: Dictionary of class derivations incl slot derivations
    """
    # Example implementation to fetch class definitions
    # This should be replaced with the actual implementation
    class_derivations ={}
    subset_classes = target_schemaview.all_classes()
    for class_name in subset_classes:
        class_derivation = ClassDerivation(populated_from=class_name,
                                           name=camelcase(class_name))
        induced_slots = target_schemaview.class_induced_slots(class_name)
        for slot in induced_slots:
            slot_derivation = SlotDerivation(populated_from=slot.name, name=underscore(slot.name))
            class_derivation.slot_derivations[underscore(slot.name)] = slot_derivation
        class_derivations[camelcase(class_name)] = class_derivation
    return class_derivations


def main():
    """Main function to convert CMDR schema to new schema."""
    schema_path = REPO_ROOT / "src" / "cmdr" / "schema" / "cmdr.yaml"  # Use quotes to denote string literals
    cmdr_sv = SchemaView(schema_path)
    class_derivations = get_source_class_derivations(target_schemaview=cmdr_sv)
    ts = TransformationSpecification(class_derivations=class_derivations)
    ts.title = "CMDR to clinical studies schema transformation"
    ts.id = "cmdr_to_clinical_studies_schema"
    yaml_dumper.dump(ts, "cmdr_to_clinical_studies_schema_transformation_spec.yaml")


if __name__ == "__main__":
    """Entry point for the script."""
    main()