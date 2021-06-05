from rcon import Client

def rcon_connect(address, port, password, command):
	with Client(f'{address}', int(port), passwd=f'{password}') as client: 
		response = client.run(str(command))
		return response

address = input("アドレス: ")
port = input("ポート(UDP): ")
password = input("Rconのパスワード: ")

while True:
	command = input("[Rcon]>")
	if command == "exit":
		input("エンターキーを押してください")
		exit()
	try:
		response = rcon_connect(address, port, password, command)
	except ValueError:
		print("エラーが発生しました。")
		print("原因として以下が考えられます。")
		print("1 - アドレスやポート等が間違えている")
		print("2 - このソフトで処理できない文字列を送信した")
		print("3 - ポートで数字以外や65535以上の数字を入力した。")
		input("エンターキーを押してください")
		exit()

	print(f"{response}")