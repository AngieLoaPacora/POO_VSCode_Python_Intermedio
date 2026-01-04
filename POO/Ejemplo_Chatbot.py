import random

class AdvancedChatbot:
    def __init__(self):
        self.runnig=True
        self.responses={
            "hola": ["¡Hola! ¿Cómo estás?", "¡Hola! ¿En qué puedo ayudarte?", "¡Buenas! ¿Qué tal?"],
            "adios": ["Adiós, ¡que tengas un buen día!", "Hasta luego linda, cuidate.", "Nos vemos, ¡hasta pronto!"],
            "cómo estás": ["Estoy bien, gracias por preguntar.", "¡Genial! ¿Y tú?","¡Haciendo lo mejor para avanzar!"],
            "cual es tu nombre": ["Soy un chatbot simple, creado por Angie Loa.", "Me llamo Boti, ¿y tú?", "Me gusta el nombre de Boti, soy un asistente."],
            "cuál es tu función": ["Mi función es responder tus preguntas.", "Estoy aqui para ayudarte.", "¡Mi trabajo es chatear contigo!"]
        }
        self.default_response=[
            "No estoy seguro de cómo responder a eso.",
            "Podrías intentar preguntarme algo más",
            "Lo siento, aún estoy aprendiendo. ¿Podrías preguntar de otra manera?"
        ]
    def start_chat(self):
        print("ChatBot avanzado iniciado. Escribe'salir' para finalizar. \n")
        while self.runnig:
            user_message=input("Usuario:").strip(). lower()
            
            if user_message=="salir":
                self.runnig=False
                print("Chatbot finalizado. Hasta luego linda!")
            else:
                bot_response= self.generate_response(user_message)
                print("Boti:", bot_response)
    
    def generate_response(self,user_message):
        #Buscand una respuesta clave del usuario
        for keyword,response in self.responses.items():
            if keyword in user_message:
                return random.choice(response)
        #Si no encontro una palabra clave, usar una respuesta pre determinada
        return random.choice(self.default_response)

if __name__=="__main__":
    chatbot=AdvancedChatbot()
    chatbot.start_chat()