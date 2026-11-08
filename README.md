![Intro scenery: a heavy black marker drawing one firm redaction bar across a single line of a cream document on a walnut desk under a green banker's lamp, the rest of the page open around it and a red wax seal waiting at the desk edge](intro-banner.png)

# acra-SecretsScanner

![Wordmark banner: a walnut desk under a pooled lamp with a tall stack of searched documents on one side, the top page carrying neat black redaction bars, and a shorter stack of finished reports tied and sealed in red wax on the other side](banner.png)

<p align="center"><img src="logo.png" alt="acra-secretsscanner logo: a cream document photographed from directly above on a walnut desk, three thick black redaction bars laid across its middle lines and a heavy black marker lettered Sharpie resting beside it, with one red wax seal at the page corner; the print outside the bars is blurred beyond reading" width="200"></p>

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
