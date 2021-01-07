# DDL -->
CREATE DATABASE kantor;

CREATE TABLE pegawai(
    no INT,
    nama VARCHAR(255),
    
);

CREATE TABLE jabatan(
    no INT,
    nama VARCHAR(255)

);

#hapus 
DROP DATABASE kantor;
DROP TABLE pegawai;
DROP TABLE jabatan;

#tambah

ALTER TABLE pegawai ADD COLUMN jabatan INT;

# DML -->
INSERT INTO pegawai VALUES(1, 'Nita', '1564326');

INSERT INTO pegawai(no, nama, nik)
    VALUES(2,'Evri', '1564327')

INSERT INTO jabatan VALUES(1, 'Sekretaris');
INSERT INTO jabatan VALUES(2, 'Kepala');

DELETE FROM pegawai WHERE no=2;

UPDATE pegawai SET nik='1564325' WHERE no=1;
UPDATE pegawai SET jabatan=1 WHERE no=1;
UPDATE pegawai SET jabatan=2 WHERE no=2;

# DQL -->
SELECT * FROM pegawai;
SELECT * FROM jabatan;

SELECT nik, nama FROM pegawai;

SELECT p.nik, p.nama, j.nama as jabatan FROM pegawai p
JOIN jabatan j ON p.jabatan=j.no;

# DCL -->