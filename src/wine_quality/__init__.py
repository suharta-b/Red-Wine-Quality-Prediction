import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(message)s]"

log_dir = "wine_quality_logs"
log_filepath = os.path.join(log_dir, "project_log.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("wineQualityLogger")
