import os, subprocess

#path = '\\'
path = "M:\security\hashcat\pcap_files"

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.pcap' in file:
            #files.append(os.path.join(r, file))
            files.append(file)


for f in files:
    print(" Trying to convert the file : ", f)
    subprocess.run(["cap2hccapx", f, f.replace(".pcap", ".hccapx")], stdout=subprocess.PIPE)
