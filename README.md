# Python-Script-to-compute-average-nucleotide-identity-between-input-FASTA-files-using-MUMerrs-DNAdiff

Description:
The script takes the specified number of genome FASTA files and computes the pairwise distance/average nucleotide identity(ANI) between the FASTA files using MUMerr's DNAdiff wrapper.
The script also requires the user to specify the number of threads (-t) to be used to run the script and (-o) the name of the final output file.
Input:
The name of the required output file, the number of threads to be used and the input FASTA files.

Requirements:
MUMerr's DNAdiff in the PATH variable
Multiprocessing, sys, org, subprocess and argparse modules.
Input files in FASTA format.

Output:
The ANI values will be printed in a matrix format with the names of the FASTA files as the column and row headers.

Sample run: 
./ parallel_ani.py -o <Output file> [-t <Number of threads>] fasta_file1 fasta_file2 fasta_file3...


