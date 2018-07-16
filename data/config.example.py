{
	'release': 'development',  # change this to "production" unless running tests
	'description': 'Curates emojis from any server and lets you use them without Nitro.',
	'decay': True,  # whether to enable the deletion of old emotes
	'prefix': 'ec/',
	# the contents of this file will be sent to the user when they run the "copyright" command
	# as provided by ben_cogs
	'copyright_license_file': 'data/short-license.txt',
	# make this a permanent invite to a guild where users can get help using the bot
	'support_server_invite_code': 'Zujf4K',
	# a user ID of someone to send logs to
	# note: currently nothing is sent except a notification of the bot's guild count being a power of 2
	'send_logs_to': 140516693242937345,

	'logs': {
		'emotes': {  # log changes to emotes
			'channel': None,
			'settings': {
				'add': False,  # whether to log whenever an emote is added
				'remove': False,  # whether to log whenever an emote is removed by the author
				'force_remove': True,  # whether to log whenever an emote is removed by a moderator
				'decay': True}}  # whether to log decayed emotes

	'extra_owners': [
		140516693242937345],  # User IDs of people authorized to run privileged commands on the bot

	# postgresql connection info
	'database': {
		'user': 'connoisseur',
		'password': 'hunter2',
		'database': 'connoisseur',
		'host': '127.0.0.1',
		'port': 5432},

	'tokens': {
		'discord': 'sek.rit.token',  # get this from https://discordapp.com/developers/applications/me
		'stats': {  # keep these set to None unless your bot is listed on either of these sites
			'bots.discord.pw': None,
			'discordbots.org': None,
			'botsfordiscord.com': None}}}
