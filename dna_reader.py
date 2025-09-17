# otwieranie pliku i czytanie sekwencji 
with open("dna.txt", "r") as f:
   dna_seq = f.read().strip()

print("Sekwencja DNA:", dna_seq)
print("Długość sekwencji:", len(dna_seq))
