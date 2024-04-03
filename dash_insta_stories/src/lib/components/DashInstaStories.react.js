import React from 'react';
import PropTypes from 'prop-types';
import Stories, {WithSeeMore} from 'react-insta-stories';


const DashInstaStories = (props) => {
    const {
        id, stories, renderers, defaultInterval, loader, header,
        storyContainerStyles, width, height, storyStyles, progressContainerStyles,
        progressWrapperStyles, progressStyles, loop, isPaused, currentIndex, onStoryStart,
        onStoryEnd, onAllStoriesEnd, onNext, onPrevious, keyboardNavigation, preventDefault,
        preloadCount
    } = props;

    return (
        <div id={id}>
            <Stories
                stories={stories}
                renderers={renderers}
                defaultInterval={defaultInterval}
                loader={loader}
                header={header}
                storyContainerStyles={storyContainerStyles}
                width={width}
                height={height}
                storyStyles={storyStyles}
                progressContainerStyles={progressContainerStyles}
                progressWrapperStyles={progressWrapperStyles}
                progressStyles={progressStyles}
                loop={loop}
                isPaused={isPaused}
                currentIndex={currentIndex}
                onStoryStart={onStoryStart}
                onStoryEnd={onStoryEnd}
                onAllStoriesEnd={onAllStoriesEnd}
                onNext={onNext}
                onPrevious={onPrevious}
                keyboardNavigation={keyboardNavigation}
                preventDefault={preventDefault}
                preloadCount={preloadCount}
            />
        </div>
    );
}

DashInstaStories.defaultProps = {
    renderers: [],
    defaultInterval: 1200,
    storyContainerStyles: {},
    width: 360,
    height: 640,
    storyStyles: {},
    progressContainerStyles: {},
    progressWrapperStyles: {},
    progressStyles: {},
    loop: false,
    isPaused: false,
    currentIndex: void 0,
    keyboardNavigation: false,
    preventDefault: false,
    preloadCount: 1,
};

DashInstaStories.propTypes = {
    id: PropTypes.string,
    stories: PropTypes.arrayOf(
        PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.shape({
                url: PropTypes.string.isRequired,
                header: PropTypes.shape({
                    heading: PropTypes.string,
                    subheading: PropTypes.string,
                    profileImage: PropTypes.string,
                }),
            })
        ])
    ).isRequired,
    renderers: PropTypes.array,
    defaultInterval: PropTypes.number,
    loader: PropTypes.elementType,
    header: PropTypes.elementType,
    storyContainerStyles: PropTypes.object,
    width: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
    height: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
    storyStyles: PropTypes.object,
    progressContainerStyles: PropTypes.object,
    progressWrapperStyles: PropTypes.object,
    progressStyles: PropTypes.object,
    loop: PropTypes.bool,
    isPaused: PropTypes.bool,
    currentIndex: PropTypes.number,
    onStoryStart: PropTypes.func,
    onStoryEnd: PropTypes.func,
    onAllStoriesEnd: PropTypes.func,
    onNext: PropTypes.func,
    onPrevious: PropTypes.func,
    keyboardNavigation: PropTypes.bool,
    preventDefault: PropTypes.bool,
    preloadCount: PropTypes.number,
};

export default DashInstaStories;