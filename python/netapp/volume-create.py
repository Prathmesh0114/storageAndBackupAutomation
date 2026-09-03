import argparse
import os
import re
import sys

from dotenv import load_dotenv


load_dotenv()


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Create a NetApp ONTAP volume"
    )

    parser.add_argument(
        "--svm",
        required=True,
        help="SVM name"
    )

    parser.add_argument(
        "--volume",
        required=True,
        help="Name of the volume"
    )

    parser.add_argument(
        "--size",
        required=True,
        help="Volume size, e.g. 500GB or 1TB"
    )

    return parser.parse_args()


def validate_environment():
    required_variables = [
        "NETAPP_HOST",
        "NETAPP_USERNAME",
        "NETAPP_PASSWORD"
    ]

    missing = []

    for variable in required_variables:
        if not os.getenv(variable):
            missing.append(variable)

    if missing:
        print("ERROR: Missing environment variables:")
        for variable in missing:
            print(f"  - {variable}")

        sys.exit(1)


def validate_volume_name(volume_name):
    pattern = r"^[A-Za-z0-9_-]+$"

    if not re.match(pattern, volume_name):
        print(
            "ERROR: Invalid volume name. "
            "Use only letters, numbers, '-' and '_'."
        )
        sys.exit(1)


def parse_size(size):
    pattern = r"^(\d+)(GB|TB)$"

    match = re.match(pattern, size.upper())

    if not match:
        print("ERROR: Invalid size format.")
        print("Example: 500GB or 1TB")
        sys.exit(1)

    value = int(match.group(1))
    unit = match.group(2)

    if unit == "GB":
        size_bytes = value * 1024 ** 3
    else:
        size_bytes = value * 1024 ** 4

    return size_bytes


def main():

    args = parse_arguments()

    print("\n=== NetApp Volume Provisioning ===")

    print(f"SVM       : {args.svm}")
    print(f"Volume    : {args.volume}")
    print(f"Size      : {args.size}")

    validate_environment()

    validate_volume_name(args.volume)

    size_bytes = parse_size(args.size)

    print(f"Size Bytes: {size_bytes}")

    print("\n[1/7] Validating SVM...")
    print(f"SVM '{args.svm}' validation placeholder")

    print("\n[2/7] Validating volume name...")
    print("Volume name validation successful")

    print("\n[3/7] Checking available capacity...")
    print("Capacity check placeholder")

    print("\n[4/7] Creating volume...")
    print("Volume creation placeholder")

    print("\n[5/7] Applying snapshot policy...")
    print("Snapshot policy placeholder")

    print("\n[6/7] Applying export policy...")
    print("Export policy placeholder")

    print("\n[7/7] Verifying volume...")
    print("Volume verification placeholder")

    print("\nResult: AUTOMATION FRAMEWORK READY")


if __name__ == "__main__":
    main()