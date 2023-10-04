def hitung_nilai_akhir(uts, uas):
    return (uts + uas) / 2

def hitung_semua_nilai(data_mahasiswa):
    data_nilai_akhir = {}

    for name, nilai in data_mahasiswa.items():
        data_nilai_akhir[name] = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
    return data_nilai_akhir

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print('Nama: {}\tNilai Akhir: {:.2f}'.format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        'Jody': {
            'uts': 90,
            'uas': 70
        },
        'Nizar': {
            'uts': 20,
            'uas': 10
        },
    }

    tampilkan_nilai_akhir(hitung_semua_nilai(data_mahasiswa))

if __name__ == "__main__":
    main()