#!/usr/bin/env python3
# encoding: utf-8

import traceback
from pathlib import Path

import discord
from discord.ext import commands

from utils import log, MockContext
import db


class EmojiConnoisseur(commands.Bot):
	cogs_path = 'cogs'

	def __init__(self, *args, **kwargs):
		self.config = db.CONFIG
		self.db = db.DB
		super().__init__(command_prefix=commands.when_mentioned_or('ec/'), *args, **kwargs)

	async def on_ready(self):
		separator = '━'
		messages = (
			'Logged in as: %s' % self.user,
			'ID: %s' % self.user.id)
		separator *= len(max(messages, key=len))
		log(separator, *messages, separator, sep='\n')

	async def on_message(self, message):
		await self.invoke(await self.get_context(message, cls=MockContext))

	def run(self, *args, **kwargs):
		for extension in (p.stem for p in Path(self.cogs_path).glob('*.py')):
			try:
				self.load_extension(self.cogs_path+'.'+extension)
			except Exception as e:
				log('Failed to load', extension)
				log(traceback.format_exc())
		super().run(self.config['tokens']['discord'], *args, **kwargs)


# defined in a function so it can be run from a REPL if need be
def run():
	EmojiConnoisseur().run()


if __name__ == '__main__':
	run()
