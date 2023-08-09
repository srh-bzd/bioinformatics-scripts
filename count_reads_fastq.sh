#!/bin/bash


### USAGE
if [ $# -lt 1 ] ; then
    echo "usage: count_reads_fastq.sh <directory> <output_file>"
    echo -e "\ncount_reads_fastq.sh is a script to counts the number of reads in FASTQ files"
    echo -e "\narguments:"
    echo -e "\tdirectory\tDirectory where there is FASTQ files;"
    echo -e "\toutput_file\tOutput file where to write counts;"
    exit 0
fi


### ARGUMENTS
# Directory where the FASTQ files are
dir=$1
# Output file
output=$2


### VERIFICATIONS
if [ ! -d "$dir" ]
then
	echo -e "error: The directory doesn't exist"
	exit
fi
if [ -z "$output" ]
then
	echo -e "error: The output file isn't inform"
	exit
fi


### PREPARATION
# Write header into the output file
echo -e "FASTQ_FILE\tNBR_READS" > "$2"


### COUNTS
# For each FASTQ file gzip in the directory
NBFASTQGZ=`ls -1 "${f}"/*fastq.gz 2>/dev/null | wc -l`
if [ ! $NBFASTQGZ = 0 ]
then 
	for file in "$dir"/*fastq.gz
    do
        # Save the name of the file
        file_wo_path=${file##*/}
        # Print the name of the file into the output file
        printf '%s\t' "$file_wo_path" >> "$2"
        # and print the results of count 
        lines="$(zcat -- "$file" | wc -l)"
        bc <<< "$lines/4" >> "$2"
    done
fi 

# For each FASTQ file not gzip in the directory
NBFASTQWOGZ=`ls -1 "${f}"/*fastq 2>/dev/null | wc -l`
if [ ! $NBFASTQWOGZ = 0 ]
then 
	for file in "$dir"/*fastq
    do
        # Save the name of the file
        file_wo_path=${file##*/}
        # Print the name of the file into the output file
        printf '%s\t' "$file_wo_path" >> "$2"
        # and print the results of count 
        lines="$(cat -- "$file" | wc -l)"
        bc <<< "$lines/4" >> "$2"
    done
fi 
