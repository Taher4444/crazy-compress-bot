# <https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from . import *
from .devtools import *
from .config import *

LOGS.info("Starting...")

try:
    bot.start(bot_token=BOT_TOKEN)
except Exception as er:
    LOGS.info(er)


####### GENERAL CMDS ########

@bot.on(events.NewMessage(pattern="/start"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!😕💔**")
    await start(e)


@bot.on(events.NewMessage(pattern="/setcode"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!😕💔**")
    await coding(e)


@bot.on(events.NewMessage(pattern="/cmds"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!😕💔**")
    await zylern(e)


@bot.on(events.NewMessage(pattern="/ping"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!😕💔**")
    await up(e)


@bot.on(events.NewMessage(pattern="/sysinfo"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!😕💔**")
    await sysinfo(e)


@bot.on(events.NewMessage(pattern="/leech"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!😕💔**")
    await dl_link(e)


@bot.on(events.NewMessage(pattern="/help"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!😕💔**")
    await help(e)


@bot.on(events.NewMessage(pattern="/renew"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!😕💔**")
    await renew(e)


@bot.on(events.NewMessage(pattern="/clear"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!😕💔**")
    await clearqueue(e)


@bot.on(events.NewMessage(pattern="/speed"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Sorry You're not An Authorised User!😕💔**")
    await test(e)
    
    

########## Direct ###########

@bot.on(events.NewMessage(pattern="/eval"))
async def _(e):
    await eval(e)

@bot.on(events.NewMessage(pattern="/bash"))
async def _(e):
    await bash(e)


######## Callbacks #########

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stats(.*)")))
async def _(e):
    await stats(e)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"skip(.*)")))
async def _(e):
    await skip(e)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back(.*)")))
async def _(e):
    await back(e)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile("ihelp")))
async def _(e):
    await ihelp(e)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile("beck")))
async def _(e):
    await beck(e)


########## AUTO ###########

@bot.on(events.NewMessage(incoming=True))
async def _(e):
    await encod(e)


async def something():
    for i in itertools.count():
        try:
            if not WORKING and QUEUE:
                user = int(OWNER.split()[0])
                e = await bot.send_message(user, "**Downloading Queue Files...😙❤️**")
                s = dt.now()
                try:
                    if isinstance(QUEUE[list(QUEUE.keys())[0]], str):
                        dl = await fast_download(
                            e, list(QUEUE.keys())[0], QUEUE[list(QUEUE.keys())[0]]
                        )
                    else:
                        dl, file = QUEUE[list(QUEUE.keys())[0]]
                        tt = time.time()
                        dl = "encode/" + dl
                        with open(dl, "wb") as f:
                            ok = await download_file(
                                client=bot,
                                location=file,
                                out=f,
                                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                                    progress(
                                        d,
                                        t,
                                        e,
                                        tt,
                                        "**Downloading...😙❤️**",
                                    )
                                ),
                            )
                except Exception as r:
                    LOGS.info(r)
                    WORKING.clear()
                    QUEUE.pop(list(QUEUE.keys())[0])
                es = dt.now()
                kk = dl.split("/")[-1]
                aa = kk.split(".")[-1]
                rr = "encode"
                bb = kk.replace(f".{aa}", " [HEVC].mkv")
                out = f"{rr}/{bb}"
                thum = "thumb.jpg"
                dtime = ts(int((es - s).seconds) * 1000)
                hehe = f"{out};{dl};{list(QUEUE.keys())[0]}"
                wah = code(hehe)
                nn = await e.edit(
                    "**Compressing...**",
                    buttons=[
                        [Button.inline("STATS", data=f"stats{wah}")],
                        [Button.inline("CANCEL", data=f"skip{wah}")],
                    ],
                )
                ffmpegcode.append("-preset fast -c:v libx265 -s 854x480 -265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -pix_fmt yuv420p -crf 29 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2  -ab 32k  -vbr 2 -level 3.1")
                cmd = f"""ffmpeg -i '{dl}' {ffmpegcode[0]} '{out}' -y"""
                process = await asyncio.create_subprocess_shell(
                    cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
                )
                stdout, stderr = await process.communicate()
                er = stderr.decode()
                try:
                    if er:
                        await e.edit(str(er) + "\n\n**ERROR**")
                        QUEUE.pop(list(QUEUE.keys())[0])
                        os.remove(dl)
                        os.remove(out)
                        continue
                except BaseException:
                    pass
                ees = dt.now()
                ttt = time.time()
                await nn.delete()
                nnn = await e.client.send_message(e.chat_id, "**Uploading...😙❤️**")
                with open(out, "rb") as f:
                    ok = await upload_file(
                        client=e.client,
                        file=f,
                        name=out,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(d, t, nnn, ttt, "**Uploading...😙❤️**")
                        ),
                    )
                ds = await e.client.send_file(
                    e.chat_id, file=ok, force_document=True, thumb=thum
                )
                await nnn.delete()
                org = int(Path(dl).stat().st_size)
                com = int(Path(out).stat().st_size)
                pe = 100 - ((com / org) * 100)
                per = str(f"{pe:.2f}") + "%"
                eees = dt.now()
                x = dtime
                xx = ts(int((ees - es).seconds) * 1000)
                xxx = ts(int((eees - ees).seconds) * 1000)
                a1 = await info(dl, e)
                a2 = await info(out, e)
                dk = await ds.reply(
                    f"**●Original File Size :** {hbs(org)}\n**●Compressed File Size :** {hbs(com)}\n**●Compressed File Percentage :** {per}\n\n**●Get Mediainfo here :** [Before]({a1})/[After]({a2})\n\n●Downloaded in : {x}\n●Compressed in : {xx}\n●Uploaded in : {xxx}\n\nDone #compress #480p",
                    link_preview=False,
                )
                QUEUE.pop(list(QUEUE.keys())[0])
                os.remove(dl)
                os.remove(out)
            else:
                await asyncio.sleep(3)
        except Exception as err:
            LOGS.info(err)


########### Start ############

LOGS.info("Bot has started.")
with bot:
    bot.loop.run_until_complete(something())
    bot.loop.run_forever()
