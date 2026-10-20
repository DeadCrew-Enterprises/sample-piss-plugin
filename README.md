# sample-piss-plugin

A sample plugin for [PISS](https://github.com/crioux/piss), installed from this repository's URL.
Its import feature `git-sample.length` gives each item:

- `git-sample.length`: how long a video or recording is, in words ("2 minutes"), by
  [humanize](https://pypi.org/project/humanize/);
- `git-sample.words`: how many words its title has;
- the keyword `from-git`.

Install it on a site as an admin:

```
piss python install https://github.com/crioux/sample-piss-plugin.git
```

then turn it on in the Plugins panel. PISS installs `humanize` into the plugin's own folder and
bundles both for import pods.
