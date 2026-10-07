from fasta_tool import FastaReader

gen = FastaReader("examples/dna.fasta").read()
print(next(gen))
print(next(gen))
print(next(gen))