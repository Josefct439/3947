meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }

for i in range(len(meme_dict)):
    print(meme_dict.keys()[i])

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(word, "significa:",meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print(word, "no se encuentra en el diccionario")
