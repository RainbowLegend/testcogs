@commands.command(pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager",
                           "Administrator", "Game Moderator", "game night moderator")
    async def pingnotif(self, ctx):
        questionOne = await self.bot.say("Would you like to ping `all`, `classic` or `coven`?")
        mentioned = await self.bot.wait_for_message(author=ctx.message.author, timeout=15)
        covenNotification = discord.Role(id='358655924342095874', server='288455332173316106')
        toscd = discord.Server(id='288455332173316106')
        optinrole = discord.Role(id='379748801197637644', server='288455332173316106')

        # If an invalid response or nothing is entered, command cancels and returns.
        if mentioned is None:
            await self.bot.say("Command cancelled.")
            await self.bot.delete_message(questionOne)
            return

        # If the coven choice is picked, continue here.
        elif mentioned.clean_content.lower() == "coven":
            await self.bot.delete_message(questionOne)
            await self.bot.delete_message(mentioned)
            roleToPing = "coven"
            questionTwo = await self.bot.say("Good. We'll be pinging the `Coven Notifications` role. "
                                             "What would you like to say?")
            messagecontent = await self.bot.wait_for_message(author=ctx.message.author, timeout=60)

            # If an invalid response or nothing is entered, command cancels and returns.
            if messagecontent is None:
                await self.bot.delete_message(questionTwo)
                await self.bot.say("Command cancelled.")
                return

            # If a message is entered, the command continues.
            else:
                await self.bot.delete_message(questionTwo)
                await self.bot.delete_message(messagecontent)
                confirmation = await self.bot.say("Okay, good. "
                                                  "Confirm (Y/n) this is what you would like the message to say: "
                                                  "```" + str(messagecontent.clean_content) + "```")
                confResponse = await self.bot.wait_for_message(author=ctx.message.author, timeout=15)

                # If the user's response is Y/y, continue here. Sends the final message.
                if confResponse.clean_content.lower() in ['y', 'yes']:

                    await self.bot.edit_role(toscd, covenNotification, name="Coven Notifications",
                                             colour=discord.Colour(0x550a94), mentionable=True)

                    await self.bot.delete_message(confirmation)
                    await self.bot.delete_message(confResponse)
                    
                    await self.bot.say("<@&358655924342095874> **||** Message from <@"
                                       + str(ctx.message.author.id) + ">")
                    await self.bot.say(str(messagecontent.clean_content))

                    await self.bot.edit_role(toscd, covenNotification, name="Coven Notifications",
                                             colour=discord.Colour(0x550a94), mentionable=False)

                    return


                # If the user's response is N/n, command cancels and returns.
                if confResponse.clean_content.lower() in ['n', 'no']:
                    await self.bot.delete_message(confirmation)
                    await self.bot.delete_message(confResponse)
                    await self.bot.say("Command cancelled.")
                    return

                # If nothing or invalid is entered, command is cancelled and returns.
                else:
                    await self.bot.delete_message(confirmation)
                    await self.bot.delete_message(confResponse)
                    await self.bot.say("command cancelled.")
                    return
