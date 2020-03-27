from pathlib import Path
import os


PROJECT_ROOT = Path(os.path.abspath(__file__)).parents[4]
APPS_ROOT = os.path.join(PROJECT_ROOT, 'src', 'portfolio', 'app')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')

STATICFILES_DIRS = (
    os.path.join(APPS_ROOT, "static"),
)
