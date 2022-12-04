async def get_shortlink(link):
    https = link.split(":")[0]
    if "http" == https:
        https = "https"
        link = link.replace("http", https)
    online_link = f'https://shorturllink.in/api'
    params = {'api': SHORTENER_API,
              'online_link': link,
              }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                data = await response.json()
                if data["status"] == "success":
                    return data['shortenedUrl']
                else:
                    logger.error(f"Error: {data['message']}")
                    return f'https://shorturllink.in/api?api={SHORTENER_API}&link={link}'


    except Exception as e:
        logger.error(e)
        return f'https://shorturllink.in/api?api={SHORTENER_API}&link={link}'
