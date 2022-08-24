from pprint import pprint
import hashlib


# Генератор
def my_generator(txt_file):
    with open(txt_file, 'r', encoding="utf-8") as origin:
        # Собственно простое построечное открытие
        for row in origin:
            yield row.strip()


if __name__ == '__main__':
    # Собственно сам генератор
    for line in my_generator('countries_links.txt'):
        with open('countries_links_hashed.txt', 'a') as modified:
            modified.write(f'{hashlib.md5(line.encode("utf-8")).hexdigest()}\n')
