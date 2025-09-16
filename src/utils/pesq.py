#Danyelle
import json
import os
def search_eventos(evento):
    termo = input("Digite o nome do evento para buscar: ").strip().lower()
    encontrados = [p for p in evento if termo in p['nome'].lower()]

    if not encontrados:
        print("Nenhum evento encontrado com esse nome.\n")
        return

    print("\n--- Resultados da Pesquisa ---")
    for evento in encontrados:
        print(f"ID: {evento['id']} | Nome: {evento['nome']} | Data: {evento['data']} | Local: {evento['local']} | Descrição: {evento['descrição']} | Tipo: {evento['tipo']} ")
    print()
