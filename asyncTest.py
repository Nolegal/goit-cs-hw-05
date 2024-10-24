import argparse
import asyncio
import logging

from aiopath import AsyncPath
from aioshutil import copyfile



#програму потрібно запустити через консоль з аргументами, як приклад
# python asyncTest.py path/to/copy/from

async def read_folder(path: AsyncPath) -> None:
    # Дописати асинхронну функцію, яка рекурсивно читає всі файли у вихідній папці та її підпапках
    # Схожий код як було в курсі "Базові Алгоритми", але тепер з async та await
    parser = argparse.ArgumentParser(description="Копіювання файлів з сортуванням за розширеннями.")
    parser.add_argument("--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("--dest", type=Path, default=Path("dist"), help="Шлях до директорії призначення")
    return parser.read_folder()

async def copy_file(file: AsyncPath) -> None:
 try:
        for file in src.iterdir():
            print(file)
            if file.is_dir():
             copy_files(file, dst) # Рекурсивний виклик для піддиректорії
            else:
                # Копіювання файлу
                extension = file.suffix[1:]
                if extension:
                    extension_dir=dst/extension
                await extension_dir.mkdir(parents=True, exit_ok=True)
                await copyfile(file, extension_dir)
 except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")






    # extension_name = file.suffix[1:]
    # extension_folder = output / extension_name
    # #TODO Логування обробки помилок через logging
    # await extension_folder.mkdir(exist_ok=True, parents=True)
    # await copyfile(file, extension_folder / file.name)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

    #TODO Створити об'єкт ArgumentParser для обробки аргументів командного рядка
   
   
    parser = argparse.ArgumentParser()
    args = vars(parser.parse_args())
    source = AsyncPath(args.get("source"))
    output = AsyncPath(args.get("output"))

    asyncio.run(read_folder(source))

    # Для перевірки на умову виконання PEP8 рекомендую використати pycodestyle
    # Приклад застосування "pycodestyle --show-source --show-pep8 exercise_10_async.py"
    # TODO

    #програму потрібно запустити через консоль з аргументами, як приклад
    # python asyncTest.py path/to/copy/from
