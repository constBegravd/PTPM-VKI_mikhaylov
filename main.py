import logging
import sys

# Шаблон строки лога (аналог template в Serilog)
# Содержит: время, уровень (до 7 символов для выравнивания), имя логгера и сообщение
log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

# Базовая настройка корневого логгера
logging.basicConfig(
    level=logging.DEBUG, # Минимальный уровень логирования (аналог MinimumLevel.Debug)
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout),          # Настройка логирования в консоль
        logging.FileHandler("logs/file_txt.log", encoding="utf-8") # Настройка логирования в файл
    ]
)

error_num = [(-1, -1), (-1, -1), (-1, -1)]
error_non_num = [(-2, -2), (-2, -2), (-2, -2)]

def triangle(a, b, c):
    logging.info(f"a: {a}, b: {b}, c: {c}")

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except:
        logging.exception("нечисловые данные")
        return "", error_non_num

    if min(a, b, c) <= 0:
        logging.exception("числа должны быть положительными")
        return "", error_num
    
    if not (a + b > c and a + c > b and b + c > a):
        logging.exception("нарушено неравенство")
        return "", error_num

    if a == b and b == c:
        t = "равносторонний"
    elif a == b or b == c or c == a:
        t = "равнобедренный"
    else:
        t = "разносторонний"
        
    x = (b ** 2 + a ** 2 - c ** 2) / (2 * a)
    y = (b ** 2 - x ** 2) ** 0.5
    verts = [
        (0, 0),
        (a, 0),
        (x, y)
    ]
    
    return t, verts

logging.info("Логгер успешно сконфигурирован")
logging.info("Приложение запущено")

if __name__ == "__main__":
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    
    t, cords = triangle(a, b, c)
    print(t, cords)
