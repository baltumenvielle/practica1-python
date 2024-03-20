import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
vocals = ["a", "e", "i", "o", "u"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_fails = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

difficulty = int(input("Ingrese la dificultad en la que quieres jugar! 1. Fácil 2. Medio 3. Difícil "))

# Valida que se ingrese una dificultad válida
while (difficulty > 3) or (difficulty < 1):
	difficulty = int(input("Ingresaste una dificultad no válida. Ingrese alguna de las siguientes: 1. Fácil 2. Medio 3. Difícil "))
 
word_displayed = "_" * len(secret_word)

if (difficulty == 1):
	NotImplemented

elif (difficulty == 2):
	NotImplemented


# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

# Inicializa la cantidad de fallos en 0
fails = 0

# Itera hasta que la cantidad de fallos alcance el maximo posible
while (fails < max_fails):
	# Pedir al jugador que ingrese una letra
	letter = input("Ingresa una letra: ").lower()
 
	# Si no se ingresó nada, se vuelve a intentar ingresar una letra
	if letter == "":
		print("No ingresaste ninguna letra. Intenta con otra")
		continue
 
	# Verificar si la letra ya ha sido adivinada
	if letter in guessed_letters:
		print("Ya has intentado con esa letra. Intenta con otra.")
		continue

 	# Agregar la letra a la lista de letras adivinadas
	guessed_letters.append(letter)

 	# Verificar si la letra está en la palabra secreta
	if letter in secret_word:
		print("¡Bien hecho! La letra está en la palabra.")
	else:
		print("Lo siento, la letra no está en la palabra.")
		fails += 1
 
	# Mostrar la palabra parcialmente adivinada
	letters = []
	for letter in secret_word:
		if letter in guessed_letters:
			letters.append(letter)
		else:
			letters.append("_")
   
	word_displayed = "".join(letters)
	print(f"Palabra: {word_displayed}")
 
	# Verificar si se ha adivinado la palabra completa
	if word_displayed == secret_word:
		print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
		break
else:
	print(f"¡Oh no! Has agotado tus {max_fails} intentos.")
	print(f"La palabra secreta era: {secret_word}")
