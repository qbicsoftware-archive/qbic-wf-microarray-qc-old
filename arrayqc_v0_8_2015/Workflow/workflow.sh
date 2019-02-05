#!/bin/bash
module load qbic/anaconda2
module load qbic/r/qbic-r-3.2.2

workflowDir=$(cat wfdir)
#parse using CTDopts and run workflow
python runWorkflow.py $workflowDir
cp wfdir wfdir2