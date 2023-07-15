import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
simboys = "@#$%^&*()!"
for_pass = lower_case + upper_case + numbers + simboys
tamanho_da_senha = 12 
password = "".join(random.sample(for_pass, tamanho_da_senha))

print("A senha gerada foi:", password)
