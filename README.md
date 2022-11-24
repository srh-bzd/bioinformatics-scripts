# bioinformatics-scripts

- [bioinformatics-scripts](#bioinformatics-scripts)
  * [gbk2table](#gbk2table)
  
## gbk2table

### Description
gbk2table.py is a python script to extract some information from a genbank format file, produced by the NCBI site, and return a table, into stdout or an output file, with all the information retrieved that is : 
- ACCESSION
- PUBMED
- DEFINITION
- /country
- /isolation_source or /note=*isolate_source
- /collection_date
- length in LOCUS line

### Usage
```
./gbk2table.py [-h] [-o OUTPUT_FILE] genbank_file
```
