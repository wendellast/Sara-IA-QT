#!/bin/bash
#Modulos pip para A sara Linux
#------------------------------------------
echo "
»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
			SARA IA Modulos
««««««««««««««««««««««««««««««««««««««««««««««««««««««««
Por favor use o >= Python3.10 para que não dê nenhum erro
"

echo

echo "------------------------------"
echo "Vamos instalar todos os moulos requisitados"
echo -e "Iniciando... \n"

echo "Atualizando Sistema"
#Atualizando Sistema
sudo apt update
sudo apt upgrade

echo

echo "Instalação do Pip"
#Instalação do Pip
sudo apt install python3-pip

echo

echo "Instalação modulos Apt"
#Modulos Apt
sudo apt-get install python-tk
sudo apt install -y python3-tk
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
pip install pyaudio --user
sudo apt-get install espeak
sudo apt-get install vlc
echo

echo "Instalação modulos Pip"
#Modulos PIP
pip3 install vosk
pip3 install rich
pip3 install PyQt5
pip3 install tk
pip3 install tk-tools
pip3 install PythonTurtle
pip3 install plyer
pip3 install psutil
pip3 install pipwin
pip3 install pyttsx3
pip3 install SpeechRecognition
pip3 install python-vlc
pip3 install wikipedia

echo


echo "Prontinho Finalizado"
echo "------------------------------"
#------------------------------------------

