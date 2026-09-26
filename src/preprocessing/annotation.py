def add_gene_annotation(variants, annotation_data):
    """
    Add gene information to each variant.

    annotation_data should be a dictionary where the key is
    a variant identifier and the value is the gene name.
    """

    annotated_variants = []

    for variant in variants:
        variant_id = (
            variant["chromosome"],
            variant["position"],
            variant["reference"],
            variant["alternate"]
        )

        gene = annotation_data.get(variant_id, "Unknown")

        variant["gene"] = gene

        annotated_variants.append(variant)

    return annotated_variants
