import csv


def parse_vcf(vcf_file):
    """
    Read a VCF file and return variant information
    as a list of dictionaries.
    """

    variants = []

    with open(vcf_file, "r") as file:
        for line in file:

            # Ignore VCF header lines
            if line.startswith("#"):
                continue

            fields = line.strip().split("\t")

            if len(fields) < 5:
                continue

            variant = {
                "chromosome": fields[0],
                "position": fields[1],
                "id": fields[2],
                "reference": fields[3],
                "alternate": fields[4]
            }

            variants.append(variant)

    return variants


def save_variants(variants, output_file):
    """
    Save parsed variants as a CSV file.
    """

    if not variants:
        return

    fieldnames = variants[0].keys()

    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(variants)


if __name__ == "__main__":
    input_vcf = "data/raw/sample.vcf"
    output_csv = "data/processed/variants.csv"

    variants = parse_vcf(input_vcf)
    save_variants(variants, output_csv)

    print(f"Parsed {len(variants)} variants.")
