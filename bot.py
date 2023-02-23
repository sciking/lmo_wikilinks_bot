import pywikibot

site_lmo = pywikibot.Site("lmo", "wikipedia")
site_it = pywikibot.Site("it", "wikipedia")
repo = site_lmo.data_repository()
categoria = ""
category = pywikibot.Category(site_lmo, categoria)
pages = category.articles(namespaces=[0])

for page in pages:
    try:
        item = pywikibot.ItemPage.fromPage(page)
        print("La pagina {} è già collegata a Wikidata con l'ID {}".format(page.title(), item.getID()))
        #item.setSitelink(site_lmo.dbName(), page.title(), summary="Aggiunto collegamento con Wikipedia in lombardo")
    except:
        print("La pagina {} non esiste su Wikidata".format(page.title()))
        try:
            page_it = pywikibot.Page(site_it, page.title())
            item_it = pywikibot.ItemPage.fromPage(page_it)
            print("La pagina omonima in italiano è {}".format(item_it.getID()))
            item = pywikibot.ItemPage(repo, item_it.getID())
            item.editLabels(labels={"lmo": page.title()}, summary="Aggiunta etichetta in lombardo")
            item.setSitelink(sitelink={'site': 'lmowiki', 'title': page.title()}, summary='Set Lombard sitelink')
#item.setSitelink(site_lmo.dbName(), page.title())
            print("Collegamento aggiunto con l'ID {}".format(item.getID()))
        except pywikibot.NoPage:
            print("La pagina omonima in italiano non esiste su Wikipedia")
            continue
