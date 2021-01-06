function hapus(id) {
    let yakin = confirm('Yakin Mau dihapus nih?');
    
    if (yakin) {
        window.location = `/registrasi/${id}/hapus`;
    }
}