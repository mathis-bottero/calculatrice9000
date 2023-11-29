def menu():
    print('\n')
    print("Choice 1: Perform Calculation")
    print("Choice 2: Show history")
    print("Choice 3: Delete history")
    print("Choice 4: Exit")


def calculator():
    history = []

    while True:
        menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            calculatrice(history)
        elif choice == '2':
            show_history(history)
        elif choice == '3':
            delete_history(history)
        elif choice == '4':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")



def calculatrice(history):
    try:
        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le deuxième nombre : "))

        operation = input("Entrez le type d'opération (+, -, *, /) : ")

        if operation == '+':
            resultat = nombre1 + nombre2
        elif operation == '-':
            resultat = nombre1 - nombre2
        elif operation == '*':
            resultat = nombre1 * nombre2
        elif operation == '/':
            if nombre2 != 0:
                resultat = nombre1 / nombre2
            else:
                print("Erreur : Division par zéro n'est pas autorisée.")
                return
        else:
            print("Erreur : Opération non valide. Utilisez l'un des opérateurs suivants : +, -, *, /")
            return
        
        history.append(f"{nombre1} {operation} {nombre2} = {resultat}")
        print(f"Le résultat de {nombre1} {operation} {nombre2} est égal à {resultat}")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")


def show_history(history):
    print("\nCalculation history:")
    for calc in history:
        print(calc)


def delete_history(history):
    history.clear()
    print("Calculation history has been deleted.")
    
calculator()