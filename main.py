from pathlib import Path

import uvicorn

from logger import LoggerBuilder
from src.app import app
from src.database.database_context import Base, engine

# Create logs dir if it doesn't exist yet:
Path("logs").mkdir(exist_ok=True)

logger_builder = LoggerBuilder(path_to_config="log.ini", logging_dir="logs/log.out")
logger = logger_builder.create_logger()

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    cwd = Path(__file__).parent.resolve()
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=f"{cwd}/log.ini")
