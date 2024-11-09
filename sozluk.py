import json
# Sözlük dosyasının adı
sozluk_dosya_adi = "sozluk.json"


def levenshtein_distance(str1: str, str2: str) -> int:
    """
    Calculate the Levenshtein distance between two strings.

    The Levenshtein distance is the minimum number of single-character edits 
    (insertions, deletions, or substitutions) required to change one string into another.

    Args:
        str1 (str): First string to compare
        str2 (str): Second string to compare

    Returns:
        int: The Levenshtein distance between str1 and str2
    """
    # Create matrix of size (len(str1) + 1) x (len(str2) + 1)
    matrix = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    # Initialize first row and column
    for i in range(len(str1) + 1):
        matrix[i][0] = i
    for j in range(len(str2) + 1):
        matrix[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            matrix[i][j] = min(
                matrix[i - 1][j] + 1,  # deletion
                matrix[i][j - 1] + 1,  # insertion
                matrix[i - 1][j - 1] + substitution_cost  # substitution
            )

    return matrix[len(str1)][len(str2)]


def sozluk_yukle():
    try:
        with open(sozluk_dosya_adi, 'r') as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return {}


def sozluk_kaydet(sozluk_dict):
    with open(sozluk_dosya_adi, 'w') as dosya:
        json.dump(sozluk_dict, dosya)


def yanit_ver(mesaj):
    yanitlar = {
        "neden":"Kaplumbağa deden. Başka bir konuda yardımcı olabilir miyim?",
        "güzel":"Teşekkürler. Başka bir konuda yardımcı olabilir miyim?",
        "yor musun?":"Maalesef hayır",
        "gıcık": "Üzgünüm, gelebilecek en yakın cevabı bulmaya çalışıyorum sadece 🤷‍♂️",
        "": "Lütfen düzgün bir mesaj yazın.",
        "merhaba": "Merhaba! Size nasıl yardımcı olabilirim?",
        "nasılsın": "Ben bir yapay zekayım, duygularım yok ama buradayım!",
        "güle güle": "Hoşça kal! Umarım tekrar görüşürüz.",
        "sa": "Aleyküm Selam",
        "güncellemeler": "Mesaj limitim 10'a çıkarıldı, sozlük.py geliştirildi ve yanıt yazma animasyonu geldi.",
        "yok": "Tamam.",
        "çok konuda yardımcı olabilirsin": "Mesela hangi konularda?",
        "bence harika": "Teşekkürler. Başka bir konuda yardımcı olabilir miyim?",
        "olur": "Veya başka bir şey hakkında konuşabiliriz. Mesela: BasicAİ hakkındaki düşünceleriniz nelerdir?",
        "neden": "Kaplumbağa Deden",
        "bilmem": "Tamam bir daha ki ne öğrenerek gelin. Başka bir konuda yardımcı olabilir miyim?",
        "hmmm":"Bir şey düşünüyorsunuz gibi görünüyor. Yardımcı olabileceğim bir konu var mı?",
        "berbat":"Üzgünüm. Başka bir konuda yardımcı olabilir miyim?",
        "yeter":"...",
    }
    en_iyi_yanit = min(yanitlar.keys(), key=lambda y: levenshtein_distance(mesaj.lower(), y))
    return yanitlar.get(en_iyi_yanit)
    # return yanitlar.get(mesaj.lower(), "Henüz bu soru karşısında eğitilmedim. Geri bildiriminizi Ali Galip'e yapınız")


if __name__ == "__main__":
    # Ana menüyü burada başlat
    pass
