import hashlib
import os
import binascii


chave_secreta = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"

# Criptografia de senha 1
def criptografar_minha_senha1(senha):
  """
  Criptografa a senha usando o algoritmo MD5.
  """
  senha = senha + chave_secreta
  hash_md5 = hashlib.md5()
  hash_md5.update(senha.encode("utf-8"))
  return hash_md5.hexdigest()

# Criptografia de senha 2
def criptografar_minha_senha2(senha):
  """
  Criptografa a senha usando o algoritmo SHA-256.
  """
  senha = senha + chave_secreta
  hash_sha256 = hashlib.sha256()
  hash_sha256.update(senha.encode("utf-8"))
  return hash_sha256.hexdigest()

# Criptografia de senha 3
def criptografar_minha_senha3(senha):
  """
  Criptografa a senha usando o algoritmo PBKDF2 com um salt aleatório de 128 bits.

  """
  senha = senha + chave_secreta
  salt = os.urandom(128)
  algoritmo = 'sha256'
  senha_criptografada = hashlib.pbkdf2_hmac(
      algoritmo,
      senha.encode("utf-8"),
      salt,
      100000,
      dklen=128)
  senha_hex = binascii.hexlify(senha_criptografada).decode('utf-8')
  return senha_hex

# Exemplo de uso
senha1 = "5678910"
senha2 = "senhasegura"
senha3 = "password"

senha1_criptografada = criptografar_minha_senha1(senha1)
senha2_criptografada = criptografar_minha_senha2(senha2)
senha3_criptografada = criptografar_minha_senha3(senha3)

print("Senha em MD5: " + senha1_criptografada)

print("Senha em SHA256: " + senha2_criptografada)

print("Senha em PBKDF2: " + senha3_criptografada)

