def help():
	return """SYNTAX:
		print(help()): print this text
		print(clr("color", "bg", "style", "text")): main function
		
STYLES:
		bold: bold text
		uline: underlined text
		If you write anything else, nothing will happen.
		
COLORS:
		red: red text
		yellow: yellow text
		blue: blue text
		magenta: magenta text
		cyan: cyan text
		black: black text
		white: white text
		bred: bright red text
		byellow: bright yellow text
		bblue: bright blue text
		bmagenta: bright magenta text
		bcyan: bright cyan text
		grey: grey text
		bwhite: bright white text
		If you write anything else, nothing will happen.
		
BACKGROUNDS:
		red: red background
		yellow: yellow background
		blue: blue background
		magenta: magenta background
		cyan: cyan background
		black: black background
		white: white background
		bred: bright red background
		byellow: bright yellow background
		bblue: bright blue background
		bmagenta: bright magenta background
		bcyan: bright cyan background
		grey: grey background
		bwhite: bright white background
		If you write anything else, nothing will happen.
		"""

def clr(color, bg, style, text):
	result = ""
	match color:
		case "red":
			result += "\033[31m"
		case "yellow":
			result += "\033[33m"
		case "green":
			result += "\033[32m"
		case "blue":
			result += "\033[34m"
		case "magenta":
			result += "\033[35m"
		case "cyan":
			result += "\033[36m"
		case "black":
			result += "\033[30m"
		case "white":
			result += "\033[37m"
		case "bred":
			result += "\033[91m"
		case "byellow":
			result += "\033[93m"
		case "bgreen":
			result += "\033[92m"
		case "bblue":
			result += "\033[94m"
		case "bmagenta":
			result += "\033[95m"
		case "bcyan":
			result += "\033[96m"
		case "grey":
			result += "\033[90m"
		case "bwhite":
			result += "\033[97m"
		case "none" | _:
			pass
	
	match bg:
		case "red":
			result += "\033[41m"
		case "yellow":
			result += "\033[34m"
		case "green":
			result += "\033[42m"
		case "blue":
			result += "\033[44m"
		case "magenta":
			result += "\033[45m"
		case "cyan":
			result += "\033[46m"
		case "black":
			result += "\033[40m"
		case "white":
			result += "\033[47m"
		case "bred":
			result += "\033[101m"
		case "byellow":
			result += "\033[103m"
		case "bgreen":
			result += "\033[102m"
		case "bblue":
			result += "\033[104m"
		case "bmagenta":
			result += "\033[105m"
		case "bcyan":
			result += "\033[106m"
		case "grey":
			result += "\033[100m"
		case "bwhite":
			result += "\033[107m"
		case "none" | _:
			pass
		
	match style:
		case "bold":
			result += "\033[1m"
		case "uline":
			result += "\033[4m"
	
	result += f"{text}\033[0m\033[21m\033[24m"
	return result
