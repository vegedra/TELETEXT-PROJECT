from bearlibterminal import terminal as blt

def intro():
    blt.set('window.size=80x20')
    blt.color('white')
    # printa texto: (x, y, 'texto')
    blt.print(30, 9, 'Pedro Ivo (c)  Copyright 2022')

    # updata o blt e imprime o que foi escrito
    blt.refresh()
 
    # delay em milisegundos (pode usar o sleep() tbm se o importar)
    blt.delay(2000)

    # limpa o blt
    blt.clear()
    blt.print(29, 9, "- Feito por Digital Cake Studio -")
    blt.refresh()
    blt.delay(2000)
    blt.clear()

    # muda o tamanho da tela para caber a arte ASCII
    blt.set('window.size=85x38')

    # comando para imprimir arte ASCII ou grandes blocos de texto
    blt.printf(1, 1, """
                                      i.
                                      .7.
                                     .. :v
                                    c:  .x
                                     i.::
                                       :
                                     ..i..
                                    #MMMMM
                                    QM  AM
                                    9M  zM
                                    6M  AM
                                    2M  2MMXX###MMMMMM@@1
                                    OM  tMMMMMMMMMMMMMMMMMM;
                               .X#MMMM  ;MMMMMMMMMMMMMMMMMMMMMv
                           cEMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM@
                     .n@MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                    MMMMMMMMMMM@@#$BWWB#@@#$WWWWWWQQQWWWWWWb#@MMM.
                    MM                                         ;M.
                    $M                                         EM
                    WMO$@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#OMM
                    #M                                         cM
                    QM                                         tM
                    MM            Digital Cake Studio          CMO
                    MM                                         MOC       
                 .MMMM                                         oMMMt   
                1MO 6MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM iMM
               .M1  BM                                          VM  ,Mt
               1M   @M ........................................ WM   M6
                MM  .A8oQWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWOAz2  #M
                 MM                                                 MM.
                  @MMY                                           VMME
                    UMMMbi                                  i8MMMt
                       C@MMMMMbt;;i..................i;XQMMMMMt
                            ;ZMMMMMMMMMMMMMMMMMMMMMMMMMM@A;.
""")
    blt.refresh()
    blt.delay(3000)

# vai para o main.py
from main import main_menu
main_menu()

# sinceramente nao sei, mas é importante
if __name__ == "__main__": 
    intro() 