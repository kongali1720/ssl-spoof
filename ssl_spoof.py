import time

def tampilkan_sertifikat(title, cert):
    print(f"\n🔒 Sertifikat: {title}")
    print("=" * 40)
    for key, value in cert.items():
        print(f"{key:15}: {value}")
    print("=" * 40)

def simulasi_ssl_spoof():
    cert_asli = {
        "Common Name": "www.bankasli.com",
        "Issuer": "DigiCert Inc",
        "Valid From": "2025-01-01",
        "Valid To": "2026-01-01",
        "SHA-256 Fingerprint": "AB:CD:EF:01:23:45:..."
    }

    cert_palsu = {
        "Common Name": "www.bankasli.com",
        "Issuer": "Unknown CA (Palsu)",
        "Valid From": "2025-01-01",
        "Valid To": "2026-01-01",
        "SHA-256 Fingerprint": "FF:EE:DD:CC:BB:AA:..."
    }

    print("""
╔══════════════════════════════════════╗
║     🛡️ SSL Spoof - Simulasi Edukasi     ║
║       Sertifikat Asli vs Palsu       ║
╚══════════════════════════════════════╝
""")
    time.sleep(1)
    tampilkan_sertifikat("ASLI", cert_asli)
    time.sleep(2)
    tampilkan_sertifikat("PALSU", cert_palsu)

    print("""
🚨 Penting:
- Sertifikat palsu bisa terlihat mirip secara kasat mata.
- Selalu cek "Issuer" dan "Fingerprint" di browser kamu.
- Jangan asal klik lanjut jika ada peringatan sertifikat!

✅ Edukasi selesai - Semoga makin waspada!
""")

if __name__ == "__main__":
    input("Tekan Enter untuk mulai simulasi SSL palsu...")
    simulasi_ssl_spoof()
