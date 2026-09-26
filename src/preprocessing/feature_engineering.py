def create_features(variants):
    """
    Convert annotated variants into a feature-ready format
    for machine learning.
    """

    features = []

    for variant in variants:
        feature = {
            "chromosome": variant.get("chromosome"),
            "position": int(variant.get("position")),
            "reference": variant.get("reference"),
            "alternate": variant.get("alternate"),
            "gene": variant.get("gene", "Unknown")
        }

        features.append(feature)

    return features
