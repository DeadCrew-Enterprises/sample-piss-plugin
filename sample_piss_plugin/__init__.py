"""A sample PISS plugin, installed from this repository: it gives each item its length in words,
through the humanize library, and the keyword ``from-git``."""

from datetime import timedelta

import humanize
from piss_plugin import Context, Contribution, Draft, Plugin, import_feature


class GitSample(Plugin):
    id = "git-sample"
    name = "Sample from git"

    @import_feature("length", "Each item's length, in words")
    def length(self, cx: Context, draft: Draft) -> Contribution:
        made = Contribution(keywords=["from-git"])
        if draft.duration_seconds:
            made.set("length", humanize.naturaldelta(timedelta(seconds=draft.duration_seconds)))
        made.set("words", float(len(draft.title.split())))
        return made
