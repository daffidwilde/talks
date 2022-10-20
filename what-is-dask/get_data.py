"""A script for getting the NYC flights data.

The core functionality of this script was graciously adapted from
https://github.com/TomAugspurger/dask-tutorial-pycon-2018
"""

import os
import urllib.request
import tarfile


def main():
    """Download and decompress the NYC flights data."""

    flights_tar = os.path.join(".", "nycflights.tar.gz")
    flights_dir = os.path.join(".", "nycflights")

    if not os.path.exists(flights_tar):
        print("Downloading compressed dataset...", end="", flush=True)
        url = "https://storage.googleapis.com/dask-tutorial-data/nycflights.tar.gz"
        urllib.request.urlretrieve(url, flights_tar)
        print("done", flush=True)

    if not os.path.exists(flights_dir):
        print("Extracting data... ", end="", flush=True)
        with tarfile.open(flights_tar, mode="r:gz") as flights:
            flights.extractall(".")
        print("done", flush=True)

    print("Finished!")


if __name__ == "__main__":
    main()
