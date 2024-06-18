# Token Recognizer menggunakan Finite Automata

class PengenalToken:
    def __init__(self):
        self.kata_s = ["saya", "dia", "sultan", "yongky", "faiq"]
        self.kata_p = ["membaca", "memakan", "memancing", "meminum", "mengambil"]
        self.kata_o = ["buku", "nasi", "ikan", "air", "baju"]
        self.kata_k = ["sekarang", "kemarin", "di sini", "di situ", "putih"]
        self.valid = True

    def kenali(self, kata):
        if kata in self.kata_s:
            return "S"
        elif kata in self.kata_p:
            return "P"
        elif kata in self.kata_o:
            return "O"
        elif kata in self.kata_k:
            return "K"
        else:
            print(f"\nKata: '{kata}' tidak dikenal")
            self.valid = False
            return None

# Parser menggunakan Pushdown Automata
class Parser:
    def __init__(self, tokenizer):
        # Inisialisasi parser dengan tokenizer
        self.tokenizer = tokenizer
        self.stack = []  # inisialisasi tumpukan kosong untuk menyimpan parse tree

    # Metode untuk parse kalimat
    def parse(self, kalimat):
        # Pisahkan kalimat menjadi beberapa kata (token)
        tokens = kalimat.split()
        for token in tokens:
            # Mengenali jenis token
            token_type = self.tokenizer.kenali(token)
            # Cek jenis token dan push ke stack yang sesuai
            if token_type == "S":
                self.stack.append("S")
            elif token_type == "P":
                self.stack.append("P")
    
            elif token_type == "O":
                self.stack.append("O")
    
            elif token_type == "K":
                    self.stack.append("K")

        # Cek apakah parse berhasil
        return self.stack == ["S", "P", "O", "K"] or self.stack == ["S", "P", "K"] or self.stack == ["S", "P", "O"] or self.stack == ["S", "P"]

# Contoh penggunaan
token = PengenalToken()
parser = Parser(token)
kalimat = input("Masukkan kalimat: ")
if parser.parse(kalimat) and token.valid:
    print("\nKalimat valid")
    print(f"Bentuk kalimat adalah: {parser.stack}")
else:
    print("\nKalimat tidak valid")
    print(f"Bentuk kalimat adalah: {parser.stack}")
