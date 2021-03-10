# InfoDeDateas

La página web [Dateas](https://www.dateas.com/) recopila información de personas en Argentina.

InfoDeDateas utiliza un archivos de excel con nombres de personas para buscarlos individualmente en Dateas y obtener su número de CUIL. Luego los guarda ordenadamente en una copia de dicho excel.

## Prerequisitos

Antes de empezar, asegúrese de cumplir con los siguientes requisitos:

* Python 3 o superior.
* Módulo [Requests](https://pypi.org/project/requests/) para Python.

```
            pip install requests
```
* Módulo [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/) para Python.
 
```
            pip install beautifulsoup4
```

## Instación de InfoDeDateas

Para instalar InfoDeDateas, siga los siguientes pasos:

* Descargue InfoDeDateas.py
* Cambie la ruta del archivo excel a utilizar:
```python
    wb = openpyxl.load_workbook(r'c:\users\Mariano\desktop\Nombres.xlsx') #Path de un excel con lista de nombres
```

## Uso de InfoDeDateas

* Asegúrese de tener acceso a internet.
* Corra el programa InfoDeDateas.py en su computadora.
* Automáticamente va a obtener informacion de www.dateas.com y guardarla en un excel al finalizar. La ruta del nuevo archivo excel va a ser su [CWD](https://linuxize.com/post/python-get-change-current-working-directory/#:~:text=To%20find%20the%20current%20working,chdir(path)%20), el cual es sencillo de obtener o cambiar (véase [python get change current working directory](https://linuxize.com/post/python-get-change-current-working-directory/#:~:text=To%20find%20the%20current%20working,chdir(path)%20) para mas detalles).


## Contacto

Puede contactarme mediante mi dirección de email, Mariano_Desivo@hotmail.com.

## License

Este proyecto usa la siguiente licencia: [MIT License](https://github.com/MarianoDesivo/InfoDeDateas/blob/main/LICENSE).
