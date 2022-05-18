#!/usr/bin/env python3

import os

#BWA is used to index the reference chromosome

#make necessary directory
number = input('\033[1;45m Enter the chromosome number: \033[0;0;0m')
os.system('mkdir bgz_'+ number)
os.system('cd bgz_'+ number)
print('\n')

#download chromosome sequence
print('\033[1;45m You will be directed to Ensembl Pub Release \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
os.system('sudo open http://ftp.ensembl.org/pub/release-104/fasta/homo_sapiens/dna/')
chrom = input('\033[1;45m Copy and paste the URL to the chromosome of interest: \033[0;0;0m')
print('\n')
print('\033[1;45m Downloading Chromosome '+ number + '\033[0;0;0m' )
os.system('wget ' + chrom)
os.system('mv *.gz* bgz_'+ number)

#indexing chromosome file
print('\033[1;45m Indexing with BWA... \033[0;0;0m' )
os.chdir('bgz_' + number)
os.system('bwa index *.gz*')
os.system('bgzip -d *.gz*')
print('\033[1;45m Indexing with BWA complete \033[0;0;0m' )