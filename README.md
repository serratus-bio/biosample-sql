# biosample-sql

## Overview

Implements a manager-worker model with AWS Lambda to parse and upload BioSample XML data into a PostgreSQL database.

## Database

Data is hosted on the Serratus PostgreSQL cluster, which is publicly accessible via any PostgreSQL client (e.g. pgAdmin)

- Endpoint: `serratus-aurora-20210223.cluster-ro-ccz9y6yshbls.us-east-1.rds.amazonaws.com`
- Database: `summary`
- Username: `public_reader`
- Password: `serratus`

Tables of interest:

- `biosample` (n=16,553,836)
- `biosample_geocode` (n=49,679)
- `biosample_geo_coordinates` (n=5,306,144)
- `srarun_geo_coordinates` (n=2,568,898)
