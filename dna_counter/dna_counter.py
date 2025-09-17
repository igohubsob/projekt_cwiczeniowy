# DNA Counter 
# 1. Pobranie sekwencji DNA od użytkownika 
dna_sequence = input("Podaj sekwencję DNA: ").upper()

# 2. Utworzenie pustego słownika na wyniki
dna_count = {"A": 0, "T": 0, "G": 0, "C": 0}

# 3. Policz nukleotydy 
for nucleotide in dna_sequence:
 if nucleotide in dna_count:
   dna_count[nucleotide] += 1 

# 4. Wyświetlanie wyników 
print("\nLiczba wystąpień nukleotydów:")
for base, count in dna_count.items():
   print(f"{base}: {count}")
