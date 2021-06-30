# coding: utf-8

import json

import requests
from sentry.plugins.bases.notify import NotificationPlugin

import sentry_c3_wxwork
from .forms import WxWorkOptionsForm

WxWork_API = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={token}"


class WxWorkPlugin(NotificationPlugin):
    """
    Sentry plugin to send error counts to c3WxWork.
    """
    author = 'anshenglm'
    author_url = 'https://github.com/c3jbz/sentry-c3-wxwork'
    version = sentry_wxwork.VERSION
    description = 'Send error counts to wxwork.'
    resource_links = [
        ('Source', 'https://github.com/c3jbz/sentry-c3-wxwork'),
        ('Bug Tracker', 'https://github.com/c3jbz/sentry-c3-wxwork/issues'),
        ('README', 'https://github.com/c3jbz/sentry-c3-wxwork/blob/master/README.md'),
    ]

    slug = 'WxWork'
    title = 'WxWork'
    conf_key = slug
    conf_title = title
    project_conf_form = WxWorkOptionsForm

    def is_configured(self, project):
        """
        Check if plugin is configured.
        """
        return bool(self.get_option('access_token', project))

    def notify_users(self, group, event, *args, **kwargs):
        self.post_process(group, event, *args, **kwargs)

    def post_process(self, group, event, *args, **kwargs):
        """
        Process error.
        """
        if not self.is_configured(group.project):
            return

        if group.is_ignored():
            return

        access_token = self.get_option('access_token', group.project)
        send_url = WxWork_API.format(token=access_token)
        title = u"New alert from {}".format(event.project.slug)

        data = {
            "msgtype": "text",
            "text": {
                "content": u"#### {title} \n > {message} [href]({url})".format(
                    title=title,
                    message=event.title or event.message,
                    url=u"{}events/{}/".format(group.get_absolute_url(), event.event_id),
                )
            }
        }
        requests.post(
            url=send_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8")
        )
