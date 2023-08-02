import os
import time

from pathlib import Path

class Colors:
	"""A helper to set the colors of the log level."""
	COLORS = {
		"INFO": "\033[96m",
		"WARN": "\033[93m",
		"ERROR": "\033[91m",
		"ENDC": "\033[0m"
	}
	
	@staticmethod
	def get_color(log_level):
		"""Get color based on the log_level.
		
		Arguments
		---
		log_level: "INFO" to debug, "WARN" to warnings or "ERROR" to errors.
		"""
		return Colors.COLORS[log_level.upper()]

class Logger:

	@staticmethod
	def __verify_data(data: str) -> bool:
		"""Verify if data is not a empty string."""
		assert len(data), "The data cannot be empty."
	
	@staticmethod		
	def __get_time():
		"""Returns the current timestamp."""
		return time.time()

	def __init__(self, filename: str, filepath: str = "./logs/"):
		self.filepath = None
		self.__create_filename(filepath, filename)
		self.end_color = Colors.get_color("ENDC")
		
		self.file = open(self.filepath, "w")
			
	def __create_filename(self, filepath: str, filename: str) -> None:
		"""Create the logs directory and the filename with timestamp.
		
		Arguments
		---
		filepath: The path to save the logs.
		filename: The name of log file.
		"""
		timestamp = Logger.__get_time()
		filepath = Path(filepath)
		os.makedirs(filepath, exist_ok=True)
		
		filename = f"{filename}_{timestamp}.txt" \
						if len(filename) else \
						f"log_{timestamp}.txt"
						
		self.filepath = os.path.join(filepath, filename)
		
	def __write_data(self, data: str) -> None:
		"""Write the data string in the log file.
		
		Arguments
		---
		data: The string you want will be written to the log file.
		"""
		data = data + "\n"
		timestamp = Logger.__get_time()
		_data = f"[{timestamp}]: {data}"
		self.file.write(_data)
		
	def log(self, data: str, verbose: bool = True, log_level: str = "INFO") -> None:
		"""Show the information in screen and write in the log file.
		
		Arguments
		---
		data: 
		verbose: A boolean that allows showing the information on the scrreen or not.
		log_level: "INFO" to debug, "WARN" to warnings or "ERROR" to errors.
		"""
		log_level_up = log_level.upper()
		color = Colors.get_color(log_level_up)
		
		_data = f"[{log_level_up}]: {data}"
		if verbose:
			print(f"{color}{_data}{self.end_color}")
		
		self.__write_data(_data)
		
	def __del__(self):
		"""A destructor to close the log file when finished."""
		_data = f"The processing finished."
		self.log(_data, log_level="INFO")
		self.file.close()
		
if __name__ == "__main__":
	log = Logger(filename="teste01")
	log.log("iniciando codigo", log_level="INFO")
	log.log("um warning apareceu", log_level="WARN")
	log.log("um erro apareceu", log_level="ERROR")

