class UTY(object):
    def __init__(self, status, nama, prodi):
        self.nama = nama
        self.status = status
        self.prodi = prodi

    def Semangat(self):
        print("Indonesia Maju Indonesia Tumbuh UTY Hebat")

    def Info(self):
        print("-- INFORMASI --")
        print("Nama        : " + self.nama)
        print("Status      : " + self.status)
        print("Program Studi : " + self.prodi)


class Dosen(UTY):
    def __init__(self, status, nama, prodi, nip):
        super().__init__(status, nama, prodi)
        self.nip = nip

    def SemangatDosen(self):
        self.Semangat()  # ambil dari kelas UTY
        print("Dosen bermartabat")

    def InfoDosen(self):
        print("NIP         : " + str(self.nip))


class Mahasiswa(UTY):
    def __init__(self, status, nama, prodi, npm):
        super().__init__(status, nama, prodi)
        self.npm = npm

    def SalamMhs(self):
        self.Semangat()  # ambil dari kelas UTY
        print("Mahasiswa cerdas dan kreatif")

    def InfoMhs(self):
        print("NPM         : " + str(self.npm))


# Contoh implementasi kode
# Membuat objek dari kelas UTY
mahasiswa = UTY("Mahasiswa", "Messi", "Informatika")
mahasiswa.Semangat()
mahasiswa.Info()

print("\n")

# Membuat objek dari kelas Dosen
dosen = Dosen("Dosen", "Klopp", "Sistem Informasi", 12345)
dosen.SemangatDosen()
dosen.InfoDosen()

print("\n")

# Membuat objek dari kelas Mahasiswa
mhs = Mahasiswa("Mahasiswa", "Dewa", "Teknik Informatika", 534)
mhs.SalamMhs()
mhs.InfoMhs()
