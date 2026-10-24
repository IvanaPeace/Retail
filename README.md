# Online Retail Data Quality Investigation

## Dataset

UCI Online Retail dataset. Chen, D. (2015). Online Retail [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33.

## Objective

Investigate the quality of the transaction data and produce a cleaned
version suitable for further analysis.

## Initial dataset

Rows: 541,909
Columns: 8

## Data quality findings

- 135,080 records have a missing CustomerID.
- 1,454 records have a missing Description.
- 5,268 exact duplicate rows were identified.
- 10,624 records have negative quantities.
- 2,515 records have a UnitPrice of £0.

## Cleaning performed

- Exact duplicate rows were removed.
- Missing CustomerID values were retained because they may represent
  legitimate transactions.
- Negative quantities were retained because they may represent
  cancellations, returns or adjustments.
- Zero-price records were retained because they may have legitimate
  business meaning.

## Output

The cleaned dataset is stored in:

data/processed/Online Retail_cleaned.xlsx