
print('\t\t\t\t\t\t\t\t\tDATA KARYAWAN PT. RPMI')
m = input('Silahkan input pilihan anda \n1. Melihat Data Karyawan\n2. Mengedit Data Karyawan\n')
if m=='1':
    print('Menampilkan data karyawan')
    ID_karyawan = {
    1:'R240001',
    2:'R240002',
    3:'R240003',
    4:'R240004',
    5:'R240005',
    6:'R240006',
    7:'R240007'
    }
    nama_karyawan ={
    1:'Shirley',
    2:'Charlie',
    3:'Sabrina',
    4:'Michael',
    5:'Cassandra',
    6:'Alexander',
    7:'Maximilian'
    }
    role ={
    1:'Finance',
    2:'Public Relation',
    3:'Human Resources',
    4:'Marketing',
    5:'Sales',
    6:'BI Analyst',
    7:'Data Analyst'
    } 
    print('ID Karyawan','\tNama Karyawan','\tPosition')
    for i in ID_karyawan:
        print(ID_karyawan[i],'\t',nama_karyawan[i],'\t',role[i])
    print('\n')
else:
    ID_karyawan = {
    1:'R240001',
    2:'R240002',
    3:'R240003',
    4:'R240004',
    5:'R240005',
    6:'R240006',
    7:'R240007'
    }
    nama_karyawan ={
    1:'Shirley',
    2:'Charlie',
    3:'Sabrina',
    4:'Michael',
    5:'Cassandra',
    6:'Alexander',
    7:'Maximilian'
    }
    role ={
    1:'Finance',
    2:'Public Relation',
    3:'Human Resources',
    4:'Marketing',
    5:'Sales',
    6:'BI Analyst',
    7:'Data Analyst'
    } 
    print('Menambah Data Karyawan')
    new_ID = input('Masukkan ID karyawan : ')
    new_name = input ('Masukkan nama karyawan : ')
    new_role = input ('Masukkan pekerjaan karyawan : ')
    ID_karyawan[8]=new_ID
    nama_karyawan[8]=new_name
    role[8]=new_role
    print('NIK Karyawan','\tNama Karyawan','\tPosition')
    for i in ID_karyawan:
        print(ID_karyawan[i],'\t',nama_karyawan[i],'\t',role[i])
    print('\n')
    print('Mengupdate Data Karyawan ')
    x = input('Apakah ID karyawan sudah sesuai? ')
    if x=='No':
        new_ID = input('Silahkan input ID yang sesuai : ')
    y = input ('Apakah nama karyawan sudah sesuai? ')
    if y =='No':
        new_name = input('Silahkan input nama karyawan yang sesuai : ')
    z = input ('Apakah posisi pekerjaan karyawan sudah sesuai? ')
    if z =='No':
        new_role = input('Silahkan input posisi pekerjaan yang sesuai :')
    ID_karyawan[8]=new_ID
    nama_karyawan[8]=new_name
    role[8]=new_role
    print('NIK Karyawan','\tNama Karyawan','\tPosition')
    for i in ID_karyawan:
        print(ID_karyawan[i],'\t',nama_karyawan[i],'\t',role[i])
    print('\n')
    s = input('Apakah ada data yang ingin dihapus? ')
    if s=='No' :
        print('NIK Karyawan','\tNama Karyawan','\tPosition')
        for i in ID_karyawan:
            print(ID_karyawan[i],'\t',nama_karyawan[i],'\t',role[i]) 
    else :
        print('Menghapus data karyawan')
        ID_karyawan.pop(8)
        nama_karyawan.pop(8)
        role.pop(8)
        print('NIK Karyawan','\tNama Karyawan','\tPosition')
        for i in ID_karyawan:
            print(ID_karyawan[i],'\t',nama_karyawan[i],'\t',role[i])