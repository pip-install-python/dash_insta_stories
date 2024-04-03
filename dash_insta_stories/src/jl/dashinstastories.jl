# AUTO GENERATED FILE - DO NOT EDIT

export dashinstastories

"""
    dashinstastories(;kwargs...)

A DashInstaStories component.

Keyword arguments:
- `id` (String; optional)
- `currentIndex` (Real; optional)
- `defaultInterval` (Real; optional)
- `header` (optional)
- `height` (Real | String; optional)
- `isPaused` (Bool; optional)
- `keyboardNavigation` (Bool; optional)
- `loader` (optional)
- `loop` (Bool; optional)
- `preloadCount` (Real; optional)
- `preventDefault` (Bool; optional)
- `progressContainerStyles` (Dict; optional)
- `progressStyles` (Dict; optional)
- `progressWrapperStyles` (Dict; optional)
- `renderers` (Array; optional)
- `stories` (required): . stories has the following type: Array of String | lists containing elements 'url', 'header'.
Those elements have the following types:
  - `url` (String; required)
  - `header` (optional): . header has the following type: lists containing elements 'heading', 'subheading', 'profileImage'.
Those elements have the following types:
  - `heading` (String; optional)
  - `subheading` (String; optional)
  - `profileImage` (String; optional)s
- `storyContainerStyles` (Dict; optional)
- `storyStyles` (Dict; optional)
- `width` (Real | String; optional)
"""
function dashinstastories(; kwargs...)
        available_props = Symbol[:id, :currentIndex, :defaultInterval, :header, :height, :isPaused, :keyboardNavigation, :loader, :loop, :preloadCount, :preventDefault, :progressContainerStyles, :progressStyles, :progressWrapperStyles, :renderers, :stories, :storyContainerStyles, :storyStyles, :width]
        wild_props = Symbol[]
        return Component("dashinstastories", "DashInstaStories", "dash_insta_stories", available_props, wild_props; kwargs...)
end

