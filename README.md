# bioinformatics-scripts

- [bioinformatics-scripts](#bioinformatics-scripts)
  * [gbk2table.py](#gbk2table)
  
## gbk2table.py

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

## frequency_alphabet.py

### Description
frequency_alphabet.py is a script that allows to count for each given position of a multi-aligned FASTA file the frequency of each letter composing DNA, RNA or proteins.

### Usage
```
./frequency_alphabet.py [-h] <input_file> <alphabet_type> [-o <output_file>]
```

### Exemple
You have a FASTA with multi-alignment of DNA sequences like this :
```
>seq1
AaTTCGTC-T
>seq2
AATNCtTCAT
>seq3
AA--CGTC-T
```
Then, you run this command in your terminal : 
```
./frequency_alphabet.py /home/workdir/example_seq_aligned.fasta dna
```
And, this kind of result will appear in your terminal :
```
POSITION	 A	T	C	G	N	a	t	c	g	-
1 	 1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
2 	 0.6667	0.0	0.0	0.0	0.0	0.3333	0.0	0.0	0.0	0.0
3 	 0.0	0.6667	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.3333
4 	 0.0	0.3333	0.0	0.0	0.3333	0.0	0.0	0.0	0.0	0.3333
5 	 0.0	0.0	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
6 	 0.0	0.0	0.0	0.6667	0.0	0.0	0.3333	0.0	0.0	0.0
7 	 0.0	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
8 	 0.0	0.0	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
9 	 0.3333	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.6667
10 	 0.0	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
```
