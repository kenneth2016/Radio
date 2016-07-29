class radio():
	def __init__ (self, marca):
		self.marca= marca
		self.encendido = False
		self.volumen= 0
		self.emisora_AM= 300
		self.emisora_FM= 87.0
		self.en_FM= True

	def encender (self):
		self.encendido=True

	def apagar (self):
		self.encendido=False

	def subir_volumen(self):
		if self.volumen>= 100:
			self.volumen=100
		else:
			self.volumen+=5

	def bajar_volumen(self):
		if self.volumen<=1:
			self.volumen=1
		else:
			self.volumen-=5

	def subir_estacion(self):
		if not self.emisora_FM:
			if self.emisora_AM>=1300:
				self.emisora_AM=300
			else:
				self.emisora_AM+=40

		else:
			if not self.emisora_AM:
			if self.emisora_AM>=107.0:
				self.emisora_AM=87.0
			else:
				self.emisora_AM+=0.5




