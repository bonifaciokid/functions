import json
import pymysql.cursors


def database_connection(server_key):
	"""
		Args:
			local : locahost
			production : production database
		Returns:
			Fetch operation context management, cursor and connect.
	"""
	open_configs = open('/path/to/file/scrapy-configs.json').read()
	load_configs = json.loads(open_configs)
	current_server = load_configs[server_key]
	user = current_server['user']
	password = current_server['password']
	db = current_server['db']
	server_host = current_server['host']
	conn = pymysql.connect(
							user=user,
							passwd=password,
							db=db,
							host=server_host,
							charset="utf8",
							use_unicode=True
						)
	cursor = conn.cursor()

	return [cursor, conn]


