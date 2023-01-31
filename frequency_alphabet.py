#!/usr/bin/env python3

import argparse, sys

"""
USAGE
    ./frequency_alphabet.py [-h] <input_file> <output_file> <alphabet_type>
DESCRIPTION
    frequency_alphabet.py is a script that allows to count for each given position 
    of a multi-aligned FASTA file the frequency of each letter composing DNA, RNA or proteins.
PREREQUISITE
    - python3
    - FASTA file with multi-alignment
AUTHOR :
    Sarah BOUZIDI
    Engineer in bioinformatics
    Centre National de la Recherche Scientifique (CNRS)
    Laboratory MIVEGEC, IRD, Montpellier
"""


def parse_fasta(input_file):
    """
    Parse input FASTA file and keep it into a dict like : {seqId : "seq"}
    """
    fastaDict = dict()
    seqId = None
    for line in input_file:
        if line.startswith(">"):
            seqId = line.strip().replace(">","")
            fastaDict[seqId] = ""
        else:
            fastaDict[seqId] += line.strip()
    return fastaDict


def count_alphabet(fastaDict, alphabet_type):
    """
    For each position of FASTA sequences, count letters
    """
    dictCount = dict()
    for position in range(len(list(fastaDict.values())[0])):
        dictAlphabetAA = {'C' : 0, 'D' : 0, 'S' : 0, 'Q' : 0, 'K' : 0, 'I' : 0, 'P' : 0, 'T' : 0, 'F' : 0, 'N' : 0, 'G' : 0, 'H' : 0, 'L' : 0, 'R' : 0, 'W' : 0, 'A' : 0, 'V' : 0, 'E' : 0, 'Y' : 0, 'M' : 0, '*' : 0, '-' : 0}
        dictAlphabetDNA = {'A' : 0, 'T' : 0, 'C' : 0, 'G' : 0, 'N' : 0, 'a' : 0, 't' : 0, 'c' : 0, 'g' : 0, '-' : 0}
        dictAlphabetRNA = {'A' : 0, 'U' : 0, 'C' : 0, 'G' : 0, 'N' : 0, 'a' : 0, 'u' : 0, 'c' : 0, 'g' : 0, '-' : 0}
        dictAlphabet = None
        if (alphabet_type == "aa"): 
            dictAlphabet = dictAlphabetAA
        if (alphabet_type == "dna"): 
            dictAlphabet = dictAlphabetDNA
        if (alphabet_type == "rna"): 
            dictAlphabet = dictAlphabetRNA
        dictCount[position] = dictAlphabet
        for seqId in fastaDict:
            letter = fastaDict[seqId][position]
            if letter in dictAlphabet.keys():
                dictCount[position][letter] += 1 
    return dictAlphabet, dictCount


def write_matrix(fastaDict, dictAlphabet, dictCount, output_file):
    """
    Write the matrix of frequencies 
    """
    print("POSITION\t","\t".join(dictAlphabet.keys()), file = output_file)
    for position in dictCount:
        counts = list(dictCount[position].values())
        freq = [str(count / len(fastaDict)) for count in counts]
        print(position+1, "\t","\t".join(freq), file=output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="frequency_alphabet.py is a script that allows to count for each given position of a multi-aligned FASTA file the frequency of each letter composing DNA, RNA or proteins.")
    parser.add_argument('input_file',  help="FASTA file with multi-alignment;", type=argparse.FileType('r'))
    parser.add_argument('alphabet_type', help="Type of letter : aa, dna or rna;", type=str)
    parser.add_argument('--output_file', '-o', required=False, help="Output file with matrix of frequency. Default : stdout;", type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()
    
    file_dict = parse_fasta(args.input_file)
    alphabet_dict, count_dict = count_alphabet(file_dict, args.alphabet_type)
    write_matrix(file_dict, alphabet_dict, count_dict, args.output_file)
