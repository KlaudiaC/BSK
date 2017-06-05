from OpenSSL import crypto

key_file = open('priv_key.pem', 'r')  # moj klucz prywatny
key = crypto.load_privatekey(crypto.FILETYPE_PEM, key_file.read())

ca_cert_file = open('ca_cert.car', 'r') # moj certyfikat
ca_cert = crypto.load_certificate(crypto.FILETYPE_PEM, ca_cert_file.read())

csr_file = open('next_person.csr', 'r') # CSR nastepnej osoby
csr = crypto.load_certificate_request(crypto.FILETYPE_PEM, csr_file.read())

cert = crypto.X509()
cert.set_subject(csr.get_subject())
cert.set_pubkey(csr.get_pubkey())
cert.set_issuer(ca_cert.get_subject())
cert.set_serial_number(7)
cert.gmtime_adj_notBefore(0)
cert.gmtime_adj_notAfter(365*24*60*60)
cert.sign(key, 'sha256')
print crypto.dump_certificate(crypto.FILETYPE_PEM, cert)
