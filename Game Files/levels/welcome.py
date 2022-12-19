from bearlibterminal import terminal as blt
from pygame import mixer

#TODO alguma tabela para as possiveis paginas que podem ser escritas no 'pag' senão seria muitos IF/ELIF;
#TODO otimizar o jeito que a tela eh desenhada pq ficou estranho do jeito que tá;
#TODO jeito melhor de animar a interface (arte/relogio)
#TODO arrumar o bkcolor que se mantem entre as paginas

def saudacao():
    #blt.open()
    blt.set('window.size=75x35')
    blt.bkcolor('black')
    """
    mixer.music.fadeout(2000)
    #mixer.music.stop()
    mixer.music.load('bgm\Ambient1.ogg')
    mixer.music.set_volume(0.8)
    mixer.music.play()
    """
    blt.printf(6, 0, '[color=#695bd4]RELITEX   << 100 >>   SEGUNDA-FEIRA - 04 DE ABRIL, 1994  22:13H[/color]')

    blt.printf(3, 1, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 2, '[color=#bad7ff]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 3, '[color=#96b4dd]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 4, '[color=#708db4]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 5, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')

    blt.printf(3, 6, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 7, '[color=#bad7ff]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 8, '[color=#96b4dd]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 9, '[color=#708db4]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 10, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')

    blt.printf(3, 11, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 12, '[color=#bad7ff]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 13, '[color=#96b4dd]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉ BEM-VINDO(A) AO RELITEX ▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 14, '[color=#708db4]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 15, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')

    blt.printf(3, 16, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 17, '[color=#bad7ff]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 18, '[color=#96b4dd]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 19, '[color=#708db4]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 20, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')

    blt.printf(3, 21, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 22, '[color=#bad7ff]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 23, '[color=#96b4dd]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 24, '[color=#708db4]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 25, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')

    blt.printf(3, 26, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 27, '[color=#bad7ff]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 28, '[color=#96b4dd]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 29, '[color=#708db4]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 30, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 31, '[color=#ececec]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
    blt.printf(3, 32, '[color=#bad7ff]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')

    blt.color('#d6945e')
    blt.print(3, 33, "USE AS SETAS OU DIGITE O NÚMERO DO CANAL PRESSIONANDO 'S' ")
    blt.refresh()

    while True:
        blt.delay(800)
        blt.printf(3, 15, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉ SUA REDE DE INFORMAÇÕES VIA TELETEXTO ▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(6, 0, '[color=#695bd4]RELITEX   << 100 >>   SEGUNDA-FEIRA - 04 DE ABRIL, 1994  22:14H[/color]')
        blt.refresh()
        blt.delay(800)
        blt.printf(3, 15, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]')
        blt.printf(6, 0, '[color=#695bd4]RELITEX   << 100 >>   SEGUNDA-FEIRA - 04 DE ABRIL, 1994  22:13H[/color]')
        blt.refresh()

        blt.printf(3, 15, '[color=#5d6f87]Y▉Y▉Y▉Y▉Y▉Y▉Y▉Y▉ SUA REDE DE INFORMAÇÕES VIA TELETEXTO ▉Y▉Y▉Y▉Y▉Y▉Y▉Y[/color]') 
        blt.refresh()

        if blt.has_input():

          key = blt.read()
    
          if key == blt.TK_LEFT:
            blt.print(30, 34, "VOCE APERTOU: <")
            blt.refresh()
            blt.delay(1500)
            saudacao()

          elif key == blt.TK_RIGHT:
            blt.print(30, 34, "VOCE APERTOU: >")
            blt.refresh()
            blt.delay(1500)
            from levels.weather import clima
            blt.clear()
            clima()

          elif key == blt.TK_S:
            blt.print(3, 34, "> ")
            rc, pag = blt.read_str(4, 34, "", 5)

            match pag:
                case 100:
                    saudacao()

                case 101:
                    blt.refresh()
                    blt.delay(500)
                    blt.clear()
                    from levels.weather import clima
                    blt.clear()
                    clima()

                case _:
                    blt.print(1,3, "ERROR")
                    blt.refresh()
                    blt.delay(500) 
                    clima() 

          elif key in (blt.TK_CLOSE, blt.TK_ESCAPE):      
            exit()

          else:
            saudacao()

if __name__ == "__main__": 
    saudacao() 