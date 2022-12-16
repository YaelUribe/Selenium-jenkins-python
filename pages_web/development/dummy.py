import json
import os
from pages_web.development.base_page import BasePage

lista = {"time_1": "300P", "time_2": "315P", "time_3": "330p", "time_4": "345p"}
for i in lista:
    print("Selected time {}: {}".format(i, lista[i]))

