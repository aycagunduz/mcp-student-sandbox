# Modüler fonksiyonlar: Her biri tek sorumluluk

def apply_markup(value, markup_percent=15):
    """Tek sorumluluk: Değere markup uygula"""
    return value * (1 + markup_percent / 100)

def format_currency(value):
    """Tek sorumluluk: Para birimi formatı uygula"""
    return f"Total: {value:.2f}"

def log_result(result, filename="log.txt"):
    """Tek sorumluluk: Sonucu dosyaya logla"""
    with open(filename, "a") as f:
        f.write(str(result) + "\n")

def process_data(data, print_output=True):
    """Ana fonksiyon: Küçük fonksiyonları orchestrate et"""
    results = [apply_markup(d) for d in data]

    if print_output:
        for result in results:
            print(format_currency(result))

    log_result(results)
    return results
