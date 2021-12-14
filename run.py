"""
    Renders pages with books cards and creates local server on http://127.0.0.1:5500
    (http://127.0.0.1:5500/pages/index1.html to see first page)
"""
# -*- coding: utf-8 -*-
from pathlib import Path
from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked

import json

with open('data.json', 'r', encoding='cp1251') as fh:
    json_dicts = json.load(fh)


def on_reload():
    """
        Function that renders pages by template
    """
    env = Environment(loader=FileSystemLoader('.'), autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('template.html')
    
    Path("pages").mkdir(parents=True, exist_ok=True)

    amount_of_books_per_page = 10    
    pages_at_all = len(list(chunked(json_dicts, amount_of_books_per_page)))

    if pages_at_all > 10:
        for index, books_packages in enumerate(list(chunked(json_dicts, amount_of_books_per_page)), start=1):

            if index <= 5:
                paginator_left_index = 1
                paginator_right_index = 11
            elif index >= pages_at_all - 5:
                paginator_right_index = pages_at_all
                paginator_left_index = pages_at_all - 10
            else:
                paginator_left_index = index - 5
                paginator_right_index = index + 5

            books_by_cols = list(chunked(list(books_packages), 2))
            rendered_page = template.render(books_data=books_by_cols, page_number=index,
                                            pages_at_all=pages_at_all, r=paginator_right_index, l=paginator_left_index)

            with open(f"pages/index{index}.html", 'w', encoding="utf8") as file:
                file.write(rendered_page)

        print("Site rebuilt")

    else:
        for index, books_packages in enumerate(list(chunked(json_dicts, amount_of_books_per_page)), start=1):

            paginator_right_index = pages_at_all
            paginator_left_index = 1

            books_by_cols = list(chunked(list(books_packages), 2))
            rendered_page = template.render(books_data=books_by_cols, page_number=index,
                                            pages_at_all=pages_at_all, r=paginator_right_index, l=paginator_left_index)

            with open(f"pages/index{index}.html", 'w', encoding="utf8") as file:
                file.write(rendered_page)

        print("Site rebuilt")




def main():
    """
        Runs on_reload
        Constantly checks for changes in template file , if there are some runs on_reload() again
    """
    on_reload()
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')


if __name__ == '__main__':
    main()
