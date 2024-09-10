#encontrar los valores mínimos de la función 

import random #Esta libraría se usa para generar números aleattorios 

#Se crea un bucle se ejecuta 10000 veces, cada iteración genera dos números aleatorios
for i in range(10000):    
    num1=round(random.uniform(-4.5,4.5),2)
    num2=round(random.uniform(-4.5, 4.5),2)

    #Se asegura que los dos números generados hayan sido diferentes 
    while num1==num2:
      num2=random.uniform(-4.5,4.5)
    resultado=(1.5-num1+(num1*num2))**2+(2.25-num1+(num1*(num2**2)))**2+(2.625-num1+num1*(num2**3))**2  #Cálculo de la función 

#Comparación para encontrar el menor 
    if i == 0:
      resultado_aux=resultado
    else:
      if resultado<resultado_aux:
        resultado_aux=round(resultado,5)
  
#Resultado final
print(f"Par de números final: {num1}, {num2} = {resultado_aux	}")