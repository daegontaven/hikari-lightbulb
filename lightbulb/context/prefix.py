# -*- coding: utf-8 -*-
# Copyright © tandemdude 2020-present
#
# This file is part of Lightbulb.
#
# Lightbulb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Lightbulb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Lightbulb. If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations

__all__ = ["PrefixContext"]

import asyncio
import typing as t

import hikari

from lightbulb.context import base

if t.TYPE_CHECKING:
    from lightbulb import app as app_
    from lightbulb import commands
    from lightbulb.utils import parser


class PrefixContext(base.Context):
    """
    An implementation of :obj:`~.context.base.Context` for prefix commands.

    Args:
        app (:obj:`~.app.BotApp`): The ``BotApp`` instance that the context is linked to.
        event (:obj:`~hikari.events.message_events.MessageCreateEvent`): The event to create the context from.
        command (Optional[:obj:`~.commands.prefix.PrefixCommand`]): The command that the context is for, or ``None``
            if no command could be resolved.
        invoked_with (:obj:`str`): The name or alias that the command was invoked with.
        prefix (:obj:`str`): The prefix that was used in this context.
    """

    __slots__ = ("_parser", "_event", "_command", "_invoked_with", "_prefix", "_options", "_defer_task")

    def __init__(
        self,
        app: app_.BotApp,
        event: hikari.MessageCreateEvent,
        command: t.Optional[commands.prefix.PrefixCommand],
        invoked_with: str,
        prefix: str,
    ) -> None:
        super().__init__(app)
        self._event = event
        self._command = command
        self._invoked_with = invoked_with
        self._prefix = prefix
        self._options: t.Dict[str, t.Any] = {}
        self._parser: parser.BaseParser

        self._defer_task: t.Optional[asyncio.Task[None]] = None
        if self._command is not None and self._command.auto_defer:

            async def _defer() -> None:
                await self.app.rest.trigger_typing(self.channel_id)

            self._defer_task = asyncio.create_task(_defer())

    @property
    def event(self) -> hikari.MessageCreateEvent:
        return self._event

    @property
    def raw_options(self) -> t.Dict[str, t.Any]:
        return self._options

    @property
    def channel_id(self) -> hikari.Snowflakeish:
        return self.event.message.channel_id

    @property
    def guild_id(self) -> t.Optional[hikari.Snowflakeish]:
        return self.event.message.guild_id

    @property
    def attachments(self) -> t.Sequence[hikari.Attachment]:
        return self.event.message.attachments

    @property
    def member(self) -> t.Optional[hikari.Member]:
        return self.event.message.member

    @property
    def author(self) -> hikari.User:
        return self.event.message.author

    @property
    def invoked_with(self) -> str:
        return self._invoked_with

    @property
    def prefix(self) -> str:
        return self._prefix

    @property
    def command(self) -> t.Optional[commands.prefix.PrefixCommand]:
        return self._command

    def get_channel(self) -> t.Optional[t.Union[hikari.GuildChannel, hikari.Snowflake]]:
        if self.guild_id is not None:
            return self.app.cache.get_guild_channel(self.channel_id)
        return self.app.cache.get_dm_channel_id(self.author.id)

    async def respond(self, *args: t.Any, **kwargs: t.Any) -> base.ResponseProxy:
        """
        Create a response for this context. This method directly calls :obj:`~hikari.messages.Message.respond`. You
        should note that it is not possible to send ephemeral messages as responses to prefix commands. All message flags
        will be removed before the call to :obj:`~hikari.messages.Message.respond`.

        Args:
            *args (Any): Positional arguments passed to :obj:`~hikari.messages.Message.respond`.
            **kwargs (Any): Keyword arguments passed to :obj:`~hikari.messages.Message.respond`.

        Returns:
            :obj:`~hikari.messages.Message`: The created message object.
        """
        if self._defer_task is not None:
            await self._defer_task
            self._defer_task = None

        kwargs.pop("flags", None)
        kwargs.pop("response_type", None)

        if args and isinstance(args[0], hikari.ResponseType):
            args = args[1:]

        self._responses.append(base.ResponseProxy(await self.event.message.respond(*args, **kwargs)))
        self._responded = True
        return self._responses[-1]
