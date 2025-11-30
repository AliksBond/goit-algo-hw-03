import os
import shutil
import argparse

def copy_files_recursive(src_dir, dest_dir):
    try:
        items = os.listdir(src_dir)
    except PermissionError:
        print(f"❌ Немає доступу до: {src_dir}")
        return
    except FileNotFoundError:
        print(f"❌ Директорію не знайдено: {src_dir}")
        return

    for item in items:
        src_path = os.path.join(src_dir, item)
        if os.path.isdir(src_path):
            copy_files_recursive(src_path, dest_dir)
        elif os.path.isfile(src_path):
            ext = os.path.splitext(item)[1][1:].lower() or "no_extension"
            dest_subdir = os.path.join(dest_dir, ext)
            os.makedirs(dest_subdir, exist_ok=True)
            dest_path = os.path.join(dest_subdir, item)
            try:
                shutil.copy2(src_path, dest_path)
                print(f"📄 Копіюю: {src_path} → {dest_path}")
            except Exception as e:
                print(f"❌ Помилка копіювання {src_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання файлів за розширеннями.")
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument("dest", nargs="?", default="dist", help="Тека призначення (за замовчуванням dist)")
    args = parser.parse_args()

    src = args.source
    dest = args.dest

    if not os.path.exists(src):
        print("❌ Вихідної директорії не існує!")
        return

    os.makedirs(dest, exist_ok=True)
    copy_files_recursive(src, dest)
    print("✅ Готово!")

if __name__ == "__main__":
    main()
