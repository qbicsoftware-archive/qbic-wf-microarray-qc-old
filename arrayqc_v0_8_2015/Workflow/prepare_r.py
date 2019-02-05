import sys
import argparse

parser = argparse.ArgumentParser(description=' Microarray Quality Control', prog='Microarray QC')
parser.add_argument('--factor','-f',
                   type=str,
                   required=True,
                   help="The experimental variable to highlight in some of the qc plots."
                   )
parser.add_argument('--data','-d',
                   type=str,
                   required=False,
                   help="Data folder"
                   )
args = parser.parse_args()

varOfInterest = '"'+args.factor+'"'
data = '"'+""+'"'
if(args.data):
	data = '"'+args.data+'/"'
pheno = "PHENOFILE"

vars = open("vars.R",'w')
vars.write("data = "+data+"\n")
vars.write("varOfInterest = "+varOfInterest+"\n")
vars.write('pd = read.AnnotatedDataFrame("'+pheno+'", header = TRUE, row.names=1)')
vars.close()
