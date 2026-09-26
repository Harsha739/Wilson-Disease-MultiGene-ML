def filter_variants(variants):
    """
    Remove variants that do not have
    the basic information required for analysis.
    """

    filtered_variants = []

    for variant in variants:
        if (
            variant.get("chromosome")
            and variant.get("position")
            and variant.get("reference")
            and variant.get("alternate")
        ):
            filtered_variants.append(variant)

    return filtered_variants
