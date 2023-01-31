# bioinformatics-scripts

- [bioinformatics-scripts](#bioinformatics-scripts)
  * [gbk2table.py](#gbk2table)
  * [frequency_alphabet.py](#frequency_alphabet)
  
## gbk2table.py

### Usage
```
usage: gbk2table.py [-h] [--output_file OUTPUT_FILE] genbank_file

gbk2table is a script to extract some information from a genbank format file, produced by the
NCBI site, and return a table with all the information retrieved that is :
ACCESSION, PUBMED, DEFINITION, /country, /isolation_source or
/note=*isolate_source, /collection_date and length in LOCUS line.

positional arguments:
  genbank_file          Genbank file with one or more items ;

optional arguments:
  -h, --help            show this help message and exit
  --output_file OUTPUT_FILE, -o OUTPUT_FILE
                        Output file where to write the table. Default : stdout;

```

## frequency_alphabet.py

### Usage
```
usage: frequency_alphabet.py [-h] [--output_file OUTPUT_FILE] input_file alphabet_type

frequency_alphabet.py is a script that allows to count for each given position of a multi-aligned FASTA file the frequency of each letter
composing DNA, RNA or proteins.

positional arguments:
  input_file            FASTA file with multi-alignment;
  alphabet_type         Type of letter : aa, dna or rna;

optional arguments:
  -h, --help            show this help message and exit
  --output_file OUTPUT_FILE, -o OUTPUT_FILE
                        Output file with matrix of frequency. Default : stdout;
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
