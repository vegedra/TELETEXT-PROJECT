from bearlibterminal import terminal as blt
from pygame import mixer

def clima():
    #blt.open()
    blt.set('window.size=75x35')
    blt.color('black')
    blt.printf(5, 0, '[color=yellow]RELITEX   << 101 >>   SEGUNDA-FEIRA - 04 DE ABRIL, 1994  22:13H[/color]')
    blt.bkcolor('#73a8d1')
    blt.printf(1, 1, """
                                                                        
                                                                        
                                                                        
                                                                        
                                       ▒▒▒▒▒▒                           
                                ▒▒     ▒▒▒▒▒▒            ▒▒▒▒▒▒▒▒       
                              ▒▒▒▒▒    ▒▒▒▒▒▒      ▒▒▒   ▒▒▒▒▒▒▒▒       
         ▒▒▒▒        ▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒     ▒▒
      ▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒  ▒▒▓▓▓▒▒▒     ▒▒
      ▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒  ▓▓▓▓▓▓▓▒     ▒▒
      ▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒▒▒  ▓▓ ▓ ▓▓▒     ▒▒
▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒
▒▒▒   ▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓ ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓ ▓ ▓▓▒▓▓▓▓▒▒▒
▒▒▒░░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▒▓▓ ▓▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓ ▓▒▒▒▒▓▓▒▒▒▒▒▓▓ ▓ ▓ ▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▒▒▒
▒▒▒▒▓▓▓▒▒▒▒▓▓ ▓▓ ▓▓▓▓  ▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓  ▓ ▓ ▓▒▒▒▒▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▓▓ ▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
                                                                        
""")
    blt.printf(1, 29, '[color=white] CLIMA DE HOJE: NUBLADO COM SOL           27° C                ↓ 8 km/h [/color]')
    blt.printf(1, 30, '[color=white] Chuva: 4%                                                 Umidade: 49% [/color]')
    blt.refresh()

    key = blt.read()

    if key == blt.TK_LEFT:
        blt.color('white')
        blt.bkcolor('black')
        blt.print(30, 34, "VOCE APERTOU: <")
        blt.refresh()
        blt.delay(500)
        from levels.welcome import saudacao
        blt.clear()
        saudacao()

    elif key == blt.TK_RIGHT:
        blt.color('white')
        blt.bkcolor('black')
        blt.print(30, 34, "VOCE APERTOU: >")
        blt.refresh()
        blt.delay(500)
        blt.close()
        #pagina3()

    elif key == blt.TK_S:
        blt.color('white')
        blt.bkcolor('black')
        blt.print(3, 34, "> ")
        rc, pag = blt.read_str(4, 34, "", 5)

        match pag:
            case 100:
                blt.refresh()
                blt.delay(500)
                blt.clear()
                saudacao()

            case 101:
                blt.print(1,2, "pagina 2")
            case _:
                blt.print(1,3, "ERROR")
                blt.refresh()
                blt.delay(500) 
                clima() 

    elif key in (blt.TK_CLOSE, blt.TK_ESCAPE):      
        exit()

    else:
        clima()

if __name__ == "__main__": 
    clima() 
