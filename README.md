# Biting the Apple: Unlocking macOS with Python

This is a presentation I prepared for [hsv.py](https://www.meetup.com/hsv-py/) meetup.

## Building the Presentation

The presentating is built using [marp](https://marp.app/).

To install marp (assumes you are using homebrew):

First install node:

```bash
brew install node
```

Then you can run marp via [npx](https://docs.npmjs.com/cli/v8/commands/npx). I create an alias:

```bash
alias marp='npx @marp-team/marp-cli@latest'
```

After installing marp, you can build the presentation with the following command:

```bash
rm -f biting-the-apple.html && marp biting-the-apple.md --html --allow-local-files
```

## View this presentation online

View online [here](https://rhettbull.github.io/biting-the-apple/).

## License

This presentation is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

All code examples are licensed under the [MIT License](https://opensource.org/licenses/MIT).
