# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashInstaStories <- function(id=NULL, currentIndex=NULL, defaultInterval=NULL, header=NULL, height=NULL, isPaused=NULL, keyboardNavigation=NULL, loader=NULL, loop=NULL, onAllStoriesEnd=NULL, onNext=NULL, onPrevious=NULL, onStoryEnd=NULL, onStoryStart=NULL, preloadCount=NULL, preventDefault=NULL, progressContainerStyles=NULL, progressStyles=NULL, progressWrapperStyles=NULL, renderers=NULL, stories=NULL, storyContainerStyles=NULL, storyStyles=NULL, width=NULL) {
    
    props <- list(id=id, currentIndex=currentIndex, defaultInterval=defaultInterval, header=header, height=height, isPaused=isPaused, keyboardNavigation=keyboardNavigation, loader=loader, loop=loop, onAllStoriesEnd=onAllStoriesEnd, onNext=onNext, onPrevious=onPrevious, onStoryEnd=onStoryEnd, onStoryStart=onStoryStart, preloadCount=preloadCount, preventDefault=preventDefault, progressContainerStyles=progressContainerStyles, progressStyles=progressStyles, progressWrapperStyles=progressWrapperStyles, renderers=renderers, stories=stories, storyContainerStyles=storyContainerStyles, storyStyles=storyStyles, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashInstaStories',
        namespace = 'dash_insta_stories',
        propNames = c('id', 'currentIndex', 'defaultInterval', 'header', 'height', 'isPaused', 'keyboardNavigation', 'loader', 'loop', 'onAllStoriesEnd', 'onNext', 'onPrevious', 'onStoryEnd', 'onStoryStart', 'preloadCount', 'preventDefault', 'progressContainerStyles', 'progressStyles', 'progressWrapperStyles', 'renderers', 'stories', 'storyContainerStyles', 'storyStyles', 'width'),
        package = 'dashInstaStories'
        )

    structure(component, class = c('dash_component', 'list'))
}
