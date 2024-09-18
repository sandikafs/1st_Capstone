from tabulate import tabulate
from datetime import datetime, timedelta

admin_username = "admin"
admin_password = "admin"

# Function to handle login
def login():
    while True:
        print("=== Login ===")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
    
    # Check if username and password match
        if username == admin_username and password == admin_password:
            print("Login berhasil. Memasuki sistem perpustakaan...")
            return True
        else:
            print("Username atau password salah.")

# Data buku
books = [
    {"ID": "1", "Judul": "Inception", "Penulis": "Christopher Nolan", "Tahun": "2010", "Stok": 3},
    {"ID": "2", "Judul": "The Usual Suspects", "Penulis": "Bryan Singer", "Tahun": "1995", "Stok": 2},
    {"ID": "3", "Judul": "Aliens", "Penulis": "James Cameron", "Tahun": "1986", "Stok": 1},
    {"ID": "4", "Judul": "Pulp Fiction", "Penulis": "Quentin Tarantino", "Tahun": "1994", "Stok": 3},
    {"ID": "5", "Judul": "DUNE", "Penulis": "Denis Villeneuve", "Tahun": "2021", "Stok": 1},
    {"ID": "6", "Judul": "12 Angry Men", "Penulis": "Reginald Rose", "Tahun": "1957", "Stok": 1},
    {"ID": "7", "Judul": "Avatar", "Penulis": "James Cameron", "Tahun": "2009", "Stok": 2},
    {"ID": "8", "Judul": "The Godfather 2", "Penulis": "Francis Ford Coppola", "Tahun": "1974", "Stok": 2},
    {"ID": "9", "Judul": "The Godfather", "Penulis": "Francis Ford Coppola", "Tahun": "1972", "Stok": 1},
    {"ID": "10", "Judul": "Fight Club", "Penulis": "David Fincher", "Tahun": "1999", "Stok": 3},
    {"ID": "11", "Judul": "TENET", "Penulis": "Christopher Nolan", "Tahun": "2020", "Stok": 5},
    {"ID": "12", "Judul": "The Dark Knight", "Penulis": "Christopher Nolan", "Tahun": "2008", "Stok": 3},
    {"ID": "13", "Judul": "Reservoir Dogs", "Penulis": "Quentin Tarantino", "Tahun": "1992", "Stok": 2},
    {"ID": "14", "Judul": "Star Wars: Episode IV", "Penulis": "George Lucas", "Tahun": "1977", "Stok": 4},
    {"ID": "15", "Judul": "X-Men", "Penulis": "Bryan Singer", "Tahun": "2000", "Stok": 2},
    {"ID": "16", "Judul": "Blade Runner", "Penulis": "Ridley Scott", "Tahun": "1982", "Stok": 1},
    {"ID": "17", "Judul": "Star Wars: Episode V", "Penulis": "George Lucas", "Tahun": "1980", "Stok": 5},
    {"ID": "18", "Judul": "Alien", "Penulis": "Ridley Scott", "Tahun": "1979", "Stok": 3},
    {"ID": "19", "Judul": "The Girl with the Dragon Tattoo", "Penulis": "David Fincher", "Tahun": "2011", "Stok": 1},
    {"ID": "20", "Judul": "Eternal Sunshine of the Spotless Mind", "Penulis": "Michel Gondry", "Tahun": "2004", "Stok": 1},
    {"ID": "21", "Judul": "Star Wars: Episode VI", "Penulis": "George Lucas", "Tahun": "1983", "Stok": 6},
    {"ID": "22", "Judul": "Avatar: The Way of Water", "Penulis": "James Cameron", "Tahun": "2022", "Stok": 2},
    {"ID": "23", "Judul": "X-Men: Days of Future Past", "Penulis": "Bryan Singer", "Tahun": "2014", "Stok": 2},
    {"ID": "24", "Judul": "Batman Begins", "Penulis": "Christopher Nolan", "Tahun": "2005", "Stok": 1},
    {"ID": "25", "Judul": "Blade Runner: 2049", "Penulis": "Denis Villeneuve", "Tahun": "2017", "Stok": 3},
    {"ID": "26", "Judul": "Kill Bill", "Penulis": "Quentin Tarantino", "Tahun": "2003", "Stok": 1},
    {"ID": "27", "Judul": "The Prestige", "Penulis": "Christopher Nolan", "Tahun": "2006", "Stok": 2},
    {"ID": "28", "Judul": "Toy Story", "Penulis": "John Lasseter", "Tahun": "1995", "Stok": 1},
    {"ID": "29", "Judul": "Shutter Island", "Penulis": "Martin Scorsese", "Tahun": "2010", "Stok": 2},
    {"ID": "30", "Judul": "Catch Me If You Can", "Penulis": "Steven Spielberg", "Tahun": "2002", "Stok": 3}



]

# Data peminjaman
borrowed_books = []

# Fungsi untuk menampilkan semua buku
def display_books():
    while True:
        print("\n=== Daftar Buku ===")
        print("1. Tampilkan semua buku")
        print("2. Tampilkan buku sesuai pengarang")
        print("3. Kembali ke Menu Utama")
    
        pilihan = input("Pilih opsi (1-3): ")
    
        if pilihan == '1':
        # Menampilkan semua buku
            print("\n=== Daftar Buku ===")
            print(tabulate(books, headers='keys', tablefmt='grid'))
        elif pilihan == '2':
        # Filter buku berdasarkan pengarang
            penulis = input("Masukkan nama pengarang: ")
            print(f"\n=== Daftar Buku oleh {penulis} ===")
            filtered_books = [book for book in books if book['Penulis'].lower()==penulis.lower()]
            if filtered_books:
                    print(tabulate(filtered_books, headers='keys', tablefmt='grid'))
        elif pilihan == '3':
            print("Kembali ke Menu Utama.")
            break
        else:
            print(f"Tidak ada buku yang ditulis oleh {penulis}.")

# Fungsi untuk menambah buku baru dengan pengecekan ID
def add_book():
    while True:
        print("\n=== Tambah Buku ===")
        print("1. Tambah Buku Baru ke dalam Koleksi")
        print("2. Kembali ke Menu Utama")
        tambahan = input("Pilih opsi (1-2): ")
        
    
    # Pengecekan ID yang sama
        if tambahan == '1':
            book_id = input("Masukkan ID Buku: ")
            for book in books:
                if book["ID"] == book_id:
                    print("ID Buku sudah ada. Silakan gunakan ID yang berbeda.")
                    return
            else:
                title = input("Masukkan Judul Buku: ")
                author = input("Masukkan Penulis Buku: ")
                for book in books:
                    if book["Judul"].lower() == title.lower() and book["Penulis"].lower() == author.lower():
                        print("Buku sudah ada.")
                        return    
                else:
                    year = input("Masukkan Tahun Terbit: ")

    # Memasukkan jumlah stok
                while True:
                    try:
                        stock = int(input("Masukkan Jumlah Stok: "))
                        break
                    except ValueError:
                        print("Stok harus berupa angka. Silakan coba lagi.")
            book = {
                "ID": book_id,
                "Judul": title,
                "Penulis": author,
                "Tahun": year,
                "Stok": stock
        
                }
            books.append(book)
            print("Buku berhasil ditambahkan.")
        elif tambahan == '2':
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")    

# Fungsi untuk mengupdate buku
def update_book():
    while True:
        print("\n=== Update Buku ===")
        print("1. Perbarui Buku dalam Koleksi")
        print("2. Kembali ke Menu Utama")
        perbaru = input("Pilih opsi (1-2): ")
    
        if perbaru == '1':
            book_id = input("Masukkan ID Buku yang akan diupdate: ")
            found = False
            for book in books:
                if book["ID"] == book_id:
                    print(f"Buku ditemukan: {book}")
                    book["Judul"] = input("Masukkan Judul Buku Baru: ")
                    book["Penulis"] = input("Masukkan Penulis Buku Baru: ")
                    book["Tahun"] = input("Masukkan Tahun Terbit Terbaru: ")
                    while True:
                        try:
                            book["Stok"] = int(input("Masukkan Jumlah Stok Terkini: "))
                            break
                        except ValueError:
                            print("Stok harus berupa angka. Silakan coba lagi.")
                    print("Buku berhasil diupdate.")
                    found = True
                    break
                if not found:
                    print("Buku dengan ID tersebut tidak ditemukan.")
                    break
        elif perbaru == '2':
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.") 
    

# Fungsi untuk menghapus buku
def delete_book():
    while True:
        print("\n=== Hapus Buku ===")
        print("1. Hapus Buku dalam Koleksi")
        print("2. Kembali ke Menu Utama")
        hapus = input("Pilih opsi (1-2): ")
        
        if hapus == '1':
            book_id = input("Masukkan ID Buku yang akan dihapus: ")
            for book in books:
                if book["ID"] == book_id:
                    books.remove(book)
                    print("Buku berhasil dihapus.")
                    break
                else:
                    print("Buku dengan ID tersebut tidak ditemukan.")
                    break
        elif hapus == '2':
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.") 

# Fungsi untuk meminjam buku
def borrow_book():
    while True:
        print("\n=== Peminjaman Buku===")
        print("1. Menyewa Buku")
        print("2. Mengembalikan Buku")
        print("3. Kembali ke Menu Utama")
    
        peminjaman = input("Pilih opsi (1-3): ")
        if peminjaman == '1':
            name = input("Masukkan Nama Peminjam (mohon masukkan nama lengkap): ")
            book_id = input("Masukkan ID Buku yang akan dipinjam: ")
            for book in books:
                if book["ID"] == book_id:
                    print(f"Buku ditemukan: {book['Judul']}")
                    if book["Stok"] > 0:
                        tanggal_peminjaman = datetime.now().date()
                        while True:
                            try:
                                durasi = int(input("Masukkan durasi peminjaman (dalam hari): "))
                                break
                            except ValueError:
                                print("Durasi harus berupa angka. Silakan coba lagi.")
                        tanggal_pengembalian = tanggal_peminjaman + timedelta(days=durasi)
                        borrowed_books.append({
                            "Nama": name,
                            "ID": book["ID"],
                            "Judul": book["Judul"],
                            "Tanggal Peminjaman": tanggal_peminjaman,
                            "Tanggal Pengembalian": tanggal_pengembalian
                        })
                        book["Stok"] -= 1
                        print(f"Buku berhasil dipinjam. Harap dikembalikan sebelum {tanggal_pengembalian}.\nTerima Kasih!")
                        break
                    else:
                        print("Stok buku habis. Tidak bisa meminjam buku ini.")
                        continue
            else:            
                print("Buku dengan ID tersebut tidak ditemukan.")
    
        elif peminjaman == '2':
            name = input("Masukkan Nama Peminjam (mohon masukkan nama lengkap): ")
            borrowed_books_by_name = [book for book in borrowed_books if book["Nama"].lower() == name.lower()]
            if not borrowed_books_by_name:
                print("Nama peminjam tidak ditemukan.")
                continue
            else:
                print(f'Peminjam atas nama {name} ditemukan.')
                print("Buku yang sedang dipinjam:")
                for borrowed in borrowed_books_by_name:
                    print(f"- {borrowed['Judul']} (ID: {borrowed['ID']})")
            book_id = input("Masukkan ID Buku yang akan dikembalikan: ")
            for borrowed in borrowed_books:
                if borrowed["Nama"].lower() == name.lower() and borrowed["ID"] == book_id:
                    tanggal_pengembalian = borrowed["Tanggal Pengembalian"]
                    tanggal_sekarang = datetime.now().date()
                    print(f"Tanggal Pengembalian: {tanggal_pengembalian}")
                    print(f"Tanggal Sekarang: {tanggal_sekarang}") 
                # Menghitung keterlambatan pengembalian
                
                    selisih_hari = (tanggal_sekarang - tanggal_pengembalian).days
                    if selisih_hari > 0:
                            denda_per_hari = 15000
                            total_denda = selisih_hari * denda_per_hari
                            print(f"Anda terlambat {selisih_hari} hari. Denda yang harus dibayar: Rp{total_denda}.")
                    else:
                            print("Tidak ada denda. Terima kasih telah mengembalikan buku tepat waktu.")
                
                # Menghapus dari daftar peminjaman dan menambah stok kembali
                    borrowed_books.remove(borrowed)
                
                    for book in books:
                            if book["ID"] == book_id:
                                book["Stok"] += 1
                    print(f"Buku '{borrowed['Judul']}' berhasil dikembalikan.")
                    break
            else:
                print(f"ID Buku {book_id} tidak sesuai dengan yang dipinjam.")          
        elif peminjaman == '3':
            print("Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi utama
def main():
    if login():
        while True:
            print("\n=== Sistem Perpustakaan THINLOVE ===")
            print("1. Daftar Buku")
            print("2. Tambah Buku")
            print("3. Update Buku")
            print("4. Hapus Buku")
            print("5. Peminjaman Buku")
            print("6. Keluar dari Program")

            choice = input("Pilih opsi (1-6): ")

            if choice == '1':
                display_books()
            elif choice == '2':
                add_book()
            elif choice == '3':
                update_book()
            elif choice == '4':
                delete_book()
            elif choice == '5':
                borrow_book()
            elif choice == '6':
                print("Keluar dari sistem perpustakaan...")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    else:
        print('Silahkan coba lagi.')
    

if __name__ == "__main__":
    main()

