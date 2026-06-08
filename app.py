from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# ═══════════════════════════════════════════
#   IDENTITAS MAHASISWA
#   Nama  : Vika Nahran Azizah Aulia
#   NIM   : K3525087
#   Tugas : UAS Pendidikan Agama Islam
# ═══════════════════════════════════════════


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(BASE_DIR, 'dakwah-rahmatan.html')

@app.route('/')
def index():
    """Halaman utama - menampilkan website Dakwah Rahmatan Lil 'Alamin."""
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html_content = f.read()
    return render_template_string(html_content)


@app.route('/health')
def health():
    """Health check endpoint."""
    return {'status': 'ok', 'message': 'Alhamdulillah, server berjalan dengan baik!'}, 200


if __name__ == '__main__':
    print("=" * 55)
    print("  ✦ Dakwah Rahmatan Lil 'Alamin - Web Server ✦")
    print("=" * 55)
    print("  Nama  : Vika Nahran Azizah Aulia")
    print("  NIM   : K3525087")
    print("  Tugas : UAS Pendidikan Agama Islam")
    print("=" * 55)
    print(f"  Buka browser dan akses: http://localhost:5000")
    print("  Tekan Ctrl+C untuk menghentikan server.")
    print("=" * 55)
    app.run(debug=True, host='0.0.0.0', port=5000)
