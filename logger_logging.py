import os
import time
import logging

class CustomHandler(logging.Handler):
	def __init__(self, log_file):
		super().__init__()
		self.log_file = log_file

	def emit(self, record):
		try:
			log_message = self.format(record)
			with open(self.log_file, 'a') as file:
				file.write(log_message + '\n')
		except Exception as e:
			print(f"Error while writing to log file: {e}")

if __name__ == "__main__":
	# Configuração do logger
	logger = logging.getLogger("ExemploLogger")
	logger.setLevel(logging.DEBUG)

	# Criando e configurando a instância do handler personalizado
	log_folder = "./logs/"
	os.makedirs(log_folder, exist_ok=True)
	log_file = os.path.join(log_folder, f"log_{time.time()}.log")
	custom_handler = CustomHandler(log_file)
	formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
	custom_handler.setFormatter(formatter)

	# Criando e configurando o StreamHandler para exibir no terminal
	stream_handler = logging.StreamHandler()
	stream_handler.setFormatter(formatter)

	# Adicionando os handlers personalizados ao logger
	logger.addHandler(custom_handler)
	logger.addHandler(stream_handler)

	# Exemplo de uso do logger
	logger.debug("Esta é uma mensagem de debug.")
	logger.info("Esta é uma mensagem informativa.")
	logger.warning("Atenção! Esta é uma mensagem de aviso.")
	logger.error("Ocorreu um erro.")
	logger.critical("Este é um erro crítico!")
