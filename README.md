# biosample-upload

## Overview

Implements a manager-worker model with AWS Lambda to parse and upload BioSample XML data into a PostgreSQL database.

## Database

Data is hosted on the Serratus PostgreSQL cluster, which is publicly accessible via any PostgreSQL client (e.g. pgAdmin)

- Endpoint: `serratus-aurora-20210215-cluster.cluster-ro-ccz9y6yshbls.us-east-1.rds.amazonaws.com`
- Database: `summary`
- Username: `public_reader`
- Password: `serratus`

Table: `biosample`
