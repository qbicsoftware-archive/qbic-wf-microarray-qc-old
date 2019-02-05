from CTDopts.CTDopts import _InFile, CTDModel, args_from_file
import sys
import os
import subprocess

wf_dir = sys.argv[1]
ctd_params = args_from_file(wf_dir + '/WORKFLOW-CTD')
ctd_files = args_from_file(wf_dir + '/IN-FILESTOSTAGE')

#TODO: define parameters using flags (input files, pheno.txt and var of interest)
command = 'python prepare_r.py '

data_path = '%s/data/' % wf_dir
result_path = '%s/result/' % wf_dir
log_path = '%s/logs/' % wf_dir

command += " -d "+wf_dir

files = []

for f in ctd_files["input"]:
	fileName = f.split('/')[-1]
	files.append('%s%s' % (data_path, fileName))

#command += '%s' % ' '.join(files)

for param in ctd_params.keys():
        command += ' -%s %s' % (param, ctd_params[param])

log = open("qclogs.txt",'w')
subprocess.call(command.split(), stderr=log, stdout=log)
subprocess.call(['mkdir',"data"])
subprocess.call(["Rscript", "runqc.R"], stderr=log, stdout=log)
subprocess.call(["mv", "-i", "figure", result_path])# figures for html qc results
subprocess.call(["mv", "-i", "data", result_path])# additional files like correlations
subprocess.call(["mv", "array_qc.html", result_path])
log.close()
subprocess.call(["mv", "qclogs.txt", log_path])# std out and std err logs