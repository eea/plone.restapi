from . import PortletSerializer
from plone.app.portlets.portlets.news import Renderer
from plone.restapi.interfaces import ISerializeToJsonSummary
from zope.component import getMultiAdapter


class NewsPortletSerializer(PortletSerializer):
    """ Portlet serializer for news portlet
    """

    def __call__(self):
        res = super(NewsPortletSerializer, self).__call__()
        renderer = NewsPortletRenderer(
            self.context,
            self.request,
            None,
            None,
            self.assignment
        )
        res['newsportlet'] = renderer.render()

        return res


class NewsPortletRenderer(Renderer):
    def render(self):
        items = []
        brains = self.published_news_items()

        for brain in brains:
            itemList = getMultiAdapter(
                (brain, self.request), ISerializeToJsonSummary)()
            ploneview = getMultiAdapter(
                (self.context, self.request), name='plone')
            itemList['date'] = ploneview.toLocalizedTime(brain.created)
            # Using datetime fails with:
            #   Object of type DateTime is not JSON serializable
            # itemList['date'] = brain.created.asdatetime()

            itemList['date'] = brain.created.strftime('%Y-%m-%d %X')
            itemList['thumb'] = ''

            if self.thumb_scale and brain.getIcon:
                itemList['thumb'] = '{}/@@images/image/{}'.format(
                                    brain.getURL(), self.thumb_scale())
            items.append(itemList)
        res = {
            'items': items,
            'all_news_link': self.all_news_link(),
        }

        return res
