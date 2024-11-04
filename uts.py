# Definisi Kelas Person sebagai Parent Class
class Person:
    def __init__(self, nama, umur):
        self.nama = nama            # Public attribute
        self._umur = umur           # Protected attribute
        self.__id = "123456"        # Private attribute
    
    def get_id(self):               # Getter for private attribute
        return self.__id

    def set_id(self, id_baru):      # Setter for private attribute
        self.__id = id_baru

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Umur: {self._umur}")

# Definisi Kelas Mahasiswa yang mewarisi Kelas Person
class Mahasiswa(Person):
    def __init__(self, nama, umur, jurusan):
        super().__init__(nama, umur)  # Memanggil konstruktor dari kelas induk
        self.jurusan = jurusan        # Public attribute
    
    # Method khusus untuk Mahasiswa
    def tampilkan_info_mahasiswa(self):
        print(f"Nama: {self.nama}, Umur: {self._umur}, Jurusan: {self.jurusan}")
    
    # setter dan getter untuk jurusan
    def get_jurusan(self):
        return self.jurusan

    def set_jurusan(self, jurusan_baru):
        self.jurusan = jurusan_baru

# Main Program
if __name__ == "__main__":
    # Membuat objek dari kelas Mahasiswa
    mahasiswa1 = Mahasiswa("Alice", 21, "Teknik Informatika")

    # Menggunakan getter dan setter
    print("Informasi Mahasiswa Sebelum Diubah:")
    mahasiswa1.tampilkan_info_mahasiswa()
    
    # Mengubah nilai jurusan menggunakan setter
    mahasiswa1.set_jurusan("Sistem Informasi")
    print("\nInformasi Mahasiswa Setelah Diubah:")
    mahasiswa1.tampilkan_info_mahasiswa()

    # Mengakses ID melalui getter (Encapsulation Private Attribute)
    print("\nID Mahasiswa:", mahasiswa1.get_id())
