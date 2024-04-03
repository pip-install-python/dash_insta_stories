import dash_insta_stories
from dash import Dash, callback, html, Input, Output

app = Dash(__name__)

# Define your stories
stories = [
    {
        "url": "https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg",
        "type": "image",
        "duration": 5000,
        "header": {
            "heading": "Colorize lizard",
            "subheading": "Cute isn't he?",
            "profileImage": "https://sea2.discourse-cdn.com/business7/user_avatar/community.plotly.com/pipinstallpython/288/27532_2.png"
        },
        # "seeMore": lambda: {"url": "https://example.com"},
        "styles": {"background": "#f5f5f5"},
        "preloadResource": True
    },
    {
        "url": "https://www.simplilearn.com/ice9/free_resources_article_thumb/what_is_image_Processing.jpg",
        "header": {
            "heading": "I see all",
            "subheading": "👀",
            "profileImage": "https://sea2.discourse-cdn.com/business7/user_avatar/community.plotly.com/pipinstallpython/288/27532_2.png"
        }
    },
{
        "url": "https://www.adobe.com/products/media_14562ad96c12a2f3030725ae81bd3ede1c68cb783.jpeg?width=750&format=jpeg&optimize=medium",
        "header": {
            "heading": "backster",
            "subheading": "puppies with sweaters",
            "profileImage": "https://sea2.discourse-cdn.com/business7/user_avatar/community.plotly.com/pipinstallpython/288/27532_2.png"
        }
    }
    # Add more stories as needed
]

app.layout = html.Div([
    dash_insta_stories.DashInstaStories(
        id='input',
        stories=stories,  # Pass the stories to DashInstaStories
        renderers=[],  # Pass the renderers to DashInstaStories
        defaultInterval=2200,  # Pass the defaultInterval to DashInstaStories
        loader=None,  # Pass the loader to DashInstaStories
        header=None,  # Pass the header to DashInstaStories
        storyContainerStyles={},  # Pass the storyContainerStyles to DashInstaStories
        width=360,  # Pass the width to DashInstaStories
        height=640,  # Pass the height to DashInstaStories
        storyStyles={},  # Pass the storyStyles to DashInstaStories
        progressContainerStyles={},  # Pass the progressContainerStyles to DashInstaStories
        progressWrapperStyles={},  # Pass the progressWrapperStyles to DashInstaStories
        progressStyles={},  # Pass the progressStyles to DashInstaStories
        loop=True,  # Pass the loop to DashInstaStories
        isPaused=False,  # Pass the isPaused to DashInstaStories
        currentIndex=None,  # Pass the currentIndex to DashInstaStories
        # onStoryStart=None,  # Pass the onStoryStart to DashInstaStories
        # onStoryEnd=None,  # Pass the onStoryEnd to DashInstaStories
        # onAllStoriesEnd=None,  # Pass the onAllStoriesEnd to DashInstaStories
        # onNext=None,  # Pass the onNext to DashInstaStories
        # onPrevious=None,  # Pass the onPrevious to DashInstaStories
        keyboardNavigation=True,  # Pass the keyboardNavigation to DashInstaStories
        preventDefault=False,  # Pass the preventDefault to DashInstaStories
        preloadCount=1,  # Pass the preloadCount to DashInstaStories
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True, port='4011')
