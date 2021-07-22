import itertools   # pomocnicza biblioteka

class transformacja:    # klasa z iteratorem
	genecode = {                              # slownik z kodonami
		'A': ['GCA','GCC','GCG','GCT'],  
	 	'C': ['TGC','TGT'], 
	 	'D': ['GAT','GAC'], 
	  	'E': ['GAA','GAG'], 
	  	'F': ['TTT','TTC'], 
	  	'G': ['GGT','GGG','GGC','GGA'], 
	  	'H': ['CAT','CAC'], 
	  	'I': ['ATT','ATA','ATC'], 
	  	'K': ['AAA','AAG'], 
	  	'L': ['TTA','TTG','CTT','CTG','CTC','CTA'], 
	  	'M': ['ATG'], 
	  	'N': ['AAT','AAC'], 
	  	'P': ['CCT','CCG','CCC','CCA'], 
	  	'Q': ['CAA','CAG'], 
	  	'R': ['CGT','CGG','CGC','CGA','AGG','AGA'], 
	  	'S': ['TCT','TCG','TCC','TCA','AGT','AGC'], 
	  	'T': ['ACT','ACG','ACC','ACA'],  
	  	'V': ['GTT','GTG','GTC','GTA'], 
	  	'W': ['TGG'], 
	  	'Y': ['TAT','TAC'],
	  	'*': ['TAA','TAG','TGA'],
	  	'x': ['NNN']
	} 

	def __init__(self,sekwencja):   # ustawiam warunki , konstruktor
		self.sekwencja = sekwencja  
		self.kodony = []    
		for amino in self.sekwencja:     
			if amino in self.genecode:                   
				self.kodony.append(self.genecode[amino])  # dodawanie do listy list kodonow odpowiadajacym aminokwasowi
		self.generator = itertools.product(*self.kodony)  # operator '*' rozpakowywuje liste na mniejsze listy
		self.i = 0      # poruszanie sie nextami 
		self.n_cds = self.num_cds()  # do zliczania sekwencji 

	def __iter__(self):   # zwraca siebie jako obiekt iteratora 
		return self

	def __next__(self):   # zwraca kolejny element 
		if self.i == self.n_cds:
			raise StopIteration
		self.i += 1
		return ''.join(next(self.generator))

	def num_cds(self):    # zlicza wszystkie mozliwe sekwencje kodujace 
		n = 1
		for lista_kodonow in self.kodony:
			n *= len(lista_kodonow)
		return n

#_______________________________________
def check_sequence(sekwencja):  # funkcja sprawdzajaca czy wprowadzana sekwencja jest poprawna
	#seq = seq.upper()
	aminokwasy = 'ACDEFGHIKLMNPQSTVWY*X'
	fine = 1
	for letter in sekwencja:
		if letter not in aminokwasy:
			fine = 0	
			print("Sekwencja nie zawiera poprawnych aminokwasow!")
			print("Uruchom program ponownie!")
			#break
	if len(sekwencja) < 3:
		fine = 0
		print("Sekwencja powinna miec conajmniej 3 aminokwasy!")
		print("Uruchom program ponownie!")
		
	if fine == 1:
		return True

#_____________________________________________________________

def begin():                                       # wypisuje ladny wstep 
	print("\nGENERATOR SEKWENCJI KODUJACYCH")
	print("------------------------------")
	print("Program generuje do 10000 sekwencji kodujacych (domyslnie)")
	print("START!")


# __________________________main_____________________________


begin()
sekwencja = input('Wpisz sekwencje: ')       # wpisuje sekwencje
sekwencja = sekwencja.upper()                      # wszystkie litery zamienia na duze 
check = check_sequence(sekwencja)            # sprawdzenie sekwencji

if check == True:
	oh = open('coding_seq.fasta', 'w')          # otwieranie pliku do zapisu
	for i,cds in enumerate(transformacja(sekwencja), start = 1):
		oh.write(f'Sekwencja {i}\n{cds}\n')         # zapisuje do pliku
		print(f'Sekwencja {i}\n{cds}\n')            # czyta na ekran
		if i == 10000:                              # domyslna maksymalna liczba sekwencji = 10000
			break
	print(f'Znaleziono {i} sekwencji')
	oh.close()
	print("GOTOWE!\nSekwencje zapisano w pliku o nazwie 'coding_seq.fasta'") 

