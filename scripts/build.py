#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import sys
from pathlib import Path

def run_command(command):
    """Запуск команды и вывод результата."""
    process = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True
    )
    if process.returncode != 0:
        print(f"Ошибка при выполнении команды: {command}")
        print(f"Вывод: {process.stdout}")
        print(f"Ошибки: {process.stderr}")
        sys.exit(1)
    return process.stdout

def clean_build():
    """Очистка директорий сборки."""
    dirs_to_clean = ['build', 'dist', '*.egg-info']
    for pattern in dirs_to_clean:
        for path in Path('.').glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()

def build_package():
    """Сборка пакета."""
    print("Очистка старых файлов сборки...")
    clean_build()

    print("Установка зависимостей для сборки...")
    run_command("pip install build twine")

    print("Сборка пакета...")
    run_command("python -m build")

    print("Проверка собранного пакета...")
    run_command("twine check dist/*")

    print("\nСборка завершена успешно!")
    print("Файлы пакета находятся в директории dist/")
    print("\nДля установки пакета локально:")
    print("pip install dist/oms_cms-0.11.0.tar.gz")
    print("\nДля публикации в PyPI:")
    print("twine upload dist/*")

if __name__ == '__main__':
    build_package() 