#!/usr/bin/env python3


import sys, argparse
from re import search

"""
USAGE
    ./gbk2table.py [-h] [-o <output_file>] <genbank_file> 
DESCRIPTION
    Python script to extract some information from a genbank format file, produced by the NCBI site, 
    and return a table with all the information retrieved that is : 
    ACCESSION, PUBMED, DEFINITION, /country, /isolation_source or /note=*isolate_source, /collection_date and length in LOCUS line.
PREREQUISITE
    - python3
    - A genbank file
AUTHOR :
    Sarah BOUZIDI - sarah.bouzidi@ird.fr
    Engineer in bioinformatics
    Centre National de la Recherche Scientifique (CNRS)
    Laboratory MIVEGEC, IRD, Montpellier
"""


def parse_gbk(input_file):
    """
    Function to parse input Genbank file and keep some information into a dict like : {accession : {"length" : , "definition" : , ...}}
    """
    genbankDict = dict()
    accession = None
    length = None
    for line in input_file:
        if line.startswith("LOCUS"):
            accession = line.strip().split()[1]
            length = int(line.strip().split()[2])
            passLineAccession = False
            genbankDict[accession] = {}
            genbankDict[accession]["length"] = length
            genbankDict[accession]["definition"] = "NA"
            genbankDict[accession]["pubmed"] = "NA"
            genbankDict[accession]["country"] = "NA"
            genbankDict[accession]["source"] = "NA"
            genbankDict[accession]["date"] = "NA"
        if line.startswith("ACCESSION"):
            passLineAccession = True
        if line.startswith("DEFINITION"):
            genbankDict[accession]["definition"] = line.strip().replace("DEFINITION  ", "")
        if genbankDict[accession]["definition"] != "NA" and passLineAccession == False:
            genbankDict[accession]["definition"] += line.strip().replace("DEFINITION  ", "")
        if line.startswith("   PUBMED"):
            genbankDict[accession]["pubmed"] = int(line.strip().split()[1])
        if search("country", line):
            genbankDict[accession]["country"] = line.strip().replace("/country=","").replace('"',"").split()[0]
        if search("_source", line):
            genbankDict[accession]["source"] = line.strip().replace(";","").replace('"',"").split("_source=",1)[1]
        if search("_date", line):
            genbankDict[accession]["date"] = line.strip().replace('"',"").split("_date=",1)[1]
    return genbankDict


def write_table(genbankDict, output_file):
    """
    Function to return a table with all the information retrieved into stdout or a output file.
    """
    print("ACCESSION\tPUBMED\tDEFINITION\tCOUNTRY\tSOURCE\tDATE\tLENGTH", file=output_file)
    for accession in genbankDict.keys():
        print(accession,"\t",genbankDict[accession]["pubmed"],"\t",genbankDict[accession]["definition"],"\t",genbankDict[accession]["country"],"\t",genbankDict[accession]["source"],"\t",genbankDict[accession]["date"],"\t",genbankDict[accession]["length"], file=output_file)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to extract some information from a genbank format file, produced by the NCBI site, and return a table with all the information retrieved that is : ACCESSION, PUBMED, DEFINITION, /country, /isolation_source or /note=*isolate_source, /collection_date and length in LOCUS line.")
    parser.add_argument('genbank_file', help="Genbank file with one or more items ;", type=argparse.FileType('r'))
    parser.add_argument('--output_file', '-o', required=False, help="Output file where to write the table. Default : stdout ;", type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()
    
    genbank_dict = parse_gbk(args.genbank_file)
    write_table(genbank_dict, args.output_file)
