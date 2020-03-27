from pathlib import Path
import os


BASE_DIR = Path(os.path.abspath(__file__)).parents[4]
APPS_ROOT = os.path.join(BASE_DIR, 'src', 'portfolio', 'app')
STATIC_ROOT = os.path.join(BASE_DIR, 'assets', 'static')
STATICFILES_DIRS = (
    os.path.join(APPS_ROOT, "static"),
)
