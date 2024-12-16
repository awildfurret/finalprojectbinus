import os

def input_transasksi():
    try:
        another = 'y'
        kasir_file = open('kasir.txt','a')

        while another == 'y' or another == 'Y':
            print('Input Data Transaksi Baru: ')
            idtrans = input('ID Transaksi? ')
            notrans = int(input('Nomor Transaksi? '))
            nama_product  = input('Nama Product? ')
            qty = int(input('Quantity? '))
            harga = int(input('Harga? '))
            subtotal = int(harga * qty)
            kasir_file.write(idtrans + '\n')
            kasir_file.write(str(notrans) + '\n')
            kasir_file.write(nama_product + '\n')
            kasir_file.write(str(qty) + '\n')
            kasir_file.write(str(harga) + '\n')
            kasir_file.write(str(subtotal) + '\n')
            print('Apakah Anda ingin menambahkan catatan lain? Y or N')
            another = input('')

        kasir_file.close()
        print('Data ditambahkan dengan sukses')

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def daftar_transaksi():
    try:
        kasir_file = open('kasir.txt', 'r')
        notrans = kasir_file.readline()
        while notrans != '':
            idtrans = kasir_file.readline()
            nama_product = kasir_file.readline()
            qty = kasir_file.readline()
            harga = kasir_file.readline()
            subtotal = kasir_file.readline()
            idtrans = idtrans.rstrip('\n')
            notrans = notrans.rstrip('\n')
            nama_product = nama_product.rstrip('\n')
            qty = qty.rstrip('\n')
            harga = harga.rstrip('\n')
            subtotal = subtotal.rstrip('\n')
            print('ID Transaksi: TRX -', idtrans)
            print('Nomor Transaksi:', notrans)
            print('Nama Product:', nama_product)
            print('Quantity:', qty)
            print('Harga: ', harga)
            print('Subtotal: ', subtotal)
            print()
            notrans = kasir_file.readline()
        kasir_file.close()

    except FileNotFoundError:
        print("File kasir.txt tidak ditemukan. Silakan membuat file tersebut dengan Input Data Transaksi Baru")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def edit_transaksi():
    try:
        found = False
        search = input('Masukkan nomor transaksi? ')
        kasir_file = open('kasir.txt', 'r')
        temp = open('temp.txt', 'w')
        notrans = kasir_file.readline()

        while notrans != '':
            idtrans = kasir_file.readline()
            nama_product = kasir_file.readline()
            qty = kasir_file.readline()
            harga = kasir_file.readline()
            subtotal = kasir_file.readline()
            idtrans = idtrans.rstrip('\n')
            notrans = notrans.rstrip('\n')
            nama_product = nama_product.rstrip('\n')
            qty = qty.rstrip('\n')
            harga = harga.rstrip('\n')
            subtotal = subtotal.rstrip('\n')

            if notrans == search:
                print('ID Transaksi: TRX-', idtrans)
                print('Nomor Transaksi:', notrans)
                print('Nama Product:', nama_product)
                print('Quantity:', qty)
                print('Harga: ', harga)
                print('Subtotal: ', subtotal)
                print()
                new_product = input('Masukkan nama product baru: ')
                new_qty = int(input('Masukkan quantity baru: '))
                new_harga = int(input('Masukkan harga baru: '))
                new_subtotal = new_qty * new_harga
                temp.write(idtrans + '\n')
                temp.write(notrans + '\n')
                temp.write(new_product + '\n')
                temp.write(str(new_qty) + '\n')
                temp.write(str(new_harga) + '\n')
                temp.write(str(new_subtotal) + '\n')
                found = True

            else:
                temp.write(idtrans + '\n')
                temp.write(str(notrans) + '\n')
                temp.write(nama_product + '\n')
                temp.write(str(qty) + '\n')
                temp.write(str(harga) + '\n')
                temp.write(str(subtotal) + '\n')

            notrans = kasir_file.readline()

        kasir_file.close()
        temp.close()
        os.remove('kasir.txt')
        os.rename('temp.txt', 'kasir.txt')

        if found:
            print('File telah diperbaharui')
        else:
            print('ID tersebut tidak ditemukan dalam file, silakan dicoba lagi')

    except FileNotFoundError:
        print("File kasir.txt tidak ditemukan. Silakan membuat file baru dengan Input Data Transaksi Baru")

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def delete_transaksi():
    try:
        found = False
        search = input('Masukkan ID transaksi? ')
        kasir_file = open('kasir.txt', 'r')
        temp = open('temp.txt', 'w')
        notrans = kasir_file.readline()

        while notrans != '':
            idtrans = kasir_file.readline()
            nama_product = kasir_file.readline()
            qty = kasir_file.readline()
            harga = kasir_file.readline()
            subtotal = kasir_file.readline()
            idtrans = idtrans.rstrip('\n')
            notrans = notrans.rstrip('\n')
            nama_product = nama_product.rstrip('\n')
            qty = qty.rstrip('\n')
            harga = harga.rstrip('\n')
            subtotal = subtotal.rstrip('\n')
            if idtrans != search:
                temp.write(idtrans + '\n')
                temp.write(notrans + '\n')
                temp.write(nama_product + '\n')
                temp.write(str(qty) + '\n')
                temp.write(str(harga) + '\n')
                temp.write(str(subtotal) + '\n')
                found = True
            else:
                notrans = kasir_file.readline()

        kasir_file.close()
        temp.close()
        os.remove('kasir.txt')
        os.rename('temp.txt', 'kasir.txt')

        if found:
            print('File telah diperbaharui')
        else:
            print('ID tersebut tidak ditemukan dalam file.')

    except FileNotFoundError:
        print('File kasir.txt tidak ditemukan.')

    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def main():
    while True:
        print('Silakan pilih menu')
        print('1. Daftar Transaksi Penjualan')
        print('2. Input Data Transaksi Baru')
        print('3. Edit Data Transaksi')
        print('4. Delete Data Transaksi')
        print('5. Exit')
        choice = input('Masukkan pilihan (Nomor) Anda: ')

        try:
            if choice == '1':
                daftar_transaksi()
            elif choice == '2':
                input_transasksi()
            elif choice == '3':
                edit_transaksi()
            elif choice == '4':
                delete_transaksi()
            elif choice == '5':
                break
            else:
                print('Input ulang, dicoba lagi')

        except Exception as e:
            print(f"Terjadi kesalahan")

main()