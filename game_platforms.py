

def game_name_plus_platform(game_name, platform_id):
	"""
		Return:
			Added cleaned game_name + platform_id
	"""
	clean_name = [char.lower() for char in game_name if char.isalnum()]#get alpha numeric characters
	join_name = ''.join(clean_name)

	return join_name + str(platform_id)


def check_platform_name(platform_id):
	"""
		Return:
			Name platform
	"""
	platform_dict = {
						1 : 'pc',
						2 : 'ps3',
						3 : 'xbox 360',
						4 : 'wii u',
						5 : 'android',
						6 : 'ios',
						7 : 'vita',
						8 : 'ps4',
						9 : 'xbox one',
						10 : '3ds',
						11 : 'switch',
						14 : 'ps5',
						228 : 'xbox series x'
					}

	return platform_dict[platform_id]


def find_game_platforms(text):
	"""
		Args:
			A string that is uncleaned but one or more platform(s) may exists.
		Returns:
			platform's name
	"""
	lower_text = ''.join(text).lower()
	platform_list = ['playstation vr', 'pc', 'windows', 'mac', 'microsoft', 'linux', 'ps3', 'playstation 3', 'playstation-3', 'xbox-360', 'xbox 360', 'xbox360', '360', 'x360', 'wii-u', 'wiiu', 'wii u', 'nintendo wii u', 'nintendo wiiu', 'android', 'iphone', 'ipad', ' ios', 'vita', 'ps-vita', 'playstation vita', 'ps vita', 'psvita', 'psvr', 'ps vr', 'playstation 4', 'playstation-4', 'ps4', 'xb1', 'xone', 'xbone', 'xboxone', 'xboxonex', 'xbox one', 'xbox-one', 'xbox one x', 'xbox-one-x', 'nintendo-3ds', 'nintendo 3ds', '3ds', 'nintendo switch', 'switch', 'nintendo-switch', 'oculus', 'htc', 'rift', 'series-x', 'series', 'ps5', 'playstation-5', 'playstation 5', 'playstation5']
	platforms = [platform for platform in platform_list if platform in lower_text]
	return ', '.join(platforms)


def get_platform_id(raw_platform):
	"""
		Args:
			Uncleaned string from scraped data, maybe a URL, a list or a string.
		Returns:
			Check if key exists in join_platform variable and returns platform_id.
	"""
	join_platform = ''.join(raw_platform).lower()
	platform_dict = {
						'rift' : 1,
						'oculus' : 1,
						'htc' : 1,
						'steam' : 1,
						'pc' : 1,
						'microsoft windows' : 1,
						'microsoft' : 1,
						'windows' : 1,
						'mac' : 1,
						'linux' : 1,
						'ps3' : 2,
						'playstation 3' : 2,
						'playstation-3' : 2,
						'playstation3' : 2,
						'xbox-360' : 3,
						'xbox 360' : 3,
						'xbox360' : 3,
						'360' : 3,
						'x360' : 3,
						'wii-u' : 4,
						'wiiu' : 4,
						'wii u' : 4,
						'nintendo wii u': 4,
						'nintendo wiiu' : 4,
						'nintendowiiu' : 4,
						'android' : 5,
						'and' : 5,
						'iphone' : 6,
						'ipad' : 6,
						'ios' : 6,
						'vita' : 7,
						'ps-vita' : 7,
						'playstation vita': 7,
						'ps vita' : 7,
						'psvita' : 7,
						'playstationvita' : 7,
						'psvr' : 8,
						'ps vr' : 8,
						'playstation 4' : 8,
						'playstation-4' : 8,
						'playstation4' : 8,
						'ps4' : 8,
						'one' : 9,
						'xo' : 9,
						'xb1' : 9,
						'xbo' : 9,
						'xone' : 9,
						'xbone' : 9,
						'xboxone' : 9,
						'xboxonex' : 9,
						'xbox one' : 9,
						'xbox-one' : 9,
						'xbox one x' : 9,
						'xbox-one-x' : 9,
						'nintendo-3ds' : 10,
						'nintendo 3ds' : 10,
						'3ds' : 10,
						'nintendo switch' : 11,
						'switch' : 11,
						'nsw' : 11,
						'nintendo-switch' : 11,
						'nintendoswitch' : 11,
						'ps5' : 14,
						'playstation-5' : 14,
						'playstation 5' : 14,
						'playstation5' : 14,
						'xbox series x' : 228,
						'xbox-series-x' : 228,
						'series x' : 228,
						'xboxseriesx' : 228
					} 

	for item in platform_dict:
		if item in join_platform:
			return platform_dict[item]
