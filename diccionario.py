import wikipedia

# Buscar información en Wikipedia
search_term = input("Introduce un término de búsqueda: ")
results = wikipedia.search(search_term)

# Seleccionar el resultado deseado
print("Resultados para '", search_term, "'")
for i, result in enumerate(results):
    print(i+1, "-", result)

selection = int(input("Selecciona el resultado deseado: ")) - 1
page = wikipedia.page(results[selection])

# Mostrar información de la página
print("\nTítulo:", page.title)
print("\nContenido:\n", page.content)