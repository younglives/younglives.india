from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.formlib import form
from zope.interface import implements


class IIndiaLogoPortlet(IPortletDataProvider):
    """ A portlet for the India logo. """


class Assignment(base.Assignment):

    implements(IIndiaLogoPortlet)


class Renderer(base.Renderer):
    _template = ViewPageTemplateFile('india-logo.pt')

    def render(self):
        return self._template()


class AddForm(base.AddForm):
    form_fields = form.Fields(IIndiaLogoPortlet)


class EditForm(base.EditForm):
    form_fields = form.Fields(IIndiaLogoPortlet)
