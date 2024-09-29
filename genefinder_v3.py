import sys
from Bio import SeqIO
from Bio.Seq import Seq


def findORF(sequence,min_len):
	orf_array = []
	stop_codons = ["TAA", "TAG", "TGA"]

	for strand in [1, -1]:
		if strand == 1:
			seq = sequence
			strand_label = "+"
		else:
			seq = sequence.reverse_complement()
			strand_label = "-"

		for frm in range (3):
			for i in range(frm, len(seq), 3):
				codon = seq[i:i+3]
				if codon == "ATG":
					for j in range(i+3, len(seq), 3):
						stopCodon = seq[j:j+3]
						if stopCodon in stop_codons:
							orf_len = (j+3 -i) // 3
							if orf_len >= min_len:	#minimum length check
								if strand == 1:
									orf_array.append((seq[i:j+3], i+1, j+3, strand_label))
								else:
									start = len(sequence) - j - 2
									end = len(sequence) - i
									orf_array.append((seq[i:j+3], start, end, strand_label))
							break
	return orf_array

def main():
	in_file = sys.argv[1]
	min_length = int(sys.argv[2])
	for record in SeqIO.parse(in_file, "fasta"):
		orf_array = findORF(record.seq,min_length)
		print(f"ORFs found in {record.id}:")
		for i, (orf, start, end, strand) in enumerate(orf_array, 1):
			print(f"ORF {i}: Position {start}-{end} ({strand} strand)")
			print(f"Sequence: {orf}")
		print(f"Total ORFs found: {len(orf_array)}\n")

if __name__ == "__main__":
	main()
