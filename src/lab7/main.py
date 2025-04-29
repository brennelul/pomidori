import zipfile
import sys


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-l' and len(sys.argv) > 2:
            try:
                with zipfile.ZipFile(sys.argv[2], 'r') as z:
                    print(f"Содержимое архива {sys.argv[2]}:")
                    z.printdir()
            except:
                print("Ошибка при открытии архива")
        elif sys.argv[1] == '-u' and len(sys.argv) > 2:
            extract_to = sys.argv[3] if len(sys.argv) > 3 else '.'
            try:
                with zipfile.ZipFile(sys.argv[2], 'r') as z:
                    z.extractall(extract_to)
                    print(f"Архив распакован в {extract_to}")
            except:
                print("Ошибка при распаковке")

    else:
        print("\n1. Просмотреть архив\n"
              "2. Распаковать архив\n"
              "3. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            path = input("Введите путь к архиву: ")
            try:
                with zipfile.ZipFile(path, 'r') as z:
                    print("Содержимое архива:")
                    z.printdir()
            except:
                print("Ошибка при открытии архива")
        elif choice == '2':
            path = input("Введите путь к архиву: ")
            extract_to = input("Куда распаковать (оставьте пустым для текущей папки): ") or '.'
            try:
                with zipfile.ZipFile(path, 'r') as z:
                    z.extractall(extract_to)
                    print(f"Архив распакован в {extract_to}")
            except:
                print("Ошибка при распаковке")


if __name__ == "__main__":
    main()