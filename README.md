![Moss cushions at close range after rain, one amber maple leaf on the nearest cushion](intro-banner.png)

# acra-SecretsScanner

![The moss garden from its gate, the name on a small board beside a pair of shoes](banner.png)

![Animated garden in three bands: canopy light, uncurling ferns and brightening mushroom caps, and one falling drop](scene.svg)

# acra-SecretsScanner
A command-line tool that scans source code files for exposed secrets like API keys, passwords, and private keys.  Uses regular expressions to identify potential secrets, and reports a Shannon entropy value (bits per character) for each found value. Found values are masked in every report, console and file: the report shows the key name, line, length of the mask, and entropy, never the value itself.

## Install
`git clone https://github.com/ShadowStrikeHQ/acra-secretsscanner`

![Raindrop line divider, a long leaf with drops at its tip](sep-heavy.svg)

## Usage
`./acra-secretsscanner [params]`

![Raindrop line divider](sep-light.svg)

## Parameters
- `-h`: Show help message and exit
- `-o`: Path to the file to save the scan results.

![Raindrop line divider](sep-light.svg)


> Loose stone at the garden edge: The Value Itself Never Appears. Every report, console and file, shows the key name, the line, the length of the mask, and the entropy, and the found value stays masked.
>
> Loose stone, the honest limits: the README documents no scan target argument and no sample output, so neither appears here.

## License
Copyright (c) ShadowStrikeHQ
