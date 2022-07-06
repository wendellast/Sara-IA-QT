#!/bin/bash
#Modulos pip para A sara Linux


#variaveis
ppp="\e[m"
preto="\e[30;1m"
vermelho="\e[31;1m"
verde="\e[32;1m"
amarelo="\e[33;1m"
azul="\e[34;1m"
rosa="\e[35;1m"
ciano="\e[36;1m"
branco="\e[37;1m"

titulo="\e[31;1m"

linha="»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»"
#------------------------------------------
echo -e " "$titulo"
»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
			SARA IA Modulos 
«««««««««««««««««««««««««««««««««««««««««««««««««««««««« "$ppp"
"$amarelo"Por favor use o Python >= 3.10 para que não ajar nenhum erro
"$ppp"
"

echo -e ""$verde""$linha""$ppp""

echo -e  ""$ciano"Vamos instalar todos os moulos requisitados"$ppp""

echo -e ""$verde""$linha""$ppp""
echo -e ""$azul"Iniciando... "$ppp""
echo -e ""$verde""$linha""$ppp""


echo -e ""$rosa"Atualizando Sistema "$ppp""
#Atualizando Sistema
sudo apt update -y
sudo apt upgrade -y

echo -e ""$verde""$linha""$ppp""

echo -e ""$rosa"Instalação do Pip"$ppp""
#Instalação do Pip
sudo apt install python3-pip

echo -e ""$verde""$linha""$ppp""

echo -e ""$rosa"Instalação modulos Apt "$ppp""
#Modulos Apt
sudo apt-get install python-tk
sudo apt install -y python3-tk
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
pip install pyaudio --user
sudo apt-get install espeak
sudo apt-get install vlc
sudo apt-get install scrot

echo -e ""$verde""$linha""$ppp""

echo -e ""$rosa"Instalação modulos Pip "$ppp""
#Modulos PIP
pip3 install vosk
pip3 install rich
pip3 install PyQt5
pip3 install PythonTurtle
pip3 install plyer
pip3 install psutil
pip3 install pyttsx3
pip3 install SpeechRecognition
pip3 install python-vlc
pip3 install wikipedia
pip3 install pywhatkit
pip install chatterbot==1.0.4
echo -e ""$verde""$linha""$ppp""

echo -e ""$rosa"Atualizando Sistema "$ppp""
#Atualizando Sistema
sudo apt update -y
sudo apt upgrade -y

echo -e ""$azul"Prontinho Finalizado"$ppp""
echo -e ""$verde""$linha""$ppp""
#------------------------------------------

