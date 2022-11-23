class RakBuku():
    def __init__(self):
        self.size = 5
        self.map = [None] * self.size

    def getHash(self,key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    
    def probing(self,key):
        for index in range(self.size):
            probeHash = self._linearProbing(key,index)
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'Deleted'):
                return probeHash
        return None

    def linearProbing(self,key,index): 
        return (self._getHash(key)+index) % self.size
    
    def tambahBuku(self,jenisBuku,namaBuku):
        key_hash = self._getHash(jenisBuku)
        key_value = [jenisBuku,namaBuku]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            key_hash = self._probing(jenisBuku)
            if key_hash is None:
                print('Rak Buku anda sudah penuh')
                return False
        self.map[key_hash] = list([key_value])
        return False
    
    def lihatBuku(self,jenisBuku):
        key_hash = self._getHash(jenisBuku)
        if (self.map[key_hash] is not None) and (self.map[key_hash]!='deleted'):
            for index in range(self.size):
                key_hash = self._linearProbing(jenisBuku,index)
                if self.map[key_hash][0][0] == jenisBuku:
                    return self.map[key_hash][0][1]
        print('Key',jenisBuku,'tidak ditemukan')
        return None
    
    def ambilBuku(self,jenisBuku):
        key_hash = self._getHash(jenisBuku)
        if self.map[key_hash] is None:
            return False
        for index in range(self.size):
                key_hash = self._linearProbing(jenisBuku,index)
                if self.map[key_hash][0][0] == jenisBuku:
                    print('deleting',jenisBuku)
                    self.map[key_hash] = 'deleted'
                    return True
        print('Key',jenisBuku,'tidak ditemukan')
        return False
    
    def printAll(self):
        print('====================== List Buku ======================')
        for item in self.map:
            if (item is not None) and (item != 'deleted'):
                print('Nama :',item[0][1],'<> Jenis :',item[0][0])
        print('========================================================')

if __name__ == "__main__":
 rak1 = RakBuku()
 rak1.tambahBuku("History", "Mein Kampf (B01)")
 rak1.tambahBuku("Fantasy", "The Witcher (B02)")
 rak1.tambahBuku("Mystery", "Exile (B03)")
 rak1.tambahBuku("Sci Fi", "The Martian (B04)")
 rak1.tambahBuku("History", "World War (B05)")
 rak1.tambahBuku("Romance", "Twilight (B06)")
 print(rak1.lihatBuku("History"))
 print(rak1.lihatBuku("Romance"))
 rak1.ambilBuku("Sci Fi")
 rak1.ambilBuku("Romance")
 rak1.printAll()