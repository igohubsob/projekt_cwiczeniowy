dna_sequence = input("Podaj sekwencję DNA: ").upper()

# 1. Licznik nukleotydów 
dna_count = { "A": 0, "T": 0, "G": 0, "C": 0}
for nucleotide in dna_sequence:
 if nucleotide in dna_count:
  dna_count[nucleotide] += 1

# 2. Długość sekwencji 
length = len(dna_sequence)

# 3. Wyniki 
print("\n Wyniki analizy DNA")
print(f"Długość sekwencji: {length} nukletydów\n")

for base, count in dna_count.items():
 percent = (count / length) * 100 if length > 0 else 0 
 bar = "*" * count # prosty wykres gwiazdkowy 
 print(f"{base}: {count} ({percent:.2f}%) {bar}")
