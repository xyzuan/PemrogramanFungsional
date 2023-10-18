expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]


def add_expenses(expenses, tgl, desc, total):
    return expenses + [{'tanggal': tgl, 'deskripsi': desc, 'jumlah': total}]


def calculate_total_expenses(expenses, tgl):
    return sum(expense['jumlah'] for expense in expenses if expense['tanggal'] == tgl)


def get_expenses_by_date(expenses, tgl):
    return [expense for expense in expenses if expense['tanggal'] == tgl]


def generate_expenses_report(expenses):
    for date in set(expense['tanggal'] for expense in expenses):
        total = calculate_total_expenses(expenses, date)
        expenses_on_date = get_expenses_by_date(expenses, date)
        detail = ', '.join(
            [
                f"{expense['deskripsi']} -  Rp {expense['jumlah']} "
                for expense in expenses_on_date
            ]
        )
        report = f"Laporan {date}: Total {total}\nDetail: {detail}\n"
        yield report


def add_expense_interactively(expenses):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    new_expenses = add_expenses(expenses, date, description, amount)
    print("Pengeluaran berhasil ditambahkan.")
    return new_expenses


def view_expenses_by_date(expenses):
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(expenses, date)
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")


def view_expenses_report(expenses):
    print("\nLaporan Pengeluaran Harian:")
    expenses_report = generate_expenses_report(expenses)
    for entry in expenses_report:
        print(entry)


def get_user_input(command): return int(input(command))


def display_menu():
    global expenses

    while True:
        print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
        print("1. Tambah Pengeluaran")
        print("2. Total Pengeluaran Harian")
        print("3. Lihat Pengeluaran berdasarkan Tanggal")
        print("4. Lihat Laporan Pengeluaran Harian")
        print("5. Keluar")

        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            date = input('Masukkan Tanggal (YYYY-MM-DD): ')
            total_expenses = calculate_total_expenses(expenses, date)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
    else:
        print("Pilihan tidak valid. Silahkan pilih menu yang benar.")


if __name__ == "__main__":
    display_menu()
