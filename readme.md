# IBM Anti-Money Laundering Dataset Pipeline

This project automates the download, transformation, and loading of the IBM AML transactions dataset.

## Structure

- `scripts`: Python scripts for each stage
- `data/`: Organized folder for raw and processed datasets (excluded from Git)
- `sql/`: (Coming soon) Schema and queries for SQL loading
- `notebooks/`: (coming soon) Exploration and visualization

## Scripts

- `aml_dataset_downloader.py`: Downloads ands copies the dataset locally
- `transform_data.py`: Validates and splits the dataset into chunks

## Setup

```bash
pip install -r requirements.txt