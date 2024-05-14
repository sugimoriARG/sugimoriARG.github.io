from colorama import Style

class Colores:
    ENTRENADOR1 = "\033[7;30;47m"
    ENTRENADOR2 = "\033[0;30;47m"
    RESET = Style.RESET_ALL
    MENU = "\033[38;5;231m"
    AGUA = "\033[38;5;33m"
    FUEGO = "\033[38;5;1m"
    ELECTRICO = "\033[38;5;226m"
    FANTASMA = "\033[38;5;53m"
    HIELO = "\033[38;5;45m"
    INSECTO = "\033[38;5;82m"
    LUCHA = "\033[38;5;131m"
    NORMAL = "\033[38;5;246m"
    PLANTA = "\033[38;5;22m"
    PSIQUICO = "\033[38;5;126m"
    TIERRA = "\033[38;5;94m"
    VENENO = "\033[38;5;54m"
    VOLADOR = "\033[38;5;248m"


# https://gist.github.com/justinabrahms/1047767
# https://askubuntu.com/questions/821157/print-a-256-color-test-pattern-in-the-terminal
# for i in {0..255} ; do
#     printf "\x1b[48;5;%sm%3d\e[0m " "$i" "$i"
#     if (( i == 15 )) || (( i > 15 )) && (( (i-15) % 6 == 0 )); then
#         printf "\n";
#     fi
# done