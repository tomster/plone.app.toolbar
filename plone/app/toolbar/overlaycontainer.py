from zope.component import getUtility
from zope.publisher.browser import BrowserView
from plone.memoize.instance import memoize
from plone.registry.interfaces import IRegistry

class OverlayContainer(BrowserView):
    """View that provides a main_template replacement for overlays.
    
    Use metal:use-macro="context/@@toolbar-overlay-container/macros/master"
    and then fill the main macro.
    """
    
    def __call__(self):
        # Disable theming
        self.request.response.setHeader('X-Theme-Disabled', 'True')
        
        # Set CMSUI theme
        self.context.changeSkin(self.settings.skinName, self.request)
        
        return self.index()

    @property
    def macros(self):
        return self.index.macros
