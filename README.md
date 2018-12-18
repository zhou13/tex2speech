# tex2speech

````
 ________    _____   __     __     ______     _____   _____     _____    _____     ____   __    __ 
(___  ___)  / ___/  (_ \   / _)   (____  \   / ____\ (  __ \   / ___/   / ___/    / ___) (  \  /  )
    ) )    ( (__      \ \_/ /          ) /  ( (___    ) )_) ) ( (__    ( (__     / /      \ (__) / 
   ( (      ) __)      \   /      __  / /    \___ \  (  ___/   ) __)    ) __)   ( (        ) __ (  
    ) )    ( (         / _ \     /  \/ / __      ) )  ) )     ( (      ( (      ( (       ( (  ) ) 
   ( (      \ \___   _/ / \ \_  ( () \__/ /  ___/ /  ( (       \ \___   \ \___   \ \___    ) )( (  
   /__\      \____\ (__/   \__)  \__\____(  /____/   /__\       \____\   \____\   \____)  /_/  \_\ 
                                                                                                   
````

This script help you dub your paper's video with Google's WaveNet-Based [Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/).

## Requirement ##

As long as you have a internet connection and you can run python, you can use this script.

## Usage ##
```
python speech.py --help
mkdir speech
python speech.py example.tex speech/
```

The output will be in the .wav files in the `speech/` directory.
