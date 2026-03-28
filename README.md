# Mystery Module

## Amaç
`mystery_module.py`, ikinci dereceden denklem için kökleri hesaplayan yardımcı bir modüldür. Benzin: `a`, `b`, `c` parametrelerine göre diskriminant hesaplar, karmaşık kökler yerine `None` döner. Kodun amacı, matematiksel çözümleyici işlevini basit, test edilebilir ve tekrar kullanılabilir biçimde sunmaktır.

## Fonksiyonlar

### `fn_x(a, b, c)`

- `a` (float veya int): x^2 katsayısı. `a` sıfır olursa bu fonksiyon ikinci derece denklem koşulunu sağlamaz.
- `b` (float veya int): x katsayısı.
- `c` (float veya int): sabit terim.

Fonksiyon, köklerin hesaplanması için diskriminantı `d = b**2 - 4*a*c` olarak alır.

- `d < 0` olduğunda: kökler reel olmadığından `None` döner.
- `d >= 0` olduğunda: `(x1, x2)` biçiminde iki kök tuple'ı döner.

**Dönüş değeri**
- `None` veya `(x1, x2)`

## Kullanım Örnekleri

```python
from mystery_module import fn_x

# 2x^2 + 3x - 2 = 0
result = fn_x(2, 3, -2)
print(result)  # (0.5, -2.0)

# reel kök yoksa
no_real = fn_x(1, 0, 1)
print(no_real)  # None
```

## Katkıda Bulunma
- `a` değerini kontrol et, gerekirse `ValueError` ekle.
- Karmaşık kökler için `complex` destekleyici bir alternatif ekle.
- Birim testleri `pytest` ile yaz ve `tests/test_mystery_module.py` olarak sakla.

## Notlar
- Bu modül, bir matematik altyapısı ya da giriş doğrulaması içermez. Üst katmanda parametrelerin uygunluğunu sağlamak önerilir.
