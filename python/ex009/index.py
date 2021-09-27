# Aula 9 - Elementos condicionais - para isso, tens que dar o comando para o computador escrever se estiver certo e também se estiver errado

#IF 
if 5 == 15/3:
    print ("é isso ai!")

# agora, neste caso a seguir não teremos resposta de saída, pq é diferente o resultado
if 5 == 18/3:
    print ("é")

if 5 != 3 * 6:
    print ("done")

# ELSE - O computador entende que é pra dar a resposta contrária ao IF

x = 1
if x > 3:
    print ("maior")
else:
    print ("menor")

#ELIF - O computador entende que é algo diferente de IF e ELSE

def compare_to_five (y):
    if y > 5:
        print ("greater")
    elif y < 5:
        print ("Less")
    else:
        return "Equal"

print (compare_to_five(10))
print (compare_to_five(2))
