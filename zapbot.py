from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Teste de automação de mensagem no WPP"
        self.pessoas = ["Júlia Emily", "Nicole Guerreiro", "Bruna Almeida"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path="D:\BOT WHATSAPP\chromedriver.exe", chrome_options=options)

    def EnviarMensagens(self):
        # <span dir="auto" title="Júlia Emily" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr"><span class="matched-text i0jNr">Jú</span>lia Emily</span>
        # <div tabindex="-1" class="p3_M1">
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
                
        for pessoa in self.pessoas:
            campo_pessoa = self.driver.find_element_by_xpath(
                f"//span[@title='{pessoa}']")
            time.sleep(3)
            campo_pessoa.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)
            
bot = WhatsappBot()
bot.EnviarMensagens()