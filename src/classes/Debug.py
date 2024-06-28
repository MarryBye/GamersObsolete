import json

class Debug:
    class TerminalColors:
        BLUE = "\033[94m"
        CYAN = "\033[96m"
        GREEN = "\033[92m"
        WHITE = "\033[97m"
        RED = "\033[91m"
        BLACK = "\033[30m"
        YELLOW = "\033[93m"
        MAGENTA = "\033[95m"
        WARNING = "\033[93m"
        FAIL = "\033[91m"
        HEADER = "\033[95m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
        END = "\033[0m"

    @staticmethod
    def debug_print(*args, text_color=TerminalColors.WHITE):
        try:
            with open("config.json", encoding="UTF-8") as config_file:
                config = json.load(config_file)
                need_debug = config["debug"]
                if need_debug:
                    print(f"{Debug.TerminalColors.GREEN}{Debug.TerminalColors.BOLD}[WEBGAMERS]:{text_color}", *args, Debug.TerminalColors.END)
        except (IOError, json.JSONDecodeError) as e:
            print(f"{Debug.TerminalColors.GREEN}{Debug.TerminalColors.BOLD}[WEBGAMERS]:{text_color} Возникла ошибка при чтении конфигурационного файла!\nПричина: {Debug.TerminalColors.FAIL}{e}", Debug.TerminalColors.END)