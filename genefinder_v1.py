import sys
from Bio import SeqIO
from Bio.Seq import Seq
# from Bio.SeqRecord import SeqRecord

def findORF(sequence):
	orf_array = []
	stop_codons = ["TAA", "TAG", "TGA"]

	for frm in range (3):
		for i in range(frm, len(sequence), 3):
			codon = sequence[i:i+3]
			if codon == "ATG":
				for j in range(i+3, len(sequence), 3):
					stopCodon = sequence[j:j+3]
					if stopCodon in stop_codons:
						orf_array.append(sequence[i:j+3])
						break
	return orf_array

def main():
	in_file = sys.argv[1]
	#out_file = sys.argv[2]

	for record in SeqIO.parse(in_file, "fasta"):
		orf_array = findORF(str(record.seq))
		print(f"ORFs found in {record.id}:")
		for i, orf in enumerate(orf_array, 1):
			print(f"ORF {i}: {orf}")
		print(f"Total ORFs found: {len(orf_array)}\n")

if __name__ == "__main__":
	main()
