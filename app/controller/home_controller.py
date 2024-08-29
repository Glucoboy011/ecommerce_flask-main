from flask import Blueprint, render_template
from app.model.category import Category
from app.model.product import Product

home_bp = Blueprint('home', __name__)

categories = [Category(1, "Bandeiras de Estados"), Category(2, "Bandeiras de Países"), Category(3, "Bandeiras de Cidades e Clubes Esportivos "), Category(4, "Símbolos e Brasões")]
products = [
    Product(1, "Bandeira do Acre", 35.99, 1, "1.35x1.93m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-acre-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-acre-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-acre-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-acre-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-acre-reta.jpg",
    ]),
    Product(2, "Bandeira do Afeganistão", 55.99, 2, "Tamanho 1.80x2.56m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-afeganistao-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-afeganistao-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-afeganistao-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-afeganistao-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-afeganistao-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/paises/bandeira-paises-afeganistao-reta.jpg",
    ]),
    Product(3, "Bandeira do Rio Grande do Sul", 35.99, 1, "Tamanho 1.35x1.93m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-grande-do-sul-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-grande-do-sul-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-grande-do-sul-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-grande-do-sul-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-grande-do-sul-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-rio-grande-do-sul-reta.jpg",
    ]),
    Product(4, "Bandeira do Estado de São Paulo", 35.99, 1, "Tamanho 1.35x1.93m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-sao-paulo-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-sao-paulo-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-sao-paulo-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-sao-paulo-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-sao-paulo-reta.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/estados/bandeira-estado-sao-paulo-reta.jpg",
    ]),
    Product(5, "Bandeira Oficial do Brasil - Modelo Bordado em Cetim", 69.99, 2, "Tamanho 2.25x3.20m", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/brasil/bandeira-brasil-cetim-bordada.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/brasil/bandeira-brasil-cetim-bordada.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/brasil/bandeira-brasil-cetim-bordada.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/brasil/bandeira-brasil-cetim-bordada.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/brasil/bandeira-brasil-cetim-bordada.jpg",
        "https://www.bandeira1.com.br/lojas/00002028/prod/brasil/bandeira-brasil-cetim-bordada.jpg",
    ]),
    Product(6, "Bandeiras de Municípios Brasileiros", 179.99, 3, "Diversos Tamanhos", [
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-municipios.jpg?cccfc=2d4c0e6e",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-municipios.jpg?cccfc=2d4c0e6e",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-municipios.jpg?cccfc=2d4c0e6e",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-municipios.jpg?cccfc=2d4c0e6e",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-municipios.jpg?cccfc=2d4c0e6e",
        "https://www.bandeira1.com.br/lojas/00002028/prod/diversas/bandeiras-diversas-municipios.jpg?cccfc=2d4c0e6e",
    ])
]

@home_bp.route('/')
def home():
    return render_template('index.html', categories=categories, products=Product.all_products)
