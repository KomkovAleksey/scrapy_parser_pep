from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

PEP_DOMAIN = 'peps.python.org'
ALLOWED_DOMAINS = [PEP_DOMAIN, ]
PEP_SPIDER_NAME = 'pep'
