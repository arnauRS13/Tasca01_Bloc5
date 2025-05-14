import pytest
from Prova_Escrita_05 import llibres_per_categoria, esta_disponible, usuari_te_prestecs, dies_prestec_total

# Definim la biblioteca d'exemple per als tests
biblioteca = [
    {
        "llibre": "El Quixot",
        "autor": "Cervantes",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Joan", "dies": 15, "retornat": True},  # Préstec retornat
            {"usuari": "Maria", "dies": 20, "retornat": False},  # Préstec no retornat
            {"usuari": "Pere", "dies": 12, "retornat": True}  # Préstec retornat
        ]
    },
    {
        "llibre": "1984",
        "autor": "Orwell",
        "categoria": "ciència-ficció",
        "prestecs": [
            {"usuari": "Pere", "dies": 10, "retornat": True},  # Préstec retornat
            {"usuari": "Anna", "dies": 25, "retornat": True},  # Préstec retornat
            {"usuari": "Marta", "dies": 18, "retornat": False}  # Préstec no retornat
        ]
    },
    {
        "llibre": "El Senyor dels Anells",
        "autor": "Tolkien",
        "categoria": "fantasia",
        "prestecs": [
            {"usuari": "Maria", "dies": 30, "retornat": True},  # Préstec retornat
            {"usuari": "Joan", "dies": 22, "retornat": True},  # Préstec retornat
            {"usuari": "Pere", "dies": 15, "retornat": False}  # Préstec no retornat
        ]
    },
    {
        "llibre": "Crim i Càstig",
        "autor": "Dostoievski",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Anna", "dies": 28, "retornat": True},  # Préstec retornat
            {"usuari": "Marta", "dies": 14, "retornat": True},  # Préstec retornat
            {"usuari": "Joan", "dies": 21, "retornat": True}  # Préstec retornat
        ]
    }
]


# Test per llibres_per_categoria
@pytest.mark.parametrize(
    "categoria, esperat",
    [
        ("novel·la", ["El Quixot", "Crim i Càstig"]),  # LLibres de novela
        ("ciència-ficció", ["1984"]),  # Llibres de ciencia ficcio
        ("fantasia", ["El Senyor dels Anells"]),  # Llibres de fantasia
        ("poesia", []),  # Si no hi ha llibres hauria de retornar una llista buida
    ]
)
def test_llibres_per_categoria(categoria, esperat):
    """
    Aquesta funcio comprova si la funcio 'llibres_per_categoria' torna els llibres correctes 
    per la categoria donada.
    """
    # Comprovem que la funcio retorna els llibres correctes
    assert llibres_per_categoria(biblioteca, categoria) == esperat


# Test per esta_disponible
@pytest.mark.parametrize(
    "llibre, esperat",
    [
        ("El Senyor dels Anells", False),  # LLibre no disponible, prestec no retornat
        ("El Quixot", False),  # Hi ha un prestec no retornat
        ("1984", False),  # LLibre no disponible, prestec no retornat
        ("Crim i Càstig", True),  # Tots els prestecs retornats
    ]
)
def test_esta_disponible(llibre, esperat):
    """
    Aquesta funcio comprova si la funcio 'esta_disponible' torna si el llibre esta disponible o no
    per ser prestat, tenint en compte els seus préstecs.
    """
    # Comprovem si el llibre esta disponible
    assert esta_disponible(biblioteca, llibre) == esperat


# Test per usuari_te_prestecs
@pytest.mark.parametrize(
    "usuari, esperat",
    [
        ("Pere", True),  # L'usuari te un prestec no retornat
        ("Joan", False),  # L'usuari no te prestec pendent
        ("Maria", True),  # L'usuari te un prestec no retornat
        ("Anna", False),  # L'usuari no te prestec pendent
    ]
)
def test_usuari_te_prestecs(usuari, esperat):
    """
    Aquesta funcio comprova si un usuari té algun préstec pendent de retornar.
    """
    # Comprovem si un usuari te prestecs pendents
    assert usuari_te_prestecs(biblioteca, usuari) == esperat


# Test per dies_prestec_total
@pytest.mark.parametrize(
    "llibre, esperat",
    [
        ("El Senyor dels Anells", 67),  # 30 + 22 + 15 (dies totals de prestec)
        ("1984", 53),  # 10 + 25 + 18 (dies totals de prestec)
        ("El Quixot", 47),  # 15 + 20 + 12 (dies totals de prestec)
        ("Crim i Càstig", 63),  # 28 + 14 + 21 (dies totals de prestec)
    ]
)
def test_dies_prestec_total(llibre, esperat):
    """
    Aquesta funcio comprova si la funcio 'dies_prestec_total' torna la suma total de dies 
    que un llibre ha estat prestat, tenint en compte tots els seus préstecs.
    """
    # Comprovem que la suma de dies de préstec es correcta
    assert dies_prestec_total(biblioteca, llibre) == esperat


# Si es volen executar les proves
if __name__ == "__main__":
    pytest.main()
