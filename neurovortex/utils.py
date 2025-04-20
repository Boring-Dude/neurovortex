import logging
import time
import platform
import queue
import threading

from functools import wraps
from contextlib import contextmanager


class AsyncLoggingHandler(logging.Handler):
    """
    A Logging handler that processes logs asynchronously.
    """
    def __init__(self):
        super().__init__()
        self.log_queue = queue.Queue()
        self.worker = threading.Thread(targer=self.__process_logs, daemon=True)
        self.worker.start()

    def emit(self, record):
        self.log_queue.put(record)

    def _process_logs(self):
        while True:
            try:
                record = self.log_queue.get()
                if record is None:
                    break
                logging.getLogger(record.name).handle(record)
            except Exception:
                pass

def setup_logging(log_file=None):
    """
    Set up logging configuration.
    
    Args:
        log_file (str): Optional file path to save logs to a file.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    if log_file:
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
    else:
        logging.basicConfig(level=logging.INFO, format=log_format)
    
    return logging.getLogger(__name__)

def log_environment_info():
    """
    Log basic environment information (OS, CPU, Python Version)
    """
    logging.info("System: %s", platform.system())
    logging.info("Release: %s", platform.release())
    logging.info("Version: %s", platform.version())
    logging.info("Python Version: %s", platform.python_version())


def log_exceptions(func):
    """
    A decorator to log exceptions raised by a function.

    Args:
        func (callable): The function to wrap.
    Returns:
        callable: Wrapped function With exception logging.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Exception in `{func.__name__}`: {e}", exc_info=True)
            raise
    return wrapper

def timeit(func):
    """
    A decorator to measure the execution time of a function.
    
    Args:
        func (callable): The function to be timed.
    
    Returns:
        callable: Wrapped function with timing.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

def memory_usage():
    """
    Get the current memory usage of the process.
    
    Returns:
        float: Memory usage in MB.
    """
    try:
        import psutil
        process = psutil.Process()
        mem_info = process.memory_info()
        return mem_info.peak_wset / (1024 ** 2), # Convert bytes to MB (Windows)
    except AttributeError:
        logging.warning("Peak Memory usage may not be available on this platform.")
        return None
    except ImportError:
        logging.warning("psutil is not installed. Memory usage cannot be determined.")
        return None

def gpu_usage():
    """
    Get detailed GPU usage if available.
    
    Returns:
        list: List of dictionaries containing GPU details (name, usage, memory, temperature).
    """
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        return [{
            "name": gpu.name,
            "load": gpu.load * 100,
            "memory_used": gpu.memoryUsed,
            "memory_total": gpu.memoryTotal,
            "temperature": gpu.temperature
        } for gpu in gpus]
    except ImportError:
        logging.warning("GPUtil is not installed. GPU details cannot be determined.")
        return None

@contextmanager
def time_block(name="Block"):
    """
    Context manager to measure the execution time of a code blovk.

    Args:
        name (str): Name of the block
    """
    start_time = time.time()
    yield
    end_time = time.time()
    logging.info(f"{name} executed in {end_time - start_time:.4f} seconds.")

def disk_usage():
    """
    Get the current disk usage statistics.
    
    Returns:
        dict: Disk usage stats (total, used, free) in GB.
    """
    try:
        import shutil
        total, used, free = shutil.disk_usage("/")
        return {
            "total": total / (1024 ** 3),  # Convert bytes to GB
            "used": used / (1024 ** 3),
            "free": free / (1024 ** 3)
        }
    except Exception as e:
        logging.warning(f"Could not determine disk usage: {e}")
        return None
