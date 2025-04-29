import os
import json
import shutil
import logging
import argparse
from datetime import datetime, timedelta

CONFIG_FILE = 'config.json'
LOG_FILE = 'backup.log'


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def load_config():
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Ошибка при загрузке конфигурации: {e}")
        return None

def save_config(config):
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        logging.error(f"Ошибка при сохранении конфигурации: {e}")

def interactive_config():
    config = {
        "backup_paths": [],
        "backup_dir": "",
        "period_days": 1,
        "last_backup": ""
    }

    try:
        config['period_days'] = int(input("Периодичность (в днях): "))
        config['backup_dir'] = input("Папка для резервных копий: ")

        while True:
            path = input("Добавьте путь для копирования (или Enter для завершения): ")
            if not path:
                break
            config['backup_paths'].append(path)

        config['last_backup'] = datetime.now().strftime('%Y-%m-%d %H:%M')
        save_config(config)
        print("Конфигурация сохранена.")
    except Exception as e:
        logging.error(f"Ошибка в интерактивной настройке: {e}")
        print("Произошла ошибка при настройке конфигурации.")

def do_backup(config):
    try:
        last_backup = datetime.strptime(config['last_backup'], '%Y-%m-%d %H:%M')
        now = datetime.now()

        if now - last_backup < timedelta(days=config['period_days']):
            print("Пока рано делать резервное копирование.")
            return

        backup_folder = os.path.join(config['backup_dir'], f"backup_{now.strftime('%Y%m%d_%H%M')}")
        os.makedirs(backup_folder, exist_ok=True)

        for path in config['backup_paths']:
            if not os.path.exists(path):
                logging.error(f"Путь не существует: {path}")
                continue
            try:
                if os.path.isfile(path):
                    shutil.copy(path, backup_folder)
                else:
                    shutil.copytree(path, os.path.join(backup_folder, os.path.basename(path)))
                logging.info(f"Скопировано: {path}")
            except Exception as e:
                logging.error(f"Ошибка при копировании {path}: {e}")

        config['last_backup'] = now.strftime('%Y-%m-%d %H:%M')
        save_config(config)
        logging.info("Резервное копирование завершено.")
        print("Резервное копирование выполнено.")
    except Exception as e:
        logging.error(f"Ошибка при резервном копировании: {e}")
        print("Произошла ошибка при выполнении резервного копирования.")

def main():
    parser = argparse.ArgumentParser(description='Резервное копирование с учётом даты и времени')
    parser.add_argument('--config', action='store_true', help='Настройка конфигурации')

    args = parser.parse_args()

    if args.config:
        interactive_config()
    else:
        config = load_config()
        if config:
            do_backup(config)
        else:
            print("Ошибка: не удалось загрузить конфигурацию.")

if __name__ == "__main__":
    main()