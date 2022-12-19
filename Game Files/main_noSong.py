from bearlibterminal import terminal as blt
from pygame import mixer
from intro import intro

# abre o blt e o configura: se pode ser arrastado, o titulo da janela e de onde vem o input
blt.open()
blt.set("""
    window.resizeable=false;
    window.title='TELETEXT - CRIME';
    input: filter={keyboard};
""")

def main_menu():
    blt.clear()
    blt.set('window.size=75x36')
    blt.refresh()
    blt.color('#fff4e6')  ##ff73da

    # Pega a arte do arquivo .txt e printa
    f = open('res\menu.txt', 'r', encoding="utf-8")
    r = f.read()
    blt.print(1, 1, '' + r)

    blt.refresh()
    blt.color('#6fcb9f')   ##73bbff
    blt.printf(35, 16, '[color=#fb2e01]CRIME[/color]')
    blt.print(30,1, '* MENU PRINCIPAL *')
    blt.printf(30, 34, "by Pedro Ivo, 2022")
    blt.printf(1, 1, " ")
    blt.refresh()

    # Lê qual tecla o usuario apertou
    key = blt.read()

    if key == blt.TK_1:
        f = open('res\menuFADE.txt', encoding='utf-8')
        r = f.read()
        blt.clear()
        blt.color('gray')
        blt.printf(1, 1, '' + r)
        blt.print(1, 1, " ")
        blt.refresh()
        blt.delay(1000)

        f = open('res\menuFADE.txt', encoding='utf-8')
        r = f.read()
        blt.clear()
        blt.color('#171717')
        blt.printf(1, 1, '' + r)
        blt.print(1, 1, " ")
        blt.refresh()
        blt.delay(1000)

        blt.clear()
        blt.refresh()
        blt.delay(1000)
        from levels.welcome import saudacao
        saudacao()

    elif key == blt.TK_2:
        blt.print(30, 35, "VOCE APERTOU: 2 - Carregar (WORK IN PROGRESS)")
        blt.refresh()
        blt.delay(1000)
        blt.close()

    elif key == blt.TK_3:
        from howtoplay import tutorial
        blt.clear()
        tutorial()

    elif key == blt.TK_4:
        blt.print(30, 35, "VOCE APERTOU: 4 - CREDITOS (WORK IN PROGRESS)")
        blt.refresh()
        blt.delay(1000)
        blt.close()

    elif key in (blt.TK_CLOSE, blt.TK_ESCAPE, blt.TK_5):      
        blt.close()
        exit()

    else:
        main_menu()


if __name__ == "__main__": 
    main_menu() 