# CalcApp (Kivy + Buildozer)

Готовый шаблон для сборки APK из Kivy‑приложения через **GitHub Actions**.

## Локальный запуск (на ПК)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install kivy
python main.py
```

## Сборка APK на GitHub

1. Создайте пустой репозиторий и загрузите сюда все файлы.
2. Откройте вкладку **Actions** → запустите workflow **Build Kivy APK** (кнопка _Run workflow_).
3. По окончании сборки скачайте артефакт `calcapp-apk` — внутри будет файл `.apk`.

> Настройки сборки лежат в `buildozer.spec`. При необходимости измените `package.domain`, `package.name`, `requirements` и т.д.