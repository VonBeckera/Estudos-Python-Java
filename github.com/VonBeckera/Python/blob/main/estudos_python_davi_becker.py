{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "https://gist.github.com/VonBeckera/890cc00392789d5dd836094d4c7fd563#file-untitled1-ipynb",
      "authorship_tag": "ABX9TyMKuf8gZvugQgSkEuys+nJY",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/VonBeckera/Eclipse/blob/main/github.com/VonBeckera/Python/blob/main/estudos_python_davi_becker.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Estudos de Faculdade e Cursos\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "E_VeYbVjZphx"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "kCjFpoujXt6Q"
      },
      "outputs": [],
      "source": [
        "#1 Manipulando Strings\n",
        "\n",
        "a = input('Digite uma palavra: ')\n",
        "print('O tipo digitado é: ', type(a))\n",
        "print('O tipo digitado tem espaços: ', a.isspace())\n",
        "print('O tipo digitado é um número: ', a.isnumeric())\n",
        "print('O tipo digitado é alfa numerico: ', a.isalnum())\n",
        "print('O tipo digitado e alfabetico: ', a.isalpha())\n",
        "print('O tipo está capitalizado: ', a.istitle())"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Exmplos de precedencias\n",
        "# Exemplo 1\n",
        "n1 = 5\n",
        "n2 = 2\n",
        "n3 = 3\n",
        "s = n1+n2*n3\n",
        "print(s)\n",
        "\n",
        "# Exemplo 2\n",
        "n4 = 3\n",
        "n5 = 5\n",
        "n6 = 4\n",
        "n7 = 2\n",
        "s1 = n4*n5+n6**n7\n",
        "print(s1)\n",
        "# Exemplo 3\n",
        "\n",
        "n8 = 3\n",
        "n9 = 5\n",
        "n0 = 4\n",
        "n11 = 2\n",
        "s2 = n8*(n9+n0)**n11\n",
        "print(s2)\n"
      ],
      "metadata": {
        "id": "OTqlNsOIVpOC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "nome = input('Qual o seu nome? ')\n",
        "print(f'Seja Bem Vindo {nome}!')"
      ],
      "metadata": {
        "id": "hgXzhrxiZufz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "n1 = int(input('Digite um valor ' ))\n",
        "n2 = int(input('Digite outro valor ' ))\n",
        "print(f'A soma vale {n1+n2}')"
      ],
      "metadata": {
        "id": "S5y-FCZYdcIT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Conversão de valores em dólar\n",
        "\n",
        "d = float(input('Digite o valor que você tem na carteria: '))\n",
        "c = d/5.07\n",
        "print(f'O valor de {d} Reais equivale a {c:.2f} dólares')"
      ],
      "metadata": {
        "id": "884aqXEPBNxF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Calcular desconto de x% do valor de um produto\n",
        "n = input('Digite seu nome para acessar o sistema: ')\n",
        "print(f'Seja bem vido {n} ao sistema de cáculos de descontos')\n",
        "v = float(input('Digite o valor do produto: '))\n",
        "d = float(input('Digite o valor do desconto: '))\n",
        "c = v - (v * d / 100)\n",
        "print(f'O valor final com o Desconto de {d:.0f}% é de R${c:.2f}')"
      ],
      "metadata": {
        "id": "sqGLri-Plo38"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Calcular a área de uma parede retangular e a quantidade de tinta a ser usada\n",
        "# 1 litro de tinta pinta 2m² de parede\n",
        "# Área - Base(b) x Altura(h)\n",
        "n = input('Digite seu nome ')\n",
        "print(f'Seja Bem vindo {n} ao sistema de cácluo de pintura de área construída')\n",
        "b = float(input('Digite o valor da Base em metros: ' ))\n",
        "h = float(input('Digite o valor da altura em metros: ' ))\n",
        "a = (b*h)\n",
        "t = (a / 2)\n",
        "print(f'A área tem {a} m² e a quantidade de tinta nescessária para pintar é de {t} Litros de tinta')"
      ],
      "metadata": {
        "id": "Mv8zfPK5GTX6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Teste de ocultar senha\n",
        "import getpass\n",
        "s = getpass.getpass(prompt='Digite sua senha ')\n",
        "s2 = \"123\"\n",
        "\n",
        "if s == s2:\n",
        "    print('Seja Bem vindo ao sistema')\n",
        "\n",
        "else:\n",
        "    print('Senha inválida!')"
      ],
      "metadata": {
        "id": "UeOXKxFfnsfK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Ler salário e mostre o novo salário com 15% de aumento\n",
        "n = input('Digite seu nome: ')\n",
        "print(f'Seja bem vindo {n} ao sistema de cálculo de salários')\n",
        "print('Este sistema irá calcular o aumento salarial de 15% sobre o salário informado')\n",
        "s = float(input('Informe o valor do salário: '))\n",
        "c = (s * 0.15)+s\n",
        "p = c-s\n",
        "print(f'O salário de R${s:.2f} com aumento de 15% é de R${c:.2f} o valor do aumento foi de R$: {p:.2f}')\n"
      ],
      "metadata": {
        "id": "-zVgTejoFRdr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Sucessor e antecessor de um número digitado\n",
        "n = int(input('Digite um número: '))\n",
        "print(f'O sucessor do número {n} é: {n+1}, é seu antecessor é: {n-1}')"
      ],
      "metadata": {
        "id": "fbSSh6e3K-XR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.\n",
        "import math\n",
        "n = int(input('Digite um número e vamos calulcar seu dobro, triplo e raiz quadrada: '))\n",
        "d = n*2\n",
        "t = n*3\n",
        "r = math.sqrt(n)\n",
        "l = n**(1/2)\n",
        "print(f'O dobro do número {n} é: {d}\\n ---- O triplo de {n} é: {t}\\n ---- A raiz quadrada de {n} é: {r}')\n",
        "print(l)"
      ],
      "metadata": {
        "id": "K1nTRN9SMHlx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.\n",
        "import getpass\n",
        "n = input('Digite seu nome: ')\n",
        "s2 = \"123\"\n",
        "\n",
        "while True:\n",
        "    s = getpass.getpass(prompt='Digite sua senha: ')\n",
        "    if s == s2:\n",
        "        print(f'Seja bem vindo {n} ao sistema de notas e médias acadêmicas')\n",
        "        break\n",
        "    else:\n",
        "        print('Senha inválida, tente novamente.')\n",
        "\n",
        "while True:\n",
        "    op = int(input('Digite 1 para sair ou 2 para um novo aluno: '))\n",
        "\n",
        "    if op == 1:\n",
        "        print('Obrigado por utilizar nosso sistema, até logo!')\n",
        "        break\n",
        "\n",
        "    elif op == 2:\n",
        "        a = input('Digite o nome do aluno: ')\n",
        "        nota1 = float(input(f'Digite a primeira nota do Aluno {a}: '))\n",
        "        nota2 = float(input(f'Digite a segunda nota do aluno {a}: '))\n",
        "        media = (nota1 + nota2) / 2\n",
        "\n",
        "        if media >= 7:\n",
        "            print(f'O aluno {a} foi aprovado com Média {media}')\n",
        "        else:\n",
        "            print(f'O aluno {a} foi reprovado com média {media}')"
      ],
      "metadata": {
        "id": "lJlv1MqNPLrr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Programa de conversão de metros para CM e MM\n",
        "\n",
        "me = int(input('Digite o valor em metros: '))\n",
        "cm = me*100 \n",
        "mm = me*1000\n",
        "print(f'O valor de {me} metros equivale a: {cm} Centímetros e {mm} Milímetros')\n"
      ],
      "metadata": {
        "id": "EUVG-xbMZeEH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Tabuada de um número digitado\n",
        "print('Bem vindo a tabuada de um número digitado')\n",
        "n = int(input('Digite um número: '))\n",
        "print(f'{n} x {1} = {n*1}')\n",
        "print(f'{n} x {2} = {n*2}')\n",
        "print(f'{n} x {3} = {n*3}')\n",
        "print(f'{n} x {4} = {n*4}')\n",
        "print(f'{n} x {5} = {n*5}')\n",
        "print(f'{n} x {6} = {n*6}')\n",
        "print(f'{n} x {7} = {n*7}')\n",
        "print(f'{n} x {8} = {n*8}')\n",
        "print(f'{n} x {9} = {n*9}')\n",
        "print(f'{n} x {10} = {n*10}')"
      ],
      "metadata": {
        "id": "ldM09OBobYP2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print('Bem vindo a tabuada de um número digitado')\n",
        "n = int(input('Digite um número: '))\n",
        "for i in range(1, 11):\n",
        "    print(f'{n} x {i} = {n*i}')"
      ],
      "metadata": {
        "id": "Z8_xN1UMwfJJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Convertendo temperatura\n",
        "\n",
        "t = float(input('Digite a temperatura em Celsius: '))\n",
        "f1 = (1.8 * t) + 32\n",
        "print(f'Converter {t}°C para a escala Fahrenheit : {f1}°')\n"
      ],
      "metadata": {
        "id": "CQNSdQ7HNwQP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Escreva um programa que pergunte a quantidade de Km percorridos por \n",
        "#um carro alugado e a quantidade de dias pelos quais ele foi alugado.\n",
        "#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.\n",
        "\n",
        "print('Seja bem vido ao Locacar')\n",
        "d = 60\n",
        "d2 = int(input('Informe a quantidade de dias de locação: '))\n",
        "km = float(input('Informe a kilometragem final: '))\n",
        "cpkm = km * 0.15\n",
        "cd = d * d2\n",
        "cf = cd+cpkm\n",
        "print(f' O custo das diárias de {d2} dias foram de R${cd:.2f}\\n o custo da kilomêtragem de {km} KM foi de R${cpkm:.2f}\\n o valor final a ser pago pelo aluguel do veículo é de R$ {cf:.2f}')\n",
        "\n"
      ],
      "metadata": {
        "id": "vz_HUvGVsVBH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "MÓDULO 2\n"
      ],
      "metadata": {
        "id": "FvUwHZoIxPtJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install emoji\n",
        "import emoji\n",
        "print(emoji.emojize(\"Olá mundo :sunglasses: \"))"
      ],
      "metadata": {
        "id": "d14LXRHFxTdq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from math import trunc\n",
        "n = float(input('Digite um numero qualquer: '))\n",
        "print(f' A porção inteira do número digitado {n} é: {trunc(n)}')"
      ],
      "metadata": {
        "id": "6AdqIN3f6lA4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from math import hypot\n",
        "copo = int(input('Digite o valor do cateto oposto: '))\n",
        "cadj = int(input('Digite o valor do cateto adjacente: '))\n",
        "\n",
        "hip = hypot(copo,cadj)\n",
        "\n",
        "print(f'O valor da Hipotenusa é: {hip}')\n",
        "\n"
      ],
      "metadata": {
        "id": "-6Ddn5aEQRqx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from  math import sin,cos,tan,radians\n",
        "\n",
        "a = int(input('Digite o valor do ângulo: '))\n",
        "\n",
        "r = math.radians(a)\n",
        "cosseno = math.cos(r)\n",
        "seno = math.sin(r)\n",
        "tangente = math.tan(r)\n",
        "\n",
        "print(f'O valor do seno é {sin(r)} do cosseno é {cos(r)} e da tangente é {tan(r)} o ângulo em radianos é de {r}')\n",
        "\n"
      ],
      "metadata": {
        "id": "cSFcUiHwSOSf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from random import choice\n",
        "nome = input('Digite o Primeiro nome: ')\n",
        "nome2 = input('Digite o segundo nome: ')\n",
        "nome3 = input('Digite o terceiro nome: ')\n",
        "nome4 = input('Digite o quarto nome: ')\n",
        "lista = [nome, nome2, nome3, nome4]\n",
        "escolhido = choice(lista)\n",
        "print(f'O aluno escolhido é: {escolhido}')"
      ],
      "metadata": {
        "id": "2BUr5iaGV_yf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "nome = input('Digite o Primeiro nome: ')\n",
        "nome2 = input('Digite o segundo nome: ')\n",
        "nome3 = input('Digite o terceiro nome: ')\n",
        "nome4 = input('Digite o quarto nome: ')\n",
        "lista = [nome, nome2, nome3, nome4]\n",
        "random.shuffle(lista)\n",
        "print(f'A ordem de apresentação será: {lista}')\n",
        "\n"
      ],
      "metadata": {
        "id": "qzZ6TG7_QOnv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "nomes = []\n",
        "\n",
        "print(\"Digite 4 nomes separados por enter: \")\n",
        "\n",
        "for i in range(4):\n",
        "    nome = input()\n",
        "    nomes.append(nome)\n",
        "\n",
        "aluno = random.choice(nomes)\n",
        "\n",
        "print(f'O nome é: {aluno}')\n",
        "\n"
      ],
      "metadata": {
        "id": "VJp0D2W0XRYD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "nomes = ['Davi','Pedro','Raissa','Claudia','Silvia','Amanda','Fabiana']\n",
        "sorteados = random.sample(nomes, 7)\n",
        "for i , nome in enumerate(sorteados):\n",
        "  print(f'{i + 1}º nome sorteado: {nome}')\n"
      ],
      "metadata": {
        "id": "GBfEmtEf-MMu"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install pygame\n",
        "import pygame\n",
        "pygame.init()\n",
        "pygame.mixer.init()\n",
        "pygame.mixer.music.load(\"/content/drive/MyDrive/Contas/teste.mp3\")\n",
        "pygame.mixer.music.play()\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "7vj_wGNWS-Wf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "\n",
        "url = \"https://justa-falta.vercel.app/#\"\n",
        "payload = {\"q\": \"' OR (SELECT COUNT(*) FROM all_tables) > 1 --\"}\n",
        "\n",
        "response = requests.get(url, params=payload)\n",
        "\n",
        "if \"error\" not in response.text:\n",
        "    print(\"SQL Injection vulnerability detected!\")\n",
        "else:\n",
        "    print(\"No SQL Injection vulnerability detected.\")"
      ],
      "metadata": {
        "id": "Gao-uJ7fL20n",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1a25249c-4ae6-4f48-d9d3-e681a231e680"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "SQL Injection vulnerability detected!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "AULA 09 - Manipulando Textos"
      ],
      "metadata": {
        "id": "dsu5naaMJz5p"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#manipulando texto\n",
        "\n",
        "frase = ('CURSO EM VIDEO PYTHON')# variavel frase recebendo valor (\"\")\n",
        "frase2 = ('CURSO EM VIDEO PYTHON')# variavel frase recebendo valor (\"\")\n",
        "\n",
        "nova_frase = frase.replace('VIDEO','XUXA ')#Substituindo uma string da frase por outra metodo replace\n",
        "\n",
        "#palavra_antiga = input(f'Digite a palavra antiga que voce quer substiruir na frase {frase}: ')\n",
        "#palavra_nova = input(f'Digite agora a palavra nova que sera inserida no lugar da palavara digita {palavra_antiga}: ')\n",
        "#frase3 = frase.replace(palavra_antiga, palavra_nova)\n",
        "\n",
        "\n",
        "\n",
        "frase_maiuscula = frase2.upper()#converte tudo para maisculo\n",
        "\n",
        "frase_minuscula = frase.lower()#capitalize(): esse método converte a primeira letra da string para maiúscula e as demais para minúsculas.\n",
        "\n",
        "frase_primeira_letra = frase.capitalize()\n",
        "\n",
        "contador = len(frase) #len () faz a contagem de todas as strings da frase\n",
        "\n",
        "a = frase.count('o') #count() faz a contagem de um determinado numero de vezes que um caracter ou palavra se repete\n",
        "\n",
        "indice = frase.find('em')#étodo de string que retorna o índice da primeira ocorrência de uma sub-string em uma string\n",
        "\n",
        "frasse_Title = frase.title()#title(): esse método converte a primeira letra de cada palavra da string para maiúscula e as demais para minúsculas.\n",
        "\n",
        "dividido = frase.split()\n",
        "\n",
        "#print(frase3)\n",
        "#print(frase[3])\n",
        "#\n",
        "print(frase.find('VIDEO'))\n",
        "print(dividido)\n",
        "print(dividido[3])\n",
        "#print(frasse_Title)\n",
        "#print(frase_primeira_letra)\n",
        "#print(frase_minuscula)\n",
        "#print(frase_maiuscula)\n",
        "#print(nova_frase)\n",
        "#print(indice)#indice da primeira ocorrência de uma sub-string em uma string\n",
        "#print(a)# imprime o numero de ocorrencias de um caracter string ou palavras\n",
        "#print(contador)# imprime o numero total de caracteres de uma string\n",
        "#print(frase[5:21])# começa do indice 5 e vai até o indice 21\n",
        "#print(frase[9:21:2])# começa a ler do indice 9 ao 21(esclui o 21)pulando 2 casas por vez\n",
        "#print(frase[:21])# ler do indice 0 até onde foi informado, neste caso 21 ele imprime a frase toda pois ela tem 21 indices"
      ],
      "metadata": {
        "id": "_WqkuvD9J6Bi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install phonenumbers\n",
        "import phonenumbers\n",
        "from phonenumbers import geocoder\n",
        "\n",
        "fone = phonenumbers.parse('+5541999590192')\n",
        "print('\\nLocalização\\n')\n",
        "print(geocoder.description_for_number(fone, 'PT'));\n"
      ],
      "metadata": {
        "id": "w6U7XYrlKCdy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import tkinter as tk\n",
        "from tkinter import messagebox\n",
        "\n",
        "root = tk.Tk()\n",
        "root.withdraw()\n",
        "\n",
        "result = messagebox.askquestion(\"Question\", \"Do you want to continue?\")\n",
        "\n",
        "if result == 'yes':\n",
        "    print(\"User wants to continue\")\n",
        "else:\n",
        "    print(\"User does not want to continue\")"
      ],
      "metadata": {
        "id": "9HxF3s3DgLPs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:\n",
        "\n",
        "#– O nome com todas as letras maiúsculas e minúsculas.\n",
        "\n",
        "#– Quantas letras ao todo (sem considerar espaços).\n",
        "\n",
        "#– Quantas letras tem o primeiro nome.\n",
        "\n",
        "\n",
        "\n",
        "nome = str(input('Digite seu nome e sobrenome: ')).strip()\n",
        "\n",
        "nome1 = nome.split()[0]\n",
        "contnome1 = len(nome1)\n",
        "print(f'O seu primero nome é: \"{nome1}\" , e contém {contnome1} letras')\n",
        "\n",
        "print(f'Seu nome em maisculo é: {nome.upper()}')\n",
        "print(f'Seu nome em minusculo é:{nome.lower()}')\n",
        "espaço = nome.replace(\" \", \"\")\n",
        "cont = len(espaço)\n",
        "print(f'Seu nome todo tem {cont} letras')\n"
      ],
      "metadata": {
        "id": "SJe4GhbwoXJN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.\n",
        "\n",
        "\n",
        "\n",
        "n = int(input('Digite um número de 0 a 9999: '))\n",
        "unidade = n % 10\n",
        "dezena = (n // 10) % 10\n",
        "centena = (n // 100 ) % 10\n",
        "milhar =  (n // 1000) % 10\n",
        "print(f'unidade {unidade}\\ndezena {dezena}\\ncentena {centena}\\nmilhar {milhar}\\n')"
      ],
      "metadata": {
        "id": "h3BMM4O1szzu"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome \"SANTO\".\n",
        "\n",
        "cidade = str(input('Digite o nome da cidade: ')).upper()\n",
        "if cidade.split()[0] == 'SANTO':\n",
        "  print('A cidade começa com o nome SANTO ')\n",
        "else:\n",
        "   print('A cidade não começa com o nome SANTO') \n",
        "\n"
      ],
      "metadata": {
        "id": "iBDdILJ5u7SN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.\n",
        "\n",
        "c = str(input('Digite o nome da sua cidade: ')).strip()\n",
        "v = c.split()[0].upper() == 'SANTO'\n",
        "print(f'A cidade digitada {c}\\n e para santo {v}')\n"
      ],
      "metadata": {
        "id": "nsG9iRQ1qn0V"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "cidade = input(\"Digite o nome da cidade: \")\n",
        "\n",
        "if cidade.upper().startswith(\"SANTO\"):\n",
        "    print(\"O nome da cidade começa com SANTO\")\n",
        "else:\n",
        "    print(\"O nome da cidade não começa com SANTO\")"
      ],
      "metadata": {
        "id": "kc2dBy5IwtIc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem \"SILVA\" no nome.\n",
        "\n",
        "name = str(input('Digite seu nome completo: ')).upper()\n",
        "\n",
        "if name.find('SILVA') != -1:\n",
        "  print(f'O nome {name} tem SILVA')\n",
        "else:\n",
        "  print(f'O nome {name} não tem SILVA') "
      ],
      "metadata": {
        "id": "LSp19bUFzgiz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem \"SILVA\" no nome.\n",
        "\n",
        "name = str(input('Digite seu nome completo: ')).upper()\n",
        "\n",
        "if 'SILVA' in name:\n",
        "  print(f'O nome {name} tem SILVA')\n",
        "else:\n",
        "  print(f'O nome {name} não tem SILVA') "
      ],
      "metadata": {
        "id": "AvdYdZTc1x_U"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "n = str(input(\"Digite seu nome completo: \")).strip()\n",
        "print(f'Existe \"Silva\" no seu nome? { \"SILVA\" in n.upper() }')"
      ],
      "metadata": {
        "id": "nBAK7i4vtkhY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#026: Faça um programa que leia uma frase pelo teclado e mostre quantas \n",
        "#vezes aparece a letra \"A\", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.\n",
        "palavra = str(input('Digite uma frase: ')).upper()\n",
        "\n",
        "rep = palavra.count('A')\n",
        "primeira = palavra.find('A')\n",
        "ultima = palavra.rfind('A')\n",
        "\n",
        "print(f'A frase {palavra} tem a letra \"A\" {rep} vezes\\n a primeira posição é em {primeira}\\n e a ultima posição é em {ultima}\\n')\n"
      ],
      "metadata": {
        "id": "6QWeFDft2EFK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.\n",
        "nome_completo = str(input('Digite seu nome completo: '))\n",
        "lista = nome_completo.split()\n",
        "\n",
        "primeiro_nome = lista[0]\n",
        "\n",
        "ultimo_nome = lista[-1]\n",
        "\n",
        "print(f'O primeiro nome de {nome_completo}\\n é {primeiro_nome}\\n e o último nome é {ultimo_nome}\\n ')\n"
      ],
      "metadata": {
        "id": "YwEWimoT3gD7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "MÓDULO 10"
      ],
      "metadata": {
        "id": "2DoTTwxzwf4j"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "n = str(input('Digite seu nome: ')).upper()\n",
        "if n == 'DAVI':\n",
        "  print(f'Seja bem vindo {n}')\n",
        "else:\n",
        "  print('Usuario não autorizado')  \n",
        "print('Sessão Finalizada')  "
      ],
      "metadata": {
        "id": "8j2ThXNHwjr9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print('Seja Bem vindo digite seu nome e senha')\n",
        "n = str(input('Digite seu nome: ')).upper()\n",
        "s = int(input('Digite sua senha: '))\n",
        "if n == 'DAVI' and s == 123:\n",
        "    print('Seja bem vindo ao sistema de notas')\n",
        "    nota1 = float(input('Digite a primeira nota: '))\n",
        "    nota2 = float(input('Digite a segunda nota: '))\n",
        "    media = (nota1+nota2)/2\n",
        "    if media >= 6.0:\n",
        "      print(f'Parabéns aluno aprovado com média {media}')\n",
        "    else:\n",
        "        print('Aluno em recuperação')\n",
        "else:\n",
        "  print('Usuário não registrado e senha inválida')\n",
        "print('FIM DO PROGRAMA')          \n"
      ],
      "metadata": {
        "id": "cWALQ9g_yV4j"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#exercício 28 gerar um numero aleatorio e verificar se o numero digitado e o correto\n",
        "import random\n",
        "from time import sleep\n",
        "print('- \\u2620 -'*20)\n",
        "print('Pensei em um número: ? ')\n",
        "print('- \\u2620 -'*20)\n",
        "sorteio = random.randint(0,5)\n",
        "n = int(input('Digite um numero entre 0 e 5 e veja se voce advinhou o numero que pensei: '))\n",
        "print('Processando...')\n",
        "sleep(4)\n",
        "if n == sorteio:\n",
        "  print('Parabéns você acertou \\U0001F973!!')\n",
        "else:\n",
        "  print(f'Não foi dessa vez ótario {sorteio} \\U0001F921!')  \n"
      ],
      "metadata": {
        "id": "LCYdw2A31dS6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#29 Radar eletrônico\n",
        "print('Qual a velocidade atual do seu veículo: ')\n",
        "v = int(input('Digite a velocidade atual: '))\n",
        "multa = (v - 80)*7\n",
        "vat = v - 80\n",
        "\n",
        "if v > 80:\n",
        "   print(f'A sua velocidade de {v}Km/h você esta acima do limite de velocidadee em {vat}km/h \\U0001F480 e isso gerou uma multa de R${multa:.2f} \\U0001F973!! ')\n",
        "   \n",
        "else:\n",
        "  print('Você está no limite correto de velocidade da via' )  "
      ],
      "metadata": {
        "id": "vPLwPZtl7c0r"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 30 par ou ímpar\n",
        "\n",
        "p = int(input('Digite um número inteiro: '))\n",
        "\n",
        "if p % 2 == 0 :\n",
        "  print('O numero é PAR')\n",
        "\n",
        "else:\n",
        "  print('O número e ímpar')  \n"
      ],
      "metadata": {
        "id": "V_qZR4kG6vta"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#31\n",
        "#custo da passagem da viajem\n",
        "\n",
        "km = float(input('Digite a distancia em KM da viajem: '))\n",
        "\n",
        "if km <= 200:\n",
        "  custo = km * 0.50\n",
        "else:\n",
        "   custo = km * 0.45 \n",
        "   \n",
        "print(f'O valor da passagem de {km}Km é de R${custo}')\n",
        "\n"
      ],
      "metadata": {
        "id": "hUJJEFGX_ccw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#32 Verificar se o ano e Bissexto\n",
        "from datetime import date\n",
        "ano = int(input('Digite o ano:   ou 0 para verificar o ano atual'))\n",
        "\n",
        "if ano == 0:\n",
        "  ano = date.today().year\n",
        "\n",
        "if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):\n",
        "  print(f'O ano {ano} é Bissexto')\n",
        "\n",
        "else:\n",
        "  print(f'O ano {ano} não é Bissexto')  \n"
      ],
      "metadata": {
        "id": "ZF90bYZlCR16",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "af746108-06ef-4547-8b73-3f0e64077f46"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o ano:   ou 0 para verificar o ano atual2023\n",
            "O ano 2023 não é Bissexto\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 33 maior ou menor número dentre 3\n",
        "\n",
        "n1 = int(input('Digite um número: '))\n",
        "n2 = int(input('Digite número 2: '))\n",
        "n3 = int(input('Digite o número 3: '))\n",
        "\n",
        "if n1 > n2 and n1 > n3:\n",
        "  print(f'O numero {n1} é maior')\n",
        "  \n",
        "elif n2 > n1 and n2 > n3:\n",
        "  print(f'O número {n2} é maior')\n",
        "\n",
        "else:\n",
        "  print(f'O numero {n3} é maior')\n",
        "\n",
        "if n1 < n2 and n1 < n3:\n",
        "  print(f'O número {n1} é menor')\n",
        "\n",
        "elif n2 < n1 and n2 < n3:\n",
        "   print(f'O número {n2} é menor') \n",
        "\n",
        "else:\n",
        "  print(f'O número {n3} é menor')       "
      ],
      "metadata": {
        "id": "PZOBYI9mElU5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 34 cálculo de sálario\n",
        "\n",
        "print('m =====Bem vindo ao sistema de Cálculo de salário=====')\n",
        "\n",
        "s = float(input('Digite o valor atual do salário do funcionário R$'))\n",
        "\n",
        "if s <= 1250.00:\n",
        "  ns = s + ((s*15)/100)\n",
        "else:\n",
        "  ns = s + ((s*10 )/ 100)  \n",
        "print(f'O novo salário é de R${ns}')"
      ],
      "metadata": {
        "id": "SvjCWcwqIf5B"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#35 formando um triângulo\n",
        "!pip install colorama\n",
        "import matplotlib.pyplot as plt\n",
        "from time import sleep\n",
        "import colorama\n",
        "from colorama import Fore\n",
        "\n",
        "a = float(input('Digite uma valor para a primeira reta : '))\n",
        "b = float(input('Digite uma valor para a segunda reta : '))\n",
        "c = float(input('Digite uma valor para a terceira reta : '))\n",
        "\n",
        "if a < b + c and b < a + c and c < a + b:\n",
        "  # Calcula as coordenadas dos três vértices do triângulo\n",
        "  x1, y1 = 0, 0\n",
        "  x2, y2 = c, 0\n",
        "  x3 = (a**2 - b**2 + c**2) / (2 * c)\n",
        "  y3 = (a**2 - x3**2)**0.5\n",
        "\n",
        "  # Plota o triângulo\n",
        "  plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1])\n",
        "\n",
        "\n",
        "  print('Processando...')\n",
        "  sleep(2)\n",
        "\n",
        "  #if a == b == c:\n",
        "   #print('Triângulo equilátero')\n",
        "   #print('Processando...')\n",
        "   #sleep(2)\n",
        "   #plt.show()\n",
        "\n",
        "  #elif a == b and a != c or a == c and a != b or b == c and b != a:\n",
        "  # print('Triângulo isosceles')  \n",
        "  # print('Processando...')\n",
        "  # sleep(2)\n",
        "  # plt.show()\n",
        "\n",
        "  #else:\n",
        "  # print('Triangulo escaleno')\n",
        "  # print('Processando...')\n",
        "  # sleep(2)\n",
        "  # plt.show()  \n",
        "\n",
        "  print('Podemos formar um triangulo ')\n",
        "  plt.show()\n",
        "\n",
        "else:\n",
        " print(Fore.RED + 'Não é possivel fazer um \\u25B2' + Fore.RESET)"
      ],
      "metadata": {
        "id": "j2063oSeLj4e"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "MUNDO 2 Aulas em vídeo"
      ],
      "metadata": {
        "id": "2mSIm-ww94eu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#36 - Calculando emprestimo de uma casa\n",
        "casa = float(input('Digite o valor do imovél R$ '))\n",
        "tempo = int(input('Digite o numeros de parcelas em meses: '))\n",
        "salario = float(input('Digite o valor do seu salário R$ '))\n",
        "\n",
        "prestação = casa / tempo\n",
        "\n",
        "salario_novo = salario * 0.3\n",
        "\n",
        "if prestação <= salario_novo:\n",
        "   print('emprestimo aceito') \n",
        "\n",
        "   print(f'O Valor das Parcelas a serem pagas em {tempo} Meses é de R${prestação:.2f} ao Mês')\n",
        "\n",
        "\n",
        "else:\n",
        "  print(f'Empréstimo negado o valor da presção R${prestação:.2f} excede o valor de 30% do seu salário')\n",
        "  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NykjDOIV98fI",
        "outputId": "79bb20e9-39e7-40cd-e0ae-51ce46705c0a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o valor do imovél R$ 150000\n",
            "Digite o numeros de parcelas em meses: 60\n",
            "Digite o valor do seu salário R$ 12000\n",
            "emprestimo aceito\n",
            "O Valor das Parcelas a serem pagas em 60 Meses é de R$2500.00 ao Mês\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "casa = float(input('\\033[35mQual o valor da casa\\033[m? '))\n",
        "salário = float(input('\\033[36mQual é o seu salário\\033[m? '))\n",
        "anos = float(input('\\033[32mEm quantos anos você vai pagar\\033[m? '))\n",
        "prestação = casa / (anos * 12)\n",
        "\n",
        "print('-=-' * 20)\n",
        "if salário * 0.30 >= prestação:\n",
        "    print('\\033[4mParabéns, seu financiamento foi aprovado\\033[m!!!')\n",
        "else:\n",
        "    print('\\033[4mDesculpe, mas seu financiamento foi negado\\033[m')"
      ],
      "metadata": {
        "id": "w4VTUIFUYwQL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#37 - Transforme um numero em binario, octal e hexadecimal\n",
        "\n",
        "n = int(input('\\033[33m Digite um número inteiro: ' ))\n",
        "\n",
        "opção = int(input('''\\033[34m\n",
        "[1] para binário \n",
        "[2] para octal \n",
        "[3] para hexadecimal \\n'''))\n",
        "\n",
        "if opção == 1 :\n",
        "  binario = bin(n)\n",
        "  print(f'\\033[33m O numero {n} em Binario é {binario[2:]}')\n",
        "elif opção == 2: \n",
        "  octal = oct(n)\n",
        "  print(f'\\033[33m O número {n} em octal é de {octal[2:]}')\n",
        "elif opção == 3:\n",
        "  hexa = hex(n)\n",
        "  print(f'\\033[33m O número {n} em hexadecimal é de {hexa[2:]}')\n",
        "\n",
        "else:\n",
        "   print('Número inválido!') \n"
      ],
      "metadata": {
        "id": "P2H64jWJdn6T",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3fb3366b-b719-4367-b75f-a6cce3bc3fdd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[33m Digite um número inteiro: 22\n",
            "\u001b[34m\n",
            "[1] para binário \n",
            "[2] para octal \n",
            "[3] para hexadecimal \n",
            "3\n",
            "\u001b[33m O número 22 em hexadecimal é de 16\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n1 = int(input('Digite o primeiro numero: '))\n",
        "n2 = int(input('Digite o segundo numero: '))\n",
        "\n",
        "if n1 > n2:\n",
        "  print(f'O primeiro número digitado e Maior')\n",
        "\n",
        "elif n2 > n1:\n",
        "  print('O segundo numero digitado e Maior')  \n",
        "\n",
        "else:\n",
        "  print('Os Numeros são iguais ')\n"
      ],
      "metadata": {
        "id": "aBrXZ06SogOR",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "663cd3c4-7059-4f59-925d-5b41a1159bc9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o primeiro numero: 2\n",
            "Digite o segundo numero: 2\n",
            "Os Numeros são iguais \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "from datetime import date #importando a biblioteca datatime\n",
        "\n",
        "#lendo o ano de nascimento do usuario\n",
        "ano_nascimento = int(input('Digite seu ano de nascimento com 4 digitos: '))\n",
        "\n",
        "#selecionando o ano atual\n",
        "ano_atual = date.today().year\n",
        "\n",
        "#calculando a idade da pessoa\n",
        "idade = ano_atual - ano_nascimento\n",
        "\n",
        "#verificando a data digitada\n",
        "if ano_nascimento <= 1900:\n",
        "  print(f'Data {ano_nascimento} inválida')\n",
        "else:  \n",
        "#verificando se a idade e maior de 18 anos e quanto anos passaram do alistamento\n",
        " if idade > 18:\n",
        "  exc = idade - 18 #calculando anos que passaram para se alistar\n",
        "\n",
        "  ano_alistamento = ano_atual - exc #calculando o ano de alistamento\n",
        "\n",
        "  print(f'Você excedeu o limite de alistamento em {exc} anos, seu alistamento foi em {ano_alistamento}')\n",
        "\n",
        "# verificando se a idade e menor de 18 anos e informando os anos que faltam par se alistar  \n",
        " elif idade < 18:\n",
        "\n",
        "  exc = 18 - idade #calculando anos que faltam para se alistar\n",
        "\n",
        "  ano_alistamento = ano_atual + exc #calculando o ano de alistamento\n",
        "\n",
        "  print(f'Voce ainda esta fora do prazo de alistamento sua idade é de {idade} anos, ainda faltam {exc} anos, seu alistamento é em {ano_alistamento}')\n",
        "\n",
        "# se a idade for igual a 18 anos informa que deve se alisatar \n",
        " else:\n",
        "  print('Você está no prazo de alistamento, procure uma unidade militar mais próxima e evite penalidades!')  \n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "XL_rC1Vrjva3",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1728cfbe-1cd0-4c02-8899-fca69ed8eb0a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite seu ano de nascimento com 4 digitos: 1975\n",
            "Você excedeu o limite de alistamento em 30 anos, seu alistamento foi em 1993\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#40 calcue a média e mostre aprovado, em recuperação e reprovado\n",
        "\n",
        "mes = '\\033[36mCácluo de Média do aluno'\n",
        "larg = 130\n",
        "print('\\033[1;33;42m=-=' * 20 + 'Bem vindo' + '=-=' * 20 + '\\033[0m')\n",
        "print(mes.center(larg))\n",
        "print('\\033[33;42m' + '=-=' * 20 + '=-=' * 23 + '\\033[0m')\n",
        "\n",
        "nota1 = float(input('Digite a primeira nota do Aluno: \\n'))\n",
        "\n",
        "nota2 = float(input('Digite a  segunda nota do Aluno: \\n'))\n",
        "\n",
        "media = (nota1 + nota2) / 2\n",
        "\n",
        "if media >= 7.0:\n",
        "  print(f'\\033[32mAluno aprovado! com média  {media:.2f}')\n",
        "\n",
        "elif media >= 5.0 and media <= 6.9:\n",
        "  print(f'\\033[33mAluno está em recuperação com média  {media:.2f}')\n",
        "\n",
        "else:\n",
        "  print(f'\\033[31mAluno está reprovado! com média  {media:.2f}')  \n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "-bEC-74pTbvk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#41 ler uma data de nascimento e mostrar a categoria dela de acordo com a idade\n",
        "\n",
        "#importando a biblioteca datetime para calcular a idade aatual\n",
        "import datetime\n",
        "\n",
        "#Inserindo o nome da pessoas a ser analisado\n",
        "nome = str(input('Digite o nome da Pessoa: '))\n",
        "\n",
        "#pegando a data de nascimeto da pessoa\n",
        "nascimento = int(input('Digite seu ano de Nascimento com 4 dígitos: '))\n",
        "\n",
        "#verificando a idade atual da pessoa\n",
        "idade = date.today().year - nascimento\n",
        "\n",
        "#Fazendo a verificação das categorias de acordo com a idade\n",
        "\n",
        "if idade <= 9 :\n",
        "  print(f'{nome} você pertence a categoria MIRIM'),\n",
        "\n",
        "elif idade > 9 and idade <= 14:\n",
        "  print(f'{nome} Você pertence a categoria INFANTIL')  \n",
        "\n",
        "elif idade > 14 and idade <= 19:\n",
        "  print(f'{nome} você pertence a categoria JÚNIOR') \n",
        "\n",
        "elif idade == 20:\n",
        "  print(f'{nome} Você pertence a categoria SÊNIOR')\n",
        "\n",
        "else:\n",
        "  print(f'{nome} você pertence a categoria MASTER')\n",
        "\n",
        "                 ##FIM##"
      ],
      "metadata": {
        "id": "_1rnd1HUuwtf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#42 Verificando se é possivel construir um triângulo e se for qual seria o triângulo\n",
        "!pip install colorama\n",
        "import matplotlib.pyplot as plt\n",
        "from time import sleep\n",
        "import colorama\n",
        "from colorama import Fore\n",
        "\n",
        "a = float(input('Digite uma valor para a primeira reta : '))\n",
        "b = float(input('Digite uma valor para a segunda reta : '))\n",
        "c = float(input('Digite uma valor para a terceira reta : '))\n",
        "\n",
        "if a < b + c and b < a + c and c < a + b:\n",
        "  # Calcula as coordenadas dos três vértices do triângulo\n",
        "  x1, y1 = 0, 0\n",
        "  x2, y2 = c, 0\n",
        "  x3 = (a**2 - b**2 + c**2) / (2 * c)\n",
        "  y3 = (a**2 - x3**2)**0.5\n",
        "\n",
        "  # Plota o triângulo\n",
        "  plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1])\n",
        "\n",
        "\n",
        "  print('Processando...')\n",
        "  sleep(2)\n",
        "\n",
        "  if a == b == c:\n",
        "   print('Triângulo equilátero')\n",
        "   print('Processando...')\n",
        "   sleep(2)\n",
        "   plt.show()\n",
        "\n",
        "  elif a == b and a != c or a == c and a != b or b == c and b != a:\n",
        "   print('Triângulo isosceles')  \n",
        "   print('Processando...')\n",
        "   sleep(2)\n",
        "   plt.show()\n",
        "\n",
        "  else:\n",
        "   print('Triangulo escaleno')\n",
        "   print('Processando...')\n",
        "   sleep(2)\n",
        "   plt.show()  \n",
        "\n",
        "#print('Podemos formar um triangulo ')\n",
        "#plt.show()\n",
        "\n",
        "else:\n",
        " print(Fore.RED + 'Não é possivel fazer um \\u25B2' + Fore.RESET)"
      ],
      "metadata": {
        "id": "mngO-ryxL27P"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#43 IMC\n",
        "peso = int(input('Digite seu peso: '))\n",
        "altura = float(input('Digite sua altura: '))\n",
        "alt = pow(altura,2)\n",
        "#mc = peso/alt\n",
        "#print(mc)\n",
        "IMC = peso / alt #(altura * altura)\n",
        "\n",
        "\n",
        "if IMC < 18.5:\n",
        "  print(f'\\033[33mSeu índice de Massa Corporal é de: {IMC:.2f} você está abaixo do Peso Ideal ')\n",
        "\n",
        "elif IMC >= 18.5 and IMC <= 25:\n",
        "  print(f'\\033[34mSeu índice de Massa Corporal é de: {IMC:.2f} você está no Peso Ideal ')\n",
        "\n",
        "elif IMC > 25 and IMC <= 30:\n",
        "  print(f'\\033[35mSeu índice de Massa Corporal é de: {IMC:.2f} você está com sobrePeso ')\n",
        "\n",
        "elif IMC > 30 and IMC <= 40:\n",
        "  print(f'\\033[32mSeu índice de Massa Corporal é de: {IMC:.2f} você está Obeso ') \n",
        "\n",
        "else :\n",
        "  print(f'\\033[33mSeu índice de Massa Corporal é de: {IMC:.2f} você está com obesidade morbida \\U0001F480')\n"
      ],
      "metadata": {
        "id": "IgIQJj_KUXFa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#44 Calculando valor a ser pago\n",
        "\n",
        "valor_normal = float(input('Digite o valor do produto R$'))\n",
        "op = int(input('''Escolha a Forma de Pagamento: \n",
        "[1] Á vista ou Cheque\n",
        "[2] Á vista no cartão\n",
        "[3] Até 2x no cartão\n",
        "[4] 3x ou mais parcelas\\n''' ))\n",
        "\n",
        "if op == 1:\n",
        "  dez = ((valor_normal /100)*10)\n",
        "  desconto = valor_normal - ((valor_normal /100)*10)\n",
        "  print(f'Valor a Pagar R${desconto:.2f}\\no valor do desconto foi de R${dez:.2f}')\n",
        "\n",
        "elif op == 2:\n",
        "    cinco = ((valor_normal /100)*5)\n",
        "    desconto = valor_normal - ((valor_normal /100)*5)\n",
        "    print(f'Valor a Pagar R${desconto:.2f}\\n o valor do desconto foi de R${cinco:.2f}')\n",
        "\n",
        "elif op == 3:\n",
        "    p = valor_normal / 2\n",
        "    print(f'O valor a pagar R${valor_normal:.2f}\\n em 2 parcelas de R${p:.2f}')\n",
        "\n",
        "elif op == 4:\n",
        "  j = valor_normal + (valor_normal *20 / 100)\n",
        "  qtd_parcelas = int(input('Informe o Número de Parcelas a partir de 3x '))\n",
        "  valor_parcelas = j / qtd_parcelas\n",
        "  print(f'O valor a pagar R${j:.2f} com juros em {qtd_parcelas}X de {valor_parcelas:.2f}')\n",
        "\n",
        "else:\n",
        "  print('Opção Inválida!')  "
      ],
      "metadata": {
        "id": "PaOf9DmmcxfZ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b53bf65f-27cb-43b5-e7c4-51bcedeccda6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o valor do produto R$3000\n",
            "Escolha a Forma de Pagamento: \n",
            "[1] Á vista ou Cheque\n",
            "[2] Á vista no cartão\n",
            "[3] Até 2x no cartão\n",
            "[4] 3x ou mais parcelas\n",
            "4\n",
            "Informe o Número de Parcelas a partir de 3x 4\n",
            "O valor a pagar R$3600.00 com juros em 4X de 900.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "from time import sleep\n",
        "opçoes = ['Pedra', 'Papel','Tesoura']\n",
        "\n",
        "op = str(input('''Digite:\n",
        "Pedra\n",
        "Papel\n",
        "Tesoura \\n\\n''')).upper()\n",
        "\n",
        "maquina = random.choice(opçoes).upper()\n",
        "print('-==-'*40)\n",
        "print('JO')\n",
        "sleep(1)\n",
        "print('KEN')\n",
        "sleep(1)\n",
        "print('PO')\n",
        "sleep(1)\n",
        "print('-==-'*40)\n",
        "\n",
        "print(f\"Você escolheu: {op}\")\n",
        "print(f\"O computador escolheu: {maquina}\")\n",
        "print('-==-'*40)\n",
        "if op == 'PEDRA' and maquina == 'TESOURA' or op == 'PAPEL' and maquina == 'PEDRA' or op == 'TESOURA' and maquina == 'PAPEL' :\n",
        "  print('Parabéns você Ganhou')\n",
        "\n",
        "elif op == 'PEDRA' and maquina == 'PAPEL' or op == 'PAPEL' and maquina == 'TESOURA' or op == 'TESOURA' and maquina == 'PEDRA':\n",
        "  print('Infelizmente você Perdeu ')\n",
        "\n",
        "elif op == maquina:\n",
        "  print('Houve um empate!') \n",
        "\n",
        "else:\n",
        "  print('Opção inválida')     \n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sYjzpUo9itIv",
        "outputId": "d9cddca0-7227-4297-c769-debf7d9176be"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite:\n",
            "Pedra\n",
            "Papel\n",
            "Tesoura \n",
            "\n",
            "papel\n",
            "-==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==-\n",
            "JO\n",
            "KEN\n",
            "PO\n",
            "-==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==-\n",
            "Você escolheu: PAPEL\n",
            "O computador escolheu: TESOURA\n",
            "-==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==-\n",
            "Infelizmente você Perdeu \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(0,22,2+2):\n",
        "  print(i)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vY32IiOQrEQf",
        "outputId": "142a0978-553d-4994-f6b4-097a93309fc6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "4\n",
            "8\n",
            "12\n",
            "16\n",
            "20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "from time import sleep\n",
        "\n",
        "print(10*'-==-==','Bem vindo ao jogo de advinhação','-==-=='*10)\n",
        "sleep(2)\n",
        "\n",
        "while True:\n",
        " \n",
        " print('Pensei em número tente advinhar!!!')\n",
        " pc = random.randint(0,10)\n",
        " sleep(2)\n",
        " \n",
        " try:\n",
        "        numero = int(input('Digite um número de 0 a 10: '))\n",
        " except ValueError:\n",
        "        print('Digite apenas números de 0 a 10.')\n",
        "        continue\n",
        "\n",
        " print('Analisando número digitado AGUARDE!')\n",
        " sleep(2)\n",
        "\n",
        " if numero == pc:\n",
        "  print(f'\\033[32mParabéns você venceu! o número que pensei foi {pc}')\n",
        " else:\n",
        "  print(f'\\033[33mvocê perdeu,o número que pensei foi {pc} tente de novo') \n",
        "\n",
        "  op = str(input('Deseja tentar novamente?\\n S - SIM === N - NÃO\\n ')).upper()\n",
        "  if op == 'S' or op == 'SIM':\n",
        "    print('Recomeçando....')\n",
        "    sleep(2)\n",
        "  else:\n",
        "    print('FIM DO JOGO')\n",
        "    break\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "OHOtZLH410Ht"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#46 Faça um programa que mostre na tela uma contagem regressiva \n",
        "#para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.\n",
        "from time import sleep\n",
        "for c in range(10,-1,-1):\n",
        "  print(c)\n",
        "  sleep(1)\n",
        "print('-=-==-= FOGOS ESTOURADOS!!!\\U0001F386 -=-==-=')\n",
        "sleep(1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "swe_-s3Jhoyt",
        "outputId": "710e2b13-ceb9-4e51-854c-5878685cefc3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10\n",
            "9\n",
            "8\n",
            "7\n",
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n",
            "0\n",
            "-=-==-= FOGOS ESTOURADOS!!!🎆 -=-==-=\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#sorteando 6 numeros entre 1 e 60\n",
        "import random\n",
        "from time import sleep\n",
        "lista = []\n",
        "for a in range(6):\n",
        "  n =  random.randint(1, 60) #input('Digite um nome ') #int(input('digite um numero ')) \n",
        "  lista.append(n)\n",
        "for n in  lista: #range(100):\n",
        " #print(n, end=' ') \n",
        " #print(n, end=' ')\n",
        " #print(n)\n",
        " #print(n, end=' ')\n",
        " print(n, end=' ')\n",
        " sleep(1)\n",
        "#s = random.randint(lista)\n",
        "\n"
      ],
      "metadata": {
        "id": "wiY7RF9JkjlE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Testando um print de load\n",
        "from time import sleep\n",
        "for a in range(6):\n",
        "  print('.', end='' )\n",
        "  #print('Parabéns', end= ' ')\n",
        "  sleep(1)\n",
        "  "
      ],
      "metadata": {
        "id": "Fz9SgexCX_wY",
        "outputId": "4daf32b6-da49-4d76-c155-5993d8902b2c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "......"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#47 Mostrar todos os números pares entre 1 e 50\n",
        "from time import sleep\n",
        "for c in range (2,51,2):\n",
        "  sleep(1)\n",
        "  print(c, end = \" - \")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kFa9rO_LJSvY",
        "outputId": "baf5bae7-d052-4c58-d835-a72828a96920"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 - 4 - 6 - 8 - 10 - 12 - 14 - 16 - 18 - 20 - 22 - 24 - 26 - 28 - 30 - 32 - 34 - 36 - 38 - 40 - 42 - 44 - 46 - 48 - 50 - "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#48 Soma de todos os numeros impares entre 1 e 500\n",
        "soma = 0\n",
        "cont = 0\n",
        "for c in range (1,501,2):\n",
        "  #SOMENTE NUMROS ÍMPARES\n",
        "  #if c % 2 !=0:\n",
        "   #print(c, end = \" - \")\n",
        "  if c % 3 ==0:\n",
        "   #print(f'Os números multiplos de 3 são: {c}')\n",
        "   soma +=  c\n",
        "   cont += 1\n",
        "print(f'A soma dos {cont} números multiplos de 3 é de: {soma}')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MD-AWYmqQbil",
        "outputId": "d96ba30b-8925-4101-fdc1-528017cf2ca9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A soma dos 83 números multiplos de 3 é de: 20667\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for c in range(1,501,2):\n",
        "  if c % 3 == 0:\n",
        "     print(c, end = ' ')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HSQ43taGuund",
        "outputId": "f6fa34e1-b7d7-4b6d-d0f8-0404dd485976"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3 9 15 21 27 33 39 45 51 57 63 69 75 81 87 93 99 105 111 117 123 129 135 141 147 153 159 165 171 177 183 189 195 201 207 213 219 225 231 237 243 249 255 261 267 273 279 285 291 297 303 309 315 321 327 333 339 345 351 357 363 369 375 381 387 393 399 405 411 417 423 429 435 441 447 453 459 465 471 477 483 489 495 "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#49\n",
        "print('Bem vindo a tabuada de um número digitado')\n",
        "n = int(input('Digite um número: '))\n",
        "for i in range(1, 11):\n",
        "    print(f'{n} x {i} = {n*i}')"
      ],
      "metadata": {
        "id": "lAok37V_Xp3F"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#50 Desenvolva um programa que leia seis \n",
        "#números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.\n",
        "\n",
        "\n",
        "n = []\n",
        "soma = 0\n",
        "cont = 0\n",
        "print('Digite seis números inteiros: ')\n",
        "for c in range(1,7):\n",
        " n = int(input((f'Digite o {c}º valor: ')))\n",
        " if n %2 == 0 :\n",
        "  soma += n\n",
        "  cont += 1\n",
        "print(f'A soma dos numeros pares é: {soma} e existem {cont} numeros pares')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Lu6O360AYndl",
        "outputId": "91a97814-8d47-436a-8212-18bc92864827"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite seis números inteiros: \n",
            "Digite o 1º valor: 2\n",
            "Digite o 2º valor: 1\n",
            "Digite o 3º valor: 1\n",
            "Digite o 4º valor: 3\n",
            "Digite o 5º valor: 8\n",
            "Digite o 6º valor: 95\n",
            "A soma dos numeros pares é: 10 e existem 2 numero pares\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#51 Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.\n",
        "a1 = int(input('Digite um termo: '))\n",
        "r = int(input('Digite a razão: '))\n",
        "for c in range(1,11):\n",
        "  an = a1 + (c - 1) * r\n",
        "  print(an, end = \" \")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4pBjpB0Zb_lm",
        "outputId": "30a0512f-8932-4554-8510-d8e9e5b05cad"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um termo: 2\n",
            "Digite a razão: 3\n",
            "2 5 8 11 14 17 20 23 26 29 "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#52 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.\n",
        "n = int(input('Digite um numero : '))\n",
        "tot=0\n",
        "for c in range(1,n+1):\n",
        "  if n % c == 0:\n",
        "      print('\\33[34m', end =' ')\n",
        "      tot += 1\n",
        "  else:\n",
        "      print('\\33[33m', end = ' ') \n",
        "  print(f'{c}', end = ' ')    \n",
        "print(f'\\n\\033[m O numero {n} foi divisivel {tot} vezes', end = ' ') \n",
        "\n",
        "if tot == 2:\n",
        "  print('O número é primo')\n",
        "else:\n",
        "  print('O número não é primo')  \n",
        "\n",
        "     \n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xUv5fT_pgGGO",
        "outputId": "c26c25cd-c8b8-4919-b356-1d5f3ce43319"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero : 13\n",
            "\u001b[34m 1 \u001b[33m 2 \u001b[33m 3 \u001b[33m 4 \u001b[33m 5 \u001b[33m 6 \u001b[33m 7 \u001b[33m 8 \u001b[33m 9 \u001b[33m 10 \u001b[33m 11 \u001b[33m 12 \u001b[34m 13 \n",
            "\u001b[m O numero 13 foi divisivel 2 vezes O número é primo\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# versão avançada Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.\n",
        "\n",
        "def is_prime(n):\n",
        "    if n <= 1:\n",
        "        return False\n",
        "    for i in range(2, int(n**0.5)+1):\n",
        "        if n % i == 0:\n",
        "            return False\n",
        "    return True\n",
        "\n",
        "n = int(input('Digite um número: '))\n",
        "if is_prime(n):\n",
        "    print(f\"{n} é primo.\")\n",
        "else:\n",
        "    print(f\"{n} não é primo.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mopwLeP8IIBZ",
        "outputId": "8a950223-c559-4207-e7f5-ee7281e9b327"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: 33\n",
            "33 não é primo.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#53 Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.\n",
        "frase = str(input('Digite uma frase e vamos ver se ela é um PALINDRO: ')).strip().upper()\n",
        "palavra = frase.split()\n",
        "junto = ''.join(palavra)\n",
        "inverso = junto[::-1]\n",
        "#for letra in range (len(junto) - 1, -1, -1):\n",
        " #  inverso += junto[letra]\n",
        "\n",
        "#palavra_reversa = palavra[::-1]\n",
        "if inverso == junto:\n",
        "  print(f'{inverso} é um palindro')\n",
        "else:\n",
        "  print('Não é palindro')  \n",
        "\n"
      ],
      "metadata": {
        "id": "LWuqLLg_ioxN",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "eca49f39-b863-4d4e-f405-872ba8335d91"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite uma frase e vamos ver se ela é um PALINDRO: anotaram a data da maratona\n",
            "ANOTARAMADATADAMARATONA é um palindro\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#54 ler 7 idades e diga quantas já são maiores de idade e quantas não são\n",
        "import datetime\n",
        "from datetime import date\n",
        "nascimento = []\n",
        "tot = 0\n",
        "tot2 = 0\n",
        "for i in range (1,8):\n",
        "  nascimento = int(input(f'Digite o {i}º ano de nascimento: '))\n",
        "  idade = date.today().year - nascimento\n",
        "  if idade >= 21:\n",
        "    tot += 1\n",
        "  else:\n",
        "    tot2 += 1\n",
        "\n",
        "\n",
        "print(f'Temos {tot2} pessoas menores de idade é {tot} pessoas maiores de idade')\n",
        "\n",
        " \n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "niZESxMZkQC0",
        "outputId": "ddb3465a-4106-4708-ecb1-a6cbd565f1ee"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o 1º ano de nascimento: 1980\n",
            "Digite o 2º ano de nascimento: 2020\n",
            "Digite o 3º ano de nascimento: 1970\n",
            "Digite o 4º ano de nascimento: 2016\n",
            "Digite o 5º ano de nascimento: 1969\n",
            "Digite o 6º ano de nascimento: 2023\n",
            "Digite o 7º ano de nascimento: 1985\n",
            "Temos 3 pessoas menores é 4 pessoas maiores\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#55 leia peso de 5 pessoas e diga o maior peso e o menor peso\n",
        "pesos = []\n",
        "cont = 0\n",
        "cont2 = 0\n",
        "for i in range (1,6):\n",
        "  peso = float(input(f'Digite o {i} peso: '))\n",
        "  pesos.append(peso) \n",
        "  menor_peso = min(pesos)\n",
        "  maior_peso = max(pesos)\n",
        "  #if menor_peso < maior_peso:\n",
        "    #cont += 1\n",
        "  #print(_'Menor peso {menor_peso}')\n",
        "  #else:\n",
        "    #cont2 += 1\n",
        "  #print(f'O maior peso é {maior_peso}')  \n",
        "print(f'O menor peso lido foi {menor_peso}Kg e o maior peso lido foi {maior_peso}Kg')  \n",
        "\n",
        " "
      ],
      "metadata": {
        "id": "go9ma9Kuroz1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6aa26ee7-3078-4f00-9cd2-ad5a283d9654"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o 1 peso: 100\n",
            "Digite o 2 peso: 200\n",
            "Digite o 3 peso: 300\n",
            "Digite o 4 peso: 400\n",
            "Digite o 5 peso: 500\n",
            "O menor peso lido foi 100.0Kg e o maior peso lido foi 500.0Kg\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#56 Leia nome idade e sexo de 4 pessoas e mostre a idade media do grupo, o nome do homen mais velho e quantas mulheres tem mais de 20 anos\n",
        "\n",
        "somaidade = 0\n",
        "mediaidade = 0\n",
        "maior_idade_homen = 0\n",
        "nome_do_homen_mais_velho ='Não existe Homens nesta lista '\n",
        "tot20 = 0\n",
        "\n",
        "print('-----= Bem vindo ao cadastro de passageiros =-----\\n')\n",
        "opcao = int(input(' -==-==- Digite quantas pessoas serão cadastradas:   -==-==-  \\n'))\n",
        "\n",
        "\n",
        "\n",
        "for i in range (opcao):\n",
        "\n",
        "   print(f'------{i+1}ª Pessoa------\\n') #coletando os dados\n",
        "\n",
        "   nome = str(input('Nome: ')).strip()\n",
        "   sexo = str(input('Sexo M/F: ')).strip()\n",
        "   idade = int(input('Idade: '))\n",
        "\n",
        "   somaidade += idade #soma todas as idades digitadas\n",
        "\n",
        "   if i == 1 and sexo in 'Mm':\n",
        "      maior_idade_homen = idade\n",
        "      nome_do_homen_mais_velho = nome\n",
        "\n",
        "   elif  sexo in 'Mm' and idade >  maior_idade_homen:\n",
        "      maior_idade_homen = idade\n",
        "      nome_do_homen_mais_velho = nome\n",
        "\n",
        "   elif sexo in 'Ff' and idade < 20:\n",
        "      tot20 += 1    \n",
        "   else:\n",
        "    print('Opção inválida, volte ao menun inicial')\n",
        "  \n",
        "\n",
        "\n",
        "mediaidade = somaidade/opcao\n",
        "\n",
        "print(f'A média de idade do grupo é de : {mediaidade:.2f} anos')\n",
        "print(f'O homen mais velho tem {maior_idade_homen} anos e se chama {nome_do_homen_mais_velho}')\n",
        "print(f'Exitem {tot20} Mulheres menores de 20 anos')\n",
        "\n",
        "\n",
        "  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IGUQ_GRpGQFy",
        "outputId": "85302211-ff67-44db-85df-0ef9e7cba24e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-----= Bem vindo ao cadastro de passageiros =-----\n",
            "\n",
            " -==-==- Digite quantas pessoas serão cadastradas:   -==-==-  \n",
            "2\n",
            "------1ª Pessoa------\n",
            "\n",
            "Nome: jose\n",
            "Sexo M/F: m\n",
            "Idade: 35\n",
            "------2ª Pessoa------\n",
            "\n",
            "Nome: msrio\n",
            "Sexo M/F: m\n",
            "Idade: 75\n",
            "A média de idade do grupo é de : 55.00 anos\n",
            "O homen mais velho tem 75 anos e se chama msrio\n",
            "Exitem 0 Mulheres menores de 20 anos\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#57 leia o sexo e só aceite F ou M se estiver errado pergunte de novo\n",
        "\n",
        "while True:\n",
        "  sexo = str(input('Digite o sexo: F ou M ')).strip().upper() [0]\n",
        "\n",
        "  if sexo == 'M' or sexo == 'F':\n",
        "    print('Sexo inserido com sucesso')\n",
        "    break\n",
        "     \n",
        "  else:\n",
        "    print('Digite o sexo novamente, sexo inválido ')\n",
        "    continue\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zh5EiXyPq_L8",
        "outputId": "6daeea05-6307-48d4-e6c8-0e7efcd51874"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o sexo: F ou M a\n",
            "Digite o sexo novamente em Maisculo \n",
            "Digite o sexo: F ou M b\n",
            "Digite o sexo novamente em Maisculo \n",
            "Digite o sexo: F ou M F\n",
            "Sexo inserido com sucesso\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#57 alternativa sem if else\n",
        "sexo = str(input('Digite o sexo: F ou M ')).strip().upper() [0]\n",
        "while sexo not in  'MmFf':\n",
        "  sexo = str(input('Digite o sexo novamente: F ou M ')).strip().upper() [0]\n",
        "\n",
        "print('Sexo inserido com sucesso')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1JwzOOeWmnDS",
        "outputId": "8b8b6a11-c392-4e3d-85fc-4513127f2d0f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o sexo: F ou M 2\n",
            "Digite o sexo novamente: F ou M s\n",
            "Digite o sexo novamente: F ou M d\n",
            "Digite o sexo novamente: F ou M m\n",
            "Sexo inserido com sucesso\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#58 Avaliando numero\n",
        "\n",
        "import random\n",
        "from time import sleep\n",
        "print('- \\u2620 -'*20)\n",
        "print('Pensei em um número: ? ')\n",
        "print('- \\u2620 -'*20)\n",
        "\n",
        "sorteio = random.randint(0,10)\n",
        "\n",
        "cont = 0\n",
        "while True:\n",
        "  n = int(input('Digite um numero entre 0 e 10 e veja se voce advinhou o numero que pensei: '))\n",
        "  print('Processando...')\n",
        "  sleep(2)\n",
        "  cont += 1\n",
        "  if n == sorteio:\n",
        "     print('Parabéns você acertou \\U0001F973!!')\n",
        "     break\n",
        "  else:\n",
        "     print(f'Não foi dessa vez ótario \\U0001F921!') \n",
        "     continue\n",
        "     \n",
        "print(f'Voce tentou acertar {cont} vezes')     \n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-p0cQrvzwSoQ",
        "outputId": "2285e841-33e0-4799-e6db-6255845c0844"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -\n",
            "Pensei em um número: ? \n",
            "- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -- ☠ -\n",
            "Digite um numero entre 0 e 10 e veja se voce advinhou o numero que pensei: 10\n",
            "Processando...\n",
            "Não foi dessa vez ótario 🤡!\n",
            "Digite um numero entre 0 e 10 e veja se voce advinhou o numero que pensei: 1\n",
            "Processando...\n",
            "Não foi dessa vez ótario 🤡!\n",
            "Digite um numero entre 0 e 10 e veja se voce advinhou o numero que pensei: 0\n",
            "Processando...\n",
            "Parabéns você acertou 🥳!!\n",
            "Voce tentou acertar 3 vezes\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ",#59 menu de calculos\n",
        "from time import sleep\n",
        "\n",
        "print(5*'-=-','Menu de Opçõea ', '-=-'*5)\n",
        "\n",
        "print('Digites dois valores abaixo: ')\n",
        "sleep(1)\n",
        "numero1 = int(input('Digite um valor\\n '))\n",
        "sleep(1)\n",
        "print('Número digitado com sucesso...')\n",
        "sleep(1)\n",
        "numero2 = int(input('Digite outro valor\\n '))\n",
        "sleep(1)\n",
        "print('Número digitado com sucesso...')\n",
        "sleep(1)\n",
        "print('Processando informações, abrindo Menu de Opções')\n",
        "sleep(2)\n",
        "\n",
        "while True:\n",
        "\n",
        "  op = int(input('Menu de Opções:\\n 1 -Somar\\n 2 - Multiplica\\n 3 - Maior Numero\\n 4 - Outros valores \\n5 - Sair\\n '))\n",
        "  print('Processando informações aguarde')\n",
        "  sleep(2)\n",
        "\n",
        "  if op == 1:\n",
        "     somar = numero1 + numero2\n",
        "     print('calculando soma')\n",
        "     sleep(1)\n",
        "     print(f'A soma foi de: {somar}')\n",
        "     continue\n",
        "\n",
        "  elif op == 2:\n",
        "     mult = numero1 * numero2\n",
        "     print('calculando a Multiplicação')\n",
        "     sleep(1)\n",
        "     print(f'A multiplicação é: {mult}')\n",
        "     continue\n",
        "\n",
        "  elif op == 3:\n",
        "    if numero1 == numero2:\n",
        "      print('Verificando números digitados aguarde...')\n",
        "      sleep(1)\n",
        "      print('Os números são iguais')\n",
        "      continue\n",
        "    num = max(numero1,numero2)\n",
        "    print('Verificando o maior número digitado aguarde...')\n",
        "    sleep(1)\n",
        "    print(f'O maior número é: {num}')\n",
        "    continue\n",
        "\n",
        "  elif op ==  4: \n",
        "      print('Digite novos valores: ')\n",
        "      sleep(1)\n",
        "      numero1 = int(input('Digite um valor novamente '))\n",
        "      numero2 = int(input('Digite outro valor novamente '))\n",
        "      print('Processando dados aguarde...')\n",
        "      sleep(1)\n",
        "      continue\n",
        "\n",
        "  elif op ==  5:\n",
        "      print('Saindo do programa,obrigado por usar nosso sistema')\n",
        "      break \n",
        "\n",
        "  else:\n",
        "      print('Opção inválida, tente novamente')\n",
        "      sleep(1)\n",
        "      continue  \n",
        "       \n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aroJzZXm18bo",
        "outputId": "dbd3887a-5668-47d4-fb60-bf9303ccb2da"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-=--=--=--=--=- Menu de Opçõea  -=--=--=--=--=-\n",
            "Digites dois valores abaixo: \n",
            "Digite um valor\n",
            " 10\n",
            "Número digiado com sucesso...\n",
            "Digite outro valor\n",
            " 15\n",
            "Número digiado com sucesso...\n",
            "Processando informações, abrindo Menu de Opções\n",
            "Menu de Opções:\n",
            " 1 -Somar\n",
            " 2 - Multiplica\n",
            " 3 - Maior Numero\n",
            " 4 - Outros valores \n",
            "5 - Sair\n",
            " 1\n",
            "Processando informações aguarde\n",
            "calculando soma\n",
            "A soma foi de: 25\n",
            "Menu de Opções:\n",
            " 1 -Somar\n",
            " 2 - Multiplica\n",
            " 3 - Maior Numero\n",
            " 4 - Outros valores \n",
            "5 - Sair\n",
            " 3\n",
            "Processando informações aguarde\n",
            "Verificando o maior número digitado aguarde...\n",
            "O maior número é: 15\n",
            "Menu de Opções:\n",
            " 1 -Somar\n",
            " 2 - Multiplica\n",
            " 3 - Maior Numero\n",
            " 4 - Outros valores \n",
            "5 - Sair\n",
            " 2\n",
            "Processando informações aguarde\n",
            "calculando a Multiplicação\n",
            "A multiplicação é: 150\n",
            "Menu de Opções:\n",
            " 1 -Somar\n",
            " 2 - Multiplica\n",
            " 3 - Maior Numero\n",
            " 4 - Outros valores \n",
            "5 - Sair\n",
            " 5\n",
            "Processando informações aguarde\n",
            "Saindo do programa,obrigado por usar nosso sistema\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#60 fatorial WHILE\n",
        "\n",
        "n = int(input('Digite um valor para calcular o fatorial '))\n",
        "c = n\n",
        "fat = 1\n",
        "print(f'Calculando Fatorial {n}! = ', end='')\n",
        "while c > 0:\n",
        "  print(f'{c}', end='')\n",
        "  print(f' X ' if c > 1 else ' = ', end='')\n",
        "  fat *= c\n",
        "  c -= 1\n",
        "print(f'{fat}')   \n",
        "  \n"
      ],
      "metadata": {
        "id": "hHq9mXXhNZme",
        "outputId": "88e091e8-72ac-4fa1-c9a8-a56484847634",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um valor para calcular o fatorial 5\n",
            "Calculando Fatorial 5! = 5 X 4 X 3 X 2 X 1 = 120\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#fatorial opção 2 FUNCTION \n",
        "from  math import factorial\n",
        "f = 0\n",
        "n = int(input('Digite um número e veja seu fatorial: '))\n",
        "f = factorial(n)\n",
        "print(f'O fatorial de {n} é: {f}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SYKpGfGaRWEg",
        "outputId": "1f0ee530-f767-432c-8e92-f3475b47f08b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número e veja seu fatorial: \n",
            "5\n",
            "O fatorial de 5 é: 120\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#fatorial opção 3 FOR\n",
        "\n",
        "n = int(input('Digite um número e veja seu fatorial: \\n'))\n",
        "f = 1\n",
        "for i in range(1, n+1):\n",
        "    print(f'{i}', end='')\n",
        "    if i < n:\n",
        "        print(' X ', end='')\n",
        "    else:\n",
        "        print(' = ', end='')\n",
        "    f *= i\n",
        "print(f)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "swJ88IhbXKvK",
        "outputId": "b5a4a305-51ab-40f6-ea6d-ada49a7035fa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número e veja seu fatorial: \n",
            "5\n",
            "1 X 2 X 3 X 4 X 5 = 120\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#61 calculando PA com WHILE\n",
        "\n",
        "termo = int(input('Digite um termo: '))\n",
        "razao = int(input('Digite a razão: '))\n",
        "c = 1 \n",
        "while c <= 10 :\n",
        "  print(termo, end = \" \")\n",
        "  termo += razao\n",
        "  c += 1\n",
        "  \n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pVArcwhxL6DR",
        "outputId": "219db294-2d45-4959-b99f-d0017a491227"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um termo: 5\n",
            "Digite a razão: 3\n",
            "5 8 11 14 17 20 23 26 29 32 "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#62 quantos termos usuario quer ver\n",
        "\n",
        "c = 1 \n",
        "termo = int(input('Digite um termo: '))\n",
        "razao = int(input('Digite a razão: '))\n",
        "termos = int(input('Digite quantos termos voce quer ver: '))\n",
        "\n",
        "\n",
        "while c <= termos :\n",
        "  print(termo, end = \" \")\n",
        "  termo = razao + termo\n",
        "  c += 1\n"
      ],
      "metadata": {
        "id": "KI6qXE-yQz8y",
        "outputId": "f337d731-fdfd-4c97-f2b6-c7a24bdd948f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um termo: 5\n",
            "Digite a razão: 3\n",
            "Digite quantos termos voce quer ver: 10\n",
            "5 8 11 14 17 20 23 26 29 32 "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#62 quantos termos usuario quer ver versao 2.0\n",
        "\n",
        "termo = int(input('Digite o termo da PA: '))\n",
        "razao = int(input('Digite a razão da PA: '))\n",
        "quantos_termos = int(input('Digite quantos termos que ver: '))\n",
        "cont = 1\n",
        "#termo = primeiro\n",
        "while cont <= quantos_termos:\n",
        "  print(termo,f' -> ', end='')\n",
        "  termo = razao+termo\n",
        "  cont += 1\n",
        "print('FIM', end='')\n",
        "\n",
        "  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SOUT_b06ePv6",
        "outputId": "d5127275-fa87-4f55-b50c-8fd21da42eea"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o termo da PA: 0\n",
            "Digite a razão da PA: 5\n",
            "Digite quantos termos que ver: 10\n",
            "0  -> 5  -> 10  -> 15  -> 20  -> 25  -> 30  -> 35  -> 40  -> 45  -> FIM"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#62 quantos termos usuario quer ver adcionando mais numeros depois\n",
        "\n",
        "c = 1 \n",
        "a1 = int(input('Digite um termo: '))\n",
        "r = int(input('Digite a razão: '))\n",
        "termos = int(input('Digite quantos termos voce quer ver: '))\n",
        "lista = []\n",
        "\n",
        "while c <= termos :\n",
        "  if r == 0 :\n",
        "    print('Não podemos adcionar 0 a razão, digite novamente: ')\n",
        "    continue\n",
        "  an = (a1 + ((c - 1)* r))\n",
        "  c += 1\n",
        "  lista.append(an)\n",
        "print(f'Os {termos} primeiros termos são {lista}')   \n",
        "\n",
        "while True:\n",
        "  opcao = int(input('Digite 1 - para adcionar mais termos\\n 2 - Sair \\n'))\n",
        "\n",
        "  if opcao == 1:\n",
        "     novos_termos = int(input('Digite quantos termos voce quer ver a mais: '))\n",
        "     for i in range(1, novos_termos+1):\n",
        "         an = (a1 + ((c - 1)* r))\n",
        "         c += 1\n",
        "         lista.append(an)\n",
        "         continue\n",
        "  elif opcao == 2:\n",
        "     print(f'Os a lista final de termos é: {lista}', end = \" \")\n",
        "     break\n",
        "  else:\n",
        "     print('Opção inválida digite novamente ')\n",
        "     continue\n",
        "  \n",
        "   \n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BSTm7TzJIhSm",
        "outputId": "807e8e95-edbf-48f5-bad3-c2b10675a598"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um termo: 5\n",
            "Digite a razão: 3\n",
            "Digite quantos termos voce quer ver: 5\n",
            "Os 5 primeiros termos são [5, 8, 11, 14, 17]\n",
            "Digite 1 - para adcionar mais termos\n",
            " 2 - Sair \n",
            "1\n",
            "Digite quantos termos voce quer ver a mais: 5\n",
            "Digite 1 - para adcionar mais termos\n",
            " 2 - Sair \n",
            "2\n",
            "Os a lista final de termos é: [5, 8, 11, 14, 17, 20, 23, 26, 29, 32] "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#62 quantos termos usuario quer ver adcionando mais numeros depois V 2.0\n",
        "\n",
        "c = 1 \n",
        "total = 0\n",
        "lista = []\n",
        "\n",
        "termo = int(input('Digite um termo:\\n '))\n",
        "razao = int(input('Digite a razão:\\n '))\n",
        "mais = int(input('Quantos termos?\\n ')) \n",
        "\n",
        "while mais != 0 :\n",
        "  total += mais\n",
        "  while c <= total:\n",
        "    lista.append(termo)\n",
        "    print(termo,' -> ', end = \" \")\n",
        "    termo += razao\n",
        "    c += 1\n",
        "  print('PAUSA')\n",
        "  mais = int(input('Quantos termos a mais?\\n '))  \n",
        "print(f'O total de termos é: {total} termos, com a seguinte lista:  {lista} -> FIM')  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c_v_SEc1hSUV",
        "outputId": "134125a2-b39e-43ce-9aa2-5416b67c1767"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um termo:\n",
            " 0\n",
            "Digite a razão:\n",
            " 2\n",
            "Quantos termos?\n",
            " 5\n",
            "0  ->  2  ->  4  ->  6  ->  8  ->  PAUSA\n",
            "Quantos termos a mais?\n",
            " 5\n",
            "10  ->  12  ->  14  ->  16  ->  18  ->  PAUSA\n",
            "Quantos termos a mais?\n",
            " 0\n",
            "O total de termos: 10, com os termos [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] -> FIM\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = 2\n",
        "lista = [0, '->'  ,1]\n",
        "\n",
        "print(lista)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SCo_Wc4zsi4t",
        "outputId": "587f65b4-1a74-4d27-cda4-e9ef1a3d597c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, '->', 1]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#63 fibonacci\n",
        "n = int(input('Quantos termos você quer mostrar? '))\n",
        "t1 = 0\n",
        "t2 = 1\n",
        "cont = 3\n",
        "print(f'{t1} -> {t2}', end='')\n",
        "while cont <= n:\n",
        "  t3 = t1 + t2\n",
        "  print(f' -> {t3}', end='')\n",
        "  t1 = t2\n",
        "  t2 = t3\n",
        "  cont += 1\n",
        "\n",
        "  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KRbvJ-1xySZi",
        "outputId": "3aab5b20-697e-416f-c9fa-3e6a4f204e49"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quantos termos você quer mostrar? 10\n",
            "0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13 -> 21 -> 34"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#63 Definindo a quantidade de números a serem gerados\n",
        "n = int(input('Quantos termos quer exibir: '))\n",
        "\n",
        "# Inicializando as variáveis com os dois primeiros números da sequência\n",
        "a = 0\n",
        "b = 1\n",
        "\n",
        "\n",
        "# Loop para gerar os próximos números da sequência\n",
        "for i in range(n):\n",
        "    print(a, end=' ')\n",
        "    a, b = b, a + b"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "10VW080Uuhru",
        "outputId": "4a4a5ceb-e6af-432a-f5b2-9c0025bb84ee"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quantos termos quer exibir: 12\n",
            "0 1 1 2 3 5 8 13 21 34 55 89 "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#63 fibonacci\n",
        "t1 = 0\n",
        "t2 = 1\n",
        "t3 = t1+t2\n",
        "lista  = [t1,t2]\n",
        "cont = 3\n",
        "n = int(10)\n",
        "while cont <= n:\n",
        "  t3 = t1+t2  \n",
        "  cont += 1\n",
        "  t1 = t2\n",
        "  t2 = t3\n",
        "  lista.append(t3)\n",
        "print(lista)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1amWfM0H3mhC",
        "outputId": "19cf5940-a36c-4d19-8449-d59234281031"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#64 Números primos\n",
        "\n",
        "num = int(input(\"Digite um número: \"))\n",
        "\n",
        "# Verifica se o número é primo\n",
        "primo = True\n",
        "for i in range(2, num):\n",
        "    if num % i == 0:\n",
        "        primo = False\n",
        "        break\n",
        "\n",
        "# Exibe o resultado\n",
        "if primo:\n",
        "    print(num, \"é um número primo\")\n",
        "else:\n",
        "    print(num, \"não é um número primo\")\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bnWgzIOYRuSX",
        "outputId": "23609534-0da0-47fe-ddbd-b834c1a5d421"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: 13\n",
            "13 é um número primo\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#63 fiboncci\n",
        "#Fn = Fn - 1 + Fn - 2\n",
        "n = int(input('Digite n '))\n",
        "#for i in range(5):\n",
        " # fn = n + (n - 1)\n",
        " # print(fn)\n",
        "\n",
        "lista = [0,1]\n",
        "c = 0\n",
        "while lista[-1] <= n :\n",
        "    lista.append(lista[-1] + lista[-2])\n",
        "    c += 1\n",
        "print(lista)    "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "glm_yFpkO9_3",
        "outputId": "7ae15269-9615-419c-ecc4-53f4cba93902"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite n 5\n",
            "[0, 1, 1, 2, 3, 5, 8]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#64/65 Crie um programa que leia vários números inteiros pelo teclado. \n",
        "#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre\n",
        "#quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).\n",
        "\n",
        "n = int(input('Digite um valor: '))\n",
        "numeros = [n]\n",
        "\n",
        "while n != 999:\n",
        "  n = int(input('Digite um valor: '))\n",
        "  if n == 999:\n",
        "    break \n",
        "  elif n > 999:\n",
        "    print('Este valor é proíbido')\n",
        "    continue \n",
        "  numeros.append(n)\n",
        "    \n",
        "soma = sum(numeros)\n",
        "media = soma / len(numeros)\n",
        "maior = max(numeros)\n",
        "menor = min(numeros)\n",
        "print(f'A soma dos valores digitados é: {soma} e a média é {media} com o maior valor de {maior} e o menor valor é {menor} com a lista de valores {numeros}')    "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GtUfZXm3WY4N",
        "outputId": "ff4151d0-bf1d-41b7-dba5-3251e8a9db0b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um valor: 10\n",
            "Digite um valor: 20\n",
            "Digite um valor: 30\n",
            "Digite um valor: 999\n",
            "A soma dos valores digitados é: 60 e a média é 20.0 com o maior valor de 30 e o menor valor é 10 com a lista de valores [10, 20, 30]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#64 Crie um programa que leia vários números inteiros pelo teclado. \n",
        "#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre\n",
        "#quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).\n",
        "n = cont = soma =0\n",
        "n = int(input('Digite um número ou 999 para sair: \\n'))\n",
        "while n != 999:\n",
        "  soma += n\n",
        "  cont += 1\n",
        "  n = int(input('Digite um número ou 999 para sair: \\n'))\n",
        "print(f'A soma é {soma} e tem {cont} digitos')  \n",
        "\n",
        " \n"
      ],
      "metadata": {
        "id": "-iufYJrD-o0C",
        "outputId": "3a3a3c1d-c6f5-4d55-c66c-8f6e9bcc86f1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número ou 999 para sair: \n",
            "1\n",
            "Digite um número ou 999 para sair: \n",
            "2\n",
            "Digite um número ou 999 para sair: \n",
            "3\n",
            "Digite um número ou 999 para sair: \n",
            "999\n",
            "A soma é 6 e tem 3 digitos\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#65 Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior \n",
        "#e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.\n",
        "\n",
        "numeros = []\n",
        "c=0\n",
        "while True:\n",
        "  op = int(input('Bem vindo, Digite 1 - Sair ou 2 - Continuar '))\n",
        "  if op == 2:\n",
        "    lista = int(input('Digite um valor: '))\n",
        "    numeros.append(lista)\n",
        "    c+=1\n",
        "    continue\n",
        "  elif op == 1:\n",
        "    print('Saindo do sistema')\n",
        "    break\n",
        "  else:\n",
        "    print('Número ou opção inválida')\n",
        "    continue \n",
        "\n",
        "soma = sum(numeros)\n",
        "media = soma/len(numeros)   \n",
        "maior = max(numeros)\n",
        "menor = min(numeros)  \n",
        "\n",
        "print(soma, media, maior, menor)\n",
        "\n",
        "\n",
        "  \n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "k_QFNP5I7Ifl",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b59d4eb1-d4f3-4363-af5e-9118bf216855"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Bem vindo, Digite 1 - Sair ou 2 - Continuar 2\n",
            "Digite um valor: 20\n",
            "Bem vindo, Digite 1 - Sair ou 2 - Continuar 2\n",
            "Digite um valor: 30\n",
            "Bem vindo, Digite 1 - Sair ou 2 - Continuar 2\n",
            "Digite um valor: 5\n",
            "Bem vindo, Digite 1 - Sair ou 2 - Continuar 2\n",
            "Digite um valor: 10\n",
            "Bem vindo, Digite 1 - Sair ou 2 - Continuar 1\n",
            "Saindo do sistema\n",
            "65 16.25 30 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#66 Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o \n",
        "#usuário digitar o valor 999, que é a condição de parada. No final,\n",
        "# mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).\n",
        "\n",
        "numeros=cont = soma = 0\n",
        "while True:\n",
        "  numeros = int(input('Digite um numero ou 999 para sair: '))\n",
        "\n",
        "  if numeros == 999:\n",
        "    print('saindo do programa')\n",
        "    break\n",
        "\n",
        "  soma += numeros\n",
        "  cont += 1\n",
        "print(f'A soma dos {cont} números digitados é {soma}')    \n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cNZkPWUnqjyl",
        "outputId": "1888c0ea-5f3c-4a16-a595-86858006e93c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero ou 999 para sair: 1\n",
            "Digite um numero ou 999 para sair: 2\n",
            "Digite um numero ou 999 para sair: 3\n",
            "Digite um numero ou 999 para sair: 4\n",
            "Digite um numero ou 999 para sair: 5\n",
            "Digite um numero ou 999 para sair: 999\n",
            "saindo do programa\n",
            "A soma dos 5 números digitados é 15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#67: Faça um programa que mostre a tabuada de vários números, um de cada vez, \n",
        "#para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.\n",
        "from time import sleep\n",
        "n = cont = 0\n",
        "\n",
        "while True:\n",
        "  n = int(input('Digite um número e veja a tabuada dele: '))\n",
        "\n",
        "  if n <= 0:\n",
        "    print('Número negativo ou zero valor, saindo do programa')\n",
        "    break\n",
        "    3\n",
        "  for i in range(1, 11):\n",
        "    print(f'{n} x {i} = {n*i}')  \n",
        "    sleep(1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PQ_po_bbtLpR",
        "outputId": "2d430655-1b50-4832-b168-9696f5de349e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número e veja a tabuada dele: 2\n",
            "2 x 1 = 2\n",
            "2 x 2 = 4\n",
            "2 x 3 = 6\n",
            "2 x 4 = 8\n",
            "2 x 5 = 10\n",
            "2 x 6 = 12\n",
            "2 x 7 = 14\n",
            "2 x 8 = 16\n",
            "2 x 9 = 18\n",
            "2 x 10 = 20\n",
            "Digite um número e veja a tabuada dele: 0\n",
            "Número negativo ou zero valor, saindo do programa\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando \n",
        "#o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.\n",
        "# acertar a soma dos numeros se é par ou impar\n",
        "from random import randint\n",
        "v = 0\n",
        "while True:\n",
        "  jogador = int(input('Digite um numero de 0 a 10: '))\n",
        "  computador = randint(0,10)\n",
        "  total = computador + jogador\n",
        "  tipo = ' '\n",
        "  tipo = str(input('Digite PAR ou IMPAR para o resultado\\n')).upper().strip() [0]\n",
        "  if tipo == 'PAR' and total % 2 == 0:\n",
        "    #if total % 2 ==0:\n",
        "      print('Você venceu')\n",
        "      v += 1\n",
        "      print(f'Você escolheu {tipo} e Você venceu: {v} vezes,Você jogou: {jogador}, o Coputador jogou: {computador}, a soma dos valores é de: {total}')\n",
        "  elif tipo == 'IMPAR' and total % 2 == 1:\n",
        "    print('Você venceu!!')\n",
        "    v+=1  \n",
        "    print(f'Você escolheu {tipo} e Você venceu: {v} vezes,Você jogou: {jogador}, o Coputador jogou: {computador}, a soma dos valores é de: {total}')\n",
        "  else:\n",
        "    print(f'Você perdeu! Resultado {total}')\n",
        "    break\n",
        "\n",
        "  print('Vamos jogar novamente....') \n",
        "  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hPZ5Hlqjz4zB",
        "outputId": "d9646f24-84fb-4df3-954e-4811f9521587"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero de 0 a 10: 6\n",
            "Digite PAR ou IMPAR para o resultado\n",
            "impar\n",
            "Você perdeu! Resultado 16\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#69 Crie um programa que leia a idade e o sexo de várias pessoas. \n",
        "#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:\n",
        "\n",
        "#A) quantas pessoas tem mais de 18 anos.\n",
        "\n",
        "#B) quantos homens foram cadastrados.\n",
        "\n",
        "#C) quantas mulheres tem menos de 20 anos.\n",
        "\n",
        "idade = 0\n",
        "tot20 = 0\n",
        "contM = 0\n",
        "contF = 0\n",
        "contIdade = 0\n",
        "print('-----= Bem vindo ao cadastro de pessoas =-----\\n')\n",
        "\n",
        "while True:\n",
        "\n",
        "  idade = int(input(' -==-==- Digite a idade:   -==-==-  \\n'))\n",
        "  if idade > 18:\n",
        "    contIdade += 1\n",
        "       \n",
        "  sexo = ' ' \n",
        "  while sexo not in 'FM':\n",
        "    sexo = str(input('   -==-==-  Digite o sexo [M/F]:   -==-==-   \\n')).upper().strip()[0]\n",
        "\n",
        "  if sexo == 'M':\n",
        "    contM += 1\n",
        "    \n",
        "\n",
        "  elif sexo == 'F':\n",
        "    if idade < 20 :\n",
        "      tot20 += 1\n",
        "\n",
        "  op = ' '\n",
        "  while op not in 'SN': \n",
        "    op = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).upper().strip()[0]\n",
        "\n",
        "  if op == 'S':\n",
        "     continue\n",
        "\n",
        "  elif op == 'N':\n",
        "     print('Saindo do programa...\\n')\n",
        "     break\n",
        "\n",
        "print(f'O total de pessoas maiores de 18 é de: {contIdade}\\n')\n",
        "print(f'O total de homens cadastrados é de: {contM}\\n')\n",
        "print(f'Exitem {tot20} Mulheres menores de 20 anos')\n"
      ],
      "metadata": {
        "id": "Mk1rVRdluZGU"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#70: Crie um programa que leia o nome e o preço de vários produtos. \n",
        "#O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:\n",
        "\n",
        "#A) qual é o total gasto na compra.\n",
        "\n",
        "#B) quantos produtos custam mais de R$1000.\n",
        "\n",
        "#C) qual é o nome do produto mais barato.\n",
        "\n",
        "soma = 0\n",
        "listaPreco = []\n",
        "listaProduto = []\n",
        "while True:\n",
        "  produto = str(input('Digite o nome do produto:\\n'))\n",
        "  listaProduto.append(produto)\n",
        "\n",
        "  preco = float(input('Digite o preço do Produto R$: \\n'))\n",
        "  listaPreco.append(preco)\n",
        "\n",
        "  \n",
        "\n",
        "  menor_preco = listaPreco.index(min(listaPreco))\n",
        "  nome_produto_mais_barato = listaProduto[menor_preco]\n",
        "\n",
        "\n",
        "  op=' '\n",
        "  op = str(input('Deseja continuar [S/N]: \\n')).upper().strip()[0]\n",
        "           \n",
        "  if op == 'S':\n",
        "     continue\n",
        "\n",
        "  if op == 'N':\n",
        "    print('{:-^40}'.format ('Saindo do Programa'))\n",
        "    break \n",
        "\n",
        "cont_maior_1000 = 0\n",
        "for preco in listaPreco:\n",
        "    if preco > 1000:\n",
        "        cont_maior_1000 += 1\n",
        "\n",
        "soma = sum(listaPreco)\n",
        "print(f'Os produtodos cadastrados são: {listaProduto} \\ncom valores de R$ {listaPreco}, \\nsoma dos valores e de R${soma:.2f}')\n",
        "print(f'O produto mais barato é \"{nome_produto_mais_barato}\" com preço de R$ {min(listaPreco):.2f}')\n",
        "print(f'{cont_maior_1000} produtos têm preço maior que R$ 1000')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8I1SCVO_3aUx",
        "outputId": "6ec26a55-07e5-465c-b11a-51dd24eaa867"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o nome do produto:\n",
            "carro\n",
            "Digite o preço do Produto R$: \n",
            "25000\n",
            "Deseja continuar [S/N]: \n",
            "s\n",
            "Digite o nome do produto:\n",
            "pao\n",
            "Digite o preço do Produto R$: \n",
            "3\n",
            "Deseja continuar [S/N]: \n",
            "s\n",
            "Digite o nome do produto:\n",
            "celular\n",
            "Digite o preço do Produto R$: \n",
            "1000\n",
            "Deseja continuar [S/N]: \n",
            "n\n",
            "-----------Saindo do Programa-----------\n",
            "Os produtodos cadastrados são: ['carro', 'pao', 'celular'] \n",
            "com valores de R$ [25000.0, 3.0, 1000.0], \n",
            "soma dos valores e de R$26003.00\n",
            "O produto mais barato é \"pao\" com preço de R$ 3.00\n",
            "1 produtos têm preço maior que R$ 1000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#71 simulando um caixa eletronico\n",
        "cedulas = [100, 50, 20, 10, 5, 1]\n",
        "\n",
        "while True:\n",
        "    valor = int(input(\"Digite o valor a ser sacado: \"))\n",
        "\n",
        "    for cedula in cedulas:\n",
        "        quantidade = valor // cedula\n",
        "        if quantidade > 0:\n",
        "            valor -= quantidade * cedula\n",
        "            print(f\"{quantidade} cédula(s) de R${cedula}\")\n",
        "\n",
        "        if valor == 0:\n",
        "            break\n",
        "\n",
        "    op = int(input('Deseja fazer outro Saque? DIGITE [1] para SIM ou [2] para NÃO\\n'))\n",
        "    \n",
        "    if op == 1:\n",
        "        continue\n",
        "\n",
        "    elif op == 2:\n",
        "        print('Obrigado por usar o Banco Becker')\n",
        "        break\n",
        "\n",
        "    else:\n",
        "        print('opção inválida')\n",
        "        continue"
      ],
      "metadata": {
        "id": "mHArQccVPiGZ",
        "outputId": "e940fce3-e0ab-4209-967d-0d3df7eebc5f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o valor a ser sacado: 356\n",
            "3 cédula(s) de R$100\n",
            "1 cédula(s) de R$50\n",
            "1 cédula(s) de R$5\n",
            "1 cédula(s) de R$1\n",
            "Deseja fazer outro Saque? DIGITE [1] para SIM ou [2] para NÃO\n",
            "2\n",
            "Obrigado por usar o Banco Becker\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install hashlib\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-Ly4u_nb9Hvs",
        "outputId": "6f8905a6-cd7a-460c-d641-e9faa6529c07"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting hashlib\n",
            "  Using cached hashlib-20081119.zip (42 kB)\n",
            "  \u001b[1;31merror\u001b[0m: \u001b[1msubprocess-exited-with-error\u001b[0m\n",
            "  \n",
            "  \u001b[31m×\u001b[0m \u001b[32mpython setup.py egg_info\u001b[0m did not run successfully.\n",
            "  \u001b[31m│\u001b[0m exit code: \u001b[1;36m1\u001b[0m\n",
            "  \u001b[31m╰─>\u001b[0m See above for output.\n",
            "  \n",
            "  \u001b[1;35mnote\u001b[0m: This error originates from a subprocess, and is likely not a problem with pip.\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25herror\n",
            "\u001b[1;31merror\u001b[0m: \u001b[1mmetadata-generation-failed\u001b[0m\n",
            "\n",
            "\u001b[31m×\u001b[0m Encountered error while generating package metadata.\n",
            "\u001b[31m╰─>\u001b[0m See above for output.\n",
            "\n",
            "\u001b[1;35mnote\u001b[0m: This is an issue with the package mentioned above, not pip.\n",
            "\u001b[1;36mhint\u001b[0m: See above for details.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#criptografia de senha  usandl sal e SHA256\n",
        "\n",
        "import hashlib\n",
        "import os\n",
        "\n",
        "# Gera um salt aleatório\n",
        "salt = os.urandom(128)\n",
        "\n",
        "senha = input(\"Digite a senha a ser criptografada: \")\n",
        "\n",
        "# Concatena o salt com a senha\n",
        "senha_com_salt = salt + senha.encode()\n",
        "\n",
        "# Criptografa a senha com o salt usando o algoritmo SHA-256\n",
        "senha_criptografada = hashlib.sha256(senha_com_salt).hexdigest()\n",
        "\n",
        "print(\"A senha criptografada é:\", senha_criptografada)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jftU5big9Ebm",
        "outputId": "57e60b8d-49c3-48e4-b585-62c996432274"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a senha a ser criptografada: Raissa123@1\n",
            "A senha criptografada é: a7c5bdc43083db32f2114177e7128cb9ba08ba4b54692f46aac768f375fa3ce7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from IPython.display import Image\n",
        "try:\n",
        "  filename = take_photo()\n",
        "  print('Saved to {}'.format(filename))\n",
        "  \n",
        "  # Show the image which was just taken.\n",
        "  display(Image(filename))\n",
        "except Exception as err:\n",
        "  # Errors will be thrown if the user does not have a webcam or if they do not\n",
        "  # grant the page permission to access it.\n",
        "  print(str(err))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 514
        },
        "id": "0jqRLzU9DjMt",
        "outputId": "d505e9dd-da3c-4fe0-c7f4-69b8d719c2c0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function takePhoto(quality) {\n",
              "      const div = document.createElement('div');\n",
              "      const capture = document.createElement('button');\n",
              "      capture.textContent = 'Capture';\n",
              "      div.appendChild(capture);\n",
              "\n",
              "      const video = document.createElement('video');\n",
              "      video.style.display = 'block';\n",
              "      const stream = await navigator.mediaDevices.getUserMedia({video: true});\n",
              "\n",
              "      document.body.appendChild(div);\n",
              "      div.appendChild(video);\n",
              "      video.srcObject = stream;\n",
              "      await video.play();\n",
              "\n",
              "      // Resize the output to fit the video element.\n",
              "      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);\n",
              "\n",
              "      // Wait for Capture to be clicked.\n",
              "      await new Promise((resolve) => capture.onclick = resolve);\n",
              "\n",
              "      const canvas = document.createElement('canvas');\n",
              "      canvas.width = video.videoWidth;\n",
              "      canvas.height = video.videoHeight;\n",
              "      canvas.getContext('2d').drawImage(video, 0, 0);\n",
              "      stream.getVideoTracks()[0].stop();\n",
              "      div.remove();\n",
              "      return canvas.toDataURL('image/jpeg', quality);\n",
              "    }\n",
              "    "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saved to photo.jpg\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "image/jpeg": "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\n",
            "text/plain": [
              "<IPython.core.display.Image object>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#dicionario,lista e tuplas\n",
        "#Essas linhas criam uma lista vazia, uma tupla vazia e um dicionário vazio, respectivamente.\n",
        "#Lista list=[]\n",
        "#Tupla tupla=()\n",
        "#Dicionario dic={}\n",
        "\n",
        "'''pessoa = {'Nome':['Davi','Maria'],'Altura':['1.76m','2.10'],'Sexo':['Masculino','Feminino']}\n",
        "print(pessoa['Nome'])\n",
        "print(pessoa['Altura'])\n",
        "print('Nome:',pessoa['Nome'][0],'Altura:',pessoa['Altura'][0],'Sexo:',pessoa['Sexo'][0])\n",
        "print(pessoa)'''\n",
        "\n",
        "pessoas = {}\n",
        "\n",
        "while True:\n",
        "    nome = str(input('Digite o Nome: (Ou sair para sair\\n)')).upper().strip()\n",
        "    if nome == 'SAIR':\n",
        "      break\n",
        "    idade = int(input('Digite a idade:\\n '))\n",
        "    sexo = str(input('Digite o Sexo: \\n'))\n",
        "\n",
        "    pessoa ={'Nome': nome, 'Sexo': sexo, 'Idade': idade}\n",
        "    pessoas[nome] = pessoa\n",
        "for nome, pessoa in pessoas.items():\n",
        "  print(f'Nome: {pessoa[\"Nome\"]}, Sexo: {pessoa[\"Sexo\"]}, Idade: {pessoa[\"Idade\"]}')\n",
        " "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZBYJ2BdbeYDz",
        "outputId": "90526c40-071d-4c2b-9366-b585aece1f48"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o Nome: (Ou sair para sair\n",
            ")davi\n",
            "Digite a idade:\n",
            " 43\n",
            "Digite o Sexo: \n",
            "masculino\n",
            "Digite o Nome: (Ou sair para sair\n",
            ")maria\n",
            "Digite a idade:\n",
            " 15\n",
            "Digite o Sexo: \n",
            "feminino\n",
            "Digite o Nome: (Ou sair para sair\n",
            ")sair\n",
            "Nome: DAVI, Sexo: masculino, Idade: 43\n",
            "Nome: MARIA, Sexo: feminino, Idade: 15\n",
            "{'Nome': 'MARIA', 'Sexo': 'feminino', 'Idade': 15}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "comedies = (\"Arrested Development\", \"How I Met Your Mother\", \"Always Sunny\")\n",
        "for show in comedies:\n",
        "    print(show)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OjaL7B3Nq2al",
        "outputId": "6ccd4849-e0af-46f6-e532-0bc744306707"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Arrested Development\n",
            "How I Met Your Mother\n",
            "Always Sunny\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#MEU PRÒPIO TRADUTOR\n",
        "#!pip install translate\n",
        "from translate import Translator\n",
        "\n",
        "translator = Translator(from_lang ='pt', to_lang ='en')\n",
        "\n",
        "palavra = str(input('Digite uma palavra:' ))\n",
        "\n",
        "traducao = translator.translate(palavra)\n",
        "\n",
        "\n",
        "print(f'A palavra:  {palavra}   traduzida é: {traducao}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zL7CP4u-1CCU",
        "outputId": "bd9f48c2-84ad-4c62-f925-b84296c3d1f6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: translate in /usr/local/lib/python3.9/dist-packages (3.6.1)\n",
            "Requirement already satisfied: lxml in /usr/local/lib/python3.9/dist-packages (from translate) (4.9.2)\n",
            "Requirement already satisfied: libretranslatepy==2.1.1 in /usr/local/lib/python3.9/dist-packages (from translate) (2.1.1)\n",
            "Requirement already satisfied: click in /usr/local/lib/python3.9/dist-packages (from translate) (8.1.3)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.9/dist-packages (from translate) (2.27.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.9/dist-packages (from requests->translate) (3.4)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.9/dist-packages (from requests->translate) (1.26.15)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.9/dist-packages (from requests->translate) (2.0.12)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.9/dist-packages (from requests->translate) (2022.12.7)\n",
            "Digite uma palavra:pai\n",
            "A palavra:  pai   traduzida é: father\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/gdrive')\n",
        "%cd /gdrive"
      ],
      "metadata": {
        "id": "KrcRq-V33z9J"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class Animal:\n",
        "    def __init__(self, nome, idade):\n",
        "        self.nome = nome\n",
        "        self.idade = idade\n",
        "\n",
        "    def fazerSom(self):\n",
        "        pass\n",
        "\n",
        "\n",
        "class Gato(Animal):\n",
        "  def __init__(self, nome):\n",
        "        self.nome = nome\n",
        "\n",
        "  def fazerSom(self):\n",
        "    return 'mia'\n",
        "\n",
        "class Cachorro(Animal):\n",
        "  def __init__(self, nome):\n",
        "        self.nome = nome\n",
        "  def fazerSom(self):\n",
        "    return 'late'        \n",
        "\n",
        "gato = Gato('Mimi')\n",
        "print(gato.fazerSom()) # output: mia\n",
        "\n",
        "dog = Cachorro('Caramelo')\n",
        "print(dog.fazerSom()) # output: late\n"
      ],
      "metadata": {
        "id": "08hy77Fa4Odt",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b54271d3-2388-4230-bff1-1f5e326662ee"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "mia\n",
            "late\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import IPython\n",
        "js_code = '''\n",
        "document.querySelector(\"#output-area\").appendChild(document.createTextNode(\"hello world!\"));\n",
        "'''\n",
        "display(IPython.display.Javascript(js_code))"
      ],
      "metadata": {
        "id": "vtxuXOcwDyAD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "letras = ['a','b','c']\n",
        "numero = [1,2,3]\n",
        "juntos = letras + numeros\n",
        "for i in range(0,3):\n",
        "  juntos1 = ''.join(letras)\n",
        "  i =+ 1\n",
        "  print(juntos1,'->', end='')\n",
        "  #print(juntos)\n",
        "print('FIM', end='') "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KEoZR7wOyJ-F",
        "outputId": "f1545d32-04b6-4945-863b-b35c90af07ff"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "abc ->abc ->abc ->FIM"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "c =1\n",
        "lista = []\n",
        "valor = ''\n",
        "\n",
        "while c != 'SAIR':\n",
        "  \n",
        "  valor = str(input('Digite um valor ou SAIR para sair ')).upper().strip()\n",
        "  if valor == 'SAIR':\n",
        "     break\n",
        "  c += 1 \n",
        " \n",
        "  lista.append(valor)\n",
        "c = c - 1     \n",
        "print(f'A lista é {lista} e tem {c} Elementos')\n",
        "print('FIM') "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dwhySqGRc9Ss",
        "outputId": "5e7b8137-6f8b-4ab5-ba0b-29487a9ede23"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um valor ou SAIR para sair 10\n",
            "Digite um valor ou SAIR para sair 20\n",
            "Digite um valor ou SAIR para sair sair\n",
            "A lista é ['10', '20'] e tem 2 Elementos\n",
            "FIM\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#cofre\n",
        "\n",
        "from time import sleep\n",
        "\n",
        "moedas = []\n",
        "moeda = 0\n",
        "quantidade_reais = 0\n",
        "quantidade_dolares = 0\n",
        "quantidade_euros = 0\n",
        "valor_total = 0\n",
        "converterDolarEmReal = 0\n",
        "converterEuroEmReal = 0\n",
        "moeda_converter = 0\n",
        "op_convercao = 0\n",
        "\n",
        "quantidade_moedas = int(input('Quantas moedas você quer adicionar?: '))\n",
        "\n",
        "for c in range(quantidade_moedas):\n",
        "   opcao = int(input('Escolha a Moeda:\\n1 - Real\\n2 - Dolar\\n3 - Euro\\n'))\n",
        "\n",
        "   if opcao == 1:\n",
        "    moeda = 'Real'\n",
        "\n",
        "   elif opcao == 2:\n",
        "    moeda = 'Dolar'\n",
        " \n",
        "   elif opcao == 3:\n",
        "    moeda = 'Euro'\n",
        "   \n",
        "   else:\n",
        "    print('Opção inválida!')\n",
        "    continue;\n",
        "\n",
        "   valor = float(input(f'Digite o valor da moeda de {moeda}: '))\n",
        "\n",
        "   nova_moeda = {'moeda': moeda, 'valor': valor}\n",
        "   \n",
        "   moedas.append(nova_moeda)\n",
        "   valor_total = valor_total + valor\n",
        "\n",
        "#print(f'{moeda} {valor} adicionado com sucesso à lista de moedas!')\n",
        "\n",
        "for moeda in moedas:\n",
        "    if moeda['moeda'] == 'Real':\n",
        "        quantidade_reais += 1\n",
        "\n",
        "    elif moeda['moeda'] == 'Dolar':\n",
        "        quantidade_dolares += 1\n",
        "        \n",
        "\n",
        "    elif moeda['moeda'] == 'Euro':\n",
        "        quantidade_euros += 1\n",
        "        \n",
        "\n",
        "        op_convercao = int(input('Deseja converter a moeda em real?  1 - Sim  2 - Não == '))\n",
        "        print('Processando opção de convesão....')\n",
        "        sleep(2)\n",
        "    while op_convercao == 1:\n",
        "        #if op_convercao == 1:\n",
        "                moeda_converter = int(input('Qual moeda deseja converter 1 - Dolar 2 - Euro  3 - Sair'))\n",
        "                print('Aguarde Processando...')\n",
        "                sleep(2);\n",
        "\n",
        "                if moeda_converter == 1:\n",
        "                         print(f'Convertendo moeda....')\n",
        "                         sleep(2)\n",
        "                         converterDolarEmReal = moeda['valor']  * 5.25\n",
        "                         print(f'Moeda Convertida {moeda[\"valor\"]}')\n",
        "\n",
        "                elif moeda_converter== 2:\n",
        "                         print(f'Convertendo moeda....')\n",
        "                         sleep(2)\n",
        "                         converterEuroEmReal = moeda['valor'] * 5.35\n",
        "                         print(f'Moeda Convertida {moeda[\"valor\"]}')\n",
        "\n",
        "                elif moeda_converter== 3:\n",
        "                         print(f'Saindo....')\n",
        "                         sleep(2)\n",
        "                         continue\n",
        "                else:\n",
        "                  print('Opção Inválida')\n",
        "                  sleep(2)\n",
        "                  print('Voltando Menu')\n",
        "                  continue;\n",
        "\n",
        "                  op_convercao = input('Deseja converter outra moeda em real? Digite Sim  OU  Não ').upper\n",
        "                  print('Processando requisção, aguarde!...')\n",
        "                  sleep(2)\n",
        "\n",
        "\n",
        "   # else:\n",
        "     # print('Voltando para o Menu')\n",
        "     # continue;\n",
        "\n",
        "\n",
        "print(f'''Foram adcionadas {quantidade_moedas} Moedas,\n",
        "{quantidade_reais} de Reais - {quantidade_dolares} de Dolar -]\n",
        "{quantidade_euros} de Euro\\n o Valor Total foi de {valor_total} Dolar Convertido {converterDolarEmReal} e Euro Convertido {converterEuroEmReal}''')\n",
        "       \n",
        "\n",
        "\n",
        "\n",
        "\n",
        "#print(f'''Foram adcionadas {quantidade_moedas} Moedas,\n",
        "#{quantidade_reais} de Reais - {quantidade_dolares} de Dolar -]\n",
        "#{quantidade_euros} de Euro\\n o Valor Total foi de {valor_total} Dolar Convertido {converterDolarEmReal} e Euro Convertido {converterEuroEmReal}''')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 884
        },
        "id": "v6JRkDo1cIh5",
        "outputId": "deefcb92-4ad4-482a-8147-8e27c1d5d58c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quantas moedas você quer adicionar?: 3\n",
            "Escolha a Moeda:\n",
            "1 - Real\n",
            "2 - Dolar\n",
            "3 - Euro\n",
            "2\n",
            "Digite o valor da moeda de Dolar: 3\n",
            "Escolha a Moeda:\n",
            "1 - Real\n",
            "2 - Dolar\n",
            "3 - Euro\n",
            "3\n",
            "Digite o valor da moeda de Euro: 3\n",
            "Escolha a Moeda:\n",
            "1 - Real\n",
            "2 - Dolar\n",
            "3 - Euro\n",
            "1\n",
            "Digite o valor da moeda de Real: 5\n",
            "Deseja converter a moeda em real?  1 - Sim  2 - Não == 1\n",
            "Processando opção de convesão....\n",
            "Qual moeda deseja converter 1 - Dolar 2 - Euro2\n",
            "Aguarde Processando...\n",
            "Convertendo moeda....\n",
            "Moeda Convertida 3.0\n",
            "Qual moeda deseja converter 1 - Dolar 2 - Euro1\n",
            "Aguarde Processando...\n",
            "Convertendo moeda....\n",
            "Moeda Convertida 3.0\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-24-86369c6cdf5c>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     56\u001b[0m     \u001b[0;32mwhile\u001b[0m \u001b[0mop_convercao\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m         \u001b[0;31m#if op_convercao == 1:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 58\u001b[0;31m                 \u001b[0mmoeda_converter\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Qual moeda deseja converter 1 - Dolar 2 - Euro'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     59\u001b[0m                 \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Aguarde Processando...'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     60\u001b[0m                 \u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m;\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    858\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    859\u001b[0m             )\n\u001b[0;32m--> 860\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    861\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    862\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    902\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    903\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 904\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    905\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    906\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#cofre\n",
        "moedas = []\n",
        "moeda = 0\n",
        "quantidade_reais = 0\n",
        "quantidade_dolares = 0\n",
        "quantidade_euros = 0\n",
        "valor_total = 0\n",
        "converterDolarEmReal = 0\n",
        "converterEuroEmReal = 0\n",
        "moeda_converter = 0\n",
        "op_convercao = ' '\n",
        "\n",
        "quantidade_moedas = int(input('Quantas moedas você quer adicionar?: '))\n",
        "\n",
        "for c in range(quantidade_moedas):\n",
        "    opcao = int(input('Escolha a Moeda:\\n1 - Real\\n2 - Dolar\\n3 - Euro\\n'))\n",
        "\n",
        "    if opcao == 1:\n",
        "        moeda = 'Real'\n",
        "    elif opcao == 2:\n",
        "        moeda = 'Dolar'\n",
        "    elif opcao == 3:\n",
        "        moeda = 'Euro'\n",
        "    else:\n",
        "        print('Opção inválida!')\n",
        "\n",
        "    valor = float(input(f'Digite o valor da moeda de {moeda}: '))\n",
        "\n",
        "    nova_moeda = {'moeda': moeda, 'valor': valor}\n",
        "\n",
        "    moedas.append(nova_moeda)\n",
        "    valor_total = valor_total + valor\n",
        "\n",
        "#print(f'{moeda} {valor} adicionado com sucesso à lista de moedas!')\n",
        "\n",
        "for moeda in moedas:\n",
        "    if moeda['moeda'] == 'Real':\n",
        "        quantidade_reais += 1\n",
        "    elif moeda['moeda'] == 'Dolar':\n",
        "        quantidade_dolares += 1\n",
        "    elif moeda['moeda'] == 'Euro':\n",
        "        quantidade_euros += 1\n",
        "\n",
        "    op_convercao = input('Deseja converter um moeda em real?Digite  Sim ou Não  ').upper()\n",
        "    while op_convercao == 'SIM':\n",
        "        moeda_converter = input('Qual moeda deseja converter? Dolar , Euro?  Ou Digite Sair para sair').upper()\n",
        "\n",
        "        if moeda_converter == 'DOLAR':\n",
        "            converterDolarEmReal = moeda['valor'] * 5.25\n",
        "            print('Convertendo valores, aguarde...')\n",
        "            sleep(2)\n",
        "            print(f'Moeda de US$ {moeda[\"valor\"]} Convertida com sucesso ')\n",
        "\n",
        "        elif moeda_converter == 'EURO':\n",
        "            converterEuroEmReal = moeda['valor'] * 5.35\n",
        "            print('Convertendo valores, aguarde...')\n",
        "            sleep(2)\n",
        "            print(f'Moeda de € {moeda[\"valor\"]} Convertida com sucesso ')\n",
        "\n",
        "        elif moeda_converter == 'SAIR':\n",
        "\n",
        "          print('Inciando Menu....')\n",
        "          sleep(2)\n",
        "          continue\n",
        "\n",
        "        else:\n",
        "            print('Opção Inválida')\n",
        "            continue\n",
        "\n",
        "        op_convercao = input('Deseja converter outra moeda em real? Digite Sim  OU  Não ').upper\n",
        "        print('Processando requisção, aguarde!...')\n",
        "        sleep(2)\n",
        "\n",
        "print(f'''Foram adicionadas {quantidade_moedas} Moedas\\n,\n",
        "{quantidade_reais} de Reais - {quantidade_dolares} de Dolar\\n -\n",
        "{quantidade_euros} de Euro.\n",
        "O Valor Total depositado foi de {valor_total}\\n - O Valor do Dolar Convertido US$,{converterDolarEmReal:.2f}\\n e o valor do Euro Convertido €{converterEuroEmReal:.2f}''')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cxUhDP1NV8Cl",
        "outputId": "b092fece-9371-4bc3-df15-dfcdfa7cdc03"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quantas moedas você quer adicionar?: 3\n",
            "Escolha a Moeda:\n",
            "1 - Real\n",
            "2 - Dolar\n",
            "3 - Euro\n",
            "1\n",
            "Digite o valor da moeda de Real: 5\n",
            "Escolha a Moeda:\n",
            "1 - Real\n",
            "2 - Dolar\n",
            "3 - Euro\n",
            "2\n",
            "Digite o valor da moeda de Dolar: 10\n",
            "Escolha a Moeda:\n",
            "1 - Real\n",
            "2 - Dolar\n",
            "3 - Euro\n",
            "3\n",
            "Digite o valor da moeda de Euro: 10\n",
            "Deseja converter a moeda em real? 1 - Sim 2 - Não == 1\n",
            "Qual moeda deseja converter? 1 - Dolar 2 - Euro  3 - Sair1\n",
            "Convertendo valores, aguarde...\n",
            "Moeda de US$ 5.0 Convertida com sucesso \n",
            "Deseja converter outra moeda em real? 1 - Sim 2 - Não == 1\n",
            "Processando requisção, aguarde!...\n",
            "Deseja converter a moeda em real? 1 - Sim 2 - Não == 1\n",
            "Qual moeda deseja converter? 1 - Dolar 2 - Euro  3 - Sair2\n",
            "Convertendo valores, aguarde...\n",
            "Moeda de € 10.0 Convertida com sucesso \n",
            "Deseja converter outra moeda em real? 1 - Sim 2 - Não == 2\n",
            "Processando requisção, aguarde!...\n",
            "Deseja converter a moeda em real? 1 - Sim 2 - Não == 2\n",
            "Foram adicionadas 3 Moedas\n",
            ",\n",
            "1 de Reais\n",
            " - 1 de Dolar\n",
            " -\n",
            "1 de Euro.\n",
            "\n",
            "O Valor Total foi de 25.0 - \n",
            "o Valor do Dolar Convertido US$,26.25\n",
            " e o valor do Euro Convertido €53.50\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "(( 10 / 2  ) > 5 ) or not ( 3 < 2 )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bdr7cEdmvZxy",
        "outputId": "84e36f8c-b2c5-469d-db16-726b74162d0a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numbers = [1, 2, 3, 4, 5]\n",
        "for num in numbers:\n",
        "  if num == 3:\n",
        "   continue\n",
        "   print(num)\n",
        "  else:\n",
        "   print(\"Done\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yQh2ogXRu-f8",
        "outputId": "52816823-4446-487f-ff6f-db7f809a9ed0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Done\n",
            "Done\n",
            "Done\n",
            "Done\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install scapy\n",
        "\n",
        "from scapy.all import *\n",
        "\n",
        "def packet_callback(packet):\n",
        "    print(packet.summary())\n",
        "\n",
        "def packet_callback(packet):\n",
        "    src_ip = packet[IP].src\n",
        "    dst_ip = packet[IP].dst\n",
        "    print(f\"Source IP: {src_ip}, Destination IP: {dst_ip}\")    \n",
        "\n",
        "sniff(prn=packet_callback, count=10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q0q8XJlqwib4",
        "outputId": "6ef59a42-142f-4b8e-c1ac-eb89d81ec7b8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting scapy\n",
            "  Downloading scapy-2.5.0.tar.gz (1.3 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.3/1.3 MB\u001b[0m \u001b[31m15.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Building wheels for collected packages: scapy\n",
            "  Building wheel for scapy (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for scapy: filename=scapy-2.5.0-py2.py3-none-any.whl size=1444346 sha256=4e8aadbaef4bd0bd1c477ac0168b3e17f2313e8eb842b521a7026db4cb53fe3b\n",
            "  Stored in directory: /root/.cache/pip/wheels/dd/1b/47/d46b1a87e339be501612cf4cd1bf57742e534f9c9aac7b00d6\n",
            "Successfully built scapy\n",
            "Installing collected packages: scapy\n",
            "Successfully installed scapy-2.5.0\n",
            "Source IP: 172.28.0.1, Destination IP: 172.28.0.12\n",
            "Source IP: 172.28.0.12, Destination IP: 172.28.0.1\n",
            "Source IP: 172.28.0.12, Destination IP: 172.28.0.1\n",
            "Source IP: 172.28.0.1, Destination IP: 172.28.0.12\n",
            "Source IP: 172.28.0.1, Destination IP: 172.28.0.12\n",
            "Source IP: 172.28.0.12, Destination IP: 172.28.0.1\n",
            "Source IP: 172.28.0.12, Destination IP: 172.28.0.1\n",
            "Source IP: 172.28.0.1, Destination IP: 172.28.0.12\n",
            "Source IP: 172.28.0.1, Destination IP: 172.28.0.12\n",
            "Source IP: 172.28.0.12, Destination IP: 172.28.0.1\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Sniffed: TCP:10 UDP:0 ICMP:0 Other:0>"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"+\" + 10 * \"-\" + \"+\")\n",
        "print((\"|\" + \" \" * 10 + \"|\\n\") * 5, end=\"\")\n",
        "print(\"+\" + 10 * \"-\" + \"+\")"
      ],
      "metadata": {
        "id": "biGuzDkDTy7p"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import pprint\n",
        "\n",
        "\n",
        "\n",
        "nums = {4: 1, 3: 2, 1: 1, 2: 3}\n",
        "\n",
        "\n",
        "\n",
        "pprint.pprint(nums, sort_dicts=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AQd5qbhwdC8b",
        "outputId": "c11ac5af-63ac-48c0-8b8c-10a7562395c2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{1: 1, 2: 3, 3: 2, 4: 1}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "palavra = 'abc'*3\n",
        "for i in palavra.split(','):\n",
        "  print(i)"
      ],
      "metadata": {
        "id": "z_VM9_J5prYO",
        "outputId": "30c761bc-1b39-4f08-b525-7b0635a4bd33",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "abcabcabc\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 1\n",
        "y = 1.0\n",
        "z = \"1\"\n",
        "\n",
        "if x == y:\n",
        "    print(\"one\")\n",
        "if y == int(z):\n",
        "    print(\"two\")\n",
        "elif x == y:\n",
        "    print(\"three\")\n",
        "else:\n",
        "    print(\"four\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RmusP99SXh4F",
        "outputId": "4e293801-f108-4594-dc93-924cfad58e3a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "one\n",
            "two\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Store the current largest number here.\n",
        "largest_number = -999999999\n",
        "\n",
        "# Input the first value.\n",
        "number = int(input(\"Enter a number or type -1 to stop: \"))\n",
        "\n",
        "# If the number is not equal to -1, continue.\n",
        "while number != -1:\n",
        "    # Is number larger than largest_number?\n",
        "    if number > largest_number:\n",
        "        # Yes, update largest_number.\n",
        "        largest_number = number\n",
        "    # Input the next number.\n",
        "    number = int(input(\"Enter a number or type -1 to stop: \"))\n",
        "\n",
        "# Print the largest number.\n",
        "print(\"The largest number is:\", largest_number)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gMI1jH80Hi_u",
        "outputId": "14c3a01f-1c72-4f46-e4cc-83ace5824756"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number or type -1 to stop: 250\n",
            "Enter a number or type -1 to stop: 1\n",
            "Enter a number or type -1 to stop: -1\n",
            "The largest number is: 250\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# A program that reads a sequence of numbers\n",
        "# and counts how many numbers are even and how many are odd.\n",
        "# The program terminates when zero is entered.\n",
        "\n",
        "odd_numbers = 0\n",
        "even_numbers = 0\n",
        "\n",
        "# Read the first number.\n",
        "number = int(input(\"Enter a number or type 0 to stop: \"))\n",
        "\n",
        "# 0 terminates execution.\n",
        "while number != 0:\n",
        "    # Check if the number is odd.\n",
        "    if number % 2 == 1:\n",
        "        # Increase the odd_numbers counter.\n",
        "        odd_numbers += 1\n",
        "    else:\n",
        "        # Increase the even_numbers counter.\n",
        "        even_numbers += 1\n",
        "    # Read the next number.\n",
        "    number = int(input(\"Enter a number or type 0 to stop: \"))\n",
        "\n",
        "# Print results.\n",
        "print(\"Odd numbers count:\", odd_numbers)\n",
        "print(\"Even numbers count:\", even_numbers)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JSWCoBK7IVo1",
        "outputId": "acb5f13e-198f-4ef0-ef89-41786ee06963"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number or type 0 to stop: 24\n",
            "Enter a number or type 0 to stop: 20\n",
            "Enter a number or type 0 to stop: 19\n",
            "Enter a number or type 0 to stop: 33\n",
            "Enter a number or type 0 to stop: 0\n",
            "Odd numbers count: 2\n",
            "Even numbers count: 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "counter = 5\n",
        "while counter != 0:\n",
        "    print(\"Inside the loop.\", counter)\n",
        "    counter -= 1\n",
        "print(\"Outside the loop.\", counter)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cG0PqPsQI4WV",
        "outputId": "241ab7c7-f203-4f75-db9d-858f4e1853aa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Inside the loop. 5\n",
            "Inside the loop. 4\n",
            "Inside the loop. 3\n",
            "Inside the loop. 2\n",
            "Inside the loop. 1\n",
            "Outside the loop. 0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "secret = 777\n",
        "print(\n",
        "\"\"\"\n",
        "+================================+\n",
        "| Welcome to my game, muggle!    |\n",
        "| Enter an integer number        |\n",
        "| and guess what number I've     |\n",
        "| picked for you.                |\n",
        "| So, what is the secret number? |\n",
        "+================================+\n",
        "\"\"\")\n",
        "number = int(input('Digite um numero ' ))\n",
        "\n",
        "while number != secret:\n",
        "    \n",
        "    if number == secret:\n",
        "        print('Ha ha! You are stuck in my loop!')\n",
        "       \n",
        "    \n",
        "    elif number != secret:\n",
        "        number = int(input('Você errou digite um numero novamente ' ))\n",
        "\n",
        "    else:\n",
        "        print('Numero invalido')\n",
        "        continue\n",
        "        \n",
        "\n",
        "print('\"Well done, muggle! You are free now.\"')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eV97erk-MPQl",
        "outputId": "8c0cc3af-4784-410b-e8d0-a7178f012dee"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "+================================+\n",
            "| Welcome to my game, muggle!    |\n",
            "| Enter an integer number        |\n",
            "| and guess what number I've     |\n",
            "| picked for you.                |\n",
            "| So, what is the secret number? |\n",
            "+================================+\n",
            "\n",
            "Digite um numero100\n",
            "Digite um numero novamente777\n",
            "\"Well done, muggle! You are free now.\"\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(100):\n",
        "    # do_something()\n",
        "    print('pass')"
      ],
      "metadata": {
        "id": "B9LbvwvcM-fe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from time import sleep\n",
        "\n",
        "for i in range(0,6):\n",
        "    print(f'{i} Mississipi!')\n",
        "    sleep(1)\n",
        "\n",
        "# Write a for loop that counts to five.\n",
        "    # Body of the loop - print the loop iteration number and the word \"Mississippi\".\n",
        "    # Body of the loop - use: time.sleep(1)\n",
        "\n",
        "# Write a print function with the final message."
      ],
      "metadata": {
        "id": "UpJo5RFIPKYH",
        "outputId": "de0dbab0-0c23-4d1e-a6f2-0262523ac7c5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 Mississipi!\n",
            "1 Mississipi!\n",
            "2 Mississipi!\n",
            "3 Mississipi!\n",
            "4 Mississipi!\n",
            "5 Mississipi!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "largest_number = -99999999\n",
        "counter = 0\n",
        "\n",
        "while True:\n",
        "    number = int(input(\"Enter a number or type -1 to end program: \"))\n",
        "    if number == -1:\n",
        "        break\n",
        "    counter += 1\n",
        "    if number > largest_number:\n",
        "        largest_number = number\n",
        "\n",
        "if counter != 0:\n",
        "    print(\"The largest number is\", largest_number ,'o programa foi executado',counter,'vezes')\n",
        "else:\n",
        "    print(\"You haven't entered any number.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VP_IMQubSEWU",
        "outputId": "00b062a5-d467-44a0-946c-f6a814ad1458"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number or type -1 to end program: 25\n",
            "Enter a number or type -1 to end program: 10\n",
            "Enter a number or type -1 to end program: -1\n",
            "The largest number is 25 o programa foi executado  2 vezes\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "secreta = 'chupacabra'\n",
        "palavra = input('Digite uma palavra ')\n",
        "\n",
        "while True :\n",
        "    \n",
        "    if palavra == secreta:\n",
        "        print(\"You've successfully left the loop.\")\n",
        "        break\n",
        "    else: \n",
        "        palavra = input('Digite uma palavra novamente ')"
      ],
      "metadata": {
        "id": "ubt30aRaThcM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Prompt the user to enter a word\n",
        "# and assign it to the user_word variable.\n",
        "user_word = input('Digite uma palavra ').upper()\n",
        "\n",
        "for letter in user_word:\n",
        "    # Complete the body of the for loop.\n",
        "    if letter in ['A', 'E', 'I', 'O', 'U']:\n",
        "        # se a letra for uma vogal, pula para a próxima iteração do loop\n",
        "        continue\n",
        "    print(letter)    \n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cUt_umKVXh5d",
        "outputId": "4cb5691a-2e7e-4b8e-f03d-43f6dc9f0fd0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(1, 'Andy', 17, [90, 97, 96])\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "word_without_vowels = \"\"\n",
        "\n",
        "# Prompt the user to enter a word\n",
        "# and assign it to the user_word variable.\n",
        "user_word = input(\"Introduza uma palavra: \").upper()\n",
        "\n",
        "\n",
        "for letter in user_word:\n",
        "    # Complete the body of the loop.\n",
        "\n",
        "# Print the word assigned to word_without_vowels.\n",
        " # Execução condicional para ignorar as vogais\n",
        "    if letter == \"A\":\n",
        "        continue\n",
        "    elif letter == \"E\":\n",
        "        continue\n",
        "    elif letter == \"I\":\n",
        "        continue\n",
        "    elif letter == \"O\":\n",
        "        continue\n",
        "    elif letter == \"U\":\n",
        "        continue\n",
        "    else:\n",
        "        # Concatenar as letras não vogais numa string\n",
        "        word_without_vowels += letter\n",
        "\n",
        "# Imprimir a palavra sem as vogais\n",
        "print(word_without_vowels)"
      ],
      "metadata": {
        "id": "0eHyTnxYbjH0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def fun_x(x):\n",
        "    x=x+'2'\n",
        "    x=x*2\n",
        "    return x\n",
        "print(fun_x('python'))"
      ],
      "metadata": {
        "id": "ap6k4v5HzDf6",
        "outputId": "0ae69db5-f386-42a9-83e5-a7e155a3ce5f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "python2python2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(10,-1,-1):\n",
        "   s = i\n",
        "   print(s)\n",
        "    "
      ],
      "metadata": {
        "id": "E5helCVaH7tR",
        "outputId": "8028af2d-706c-4a7d-b813-c374751f89ad",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10\n",
            "9\n",
            "8\n",
            "7\n",
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n",
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nums = [10, 20, 30]\n",
        "temp =nums\n",
        "nums.append(temp)\n",
        "print(nums)"
      ],
      "metadata": {
        "id": "i5mK00EVd06Z",
        "outputId": "a90a5448-2e84-46a7-9d57-e6ba86b46cc8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[10, 20, 30, [...]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def func(x):\n",
        " x[0]='def'\n",
        " x[1]='abc'\n",
        " return id(x)\n",
        "q = ['abc', 'def']\n",
        "print(id(q) == func(q))"
      ],
      "metadata": {
        "id": "PacSypDwiZYp",
        "outputId": "982dd642-844f-4f39-f175-70a46f37c48c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s = \"1234\"\n",
        "print(list(s))\n"
      ],
      "metadata": {
        "id": "sUAQnxUzjS-Y",
        "outputId": "ab9596e3-a488-497b-80de-8c4452206430",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['1', '2', '3', '4']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#manipulando arquvios\n",
        "\n",
        "def escrever_arquivo():\n",
        "    nome_arquivo = input(\"Digite o nome do arquivo: \")\n",
        "    conteudo = input(\"Digite o conteúdo do arquivo: \")\n",
        "\n",
        "    with open(nome_arquivo, 'w') as arquivo:\n",
        "        arquivo.write(conteudo)\n",
        "        print(f\"Arquivo {nome_arquivo} salvo com sucesso!\")\n",
        "\n",
        "def ler_arquivo():\n",
        "    nome_arquivo = input(\"Digite o nome do arquivo: \")\n",
        "\n",
        "    with open(nome_arquivo, 'r') as arquivo:\n",
        "        conteudo = arquivo.read()\n",
        "        print(conteudo)        \n",
        "\n",
        "escrever_arquivo()  \n",
        "ler_arquivo()      "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-Ut8Wlu9chq6",
        "outputId": "6d8fab3d-24c4-43e0-a35e-1133b978c9c6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o nome do arquivo: davi\n",
            "Digite o conteúdo do arquivo: teste\n",
            "Arquivo davi salvo com sucesso!\n",
            "Digite o nome do arquivo: davi\n",
            "teste\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#We need a function that can transform a number (integer) into a string.\n",
        "\n",
        "#What ways of achieving this do you know?\n",
        "\n",
        "'''Examples (input --> output):\n",
        "123  --> \"123\"\n",
        "999  --> \"999\"\n",
        "-100 --> \"-100\"'''\n",
        "\n",
        "number = int(input('Digite um numero: '))\n",
        "number2 = str(number)\n",
        "print(number2)"
      ],
      "metadata": {
        "id": "TG285WM1iCtx",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "529993f3-e3b4-44a2-93de-0fb1e1e8984b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero: 5\n",
            "number\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = int(input('Digite: '))\n",
        "b = int(input('Digite: '))\n",
        "\n",
        "c = a // b\n",
        "d = a / b\n",
        "print(c)\n",
        "print(d)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kdMjJ4UfRNUl",
        "outputId": "692e6970-c506-4957-ac98-e82fc21b9a22"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite: 4\n",
            "Digite: 6\n",
            "0\n",
            "0.6666666666666666\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__ == '__main__':\n",
        "    n = int(input())\n",
        "    seq = ''.join(str(i) \n",
        "    for i in range(1, n+1))\n",
        "    print(seq)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L0NY3XaMhHya",
        "outputId": "cc6f6b07-6b14-47b1-f996-534168941669"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "12345\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#listando repositórios do GitHub\n",
        "\n",
        "import requests\n",
        "\n",
        "class ListaRepositorio():\n",
        "    \n",
        "    def __init__(self,usuario):\n",
        "        self._usuario = usuario\n",
        "        \n",
        "        \n",
        "    def requisicao_api(self):\n",
        "        \n",
        "        resposta = requests.get( f'https://api.github.com/users/{self._usuario}/repos')\n",
        "        \n",
        "        if resposta.status_code == 200:\n",
        "            return resposta.json()\n",
        "        else:\n",
        "            return resposta.status_code    \n",
        "        \n",
        "    def imprime_repositorios(self):\n",
        "        \n",
        "        dados_api = self.requisicao_api()\n",
        "        \n",
        "        if type(dados_api) is not int:\n",
        "            for i in range(len(dados_api)):\n",
        "                print(dados_api[i]['name'])\n",
        "        else:\n",
        "            print(dados_api)\n",
        "            \n",
        "            \n",
        "repositorios = ListaRepositorio('VonBeckera')\n",
        "repositorios.imprime_repositorios() "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nd4Hp3WsAWIW",
        "outputId": "f65a61d1-9ad5-4107-eb43-0f2b5c411d35"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Eclipse\n",
            "Python\n",
            "Teste\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install flask\n",
        "pip install pandas\n",
        "pip install watchdog\n",
        "pip install xlsxwriter\n",
        "\n",
        "from flask import Flask, request, jsonify\n",
        "import pandas as pd\n",
        "import os\n",
        "\n",
        "app = Flask(__name__)\n",
        "\n",
        "# Define o caminho para o arquivo Excel\n",
        "excel_path = 'caminho/para/o/arquivo/excel.xlsx'\n",
        "\n",
        "# Lê os dados do Excel\n",
        "df = pd.read_excel(excel_path)\n",
        "\n",
        "# Define a rota para receber os dados do Excel\n",
        "@app.route('/update', methods=['POST'])\n",
        "def update_excel():\n",
        "    global df\n",
        "\n",
        "    # Lê os dados enviados via POST\n",
        "    data = request.json\n",
        "\n",
        "    # Atualiza o dataframe com os novos dados\n",
        "    df = pd.DataFrame(data)\n",
        "\n",
        "    # Salva os dados no arquivo Excel\n",
        "    writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')\n",
        "    df.to_excel(writer, index=False)\n",
        "    writer.save()\n",
        "\n",
        "    return jsonify({'status': 'success'})\n",
        "\n",
        "# Define a rota para retornar os dados do Excel\n",
        "@app.route('/data')\n",
        "def get_data():\n",
        "    global df\n",
        "    return df.to_json(orient='records')\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    app.run(debug=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Wc2FzqzBtNF-",
        "outputId": "fcc5a607-9835-4bc4-c940-c700a646c344"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Erro ao acessar a API: 404\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "CURSO EM VÍDEO -> MUNDO 03 -> AULA 16 TUPLAS\n",
        "\n"
      ],
      "metadata": {
        "id": "JI0Dt9-RGXZU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#TUPLAS#COmeçam com ()\n",
        "\n",
        "lanches = ('Hamburguer','Suco','Pizza','Pudim','Batata Frita')\n",
        "#print(lanches)\n",
        "#print(lanches[0])\n",
        "#print(lanches[:2])\n",
        "#print(lanches[2:])\n",
        "#print(lanches[-2])\n",
        "#print(lanches[1:3])\n",
        "#print(lanches[1:2:1])\n",
        "\n",
        "#imprimir a tupla sem posição\n",
        "for cont in lanches:\n",
        "  print(cont)\n",
        "\n",
        "print('=='*30)\n",
        "#imprimir usando o elemento da tupla com sua posição impressa\n",
        "for cont in range(0,len(lanches)):\n",
        "  print(f'Eu comi: {lanches[cont]} posição: {cont}')\n",
        "\n",
        "print('=='*30)\n",
        "#imprimir usando o elemento da tupla com sua posição impressa usando enumerate\n",
        "for pos,cont in enumerate(lanches):\n",
        "  print(f'Eu comi: {cont} na posicção {pos}')\n",
        "\n",
        "print('=='*30)\n",
        "\n",
        "#colocando a tupla para exibir elementos em ordem\n",
        "print(sorted(lanches))\n",
        "\n",
        "print('=='*30)\n",
        "'''\n",
        "for i in lanches:\n",
        "  print(i)\n",
        "\n",
        "testar = 'Refri' not in lanches\n",
        "testar2 = 'Refri' in lanches\n",
        "\n",
        "if testar == True:\n",
        "  print('e verdadeiro que Refri não faz parte da lista')\n",
        "if testar2 == False:\n",
        "  print('Refri não faz parte da lista')  \n",
        "\n",
        "print(testar)\n",
        "print(testar2)'''"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 400
        },
        "id": "RoCA_HOuGdAq",
        "outputId": "7dbdfa5f-79bd-4341-9c2e-76d413c133b2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hamburguer\n",
            "Suco\n",
            "Pizza\n",
            "Pudim\n",
            "Batata Frita\n",
            "============================================================\n",
            "Eu comi: Hamburguer posição: 0\n",
            "Eu comi: Suco posição: 1\n",
            "Eu comi: Pizza posição: 2\n",
            "Eu comi: Pudim posição: 3\n",
            "Eu comi: Batata Frita posição: 4\n",
            "============================================================\n",
            "Eu comi: Hamburguer na posicção 0\n",
            "Eu comi: Suco na posicção 1\n",
            "Eu comi: Pizza na posicção 2\n",
            "Eu comi: Pudim na posicção 3\n",
            "Eu comi: Batata Frita na posicção 4\n",
            "============================================================\n",
            "['Batata Frita', 'Hamburguer', 'Pizza', 'Pudim', 'Suco']\n",
            "============================================================\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "\"\\nfor i in lanches:\\n  print(i)\\n\\ntestar = 'Refri' not in lanches\\ntestar2 = 'Refri' in lanches\\n\\nif testar == True:\\n  print('e verdadeiro que Refri não faz parte da lista')\\nif testar2 == False:\\n  print('Refri não faz parte da lista')  \\n\\nprint(testar)\\nprint(testar2)\""
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lanches = ('Hamburguer','Suco','Pizza','Pudim','Batata Frita','Suco')\n",
        "lanches2 = ('macarrao','bolo','sorvete')\n",
        "lanches3 = lanches + lanches2\n",
        "\n",
        "print(lanches3)\n",
        "print('=='*50)\n",
        "\n",
        "print(sorted(lanches3))\n",
        "print('=='*50)\n",
        "\n",
        "for pos,cont in enumerate(lanches):\n",
        "  print(f'Eu comi: {cont} na posicção {pos}')\n",
        "print('=='*50)\n",
        "\n",
        "#achando a primeira ocorrencia de um objeto index()\n",
        "print(lanches.index('Suco'))  \n",
        "print('=='*50)\n",
        "\n",
        "#quantas vezes aparece um objeto count()\n",
        "print(lanches.count('Suco'))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ksn_CMN2IEly",
        "outputId": "9bb46afb-e256-4fb4-ea28-978dac8de85f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita', 'Suco', 'macarrao', 'bolo', 'sorvete')\n",
            "====================================================================================================\n",
            "['Batata Frita', 'Hamburguer', 'Pizza', 'Pudim', 'Suco', 'Suco', 'bolo', 'macarrao', 'sorvete']\n",
            "====================================================================================================\n",
            "Eu comi: Hamburguer na posicção 0\n",
            "Eu comi: Suco na posicção 1\n",
            "Eu comi: Pizza na posicção 2\n",
            "Eu comi: Pudim na posicção 3\n",
            "Eu comi: Batata Frita na posicção 4\n",
            "Eu comi: Suco na posicção 5\n",
            "====================================================================================================\n",
            "1\n",
            "====================================================================================================\n",
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#72  Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, \n",
        "#de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. \n",
        "\n",
        "numeros_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')\n",
        "\n",
        "while True:\n",
        "    numero = int(input('Digite um valor entre 0 e 20: '))\n",
        "    op = input('Deseja continuar? [S/N] ').strip().upper()\n",
        "\n",
        "    if op == 'N':\n",
        "      break\n",
        "\n",
        "    else:\n",
        "      print(f'O número que você digitou foi {numeros_por_extenso[numero]}.')\n",
        "      continue  \n",
        "    \n",
        "    if numero >= 0 and numero <= 20:\n",
        "      break\n",
        "\n",
        "    else:\n",
        "        print('Número inválido. Tente novamente.')\n",
        "        \n",
        "    \n",
        "    \n",
        "\n",
        "print(f'O número que você digitou foi {numeros_por_extenso[numero]}.')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5mjGZUCnONb8",
        "outputId": "07273a93-0cef-47a2-9a77-e998d14e510a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um valor entre 0 e 20: 10\n",
            "Deseja continuar? [S/N] s\n",
            "O número que você digitou foi dez.\n",
            "Digite um valor entre 0 e 20: 9\n",
            "Deseja continuar? [S/N] n\n",
            "O número que você digitou foi nove.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do \n",
        "#Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:\n",
        "#a) Os 5 primeiros times.\n",
        "#b) Os últimos 4 colocados.\n",
        "#c) Times em ordem alfabética. \n",
        "#d) Em que posição está o time da Chapecoense.\n",
        "\n",
        "campeonato_brasileiro = (\"Palmeiras\", \"Atlético-MG\", \"Fortaleza\", \"Bragantino\", \"Athletico-PR\", \n",
        "                        \"Fluminense\", \"Flamengo\", \"Cuiabá\", \"Santos\", \"Atlético-GO\", \n",
        "                        \"Corinthians\", \"Internacional\", \"Juventude\", \"Ceará\", \"São Paulo\", \n",
        "                        \"Sport Recife\", \"América-MG\", \"Grêmio\", \"Bahia\", \"Chapecoense\")\n",
        "\n",
        "\n",
        "print(f'O 5 primeiros times são: {campeonato_brasileiro[0:5]}')\n",
        "\n",
        "print(f'O 4 últimos colocados são os times: {campeonato_brasileiro[-4:]}')\n",
        "\n",
        "print(f'O 4 últimos colocados são os times: {sorted(campeonato_brasileiro)}')\n",
        "\n",
        "print(f'O Chapecoense está na: {campeonato_brasileiro.index(\"Chapecoense\")+1}ª posição')\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qriRqv1MzLot",
        "outputId": "ec89d285-c0b1-4fe5-cc0b-7c7b32c8be8d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "O 5 primeiros times são: ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Athletico-PR')\n",
            "O 4 últimos colocados são os times: ('América-MG', 'Grêmio', 'Bahia', 'Chapecoense')\n",
            "O 4 últimos colocados são os times: ['América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Bragantino', 'Ceará', 'Chapecoense', 'Corinthians', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'Sport Recife', 'São Paulo']\n",
            "O Chapecoense está na: 20ª posição\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tpl = (1,2,3,4,5)\n",
        "print(tpl.index(3, 2, 4))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6JPurymIwusr",
        "outputId": "bf5c9cf4-78e6-497b-db30-875ff172a5cb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#074 - Maior e menor valores em Tupla sorteado\n",
        "from random import randint\n",
        "lista = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))\n",
        "print(f'O valores sorteados são: {lista}')\n",
        "print(f'\\nO maior valor foi {max(lista)} \\nO menor valor foi {min(lista)}')\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8wUo-rKq5Hw1",
        "outputId": "3689ead4-b0e4-4836-80ce-5450d6373d23"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "O valores sorteados são: (2, 8, 5, 7, 1)\n",
            "\n",
            "O maior valor foi 8 \n",
            "O menor valor foi 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#75 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:\n",
        "\n",
        "#A) Quantas vezes apareceu o valor 9.\n",
        "\n",
        "#B) Em que posição foi digitado o primeiro valor 3.\n",
        "\n",
        "#C) Quais foram os números pares.\n",
        "\n",
        "lista = []\n",
        "cont = 0\n",
        "pares=[]\n",
        "for i in range(1,5):\n",
        "  n = int(input((f'Digite o {i}ª número: ')))\n",
        "  lista.append(n)\n",
        "\n",
        "  #if n == 9:\n",
        "    #cont +=1\n",
        "for i in lista:\n",
        "  if i % 2 == 0:\n",
        "    pares.append(i)\n",
        "\n",
        "  \n",
        "tupla_lista = tuple(lista)\n",
        "pares_tupla = tuple(pares)\n",
        "cont_nove = tupla_lista.count(9)\n",
        "\n",
        "\n",
        "print(f'A tupla é : {tupla_lista}')\n",
        "print('-=-'*15)\n",
        "if 3 in lista:\n",
        "  print('-=-'*15)\n",
        "  print(f'A posição do número 3 é : {tupla_lista.index(3)+1} posição')\n",
        "  print('-=-'*15)\n",
        "else:\n",
        "  print('-=-'*15)\n",
        "  print('O número 3 não foi encontrado')  \n",
        "  print('-=-'*15)\n",
        "print(f' número 9 apareceu {cont_nove} vezes')\n",
        "print('-=-'*15)\n",
        "print(f'Os números pares são:{pares_tupla} ')  \n",
        "print('-=-'*15)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HQ1ARAyvLu4o",
        "outputId": "3ae43d6f-1e75-4d38-a77e-fb316c850cba"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o 1ª número: 9\n",
            "Digite o 2ª número: 10\n",
            "Digite o 3ª número: 2\n",
            "Digite o 4ª número: 5\n",
            "A tupla é : (9, 10, 2, 5)\n",
            "-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\n",
            "-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\n",
            "O número 3 não foi encontrado\n",
            "-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\n",
            " número 9 apareceu 1 vezes\n",
            "-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\n",
            "5e os números pares são:(10, 2) \n",
            "-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#76: Crie um programa que tenha uma tupla única com nomes de produtos e seus \n",
        "#respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.\n",
        "\n",
        "ls = ('Agua',2.50,\n",
        "      'Refrigerante',2,\n",
        "      'Hamburguer', 5,\n",
        "      'Pizza',25,\n",
        "      'Batat Frita',10)\n",
        "\n",
        "print('='*40)\n",
        "print(f'{\"LISTAGEM DE PREÇOS\":^40}')\n",
        "print('='*40)\n",
        "for p in range(len(ls)):\n",
        "  if p % 2 == 0:\n",
        "    print(f'{ls[p]:.<30}',end='')\n",
        "  else:\n",
        "    print(f'R${ls[p]:>5.2f}')\n",
        "print('='*40)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hr4_IIOIwx2o",
        "outputId": "f26085af-4bfb-4590-d373-0c0cb48ff27d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "========================================\n",
            "           LISTAGEM DE PREÇOS           \n",
            "========================================\n",
            "Agua..........................R$ 2.50\n",
            "Refrigerante..................R$ 2.00\n",
            "Hamburguer....................R$ 5.00\n",
            "Pizza.........................R$25.00\n",
            "Batat Frita...................R$10.00\n",
            "========================================\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#treinamento\n",
        "\n",
        "lista = ('Lápis', 0.75,'Tesoura' , 1.75, 'Caderno 12 matérias', 20,'Cola Branca', 4,'Caneta Bic',1.25)\n",
        "print('='*40)\n",
        "print(f'{\"LISTA DE PREÇOS\":^40}')\n",
        "print('='*40)\n",
        "for i in range(len(lista)):\n",
        "  if i % 2 == 0:\n",
        "    print(f'{lista[i]:.<30}', end=' ')\n",
        "  else:\n",
        "    print(f'R${lista[i]:>6.2f}')  \n",
        "print('='*40)   \n",
        "\n",
        "print(lista[0])\n",
        "print(lista[1])#indice ímpar mostra o valor do produto\n",
        "print(lista[2])#Indice par mostra nome do produto"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UuYZFGTn_UXN",
        "outputId": "0f9eb220-27b8-41e2-de37-fe964ed3e3a0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "========================================\n",
            "            LISTA DE PREÇOS             \n",
            "========================================\n",
            "Lápis......................... R$  0.75\n",
            "Tesoura....................... R$  1.75\n",
            "Caderno 12 matérias........... R$ 20.00\n",
            "Cola Branca................... R$  4.00\n",
            "Caneta Bic.................... R$  1.25\n",
            "========================================\n",
            "Lápis\n",
            "0.75\n",
            "Tesoura\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).\n",
        "# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.\n",
        "vogais = []\n",
        "palavras = ('cafe', 'lapis', 'agua', 'refrigerante', 'cera','python')\n",
        "\n",
        "for p in palavras:\n",
        "  print(f'\\nNa palavra {p.upper()} temos as vogais:', end=' ')\n",
        "  for letra in p:\n",
        "    if letra.lower() in 'aeiouy':\n",
        "      print(letra, end=' ')\n",
        "  \n",
        " \n",
        "    "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tYh6Cho5ED3k",
        "outputId": "ce3f686f-25d6-478e-ec9e-e83ac6ef021e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Na palavra CAFE temos as vogais: a e \n",
            "Na palavra LAPIS temos as vogais: a i \n",
            "Na palavra AGUA temos as vogais: a u a \n",
            "Na palavra REFRIGERANTE temos as vogais: e i e a e \n",
            "Na palavra CERA temos as vogais: e a \n",
            "Na palavra PYTHON temos as vogais: y o "
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "CeUlPm1f9tyZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "CURSO EM VÍDEO -> Mundo 03 PYTHON -> AULA 17 LISTA []"
      ],
      "metadata": {
        "id": "8FvFA8X19lne"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Listas [ ]\n",
        "'''num = [1,2,5,3,4,9,83,6,8,7]\n",
        "num.sort()#ordem crescente\n",
        "num.remove(83)#remove o valor 83 da lista\n",
        "num.insert(0,0)# insere o valor 0 na posição 0\n",
        "num.pop()#remove o último elemento da lista com pop\n",
        "num.pop(3)#remove o número 3 da lista\n",
        "num.append(10)#add número 10 a lista\n",
        "num.append(2)#add número 2 a lista\n",
        "print(f'A lista tem {len(num)} elementos')\n",
        "print(num.index(4))# Mostra a posição do número 10\n",
        "print(num)  \n",
        "\n",
        "for i in range(len(num)):#removendo todas as ocorrências de um determinado valor ou o que for solicitado na lista\n",
        "  if 2 in num:\n",
        "    num.remove(2)\n",
        "\n",
        "print(num)  \n",
        "'''\n",
        "\n",
        "lista = []\n",
        "lista.append(0)\n",
        "lista.append(1)\n",
        "lista.append(2)\n",
        "\n",
        "for v in lista:\n",
        "  print(f'Os valores são {v}')#imprimindo de forma mais elaborada,formatada\n",
        "\n",
        "\n",
        "for c,v in enumerate(lista):# Imprimindo lista com a posição e o valor\n",
        "  print(f'Os valor da posição {c}ª é {v}')\n",
        "\n",
        "print(lista)\n",
        "\n",
        "lista2 = []\n",
        "for cont in range(0,10):\n",
        "  lista2.append(int(input('Digite um valor: ')))\n",
        "\n",
        "print(lista2)  \n",
        "print(f'O mairo valor é: {max(lista2)}')\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qk0rIYrP9vlV",
        "outputId": "6016a9ff-4fe8-4964-c50a-8c9b49d71729"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Os valores são 0\n",
            "Os valores são 1\n",
            "Os valores são 2\n",
            "Os valor da posição 0ª é 0\n",
            "Os valor da posição 1ª é 1\n",
            "Os valor da posição 2ª é 2\n",
            "[0, 1, 2]\n",
            "Digite um valor: 10\n",
            "Digite um valor: 20\n",
            "Digite um valor: 30\n",
            "Digite um valor: 40\n",
            "Digite um valor: 50\n",
            "Digite um valor: 60\n",
            "Digite um valor: 70\n",
            "Digite um valor: 80\n",
            "Digite um valor: 90\n",
            "Digite um valor: 100\n",
            "[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]\n",
            "O mairo valor é: 100\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#USANDO VOZES NO PYTHON\n",
        "\n",
        "import pyttsx3\n",
        "\n",
        "# inicializa a engine\n",
        "engine = pyttsx3.init()\n",
        "\n",
        "# configura as propriedades da voz robótica\n",
        "voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_PT-BR_MARIA_11.0'\n",
        "engine.setProperty('voice', voice_id)  # selecione uma voz robótica\n",
        "# fala um texto com a voz robótica\n",
        "\n",
        "engine.say(\"Qual é o seu nome? \")\n",
        "engine.runAndWait()\n",
        "\n",
        "nome=str(input('Nome: '))\n",
        "\n",
        "engine.say(f'Seja bem vindo{nome}, eu sou a Anna,  o que vamos fazer hoje?')\n",
        "engine.runAndWait()\n",
        "\n",
        "engine.say(f'Escolhas as opções: 1- cadastrar 2 - Sair')\n",
        "engine.runAndWait()\n",
        "op = int(input('Opção: '))\n",
        "if op == 1 :\n",
        "    engine.say(\"Digite sua idade e sexo:\")\n",
        "    engine.runAndWait()\n",
        "    idade=int(input('Idade: '))\n",
        "    sexo=str(input('Sexo: '))\n",
        "    engine.say(f'Sua idade é de {idade} anos e seu sexo é {sexo}, obrigado por utilizar nosso sistema')\n",
        "    engine.runAndWait()\n",
        "elif op == 2 :\n",
        "    engine.say(f'Saindo do sistema {nome} até mais..')\n",
        "    engine.runAndWait()\n",
        "\n",
        "else:\n",
        "    engine.say(f'Opção errado..')\n",
        "    engine.runAndWait() \n"
      ],
      "metadata": {
        "id": "jJCGta0OdEeZ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 391
        },
        "outputId": "372b13b7-9607-4244-d624-cd59898f5b28"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-26-b7d186e2dc47>\u001b[0m in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#USANDO VOZES NO PYTHON\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mpyttsx3\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;31m# inicializa a engine\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'pyttsx3'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from random import randint\n",
        "\n",
        "lista = []\n",
        "\n",
        "for i in range(0,11):\n",
        "  sorte = randint(0,10)\n",
        "  lista.append(sorte)\n",
        "  print(f'{lista[i]}', end =' ')\n",
        "\n",
        "for i in range(len(lista)):\n",
        "  for j in range(i+1, len(lista)):\n",
        "    if lista[i] == lista[j]:\n",
        "            lista.pop(j)\n",
        "            break\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "print(f'\\n{sorted(lista)}',end = '')       "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BObX_bxoumV0",
        "outputId": "02ddead1-8d9d-4bfd-d82b-7f5a640a0906"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7 5 9 4 1 2 5 10 10 5 0 \n",
            "[0, 1, 2, 4, 5, 5, 7, 9, 10]"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# USANDO MATPLOTLIB \n"
      ],
      "metadata": {
        "id": "n8-XnIOSYZ1O"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Criando primeiro gráfico\n",
        "[MATPLOTLIB SITE OFICIAL](https://matplotlib.org/stable/users/getting_started/)"
      ],
      "metadata": {
        "id": "ZrjD-6VFYnW4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "\n",
        "x = np.linspace(0, 2 * np.pi, 200)\n",
        "y = np.sin(x)\n",
        "\n",
        "fig, ax = plt.subplots()\n",
        "ax.plot(x, y)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 430
        },
        "id": "GG6YTTgqYmCg",
        "outputId": "384d176a-f22b-47bf-b475-ff7a5fc6c651"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.DataFrame(\n",
        "    {\n",
        "        \"Name\": [\n",
        "            \"Braund, Mr. Owen Harris\",\n",
        "            \"Allen, Mr. William Henry\",\n",
        "            \"Bonnell, Miss. Elizabeth\",\n",
        "            \"Becker,Mrs. Davi\",\n",
        "        ],\n",
        "        \"Age\": [22, 35, 58, 60],\n",
        "        \"Sex\": [\"male\", \"male\", \"female\",\"male\"],\n",
        "    }\n",
        ")\n",
        "\n",
        "#idade_maxima = df['Age'].max()#imprimindo a idade maxima\n",
        "#print(f'A idade máxima de lista é\\n: {idade_maxima}\\n anos')\n",
        "#df['Name']#Imprimindo somente os nomes\n",
        "#df.describe()#é um método do pandas que retorna um resumo estatístico das colunas numéricas em um DataFrame.\n",
        "#mean é a média aritmética dos valores na coluna correspondente  é o desvio padrão dos valores na coluna correspondente. \n",
        "#O desvio padrão é uma medida de quão dispersos os valores estão em torno da média\n",
        "#df['Sex']#imprime somente o sexo\n",
        "print(df.iloc[2])#imprime as informações do indece 2\n",
        "\n",
        "df.to_excel(\"df.xlsx\", sheet_name=\"passengers\", index=False)#grava o dataframe em um planilha excel "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gl25IF7WdRpo",
        "outputId": "1ab220e0-449e-4ee1-b7fc-6eb5dc4cdae7"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Name    Bonnell, Miss. Elizabeth\n",
            "Age                           58\n",
            "Sex                       female\n",
            "Name: 2, dtype: object\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "plt.plot([1, 2, 3, 4])\n",
        "plt.ylabel('some numbers')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 430
        },
        "id": "Bo_7qhdvaAIL",
        "outputId": "d14d90b9-5140-4041-f63d-3b7363ca13c0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Python UNINTER AULAS DE DATA SCIENCE\n"
      ],
      "metadata": {
        "id": "jdJwlFk88fP3"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "NUMPY 1 - Lista X Array"
      ],
      "metadata": {
        "id": "Gywl41rh-vBw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# listas versus array numpy\n",
        "import numpy as np\n",
        "\n",
        "num_elementos = 100000000\n",
        "#lista_elementos = []\n",
        "\n",
        "#for x in range(num_elementos):\n",
        " # lista_elementos.append(x)\n",
        "#print(lista_elementos[-1])  \n",
        "#tempo de execução 21 segundos e 4,8Gb de Memória\n",
        "\n",
        "#AARRAY NUMPY\n",
        "#0 segundos e 300MB de memória\n",
        "array_elementos = np.arange(num_elementos)\n",
        "\n",
        "print(array_elementos[-1])\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t1Xy7eIPMKA7",
        "outputId": "417ab88a-3689-4b9e-9477-5ae658a88da2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "99999999\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "NUPY 2 - criando um lista de array com numpy"
      ],
      "metadata": {
        "id": "v7X1ROgN-0Cy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#criando um lista de array com numpy\n",
        "import numpy as np\n",
        "array_numpy = np.array([0,1,2,3,4,5,6,7,8,9])\n",
        "numpy = [0,1,2,3,4,5,6,7,8,9]\n",
        "\n",
        "#10 elementos 0 a 9 matriz\n",
        "print(np.arange(10).reshape(2,5))\n",
        "\n",
        "print(np.arange(100+1))\n",
        "\n",
        "print(f'Criando um array de 40 elementos usando LINSPACE 0 a 40 com 41 elementos\\n {np.linspace(0,40, num =41)}\\n')\n",
        "\n",
        "print(f'Criando array usando numpy com metódo .array: \\n{array_numpy}\\n')\n",
        "print(f'Criando array usando numpy com metódo .ones: \\n{np.ones(10)}\\n')#ponto flutuante de 64bits 1.\n",
        "print(f'Criando array usando numpy com metódo .zeros: \\n{np.zeros(10)}\\n')#ponto flutuante de 64bits 0.\n",
        "print(f'Criando array usando numpy com metódo .reshape matrizes: \\n{np.array(array_numpy).reshape(2,5)}\\n')#Criando matriz"
      ],
      "metadata": {
        "id": "lLVK-WQKTnVS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "NUMPY 3 - TESTANDO CONSUM DE MEMÓRIA"
      ],
      "metadata": {
        "id": "j0hLmhMV-8Qq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#testando tipos de dados e consumo de memoria\n",
        "\n",
        "import numpy as np\n",
        "\n",
        "elementos = 1000000000000\n",
        "array_elementos = np.zeros(elementos)#, dtype = np.int8)\n",
        "print(array_elementos)"
      ],
      "metadata": {
        "id": "WWIRXfy0dTtM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "NUMPY 5 - CRIANDO NÚMEROS RANDÔMICOS"
      ],
      "metadata": {
        "id": "xnxeLDi__DVI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#criando numeros randômicos\n",
        "\n",
        "num = np.random.default_rng()\n",
        "\n",
        "print(num.random(10))"
      ],
      "metadata": {
        "id": "YChEmkEHfI67"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "NUMPY 6 - VETOR,MATRIZ E TENSOR"
      ],
      "metadata": {
        "id": "jobxU43q-lt5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Matrizes, vetores e tensores\n",
        "num = np.random.default_rng()\n",
        "vetor = num.random(4)\n",
        "print(f'Array de 1 dimensão = VETOR {vetor}\\n')\n",
        "print('-=-'*30)\n",
        "matriz = num.random([3,3])\n",
        "print(f'Array de 2 dimensões = MATRIZ \\n {matriz}\\n')\n",
        "print('-=-'*30)\n",
        "tensor = num.random([3,3,3,3])\n",
        "print(f'Array de 3 ou mais dimensões = TENSOR \\n {tensor}\\n')\n",
        "print('-=-'*30)"
      ],
      "metadata": {
        "id": "fZPzkEc1ghs7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "NUMPY 7 ORDENAÇÃO E ADIÇÃO DE ELEMENTOS\n"
      ],
      "metadata": {
        "id": "KFuaYAJ3_MB4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#NUMPY 7 ORDENAÇÃO E ADIÇÃO DE ELEMENTOS\n",
        "import numpy as np\n",
        "\n",
        "ngr = np.random.default_rng()\n",
        "\n",
        "array_1 = ngr.random([5,5])\n",
        "\n",
        "print(f'Array 1 SEM ORENAÇÃO:\\n {array_1}\\n')\n",
        "print(f'Array 2 ORENAÇÃO SIMPLES: \\n {np.sort(array_1)}\\n')\n",
        "print(f'Array 2 ORENAÇÃO SIMPLES HORIZONTAL EIXO X AXIS: \\n {np.sort(array_1, axis=None)}\\n')#Eixo horizontal apenas linhas\n",
        "print(f'Array 2 ORENAÇÃO SIMPLES Colunas: \\n {np.sort(array_1, axis=0)}\\n')#Ordena Colunas\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hXpEgh1o9BNS",
        "outputId": "0a684a54-c252-44dc-e2ff-18f2ec3be326"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Array 1 SEM ORENAÇÃO:\n",
            " [[0.10262821 0.01036806 0.71505954 0.90252851 0.82025941]\n",
            " [0.56882654 0.3425913  0.74407165 0.78641041 0.21024858]\n",
            " [0.12901641 0.89387044 0.29954194 0.50698563 0.18440761]\n",
            " [0.48603919 0.96787374 0.26848494 0.53941411 0.35852024]\n",
            " [0.69340347 0.88721011 0.78699561 0.46544344 0.18954041]]\n",
            "\n",
            "Array 2 ORENAÇÃO SIMPLES: \n",
            " [[0.01036806 0.10262821 0.71505954 0.82025941 0.90252851]\n",
            " [0.21024858 0.3425913  0.56882654 0.74407165 0.78641041]\n",
            " [0.12901641 0.18440761 0.29954194 0.50698563 0.89387044]\n",
            " [0.26848494 0.35852024 0.48603919 0.53941411 0.96787374]\n",
            " [0.18954041 0.46544344 0.69340347 0.78699561 0.88721011]]\n",
            "\n",
            "Array 2 ORENAÇÃO SIMPLES HORIZONTAL EIXO X AXIS: \n",
            " [0.01036806 0.10262821 0.12901641 0.18440761 0.18954041 0.21024858\n",
            " 0.26848494 0.29954194 0.3425913  0.35852024 0.46544344 0.48603919\n",
            " 0.50698563 0.53941411 0.56882654 0.69340347 0.71505954 0.74407165\n",
            " 0.78641041 0.78699561 0.82025941 0.88721011 0.89387044 0.90252851\n",
            " 0.96787374]\n",
            "\n",
            "Array 2 ORENAÇÃO SIMPLES Colunas: \n",
            " [[0.10262821 0.01036806 0.26848494 0.46544344 0.18440761]\n",
            " [0.12901641 0.3425913  0.29954194 0.50698563 0.18954041]\n",
            " [0.48603919 0.88721011 0.71505954 0.53941411 0.21024858]\n",
            " [0.56882654 0.89387044 0.74407165 0.78641041 0.35852024]\n",
            " [0.69340347 0.96787374 0.78699561 0.90252851 0.82025941]]\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "tips = sns.load_dataset(\"tips\")\n",
        "\n",
        "sns.barplot(x=\"sex\", y=\"total_bill\", data=tips)\n",
        "\n",
        "plt.show()\n",
        "\n",
        "tips = sns.load_dataset(\"tips\")\n",
        "\n",
        "sns.barplot(x=\"sex\", y=\"total_bill\", hue=\"size\", data=tips)\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "YNXkk-1JbXBE",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 883
        },
        "outputId": "0e9a802c-f002-4875-dc08-5a8d40a3fbdd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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LF++vMH9wYMHR0TE2rVrIyKia9eu0bVr1/j1r399BMcDADi0RsfMiy+++JF3vmnTpigrK4tWrfwEFADQPJq1Mj796U/H+vXrm/MpAIBjXLPGjG8GBgCam/M/AEDSxAwAkDQxAwAkrVljJpPJNOfuAQBcAAwApK1JPzTZWCtXroyysrLmfAoA4BjX6JgZM2ZMo3f69NNPR0REeXn5R58IAOAjaHTMlJaWNuccAABN0uiYmTt3bnPOAQDQJD6aDQAkrckXAD/11FPxgx/8IDZs2BB79+5tsO71118/7MEAABqjSUdmZs6cGRMnTozu3bvH8uXL43Of+1x06dIlfvvb38aIESOO9IwAAAfVpJh54IEH4sEHH4z77rsv2rZtGzfeeGM8//zzce2118bOnTuP9IwAAAfVpJjZsGFDnH322RER0a5du9i1a1dERFxxxRXxxBNPHLnpAAA+RJNipkePHrF9+/aIiOjVq1e89tprERGxbt063/oLALSoJsXMBRdcED/60Y8iImLixIkxefLk+OM//uP4yle+EqNHjz6iAwIAHEqTPs304IMPRn19fURETJo0Kbp06RKvvvpqXHzxxfH1r3/9iA4IAHAoTYqZTZs2NfipgrFjx8bYsWMjm83Gxo0bo1evXkdsQACAQ2nSaaY+ffrE1q1b91u+ffv26NOnz2EPBQDQWE2KmWw2G5lMZr/lNTU1UVxcfNhDAQA01kc6zVRZWRkREZlMJm655ZY47rjjcuvq6upiyZIlcdpppx3RAQEADuUjxczy5csj4vdHZt58881o27Ztbl3btm1j4MCBccMNNxzZCQEADuEjxcyLL74YEb//OPa9994bJSUlzTIUAEBjNenTTHPnzs39vWnTpoiIOOGEE47MRAAAH0GTLgCur6+P22+/PUpLS6N3797Ru3fv6NSpU9xxxx25758BAGgJTToyc9NNN8UjjzwS3/72t+Occ86JiIhXXnklbrvtttizZ0/ceeedR3RIAICDaVLMPProo/Hwww/HxRdfnFs2YMCA+KM/+qP4q7/6KzEDALSYJp1m2r59e/Tt23e/5X379s39AGVjvPzyyzFy5MgoKyuLTCYTzzzzTIP12Ww2pk6dGj179ox27drF0KFD46233mrKyADAUapJMTNw4MC4//7791t+//33x8CBAxu9n927d8fAgQNj1qxZB1z/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\n"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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UHp6uvbt26dly5Zp1apVmj17doPtnn32WU2YMEF79uxRXFycHnzwQT366KPKzMxUfn6+LMtqcBPVqqoq/ehHP9LmzZu1e/du3XnnnRo1apQKCwubzPLjH/9YpaWleu+991RQUKBBgwbp9ttv17Fjxzz2+eFhFuCFJk6caI0ePdoqLS21/P39raNHj1pHjx61AgICrLKyMmv06NHWxIkTz7tvWVmZJcnau3evZVmWdeTIEUuStXv3bsuyLOvZZ5+1Ro4c2WCfoqIiS5J14MABT34soM2bOHGi5evra3Xu3Nk13Xfffdbtt99uzZkzp8G2//3f/2317NnTNS/JevLJJ13zO3bssCRZK1ascC373e9+ZwUEBFwwQ9++fa2XXnrJNR8TE2PNnz/fsizL+stf/mIFBQVZNTU1Dfb5wQ9+YC1btuySPy+8gxGPM0D7FRYWprvuukurVq2SZVm66667dMUVVzTY5uDBg8rKytLOnTv13XffuUZkCgsL1a9fv0bH/PTTT/Xhhx+qS5cujdYdPnxY11xzjWc+DNBO3HbbbcrOznbNd+7cWfHx8dq2bVuDkZi6ujrV1NToxIkT6tSpkyQpPj7etf7cM/j69+/fYFlNTY0qKysVFBSkqqoqPfPMM/rjH/+o4uJinTlzRidPnmxyZObTTz9VVVWVQkNDGyw/efLkRU9Pw3tRZuD1Jk+e7BpWXrJkSaP1o0aNUkxMjJYvX67IyEjV19erX79+OnXq1HmPV1VVpVGjRun5559vtK5nz54tGx5ohzp37qzevXs3WFZVVaWZM2cqNTW10fYBAQGu1x07dnS9djgcTS4794+Wxx9/XJs2bdJ//dd/qXfv3goMDNR99913we9/z549tWXLlkbrQkJCmvcB4XUoM/B6d955p06dOiWHw6Hk5OQG677//nsdOHBAy5cv1y233CJJ+uijjy54vEGDBun3v/+9rrzySnXowFcAaA2DBg3SgQMHGpWcy7Vt2zY9/PDDuvfeeyWdLStHjx69YI6SkhJ16NBBV155ZYtmgX24ABhez9fXV/v379e+ffvk6+vbYF23bt0UGhqqV155RYcOHdKf//xnZWRkXPB4aWlpOnbsmMaNG6ddu3bp8OHD2rhxoyZNmqS6ujpPfhSg3crKytJvfvMbzZw5U1988YX279+v1atX68knn7ys41599dVat26d9uzZo08//VQPPvhgkxf/S1JSUpISExM1ZswYvf/++zp69Ki2b9+uGTNmKD8//7KywD6UGRghKChIQUFBjZb7+Pho9erVKigoUL9+/TR9+nS98MILFzxWZGSktm3bprq6Oo0cOVL9+/fXtGnTFBISIh8fvhKAJyQnJ+vdd9/V+++/rxtvvFFDhgzR/PnzFRMTc1nHffHFF9WtWzfddNNNGjVqlJKTkzVo0KAmt3c4HPrTn/6kYcOGadKkSbrmmmv0wAMP6H/+539c1+jAPA7Lsiy7QwAAALiLf4YCAACjUWYAAIDRKDMAAMBolBkAAGA0ygwAADAaZQYAABiNMgMAAIxGmQEAAEajzAAAAKNRZgAAgNEoMwC80tq1a9W/f38FBgYqNDRUSUlJqq6uliS9+uqr6tOnjwICAhQXF6elS5e69ps8ebLi4+NVW1srSTp16pQGDhyoCRMm2PI5AHgeZQaA1ykuLta4ceM0efJk7d+/X1u2bFFqaqosy9Lrr7+urKwszZ49W/v379ecOXP01FNP6bXXXpMkLVq0SNXV1fqP//gPSdKMGTNUXl6uxYsX2/mRAHhQB7sDAMA/Ki4u1pkzZ5Samup6qnL//v0lSU8//bR+9atfKTU1VZIUGxurffv2admyZZo4caK6dOmi3/72t7r11lvVtWtXLViwQB9++OF5n7oOoG3gqdkAvE5dXZ2Sk5P18ccfKzk5WSNHjtR9990nPz8/denSRYGBgfLx+dvA8pkzZxQcHCyn0+la9p//+Z+aO3eunnjiCc2bN8+OjwGglTAyA8Dr+Pr6atOmTdq+fbvef/99vfTSS5oxY4beeecdSdLy5cs1ePDgRvucU19fr23btsnX11eHDh1q1ewAWh/XzADwSg6HQ0OHDtXMmTO1e/du+fn5adu2bYqMjNTXX3+t3r17N5hiY2Nd+77wwgv68ssvlZubqw0bNmjlypU2fhIAnsbIDACvs3PnTm3evFkjR45Ujx49tHPnTpWVlalPnz6aOXOmHnvsMQUHB+vOO+9UbW2t8vPz9de//lUZGRnavXu3srKytHbtWg0dOlQvvvii0tPTdeutt+qqq66y+6MB8ACumQHgdfbv36/p06frk08+UWVlpWJiYjR16lRNmTJFkpSTk6MXXnhB+/btU+fOndW/f39NmzZNKSkpSkhI0M0336xly5a5jjd69Gh999132rp1a4PTUQDaBsoMAAAwGtfMAAAAo1FmAACA0SgzAADAaJQZAABgNMoMAAAwGmUGAAAYjTIDAACMRpkBAABGo8wAAACjUWYAAIDRKDMAAMBolBkAAGC0/w/XI5TNiJKZZAAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import re\n",
        "\n",
        "cep = '72235-500'\n",
        "cep2 = r'[\\d]{5}-[\\d]{3}'\n",
        "if re.match(cep2, cep):\n",
        "  print(True)\n",
        "else:\n",
        "  print(False)  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WYHNtamM2KNd",
        "outputId": "9f642a1b-5653-4aa7-c297-142bdaa01ae4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import plotly.express as px\n",
        "import ipywidgets as widgets\n",
        "\n",
        "# carregar o conjunto de dados \"gapminder\"\n",
        "df = px.data.gapminder()\n",
        "\n",
        "# criar o gráfico de dispersão com Plotly Express\n",
        "fig = px.scatter(df, x=\"gdpPercap\", y=\"lifeExp\", size=\"pop\", color=\"continent\",\n",
        "                 hover_name=\"country\", log_x=True, size_max=60)\n",
        "\n",
        "# criar um slider de ano\n",
        "slider = widgets.IntSlider(min=df[\"year\"].min(), max=df[\"year\"].max(), step=1, value=df[\"year\"].min())\n",
        "\n",
        "# definir uma função para atualizar o gráfico com base no valor do slider\n",
        "def update_plot(year):\n",
        "    # filtrar o conjunto de dados para o ano selecionado\n",
        "    df_year = df[df[\"year\"] == year]\n",
        "    \n",
        "    # atualizar os dados do gráfico\n",
        "    fig.data[0].x = df_year[\"gdpPercap\"]\n",
        "    fig.data[0].y = df_year[\"lifeExp\"]\n",
        "    fig.data[0].marker.size = df_year[\"pop\"] / 1e6\n",
        "    \n",
        "    # atualizar o título do gráfico com o ano selecionado\n",
        "    fig.update_layout(title=f\"GDP per Capita vs. Life Expectancy ({year})\")\n",
        "    \n",
        "    # exibir o gráfico\n",
        "    fig.show()\n",
        "\n",
        "# conectar o slider à função de atualização\n",
        "widgets.interact(update_plot, year=slider)"
      ],
      "metadata": {
        "id": "yJT9suZoK2Kq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#CRIPTOGRAFIA COM AES\n",
        "from cryptography.fernet import Fernet\n",
        "from getpass import getpass\n",
        "\n",
        "def aes_encrypt(message, key):\n",
        "    f = Fernet(key)\n",
        "    encrypted_message = f.encrypt(message.encode())\n",
        "    return encrypted_message\n",
        "\n",
        "def aes_decrypt(encrypted_message, key):\n",
        "    f = Fernet(key)\n",
        "    decrypted_message = f.decrypt(encrypted_message)\n",
        "    return decrypted_message.decode()\n",
        "\n",
        "mensagem_original = getpass(\"Digite a mensagem que deseja criptografar: \")\n",
        "chave = Fernet.generate_key()\n",
        "\n",
        "mensagem_criptografada = aes_encrypt(mensagem_original, chave)\n",
        "print(\"Mensagem criptografada:\", mensagem_criptografada)\n",
        "\n",
        "mensagem_descriptografada = aes_decrypt(mensagem_criptografada, chave)\n",
        "print(\"Mensagem descriptografada:\", mensagem_descriptografada)"
      ],
      "metadata": {
        "id": "K7FTDt2dl3Sf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "i = 0\n",
        "while i <= 3:\n",
        "  i+=2\n",
        "  print(\"*\")"
      ],
      "metadata": {
        "id": "XpOtBu3kIVqT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "''' O código irá imprimir a lista [1, 2, 3] quatro vezes, pois o loop for será \n",
        "executado 4 vezes devido ao uso do operador de deslocamento de bits << que multiplica o valor de len(lista) por 2 elevado a 2 (ou seja, 4).\n",
        "\n",
        "No primeiro ciclo do loop, i será igual a 0 e a lista [1, 2, 3] será impressa.\n",
        "No segundo ciclo, i será igual a 1 e a lista [1, 2, 3] será impressa novamente. \n",
        "O loop continuará a executar até que i seja igual a 11 (pois len(lista) é igual \n",
        "a 3 e multiplicado por 4 dá 12, mas como a contagem começa em 0, o loop terminará quando i for igual a 11).\n",
        "No entanto, como a lista é sempre a mesma e não há nenhuma mudança sendo feita na mesma dentro do loop, \n",
        "o resultado será apenas a impressão da lista [1, 2, 3] quatro vezes.\n",
        "'''\n",
        "#lista = [1,2,3]\n",
        "#for i in range(len(lista)<<50):\n",
        "  #print(lista,i)\n",
        "\n",
        "#for i in range(10<<10):\n",
        "  #print('@',i)  \n",
        "\n",
        "b = bin((10^2)*10)\n",
        "\n",
        "print(b[2:])\n",
        "\n"
      ],
      "metadata": {
        "id": "ODlww9kAIsfC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a = bin(14)\n",
        "b = a[2:]\n",
        "print(b)\n",
        "\n",
        "14 >> 9 "
      ],
      "metadata": {
        "id": "-seIfWPJugga"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from random import randint\n",
        "\n",
        "def gerar_ISBN():\n",
        "  isbn = \"9\"\n",
        "  print(isbn, end='')\n",
        "\n",
        "  for i in range(12):\n",
        "    isbn += str(randint(0,9))\n",
        "    print(isbn[-1], end='')\n",
        "\n",
        "  return isbn\n",
        "\n",
        "def validar_ISBN13(isbn):\n",
        "  if len(isbn) != 13:\n",
        "    return False\n",
        "\n",
        "  soma = 0\n",
        "  for i in range(12):\n",
        "    if i % 2 == 0:\n",
        "      soma += int(isbn[i])\n",
        "    else:\n",
        "      soma += 3 * int(isbn[i])\n",
        "\n",
        "  verif = (10 - (soma % 10)) % 10\n",
        "\n",
        "  return int(isbn[12]) == verif\n",
        "\n",
        "# exemplo de uso\n",
        "isbn = gerar_ISBN()\n",
        "if validar_ISBN13(isbn):\n",
        "  print(\"\\nO ISBN-13\", isbn, \"é válido\")\n",
        "else:\n",
        "  print(\"\\nO ISBN-13\", isbn, \"é inválido\")"
      ],
      "metadata": {
        "id": "Vmn9kW9_xvV0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from itertools import permutations\n",
        "\n",
        "\n",
        "\n",
        "list1 = [\"A\", \"B\", \"C\"]\n",
        "\n",
        "print(len(list(permutations(list1, 3))))"
      ],
      "metadata": {
        "id": "DbuxBe5rrKQp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'''palavra = \"A screaming comes across the sky.\"\n",
        "nova = palavra.replace('s','$')\n",
        "print(nova)\n",
        "\n",
        "p = \"Hemingway\"\n",
        "p2= p.find('m')\n",
        "print(p2)\n",
        "\n",
        "string = 'O um anel para todos dominar'\n",
        "print(string)\n",
        "\n",
        "concatenacao = 't'+'h'+'r'+'e'+'e','t'+'h'+'r'+'e'+'e','t'+'h'+'r'+'e'+'e'\n",
        "multi =('Three '*3)\n",
        "print(multi)\n",
        "print(concatenacao)\n",
        "fatiar = \"It was a bright cold day in April, and the clocks were striking thirteen.\"\n",
        "novaFatiar = fatiar[:34]\n",
        "print(novaFatiar)\n",
        "\n",
        "palavra= 'camus'\n",
        "print(palavra[0])\n",
        "print(palavra[1])\n",
        "print(palavra[2])\n",
        "print(palavra[3])\n",
        "print(palavra[4])\n",
        "\n",
        "frase =  ('Yesterday I wrote a [resposta_um]. I sent it to [resposta_dois]!')\n",
        "\n",
        "r1 = input('Digite a resposta 1: ')\n",
        "r2 = input('Digite a resposta 2: ')\n",
        "novaFrase = (f'Yesterday I wrote a {r1}. I sent it to {r2}!')\n",
        "print(novaFrase)\n",
        "\n",
        "frase2 = \"aldous Huxley was born in 1894.\"\n",
        "maiuscula = frase2.capitalize()\n",
        "print(maiuscula)\n",
        "\n",
        "lista =[\"The\", \"fox\", \"jumped\", \"over\", \"the\", \"fence\", \".\"]\n",
        "correta = ' '.join(lista).replace(' .','.')\n",
        "print(correta)\n",
        "\n",
        "lst = \"Where now? Who now? When now?\".split(\"?\")\n",
        "print(lst)'''\n"
      ],
      "metadata": {
        "id": "IM9bQSgG0ZYr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Usando for para deixar tudo maiusculo:\n",
        "\n",
        "lista = 'A medalha foi dada a ele'\n",
        "\n",
        "for i in lista:\n",
        "  x = lista.upper()\n",
        "print(x)"
      ],
      "metadata": {
        "id": "yrWv28R28URC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "name = ['davi','pedro','maria']\n",
        "for i in name:\n",
        "  print(i)\n",
        " \n"
      ],
      "metadata": {
        "id": "5Dp592Ch8UXC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "mLJonOLO-Ybc"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}