 # osmtodb - Extracting Bicycle Shops from OpenStreetMap Data and Storing in SQLite Database

Welcome to the `osmtodb` project, a Python application designed for extracting bicycle shops from an OpenStreetMap (OSM) map file and storing their locations in a SQLite database. This tool serves as a practical example of working with OSM data using Python.

## Project Overview

The `osmtodb` project uses the [osmium](https://github.com/openstreetmap-carto/osmium) library for parsing OSM files and the [SQLAlchemy](https://www.sqlalchemy.org/) ORM for interacting with a SQLite database. The application provides a simple command-line interface to filter and store bicycle shops in a database.

## Installation

To install the required packages, run the following command:

```bash
pip install -r Pipfile
```

## Usage

Run the `testit.py` script with your OSM file name as an argument. For example:

```bash
python testit.py bicycleshops
```

The script will create a SQLite database named `bicycleshops.db` and store all bicycle shops found in the given OSM file in the database's `locations` table.

## Testing API

To test the stored data, run the `testapi.py` script:

```bash
python testapi.py
```

This script will fetch the nearest bicycle shop to the coordinates (52.21395053208327, 6.89347062803371) and print its details.

## Contributing

We welcome contributions from the community. To get started, please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or concerns, feel free to open an issue or contact the project maintainer at your convenience.

We hope you find `osmtodb` useful in your OSM data processing needs! Happy coding!