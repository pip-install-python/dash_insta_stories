# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashInstaStories(Component):
    """A DashInstaStories component.


Keyword arguments:

- id (string; optional)

- currentIndex (number; default void 0)

- defaultInterval (number; default 1200)

- header (optional)

- height (number | string; default 640)

- isPaused (boolean; default False)

- keyboardNavigation (boolean; default False)

- loader (optional)

- loop (boolean; default False)

- preloadCount (number; default 1)

- preventDefault (boolean; default False)

- progressContainerStyles (dict; optional)

- progressStyles (dict; optional)

- progressWrapperStyles (dict; optional)

- renderers (list; optional)

- stories (list of dicts; required)

    `stories` is a list of string | dict with keys:

    - header (dict; optional)

        `header` is a dict with keys:

        - heading (string; optional)

        - profileImage (string; optional)

        - subheading (string; optional)

    - url (string; required)s

- storyContainerStyles (dict; optional)

- storyStyles (dict; optional)

- width (number | string; default 360)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_insta_stories'
    _type = 'DashInstaStories'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, stories=Component.REQUIRED, renderers=Component.UNDEFINED, defaultInterval=Component.UNDEFINED, loader=Component.UNDEFINED, header=Component.UNDEFINED, storyContainerStyles=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, storyStyles=Component.UNDEFINED, progressContainerStyles=Component.UNDEFINED, progressWrapperStyles=Component.UNDEFINED, progressStyles=Component.UNDEFINED, loop=Component.UNDEFINED, isPaused=Component.UNDEFINED, currentIndex=Component.UNDEFINED, onStoryStart=Component.UNDEFINED, onStoryEnd=Component.UNDEFINED, onAllStoriesEnd=Component.UNDEFINED, onNext=Component.UNDEFINED, onPrevious=Component.UNDEFINED, keyboardNavigation=Component.UNDEFINED, preventDefault=Component.UNDEFINED, preloadCount=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'currentIndex', 'defaultInterval', 'header', 'height', 'isPaused', 'keyboardNavigation', 'loader', 'loop', 'preloadCount', 'preventDefault', 'progressContainerStyles', 'progressStyles', 'progressWrapperStyles', 'renderers', 'stories', 'storyContainerStyles', 'storyStyles', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'currentIndex', 'defaultInterval', 'header', 'height', 'isPaused', 'keyboardNavigation', 'loader', 'loop', 'preloadCount', 'preventDefault', 'progressContainerStyles', 'progressStyles', 'progressWrapperStyles', 'renderers', 'stories', 'storyContainerStyles', 'storyStyles', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['stories']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashInstaStories, self).__init__(**args)
