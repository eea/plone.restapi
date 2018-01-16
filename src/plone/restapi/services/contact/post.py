# -*- coding: utf-8 -*-
from plone.restapi.services import Service
from zope.component import getMultiAdapter
from plone.restapi.deserializer import json_body


class ContactPost(Service):

    def reply(self):
        data = json_body(self.request)

        sender_from_address = data.get('from', None)
        message = data.get('message', None)
        sender_fullname = data.get('name', '')
        subject = data.get('subject', '')

        if not sender_from_address or not message:
            self.request.response.setStatus(400)
            return dict(error=dict(
                type='BadRequest',
                message='Missing from or message parameters'))

        ctrlOverview = getMultiAdapter((self.context, self.request),
                                       name='overview-controlpanel')
        if ctrlOverview.mailhost_warning():
            self.request.response.setStatus(400)
            return dict(error=dict(
                type='BadRequest',
                message='MailHost is not configured.'))

        contact_info_view = getMultiAdapter((self.context, self.request),
                                            name='contact-info')

        contact_info_view.send_message(
            dict(
              message=message,
              subject=subject,
              sender_from_address=sender_from_address,
              sender_fullname=sender_fullname
            )
        )

        self.request.response.setStatus(204)
        return
