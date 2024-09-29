# Gene Finder
This repository is a python3 + biopython based tool for finding Open Reading Frames. The repo acts as a submission for BioE 201/230 course.


## Requirements
* Bio-Python (ver 1.6 +)
* Python (ver 3.6 +)

To utilise this tool:
* Clone the repository onto your local machine.
* Install the dependencies using either ```conda install biopython``` or ```pip install biopython ``` .
* Pass inputs as arguments as described [in this section](#cli-commands-to-execute-scripts).


## Description of the four versions of Gene Finder tool


## CLI commands to execute scripts
```
[ver 1]
python genefinder_v1.py (/path/to/genome.fasta) > out1.txt

[ver 2]
python genefinder_v2.py (/path/to/genome.fasta) > out2.txt

[ver 3]
python genefinder_v3.py (path/to/genome.fasta) (minimum_length) > out3.txt

[ver 4]


```


### Applying ORF finder to all genome files in the NCBI Bacteria dataset.
```
find /home/ahmedo/ncbi_dataset/data -type f -name "*GCF*.fna" | while read genome; do python ~/genefinder_v2.py "$genome"; done > fourteen_gen.txt 

```


