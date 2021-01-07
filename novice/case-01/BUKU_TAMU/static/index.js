function hapus(id) {
    let yakin = confirm('Beneran nih mau hapus ya?');
        yakin = confirm('Ya udah lah terserah loe deh hapus - hapus ajalah?');

    if (yakin) {
        window.location = `/registrasi/${id}/hapus`;
    }
}