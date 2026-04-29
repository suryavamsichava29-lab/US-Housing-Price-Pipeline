# U.S. Housing Price Analytics Pipeline

### Project Overview
This project is an automated ETL (Extract, Transform, Load) pipeline designed to ingest, clean, and standardize U.S. housing market data. The pipeline handles data integrity issues such as duplicates and invalid entries, reducing manual data preparation time by approximately 40%.

### Technologies Used
* **Python**: Core logic and automation.
* **Pandas**: Data transformation, filtering, and schema validation.
* **Git/GitHub**: Version control and project management.

### Pipeline Features
1. **Extraction**: Automated ingestion of raw regional housing records (CSV format).
2. **Transformation**:
   * Removed duplicate property entries.
   * Corrected data types for bedroom counts (schema validation).
   * Filtered for 'Sold' status to focus on completed market transactions.
3. **Loading**: Exported processed, high-integrity data to a master analytical file (`master_housing_data.csv`).
