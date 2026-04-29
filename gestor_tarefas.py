# ==========================================
# GESTOR DE TAREFAS
# ==========================================
# ==========================================
# Gabriel Lopes
# ==========================================

# ==========================================
# 1. IMPORTAÇÕES
# ==========================================

import json
import os


# ==========================================
# 2. CONFIGURAÇÃO DO FICHEIRO DE DADOS
# ==========================================

FICHEIRO_TAREFAS = "tarefas.json"


# ==========================================
# 3. CARREGAR TAREFAS
# ==========================================

def carregar_tarefas():
    if not os.path.exists(FICHEIRO_TAREFAS):
        return []

    try:
        with open(FICHEIRO_TAREFAS, "r", encoding="utf-8") as ficheiro:
            return json.load(ficheiro)
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro. A iniciar lista vazia.")
        return []


# ==========================================
# 4. GUARDAR TAREFAS
# ==========================================

def guardar_tarefas(tarefas):
    with open(FICHEIRO_TAREFAS, "w", encoding="utf-8") as ficheiro:
        json.dump(tarefas, ficheiro, ensure_ascii=False, indent=4)


# ==========================================
# 5. MOSTRAR MENU PRINCIPAL
# ==========================================

def mostrar_menu():
    print("\n========== GESTOR DE TAREFAS ==========")
    print("1. Ver tarefas")
    print("2. Adicionar tarefa")
    print("3. Marcar tarefa como concluída")
    print("4. Apagar tarefa")
    print("5. Sair")
    print("=======================================")


# ==========================================
# 6. VER TAREFAS
# ==========================================

def ver_tarefas(tarefas):
    print("\n========== LISTA DE TAREFAS ==========")

    if not tarefas:
        print("Ainda não há tarefas registadas.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        estado = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['titulo']} - {estado}")


# ==========================================
# 7. ADICIONAR TAREFA
# ==========================================

def adicionar_tarefa(tarefas):
    titulo = input("\nDigite o título da tarefa: ").strip()

    if titulo == "":
        print("O título da tarefa não pode estar vazio.")
        return

    nova_tarefa = {
        "titulo": titulo,
        "concluida": False
    }

    tarefas.append(nova_tarefa)
    guardar_tarefas(tarefas)

    print("Tarefa adicionada com sucesso!")


# ==========================================
# 8. MARCAR TAREFA COMO CONCLUÍDA
# ==========================================

def concluir_tarefa(tarefas):
    ver_tarefas(tarefas)

    if not tarefas:
        return

    try:
        numero = int(input("\nDigite o número da tarefa concluída: "))

        if numero < 1 or numero > len(tarefas):
            print("Número inválido.")
            return

        tarefas[numero - 1]["concluida"] = True
        guardar_tarefas(tarefas)

        print("Tarefa marcada como concluída!")

    except ValueError:
        print("Por favor, digite um número válido.")


# ==========================================
# 9. APAGAR TAREFA
# ==========================================

def apagar_tarefa(tarefas):
    ver_tarefas(tarefas)

    if not tarefas:
        return

    try:
        numero = int(input("\nDigite o número da tarefa que deseja apagar: "))

        if numero < 1 or numero > len(tarefas):
            print("Número inválido.")
            return

        tarefa_removida = tarefas.pop(numero - 1)
        guardar_tarefas(tarefas)

        print(f"Tarefa '{tarefa_removida['titulo']}' apagada com sucesso!")

    except ValueError:
        print("Por favor, digite um número válido.")


# ==========================================
# 10. FUNÇÃO PRINCIPAL
# ==========================================

def main():
    tarefas = carregar_tarefas()

    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ").strip()

        print(f"\nOpção escolhida: {opcao}")

        if opcao == "1":
            print("A abrir a lista de tarefas...")
            ver_tarefas(tarefas)
            input("\nPrima ENTER para voltar ao menu...")

        elif opcao == "2":
            adicionar_tarefa(tarefas)
            input("\nPrima ENTER para voltar ao menu...")

        elif opcao == "3":
            concluir_tarefa(tarefas)
            input("\nPrima ENTER para voltar ao menu...")

        elif opcao == "4":
            apagar_tarefa(tarefas)
            input("\nPrima ENTER para voltar ao menu...")

        elif opcao == "5":
            print("\nA sair do gestor de tarefas. Até breve!")
            break

        else:
            print("Opção inválida. Tente novamente.")
            input("\nPrima ENTER para voltar ao menu...")


# ==========================================
# 11. INICIAR O PROGRAMA
# ==========================================

if __name__ == "__main__":
    main()
