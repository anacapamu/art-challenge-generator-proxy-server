# Art Challenge Generator Proxy Server
The Art Challenge proxy server is to be used with the [Art Challenge Generator](https://github.com/anacapamu/art-challenge-generator) web app. 

## Quick Start
1. Create a `.env` file with API keys
    ```bash
    # .env

    # Rijksmuseum API key
    ART_KEY="replace_with_your_api_key"

    # Wordnik API Key
    WORD_KEY="replace_with_your_api_key"
    ```

## Endpoints

### GET
`[/word]` read a random word<br/>
`[/art]` read all art collection of Rijksmuseum that contain images<br/>
