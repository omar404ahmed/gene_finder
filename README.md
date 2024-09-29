# Gene Finder
This repository is a python3 + biopython based tool for finding Open Reading Frames. The repo acts as a submission for BioE 201/230 course.


## Requirements
* Bio-Python (ver 1.6 +)
* Python (ver 3.6 +)

To utilise this tool:
* Clone the repository onto your local machine.
* Install the dependencies using either ```conda install biopython``` or ```pip install biopython ``` .
* Pass inputs as arguments as described [in this section](#cli-commands-to-execute-scripts).


## Descriptions of the four versions of Gene Finder tool

### Ver1

Creation of this version was preceeded by creation of github repository and cloning it onto the ibex cluster. Ver1 located open reading frames (ORFs) only in forward strands and covers three of six possible reading frames.


![Alt text](/Screenshots/1.png?raw=true "Output of Ver1")


### Ver2

This version of the Gene Finder considers all possible reading frames by utilising ```reverse_complement``` method of the ```Seq``` object. It is of note that the forward strands have label as ```+``` while reverse strands have label ```-```


![Alt text](/Screenshots/2.png?raw=true "Output of Ver2")


### Ver3

Ver3 involved creating a check to avoid filtering smaller ORFs. The motivation being that smaller ORFs are unlikely to be functional genes.

![Alt text](/Screenshots/3.png?raw=true "Output of Ver3")


### Ver4

The final filter is implemented in Ver4, where we filter all predicted ORFs based on whether they contain a Shine-Dalgarno sequence up to 20bp upstream of the start codon.

![Alt text](/Screenshots/4.png?raw=true "Output of Ver4")



## CLI commands to execute scripts


```
[ver 1]
python genefinder_v1.py (/path/to/genome.fasta) > out.txt

[ver 2]
python genefinder_v2.py (/path/to/genome.fasta) > out2.txt

[ver 3]
python genefinder_v3.py (path/to/genome.fasta) (minimum_length) > out3.txt

[ver 4]
python genefinder_v4.py (path/to/genome.fasta) (minimum_length) (SD_sequence) > out4.txt

```

## Applying ORF finder to all genome files in the NCBI Bacteria dataset.
```
find /home/ahmedo/ncbi_dataset/data -type f -name "*GCF*.fna" | while read genome; do python ~/genefinder_v2.py "$genome"; done > fourteen_gen.txt 

```

### Problem number 72 of rosalind is solved in [ORF_protein.ipynb](https://github.com/omar404ahmed/gene_finder/blob/main/ORF_protein.ipynb) 

